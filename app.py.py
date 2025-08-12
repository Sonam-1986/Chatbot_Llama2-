import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from contextlib import nullcontext

# -------------------------
# CONFIG
# -------------------------
MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"
HF_TOKEN = os.getenv("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")
MAX_TOKENS = 150
TEMPERATURE = 0.7
TOP_P = 0.9
USE_8BIT =  False

# -------------------------
# FLASK SETUP
# -------------------------
app = Flask(__name__, static_folder=".")
CORS(app)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/health")
def health():
    return jsonify({"ok": True})

# -------------------------
# MODEL LOADING
# -------------------------
print("Checking GPU...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

load_kwargs = {}
if USE_8BIT:
    load_kwargs = {"load_in_8bit": True, "device_map": "auto"}
elif device.type == "cuda":
    load_kwargs = {"torch_dtype": torch.float16, "device_map": "auto"}

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True, token=HF_TOKEN)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, token=HF_TOKEN, **load_kwargs)
if not any(p.device.type == "cuda" for p in model.parameters()) and device.type == "cuda":
    model.to(device)

torch.backends.cudnn.benchmark = True

# -------------------------
# CHAT ENDPOINT
# -------------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_input = data.get("message", "").strip()
    if not user_input:
        return jsonify({"response": "Please type something."})

    prompt = f"<s>[INST] {user_input} [/INST]"

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    use_autocast = (model.device.type == "cuda" and next(model.parameters()).dtype == torch.float16)
    ctx = torch.autocast(device_type="cuda", dtype=torch.float16) if use_autocast else nullcontext()

    with torch.no_grad():
        with ctx:
            output_ids = model.generate(
                **inputs,
                max_new_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                top_p=TOP_P,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                repetition_penalty=1.05,
            )

    full_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # ✅ FIX: Remove instruction part from reply
    if "[/INST]" in full_text:
        reply = full_text.split("[/INST]", 1)[-1].strip()
    else:
        reply = full_text.replace(prompt, "").strip()

    if not reply:
        reply = "I couldn't make a good reply. Try again."

    return jsonify({"response": reply})

# -------------------------
# RUN
# -------------------------
from pyngrok import ngrok

public_url = ngrok.connect(5000)
print("Public URL:", public_url)

app.run(host="0.0.0.0", port=5000)

# Chatbot_Llama2-

# 🦙💬 LLaMA LangChain Chatbot-
A conversational AI powered by Meta’s LLaMA and the LangChain framework


# 🤖 LLaMA-Powered Flask Chatbot

A simple yet powerful chatbot built with Meta’s LLaMA-2, Hugging Face Transformers, and Flask, featuring a neon-styled responsive chat UI.


# 📖 Overview

This project serves a Meta LLaMA-2 model via a Flask backend and provides a sleek HTML/CSS/JavaScript front-end for chatting in real time. It uses ngrok for public URL tunneling, enabling you to share your chatbot instantly without complex hosting.

# ✨ Features

1. LLaMA-2 model integration via Hugging Face transformers

2. Real-time text generation with configurable sampling parameters

3. Flask API backend with /chat endpoint

4. Neon cyberpunk UI styled with CSS

5. CORS enabled for cross-origin requests

6. Public access via ngrok tunnel

# 🛠️ Tech Stack

   | Component         | Technology Used                                                   |
| ----------------- | ----------------------------------------------------------------- |
| Language Model    | [Meta LLaMA-2-7B-Chat](https://ai.meta.com/llama/) (Hugging Face) |
| Backend Framework | Flask                                                             |
| Frontend          | HTML, CSS, JavaScript                                             |
| Styling           | Custom neon UI (CSS)                                              |
| Model Inference   | Hugging Face Transformers + PyTorch                               |
| Public Tunneling  | pyngrok                                                           |
| Environment Mgmt  | Python 3.9+                                                       |

# 📚 How It Works -

1. Frontend (index.html)

 - Captures user input and sends it to /chat via fetch() POST request.

 - Displays messages with glowing cyberpunk styling.

2. Backend (app.py) 

 - Loads the LLaMA-2 tokenizer and model from Hugging Face.

 - Runs inference with configurable temperature, top_p, and max_new_tokens.

 - Returns the model’s reply as JSON.

3. ngrok

 - Exposes the local Flask server to the internet for easy sharing.

# 📜 Roadmap

 1. Add conversation history memory

 2. Deploy on cloud platforms (Render, Hugging Face Spaces, etc.)

3.  Add LangChain for tool use and retrieval-augmented generation

# INSTALLATION AND REQUIREMENT


# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2️⃣ Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Add your Hugging Face token in the .env file
HF_TOKEN=your_huggingface_token_here

# 5️⃣ Run Flask app
python app.py

# 6️⃣ (Optional) Start ngrok tunnel
ngrok http 5000







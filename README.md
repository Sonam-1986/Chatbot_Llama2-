# 🦙💬 Chatbot_LLaMA2  
**A Neon-Styled Conversational AI powered by Meta’s LLaMA-2 & Flask**

A powerful, real-time chatbot built using **Meta’s LLaMA-2** model, **Hugging Face Transformers**, and **Flask**, featuring a responsive **cyberpunk neon UI**. Easily accessible via **ngrok** for instant sharing without complex deployment.

---

## 📖 Overview
This project serves a **Meta LLaMA-2 model** through a Flask backend and provides an interactive **HTML/CSS/JavaScript** frontend for real-time chatting.  
It supports **public sharing** via `ngrok` so anyone can talk to your chatbot instantly.  

---

## ✨ Features
- ⚡ **LLaMA-2 Integration** via Hugging Face Transformers  
- 💬 Real-time text generation with **customizable parameters** (temperature, top_p, max tokens)  
- 🖥️ Sleek **Neon Cyberpunk UI** (HTML/CSS/JS)  
- 🔗 **Flask API** with `/chat` endpoint  
- 🌐 **CORS enabled** for smooth frontend-backend communication  
- 🌍 **Public access** with ngrok tunnel  

---

## 🛠️ Tech Stack
| Component          | Technology Used |
|--------------------|-----------------|
| **Language Model** | Meta LLaMA-2-7B-Chat (Hugging Face) |
| **Backend**        | Flask |
| **Frontend**       | HTML, CSS, JavaScript |
| **Styling**        | Custom Neon UI (CSS) |
| **Inference**      | Hugging Face Transformers + PyTorch |
| **Public Access**  | pyngrok |
| **Environment**    | Python 3.9+ |

---

## 📚 How It Works
### **Frontend (`index.html`)**
- Captures user messages & sends them to the Flask `/chat` endpoint using `fetch()`  
- Displays chat messages with glowing cyberpunk animations  

### **Backend (`app.py`)**
- Loads LLaMA-2 tokenizer & model from Hugging Face  
- Runs inference with user-defined parameters (temperature, top_p, max_new_tokens)  
- Sends back the chatbot’s reply as JSON  

### **Ngrok**
- Creates a **public URL** for your local server  
- Lets you share the chatbot instantly without deploying to the cloud  

---

## ⚙️ Installation & Setup

```bash
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

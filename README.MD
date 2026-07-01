# 🤖 Guided AI Chatbot

A web-based AI chatbot built with **Python**, **FastAPI**, **HTML**, **CSS**, and **JavaScript**. The chatbot demonstrates the concepts of **Personal System Prompt** and **Conversation Memory**, allowing users to have guided and context-aware conversations with an AI assistant.

---

## 🚀 Features

- 💬 Interactive AI Chat Interface
- 🧠 Personal System Prompt
- 📝 Conversation Memory
- ⚡ FastAPI Backend
- 🌐 Responsive Web UI
- 🔐 Environment Variable Support (.env)
- 📂 Modular Project Structure
- 🎯 Beginner-Friendly Codebase

---

## 📁 Project Structure

```
guided-ai-chatbot/
│── static/
│   ├── style.css
│   └── script.js
│
│── templates/
│   └── index.html
│
│── app.py
│── chatbot.py
│── memory.py
│── prompts.py
│── requirements.txt
│── .env
│── README.md
│── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3.13+
- FastAPI
- HTML5
- CSS3
- JavaScript
- Jinja2
- python-dotenv
- OpenAI API *(or Gemini API if configured)*

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Ronit049/Guided-AI-Chatbot.git

cd guided-ai-chatbot
```

---

### Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Create a `.env` File

```env
OPENAI_API_KEY=your_api_key_here
```

> **Note:** Never upload your `.env` file to GitHub.

---

## ▶️ Run the Application

```bash
python -m uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 📷 Preview

```
+----------------------------------------+
|        Guided AI Chatbot               |
|----------------------------------------|
| You: Hello                            |
| AI : Hi! How can I help you today?    |
|                                        |
|                                        |
|________________________________________|
| Type your message...       [Send]      |
+----------------------------------------+
```

---

## 🧠 How It Works

### Personal System Prompt

The chatbot follows a predefined system prompt stored in `prompts.py`. This defines the chatbot's personality and response style.

Example:

```python
SYSTEM_PROMPT = """
You are Guided AI.

- Be helpful.
- Explain concepts simply.
- Give examples.
- Remember previous messages.
"""
```

---

### Conversation Memory

The chatbot stores the conversation during the session using the `ConversationMemory` class.

Example:

```python
memory.add("user", message)
memory.add("assistant", response)
```

This enables context-aware conversations.

---

## 📦 Dependencies

```
fastapi
uvicorn
jinja2
python-dotenv
openai
```

---

## 🔒 Security

- Store API keys in `.env`
- Never commit secrets to GitHub
- Add `.env` to `.gitignore`

Example:

```
.env
__pycache__/
*.pyc
.venv/
```

---

## 🚀 Future Improvements

- User Authentication
- Persistent Chat History
- SQLite Database
- Dark Mode
- Streaming AI Responses
- Markdown Support
- Multiple Chat Sessions
- File Upload Support
- Voice Input & Output
- Tool Calling
- RAG (Retrieval-Augmented Generation)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ronit Raj**

- GitHub: https://github.com/Ronit049
- LinkedIn: https://www.linkedin.com/in/ronitraj49

---

⭐ If you found this project useful, don't forget to **Star** the repository!
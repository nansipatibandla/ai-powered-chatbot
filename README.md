# 🤖 AI-Powered Chatbot

An intelligent chatbot built with Python and Flask that uses Natural Language Processing (NLP) to answer customer support FAQs.

## 🚀 Features
- Natural Language Processing using NLTK
- Intent-based response system
- Conversation logging with SQLite database
- Clean and responsive chat UI
- REST API endpoints

## 🛠️ Technologies Used
- Python
- Flask
- NLTK (Natural Language Toolkit)
- SQLite
- HTML, CSS, JavaScript

## 📁 Project Structure# ai-powered-chatbot
ai-powered-chatbot/
├── app.py          # Flask application
├── chatbot.py      # NLP logic
├── database.py     # SQLite logging
├── intents.json    # Training data
├── templates/
│   └── index.html  # Chat UI
├── static/
│   └── style.css   # Styling
└── requirements.txt
## ⚙️ Installation & Setup
```bash
# Clone the repository
git clone https://github.com/nansipatibandla/ai-powered-chatbot.git
cd ai-powered-chatbot

# Install dependencies
pip install flask nltk

# Run the application
python app.py
💻 Usage
Open browser and go to http://127.0.0.1:5000
Type any message in the chat box
The chatbot will respond based on trained intents
View conversation logs at http://127.0.0.1:5000/logs
📌 Sample Questions to Ask
"Hello"
"What services do you offer?"
"How can I contact you?"
"What are your working hours?"
"Thank you"
🔗 API Endpoints
Endpoint Method description
/       GET    Chat UI
/chat    POST    Get bot response
/logs    GET     View all conversations
👩‍💻 Developer
Nancy Patibandla
GitHub: @nansipatibandla

from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from database import init_db, log_conversation, get_all_logs

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    if not user_message:
        return jsonify({'response': 'Please type a message.'})
    bot_response = get_response(user_message)
    log_conversation(user_message, bot_response)
    return jsonify({'response': bot_response})

@app.route('/logs')
def logs():
    all_logs = get_all_logs()
    return jsonify([{'id': row[0], 'user': row[1], 'bot': row[2], 'time': row[3]} for row in all_logs])

if __name__ == '__main__':
    app.run(debug=True)

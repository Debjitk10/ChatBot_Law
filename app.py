from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_Chat_response(text):
    api_url = "https://api.example.com/chatbot"
    api_key = "your-api-key-1234567890"

    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"message": text}

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        chatbot_response = response.json().get("response")
        print("Chatbot response:", chatbot_response)
        return chatbot_response
    else:
        print("Error:", response.text)
        return "Error"

@app.route("/")
def index():
    return render_template('chatbot.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    response = get_Chat_response(msg)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run()

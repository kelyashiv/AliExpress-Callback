import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/callback")
def callback():
    auth_code = request.args.get("code")
    return f"Received Authorization Code: {auth_code}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # שימוש ב-PROD PORT
    app.run(host="0.0.0.0", port=port)

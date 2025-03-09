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
    import os
port = int(os.environ.get("PORT", 10000))  # אם PORT לא קיים, השתמש ב-10000
app.run(host="0.0.0.0", port=port)


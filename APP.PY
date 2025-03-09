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
    app.run(host="0.0.0.0", port=10000)

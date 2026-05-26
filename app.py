# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Deploy de produção funcionando!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

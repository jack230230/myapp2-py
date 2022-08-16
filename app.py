import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return "ok"

@app.route("/env")
def env():
    return os.environ["ENV_NAME"]

if __name__ == "__main__":
    app.run(debug=True)
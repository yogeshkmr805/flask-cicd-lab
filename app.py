import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
APP_VERSION = os.environ.get("APP_VERSION", "dev")


@app.route("/")
def home():
    return render_template("index.html", version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok", version=APP_VERSION)


@app.route("/api/greet")
def greet():
    name = request.args.get("name", "").strip()
    if not name:
        return jsonify(error="name is required"), 400
    return jsonify(message=f"Hello, {name}!")


@app.route("/api/add")
def add():
    try:
        a = int(request.args.get("a", ""))
        b = int(request.args.get("b", ""))
    except ValueError:
        return jsonify(error="a and b must be integers"), 400
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

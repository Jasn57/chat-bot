from flask import request, jsonify, render_template
from . import app, client

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    return jsonify({"reply": response.output_text})

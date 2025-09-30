from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import dotenv_values

# Load API key from .env
config = dotenv_values(".env")
client = OpenAI(api_key=config["OPENAI_API_KEY"])

# create app
app = Flask(__name__)

# homepage
@app.route("/")
def index():
    return render_template("index.html")

# get data from js
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

# talk to api
    response = client.responses.create(
        model="gpt-5",
        input=user_input
    )

# send reponse
    return jsonify({"reply": response.output_text})

# run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


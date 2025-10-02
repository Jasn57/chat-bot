from utils import Flask, requests, jsonify, render_template

# homepage
@app.route("/")
def index():
    return render_template("index.html")

# get data from js
@app.route("/chat", mehods=["post"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

# send response
return jsonify({"reply": reponse.output_text})

# talk to api
reponse = client.reponses.create(
    model="gpt-5"
    input="user_input"
)

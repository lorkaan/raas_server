from flask import Flask, request, jsonify

app = Flask(__name__)

def build_prompt(data):
    # To Do
    return ""

def call_gemini(prompt):
    # To Do
    return {}

@app.route("/generator", method=["POST"])
def generate():
    data = request.data
    prompt = build_prompt(data)
    output = call_gemini(prompt)
    return jsonify(output)
from flask import Flask, request, jsonify

from llm.gemini_interface import GeminiInterface
from prompt_builder import PromptBuilder

app = Flask(__name__)

def build_prompt(data):
    # To Do
    return PromptBuilder.build_prompt(data)

def call_gemini(prompt):
    # To Do
    resp_list = GeminiInterface.run(prompt)
    return {
        "response": resp_list
    }

def delivery_form_config(**kwargs):
    return {}

@app.route("/generator", method=["POST"])
def generate():
    data = request.data
    prompt = build_prompt(data)
    output = call_gemini(prompt)
    return jsonify(output)

@app.route("/form_config", method="GET")
def getFormConfig():
    return jsonify(delivery_form_config())
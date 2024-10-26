from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Default index endpoint
@app.route('/')
def index():
    return "Welcome to the Flask App!"

# A simple endpoint to echo back the data sent
@app.route('/get/', methods=['GET'])
def respond():
    user_input_text = request.args.get("data", None)
    if user_input_text:
        return jsonify({"response": user_input_text})
    else:
        return jsonify({"error": "No data provided"}), 400

if __name__ == '__main__':
    # Run the app on the specified port
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

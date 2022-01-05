from tensorflow.keras.models import load_model
from flask import Flask, json, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)
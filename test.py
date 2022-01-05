from tensorflow.keras.models import load_model
model = load_model("lotto.h5")
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)

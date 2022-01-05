from tensorflow.keras.models import load_model
from flask import Flask, json, jsonify
import tensorflow
model = load_model("lotto.h5")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(tensorflow.__version__)

if __name__ == '__main__':
    app.run(debug=True)
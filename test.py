from tensorflow.keras.models import load_model
from flask import Flask, jsonify
import numpy as np
def onehot(number):
    returnarray = []
    for i in range(len(number)):
        b = np.zeros(47)
        for k in range(6):
            b[number[i][k]] = 1
        returnarray.append(b)
    return returnarray

model = load_model("lotto.h5")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)

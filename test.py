from tensorflow.keras.models import load_model
from flask import Flask, jsonify
import numpy as np
import requests
def find_number(numbers):
    find_numbers = []
    numbers = list(numbers[0])
    for i in range(6):
        tmp = max(numbers)
        index = numbers.index(tmp)
        if(index==0):
            numbers[index] = -99
            a = numbers.index(max(numbers))
            find_numbers.append(a)
            continue
        numbers[index] = -99
        find_numbers.append(index)
    find_numbers.sort()
    return find_numbers
def onehot(number):
    returnarray = []
    for i in range(len(number)):
        b = np.zeros(47)
        for k in range(6):
            b[number[i][k]] = 1
        returnarray.append(b)
    return returnarray


def test_lottonumber_load(number):
    lotto_numbers = []
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(number)
    req_result = requests.get(url)
    small_lotto_numbers = [] 
    for i in range(6):
            small_lotto_numbers.append(req_result.json()['drwtNo'+str(i+1)])
    lotto_numbers.append(small_lotto_numbers)
    
    return lotto_numbers 

model = load_model("lotto.h5")
test = onehot(test_lottonumber_load(995))
test = np.array(test)
predict=model.predict(test)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)

import numpy as np 
import requests

repeat = 444
test_number = 995


def test_lottonumber_load(number):
    lotto_numbers = []
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(number)
    req_result = requests.get(url)
    small_lotto_numbers = [] 
    for i in range(6):
            small_lotto_numbers.append(req_result.json()['drwtNo'+str(i+1)])
    lotto_numbers.append(small_lotto_numbers)
    
    return lotto_numbers 

def lottonumber_load(number):
    lotto_numbers = []
    for i in range(number):
        url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(i+1)
        req_result = requests.get(url)
        small_lotto_numbers = [] 
        for i in range(6):
            small_lotto_numbers.append(req_result.json()['drwtNo'+str(i+1)])
        lotto_numbers.append(small_lotto_numbers)
    return lotto_numbers 

def onehot(number):
    returnarray = []
    for i in range(len(number)):
        b = np.zeros(47)
        for k in range(6):
            b[number[i][k]] = 1
        returnarray.append(b)
    return returnarray

def onehotdecode(onehotlist):
    find_list = []
    for i in range(len(onehotlist)):
        a = np.where(1==onehotlist[i])[0]
        find_list.append(a)
    return find_list

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

# data = lottonumber_load(repeat)
# data = onehot(data)
# train = np.array(data[:repeat//2])
# target = np.array(data[repeat//2:])

# from tensorflow.keras.layers import LSTM
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
# model = Sequential()
# model.add(Dense(777,input_shape=(train.shape)))    #LSTM need timesteps
# model.add(Dense(47))
# model.compile(loss='mean_squared_error',optimizer='adam')
# model.fit(train,target,epochs=77,batch_size=77)

# model.save('lotto.h5')
model = load_model('lotto.h5')
test = onehot(test_lottonumber_load(test_number))
test = np.array(test)
predict=model.predict(test)

#print('\nanswer:',test_lottonumber_load(test_number+1)[0])
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)

from numpy.core.fromnumeric import repeat
import numpy as np 
import requests

repeat = 4

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
        numbers[index] = -99
        find_numbers.append(index)
    find_numbers.sort()
    return find_numbers

data = lottonumber_load(repeat)
data = onehot(data)
train = np.array(data[:repeat//2])
target = np.array(data[repeat//2:])

from tensorflow.keras.layers import LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()
model.add(Dense(128,input_shape=(train.shape)))    #LSTM need timesteps
model.add(Dense(47))
model.compile(loss='mean_squared_error',optimizer='adam')
model.fit(train,target,epochs=1,batch_size=30)

test = onehot(test_lottonumber_load(5))
test = np.array(test)
predict=model.predict(test)
print(find_number(predict))

print('\nanswer',test_lottonumber_load(5))
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense
# model = Sequential()
# train = [1,2,3]
# target = [4,5,6]
# model.add(Dense(1))
# model.add(Dense(1))
# model.compile(loss='mean_squared_error',optimizer='adam')
# model.fit(train,target,epochs=10)
# model.save("linear.h5")
model = load_model("linear.h5")
predict = model.predict([4,5,6])
predict_array = []
for i in range(3):
    predict_array.append(int(predict[i][0]))
from flask import Flask, json, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(array=predict_array)

if __name__ == '__main__':
    app.run(debug=True)
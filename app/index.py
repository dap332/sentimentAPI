from flask import Flask, jsonify, request
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

import pickle

app = Flask('_name_')


# load the tokenizer and the model
global tokenizer
with open("keras_tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)

global model
model = load_model("yelp_model.h5")
model._make_predict_function()
def predict_sentiment(texts):
    print(texts[0])
    sequences = tokenizer.texts_to_sequences(texts)
    data = pad_sequences(sequences, maxlen=300)

    # get predictions for each of your new texts
    predictions = model.predict(data)
    return predictions


@app.route('/')
def hello_world():
    return 'Hello World!!!'


@app.route('/predict', methods=['POST'])
def predict():
    req_data = request.get_json()
    return jsonify(predict_sentiment(req_data['texts']).tolist())


app.run()

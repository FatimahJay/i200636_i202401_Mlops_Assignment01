from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Welcome to the Iris Flower Prediction API!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)

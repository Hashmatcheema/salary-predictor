from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Salary Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the pre-trained model
        model = joblib.load("salary_model.pkl")

        # Get JSON data from request
        data = request.get_json()
        experience = float(data["YearsExperience"])  # Convert to float

        # Reshape for prediction
        prediction = model.predict([[experience]])[0]

        return jsonify({"predicted_salary": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
from flask import Flask, request, jsonify
import pandas as pd
import joblib  # For saving and loading the model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load and preprocess data
data = pd.read_csv('salary_data.csv')
X = data[['YearsExperience']]  # Using double brackets to keep it a DataFrame
y = data['Salary']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'salary_model.pkl')

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# Initialize Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Salary Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load the model
        model = joblib.load("salary_model.pkl")

        # Get JSON data from request
        data = request.get_json()
        experience = float(data["YearsExperience"])  # Convert to float

        # Make a prediction
        prediction = model.predict([[experience]])[0]

        return jsonify({"predicted_salary": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

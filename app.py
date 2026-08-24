from flask import Flask, request, jsonify, send_file
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("linear_regression_model.pkl")


@app.route("/")
def home():
    return send_file("index.html")


@app.route("/style.css")
def style():
    return send_file("style.css")


@app.route("/script.js")
def script():
    return send_file("script.js")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    temperature = float(data["Temperature_C"])

    prediction = model.predict([[temperature]])

    return jsonify({
        "Temperature_C": temperature,
        "Predicted_IceCream_Sales": float(prediction[0])
    })


if __name__ == "__main__":
    app.run(debug=True)
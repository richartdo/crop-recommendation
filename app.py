import pickle
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load trained objects
with open("models/best_model_xgboost.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.route("/")
def home():
    return {"message": "Crop Recommendation API is running 🚀"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Expected input: dict with N, P, K, temperature, humidity, ph, rainfall
        features = [
            data["N"],
            data["P"],
            data["K"],
            data["temperature"],
            data["humidity"],
            data["ph"],
            data["rainfall"],
        ]

        # Scale input
        scaled_features = scaler.transform([features])

        # Predict crop
        prediction = model.predict(scaled_features)[0]
        crop_name = label_encoder.inverse_transform([prediction])[0]

        return jsonify({"recommended_crop": crop_name})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

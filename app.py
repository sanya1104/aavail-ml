
from flask import Flask, request, jsonify
from model import load_model, predict
from logging_config import setup_logging

app = Flask(__name__)
setup_logging()
model = load_model("model.pkl")

@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.get_json()
    target_date = data.get("target_date")
    country = data.get("country")
    if not target_date or not country:
        return jsonify({"error": "target_date and country are required"}), 400
    result = predict(model, target_date, country)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)


import pickle

def load_model(path):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model

def predict(model, target_date, country):
    return {"target_date": target_date, "country": country, "revenue_forecast": 1000}

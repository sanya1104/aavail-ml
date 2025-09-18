
import pickle
dummy_model = {"dummy": True}
with open("model.pkl", "wb") as f:
    pickle.dump(dummy_model, f)
print("Dummy model created as model.pkl")

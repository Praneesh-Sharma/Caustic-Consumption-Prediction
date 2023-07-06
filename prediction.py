import joblib
import pickle

# def predict(data):
#     clf = joblib.load("rf_model.sav")
#     return clf.predict(data)

def predict(data):
    with open("consump_pred_v2.pkl", 'rb') as f:
      clf = pickle.load(f)
    return clf.predict(data)

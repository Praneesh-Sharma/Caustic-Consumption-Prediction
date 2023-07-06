import joblib
import pickle
def predict(data):
    clf = joblib.load("rf_model.sav")
    return clf.predict(data)

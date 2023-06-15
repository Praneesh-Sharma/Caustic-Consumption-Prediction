import joblib


def predict(data):
    clf = joblib.load("consump_pred.pkl")
    return clf.predict(data)

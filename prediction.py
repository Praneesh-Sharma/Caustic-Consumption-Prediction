import joblib

def predict(data):
    clf = joblib.load("rf_model.sav")
    return clf.predict(data)

def predicts(data):
    clf = joblib.load("rf_model_v2.sav")
    return clf.predict(data)

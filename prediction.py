import pickle


def predict(data):
    clf = pickle.load("consump_pred.pkl")
    return clf.predict(data)

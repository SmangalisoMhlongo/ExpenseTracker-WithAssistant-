import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "expense_classifier.pkl")

#training the text based classifier to identify the different categories
def train_model():
    
    DATA_PATH = os.path.join(BASE_DIR, "data", "training_data.csv")
    df = pd.read_csv(DATA_PATH)

    X_text = df["description"]
    y = df["category"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X_text)

    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump((model, vectorizer), MODEL_PATH)
    print("Model trained and saved.")

#predicting a category with the model
def predict_category(description):
   
    model, vectorizer = joblib.load(MODEL_PATH)
    X = vectorizer.transform([description])
    prediction = model.predict(X)

    return prediction[0]

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Check if model already exists
if not os.path.exists('spam_model.pkl') or not os.path.exists('vectorizer.pkl'):
    # Load dataset
    df = pd.read_csv('emails.csv')

    # Features and labels
    X = df['text']
    y = df['label']

    # Text vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    X_vect = vectorizer.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

    # Train model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Save model and vectorizer
    joblib.dump(model, 'spam_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    print(f"✅ Model trained! Accuracy: {model.score(X_test, y_test) * 100:.2f}%")

# Prediction function
def predict_email(email_text):
    model = joblib.load('spam_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    vect_email = vectorizer.transform([email_text])
    return model.predict(vect_email)[0]

# Console interface
while True:
    user_input = input("\n📨 Enter email content (or type 'exit' to quit):\n> ")
    if user_input.lower() == 'exit':
        break
    result = predict_email(user_input)
    print(f"🔎 This email is likely: {result.upper()}")

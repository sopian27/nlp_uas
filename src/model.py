# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from src.preprocessing import clean_text  # pastikan path ini sesuai

def train_model():
    # Load data
    df = pd.read_csv('data/imdb_dataset.csv')
    df['review'] = df['review'].apply(clean_text)
    df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        df['review'], df['sentiment'], test_size=0.2, random_state=42
    )

    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Model
    model = LogisticRegression()
    model.fit(X_train_tfidf, y_train)
    y_pred = model.predict(X_test_tfidf)

    # ✅ Tambahkan semua variabel yang dibutuhkan ke return
    return model, vectorizer, X_test, y_test, y_pred

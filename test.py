from src.model import train_model

if __name__ == '__main__':
    print("Training model...")
    model, vectorizer, X_test, y_test, y_pred = train_model()
    print("Model selesai dilatih.")

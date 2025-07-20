import streamlit as st
import pickle
from src.preprocessing import clean_text
from src.model import train_model

st.title("🎬 Analisis Sentimen Ulasan Film")

# Load / latih model
@st.cache_resource
def load_model():
    model, vectorizer, _, _, _ = train_model()
    return model, vectorizer

model, vectorizer = load_model()

# Input user
user_input = st.text_area("Masukkan ulasan film:")

if st.button("Prediksi Sentimen"):
    if user_input.strip() == "":
        st.warning("Teks tidak boleh kosong.")
    else:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        label = "Positif" if prediction == 1 else "Negatif"
        st.success(f"Prediksi Sentimen: **{label}** 🎉")

## 🎮 Sentiment Analysis of Movie Reviews

Analisis sentimen terhadap ulasan film menggunakan model Machine Learning berbasis **TF-IDF + Logistic Regression**, dilatih pada dataset IMDB berbahasa Inggris.

---

### 🌐 Akses Aplikasi Online

🔗 [Klik di sini untuk mencoba aplikasi Streamlit](https://develop-bcdvavsovcpx3yjvpiz7au.streamlit.app/)

---

### 📁 Struktur Proyek

```
.
├── app/
│   ├── sentiment_app.py      # Aplikasi Streamlit
├── src/
│   ├── preprocessing.py      # Pembersihan dan normalisasi teks
│   ├── model.py              # Pelatihan dan evaluasi model
├── data/
│   └── imdb_dataset.csv      # Dataset IMDB
├── notebook/
│   └── evaluation.ipynb      # Evaluasi model dengan metrik
├── README.md
```

---

### 📊 Deskripsi Proyek

Proyek ini bertujuan untuk:
- Mengklasifikasikan ulasan film sebagai **positif** atau **negatif**
- Menggunakan pendekatan NLP: **TF-IDF + Logistic Regression**
- Disediakan antarmuka pengguna melalui **Streamlit Web App**

---

### 📌 Fitur Aplikasi
- Input ulasan film secara langsung
- Prediksi sentimen (positif / negatif)
- Contoh ulasan tersedia
- Prediksi ditampilkan secara interaktif

---

### 🛠️ Teknologi yang Digunakan

- Python 3.x
- Pandas, Scikit-learn, NLTK
- Streamlit
- TF-IDF Vectorizer
- Logistic Regression

---

### 📈 Evaluasi Model

- **Akurasi**: 88.38%
- **Precision**: 0.87–0.90
- **Recall**: 0.87–0.90
- **F1-Score**: 0.88–0.89

Evaluasi dilakukan menggunakan 20% data test dari dataset IMDB.

---

### 🌤️ Bahasa yang Didukung

✅ **Bahasa Inggris**  
Model dilatih menggunakan dataset **IMDB Movie Reviews** yang berbahasa Inggris. Oleh karena itu:

⚠️ **Ulasan dalam Bahasa Indonesia mungkin tidak dikenali dengan baik.**

#### 💡 Saran:
Gunakan **terjemahan ke Bahasa Inggris** sebelum menguji ulasan dalam Bahasa Indonesia.

---

### 🧪 Contoh Input

#### Positif
> *"This movie was fantastic! I loved every minute of it."*

#### Negatif
> *"The plot was boring and the acting was terrible."*

---

### 🚀 Menjalankan Secara Lokal

#### 1. Clone repo dan install dependensi
```bash
pip install -r requirements.txt
```

#### 2. Jalankan aplikasi
```bash
streamlit run sentiment_app.py
```

---

### 📚 Dataset
Dataset diambil dari:

> [IMDb Movie Reviews Dataset (Kaggle)](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

---

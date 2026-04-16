# 🩺 Diabetes Prediction using Machine Learning

## 📌 Project Overview

Proyek ini bertujuan untuk membangun model *machine learning classification* untuk memprediksi apakah seseorang berpotensi menderita diabetes berdasarkan data kesehatan.

Model dikembangkan melalui tahapan lengkap *data science pipeline*, mulai dari data preprocessing, exploratory data analysis (EDA), modeling, evaluation, hingga deployment menggunakan Streamlit.

---

## 📊 Dataset

Dataset yang digunakan merupakan dataset diabetes dengan total:

* 768 data
* 8 fitur + 1 target (Outcome)

### 🔹 Fitur:

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age

### 🎯 Target:

* `0` = Tidak Diabetes
* `1` = Diabetes

---

## ⚙️ Data Preprocessing

Beberapa langkah preprocessing yang dilakukan:

* Mengidentifikasi nilai tidak valid (nilai 0 pada beberapa fitur)
* Mengubah nilai 0 menjadi missing value (NaN)
* Melakukan imputasi menggunakan median
* Train-test split (80:20)
* Menghindari **data leakage** dengan preprocessing hanya pada data training

---

## 📈 Exploratory Data Analysis (EDA)

* Analisis distribusi data
* Visualisasi hubungan antar fitur
* Correlation heatmap
* Identifikasi fitur penting seperti:

  * Glucose
  * BMI
  * Age

---

## 🤖 Modeling

Beberapa algoritma yang digunakan:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)

---

## 📊 Model Evaluation

Evaluasi dilakukan menggunakan:

* Accuracy
* Confusion Matrix
* Precision
* Recall
* F1-Score

### ⚠️ Fokus utama:

Recall pada kelas diabetes (1), untuk meminimalkan **False Negative**

---

## 🏆 Best Model

Model terbaik yang diperoleh adalah:

👉 **Decision Tree (tanpa tuning)**

### Alasan:

* Recall tertinggi pada kelas diabetes (~73%)
* False Negative paling rendah
* Lebih optimal dibanding model lain

---

## 🔧 Hyperparameter Tuning

Dilakukan menggunakan:

* GridSearchCV
* Cross-validation (cv=5)
* Scoring: Recall

Namun, hasil tuning tidak meningkatkan performa model secara signifikan.

---

## 🚀 Deployment

Model di-deploy menggunakan **Streamlit** sehingga dapat digunakan secara interaktif.

### Cara Menjalankan Aplikasi:

```bash
streamlit run app.py
```

---

## 🖥️ Demo Aplikasi

Aplikasi memungkinkan pengguna:

* Menginput data kesehatan
* Mendapatkan prediksi diabetes secara langsung

---

## 📁 Project Structure

```bash
├── data/
│   └── diabetes.csv
├── notebook/
│   └── diabetes_analysis.ipynb
├── model/
│   └── model_diabetes.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## 🧠 Key Insights

* Glucose merupakan fitur paling berpengaruh terhadap diabetes
* Model dengan kompleksitas lebih tinggi tidak selalu memberikan performa terbaik
* Recall lebih penting dibanding accuracy dalam kasus medis

---

## 📌 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib & Seaborn
* Streamlit

---

## 🙌 Author

**Arif Ihsan Rayhandanis**

---

## ⭐ Notes

Proyek ini dibuat sebagai bagian dari pembelajaran Data Science dan dapat dikembangkan lebih lanjut dengan:

* Feature engineering
* Hyperparameter tuning lanjutan
* Model ensemble
* Deployment ke cloud

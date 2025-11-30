# ❤️ Heart Attack Prediction System Using Machine Learning & Streamlit
Live Demo App here: [Open App](https://heart-attack-risk-detection.streamlit.app/)

This project predicts the **risk of heart attack** using a machine learning model trained on medical attributes such as blood pressure, cholesterol, chest pain type, and more. The project includes a **Streamlit web app**, making it easy for anyone to input data and instantly view prediction results.

---

## 🚀 Features
- Predicts heart attack risk using a trained **KNN classifier**
- Simple and interactive **Streamlit UI**
- Scales input data using saved **scaler.pkl**
- Uses **columns.pkl** to ensure correct input order
- Real-time prediction output (Low Risk / High Risk)
- Clean project structure with dataset and notebook included

---

## 📁 Project Structure
``` bash 
.
├── app.py                   # Streamlit Application
├── KNN_heart.pkl            # Trained Machine Learning Model
├── scaler.pkl               # MinMax/Standard Scaler
├── columns.pkl              # Column order for model input
├── heart.csv                # Dataset used for training
├── HeartDisease.ipynb       # Jupyter Notebook (Model Training)
├── requirements.txt         # List of dependencies
└── README.md                # Project Documentation
```
---
## 🛠️ How to Run This Project
```
git clone https://github.com/ManjeshYdv/heart-attack-risk-detection.git
cd heart-attack-risk-detection
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 🧠 Model Used

#The model used in this project is:

- K-Nearest Neighbors (KNN Classifier)
- Trained on heart disease dataset
- Scaled using StandardScaler / MinMaxScaler
- Saved using Joblib
- Uses column ordering with columns.pkl

## ✨ Author
Manjesh Kumar Yadav 
Machine Learning & Python Developer

If anyone wants to improve this project, feel free to make changes, **add features, or enhance** it. Pull requests and suggestions are always welcome!  

---

## Prediction Output 
<img width="1366" height="1564" alt="screencapture-localhost-8501-2025-11-30-22_19_50" src="https://github.com/user-attachments/assets/a0801da0-2b2b-44ec-896a-93517a56d397" />



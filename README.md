 📰 Fake News Detection App

A simple and interactive web app to detect whether a news article is **real** or **fake**, built using **Python**, **Scikit-learn**, and **Streamlit**. Enter a headline or article text and get an instant prediction powered by machine learning.

🚀 Live Demo
👉 [Try the App on Streamlit] https://gxphig7qbvtx6a89k5fd8j.streamlit.app/

💡 Features
- 🔎 Detects **Fake** or **Real** news in real time
- 🧠 Built with a trained **machine learning model**
- 💬 Clean UI with **instant user input prediction**
- 🧪 Powered by `TfidfVectorizer` and `Logistic Regression`
- 🎯 Trained on real-world fake news data from Kaggle

🏗️ Project Structure
fake-news-detector/
├── app.py # Streamlit web app
├── fake_news_model.pkl # Trained ML model file
├── requirements.txt # Python dependencies
└── README.md # Project documentation


🧠 Model Details
Vectorizer: TfidfVectorizer
Classifier: Logistic Regression
Dataset: https://www.kaggle.com/code/therealsampat/fake-news-detection/input?select=True.csv
The model is trained to classify articles based on word patterns and content relevance using supervised learning.

📦 Dependencies
streamlit
scikit-learn
pandas
joblib
numpy

📚 Dataset Source
Fake and Real News Dataset from Kaggle
📌 View on Kaggle → https://www.kaggle.com/code/therealsampat/fake-news-detection/input?select=True.csv


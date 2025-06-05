import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detection App")
st.write("This app uses machine learning (Tfidf + PassiveAggressiveClassifier) to detect whether a news headline or article is **Fake** or **Real**.")

# Input box
news_input = st.text_area("📝 Enter News Text", height=200)

if st.button("Predict"):
    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        # Vectorize input and predict
        input_vec = vectorizer.transform([news_input])
        prediction = model.predict(input_vec)[0]

        if prediction == "fake":
            st.error("❌ This news is likely FAKE.")
        else:
            st.success("✅ This news is likely REAL.")

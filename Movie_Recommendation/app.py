import streamlit as st
import pandas as pd
import joblib

df = pd.read_pickle("movies.pkl")
similarity_matrix = joblib.load("similarity_matrix.pkl")

st.title("🎬 Movie Recommendation System")

movie = st.selectbox(
    "Select a movie",
    df["title"].values
)

if st.button("Recommend"):

    index = df[df["title"] == movie].index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    st.subheader("Recommended Movies")

    for i, score in similarity_scores[1:6]:
        st.write(df.iloc[i]["title"])
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from process_data import data_process


st.title("Similarity Cosnus")
data = pd.read_csv("data/data.csv")



# new_paper ="Efficient algorithms for large-scale machine learning."
new_paper =  st.text_input("Give the title of your documents")
new_paper_process = data_process(new_paper)

if st.button("new_paper"):
    data["title"] = data["title"].apply(data_process)
    vectorizer = TfidfVectorizer()
    vectorizer_data = vectorizer.fit_transform(data["title"])
    vectorizer_new_paper = vectorizer.transform([new_paper_process])
    similarity_papers = cosine_similarity(vectorizer_new_paper,vectorizer_data).flatten()
    indice_papers = similarity_papers.argsort()[:-6:-1]
    papers = data.iloc[indice_papers]
    st.write("Les papiers les plus similaires sont :")
    st.write(papers)


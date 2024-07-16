import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from process_data import data_process

data = pd.read_csv("data/data.csv")

data["title"] = data["title"].apply(data_process)

vectorizer = TfidfVectorizer()

vectorizer_data = vectorizer.fit_transform(data["title"])

new_paper = "Efficient algorithms for large-scale machine learning."
vectorizer_new_paper = vectorizer.transform({new_paper})

similarity_papers = cosine_similarity(vectorizer_data,vectorizer_new_paper).flatten()

indice_papers = similarity_papers.argsort()[:-5][::-1]

similarity_papers = data.iloc[indice_papers]

print("Les papiers les plus similaires sont :")
print(similarity_papers['title'])


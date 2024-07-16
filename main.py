import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from process_data import data_process

data = pd.read_csv("data/data.csv")

data["title"] = data["title"].apply(data_process)

vectorizer = TfidfVectorizer()

vectorizer_data = vectorizer.fit_transform(data["title"])

print(vectorizer_data)
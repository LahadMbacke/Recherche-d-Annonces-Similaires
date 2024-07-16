import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

data = pd.read_csv("data/data.csv")


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def data_process(text):
    text = text.lower()
    text = text.replace(r"\d+","")
    text = text.replace(r"\W+","")
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)


data["title"] = data["title"].apply(data_process)
print(data["title"])
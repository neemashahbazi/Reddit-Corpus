import os
import re
import string
import sys
import unicodedata

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

translator_2 = dict.fromkeys(i for i in range(sys.maxunicode)
                             if unicodedata.category(chr(i)).startswith('P'))


def text_lowercase(text):
    return text.lower()


def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result


def remove_whitespace(text):
    return " ".join(text.split())


def remove_punctuation(text):
    translator_1 = str.maketrans('', '', string.punctuation)
    return text.translate(translator_1).translate(translator_2)


corpus = []
for file in os.walk("data/NLP/ml_dataset"):
    text = ""
    for f in file[2]:
        document = open(file[0] + "/" + f, 'r', encoding='windows-1252')
        post = document.read()
        post = text_lowercase(post)
        post = remove_numbers(post)
        post = remove_punctuation(post)
        post = remove_whitespace(post)
        re.sub(' +', ' ', post)
        post += " "
        text += post
    if len(text) != 0:
        text.rstrip()
        corpus.append(text)
tfidf_vectorizer = TfidfVectorizer(use_idf=True)
tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(corpus)
first_vector_tfidfvectorizer = tfidf_vectorizer_vectors[1]
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(),
                  columns=["tfidf"])
df = df.sort_values(by=['tfidf'], ascending=False)
df.head(1000).to_csv('data/mlpa4001.csv')

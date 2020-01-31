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


authors = set()
with open("data/NLP/imdb62.txt", encoding='utf-8') as f:
    for line in f:
        author = line.split('\t')[1].strip()
        authors.add(author)

obj = {}

for author in authors:
    reviews = []
    with open("data//NLP/imdb62.txt", encoding='utf-8') as f:
        for line in f:
            if line.split('\t')[1].strip() == author:
                reviews.append(line.split('\t')[5].strip())
    obj.update({author: reviews})

corpus = []
for o in obj:
    text = ""
    for p in obj.get(o):
        post = p
        post = text_lowercase(post)
        post = remove_numbers(post)
        post = remove_punctuation(post)
        post = remove_whitespace(post)
        re.sub(' +', ' ', post)
        post += " "
        text += post
    text.rstrip()
    corpus.append(text)
tfidf_vectorizer = TfidfVectorizer(use_idf=True)
tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(corpus)
first_vector_tfidfvectorizer = tfidf_vectorizer_vectors[0]
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(),
                  columns=["tfidf"])
df = df.sort_values(by=['tfidf'], ascending=False)
df.head(1000).to_csv('data/imdb.csv')

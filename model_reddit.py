import json
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


# def remove_stopwords(text):
#     stop_words = set(stopwords.words("english"))
#     word_tokens = word_tokenize(text)
#     filtered_text = [word for word in word_tokens if word not in stop_words]
#     return detokenizer.detokenize(filtered_text)
#
#
# def stem_words(text):
#     word_tokens = word_tokenize(text)
#     stems = [stemmer.stem(word) for word in word_tokens]
#     return detokenizer.detokenize(stems)
#
#
# def lemmatize_word(text):
#     word_tokens = word_tokenize(text)
#     lemmas = [lemmatizer.lemmatize(word, pos='v') for word in word_tokens]
#     return detokenizer.detokenize(lemmas)


data_file = 'data/scraper/data.json'
with open(data_file, 'r') as file:
    data_content = file.read()
    data = json.loads(data_content)
    corpus = []
    for item in data['data']:
        text = ""
        for obj in item.get("posts"):
            post = obj.get("selftext")
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
    df.head(1000).to_csv('data/myfile.csv')

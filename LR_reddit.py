import json
import re
import string
import sys
import unicodedata
from collections import Counter

import gmpy2

translator_2 = dict.fromkeys(i for i in range(sys.maxunicode)
                             if unicodedata.category(chr(i)).startswith('P'))


def bi_dist(x, n, p):
    return gmpy2.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))


def text_lowercase(text):
    return text.lower()


def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result


def remove_whitespace(text):
    return " ".join(text.split())


def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def remove_punctuation(text):
    translator_1 = str.maketrans('', '', string.punctuation)
    return text.translate(translator_1).translate(translator_2)


data_file = 'data/scraper/data.json'
with open(data_file, 'r') as file:
    b = {}
    author_full_text = []
    data_content = file.read()
    data = json.loads(data_content)
    corpus = ""
    for item in data['data']:
        text = ""
        for obj in item.get("posts"):
            post = obj.get("selftext")
            post = text_lowercase(post)
            post = remove_numbers(post)
            post = remove_emoji(post)
            post = remove_punctuation(post)
            post = remove_whitespace(post)
            re.sub(' +', ' ', post)
            post += " "
            text += post
        corpus += text
        text.rstrip()
        author_full_text.append(text)
    corpus.rstrip()
    n = len(corpus.split())
    wordcount = Counter(corpus.split())
    for k in wordcount:
        binomial = bi_dist(wordcount.get(k), n, wordcount.get(k) / n)
        b.update({k: binomial})

    for l in author_full_text:
        excluded_list = author_full_text.copy()
        excluded_list.remove(l)
        corpus = " ".join(excluded_list)
        b_C = {}
        n = len(corpus.split())
        wordcount = Counter(corpus.split())
        for k in wordcount:
            binomial = bi_dist(wordcount.get(k), n, wordcount.get(k) / n)
            b_C.update({k: binomial})
        b_A = {}
        n = len(l.split())
        wordcount = Counter(l.split())
        # x = {}
        for k in wordcount:
            binomial = bi_dist(wordcount.get(k), n, wordcount.get(k) / n)
            b_A.update({k: binomial})
            # if b_C.get(k) is not None:
            #     # x.update({k: -2 * math.log1p(b.get(k) / (b_A.get(k) * b_C.get(k)))})
            #     print(k + "       " + str(-2 * math.log1p(b.get(k) / (b_A.get(k) * b_C.get(k)))))
            # else:
            #     print(k + "       " + str(-2 * math.log1p(b.get(k) / b_A.get(k))))
            # x.update({k: -2 * math.log1p(b.get(k) / b_A.get(k))})

        # for key, value in sorted(x.items(), key=itemgetter(1)):
        #     print(str(key) + "        " + str(value))

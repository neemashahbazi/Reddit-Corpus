import math
import os
import re
import string
import sys
import unicodedata
from collections import Counter

from scipy.stats import binom

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


corpus = ""
b = {}
author_full_text = []
for file in os.walk("data/NLP/pan14-authorship-verification-training-corpus-2014-04-22"):
    text = ""
    for f in file[2]:
        if "known0" in f:
            document = open(file[0] + "/" + f, 'r')
            post = document.read()
            post = text_lowercase(post)
            post = remove_numbers(post)
            post = remove_punctuation(post)
            post = remove_whitespace(post)
            re.sub(' +', ' ', post)
            post += " "
            text += post
        if len(text) != 0:
            corpus += text
            text.rstrip()
            author_full_text.append(text)
corpus.rstrip()
n = len(corpus.split())
wordcount = Counter(corpus.split())
for k in wordcount:
    binomial = binom.pmf(wordcount.get(k), n, wordcount.get(k) / n)
    b.update({k: binomial})

for l in author_full_text:
    excluded_list = author_full_text.copy()
    excluded_list.remove(l)
    corpus = " ".join(excluded_list)
    b_C = {}
    n = len(corpus.split())
    wordcount = Counter(corpus.split())
    for k in wordcount:
        binomial = binom.pmf(wordcount.get(k), n, wordcount.get(k) / n)
        b_C.update({k: binomial})
    b_A = {}
    n = len(l.split())
    wordcount = Counter(l.split())
    x = {}
    for k in wordcount:
        binomial = binom.pmf(wordcount.get(k), n, wordcount.get(k) / n)
        b_A.update({k: binomial})
        print(str(k) + "   " + "b:" + str(b.get(k)) + "   " + "b_A:" + str(b_A.get(k)) + "    b_C:" + str(b_C.get(k)))
        if b_C.get(k) is not None:
            # x.update({k: -2 * math.log1p(b.get(k) / (b_A.get(k) * b_C.get(k)))})
            print(k + "       " + str(-2 * math.log1p(b.get(k) / (b_A.get(k) * b_C.get(k)))))
        else:
            # x.update({k: -2 * math.log1p(b.get(k) / b_A.get(k))})
            print(k + "       " + str(-2 * math.log1p(b.get(k) / b_A.get(k))))

    # for key, value in sorted(x.items(), key=itemgetter(1)):
    #     print(str(key) + "        " + str(value))

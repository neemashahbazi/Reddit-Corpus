import codecs
import os

import pandas as pd
from bs4 import BeautifulSoup

# temp = []
# for filename in os.listdir("data/NLP/blogs"):
#     blog = BeautifulSoup(codecs.open("data/NLP/blogs" + '/' + filename, encoding='utf-8', errors='ignore'),
#                          "lxml")
#     temp.append(len(blog.find_all('post')))
#     for post in blog.find_all('post'):
#         post_text = post.text
#         temp.append(len(post_text.split()))
#
# print(min(temp))
# print(max(temp))
# print(sum(temp) / len(temp))

domains = {}
df = pd.DataFrame(columns=['label', 'text', 'gender', 'age', 'zodiac'])
for f in os.listdir("data/NLP/blogs"):
    ds_gender = f.split('.')[1].lower()
    ds_age = f.split('.')[2]
    ds_label = f.split('.')[3].lower()
    ds_zodiac = f.split('.')[4].lower()

    blog_file = BeautifulSoup(codecs.open("data/NLP/blogs" + '/' + f, encoding='utf-8', errors='ignore'), "lxml")
    if ds_label not in domains:
        domains[ds_label] = len(blog_file.find_all('post'))
    else:
        domains[ds_label] += len(blog_file.find_all('post'))
temp = []
for d in domains:
    print(d + ": " + str(domains.get(d)))
    temp.append(domains.get(d))
print("Avg # of posts per domain: " + str(sum(temp) / len(temp)))

#     if ds_label not in domains:
#         domains[ds_label] = 1
#     else:
#         domains[ds_label] += 1
# temp = []
# for d in domains:
#     print(d + ": " + str(domains.get(d)))
#     temp.append(domains.get(d))
# print("Avg # of authors per domain: " + sum(temp) / len(temp))

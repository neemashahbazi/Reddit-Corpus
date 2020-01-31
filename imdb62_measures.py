authors = set()
with open("data/NLP/imdb62.txt", encoding='utf-8') as f:
    for line in f:
        author = line.split('\t')[1].strip()
        authors.add(author)

obj = {}
for author in authors:
    reviews = []
    with open("data/NLP/imdb62.txt", encoding='utf-8') as f:
        for line in f:
            if line.split('\t')[1].strip() == author:
                reviews.append(line.split('\t')[5].strip())
    obj.update({author: reviews})

temp = []
for o in obj:
    for p in obj.get(o):
        temp.append(len(p))
print(min(temp))
print(max(temp))
print(sum(temp) / len(temp))

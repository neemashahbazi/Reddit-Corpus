import os


def remove_whitespace(text):
    return " ".join(text.split())


cpt = sum([len(files) for r, d, files in os.walk("data/NLP/ml_dataset")])
print(cpt)

temp = []
for file in os.walk("data/NLP/ml_dataset"):
    x = file[0].split("/")
    if len(file[2]) != 0:
        temp.append(len(file[2]))
print(min(temp))
print(max(temp))
print(sum(temp) / len(temp))

temp = []
for file in os.walk("data/NLP/ml_dataset"):
    for f in file[2]:
        document = open(file[0] + "/" + f, 'r', encoding='windows-1252')
        count = 0

        for x in document.read().split():
            count += 1
        temp.append(count)
print(min(temp))
print(max(temp))
print(sum(temp) / len(temp))

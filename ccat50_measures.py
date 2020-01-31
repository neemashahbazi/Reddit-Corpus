import os

temp = []
for file in os.walk("data/NLP/C50"):
    for f in file[2]:
        document = open(file[0] + "/" + f, 'r', encoding='windows-1252')
        count = 0
        for x in document.read().split():
            count += 1
        temp.append(count)
print(len(temp))
print(min(temp))
print(max(temp))
print(sum(temp) / len(temp))

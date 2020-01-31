import json
import os

# cpt = sum([len(files) for r, d, files in os.walk("data/NLP/enron_maildir")])
# print(cpt)

# temp=[]
# for file in os.walk("data/NLP/enron_maildir"):
#     cpt = sum([len(files) for r, d, files in os.walk(file[0])])
#     x = file[0].split("/")
#     if len(x) == 4:
#         temp.append(cpt)
#         print(file[0] + ": " + str(cpt))
# print(min(temp))
# print(max(temp))
# print(sum(temp)/len(temp))

temp = []
for file in os.walk("data/NLP/enron_maildir"):
    x = file[0].split("/")
    if len(x) == 4:
        with open(file[0] + "/" + 'messages.json', 'r') as f:
            data_content = f.read()
            data = json.loads(data_content)
            for item in data:
                temp.append(len(item.get("message").split()))
print(min(temp))
print(max(temp))
print(sum(temp) / len(temp))

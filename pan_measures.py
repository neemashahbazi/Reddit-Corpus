import os

cpt = sum([len(files) for r, d, files in os.walk(
    "data/NLP/pan14-authorship-verification-training-corpus-2014-04-22/pan14-author-verification-training-corpus-english-essays-2014-04-22")])
print(cpt - 203)
# temp = []
# for file in os.walk("data/NLP/pan14-authorship-verification-training-corpus-2014-04-22"):
#     x = file[0].split("/")
#     if len(x) == 5:
#         # print(file[0] + ": " +str(len(file[2])-1))
#         temp.append(len(file[2]) - 1)
# print(min(temp))
# print(max(temp))
# print(sum(temp) / len(temp))

# temp = []
# for file in os.walk("data/NLP/pan14-authorship-verification-training-corpus-2014-04-22"):
#     for f in file[2]:
#         if "known0" in f:
#             document = open(file[0]+"/"+f, 'r')
#             count = 0
#             for x in document.read().split():
#                 count += 1
#             temp.append(count)
# print(len(temp))
# print(min(temp))
# print(max(temp))
# print(sum(temp) / len(temp))

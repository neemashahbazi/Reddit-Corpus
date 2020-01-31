import json

data_file = 'data/scraper/data.json'
with open(data_file, 'r') as file:
    data_content = file.read()
    data = json.loads(data_content)
    print("#####################DATASET IN A NUTSHELL#######################")
    print("Number of Authors: " + str(len(data['data'])))
    count = 0
    for item in data['data']:
        for obj in item.get("posts"):
            count += 1
        for obj in item.get("comments"):
            count += 1
    print("Number of documents: " + str(count))
    post_count = []
    post_length = []
    for item in data['data']:
        post_count.append(len(item.get("posts")))
    print("Min number of posts in total: " + str(min(post_count)))
    print("Max number of posts in total: " + str(max(post_count)))
    print("Avg number of posts in total: " + str(sum(post_count) / len(post_count)))

    for item in data['data']:
        for obj in item.get("posts"):
            post_length.append(len(obj.get("selftext").split()))
    print("Min length of posts in total: " + str(min(post_length)))
    print("Max length of posts in total: " + str(max(post_length)))
    print("Avg length of posts in total: " + str(sum(post_length) / len(post_length)))

    subreddits = {}
    for item in data['data']:
        for obj in item.get("posts"):
            if obj.get("subreddit") not in subreddits:
                subreddits[obj.get("subreddit")] = 1
            else:
                subreddits[obj.get("subreddit")] += 1
    sum_ = 0
    for key in subreddits:
        sum_ += subreddits.get(key)
    print("Avg # of posts per subreddit: " + str(sum_ / len(subreddits)))
    authors = {}
    for item in data['data']:
        temp = {}
        for obj in item.get("posts"):
            if obj.get("subreddit") not in temp:
                temp[obj.get("subreddit")] = 1
        for key in temp:
            if key not in authors:
                authors[key] = 1
            else:
                authors[key] += 1

    sum_ = 0
    for key in authors:
        sum_ += authors.get(key)
    print("Avg # of authors per subreddit: " + str(sum_ / len(authors)))
    authors = []
    for item in data['data']:
        subreddits = {}
        for obj in item.get("posts"):
            if obj.get("subreddit") not in subreddits:
                subreddits[obj.get("subreddit")] = 1
            else:
                subreddits[obj.get("subreddit")] += 1
        authors.append(subreddits[obj.get("subreddit")])
    print("Avg number of subreddits per author: " + str(sum(authors) / len(authors)))
    top = []
    for item in data['data']:
        subreddits = {}
        for obj in item.get("posts"):
            if obj.get("subreddit") not in subreddits:
                subreddits[obj.get("subreddit")] = 1
            else:
                subreddits[obj.get("subreddit")] += 1
        sorted_map = sorted(subreddits.items(), key=lambda x: x[1], reverse=True)
        top.append(sorted_map[0][1])
    print("Avg # of posts for favorite subreddit per user: " + str(sum(top) / len(top)))

    comment_count = []
    comment_length = []
    for item in data['data']:
        comment_count.append(len(item.get("comments")))
    print("Min number of comments in total: " + str(min(comment_count)))
    print("Max number of comments in total: " + str(max(comment_count)))
    print("Avg number of comments in total: " + str(sum(comment_count) / len(comment_count)))

    for item in data['data']:
        for obj in item.get("comments"):
            comment_length.append(len(obj.get("body").split()))
    print("Min length of comments in total: " + str(min(comment_length)))
    print("Max length of comments in total: " + str(max(comment_length)))
    print("Avg length of comments in total: " + str(sum(comment_length) / len(comment_length)))
    # print("#####################AUTHORS IN A NUTSHELL#######################")
    # for item in data['data']:
    #     subreddits = {}
    #     for obj in item.get("posts"):
    #         if obj.get("subreddit") not in subreddits:
    #             subreddits[obj.get("subreddit")] = 1
    #         else:
    #             subreddits[obj.get("subreddit")] += 1
    #     sorted_map = sorted(subreddits.items(), key=lambda x: x[1], reverse=True)
    #     print("_______________________________________________")
    #     print("For " + item.get("id") + ": " + item.get("name"))
    #     print("Max number of posts per subreddit: " + str(sorted_map[0][1]))
    #     print("Min number of posts per subreddit: " + str(sorted_map[len(sorted_map) - 1][1]))
    #     print("Avg number of posts per subreddit: " + str(sum(map(lambda x: x[1], sorted_map)) / len(sorted_map)))
    #     print()
    #     post_length = []
    #     for obj in item.get("posts"):
    #         post_length.append(len(obj.get("selftext").split()))
    #     print("Min length of posts: " + str(min(post_length)))
    #     print("Max length of posts: " + str(max(post_length)))
    #     print("Avg length of posts: " + str(sum(post_length) / len(post_length)))

    shared_subreddit = []
    for author1 in data['data']:
        temp1 = set()
        for post1 in author1.get("posts"):
            temp1.add(post1.get('subreddit'))
        for author2 in data['data']:
            if author2.get("id") != author1.get("id"):
                temp2 = set()
                for post2 in author2.get("posts"):
                    temp2.add(post2.get('subreddit'))
                intersect = temp1.intersection(temp2)
                # print(author1.get("id") + " & " + author2.get("id") + " :" + str(len(intersect)))
                shared_subreddit.append(len(intersect))
    print("Avg number of shared subreddits between any pair: " + str(sum(shared_subreddit) / len(shared_subreddit)))

    # for author in data['data']:
    #     temp = set()
    #     for post in author.get("posts"):
    #         if post.get('subreddit') in {"AmItheAsshole",
    #                                      "relationship_advice",
    #                                      "unpopularopinion",
    #                                      "legaladvice",
    #                                      "rant",
    #                                      "tifu"
    #                                      }:
    #             temp.add(post.get('subreddit'))
    #     print("Number of top subreddits " + author.get("id") + " has posted in: " + str(len(temp)))

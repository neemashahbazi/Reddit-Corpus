import json

data_file = 'data/unpopularopinion/data.json'
with open(data_file, 'r') as file:
    data_content = file.read()
    data = json.loads(data_content)
    count = 0
    for item in data['data']:
        subreddits = {}
        for obj in item.get("otherPosts"):
            if obj.get("subreddit") not in subreddits:
                subreddits[obj.get("subreddit")] = 1
            else:
                subreddits[obj.get("subreddit")] += 1
        sorted_map = sorted(subreddits.items(), key=lambda x: x[1], reverse=True)
        temp = []
        for key in sorted_map:
            if key[0] in {"AmItheAsshole",
                          "relationship_advice",
                          "unpopularopinion",
                          "legaladvice",
                          "casualconversation",
                          "rant",
                          "personalfinance",
                          "Advice",
                          "Jokes",
                          "relationships",
                          "raisedbynarcissists",
                          "AskReddit",
                          "tifu"
                          } and key[1] >= 3:  # No. of posts in other subreddits
                temp.append("       " + str(key[0]) + ": " + str(key[1]))
        if len(temp) >= 2:  # No. of subreddits except original subreddit
            print("__________________________________________")
            print(item.get("id") + ": " + item.get("author"))
            print("       unpopularopinion: " + str(len(item.get("post"))))
            print("       unpopularopinion comments: " + str(len(item.get("comment"))))
            print(*temp, sep='\n')
            count += 1
    print("__________________________________________")
    print("NUMBER OF QUALIFIED AUTHORS: " + str(count))

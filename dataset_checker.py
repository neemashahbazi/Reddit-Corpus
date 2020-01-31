import json

data_file = 'data/scraper/data.json'
with open(data_file, 'r') as file:
    data_content = file.read()
    data = json.loads(data_content)
    noise = set()
    for item in data['data']:
        subreddits = {}
        for obj in item.get("posts"):
            if obj.get("subreddit") in {"AmItheAsshole",
                                        "relationship_advice",
                                        "unpopularopinion",
                                        "legaladvice",
                                        "rant",
                                        "tifu"
                                        }:
                if obj.get("subreddit") not in subreddits:
                    subreddits[obj.get("subreddit")] = 1
                else:
                    subreddits[obj.get("subreddit")] += 1
        sorted_map = sorted(subreddits.items(), key=lambda x: x[1], reverse=True)
        if sorted_map:
            top = sorted_map.pop(0)
            if top[1] < 5:
                print(item.get("id") + ": " + item.get("name") + "   " + str(top[0]) + ": " + str(top[1]))
                noise.add(item.get("id"))
        else:
            print(item.get("id") + ": " + item.get("name") + "   empty!")
            noise.add(item.get("id"))

    for item in data['data']:
        if item.get("id") in noise:
            print(data['data'][data['data'].index(item)].get("id") + " deleted!")
            del data['data'][data['data'].index(item)]
    open(data_file, "w").write(
        json.dumps(data, sort_keys=True, indent=4)
    )

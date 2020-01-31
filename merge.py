import json

import praw
from prawcore.exceptions import RequestException
from psaw import PushshiftAPI

data_files = {'data/unpopularopinion/data.json', 'data/tifu/data.json', 'data/AmItheAsshole/data.json',
              'data/relationship_advice/data.json', 'data/legaladvice/data.json', 'data/rant/data.json'}
scraped = 0
authors = {}
data = {'data': []}
for data_file in data_files:
    with open(data_file, 'r') as file:
        data_content = file.read()
        data = json.loads(data_content)
        for item in data['data']:
            if item.get("author") not in authors:
                authors.update({str(item.get("author")): 1})
            else:
                authors[item.get("author")] += 1

with open('data/scraper/data.json', 'r') as file:
    data_content = file.read()
    data = json.loads(data_content)
    for item in data['data']:
        if item.get("name") in authors:
            authors.pop(item.get("name"))
            scraped += 1

print(str(len(authors)))
reddit = praw.Reddit(client_id='ZKM8R8JsjFf7SA',
                     client_secret='C4XB8mrTAAFg0LvzJXsZaUDYz2M',
                     user_agent='my user agent')

api = PushshiftAPI(reddit)
author_counter = scraped + 1

for author in authors:
    print("Working on Author_" + str(author_counter) + ": " + author)
    gen1 = []
    try:
        gen1 = api.search_submissions(author=str(author))
    except RequestException:
        print("Failed to fetch submission")
    author_instance = {}
    author_instance.update({"id": "author_" + str(author_counter)})
    author_instance.update({"name": str(author)})
    posts_list = list(gen1)
    posts = []
    for post_item in posts_list:
        if len(post_item.selftext.split()) >= 100:
            post_instance = {}
            post_instance.update({"id": post_item.id})
            post_instance.update({"created_utc": post_item.created_utc})
            post_instance.update({"subreddit": str(post_item.subreddit)})
            post_instance.update({"title": post_item.title})
            post_instance.update({"selftext": post_item.selftext})
            post_instance.update({"score": post_item.score})
            post_instance.update({"num_comments": post_item.num_comments})
            posts.append(post_instance)
    author_instance.update({"posts": posts})
    comments = []
    gen2 = []
    try:
        gen2 = api.search_comments(author=str(author))
    except RequestException:
        print("Failed to fetch comment")
    comments_list = list(gen2)
    for comment_item in comments_list:
        if len(comment_item.body.split()) >= 100:
            comment_instance = {}
            comment_instance.update({"id": comment_item.id})
            comment_instance.update({"created_utc": comment_item.created_utc})
            comment_instance.update({"subreddit": str(comment_item.subreddit)})
            comment_instance.update({"body": comment_item.body})
            comment_instance.update({"score": comment_item.score})
            comments.append(comment_instance)
    author_instance.update({"comments": comments})
    author_counter += 1
    with open("data/scraper/data.json", 'r') as file:
        file_content = file.read()
        if file_content:
            data = json.loads(file_content)
            data['data'].append(author_instance)
    with open("data/scraper/data.json", 'w') as file:
        json_content = json.dump(data, file, indent=4)

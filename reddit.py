import json

import praw
from prawcore.exceptions import RequestException
from psaw import PushshiftAPI

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='my user agent')

api = PushshiftAPI(reddit)
gen1 = []
try:
    gen1 = api.search_submissions(subreddit='rant', limit=327107)
except RequestException:
    print("Failed to fetch submission")
allPosts = list(gen1)
data_file = 'data/rant/data.json'
data = {'data': []}
author_file = 'data/rant/author.json'
authors = {'author': []}
author_counter = 1
author_list = ["AutoModerator"]

for submission in allPosts:
    author = submission.author
    gen2 = []
    try:
        gen2 = api.search_submissions(subreddit='rant', author=str(author), limit=1000)
    except RequestException:
        print("Failed to fetch submission")
    authorPosts = list(gen2)
    document_counter = 0
    document_dict = {}
    author_dict = {}
    post_id = []
    if len(authorPosts) >= 5:
        for post in authorPosts:
            if len(post.selftext.split()) >= 100:
                post_id.append(str(post.id))
                document_counter += 1
    if not str(author) in author_list:
        author_list.append(str(author))
        if document_counter >= 5:
            print("author_" + str(author_counter) + " " + str(author))

            document_dict.update({"id": "author_" + str(author_counter)})
            document_dict.update({"author": str(author)})
            author_dict.update({"id": "author_" + str(author_counter)})
            author_counter += 1
            author_dict.update({"author": str(author)})
            document_dict.update({"post": post_id})
            gen3 = []
            try:
                gen3 = api.search_comments(subreddit='rant', author=str(author), limit=1000)
            except RequestException:
                print("Failed to fetch comment")
            comments = list(gen3)
            if len(comments) >= 0:
                comment_id = []
                for comment in comments:
                    if len(comment.body.split()) >= 100:
                        comment_id.append(str(comment.id))
                document_dict.update({"comment": comment_id})
            gen4 = []
            try:
                gen4 = api.search_submissions(author=str(author), subreddit='!rant', limit=1000)
            except RequestException:
                print("Failed to fetch submission")
            otherPosts = list(gen4)
            if len(otherPosts) >= 0:
                otherPosts_ent = []
                for post in otherPosts:
                    if len(post.selftext.split()) >= 100:
                        otherPosts_dict = {}
                        otherPosts_dict.update({"post": str(post.id)})
                        otherPosts_dict.update({"subreddit": str(post.subreddit)})
                        otherPosts_ent.append(otherPosts_dict)
                document_dict.update({"otherPosts": otherPosts_ent})
            with open(data_file, 'r') as file:
                data_content = file.read()
                if data_content:
                    data = json.loads(data_content)
                    data['data'].append(document_dict)

            with open(data_file, 'w') as file:
                json_content = json.dump(data, file, indent=4)

            with open(author_file, 'r') as file:
                author_content = file.read()
                if author_content:
                    authors = json.loads(author_content)
                    authors['author'].append(author_dict)

            with open(author_file, 'w') as file:
                json_content = json.dump(authors, file, indent=4)

            document_counter = 0

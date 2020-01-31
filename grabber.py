import praw
from prawcore.exceptions import RequestException
from psaw import PushshiftAPI

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='my user agent')

api = PushshiftAPI(reddit)
gen1 = []
try:
    gen1 = api.search_submissions(author="newtothistinderthing")
except RequestException:
    print("Failed to fetch submission")

    posts_list = list(gen1)
    posts = []
    for post_item in posts_list:
        if len(post_item.selftext.split()) >= 100:
            post_instance = {}
            post_instance.update({"id": post_item.id})
            post_instance.update({"created_utc": post_item.created_utc})
            post_instance.update({"subreddit": str(post_item.subreddit)})
            post_instance.update({"titlxe": post_item.title})
            post_instance.update({"selftext": post_item.selftext})
            post_instance.update({"score": post_item.score})
            post_instance.update({"num_comments": post_item.num_comments})
            posts.append(post_instance)

    for post in posts:
        print(post)

import praw

reddit = praw.Reddit('ryancreamervideobot', user_agent="RyanCreamerVideoBot/0.1")

subreddit = reddit.subreddit('ryancreamervideobot')

def create_post(title, url):
    subreddit.submit("New Video: {}".format(title), url=url, nsfw=True)
import praw

reddit = praw.Reddit('ryancreamervideobot')

subreddit = reddit.subreddit('ryancreamervideobot')

def create_post(title, url):
    subreddit.submit("New Video: {}".format(title), url=url, nsfw=True)
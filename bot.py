import requests

from rcbot import db, reddit

ret = requests.get("http://www.pornhub.com/webmasters/search?id=44bc40f3bc04f65b7a35&search=ryancreamer&ordering=newest")

j = ret.json()


def post(video):
    print("Posting video with id {}: {}".format(video.video_id, video.title))
    reddit.create_post(video.title, video.url)


for v in j["videos"]:

    if not db.get_video(video_id=v["video_id"]):
        obj = db.Video(url=v["url"], title=v["title"], video_id=v["video_id"], thumbnail=v["thumb"])
        obj.save()

        post(obj)
    

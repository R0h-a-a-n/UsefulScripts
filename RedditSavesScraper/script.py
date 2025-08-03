import praw
import os
import time
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

saved_links = []
count=0

for item in reddit.user.me().saved(limit=None):
    if hasattr(item,'url'):
        saved_links.append(item.url)
    elif hasattr(item,'permalink'):
        saved_links.append("https://reddit.com"+item.permalink)

    count += 1
    if count%30==0:
        print("Pausing after", count, "items")
        time.sleep(2)

with open("saved_posts_links.txt","w") as f:
     for link in saved_links:
         f.write(link+"\n")

print(len(saved_links), "saved links written to saved_posts_links.txt")

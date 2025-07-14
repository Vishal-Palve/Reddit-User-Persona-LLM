import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="RedditPersonaApp"
)

def scrape_user_data(username):
    user = reddit.redditor(username)
    posts, comments = [], []

    try:
        for submission in user.submissions.new(limit=20):
            posts.append(f"Title: {submission.title}\nBody: {submission.selftext}")
        for comment in user.comments.new(limit=20):
            comments.append(f"Comment: {comment.body}")
    except Exception as e:
        print(f"[ERROR] Failed to fetch user data: {e}")

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }

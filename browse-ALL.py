#!/usr/bin/python
import praw

reddit = praw.Reddit('PRAW_INSTANCE_HERE')

subreddit = reddit.subreddit("All")

for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

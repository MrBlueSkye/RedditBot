#!/usr/bin/python

import praw
import time
import random

reddit = praw.Reddit('YOUR_PRAW_INSTANCE_HERE')
subreddit = reddit.subreddit("CHOOSE_SUBREDDIT_HERE")
comments = subreddit.stream.comments()
AVAILABLE_RESPONSES = ['REPLY1', 'REPLY2', 'REPLY3', 'REPLY4', 'REPLY5']

for comment in comments:
    text = comment.body 
    author = comment.author 
    if 'CHOOSE_A_KEYWORD_HERE' in text.lower():
        CHOSEN_REPONSE = random.choice(AVAILABLE_RESPONSES)
        message = CHOSEN_REPONSE.format(author)
        comment.reply(message) 
        time.sleep(600)

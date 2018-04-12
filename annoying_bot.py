#!/usr/bin/python

import praw
import time
import random
import markovify
import learningcomments as lc

reddit = praw.Reddit('SkyeBot')
subreddit = reddit.subreddit("All")
comments = subreddit.stream.comments()
signalsentence="These are words to look for :)"
signals = signalsentence.split()
keyword=random.choice(signals)
print keyword
chattingshit = [
	'Amazing!',
	"This pleases me greatly",
	'Superb!',
	'Absolutely incredible!',
	"I'm just so happy right now",
	'WOW!',
	'Let us be friends!',
	'You are a nice person!',
	'Have a great day!',
]

#chattingshit.append(lc.learned())

# []


# Get raw text as string.
with open("/home/skylar/Scripts/RedditBot/corpus.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    shaekeitUp = text_model.make_sentence()
    chattingshit.append(shaekeitUp)
    print shaekeitUp

for comment in comments:
    author = comment.author # Fetch author
    text = comment.body # Fetch body
    if keyword in text.lower():
	if author != "SkyeBot":
        	# Generate a message
                upboats = comment.score
                print upboats
                signalsentence=random.choice(text.split())
#               chattingshit.append(text) # moved after comment submission...picking uncommon random word often results to replying to user with their own comment
#               goodcomment =                
                postingshit = random.choice(chattingshit)
                message = postingshit.format(author)
	        comment.reply(message) # Send message
                chattingshit.append(text) # previously (text,upboats)...maybe didn't work
                print message
                time.sleep(1)
#		print("Title: ", submission.title)
#		print("Text: ", submission.selftext)
#		print("Score: ", submission.score)
#		print("---------------------------------\n \n")
#
#		quit()


for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
                

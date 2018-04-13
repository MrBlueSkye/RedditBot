#!/usr/bin/python

import praw
import time
import random
import markovify

reddit = praw.Reddit('MY_BOT_USERNAME')
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

# []


# Get raw text as string.
with open("/path/to/corpus.txt") as f:
    textsource = f.read()

# Build the model.
text_model = markovify.NewlineText(textsource)

try:
    for comment in comments:
        author = comment.author # Fetch author
        text = comment.body # Fetch body
        if keyword in text.lower():
            if author != "MY_BOT_USERNAME":
                    # Generate a message
                    for i in range(3):
                        shaekeitUp = text_model.make_sentence()
                        chattingshit.append(shaekeitUp)
                        print shaekeitUp
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
                    time.sleep(20)
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

except KeyboardInterrupt:
    print("Shutting down.")
    quit()
except praw.errors.HTTPException as e:
    exc = e._raw
    print("Some thing bad happened! HTTPError", exc.status_code)
    if exc.status_code == 503:
        print("Let's wait til reddit comes back! Sleeping 60 seconds.")
        time.sleep(60)
except Exception as e:
    print("Some thing bad happened! :O ", e)
    traceback.print_exc()                

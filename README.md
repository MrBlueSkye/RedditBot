# RedditBot

Make sure you have python and praw ready to go:

apt install python && apt install pip && pip install praw

skylar@SkyeNetDev RedditBot  ✗ python --version
Python 2.7.12


# Update the praw.ini file for your install with the details of your new bot instance

sudo vim /usr/local/lib/python2.7/dist-packages/praw/praw.ini

# Fill in the indicated fields in the comment_test.py script, make script executable and run

sudo vim comment_test.py
sudo chmod +x comment_test.py
./comment_test.py



import praw
import random
import time
import os

"""
Python Reddit API Wrapper - PRAW

User: mister_good_bot
"""
# client_id="nC9hMVXjUpykFA",
# client_secret="nHdGA_nrl1h3HGZT1kAnOTnRpG8i0g",
# username="mister_good_bot",
# password="zdarova",

# Instantiate a PRAW.Reddit object
my_reddit_instance = praw.Reddit(
    client_id=os.environ.get("client_id"),
    client_secret=os.environ.get("client_secret"),
    username=os.environ.get("reddit_username"),
    password=os.environ.get("reddit_password"),
    user_agent="<console:mister_good_bot:1.0>"
)

# Access a specific subreddit
subreddit = my_reddit_instance.subreddit('selfimprovement')

# Create a string variable with the desired message
robot_speech = "boop boop beep - I'm the reddit inspirational quote bot. Quote of the day: \n"

def select_quote():
    test = open('quotes.txt')

    quote_list = []
    for line in test:
        quote_list.append(line)

    quote_today = random.randint(1, len(quote_list)-1)
    return quote_list[quote_today]

while True:
    for submission in subreddit.new(limit=100):
        all_authors = []
        if 'motivated' in submission.title or 'motivation' in submission.title or 'motivate' in submission.title:
            for comment in submission.comments:
                all_authors.append(str(comment.author))
            if 'mister_good_bot' not in all_authors:
                print(submission.title)
                submission.reply(f'{robot_speech}\n{select_quote()}')
    time.sleep(20)




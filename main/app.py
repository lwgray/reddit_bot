''' Collect Testing Data '''
# coding: utf-8
import praw
import os
# import IBM Watson Text Analysis API
from alchemyapi import AlchemyAPI
import csv
import sys


REDDIT_ID = os.environ['REDDIT_ID']
REDDIT_SECRET = os.environ['REDDIT_SECRET']


def collect_data():
    ''' Collect Depression Subreddit Data'''
    # alchemyapi = AlchemyAPI()
    # Define Reddit bot
    user_agent = "depression_app v0.1"
    reddit = praw.Reddit(user_agent=user_agent, client_id=REDDIT_ID,
                         client_secret=REDDIT_SECRET)
    # Retreive Depression Subreddit
    submissions = reddit.get_subreddit("deppression").get_new()
    return submissions


def analyze(submissions):
    ''' Send reddit data to IBM Sentiment Api '''
    alchemyapi = AlchemyAPI()
    with open('data.csv', 'w') as data:
        writer = csv.writer(data, delimiter=',')
        for post in submissions:
            try:
                text = post.selftext
                response = alchemyapi.sentiment("text", text)
                writer.writerow([post.title, post.score,
                                response["docSentiment"]['score'],
                                response["docSentiment"]["type"]])
            except:
                continue
    return response

if __name__ == '__main__':
    sys.exit(collect_data())

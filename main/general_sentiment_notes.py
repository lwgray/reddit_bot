# coding: utf-8
'''
Use IBM Sentimental Analysis API
to determine binary sentiment of
depression-related subreddit posts
'''

import os
import nltk.data
from alchemyapi import AlchemyAPI
import sys


def cycle():
    '''Parse and assign sentiment for Suicide corpora'''
    # open IBM Watson API
    api = AlchemyAPI()
    logdir = "suicide_notes"
    logfiles = sorted([f for f in os.listdir(logdir) if f.endswith('.txt')])

    results = {'negative': 0, 'positive': 0}
    for index, note in enumerate(logfiles):
        letter = nltk.data.load("{0}/{1}".format(logdir, note), format='raw')
        response = api.sentiment('text', letter)
        print index, note, response
        if response['docSentiment']['type'] == 'negative':
            results['negative'] += float(response['docSentiment']['score'])
        else:
            results['positive'] += float(response['docSentiment']['score'])
    return results


def score(results):
    ''' Tally and output Sentiment Score '''
    avg_score = (results['negative'] + results['positive'])/25
    if avg_score < 0:
        print "Overall Sentiment: Negative"
    else:
        print "Overall Sentiment: Positive"

    print "Average Score = {0}".format(avg_score)
    print "Average Positive Sentiment", results['positive']/7
    print "Average Negative Sentiment", results['negative']/18
    return avg_score


def main():
    ''' Analyze and score general sentiment of Suicide Notes  '''
    results = cycle()
    avg_score = score(results)
    return [results, avg_score]


if __name__ == '__main__':
    sys.exit(main())

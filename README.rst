REDDIT BOT
----------
A Bot that performs Sentiment Analysis on posts from r/depression subreddit

.. image:: img/sad3.png
 
Goals of project:
-----------------
1.  Reddit bot which reads new posts in depression subreddit 
2.  Analyze sentiment of posts
3.  Score the likelyhood of suicide
4.  Respond with appropriate suicide hotline information

Quick Start:
------------
::    
    $ python app.py

File info:
-----------------
1.  All files are located in main folder
2.  All files must be run from mail folder in order to work
3.  general_sentiment file runs analysis on suicide notes
4.  suicide notes are located within suicide_notes subfolder in the main folder 
5.  reddit_sentiment_scoring file calculates /r/depression scores 
6.  app.py file collects testing text scoring of /r/depression into data.csv
7.  data.csv file is created with app.py... it contains title, upvotes, sentiment, and score of each /r/depression posts
8.  api_key.txt - contains api key - visit alchemyapi website if you would like to request your own free api key.  The free key only allows 1000 requests per day.
9.  all other files in main folder belong to alchemyapi library, ie LICENSE, example.py, README

Add Later:
----------
-  Provide community psychiatrist/psychologist resources based on poster's location

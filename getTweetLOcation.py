import tweepy
import csv
import pandas as pd
import time
import re
import calendar

consumer_key = XXXXXXXXXXXXXXXXXXXXXXX
consumer_secret = XXXXXXXXXXXXXXXXXXXXXXX
access_token = XXXXXXXXXXXXXXXXXXXXXXX
access_secret = XXXXXXXXXXXXXXXXXXXXXXX

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def get_all_tweets(screen_name):
    global outtweets
    all_the_tweets = []

    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    all_the_tweets.extend(new_tweets)

    oldest_tweet = all_the_tweets[-1].id - 1

    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name,
                                       count=200, max_id=oldest_tweet)
        all_the_tweets.extend(new_tweets)
        oldest_tweet = all_the_tweets[-1].id - 1

        for tweet in all_the_tweets:
            try:
                if tweet.coordinates is not None:
                    print(tweet)
                    outtweets = [[screen_name, tweet.created_at, tweet.coordinates]]
            except:
                pass
    with open('tweetsLocation.csv', 'a', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)

if __name__ == '__main__':

    file = 'users.csv'

    df = pd.read_csv(file)

    userSet = set(df.user)  # user.name
    finishedUser = set()

    for user in userSet:
        print(user)
        print(len(userSet) - len(finishedUser))
        time.sleep(1)
        try:
            get_all_tweets(user)
        except:
            pass
        finishedUser.add(user)
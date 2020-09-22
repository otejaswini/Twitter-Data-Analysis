import tweepy
import pandas as pd
import time
import json

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
    file = open("JSON_FILES/"+screen_name+'_tweet.json', "a")
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=screen_name,
                                       count=200, max_id=oldest_tweet)
        all_the_tweets.extend(new_tweets)
        oldest_tweet = all_the_tweets[-1].id - 1
        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(screen_name=screen_name,
                                           count=200, max_id=oldest_tweet)
            all_the_tweets.extend(new_tweets)

            oldest_tweet = all_the_tweets[-1].id - 1
        print("\n")
        for status in all_the_tweets:
            print(json.dumps(status._json, sort_keys=True, ensure_ascii=True), file=file)
        return all_the_tweets

if __name__ == '__main__':
    # pass in the username of the account you want to download
    file = 'users.csv'

    df = pd.read_csv(file)

    userSet = set(df.user)  # user.name
    finishedUser = set()

    for user in userSet:
        print(user)
        print(len(userSet) - len(finishedUser))
        time.sleep(10)
        try:
            get_all_tweets(user)
            # get_text('CSV_FILES/'+user + '_tweets.csv')
        except:
            pass
        finishedUser.add(user)


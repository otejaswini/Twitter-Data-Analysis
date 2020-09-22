import tweepy
import csv

consumer_key = XXXXXXXXXXXXXXXXXXXXXXX
consumer_secret = XXXXXXXXXXXXXXXXXXXXXXX
access_token = XXXXXXXXXXXXXXXXXXXXXXX
access_secret = XXXXXXXXXXXXXXXXXXXXXXX

def get_followers(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    follower_count = api.get_user(screen_name).followers_count
    friend_count = api.get_user(screen_name).friends_count
    user = api.get_user(screen_name)
    count = numberoftweets('CSV_FILES/' + screen_name + '_tweets.csv')
    followers = [screen_name, follower_count, friend_count, user.id, user.location, count]

    with open('followers_tweets.csv', 'a', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(followers)

def numberoftweets(filename):
    cnt = 0
    with open(filename) as f:
        cr = csv.reader(f)
        for row in cr:
            cnt += 1
    return cnt - 1
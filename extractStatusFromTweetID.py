import tweepy
import json

consumer_key = XXXXXXXXXXXXXXXXXXXXXXX
consumer_secret = XXXXXXXXXXXXXXXXXXXXXXX
access_token = XXXXXXXXXXXXXXXXXXXXXXX
access_secret = XXXXXXXXXXXXXXXXXXXXXXX

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def get_all_tweets(id):
    all_the_tweets = []

    new_tweets = api.get_status(id)
    print(new_tweets)
    all_the_tweets.extend(new_tweets)
    print(all_the_tweets)
    oldest_tweet = all_the_tweets[-1].id - 1
    file = open('statuses_tweet.json', "a")
    while len(new_tweets) > 0:
        new_tweets = api.get_status(id, max_id=oldest_tweet)
        all_the_tweets.extend(new_tweets)
        oldest_tweet = all_the_tweets[-1].id - 1
        while len(new_tweets) > 0:
            new_tweets = api.get_status(id, max_id=oldest_tweet)
            all_the_tweets.extend(new_tweets)

            oldest_tweet = all_the_tweets[-1].id - 1
        for status in all_the_tweets:
            print(json.dumps(status._json, sort_keys=True, ensure_ascii=True), file=file)
        return all_the_tweets


filename = "/Users/tejaswini/PycharmProjects/extractData/tweetIDs.txt"

with open(filename) as f:
    lines = f.read().splitlines()

print(lines)
if __name__ == '__main__':

    for i in range(0, len(lines)-1):
        try:
            get_all_tweets(lines[i])
        except:
            print("Inside the exception - no:2")
            continue
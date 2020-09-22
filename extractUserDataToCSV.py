import tweepy  # https://github.com/tweepy/tweepy
import csv
import time
import pandas as pd
import re
import calendar
consumer_key = XXXXXXXXXXXXXXXXXXXXXXX
consumer_secret = XXXXXXXXXXXXXXXXXXXXXXX
access_token = XXXXXXXXXXXXXXXXXXXXXXX
access_secret = XXXXXXXXXXXXXXXXXXXXXXX

def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")
    print(alltweets[0])
    # transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text,calendar.day_name[tweet.created_at.weekday()],tweet.created_at.strftime("%H:%M:%S")] for tweet in alltweets]

    # write the csv  
    with open('/Users/tejaswini/PycharmProjects/extractData/CSV_FILES/'+screen_name+'_tweets.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "created_at", "text","Day of the week","Time at which it was posted"])
        writer.writerows(outtweets)
    pass

def get_text(file):
    data = pd.read_csv(file)
    text = " "
    a = data.text.tolist()
    for ele in a:
        text = text+ ele
    newText = re.sub(r'^https?:\/\/.*[\r\n]*[^\w\s]', '', str(text))
    with open('/Users/tejaswini/PycharmProjects/extractData/UserText/'+user+'_textdata.txt', 'w') as file:
        file.write(newText)

if __name__ == '__main__':
    # pass in the username of the account you want to download
    file = 'extraUsers.csv'

    df = pd.read_csv(file)

    userSet = set(df.user)  # user.name
    finishedUser = set()

    for user in userSet:
        print(user)
        print(len(userSet) - len(finishedUser))
        time.sleep(10)
        try:
            get_all_tweets(user)
            get_text('CSV_FILES/'+user + '_tweets.csv')
        except:
            pass
        finishedUser.add(user)

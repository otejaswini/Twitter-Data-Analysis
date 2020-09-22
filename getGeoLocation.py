#!/usr/bin/env python
from __future__ import print_function
import tweepy
import csv
import pandas as pd
import time
from geopy.geocoders import Nominatim
locator = Nominatim(user_agent="myGeocoder")

consumer_key = XXXXXXXXXXXXXXXXXXXXXXX
consumer_secret = XXXXXXXXXXXXXXXXXXXXXXX
access_token = XXXXXXXXXXXXXXXXXXXXXXX
access_secret = XXXXXXXXXXXXXXXXXXXXXXX
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == '__main__':

    file = 'randUsers.csv'

    df = pd.read_csv(file)

    userSet = set(df.user)  # user.name
    finishedUser = set()

    for user in userSet:
        time.sleep(10)
        getData = api.get_user(user)
        try:
            print(getData.location)
            loc = locator.geocode(getData.location)
            data = [user, getData.location,getData.followers_count,getData.friends_count, [loc.latitude, loc.longitude]]
            with open('profileLocation.csv', 'a', newline='', encoding='utf8') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
        except:
            pass
        finishedUser.add(user)
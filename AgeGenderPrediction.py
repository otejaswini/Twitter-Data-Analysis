import os
import csv
import re
import tweepy
import csv

age_intercept = 23.2188604687
gender_intercept = -0.06724152

consumer_key = XXXXXXXXXXXXXXXXXXXXXXX
consumer_secret = XXXXXXXXXXXXXXXXXXXXXXX
access_token = XXXXXXXXXXXXXXXXXXXXXXX
access_secret = XXXXXXXXXXXXXXXXXXXXXXX

with open('predictions.csv','w',encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['Username','Gender','Age', 'follower_count', 'friend_count', 'user.id', 'user.location', 'count'])

def get_age_lexica(file_name="emnlp14age.csv"):
    age_lex = {}
    with open(file_name, mode='r') as infile:
        reader = csv.DictReader(infile)
        for data in reader:
            weight = float(data['weight'])
            term = data['term']
            age_lex[term] = weight

    del age_lex['_intercept']
    return age_lex


def get_gender_lexica(file_name="emnlp14gender.csv"):
    gender_lex = {}
    with open(file_name, mode='r') as infile:
        reader = csv.DictReader(infile)
        for data in reader:
            weight = float(data['weight'])
            term = data['term']
            gender_lex[term] = weight

    del gender_lex['_intercept']
    return gender_lex


age_lex = get_age_lexica()
gender_lex = get_gender_lexica()


def get_gender(text):
    words = text.split()

    total_frequency = {}
    for word in words:
        total_frequency[word] = total_frequency.get(word, 0) + 1

    gender = 0
    words_frequency = 0
    for word, frequency in total_frequency.items():
        if word in gender_lex:
            words_frequency += frequency
            gender += frequency * gender_lex[word]
    if words_frequency != 0:
         gender = gender / words_frequency + gender_intercept
    return gender

def get_age(text):
    words = text.split()

    total_frequency = {}
    for word in words:
        total_frequency[word] = total_frequency.get(word, 0) + 1

    age = 0
    words_frequency = 0
    for word, frequency in total_frequency.items():
        if word in age_lex:
            words_frequency += frequency
            age += frequency * age_lex[word]
    if words_frequency != 0:
        age = age / words_frequency + age_intercept
    return age


def getUserData(filename):
    global Value, Result
    global Age
    for filename in os.listdir('/Users/tejaswini/PycharmProjects/extractData/UserText'):
        if filename.endswith('.txt'):
            file = open('/Users/tejaswini/PycharmProjects/extractData/UserText/'+filename, "r")
            data = file.read()
            data = re.sub(r'[^\w\s]', '', data)
            Gender = get_gender(data)
            Age = get_age(data)
            if Gender > 0:
                Value = "Female"
            elif Gender < 0:
                Value = "Male"
            Result = [filename.split('_text')[0], Value, Age]

        with open('predictions.csv', 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(Result)



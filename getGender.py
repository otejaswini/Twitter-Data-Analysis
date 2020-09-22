#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


with open("predictions.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    num_rows = 0
    num_users = 0
    num_female = 0
    for lines in csv_reader:
        """if float(lines['Age']) < 21:
            print(lines['Age'])
            num_users +=1
            for row in open('/Users/tejaswini/PycharmProjects/Lexica/CSV_FILES/'+lines['Username']+"_tweets.csv"):
                num_rows += 1"""
        """ if 21 <= float(lines['Age']) < 31 :
            print(lines['Age'])
            num_users += 1
            for row in open('/Users/tejaswini/PycharmProjects/Lexica/CSV_FILES/' + lines['Username'] + "_tweets.csv"):
                num_rows += 1 """
        """if 31 <= float(lines['Age']) < 41 :
            print(lines['Age'])
            num_users += 1
            for row in open('/Users/tejaswini/PycharmProjects/Lexica/CSV_FILES/' + lines['Username'] + "_tweets.csv"):
                num_rows += 1"""
        """if 41 <= float(lines['Age']) < 51:
            print(lines['Age'])
            num_users += 1
            for row in open('/Users/tejaswini/PycharmProjects/Lexica/CSV_FILES/' + lines['Username'] + "_tweets.csv"):
                num_rows += 1"""
        """ if 51 <= float(lines['Age']) < 61:
            print(lines['Age'])
            num_users += 1
            for row in open('/Users/tejaswini/PycharmProjects/Lexica/CSV_FILES/' + lines['Username'] + "_tweets.csv"):
                num_rows += 1"""
        if float(lines['Age']) > 61:
            num_users += 1
            for row in open('CSV_FILES/' + lines['Filename'] + "_tweets.csv"):
                num_rows += 1
    print(num_rows)
    print(num_users)
    print(num_rows/num_users)


# In[ ]:





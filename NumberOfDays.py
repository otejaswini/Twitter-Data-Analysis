import csv
import pandas as pd
import numpy as np
import os
from datetime import datetime
firstDate = datetime.now().date()
lastDate = datetime.strptime('01/01/1800','%d/%m/%Y').date()
for filename in os.listdir('/Users/tejaswini/PycharmProjects/extractData/CSV_FILES'):
    if filename.endswith('.csv'):
        num_rows = 0
        with open('/Users/tejaswini/PycharmProjects/extractData/CSV_FILES/'+filename) as f:
            cr = csv.reader(f)
            for row in cr:
                num_rows += 1
        print(num_rows)
        data = pd.read_csv('/Users/tejaswini/PycharmProjects/extractData/CSV_FILES/'+filename)
        numpyArray = np.array(data)
        d = datetime.strptime(numpyArray[num_rows - 2, 1], "%Y-%m-%d %H:%M:%S")
        d1 = datetime.strptime(numpyArray[0, 1], "%Y-%m-%d %H:%M:%S")
        if firstDate > d.date():
            firstDate = d.date()
        if lastDate < d1.date():
            lastDate = d1.date()
        delta = abs((d1 - d).days)
        Result = [filename.split('_tweet')[0], delta]
        print(Result)
        with open('Numberofdays.csv', 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(Result)
print(firstDate)
print(lastDate)
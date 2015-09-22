# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:47:19 2015

@author: m01i795
"""

## Parameters
train='C:/Users/m01i795/iPython Notebooks/Kaggle/Input/train.csv'
test='C:/Users/m01i795/iPython Notebooks/Kaggle/Input/test.csv'

D = 2 ** 24             # number of weights to use

## Importing packages

from sklearn import linear_model
import pandas as pd
import csv
from datetime import datetime

## Initiate by reading first line

with open(train, 'rb') as f:
    reader = csv.reader(f)
    coltxt = next(reader)   #gets the first line

coltxt=coltxt[1:] # Removing the first element, as I don't need ID
coltxt=coltxt[:len(coltxt)-1] # Removing the last element

## Putting this into a data-frame

features_train = pd.DataFrame(columns = coltxt)
features_test = pd.DataFrame(columns = coltxt)
labels_train = pd.DataFrame(columns = ['target'])
labels_test = pd.DataFrame(columns = ['target'])

## Help generator for getting data from CVS and encoding

def data(path, D):
    ''' GENERATOR: Apply hash-trick to the original csv row
                   and for simplicity, we one-hot-encode everything

        INPUT:
            path: path to training or testing file
            D: the max index that we can hash to

        YIELDS:
            ID: id of the instance, mainly useless
            x: a list of hashed and one-hot-encoded 'indices'
               we only need the index since all values are either 0 or 1
            y: y = 1 if we have a click, else we have y = 0
    '''

    for t, row in enumerate(DictReader(open(path), delimiter=',')):
      
        try:
            ID=row['ID']
            del row['ID']
        except:
            pass
        # process clicks
        y = 0.
        target='target'#'IsClick' 
        if target in row:
            if row[target] == '1':
                y = 1.
            del row[target]


        # build x
        x = []
        for key in row:
            value = row[key]

            # one-hot encode everything with hash trick
            index = abs(hash(key + '_' + value)) % D
            x.append(index)

        yield ID,  x, y

## Reading the data

count = 0

for t, x, y in data(train, D):  # data is a generator    
    features_train.loc[len(features_train)]=x
    labels_train.loc[len(labels_train)]=y
    count+=1
    if count%15000==0:
        print('%s\tencountered: %d\tcurrent' % (datetime.now(), count))

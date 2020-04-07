#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 17:48:56 2017

@author: harsh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

X_train = train.drop('target',1) 
y_train = train.target

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit(X_train,y_train).predict(test)

sub3 = pd.DataFrame({'id':test.id, 'target':0.5})
sub3 = sub3[['id','target']]
sub3.to_csv('sub.csv', index=False)

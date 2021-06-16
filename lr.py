# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:37:41 2021

@author: Fasih
"""

# imports
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
# generate random data-set

df = pd.read_excel (r'H:\\population.xlsx')
#print (df)
x=df.iloc[1:61, 1:2]

y=df.iloc[1:61, 2:3]
p=df.iloc[1:11, 3:4]
print(p)
# sckit-learn implementation

# Model initialization
regression_model = LinearRegression()
# Fit the data(train the model)
regression_model.fit(x, y)
# Predict

y_predicted = regression_model.predict(p)
print(y_predicted)

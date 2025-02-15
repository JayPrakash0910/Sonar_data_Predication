# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bJB45zbaAhjxTdpejh6b4LuClWFC3c8g
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""DATA COLLECTION AND DATA PROCING"""

Sonar_data=pd.read_csv('/content/Copy of sonar data.csv',header=None)
Sonar_data.head()

# umber of row and column
Sonar_data.shape
Sonar_data.describe()#describe statistical measures of the data

Sonar_data[60].value_counts()

Sonar_data.groupby(60).mean()

"""SEPARAING DATA AND LABELS"""

X = Sonar_data.drop(columns=60, axis=1)
Y = Sonar_data[60]

print(X)
print(Y)

"""TRAINING AND TEST DATA"""

X_train, X_test,Y_train, Y_test=train_test_split(X,Y,test_size=0.1, stratify=Y, random_state=1)
print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

"""MODEL TRANING --> LOGISTIC REGRESSION"""

model=LogisticRegression()

#Traininng the logistic regression model with training data
model.fit(X_train, Y_train)

"""MODEL EVALUTION"""

#ACCURECY ON TRAINING DATA
X_test_prediction=model.predict(X_train)
test_data_accuracy=accuracy_score(X_test_prediction,Y_train)
print("Accuracy on test data : ",test_data_accuracy)

"""MAKING ON TEST DATA SYSTEM"""

#  rock data :
input_data=(0.0286,	0.0453,	0.0277,	0.0174,	0.0384,	0.099,	0.1201,	0.1833,	0.2105,	0.3039,	0.2988,	0.425,	0.6343,	0.8198,	1,	0.9988,	0.9508,	0.9025,	0.7234,	0.5122,	0.2074,	0.3985,	0.589,	0.2872,	0.2043,	0.5782,	0.5389,	0.375,	0.3411,	0.5067,	0.558,	0.4778,	0.3299,	0.2198,	0.1407,	0.2856,	0.3807,	0.4158,	0.4054,	0.3296,	0.2707,	0.265,	0.0723,	0.1238,	0.1192,	0.1089,	0.0623,	0.0494,	0.0264,	0.0081,	0.0104,	0.0045,	0.0014,	0.0038,	0.0013,	0.0089,	0.0057,	0.0027,	0.0051,	0.0062)
# mines data
input_data = (0.0307,	0.0523,	0.0653,	0.0521,	0.0611,	0.0577,	0.0665,	0.0664,	0.146,	0.2792,	0.3877,	0.4992,	0.4981,	0.4972,	0.5607,	0.7339,	0.823,	0.9173,	0.9975,	0.9911,	0.824,	0.6498,	0.598,	0.4862,	0.315,	0.1543,	0.0989,	0.0284,	0.1008,	0.2636,	0.2694,	0.293,	0.2925,	0.3998,	0.366,	0.3172,	0.4609,	0.4374,	0.182,	0.3376,	0.6202,	0.4448,	0.1863,	0.142,	0.0589,	0.0576,	0.0672,	0.0269,	0.0245,	0.019,	0.0063,	0.0321,	0.0189,	0.0137,	0.0277,	0.0152,	0.0052,	0.0121,	0.0124,	0.0055)
# changing the input data to an numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape the np aray as we are prediction for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction=='R'):
  print("the objecct is a Rock")
else:
  print("the objecct is a Mines")


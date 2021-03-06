# -*- coding: utf-8 -*-
"""GRIP_Feb22.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yTFiN06BR0ph7djocUsaF7fARdSrXb4-

Name : Markanti Ratan Reddy

Task 1: Prediction using supervised ML

The Spark Foundation GRIPFEB22 

Predict the percentage of students based on the no. of study hours.

#### In this task we will predict the percentage of marks that a student is expected to score based upon the no. of hours that they studied. This is sample linear regression task as it involves two variables.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline

url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")

s_data.head(10)

s_data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.show()

X = s_data.iloc[:, :-1].values  
y = s_data.iloc[:, 1].values

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                            test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 

print("Training complete.")

line = regressor.coef_*X+regressor.intercept_


plt.scatter(X, y)
plt.plot(X, line);
plt.show()

print(X_test)
y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df

hours = 9.25
own_pred = regressor.predict([[hours]])
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))

from sklearn import metrics  
print('Mean Absolute Error:', 
      metrics.mean_absolute_error(y_test, y_pred))
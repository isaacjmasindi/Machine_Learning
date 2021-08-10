import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#training set of the telsa price over the years 
# x_train is the years from 2012 to 2020
x_train =[[2012], [2013], [2014], [2015], [2016], [2017], [2018], [2019], [2020]]

#y_train is the stock price close of telsa at the end of each year
y_train =[[6.77], [24.08], [58.48], [72.00], [91.73], [157.27], [231.56], [457.66], [705.67]]

#this will call the polynomial fuction 
poly=PolynomialFeatures(degree=2)

#this transforms the data into quadratic data 
X_train_ploy = poly.fit_transform(x_train)

#declares the quadratic regressor
ploy_reg=LinearRegression()

#this will  fit the data
ploy_reg.fit(X_train_ploy,y_train)

plt.grid(True)

plt.scatter(x_train, y_train, color="red")

plt.plot(x_train, ploy_reg.predict(poly.fit_transform(x_train)),color="blue")

plt.title("Polynomial Regression")

plt.xlabel("Years")

plt.ylabel("Tesla share price")

plt.show()



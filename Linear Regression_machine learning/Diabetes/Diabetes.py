import matplotlib.pyplot as plt
import numpy as np 
from sklearn.datasets import load_diabetes

#This is the Linear regression function that will return M and b
def Linear_Regression(X,y):
    #the mean of the x coordinates
    x_mean=np.mean(X)
    
    #the mean of the y coordinates
    y_mean=np.mean(y)
    
    #the value of the slope 
    m=np.dot(np.transpose(X-x_mean),y-y_mean)/np.dot(np.transpose(X-x_mean),X-x_mean)
    
    #the value of the Intercept
    b=y_mean-m*x_mean
    
    return [m,b]

#loading diebetes data
Diabetes_data=load_diabetes()


X = Diabetes_data.data[:, np.newaxis, 2]

dX_train = X[:-20]

dy_train = Diabetes_data.target[:-20]

dX_test = X[-20:]

dy_test = Diabetes_data.target[-20:]


#the linear regression fuction is called to turn the values of the slope and intercept 
m,b=Linear_Regression(dX_train,dy_train)

#the linear regression formula is set 
Dependent_variable_Y=b+m*X


#the data is plotted onto the graph
plt.scatter(dX_train,dy_train,c='r',label="Train")

plt.scatter(dX_test,dy_test,c='g',label="Test")

plt.plot(X,Dependent_variable_Y,c='b')

plt.legend()

plt.show()
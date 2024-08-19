# Implementation of Univariate Linear Regression
## AIM:
To implement univariate Linear Regression to fit a straight line using least squares.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Jupyter notebook

## Algorithm
1. Get the independent variable X and dependent variable Y.
2. Calculate the mean of the X -values and the mean of the Y -values.
3. Find the slope m of the line of best fit using the formula. 
<img width="231" alt="image" src="https://user-images.githubusercontent.com/93026020/192078527-b3b5ee3e-992f-46c4-865b-3b7ce4ac54ad.png">
4. Compute the y -intercept of the line by using the formula:
<img width="148" alt="image" src="https://user-images.githubusercontent.com/93026020/192078545-79d70b90-7e9d-4b85-9f8b-9d7548a4c5a4.png">
5. Use the slope m and the y -intercept to form the equation of the line.
6. Obtain the straight line equation Y=mX+b and plot the scatterplot.

## Program:
```
/*
Program to implement univariate Linear Regression to fit a straight line using least squares.
Developed by: Shri Sai Aravind. R
RegisterNumber:  212223040197
*/
```
```py
import numpy as np
import matplotlib.pyplot as plt

x = np.array(eval(input()))
y = np.array(eval(input()))

mean_x = np.mean(x)
mean_y = np.mean(y)

num = 0
den = 0

for i in range(len(x)):
    num += (x[i] - mean_x)*(y[i] - mean_y)
    den+=(x[i] - mean_x)**2

m = num/den

c = mean_y - (m*mean_x)
Y_pred = m*x + c

plt.scatter(x,y, color = "green", label = "Data Points")
plt.plot(x,Y_pred, color = "red", label = "Regression line")
plt.legend()
plt.show()
```

## Output:
![image](https://github.com/user-attachments/assets/27a09a50-8ba7-4d6c-9992-305083934110)

![image](https://github.com/user-attachments/assets/b97b85e4-a5d4-4371-8b69-b5f23943dc5e)



## Result:
Thus the univariate Linear Regression was implemented to fit a straight line using least squares using python programming.

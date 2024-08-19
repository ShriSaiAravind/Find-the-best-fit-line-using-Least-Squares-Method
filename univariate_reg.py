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
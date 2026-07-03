'''
. Create x values: 0 to 10
2. Create y = x^2
3. Plot line
4. Add title "Quadratic Function"
5. Add x and y labels
6. Show grid
7. Display plot
'''
import matplotlib.pyplot as plt
import numpy as np
xaxis = np.array([0,1,2,3,4,5,6,7,8,9,10])
yaxis = np.square(xaxis)
plt.title("Quadratic Function")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(visible=True)
plt.plot(xaxis,yaxis)
plt.show()

'''
1. Plot y = x
2. Plot y = x^2
3. Plot y = x^3
4. Add legend (y=x, y=x^2, y=x^3)
5. Customize line colors and styles
6. Add title and labels
'''

y=xaxis 
cubed_y=np.power(xaxis,3)
plt.plot(xaxis, y, label="y=x", color='red', linestyle='-', linewidth=2)
plt.plot(xaxis, yaxis, label="y=x^2", color='blue', linestyle='--', linewidth=2)
plt.plot(xaxis, cubed_y, label="y=x^3", color='green', linestyle=':', linewidth=2)
plt.title("Exercise 2")
plt.legend()
plt.show()

'''
1. Generate random x, y data (100 points)
2. Create scatter plot
3. Color points by z values
4. Add colorbar
5. Set marker size
6. Add title and labels
'''
 


import matplotlib.pyplot as plt
import numpy as np
import math


# Function to calculate the Taylor approximation
def taylor_approximation(x, epsilon):
    result = 0
    term = 1
    n = 0
    while abs(term) > epsilon:
        result += term
        n += 1
        term *= -x / n
    return result


# Predefined parameters
Xнач = -10
Xкон = 10
dx = 0.1
ε = 0.001
b = 1

# Create the x values
x_values = np.arange(Xнач, Xкон, dx)

# Calculate the y values for the two functions
y_values = [taylor_approximation(x, ε) for x in x_values]
z_values = [math.exp(-x) + b for x in x_values]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values,
         y_values,
         label='y(x) = Taylor series approximation of e^-x',
         color='blue')
plt.plot(x_values, z_values, label='z(x) = e^-x + b', color='red')
plt.xlabel('x')
plt.ylabel('y, z')
plt.title('Plot of y(x) and z(x)')
plt.legend()
plt.grid(True)
plt.show()

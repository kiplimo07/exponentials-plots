import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the function to be integrated
def integrand(t, zt):
    return np.exp(zt)

# Define a range of zt values
zt_values = np.linspace(0, 10, 100)  # Adjust the range and number of points as needed

# Initialize lists to store the results
integral_values = []

# Integrate the function for each zt value
for zt in zt_values:
    result, _ = quad(integrand, 0, np.inf, args=(zt,))
    integral_values.append(result)

# Create a plot
plt.plot(zt_values, integral_values)
plt.xlabel('zt')
plt.ylabel('Integral Value')
plt.title('Integral of Exp(zt)')
plt.grid(True)
plt.show()

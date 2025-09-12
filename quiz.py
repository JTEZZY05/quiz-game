import matplotlib.pyplot as plt
import numpy as np

A = np.array([[2, 1],
              [1, 3]])

# Original unit vectors
vectors = np.array([[1, 0], [0, 1]]).T  # columns are vectors

# Apply transformation
transformed = A @ vectors

origin = np.zeros((2,2))  # origin points for arrows

plt.quiver(*origin, vectors[0], vectors[1], color='blue', scale=1, scale_units='xy', angles='xy', label='Original')
plt.quiver(*origin, transformed[0], transformed[1], color='red', scale=1, scale_units='xy', angles='xy', label='Transformed')

plt.xlim(-1,5)
plt.ylim(-1,5)
plt.grid()
plt.legend()
plt.show()

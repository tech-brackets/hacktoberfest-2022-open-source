import numpy as np

"""Matrix Operation"""

a = [[5,2,5],[19,2,6]]
b = [[4,21,5],[2,7,11]]

c = [[5,2,5],[5,6,2]]
d = [[4,5],[2,6],[2,1]]
# Addition
print(np.add(a,b))

# Multiplication
print(np.multiply(a,b))

# Dot Multiplication
print(np.dot(c,d))
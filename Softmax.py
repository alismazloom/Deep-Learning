import numpy as np
a = np.array([1,2,3,4])
b = np.array([np.exp(a)/np.sum(np.exp(a))])
print(a)
print(b)
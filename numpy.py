
"""
NumPy – Complete Feature Overview

This file covers almost all core NumPy features required for AI/ML foundations.
"""

import numpy as np


# 1. ARRAY CREATION


a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

zeros = np.zeros((2, 3))
ones = np.ones((3, 3))
empty = np.empty((2, 2))

range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)


# 2. DATA TYPES


arr_int = np.array([1, 2, 3], dtype=int)
arr_float = np.array([1, 2, 3], dtype=float)
arr_bool = np.array([True, False])

arr_int.astype(float)


# 3. ARRAY ATTRIBUTES


arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.ndim
arr.shape
arr.size
arr.dtype
arr.itemsize


# 4. INDEXING & SLICING


arr = np.array([10, 20, 30, 40, 50])

arr[0]
arr[-1]
arr[1:4]
arr[:3]
arr[::2]

matrix = np.array([[1, 2], [3, 4]])
matrix[0, 1]


# 5. BOOLEAN INDEXING


arr = np.array([5, 10, 15, 20])

mask = arr > 10
filtered = arr[mask]

# 6. FANCY INDEXING


arr = np.array([10, 20, 30, 40])
arr[[0, 2]]

# 7. RESHAPING


arr = np.array([1, 2, 3, 4, 5, 6])

arr.reshape(2, 3)
arr.reshape(-1, 2)
arr.flatten()
arr.ravel()

# 8. STACKING & SPLITTING

a = np.array([1, 2])
b = np.array([3, 4])

np.vstack((a, b))
np.hstack((a, b))
np.split(np.array([1, 2, 3, 4]), 2)

# 9. COPY VS VIEW

a = np.array([1, 2, 3])
b = a.view()
c = a.copy()

b[0] = 99      # affects a
c[1] = 100     # does NOT affect a

# 10. MATHEMATICAL OPERATIONS

arr = np.array([1, 2, 3])

arr + 5
arr - 1
arr * 2
arr / 2
arr ** 2

# 11. UNIVERSAL FUNCTIONS (UFUNCS)

np.sqrt(arr)
np.exp(arr)
np.log(arr)
np.sin(arr)
np.cos(arr)

# 12. AGGREGATIONS

arr = np.array([1, 2, 3, 4])

arr.sum()
arr.mean()
arr.min()
arr.max()
arr.std()
arr.var()


# 13. AXIS OPERATIONS

matrix = np.array([[1, 2, 3], [4, 5, 6]])

matrix.sum(axis=0)   # column-wise
matrix.sum(axis=1)   # row-wise

# 14. BROADCASTING

arr = np.array([1, 2, 3])
arr + np.array([10])

matrix + 5

# 15. RANDOM MODULE

np.random.rand(3)
np.random.randn(3)
np.random.randint(0, 10, size=5)

np.random.seed(42)

# 16. SORTING & SEARCHING

arr = np.array([4, 1, 3, 2])

np.sort(arr)
np.argsort(arr)
np.where(arr > 2)

# 17. LINEAR ALGEBRA

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.dot(A, B)
A @ B
np.linalg.det(A)
np.linalg.inv(A)
np.linalg.eig(A)

# 18. STATISTICS

arr = np.array([1, 2, 3, 4, 5])

np.median(arr)
np.percentile(arr, 50)
np.corrcoef(arr, arr)

# 19. FILE I/O

np.save("array.npy", arr)
loaded = np.load("array.npy")

np.savetxt("array.txt", arr)
np.loadtxt("array.txt")

# 20. MASKED / NAN HANDLING

arr = np.array([1, 2, np.nan, 4])

np.isnan(arr)
np.nanmean(arr)

# ==============================
# END OF NUMPY CORE FEATURES
# ==============================
#this file covers near to 100% of numpy features

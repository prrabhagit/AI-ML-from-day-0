import numpy as np

# ---------- ARRAY CREATION ----------
a = np.array([1, 2, 3])              # 1D array
b = np.array([[1, 2], [3, 4]])       # 2D array (matrix)
c = np.zeros((2, 3))                 # Array filled with zeros
d = np.ones((3, 2))                  # Array filled with ones
e = np.full((2, 2), 7)               # Array filled with a constant value
f = np.eye(3)                        # Identity matrix
g = np.arange(0, 10, 2)              # Values from 0 to 8 with step 2
h = np.linspace(0, 1, 5)             # 5 evenly spaced values between 0 and 1
i = np.random.rand(3, 3)             # Random values (0 to 1)
j = np.random.randn(2, 2)            # Random values (normal distribution)
k = np.random.randint(1, 10, (3, 3)) # Random integers between 1 and 9

# ---------- ARRAY PROPERTIES ----------
a.shape      # Shape of array
b.ndim       # Number of dimensions
b.size       # Total number of elements
b.dtype      # Data type of elements
b.T          # Transpose of matrix

# ---------- RESHAPING ----------
b.reshape(4, 1)   # Reshape without changing data
b.flatten()       # Copy and flatten to 1D
b.ravel()         # View and flatten to 1D

# ---------- ELEMENT-WISE OPERATIONS ----------
a + 2             # Add scalar to each element
a * 3             # Multiply each element
a + np.array([4, 5, 6])  # Element-wise addition
a ** 2            # Power
np.sqrt(a)        # Square root
np.exp(a)         # Exponential
np.log(a)         # Natural log

# ---------- AGGREGATION ----------
np.sum(a)         # Sum of elements
np.mean(a)        # Mean
np.median(a)      # Median
np.std(a)         # Standard deviation
np.var(a)         # Variance
np.min(a)         # Minimum
np.max(a)         # Maximum
np.argmin(a)      # Index of minimum
np.argmax(a)      # Index of maximum

# ---------- INDEXING & SLICING ----------
b[0, 1]           # Element at row 0, column 1
b[:, 0]           # All rows, first column
b[1:]             # Rows from index 1 onward
b[b > 2]          # Boolean filtering

x = np.array([1, 2, 3, 4, 5])
x[x % 2 == 0]     # Select even numbers

# ---------- MATRIX OPERATIONS ----------
m = np.array([[1, 2], [3, 4]])
n = np.array([[5, 6], [7, 8]])
m + n             # Matrix addition
m - n             # Matrix subtraction
m * n             # Element-wise multiplication
m @ n             # Matrix multiplication
np.dot(m, n)      # Dot product

# ---------- STACKING & SPLITTING ----------
np.concatenate([a, g])   # Join arrays
np.vstack([m, n])        # Vertical stack
np.hstack([m, n])        # Horizontal stack
np.split(g, 5)           # Split into equal parts

# ---------- LOGICAL ----------
np.where(a > 1)    # Indices where condition is true
np.any(a > 2)      # True if any condition is true
np.all(a > 0)      # True if all conditions are true

# ---------- SORTING ----------
u = np.array([3, 1, 2])
np.sort(u)         # Sorted array
np.argsort(u)      # Indices of sorted order

# ---------- UNIQUE ----------
p = np.array([1, 2, 2, 3])
np.unique(p, return_counts=True)  # Unique values and counts

# ---------- CLIPPING ----------
np.clip(a, 1, 2)   # Limit values between 1 and 2

# ---------- AXIS OPERATIONS ----------
q = np.array([[1, 2, 3], [4, 5, 6]])
np.sum(q, axis=0)  # Column-wise sum
np.sum(q, axis=1)  # Row-wise sum

# ---------- BROADCASTING ----------
r = np.array([1, 2, 3])
s = np.array([[1], [2], [3]])
r + s              # Broadcasting addition

# ---------- LINEAR ALGEBRA ----------
t = np.array([[1, 2], [3, 4]], dtype=float)
np.linalg.det(t)   # Determinant
np.linalg.inv(t)   # Inverse
np.linalg.eig(t)   # Eigenvalues and eigenvectors

# ---------- FILE I/O ----------
np.save("array.npy", a)     # Save binary file
np.load("array.npy")        # Load binary file
np.savetxt("array.txt", a)  # Save text file
np.loadtxt("array.txt")     # Load text file

# ADVANCED 
np.vectorize(lambda x: x * 2)(a)   # Vectorized function
np.meshgrid(np.arange(3), np.arange(3))  # Coordinate matrices
np.cumsum(a)        # Cumulative sum
np.cumprod(a)       # Cumulative product
np.diff(a)          # Difference between elements

# ---------- NaN & INF ----------
np.isnan(np.array([1, np.nan, 3]))     # Check NaN
np.isfinite(np.array([1, np.inf, 3]))  # Check finite values

# ---------- COPYING ----------
np.copy(a)          # Deep copy
a.view()            # Shallow copy

# ---------- BROADCAST SHAPE ----------
np.broadcast_to(a, (3, 3))  # Broadcast array to new shape

import numpy as np
from scipy.sparse import csr_matrix

# Step 1: Create a dense NumPy matrix (with many zeros)
dense_matrix = np.array([
    [4, 0, 0, 0, 1],
    [0, 3, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 3, 0],
    [1, 0, 0, 0, 4]
])
print("Dense matrix:")
print(dense_matrix)
# Step 2: Convert the dense matrix to a sparse matrix using CSR format
sparse_matrix = csr_matrix(dense_matrix)
# Step 3: Print the internal structure of the CSR matrix
# CSR stores data in three arrays: data, indices, and indptr
print("\nSparse matrix (CSR format):")
print(sparse_matrix)
# Step 4: Show the data structure of the sparse matrix
print("\nCSR Matrix internal structure:")
print("Data (non-zero values):", sparse_matrix.data)
print("Indices (column indices of data):", sparse_matrix.indices)
print("Index pointer (row start points):", sparse_matrix.indptr)
# Step 5: Solve the linear system Ax = b (for educational purposes)
b = np.array([1, 2, 3, 4, 5])
from scipy.sparse.linalg import spsolve
x = spsolve(sparse_matrix, b)
print("\nSolution to Ax = b:")
print("x =", x)

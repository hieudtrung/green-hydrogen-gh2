import numpy as np

l = [[1,2,3], [4,5,6]]
mat = np.array(l)

print(mat.shape)

for i in range(10):
    weights = np.random.randn(3,1)
    print(f"Vectorh {i}-th")
    vec = np.matmul(mat, weights)
    print(vec, "\n")
import numpy as np

# Data points
X = np.array([1, 2, 3, 8, 9, 10])
n = len(X)

# Initialize parameters
mu1, mu2 = 2, 9
var1 = var2 = 1
pi1 = pi2 = 0.5

# Gaussian function
def gauss(x, mu, var):
    return np.exp(-(x-mu)**2/(2*var)) / np.sqrt(2*np.pi*var)

# EM Algorithm
for _ in range(10):
    # E-step
    r1 = pi1 * gauss(X, mu1, var1)
    r2 = pi2 * gauss(X, mu2, var2)
    sum_r = r1 + r2
    r1, r2 = r1/sum_r, r2/sum_r

    # M-step
    mu1 = np.sum(r1 * X) / np.sum(r1)
    mu2 = np.sum(r2 * X) / np.sum(r2)
    pi1 = np.mean(r1)
    pi2 = np.mean(r2)

# Cluster assignment
clusters = [1 if r1[i] > r2[i] else 2 for i in range(n)]
print("Clusters:", clusters)

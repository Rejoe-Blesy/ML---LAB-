# Single Layer Perceptron

import numpy as np

# Input data (AND logic)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0, 0, 0, 1])

# Initialize weights and bias
w = np.zeros(2)
b = 0
lr = 0.1

# Training
for _ in range(10):
    for i in range(len(X)):
        y_pred = 1 if np.dot(X[i], w) + b >= 0 else 0
        w += lr * (y[i] - y_pred) * X[i]
        b += lr * (y[i] - y_pred)

# Testing
for x in X:
    print(x, "->", 1 if np.dot(x, w) + b >= 0 else 0)

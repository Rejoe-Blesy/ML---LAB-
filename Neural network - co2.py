import numpy as np

# Dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[1],[1]])

# Initialize weights
np.random.seed(1)
W1 = np.random.rand(2,2)
W2 = np.random.rand(2,1)
lr = 0.5

# Sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Training using backpropagation
for _ in range(5000):
    h = sigmoid(np.dot(X, W1))
    o = sigmoid(np.dot(h, W2))
    W2 += lr * np.dot(h.T, (y - o))
    W1 += lr * np.dot(X.T, np.dot((y - o), W2.T))

# Output
print("Predicted Output:")
print(np.round(o))

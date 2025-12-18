import math

# Training data
X = [[1,1], [1,0], [0,1], [0,0]]
y = [1, 1, 0, 0]   # Class labels

# Separate data by class
def separate(X, y):
    data = {0:[], 1:[]}
    for xi, yi in zip(X, y):
        data[yi].append(xi)
    return data

data = separate(X, y)

# Prior probabilities
priors = {c: len(data[c])/len(X) for c in data}

# Likelihood with Laplace smoothing
def likelihood(x, cls):
    prob = 1
    for i in range(len(x)):
        count = sum(row[i] == x[i] for row in data[cls])
        prob *= (count + 1) / (len(data[cls]) + 2)
    return prob

# Prediction
x_test = [1,0]
post = {c: priors[c] * likelihood(x_test, c) for c in data}

print("Predicted Class:", max(post, key=post.get))

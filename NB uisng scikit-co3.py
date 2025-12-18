# Naïve Bayes Classification (Binary features)

# Training data
X = [[1,1],[1,0],[0,1],[0,0]]
y = [1,1,0,0]   # Class labels

# Separate data by class
data = {0:[], 1:[]}
for xi, yi in zip(X, y):
    data[yi].append(xi)

# Prior probabilities
P = {c: len(data[c])/len(X) for c in data}

# Likelihood with Laplace smoothing
def likelihood(x, c):
    prob = 1
    for i in range(len(x)):
        count = sum(row[i] == x[i] for row in data[c])
        prob *= (count + 1) / (len(data[c]) + 2)
    return prob

# Test sample
x_test = [1,0]

# Posterior probability
post = {c: P[c] * likelihood(x_test, c) for c in data}

# Classification result
print("Predicted Class:", max(post, key=post.get))



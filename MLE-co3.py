import numpy as np

# Observed data (Bernoulli trials)
data = np.array([1, 0, 1, 1, 0, 1, 1])

# MLE for probability p
p_mle = np.sum(data) / len(data)

print("MLE of p:", p_mle)

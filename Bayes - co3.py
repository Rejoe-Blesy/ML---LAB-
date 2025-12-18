# Bayes Theorem for Classification

# Prior probabilities
P_C1 = 0.6   # Class 1
P_C2 = 0.4   # Class 2

# Likelihoods
P_X_C1 = 0.5
P_X_C2 = 0.2

# Evidence
P_X = P_X_C1*P_C1 + P_X_C2*P_C2

# Posterior probabilities
P_C1_X = (P_X_C1 * P_C1) / P_X
P_C2_X = (P_X_C2 * P_C2) / P_X

# Classification
if P_C1_X > P_C2_X:
    print("Classified as Class 1")
else:
    print("Classified as Class 2")

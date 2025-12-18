import random

# Sample dataset (features only for demo)
features = ['F1','F2','F3','F4']
pop = [[random.randint(0,1) for _ in range(4)] for _ in range(6)]

# Fitness = number of selected features (demo purpose)
def fitness(chrom):
    return sum(chrom)

# Genetic Algorithm
for _ in range(10):
    pop = sorted(pop, key=fitness, reverse=True)  # Selection
    p1, p2 = pop[0], pop[1]
    c1 = p1[:2] + p2[2:]                           # Crossover
    c2 = p2[:2] + p1[2:]
    c1[random.randint(0,3)] ^= 1                   # Mutation
    c2[random.randint(0,3)] ^= 1
    pop = pop[:4] + [c1, c2]

# Best feature subset
best = max(pop, key=fitness)
print("Selected Features:", best)

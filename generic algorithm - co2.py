import random

# Objective function
def fitness(x):
    return x*x

# Initial population
pop = [random.randint(-10,10) for _ in range(6)]

# Genetic Algorithm
for _ in range(20):
    pop = sorted(pop, key=fitness)          # Selection
    pop = pop[:3]                           # Best parents
    pop += [pop[0]+random.randint(-1,1),    # Crossover + Mutation
            pop[1]+random.randint(-1,1),
            pop[2]+random.randint(-1,1)]

# Best solution
best = min(pop, key=fitness)
print("Best x:", best, "Minimum value:", fitness(best))

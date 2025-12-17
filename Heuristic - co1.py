# Heuristic Search in Hypothesis Space

hypotheses = ['h1','h2','h3','h4']
scores = {'h1':3, 'h2':1, 'h3':0, 'h4':2}   # heuristic values

best = hypotheses[0]
for h in hypotheses:
    if scores[h] < scores[best]:   # lower score = better hypothesis
        best = h

print("Best Hypothesis:", best)

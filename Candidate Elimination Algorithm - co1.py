# Candidate Elimination Algorithm

data = [
 ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
 ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
 ['Rainy','Cold','High','Strong','Warm','Change','No'],
 ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

S = ['0'] * 6
G = [['?'] * 6]

for ex in data:
    if ex[-1] == 'Yes':
        for i in range(6):
            S[i] = ex[i] if S[i] in ['0', ex[i]] else '?'
        G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(6))]
    else:
        G = [[g[i] if g[i] != ex[i] else S[i] for i in range(6)] for g in G]

print("Specific Hypothesis:", S)
print("General Hypotheses:", G)

# Inductive Bias using Find-S Algorithm (simple example)

data = [
 ['A','B','C','Yes'],
 ['A','B','C','Yes'],
 ['A','D','C','No']
]

hypothesis = ['0','0','0']   # most specific hypothesis (bias)

for ex in data:
    if ex[-1] == 'Yes':
        for i in range(3):
            if hypothesis[i] == '0':
                hypothesis[i] = ex[i]
            elif hypothesis[i] != ex[i]:
                hypothesis[i] = '?'

print("Final Hypothesis:", hypothesis)

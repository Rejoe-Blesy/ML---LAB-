data = [
 ['Sunny','Warm','Strong','Warm','Same','Yes'],
 ['Sunny','Warm','Strong','Warm','Same','Yes'],
 ['Rainy','Cold','Weak','Cool','Change','No']
]

hypothesis = ['0'] * 5

for example in data:
    if example[-1] == 'Yes':
        for i in range(5):
            hypothesis[i] = example[i] if hypothesis[i] in ['0', example[i]] else '?'

print("Final Hypothesis:", hypothesis)

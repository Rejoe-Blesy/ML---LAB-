import math

data = [
 ['A','X','Yes'],
 ['A','Y','Yes'],
 ['B','X','No'],
 ['B','Y','No']
]

def entropy(data):
    p = sum(1 for d in data if d[-1]=='Yes')
    n = len(data) - p
    if p==0 or n==0: return 0
    return -p/len(data)*math.log2(p/len(data)) - n/len(data)*math.log2(n/len(data))

def information_gain(data, attr):
    total = entropy(data)
    vals = set(d[attr] for d in data)
    rem = sum((len([d for d in data if d[attr]==v])/len(data)) *
              entropy([d for d in data if d[attr]==v]) for v in vals)
    return total - rem

print("Information Gain of attribute 0:", information_gain(data,0))
print("Information Gain of attribute 1:", information_gain(data,1))

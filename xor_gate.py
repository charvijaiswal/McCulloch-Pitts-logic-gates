# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 15:00:12 2024

@author: charv
"""
'''
XOR TABLE
0   0  -->  0      
0   1  -->  1
1   0  -->  1
1   1  -->  1
'''
# Inputs
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

#weights and biases
bias = -0.5
threshold = 1
o1w2 = -2
o1w1 = 1
o2w2 = 1
o2w1 = -1

def xorFunc(x1, x2, o1w1, o1w2, o2w1, o2w2, bias, threshold):
    results = []
    o1 = []
    o2 = []
    
    for i in range(len(x1)):
        v1 = (x2[i] * o1w2) + (x1[i] * o1w1) + bias
        v2 = (x2[i] * o2w2) + (x1[i] * o2w1) + bias
        
        if v1 < 0:
            o1.append(-1)
        else:
            o1.append(1)
            
        if v2 < 0:
            o2.append(-1)
        else:
            o2.append(1)

        v3 = o2[i] + o1[i] + threshold
        
        if v3 <= 0:
            results.append(0)
        else:
            results.append(1)
        
    return results

results = xorFunc(x1, x2, o1w1, o1w2, o2w1, o2w2, bias, threshold)

print("Inputs:")
for i in range(len(x1)):
    print(f"{x1[i]}, {x2[i]}")
print("Outputs:")
print(results)



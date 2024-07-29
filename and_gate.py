# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:45:09 2024

@author: charv
"""
'''
AND TABLE
0   0  -->  0
0   1  -->  0
1   0  -->  0
1   1  -->  1
'''
#inputs
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

threshold = int(input("Enter the threshold (1 or 2): "))

#setting weights based on threshold
if threshold == 1:
    w1 = 0.5
    w2 = 0.5
elif threshold == 2:
    w1 = 1.0
    w2 = 1.0
else:
    raise ValueError("Threshold must be 1 or 2")

outputs = []
for i in range(len(x1)):
    weighted_sum = x1[i] * w1 + x2[i] * w2

    if weighted_sum >= threshold:
        outputs.append(1)
    else:
        outputs.append(0)

print("Inputs:")
for i in range(len(x1)):
    print(f"{x1[i]}, {x2[i]}")
print("Outputs:")
print(outputs)

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:01:09 2024
@author: charv
"""

'''
OR TABLE
0   0  -->  0      
0   1  -->  1
1   0  -->  1
1   1  -->  1
'''

#inputs
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

#threshold input
threshold = int(input("Enter the threshold (1 or 2): "))

#setting the weight based on threshold
if threshold == 1:
    w1 = 1
    w2 = 1
elif threshold == 2:
    w1 = 2
    w2 = 2
else:
    raise ValueError("Threshold must be 1 or 2")

# Calculate outputs based on OR logic
outputs = []
for i in range(len(x1)):
    weighted_sum = x1[i] * w1 + x2[i] * w2

    if weighted_sum >= threshold:
        outputs.append(1)
    else:
        outputs.append(0)

# Print inputs and outputs
print("Inputs:")
for i in range(len(x1)):
    print(f"{x1[i]}, {x2[i]}")
print("Outputs:")
print(outputs)








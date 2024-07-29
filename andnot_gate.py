'''
andnot gate
0  0 --> 0
0  1 --> 0
1  0 --> 1
1  1 --> 0
'''

#inputs
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]

#setting weights based on threshold
threshold =1
w1=1
w2=-1

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

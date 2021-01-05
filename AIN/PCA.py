import numpy as np

def avg(row):
    return sum(row) * 1.0 / len(row)

def dec(np_arr):
    return [el for el in np_arr]

def decm(np_mat):
    lines = [dec(arr) for arr in np_mat]
    for line in lines:
        print "\t", line

rows = [
    [4, 2, 3],
    [6, 1, 3],
    [4, 2, 5],
    [7, 8, 3]
]


x_mean = [avg(row) for row in np.array(rows).T]

print "x mean:\n\t", dec(x_mean)

X_mean = [np.array(x_mean)] * len(rows)

print"X mean: "
decm(X_mean)

# B = X - X_mean
X = np.array(rows)
B = X - X_mean


print"B: "
decm(B)

# C = B.T - B
C = np.matmul(B.T, B)
print"C: "
decm(C)
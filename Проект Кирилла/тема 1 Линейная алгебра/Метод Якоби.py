import numpy as np
# я хочу чтобы все работало
import math as mt
A = np.array([[5,-4,22],[-4,9,-11],[22,-11,5]])
V = np.eye(3)
for i in range (8):
    print(f'Номер итерации { i+1 }')
    a = abs(A[0][1])
    k = 0
    m = 1
    if a < abs(A[0][2]):
        a = abs(A[0][2])
        k = 0
        m = 2
    elif a < abs(A[1][2]):
        a = abs(A[1][2])
        k = 1
        m = 2
    print(a)
    print(k)
    print(m)
    f = (1/2)*mt.atan((2*a)/(A[k][k]-A[m][m]))
    print(f)
    H = np.eye(3)
    print('\n',H)
    H[k][k] = mt.cos(f)
    H[m][k] = mt.sin(f)
    H[k][m] = -mt.sin(f)
    H[m][m] = mt.cos(f)
    print('\n',H)
    V = np.dot(V,H)
    A = np.dot(H.T,A)
    A = np.dot(A,H)
    print('\n')
    for row in A:
        for list in row:
            print('{:.9f}'.format(list),end = ' ')
        print()
    print('\n','--'*10)

L1 = A[0][0]
L2 = A[1][1]
L3 = A[2][2]
print(L1,L2,L3)
print('\n',V)

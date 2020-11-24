import numpy as np
A = np.array([[5,-4,22],[-4,9,-11],[22,-11,5]])
W = np.array([[1],[1],[1]])
for row in W:
    for list in row:
        print('{:.9f}'.format(list),end = ' ')
print('\n','Конец 0-я итерации')
for i in range (10):
    print(f'Номер итерации { i+1 }')
    V = np.dot(A,W)
    print ('\n','Выведи мне A','\n',A,'\n')

    print ('Выведи мне V','\n')
    for row in V:
        for list in row:
            print('{:.9f}'.format(list),end = ' ')
    print('\n')
    S = abs(V[0][0])
    for I in V:
        for list in I:
            if S < abs(list):
                S = abs(list)
    print('\n','Выведи мне максимальное число','\n'*2,S,'\n')
    W = V/S
    print('\n','Выведи мне W','\n'*2,W,'\n')
    V = np.dot(A,W)
    print('\n','Выведи мне V','\n'*2,V,'\n')
    print('\n','--'*10)

import numpy as np
A = np.array([[5,-4,22],[-4,9,-11],[22,-11,5]])
W = np.array([[1/3**(1/2)],[1/3**(1/2)],[1/3**(1/2)]])
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
    P = np.dot(V.T,W)
    print ('\n'*2,'Выведи мне Р','\n'*2,P,'\n')
    E = (V[0][0]**2+V[1][0]**2+V[2][0]**2)**(1/2)
    print ('\n','Выведи мне E','\n'*2,E,'\n',)
    W = (V/E)
    print ('Выведи мне W','\n')
    for row in W:
        for list in row:
            print('{:.9f}'.format(list),end = ' ')
    print('\n','--'*10)

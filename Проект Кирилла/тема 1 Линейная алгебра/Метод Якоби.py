import numpy as np
import math as mt
A = np.array([[5,-4,22],[-4,9,-11],[22,-11,5]])#дано
V = np.eye(3)
for i in range (1):#начало цикла
    print('\n',f'Номер итерации {i+1}','\n')
    a = abs(A[0][1])# 7-17 строка проверка чисел по глав. диагонали
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
    if A[k][k] != A[m][m]:
        x = mt.atan(2*A[k][m]/(A[k][k]-A[m][m]))
    else:
        if A[k][m] >= 0:
            x = mt.pi/4
        else:
            x = -mt.pi/4
    f = 0.5*x
    print('\n')
    print('Угол поворота ','\n',f,'\n')
    H = np.eye(3)# 23-26 строка изменение матрици H
    H [k][k] = mt.cos(f)
    H [k][m] = - mt.sin(f)
    H [m][k] = mt.sin(f)
    H [m][m] = mt.cos(f)
    print(f' Матрица поворота H { i+1 }')
    print('\n',H)
    print('\n','Транспонированная матрица поворота H.T ','\n',H.T)
    A = np.dot(H.T,A) # перемножение транспонировоной матрици H на матрицу A
    print('\n',f'A { i+1 }','\n')
    A = np.dot(A,H)
    for row in A:
        for list in row:
            print('{:.9f}'.format(list),end = ' ') #вывод матрици А
            V = np.dot(V,H)# перемножение  матриц H и получение матрици V
        print()
    print('\n','__'*34)
print('Ответ','\n')
L1 = A[0][0]
L2 = A[1][1]
L3 = A[2][2]
print('Собственные числа','\n')
print('L1=',L1,'L2=',L2,'L3=',L3)#39-42  вывод собственных чисел
print('\n','Собственный вектор','\n'*2,V) # вывод собственных векторов
V = V/V.max(axis=0)# нормировка
print('\n','После нормированный столб матрицы V' )
p = 1
for row in V:
    print('\n',f' столб {p}')
    p+= 1
    for list in row:
        print('\n','{:.9f}'.format(list),'\n',end = '  ')

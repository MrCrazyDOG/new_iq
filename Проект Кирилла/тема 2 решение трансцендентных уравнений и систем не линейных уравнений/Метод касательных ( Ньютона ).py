from sympy import *

P = 0 # начало отрезка
Z = 8 # конец отрезока
Go = 6 #кол-во прогонок
# тело программы
Fp = (0.5*P**3+13*P-21)
Fz = (0.5*Z**3+13*Z-21)
X = Symbol('X')
F = (0.5*X**3+13*X-21)
PRO3 = lambdify(X, F.diff(X,2))
PRO4 = lambdify(X, F.diff(X,2))
PRO3 = PRO3(P)
PRO4 = PRO4(Z)
if Fz*PRO4 > 0:#проверяем условие
    for i in range(Go):
        print ('\n'*2,'Номер итерации ',i)
        Fp = (0.5*P**3+13*P-21)
        Fz = (0.5*Z**3+13*Z-21)
        X = Symbol('X')
        F = (0.5*X**3+13*X-21)
        PRO = lambdify(X, F.diff(X,1))
        PRO2 = lambdify(X, F.diff(X,1))
        PRO = PRO(P)
        PRO2 = PRO2(Z)
        PRO3 = lambdify(X, F.diff(X,2))
        PRO4 = lambdify(X, F.diff(X,2))
        PRO3 = PRO3(P)
        PRO4 = PRO4(Z)
        Q = Z - (Fz/PRO2)
        print('\n','a(n-1)=',('{:.9f}'.format(Z)))
        print('\n','Fp=',('{:.9f}'.format(Fz)))
        print('\n','Pp=',('{:.9f}'.format(PRO2)))
        print('\n','P**2=',('{:.9f}'.format(PRO4)))
        print('\n','a(n)=',('{:.9f}'.format(Q)))
        print('\n','--'*10)
        Z = Q
elif Fp*PRO3 > 0:
    for i in range(Go):
        print ('Номер итерации ',i)
        Fp = (0.5*P**3+13*P-21)
        Fz = (0.5*Z**3+13*Z-21)
        X = Symbol('X')
        F = (0.5*X**3+13*X-21)
        PRO = lambdify(X, F.diff(X,1))
        PRO2 = lambdify(X, F.diff(X,1))
        PRO = PRO(P)
        PRO2 = PRO2(Z)
        PRO3 = lambdify(X, F.diff(X,2))
        PRO4 = lambdify(X, F.diff(X,2))
        PRO3 = PRO3(P)
        PRO4 = PRO4(Z)
        Q = P - (Fp/PRO)
        print('\n','a(n-1)=',('{:.9f}'.format(P)))
        print('\n','Fp=',('{:.9f}'.format(Fp)))
        print('\n','Pp=',('{:.9f}'.format(PRO)))
        print('\n','P**2=',('{:.9f}'.format(PRO3)))
        print('\n','a(n)=',('{:.9f}'.format(Q)))
        print('\n','--'*10)
        P = Q
else:
    for i in range(Go):
        print('Ошибка',i)

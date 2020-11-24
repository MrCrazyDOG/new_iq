import math,string

def f(x):
    y= (x*x)-5
    return y
def shag():
    e=0.0001
    x=0.2
    h=1
    y=f(x)
    while h>e:
        print (x, f(x),h)
        if (f(x-h)*f(x))<0:
            x=x-h
            h=h/2.0
            x=x+h
    def main():
        shag()
        return 0

if __name__ == '__main__':
    main()

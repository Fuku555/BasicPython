from math import sin
import math

#関数を定義する
def trapezoidal_integral(f,a=0,b=1,n=100):
    h=(b-a)/n
    M=float(0)
    for k in range(1,int(n+1)):
        M+=f(a+(k-1)*h)+f(a+k*h)
    S=(h/2)*M
    return(S)

#sin(x)を定義
def f1(x):
    result=sin(x)
    return result

#4/(1+x^2)を定義
def f2(x):
    result=4/(1+x*x)
    return result

#√π*exp(-x^2)を定義
def f3(x):
    result=(math.sqrt(math.pi))*(math.exp(-x*x))
    return result

#(1)の答えを求めるときに、コメントを解除
""" 
a=float(0)
b=float(math.pi/2)
n=float(50)
f=f1
"""

#(2)の答えを求めるときに、コメントを解除
"""
a=float(0)
b=float(1)
n=float(100)
f=f2
"""

#(3)の答えを求めるときに、コメントを解除
"""
a=float(-100)
b=float(100)
n=float(1000)
f=f3
"""

result=trapezoidal_integral(f,a,b,n)
print(result)
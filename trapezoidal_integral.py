from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------
a=float(0)
b=math.pi/2
N=float(100)
h=(b-a)/N
M=float(0)

for k in range(1,int(N+1)):
    M+=sin(a+(k-1)*h)+sin(a+k*h)

S=(h/2)*M
print(S)
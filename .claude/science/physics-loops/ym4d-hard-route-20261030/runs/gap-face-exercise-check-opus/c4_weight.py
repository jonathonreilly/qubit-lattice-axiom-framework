# Guide: the weight f = 1 + 0.9 chi_1 on SU(2). Check f > 0, int f = 1, c_1/2(f) = 0, c_1(f) = 0.3, c_3/2(f) = 0.
import math
N = 200000
def chi(n, th):  # n = 2j
    s = math.sin(th)
    return (n+1) if s == 0 else math.sin((n+1)*th)/s
def f(th): return 1 + 0.9*chi(2, th)
h = math.pi/N
mn = min(f((k+0.5)*h) for k in range(N))
def haar_int(g):  # Haar density (2/pi) sin^2 on [0, pi], midpoint rule
    return sum(g((k+0.5)*h)*(2/math.pi)*math.sin((k+0.5)*h)**2 for k in range(N))*h
print('min f = %.4f' % mn)
print('int f = %.6f' % haar_int(f))
for n in (1,2,3,4):
    cj = haar_int(lambda t: f(t)*chi(n,t))/(n+1)
    print('c_%s(f) = %.6f' % (str(n/2), cj))

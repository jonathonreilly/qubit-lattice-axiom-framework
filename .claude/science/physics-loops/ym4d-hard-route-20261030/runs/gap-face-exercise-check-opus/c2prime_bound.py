# Guide: is sum_{j>=1/2} (2j+1)^2 c_j^L <= 5 c_{1/2}^L ?  c_j = I_{2j+1}(b)/I_1(b), Bessel by series.
import math
def I(n,x):
    return sum(math.exp((2*k+n)*math.log(x/2) - math.lgamma(k+1) - math.lgamma(k+n+1)) for k in range(80))
for b in (2.3,2.4,2.5,2.6):
    c = {n: I(n+1,b)/I(1,b) for n in range(1,40)}   # n = 2j
    print('beta=%.1f c_1/2=%.4f c_1=%.4f c_3/2=%.4f' % (b, c[1], c[2], c[3]))
    for L in range(1,8):
        s = sum((n+1)**2 * c[n]**L for n in range(1,40))
        print('   L=%d  sum=%.4e  5c^L=%.4e  ok=%s' % (L, s, 5*c[1]**L, s <= 5*c[1]**L))

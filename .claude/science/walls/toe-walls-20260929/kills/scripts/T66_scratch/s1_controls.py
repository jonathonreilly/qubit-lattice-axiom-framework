# CONTROL 1: degree-1 bracket reproduces G1[xi0] (block 112 T1), fails for c != 1/2
from model import *
def deg1(c):
    return fadd(bracket(C1('N'), T2('M', c=c)), bracket(T2('N', c=c), C1('M')))
g = G1_of_xi(xi0())
for c in (F(1,2), F(0), F(1,3)):
    d = fadd(deg1(c), g, F(-1))
    print("c=",c," residual monomials:", len(d), "" if len(d)==0 else list(d.items())[:4])
# also check sign convention: with G1 having opposite sign fails
d = fadd(deg1(F(1,2)), g, F(1))
print("wrong-sign residual monomials:", len(d))

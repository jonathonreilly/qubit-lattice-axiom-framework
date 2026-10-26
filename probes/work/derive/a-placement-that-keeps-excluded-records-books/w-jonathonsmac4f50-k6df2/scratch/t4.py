import pickle, random, itertools, sympy as sp
from fractions import Fraction as Fr
from math import factorial
exec(open('t3.py').read().split("random.seed(1)")[0])   # reuse table, series, gm, ipow
# Pythagorean unit vectors
pyth=[(Fr(3,5),Fr(4,5)),(Fr(4,5),Fr(3,5)),(Fr(5,13),Fr(12,13)),(Fr(12,13),Fr(5,13)),(Fr(8,17),Fr(15,17)),(Fr(15,17),Fr(8,17)),(Fr(20,29),Fr(21,29)),(Fr(21,29),Fr(20,29))]
pyth+= [(-x,y) for x,y in pyth]+[(x,-y) for x,y in pyth]+[(-x,-y) for x,y in pyth]
def onshell(e1,e2,e1p,e2p,lam1=Fr(1)):
    # lam2, lam1p, lam2p >0 with lam1 e1 + lam2 e2 = lam1p e1p + lam2p e2p and lam1+lam2 = lam1p+lam2p
    l2,a,b=sp.symbols('l2 a b')
    eqs=[lam1*e1[0]+l2*e2[0]-a*e1p[0]-b*e2p[0], lam1*e1[1]+l2*e2[1]-a*e1p[1]-b*e2p[1], lam1+l2-a-b]
    sol=sp.solve(eqs,[l2,a,b],dict=True)
    if not sol: return None
    s=sol[0]
    if len(s)<3: return None
    v=[Fr(int(sp.numer(s[x])),int(sp.denom(s[x]))) for x in (l2,a,b)]
    if min(v)<=0: return None
    return v
random.seed(3)
found=[]
for _ in range(400):
    e1,e2,e1p,e2p=[random.choice(pyth) for _ in range(4)]
    r=onshell(e1,e2,e1p,e2p)
    if r and e1p!=e1 and e1p!=e2:
        found.append((e1,e2,e1p,e2p,r))
    if len(found)>=6: break
print(len(found))
pickle.dump(found,open('onshell_points.pkl','wb'))
for f in found: print(f)

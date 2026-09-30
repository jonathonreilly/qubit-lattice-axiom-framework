import numpy as np
N={6:17,7:69,8:87,9:171,10:217,11:615,12:1039,13:2399}
Ls=np.array(sorted(N)); y=np.log([N[l] for l in Ls])
def fit(Ls,y,basis):
    X=np.array([[f(l) for f in basis] for l in Ls],float)
    c,res,_,_=np.linalg.lstsq(X,y,rcond=None); r=y-X@c
    return c,(r**2).sum()
for lo in (6,8,9):
    m=Ls>=lo
    print("L>=",lo)
    for name,b in (("a L + b",[lambda l:l,lambda l:1]),("a L^2 + b",[lambda l:l*l,lambda l:1]),("a L^2 (no b)",[lambda l:l*l]),("a L (no b)",[lambda l:l]),("aL^2+bL",[lambda l:l*l,lambda l:l]),("a L^1.5+b",[lambda l:l**1.5,lambda l:1])):
        c,s=fit(Ls[m],y[m],b); print("  ",name,np.round(c,4),"SSE %.3f"%s)
# mod-4 subsequences
for r in range(4):
    sel=[l for l in Ls if l%4==r]
    print("L mod4 =",r,[(l,N[l]) for l in sel],[round(np.log(N[l])/l,3) for l in sel])

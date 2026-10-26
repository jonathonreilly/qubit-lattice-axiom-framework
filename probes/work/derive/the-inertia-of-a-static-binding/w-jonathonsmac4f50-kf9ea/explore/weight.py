import sys; sys.path.insert(0,'.')
from exact import *
from fiber import fiber
import numpy as np
def E0_float(m,V,N=1600):
    w=fiber(N,0.0,m,V); pos=[x for x in w if 1e-6<x<2*m-1e-9]
    return pos[-1] if pos else None
def W(m,V,e0=None,h=0.02,n=5):
    m=mp.mpf(m);V=mp.mpf(V)
    if e0 is None: e0=E0_float(float(m),float(V))
    g=mp.mpf(e0)
    Ks=[mp.mpf(h)*j for j in range(1,n+1)]
    Es=[]
    cur=g
    for k in Ks:
        cur=mp.findroot(lambda E:F(E,k,m,V).real,cur); Es.append(cur)
    # fit E = c0 + c2 K^2 + c4 K^4 ...
    A=mp.matrix(n,n); b=mp.matrix(n,1)
    for i,k in enumerate(Ks):
        for j in range(n): A[i,j]=k**(2*j)
        b[i]=Es[i]
    c=mp.lu_solve(A,b)
    return c[0],2*c[1],c[0]*2*c[1]
if __name__=="__main__":
    for (m,V) in [(4,-0.5),(4,-0.3),(4,-0.15),(4,-0.115),(0.8,-0.9)]:
        E0,Epp,Wv=W(m,V)
        print(m,V,mp.nstr(E0,12),mp.nstr(Epp,10),mp.nstr(Wv,10),'eff 1/(4m|V|)=',1/(4*m*abs(V)))

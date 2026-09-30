import numpy as np, sys, time
from k1_gas_contents import *
trip=tuple(float(x) for x in sys.argv[1].split(',')); p,q,r=trip
H=float(sys.argv[3]) if len(sys.argv)>3 else 1.0
gs=[float(x) for x in sys.argv[2].split(',')]
print("triple",trip,"H=",H)
res={}
for L in (6,8,10):
    for g in gs:
        W=Wmatrix(g,p,q,r); z=g**-3*H/6.0
        m1,m2,m4,rho=run(L,W,z,2000,40000,int(1000*g)+L,True)
        res[(L,g)]=(m1,1-m4/(3*m2*m2),rho)
for g in gs:
    print(f"g={g:.3f} "+"  ".join(f"L={L}: U={res[(L,g)][1]:.4f} m={res[(L,g)][0]:.3f} rho={res[(L,g)][2]:.3f}" for L in (6,8,10)))
def crossing(La,Lb):
    d=[res[(La,g)][1]-res[(Lb,g)][1] for g in gs]
    for k in range(len(gs)-1):
        if d[k]*d[k+1]<0: return gs[k]+(gs[k+1]-gs[k])*d[k]/(d[k]-d[k+1])
print("crossings (6,8),(8,10),(6,10):",crossing(6,8),crossing(8,10),crossing(6,10))

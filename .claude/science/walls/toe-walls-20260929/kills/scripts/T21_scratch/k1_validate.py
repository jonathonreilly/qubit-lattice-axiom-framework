import numpy as np, sys, time
from k1_gas_contents import *
# validate contentless gas: p=q=r, H=1, z = g^-3/6
t0=time.time()
res={}
gs=[0.36,0.39,0.41,0.42,0.44]
for L in (6,8,10):
    for g in gs:
        W=Wmatrix(g,1,1,1); z=g**-3/6.0
        m1,m2,m4,rho=run(L,W,z,2000,40000,int(1000*g)+L,True)
        res[(L,g)]=(m1,1-m4/(3*m2*m2),rho)
print("contentless, heat bath (own code). Binder U and <|m|>, rho")
for g in gs:
    print(g, "  ".join(f"L={L}: U={res[(L,g)][1]:.4f} m={res[(L,g)][0]:.3f} rho={res[(L,g)][2]:.3f}" for L in (6,8,10)))
print("time",time.time()-t0)

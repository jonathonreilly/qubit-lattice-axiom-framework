import numpy as np, sys, time
from k1_gas_contents import *
trip=tuple(float(x) for x in sys.argv[1].split(','))
p,q,r=trip
L=8
print("triple",trip,"c0=",6/(p+q+4*r),"L=8; m=<|staggered occupancy|>, rho; start ordered / start random")
Hs=[0.25,0.5,1.0,2.0,4.0,8.0]
for g in [float(x) for x in sys.argv[2].split(',')]:
    for H in Hs:
        W=Wmatrix(g,p,q,r); z=g**-3*H/6.0
        a=run(L,W,z,1500,6000,11,True); b=run(L,W,z,1500,6000,12,False)
        print(f"g={g:.3f} H={H:5.2f}  ordered-start m={a[0]:.3f} rho={a[3]:.3f} | random-start m={b[0]:.3f} rho={b[3]:.3f}")
    sys.stdout.flush()

import numpy as np, beam_vs_sea as b
from gauss import holevo
from numbound import num_info
L=300; h=b.chain_h(L); j0=110
Phi0=b.packets(L,j0,2,sigma=2.0,spacing=12,first=8)
Pu=b.evolve(h,j0,20.0,Phi0,44.0); Pd=b.evolve(h,j0,0.0,Phi0,44.0)
Du,Dd=b.corr(Pu),b.corr(Pd)
worst=0
for (i,m) in [(5,8),(8,8),(11,8),(40,8),(150,8),(210,8),(100,6),(160,6),(-1+ 60,8),(20,8)]:
    a,c=Du[i:i+m,i:i+m],Dd[i:i+m,i:i+m]
    ex=holevo(a,c) if np.linalg.norm(a-c)>1e-7 else 0.0
    nb=num_info(a,c)
    print(i,m,'exact',round(ex,4),'number-bound',round(nb,4), 'OK' if nb<=ex+1e-9 else 'VIOLATION')

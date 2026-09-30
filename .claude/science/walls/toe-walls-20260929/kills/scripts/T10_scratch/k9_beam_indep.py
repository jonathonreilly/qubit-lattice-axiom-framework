"""Independent check of the cap-36 beam windows (attack's winners) by direct site-occupation measurement (Monte Carlo lower bound on chi)."""
import numpy as np, json
import beam_vs_sea as b
from patmc import mi_pattern
from numbound import num_info
from gauss_trunc import holevo_trunc
rng=np.random.default_rng(11)
L=300; h=b.chain_h(L); j0=110
NB=3
Phi0=b.packets(L,j0,NB,sigma=2.0,spacing=12,first=8)
Pu=b.evolve(h,j0,20.0,Phi0,44.0); Pd=b.evolve(h,j0,0.0,Phi0,44.0)
Du,Dd=b.corr(Pu),b.corr(Pd)
for off,m in [(-103,36),(-67,20),(25,36),(61,20)]:
    i=j0+off
    a,c=Du[i:i+m,i:i+m],Dd[i:i+m,i:i+m]
    chi,lost=holevo_trunc(a,c,K=4,maxpart=10)
    mi,se=mi_pattern(a,c,2000,rng)
    print(f'window offset {off:5d} len {m}: attack chi(trunc)={chi:.4f} lost={lost:.1e} | number-bound={num_info(a,c):.4f} | occupation-pattern MC={mi:.4f}+-{se:.4f}',flush=True)

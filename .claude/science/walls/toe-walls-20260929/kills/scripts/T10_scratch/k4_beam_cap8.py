"""Does the pre-registered cap-8 beam test reach R(0.9)>=3 for any reasonable packet width?  Number-bound is exact for
single-carrier packet windows (checked), and exact Holevo (gauss_trunc) is used for confirmation."""
import numpy as np, json, sys
import beam_vs_sea as b
from numbound import scan_num, disjoint
from gauss_trunc import holevo_trunc
L=300; h=b.chain_h(L); j0=110
res=[]
for sigma in (0.7,1.0,1.5,2.0):
  for NB in (1,2,4,6):
    spacing=12; first=8
    Phi0=b.packets(L,j0,NB,sigma=sigma,spacing=spacing,first=first)
    for g in (20.0,):
        Pu=b.evolve(h,j0,g,Phi0,44.0); Pd=b.evolve(h,j0,0.0,Phi0,44.0)
        Du,Dd=b.corr(Pu),b.corr(Pd)
        tab={}
        for i in range(1,L-9):
            for m in range(1,9):
                a,c=Du[i:i+m,i:i+m],Dd[i:i+m,i:i+m]
                if np.linalg.norm(a-c)<1e-7: tab[(i,m)]=0.0; continue
                chi,lost=holevo_trunc(a,c,K=4,maxpart=10)
                tab[(i,m)]=chi if lost<1e-6 else float('nan')
        good={k:v for k,v in tab.items() if v==v}
        ov=float(np.prod(np.linalg.svd(Pu.conj().T@Pd,compute_uv=False)))
        r=dict(sigma=sigma,NB=NB,g=g,overlap=ov,nan_windows=len(tab)-len(good),R09=len(disjoint(good,0.9)),R07=len(disjoint(good,0.7)),R05=len(disjoint(good,0.5)),maxchi=round(max(good.values()),3))
        print(r,flush=True); res.append(r)
json.dump(res,open('k4_beam_cap8.json','w'),indent=1)

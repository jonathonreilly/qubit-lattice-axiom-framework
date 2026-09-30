"""Pre-registered cap-8 test but with shorter evolution so packets have not dispersed (T tied to the last packet's bounce)."""
import numpy as np, json
import beam_vs_sea as b
from numbound import disjoint
from gauss_trunc import holevo_trunc
L=300; h=b.chain_h(L); j0=150
res=[]
for sigma in (1.5,2.0,2.5):
  for NB in (1,2,3,4,6):
    spacing=12; first=6
    T=(first+spacing*(NB-1))/2+ 9.0
    Phi0=b.packets(L,j0,NB,sigma=sigma,spacing=spacing,first=first)
    Pu=b.evolve(h,j0,20.0,Phi0,T); Pd=b.evolve(h,j0,0.0,Phi0,T)
    Du,Dd=b.corr(Pu),b.corr(Pd)
    tab={}
    for i in range(1,L-9):
        for m in range(1,9):
            a,c=Du[i:i+m,i:i+m],Dd[i:i+m,i:i+m]
            if np.linalg.norm(a-c)<1e-7: tab[(i,m)]=0.0; continue
            chi,lost=holevo_trunc(a,c,K=4,maxpart=10)
            tab[(i,m)]=chi if lost<1e-6 else float('nan')
    good={k:v for k,v in tab.items() if v==v}
    r=dict(sigma=sigma,NB=NB,T=T,nan=len(tab)-len(good),R09=len(disjoint(good,0.9)),R07=len(disjoint(good,0.7)),R05=len(disjoint(good,0.5)),maxchi=round(max(good.values()),3),win09=disjoint(good,0.9))
    print(r,flush=True); res.append(r)
json.dump(res,open('k5_beam_cap8_shortT.json','w'),indent=1)

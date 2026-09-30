"""Threshold sensitivity of the cap-36 beam result (attack's beam2 design): R at 0.8, 0.9, 0.95, 0.97."""
import numpy as np, json
import beam_vs_sea as b
from gauss_trunc import holevo_trunc
LENS=[4,6,8,10,12,14,16,20,24,28,32,36]
L=300; h=b.chain_h(L); j0=110; res=[]
for NB in (1,2,3,4):
    Phi0=b.packets(L,j0,NB,sigma=2.0,spacing=12,first=8)
    Pu=b.evolve(h,j0,20.0,Phi0,44.0); Pd=b.evolve(h,j0,0.0,Phi0,44.0)
    Du,Dd=b.corr(Pu),b.corr(Pd); tab={}
    for i in range(1,L-2):
        for m in LENS:
            if i+m>L-1: break
            a,c=Du[i:i+m,i:i+m],Dd[i:i+m,i:i+m]
            if np.linalg.norm(a-c)<1e-7: tab[(i,m)]=0.0; continue
            chi,lost=holevo_trunc(a,c,K=4,maxpart=10)
            if lost>1e-6: continue
            tab[(i,m)]=chi
    r={'NB':NB}
    for thr in (0.8,0.9,0.95,0.97,0.99):
        r[f'R{thr}']=len(b.disjoint_count(tab,thr))
    r['maxchi']=round(max(tab.values()),4)
    print(r,flush=True); res.append(r)
json.dump(res,open('k8_beam_thresholds.json','w'),indent=1)

import numpy as np, json
from common import *
from A4lib import obs, dist
rng=np.random.default_rng(5)
D21, D31 = 7.42e-5, 2.515e-3
sname,p="LOW",1.0
te=np.array(MASSES[sname]["e"])**p
m1s=np.geomspace(1e-4,1.0,40)
tns=[(np.array([m1,np.sqrt(m1**2+D21),np.sqrt(m1**2+D31)])*1e-6)**p for m1 in m1s]
def best_dist(R):
    Ue,_,re_=dressed_U(R,te)
    if re_>1e-8: return None
    b=None
    for tn in tns:
        Un,_,rn=dressed_U(R,tn)
        if rn>1e-8: continue
        d=dist(obs(Ue.conj().T@Un))
        if b is None or d<b: b=d
    return b
ds=[]
for k in range(400):
    R=seed(rng.uniform(0.05,1.0),rng.uniform(0.05,1.0),rng.uniform(0.0,1.0),rng.uniform(0,2*np.pi))
    d=best_dist(R)
    if d is not None: ds.append(d)
ds=np.array(ds)
print(f"random seeds: n={len(ds)}; best box-distance quantiles (box widths): 5%={np.quantile(ds,.05):.2f} 25%={np.quantile(ds,.25):.2f} median={np.median(ds):.2f}; fraction <=1.38 (the CKM-fitted seed's value): {np.mean(ds<=1.38):.3f}; fraction inside box (d=0): {np.mean(ds<=1e-9):.3f}")

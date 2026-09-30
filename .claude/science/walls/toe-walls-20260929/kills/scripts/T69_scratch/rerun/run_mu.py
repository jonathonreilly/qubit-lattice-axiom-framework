import numpy as np, json
from sea_stiffness import a2_bz, qlat2
def kap(N,m,mu,d):
    a2,c0=a2_bz(N,m,mu,3,d); return 4*(a2-c0/4)/qlat2(N,m,3,d), c0
out=[]
for mu in [0.0,0.1,0.25,0.4,0.49]:
    row={'mu':mu}
    for d in ['x','d']:
        (k1,c0),(k2,_)=kap(128,4,mu,d),kap(128,8,mu,d)
        q1,q2=(2*np.pi*4/128)**2,(2*np.pi*8/128)**2
        k0=(k1*q2-k2*q1)/(q2-q1)
        row[d]=float(k0); row['k_'+d+'_q0.196']=float(k1)
    row['c0']=float(c0)
    out.append(row); print(row,flush=True)
ks=np.array([r['x'] for r in out])
print('kappa(mu) x-dir:',ks,' spread (max-min)/mean =',(ks.max()-ks.min())/ks.mean())
kd=np.array([r['d'] for r in out]); print('iso check |x-d|/x:',np.abs(ks-kd)/ks)
json.dump(out,open('T69_results_mu.json','w'),indent=1)

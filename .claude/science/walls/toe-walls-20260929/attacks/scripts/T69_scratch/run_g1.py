import numpy as np, json
from sea_stiffness import a2_bz, qlat2
rows=[]
for N,m in [(2**16,256),(2**18,1024),(2**20,4096),(2**16,128),(2**18,512),(2**20,2048),(2**20,1024),(2**20,512),(2**20,256)]:
    a2,c0=a2_bz(N,m,0.0,1,'x'); k=4*(a2-c0/4)/qlat2(N,m,1,'x')
    rows.append(dict(N=N,m=m,q=2*np.pi*m/N,kappa=float(k)))
    print(rows[-1],flush=True)
# fixed q ~0.0245 with growing N (mesh convergence)
for N,m in [(4096,16),(2**15,128),(2**17,512),(2**20,4096)]:
    a2,c0=a2_bz(N,m,0.0,1,'x'); k=4*(a2-c0/4)/qlat2(N,m,1,'x')
    print('fixed-q',N,m,2*np.pi*m/N,k)
qs=np.array([r['q']**2 for r in rows if r['N']==2**20]); ks=np.array([r['kappa'] for r in rows if r['N']==2**20])
print('1/(3pi)=',1/(3*np.pi))
# linear fit in q^2 on N=2^20 rows
A=np.vstack([np.ones_like(qs),qs]).T
print('fit kappa0, slope:',np.linalg.lstsq(A,ks,rcond=None)[0])
json.dump(rows,open('T69_results_g1.json','w'),indent=1)

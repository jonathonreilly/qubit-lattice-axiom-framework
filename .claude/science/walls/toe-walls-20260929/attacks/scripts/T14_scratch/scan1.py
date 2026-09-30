import numpy as np, json, time
from yukawa_euclid_gap import run
out={}
print("== P1: hypercubic point eps=1, c_psi=lam=1 ==")
rows=[]
for (m,mu) in [(0.5,0.5),(1.0,0.3),(0.3,1.0),(0.7,0.7)]:
    for N in (16,24,32):
        r=run(N,N,1.0,m,mu)
        rows.append(dict(N=N,m=m,mu=mu,**r))
        print(f"N={N:3d} m={m} mu={mu}  a_psi={r['a_psi']: .3e} a_phi={r['a_phi']: .3e} gap={r['gap']: .3e}   (ft={r['ft']:.6f} fx={r['fx']:.6f} tt={r['tt']:.6f} ts={r['ts']:.6f})")
out['P1']=rows
json.dump(out,open('scan1.json','w'),indent=1)

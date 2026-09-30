import numpy as np, json, time
from yukawa_euclid_gap import run
m=mu=0.5
rows=[]
print("== P2/P3: eps scan, tree speeds 1 (c_psi=lam=1), m=mu=0.5 ==")
for eps in [2.0,1.25,1.1,1.02,1.0,0.98,0.9,0.8,0.7,0.5,0.35,0.25,0.18,0.12]:
    res={}
    for fac in (24,48):
        Nt=int(max(24,round(fac/eps))) if eps<1 else fac
        Ns=24
        t0=time.time()
        r=run(Nt,Ns,eps,m,mu)
        res[fac]=(Nt,Ns,r,time.time()-t0)
    (Nt1,Ns1,r1,_),(Nt2,Ns2,r2,dt)=res[24],res[48]
    print(f"eps={eps:5.2f}  Nt={Nt1:4d}->{Nt2:4d}  gap={r1['gap']: .6f} -> {r2['gap']: .6f}  a_psi={r2['a_psi']: .6f} a_phi={r2['a_phi']: .6f}  ({dt:.1f}s)",flush=True)
    rows.append(dict(eps=eps,Nt=Nt2,Ns=Ns2,gap_coarse=r1['gap'],**r2))
json.dump(rows,open('scan2.json','w'),indent=1)

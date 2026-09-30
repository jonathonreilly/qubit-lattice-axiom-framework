import numpy as np, json, time
from yukawa_chunked import run_chunked as run
rows=[]
print("== P4: eps->0 plateau and fermion piece vs probe 3 (walker massless: -0.0096707/-0.0110696/-0.0115076/-0.0116301 at mu=1,1/2,1/4,1/8) ==")
def go(eps,m,mu,Nt,Ns):
    t0=time.time(); r=run(Nt,Ns,eps,m,mu); dt=time.time()-t0
    rows.append(dict(eps=eps,m=m,mu=mu,Nt=Nt,Ns=Ns,**{k:float(v) for k,v in r.items()}))
    print(f"eps={eps:5.3f} m={m} mu={mu} Nt={Nt} Ns={Ns}  a_psi={r['a_psi']: .5f} a_phi={r['a_phi']: .5f} gap={r['gap']: .5f}  ({dt:.0f}s)",flush=True)
for eps in (0.12,0.08,0.05):
    for fac in (1,2):
        go(eps,0.5,0.5,int(round(fac*24/eps/0.5*0.5*1)),32)
for (m,mu) in [(0.5,1.0),(0.5,0.25),(0.25,0.5),(0.25,0.25)]:
    Ns=48 if min(m,mu)>=0.25 else 64
    for fac in (1,2):
        go(0.12,m,mu,int(round(fac*24/0.12*0.5/ min(m,0.5)*0.5)),Ns)
json.dump(rows,open('scan4.json','w'),indent=1)

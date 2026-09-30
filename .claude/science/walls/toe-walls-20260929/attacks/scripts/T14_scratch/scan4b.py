import numpy as np, json, time
from yukawa_chunked import run_chunked as run
rows=[]
for (eps,m,mu,Nt,Ns) in [(0.12,0.25,0.25,800,48),(0.12,0.25,0.25,1600,48),(0.12,0.25,0.25,1600,64),(0.25,0.25,0.25,800,64),(0.25,0.125,0.125,1600,64)]:
    t0=time.time(); r=run(Nt,Ns,eps,m,mu)
    print(f"eps={eps} m={m} mu={mu} Nt={Nt} Ns={Ns} a_psi={r['a_psi']:.5f} a_phi={r['a_phi']:.5f} a_phi/4={r['a_phi']/4:.5f} gap4flav={r['a_psi']-r['a_phi']/4:.5f} ({time.time()-t0:.0f}s)",flush=True)
    rows.append(dict(eps=eps,m=m,mu=mu,Nt=Nt,Ns=Ns,**{k:float(v) for k,v in r.items()}))
json.dump(rows,open('scan4b.json','w'),indent=1)

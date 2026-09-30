"""Driven (non-equilibrium) thermal source: left segment is a thermal gas, right of the segment vacuum; pointer wall/no-wall at j0.
Same chain, same coupling.  Number-statistic lower bound on chi, windows up to 36."""
import numpy as np, json
import beam_vs_sea as b
from numbound import scan_num, disjoint
L=400; j0=200; T=44.0
h=b.chain_h(L)
def run(mu,Tth,seg=(60,190),g=20.0):
    a0,a1=seg; n=a1-a0
    hs=b.chain_h(n); e,U=np.linalg.eigh(hs); f=1/(np.exp((e-mu)/Tth)+1)
    Phi=np.zeros((L,n),complex); Phi[a0:a1,:]=U
    def ev(V):
        hh=h.copy(); hh[j0,j0]+=V; w,W=np.linalg.eigh(hh)
        Ut=(W*np.exp(-1j*w*T)[None,:])@W.conj().T
        P=Ut@Phi
        return (P.conj()*f[None,:])@P.T
    Du,Dd=ev(g),ev(0.0)
    lo,hi=1,L-1
    tab=scan_num(Du,Dd,lo,hi,36)
    out=dict(mu=mu,Tth=Tth,dens=round(float(f.sum()/n),3),particles=round(float(f.sum()),1))
    for cap in (8,18,36):
        t={k:v for k,v in tab.items() if k[1]<=cap}
        out[f'cap{cap}']=dict(R09=len(disjoint(t,0.9)),R05=len(disjoint(t,0.5)),max=round(max(t.values()),3))
    return out
for mu,Tth in [(-1.5,1.0),(-2.5,0.8),(-1.0,0.5)]:
    o=run(mu,Tth); print(json.dumps(o),flush=True)
    open('k10_thermal_source.jsonl','a').write(json.dumps(o)+'\n')

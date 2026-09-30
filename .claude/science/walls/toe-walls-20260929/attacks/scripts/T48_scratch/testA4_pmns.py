"""A4: PMNS from the SAME universal seed R (multiplicative form), charged leptons from e,mu,tau masses, neutrinos with
normal ordering, m1 scanned.  Comparators: NuFIT-6.1 3-sigma box as quoted in the repo (T52 common.py BOX61)."""
import numpy as np, json
from common import *
BOX61 = {"s12": (0.2893, 0.3295), "s13": (0.02070, 0.02418), "s23": (0.435, 0.584)}
R_res = json.load(open("testA_results.json"))
D21, D31 = 7.42e-5, 2.515e-3   # eV^2 (comparators)
def obs(U):
    a=np.abs(U)**2; s13=a[0,2]; c13=1-s13
    return a[0,1]/c13, s13, a[1,2]/c13
def dist(o):
    d=0
    for v,k in zip(o,("s12","s13","s23")):
        lo,hi=BOX61[k]; d=max(d, (lo-v)/(hi-lo) if v<lo else (v-hi)/(hi-lo) if v>hi else 0)
    return d
out={}
for key,rec in R_res.items():
    u=rec["unconstrained"]; R=seed(u["r12"],u["r23"],u["r13"],u["theta"])
    sname,p=key.split("_p"); p=float(p)
    te=np.array(MASSES[sname]["e"])**p
    Ue,_,re_=dressed_U(R,te)
    best=None
    for m1 in np.geomspace(1e-4,1.0,200):
        mn=np.array([m1,np.sqrt(m1**2+D21),np.sqrt(m1**2+D31)])*1e-6   # MeV
        tn=mn**p
        Un,dn,rn=dressed_U(R,tn)
        if rn>1e-8: continue
        U=Ue.conj().T@Un
        # columns already ordered by ascending |eig| => nu1,nu2,nu3
        o=obs(U); d=dist(o)
        if best is None or d<best[0]: best=(d,m1,o)
    print(f"{key}: best over m1: box-distance (in box-widths) = {best[0]:.2f} at m1={best[1]:.3g} eV; (s12^2,s13^2,s23^2)=({best[2][0]:.3f},{best[2][1]:.3f},{best[2][2]:.3f})",flush=True)
    out[key]=dict(box_distance=float(best[0]),m1_eV=float(best[1]),s=[float(x) for x in best[2]])
json.dump(out,open("testA4_results.json","w"),indent=1)

"""Additive universal coupling with INDEPENDENT k12,k23,k13 (real): how non-circulant must the shared K be to fit the CKM magnitudes?"""
import numpy as np, json
from scipy.optimize import least_squares
from common import *
def Kgen(k12,k23,k13):
    K=np.zeros((3,3)); K[0,1]=K[1,0]=k12; K[1,2]=K[2,1]=k23; K[0,2]=K[2,0]=k13; return K
def V_of(sname,p,k):
    mu=np.array(MASSES[sname]["u"])**p; md=np.array(MASSES[sname]["d"])**p
    K=Kgen(*k)
    _,Uu=eig_sorted(np.diag(mu)+K); _,Ud=eig_sorted(np.diag(md)+K)
    a,J=ckm_from(Uu,Ud); return a
out={}
for sname in ("MZ","LOW"):
    for p in (1.0,0.5):
        sc=np.array(MASSES[sname]["d"])[1]**p
        best=None
        rng=np.random.default_rng(1)
        for trial in range(200):
            x0=np.exp(rng.uniform(np.log(1e-3),np.log(1.0),3))*sc*np.array([1,0.3,0.1])*rng.choice([-1,1],3)
            f=lambda k:[np.log(V_of(sname,p,k)[0,1]/OBS["Vus"]),np.log(V_of(sname,p,k)[1,2]/OBS["Vcb"]),np.log(V_of(sname,p,k)[0,2]/OBS["Vub"])]
            try: s=least_squares(f,x0,xtol=1e-13,ftol=1e-13)
            except Exception: continue
            c=np.max(np.abs(s.fun))
            if c<1e-6:
                k=s.x; ak=np.abs(k)
                rec=(ak[1]/ak[0], ak[2]/ak[0], k)
                if best is None or abs(np.log(rec[0]))+abs(np.log(rec[1])) < abs(np.log(best[0]))+abs(np.log(best[1])): best=rec
        if best is None: print(sname,p,"no exact fit found"); continue
        a=V_of(sname,p,best[2])
        te=np.array(MASSES[sname]["e"])**p
        _,Ue=eig_sorted(np.diag(te)+Kgen(*best[2])); ae=np.abs(Ue)
        th=np.degrees(np.arcsin(ae[0,1]/np.hypot(ae[0,0],ae[0,1])))
        print(f"{sname} p={p}: exact fit of (Vus,Vcb,Vub) needs |k23|/|k12|={best[0]:.3f}, |k13|/|k12|={best[1]:.3f} (circulant would be 1, 1); k/sqrt-units={np.round(best[2],4)};  lepton theta_e12={th:.2f} deg")
        out[f"{sname}_p{p}"]=dict(k23_over_k12=float(best[0]),k13_over_k12=float(best[1]),k=[float(v) for v in best[2]],theta_e12=float(th))
json.dump(out,open("testB2_results.json","w"),indent=1)

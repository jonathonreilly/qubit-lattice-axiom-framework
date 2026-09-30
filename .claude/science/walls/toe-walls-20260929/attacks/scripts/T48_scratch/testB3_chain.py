"""Additive universal chain coupling K = k12,k23 only (k13 = 0): 2 parameters fit |Vus|,|Vcb|; predict |Vub| and charged-lepton rotations; neutrino-scale check."""
import numpy as np, json
from scipy.optimize import least_squares
from common import *
def Kc(k12,k23,k13=0.0):
    K=np.zeros((3,3)); K[0,1]=K[1,0]=k12; K[1,2]=K[2,1]=k23; K[0,2]=K[2,0]=k13; return K
out={}
for sname in ("MZ","LOW"):
    for p in (0.5,1.0):
        mu=np.array(MASSES[sname]["u"])**p; md=np.array(MASSES[sname]["d"])**p; me=np.array(MASSES[sname]["e"])**p
        def V(k):
            _,Uu=eig_sorted(np.diag(mu)+Kc(*k)); _,Ud=eig_sorted(np.diag(md)+Kc(*k)); return ckm_from(Uu,Ud)[0]
        f=lambda k:[np.log(V(k)[0,1]/OBS["Vus"]),np.log(V(k)[1,2]/OBS["Vcb"])]
        best=None; rng=np.random.default_rng(0); sc=md[1]
        for t in range(150):
            x0=np.array([rng.uniform(0.05,3),rng.uniform(0.05,3)*0.5])*sc*(md[2]/md[1] if p==1 else 1)*0.1*rng.choice([-1,1],2)
            try: s=least_squares(f,x0,xtol=1e-13,ftol=1e-13)
            except Exception: continue
            if np.max(np.abs(s.fun))<1e-7:
                best=s.x; break
        if best is None: print(sname,p,"no fit"); continue
        a=V(best)
        _,Ue=eig_sorted(np.diag(me)+Kc(*best)); ae=np.abs(Ue)
        th12=np.degrees(np.arcsin(ae[0,1]/np.hypot(ae[0,0],ae[0,1])))
        lam=np.abs(np.linalg.eigvalsh(Kc(*best)))**(1/p)
        print(f"{sname} p={p}: k12,k23={np.round(best,3)}  Vub predicted={a[0,2]:.5f} (obs 0.0037, x{a[0,2]/OBS['Vub']:.2f});  charged-lepton U_e row1 |.|={np.round(ae[0],3)} theta_e12={th12:.2f} deg; K-eigenvalue mass scale (if a neutrino were K-dominated) = {np.max(lam):.3g} MeV = {np.max(lam)*1e6/0.05:.2g} x 0.05 eV")
        out[f"{sname}_p{p}"]=dict(k=[float(v) for v in best],Vub=float(a[0,2]),Vub_ratio=float(a[0,2]/OBS["Vub"]),theta_e12=float(th12),nu_scale_MeV=float(np.max(lam)))
json.dump(out,open("testB3_results.json","w"),indent=1)

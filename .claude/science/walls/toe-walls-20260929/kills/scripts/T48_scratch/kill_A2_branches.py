"""A2 re-check with (i) wide rho (0.03..30, i.e. up to a zero-diagonal circulant), (ii) ALL dressing branches: for each (rho,phi)
solve D_s by multi-start (distinct positive solutions), then take every (u-branch, d-branch) pair. Circulant seed, magnitudes only."""
import numpy as np, sys
from scipy.optimize import least_squares
from common import *
rng=np.random.default_rng(5)
def solve_all(R,t,nstart=14):
    lt=np.log(t); sols=[]
    def f(x):
        w=np.linalg.eigvalsh(np.exp(x)[:,None]*R*np.exp(x)[None,:])
        return np.log(np.sort(np.abs(w))+1e-300)-lt
    for k in range(nstart):
        x0=np.log(np.sqrt(t))+rng.normal(0,0.9,3)
        try: s=least_squares(f,x0,xtol=1e-13,ftol=1e-13,max_nfev=80)
        except Exception: continue
        if np.max(np.abs(s.fun))<1e-9:
            d=np.exp(s.x)
            if not any(np.allclose(d,e,rtol=1e-5) for e in sols): sols.append(d)
    return sols
def Uof(R,d):
    H=d[:,None]*R*d[None,:]; w,U=np.linalg.eigh(H); return U[:,np.argsort(np.abs(w))]
rhos=np.geomspace(0.03,30,36); phis=np.linspace(0,np.pi,19)
for sname in ("MZ","LOW"):
  for p in (1.0,0.5):
    tu=np.array(MASSES[sname]["u"])**p; td=np.array(MASSES[sname]["d"])**p
    best=None; nb=0
    for rho in rhos:
        for phi in phis:
            R=circ_seed(rho,phi)
            su=solve_all(R,tu); sd=solve_all(R,td)
            for du in su:
                Uu=Uof(R,du)
                for dd in sd:
                    a,J=ckm_from(Uu,Uof(R,dd)); nb+=1
                    w=max(abs(a[0,1]/OBS['Vus']-1),abs(a[1,2]/OBS['Vcb']-1),abs(a[0,2]/OBS['Vub']-1))
                    if best is None or w<best[0]: best=(w,rho,phi,a[0,1],a[1,2],a[0,2],len(su),len(sd))
    print(f"{sname} p={p}: circulant seed, ALL dressing branches ({nb} pairs), rho 0.03..30: best worst-rel-err(|V| only)={best[0]:.3f} at rho={best[1]:.3f} phi={np.degrees(best[2]):.0f}: Vus,Vcb,Vub={best[3]:.4f},{best[4]:.4f},{best[5]:.5f} (n branches u,d={best[6]},{best[7]})",flush=True)

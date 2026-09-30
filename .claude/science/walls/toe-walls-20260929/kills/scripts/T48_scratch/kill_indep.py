"""Independent re-check of A1/A2: joint least-squares over seed AND both diagonals (no dressing homotopy),
multi-start, to see (i) all exact seed solutions (A1) and (ii) best circulant seed incl. rho -> infinity (A2)."""
import numpy as np, sys
from scipy.optimize import least_squares
sys.path.insert(0,'.')
from common import MASSES, OBS, ckm_from

def build(R, d):
    return d[:,None]*R*d[None,:]
def eigs(H):
    w,U=np.linalg.eigh(H); idx=np.argsort(np.abs(w)); return w[idx],U[:,idx]

def seed_general(x):
    r12,r23,r13,th=x[:4]
    R=np.eye(3,dtype=complex); R[0,1]=R[1,0]=r12; R[1,2]=R[2,1]=r23
    R[0,2]=r13*np.exp(-1j*th); R[2,0]=np.conj(R[0,2]); return R
def seed_circ(x):
    rho,phi=x[:2]; b=rho*np.exp(1j*phi)
    R=np.eye(3,dtype=complex); R[0,1]=b;R[1,0]=np.conj(b);R[1,2]=b;R[2,1]=np.conj(b);R[2,0]=b;R[0,2]=np.conj(b); return R

def resid(x, kind, tu, td, use_J=True):
    ns = 4 if kind=='gen' else 2
    R = seed_general(x) if kind=='gen' else seed_circ(x)
    du=np.exp(x[ns:ns+3]); dd=np.exp(x[ns+3:ns+6])
    wu,Uu=eigs(build(R,du)); wd,Ud=eigs(build(R,dd))
    a,J=ckm_from(Uu,Ud)
    r=list(np.log(np.abs(wu)/tu))+list(np.log(np.abs(wd)/td))
    r+= [np.log(a[0,1]/OBS['Vus']),np.log(a[1,2]/OBS['Vcb']),np.log(a[0,2]/OBS['Vub'])]
    if use_J: r.append(np.log(max(J,1e-30)/OBS['J']))
    return np.array(r)

rng=np.random.default_rng(11)
for sname in ("MZ","LOW"):
  for p in (1.0,0.5):
    tu=np.array(MASSES[sname]['u'])**p; td=np.array(MASSES[sname]['d'])**p
    # A1: general seed; collect exact solutions
    sols=[]
    for t in range(400):
        x0=np.concatenate([[rng.uniform(0.05,1.5),rng.uniform(0.05,1.5),rng.uniform(0,1.5),rng.uniform(0,2*np.pi)],
                           np.log(np.sqrt(tu))+rng.normal(0,0.5,3),np.log(np.sqrt(td))+rng.normal(0,0.5,3)])
        try: s=least_squares(resid,x0,args=('gen',tu,td),xtol=1e-14,ftol=1e-14,gtol=1e-14,max_nfev=400)
        except Exception: continue
        if np.max(np.abs(s.fun))<1e-7:
            x=s.x; sols.append((abs(x[1])/abs(x[0]),abs(x[2])/abs(x[0]),abs(x[0]),abs(x[1]),abs(x[2])))
    sols=np.array(sols)
    if len(sols):
        print(f"{sname} p={p} A1 exact solutions found: {len(sols)}; r23/r12 in [{sols[:,0].min():.3f},{sols[:,0].max():.3f}], r13/r12 in [{sols[:,1].min():.3f},{sols[:,1].max():.3f}], r12 in [{sols[:,2].min():.3f},{sols[:,2].max():.3f}]",flush=True)
        # closest-to-circulant exact solution
        dist=np.hypot(np.log(sols[:,0]),np.log(sols[:,1])); k=np.argmin(dist)
        print(f"     closest-to-circulant exact solution: r23/r12={sols[k,0]:.3f}, r13/r12={sols[k,1]:.3f}",flush=True)
    else: print(f"{sname} p={p} A1: no exact solution found",flush=True)
    # A2: circulant, full unbounded, J used or not, worst rel err on magnitudes
    best=None
    for t in range(400):
        x0=np.concatenate([[np.exp(rng.uniform(np.log(0.02),np.log(30))),rng.uniform(0,np.pi)],
                           np.log(np.sqrt(tu))+rng.normal(0,0.7,3),np.log(np.sqrt(td))+rng.normal(0,0.7,3)])
        try: s=least_squares(resid,x0,args=('circ',tu,td,False),xtol=1e-14,ftol=1e-14,max_nfev=400)
        except Exception: continue
        # require eigenvalues matched
        if np.max(np.abs(s.fun[:6]))>1e-6: continue
        w=np.max(np.abs(np.exp(s.fun[6:9])-1))
        if best is None or w<best[0]: best=(w,s.x[:2],np.exp(s.fun[6:9])*np.array([OBS['Vus'],OBS['Vcb'],OBS['Vub']]))
    if best: print(f"     A2 circulant, |V| only, eigenvalues matched exactly: best worst-rel-err={best[0]:.3f} at rho={best[1][0]:.3f}, phi={np.degrees(best[1][1]):.0f}; V={np.round(best[2],4)}",flush=True)
    else: print("     A2: no eigenvalue-matched circulant solution",flush=True)

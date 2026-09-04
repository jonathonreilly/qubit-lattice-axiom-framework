"""
T281 - dilution, final instrument.  (supersedes T277/T279; T277 hung on shift-invert)

D measured at the scale the heat trace actually probes, from the a0 term itself:
    K_free(s) = L^3 (4 pi D s)^{-3/2}   =>   D_heat(s) = [K_pure(s)/K_p(s)]^{2/3}
with K_pure the PURE-lattice trace in closed form,
    K_pure(s) = [ sum_k exp(-2s(1-cos k)) ]^3   over k = 2 pi n/L,
so D_heat == 1 at p=1 BY CONSTRUCTION, and the residual there measures the
stochastic pipeline's own error (a free control).

This is the honest structure of the measurement: a0 calibrates D, and a1 is
then a PARAMETER-FREE prediction.  T280 established D is flat to ~3% across
five levels at p=0.85 but runs 44% at p=0.70, so a single D exists at 0.85
and does not at 0.70 -- which is why D must be taken at the probing scale.

Test (occupancy factor q = n/L^3 derived in T279, before seeing any numbers):
    q * D^{3/2} * Rtil(s) / R_cont(D s kappa^2) == 1
"""
import numpy as np, time
from scipy.sparse import diags
from opus_t275 import build, giant, cheb_trace, R_cont

def K_pure(L,s):
    k=2*np.pi*np.arange(L)/L
    return np.array([np.sum(np.exp(-sv*2*(1-np.cos(k))))**3 for sv in s])

def run(L,p,xs,seed=11,nz=32,h=0.05):
    kap=2*np.pi/L; s=xs/kap**2
    g=giant(L,p,seed); idx=np.where(g)[0]; n=len(idx)
    rng=np.random.default_rng(101); Z=rng.choice([-1.0,1.0],size=(n,nz))
    Ks={};Vs={}
    for ei in (-2,-1,0,1,2):
        A,m=build(L,ei*h,g); ms=m[idx]
        Dm=diags(1.0/np.sqrt(ms)); B=(Dm@A[idx][:,idx]@Dm).tocsr()
        lmax=float(abs(B).sum(axis=1).max())*1.02
        Ks[ei]=cheb_trace(B,s,Z,lmax); Vs[ei]=ms.sum()
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    Rtil=(4*np.pi*s)**1.5*d2(Ks)/d2(Vs)
    D=(K_pure(L,s)/Ks[0])**(2.0/3.0)
    return Rtil, D, n/L**3, Ks[0], s

Ls=(40,56,72); ps=(1.00,0.85,0.70); xs=np.array([0.10,0.16,0.24,0.34,0.46])
RT={};DD={};QQ={}
for L in Ls:
    for p in ps:
        t0=time.time(); R,D,q,K0,s=run(L,p,xs); RT[(L,p)]=R; DD[(L,p)]=D; QQ[(L,p)]=q
        ctl="   <-- control: must be 1.000" if p>=1.0 else ""
        print(f"  L={L:3d} p={p:.2f} q={q:.4f}  D_heat(s) = "
              +" ".join(f"{v:6.4f}" for v in D)+f"  [{time.time()-t0:.0f}s]{ctl}")
np.savez("t281_raw.npz",xs=xs,Ls=Ls,ps=ps,
         RT=np.array([[RT[(L,p)] for p in ps] for L in Ls]),
         DD=np.array([[DD[(L,p)] for p in ps] for L in Ls]),
         QQ=np.array([[QQ[(L,p)] for p in ps] for L in Ls]))

print("\n=== q * D^1.5 * Rtil(s) / R_cont(D x)    (1.000 = curvature term survives) ===")
for L in Ls:
    print(f"  --- L={L} ---")
    for p in ps:
        D=DD[(L,p)]; c=QQ[(L,p)]*D**1.5*RT[(L,p)]/R_cont(D*xs)
        print(f"    p={p:.2f}  "+" ".join(f"{v:7.4f}" for v in c))
print("\n=== after removing the 1/s artifact (fit over L at fixed x, T271's procedure) ===")
print("     p     "+"".join(f"  x={x:.2f}" for x in xs))
for p in ps:
    out=[]
    for i,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in Ls])
        cv=np.array([QQ[(L,p)]*DD[(L,p)][i]**1.5*RT[(L,p)][i]/R_cont(DD[(L,p)][i]*x) for L in Ls])
        out.append(np.polyfit(1.0/sv,cv,1)[1])
    print(f"   {p:.2f}   "+" ".join(f"{v:7.4f}" for v in out))

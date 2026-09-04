"""
T277 - dilution, redone with a CALIBRATED D.  (supersedes T275's intercept route)

T276: D from the lowest nonzero mode gives 0.9979 against the exact 0.99795 at
p=1 -- agreement to 5e-5, no fitting -- with the 6-fold plane-wave degeneracy
and PR ~ 0.4-0.5 (extended, not Lifshitz-localised) both confirming the mode is
the plane wave the formula assumes.

Every heat-trace-based D disagrees with it: the T275 intercept gave D(0.85) =
0.58/0.63/0.70 across L (unstable), R184/R185 gave 0.64/0.67, against 0.758.

Second, independent route on D used here: the Rayleigh quotient of the k=2pi/L
plane wave restricted to the giant component, projected off the zero mode.
One matvec, no solver, and it must agree with the eigensolver.

Then the test, with no free parameter left:
    Rtil(s) = D^{-3/2} R_cont(D x) + (1/s lattice artifact)
so extrapolate the artifact at fixed x across L (T271's validated procedure) and
check the collapse  D^{3/2} Rtil_inf(x) / R_cont(D x)  == 1.
"""
import numpy as np, time
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh
from opus_t275 import build, giant, Rtil, R_cont

def D_rayleigh(L,p,seed=11):
    g=giant(L,p,seed); idx=np.where(g)[0]; n=len(idx)
    A,m=build(L,0.0,g); As=A[idx][:,idx]; ms=m[idx]
    Dm=diags(1.0/np.sqrt(ms)); B=(Dm@As@Dm).tocsr()
    i,_,_=np.indices((L,L,L)); x0=i.ravel()[idx]
    out={}
    for lab,f in (("cos",np.cos),("sin",np.sin)):
        v=f(2*np.pi*x0/L)*np.sqrt(ms)          # plane wave in the B-metric
        v=v-np.mean(v); v/=np.linalg.norm(v)
        out[lab]=float(v@(B@v))*(L/(2*np.pi))**2
    return 0.5*(out["cos"]+out["sin"]), n

def D_eig(L,p,seed=11):
    g=giant(L,p,seed); idx=np.where(g)[0]
    A,m=build(L,0.0,g); As=A[idx][:,idx]; ms=m[idx]
    Dm=diags(1.0/np.sqrt(ms)); B=(Dm@As@Dm).tocsr()
    ev=np.sort(eigsh(B,k=8,sigma=-1e-6,which='LM',return_eigenvectors=False))
    return float(ev[ev>1e-9][0])*(L/(2*np.pi))**2

Ls=(40,56,72); ps=(1.00,0.85,0.70)
xs=np.array([0.10,0.16,0.24,0.34,0.46])
print("=== D: two independent routes ===")
print("   L    p     n        D(Rayleigh)   D(eigensolver)   agree     p=1 exact")
Dtab={}
for L in Ls:
    for p in ps:
        dr,n=D_rayleigh(L,p)
        de=D_eig(L,p) if L<=56 else float('nan')
        Dtab[(L,p)]=dr
        ex=f"{2*(1-np.cos(2*np.pi/L))*(L/(2*np.pi))**2:.5f}" if p>=1.0 else "    -"
        ag=f"{dr/de:.5f}" if de==de else "   -"
        print(f"  {L:3d}  {p:.2f} {n:7d}   {dr:10.5f}    {de:10.5f}     {ag}    {ex}")
np.save("t277_D.npy",np.array([[Dtab[(L,p)] for p in ps] for L in Ls]))

print("\n=== Rtil(x) raw ===")
RT={}
for L in Ls:
    for p in ps:
        t0=time.time(); R,n=Rtil(L,p,xs); RT[(L,p)]=R
        print(f"  L={L:3d} p={p:.2f}  "+" ".join(f"{r:8.4f}" for r in R)+f"   [{time.time()-t0:.0f}s]")
np.savez("t277_raw.npz",xs=xs,Ls=Ls,ps=ps,
         RT=np.array([[RT[(L,p)] for p in ps] for L in Ls]),
         D=np.array([[Dtab[(L,p)] for p in ps] for L in Ls]))

print("\n=== collapse after removing the 1/s artifact (fit A+B/s at fixed x over L) ===")
print("   p     D(L=72)    D^1.5*Rtil_inf(x) / R_cont(D x)   at x = "+" ".join(f"{x:.2f}" for x in xs))
for j,p in enumerate(ps):
    Dp=Dtab[(72,p)]
    coll=[]
    for i,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in Ls])
        rv=np.array([RT[(L,p)][i] for L in Ls])
        A=np.polyfit(1.0/sv,rv,1)[1]
        coll.append(Dp**1.5*A/R_cont(Dp*x))
    print(f"  {p:.2f}   {Dp:7.4f}     "+" ".join(f"{c:8.4f}" for c in coll))

"""
T255 - does the record field order in TWO dimensions?

The dimension argument so far:
   odd d  -- excluded, chirality space is exactly {0}          (R133)
   d = 4  -- induced gauge coupling marginal                   (R157)
   d = 2  -- NOT YET EXCLUDED
The record field's symmetry is continuous (SU(n) acting on CP^{n-1}), and a
continuous symmetry cannot break with short-range interactions in two
dimensions.  If the field cannot order on Z^2 there is no continuum limit there,
and the argument tightens to d >= 4 even.

Measured directly, at the Born point, with cold and hot starts, and with the
system size varied -- true long-range order is L-independent; its absence shows
as an order parameter falling with L.
"""
import numpy as np, time

def run(d, L, n, cold, nsweep=4000, seed=353):
    rng = np.random.default_rng(seed)
    if cold:
        z0 = rng.normal(size=n)+1j*rng.normal(size=n); z0/=np.linalg.norm(z0)
        psi = np.broadcast_to(z0, (L,)*d+(n,)).copy()
    else:
        psi = rng.normal(size=(L,)*d+(n,))+1j*rng.normal(size=(L,)*d+(n,))
        psi /= np.linalg.norm(psi,axis=-1,keepdims=True)
    idx = np.indices((L,)*d); masks=[(idx.sum(axis=0)%2==p) for p in (0,1)]
    cone=0.5
    for t in range(nsweep):
        ar=[]
        for mask in masks:
            prop = psi + cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop /= np.linalg.norm(prop,axis=-1,keepdims=True)
            wo=np.ones(psi.shape[:d]); wn=np.ones(psi.shape[:d])
            for ax in range(d):
                for sg in (1,-1):
                    nb=np.roll(psi,sg,ax)
                    wo*=np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn*=np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            a=(rng.random(psi.shape[:d])<np.clip(wn/np.maximum(wo,1e-300),0,1))&mask
            psi[a]=prop[a]; ar.append(a[mask].mean())
        if t%100==99:
            m=np.mean(ar); cone*=1.15 if m>0.55 else (0.87 if m<0.35 else 1.0)
            cone=min(max(cone,0.02),4.0)
    rho = np.einsum('...i,...j->...ij', psi, np.conj(psi))
    return np.linalg.norm(rho.mean(axis=tuple(range(d))) - np.eye(n)/n)

n = 4
ideal = np.sqrt(1-1/n)
print(f"CP^3 record field at the Born point; order parameter |<rho> - I/n|_F")
print(f"perfect order = {ideal:.4f};  true long-range order is L-INDEPENDENT\n")
print(f"{'d':>2s} {'L':>4s} {'sites':>7s} {'cold':>9s} {'hot':>9s}")
for d, Ls in ((2,(16,32,64)), (3,(8,12,16)), (4,(6,8,10))):
    for L in Ls:
        t0=time.time()
        c = run(d,L,n,True); h = run(d,L,n,False)
        print(f"{d:2d} {L:4d} {L**d:7d} {c:9.4f} {h:9.4f}   [{time.time()-t0:.0f}s]")

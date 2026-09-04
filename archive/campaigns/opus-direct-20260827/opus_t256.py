"""
T256 - where is the transition in the PROPOSED setting?

R137 measured lambda_c ~ 0.68 for CP^1 on Z^3.  The proposal is CP^3 on Z^4, and
the packet has been quoting a 3D number for a 4D theory -- R137's continuum-limit
bound and R165's "approaching criticality" both inherit it.

Scans t in  phi = (1-t) + t |<psi|psi'>|^2  for CP^3 on Z^4, using T255's
L-scaling test: an ORDERED phase has an L-independent order parameter, a
disordered one has it falling with L.  The Born point is t = 1.
"""
import numpy as np, time

n = 4
def run(t, L, cold, nsweep=3000, seed=373):
    rng = np.random.default_rng(seed)
    if cold:
        z0 = rng.normal(size=n)+1j*rng.normal(size=n); z0/=np.linalg.norm(z0)
        psi = np.broadcast_to(z0,(L,)*4+(n,)).copy()
    else:
        psi = rng.normal(size=(L,)*4+(n,))+1j*rng.normal(size=(L,)*4+(n,))
        psi /= np.linalg.norm(psi,axis=-1,keepdims=True)
    idx=np.indices((L,)*4); masks=[(idx.sum(axis=0)%2==p) for p in (0,1)]
    cone=0.5
    for s in range(nsweep):
        ar=[]
        for mask in masks:
            prop=psi+cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop/=np.linalg.norm(prop,axis=-1,keepdims=True)
            wo=np.ones(psi.shape[:4]); wn=np.ones(psi.shape[:4])
            for ax in range(4):
                for sg in (1,-1):
                    nb=np.roll(psi,sg,ax)
                    wo*=(1-t)+t*np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn*=(1-t)+t*np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            a=(rng.random(psi.shape[:4])<np.clip(wn/np.maximum(wo,1e-300),0,1))&mask
            psi[a]=prop[a]; ar.append(a[mask].mean())
        if s%100==99:
            m=np.mean(ar); cone*=1.15 if m>0.55 else (0.87 if m<0.35 else 1.0)
            cone=min(max(cone,0.02),4.0)
    rho=np.einsum('...i,...j->...ij',psi,np.conj(psi))
    return np.linalg.norm(rho.mean(axis=(0,1,2,3))-np.eye(n)/n)

print("NARROWED SCAN. t=1 is the only value where phi VANISHES on orthogonal\n      neighbours (a hard constraint); below it phi >= 1-t > 0.")
print("CP^3 on Z^4.  order parameter |<rho> - I/n|_F ; perfect order 0.8660")
print("ORDERED = L-independent ; disordered = falls with L\n")
print(f"{'t':>5s}  {'L=6':>17s}  {'L=8':>17s}  {'L=10':>17s}   trend")
for t in (0.85, 0.90, 0.94, 0.97, 0.99, 1.00):
    vals=[]
    for L in (6,8,10):
        c=run(t,L,True); h=run(t,L,False); vals.append((c,h))
    r = vals[0][0]/max(vals[2][0],1e-12)
    trend = "ORDERED (flat)" if r < 1.35 else "falls -> disordered"
    print(f"{t:5.2f}  " + "  ".join(f"{c:7.4f}/{h:<7.4f}" for c,h in vals)
          + f"   L6/L10 = {r:5.2f}  {trend}")

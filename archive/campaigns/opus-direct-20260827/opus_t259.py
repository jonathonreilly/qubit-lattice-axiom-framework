"""
T259 - the clause the whole campaign ignored: PARTIAL record configurations.

The Record axiom says "WHEN PRESENT, a record locks exactly one admissible local
possibility" and "A site with no record cannot be read."  Both explicitly allow
sites with NO record.  Every simulation in this packet has assumed a complete
configuration -- a record at every site.

If records form and are permanent, the recorded set GROWS, so at any stage a
fraction p of sites carry records.  The record field then lives on a diluted
lattice.  This measures whether it still orders, and at what p.

Setup: a random fraction p of Z^4 sites carry records; edges between two
recorded sites carry the Born weight; edges touching an unrecorded site
contribute nothing.  Order parameter measured over recorded sites only.
"""
import numpy as np, time

n = 4
def run(p, L, cold, nsweep=2500, seed=433):
    rng = np.random.default_rng(seed)
    occ = rng.random((L,)*4) < p
    if cold:
        z0 = rng.normal(size=n)+1j*rng.normal(size=n); z0/=np.linalg.norm(z0)
        psi = np.broadcast_to(z0,(L,)*4+(n,)).copy()
    else:
        psi = rng.normal(size=(L,)*4+(n,))+1j*rng.normal(size=(L,)*4+(n,))
        psi /= np.linalg.norm(psi,axis=-1,keepdims=True)
    idx=np.indices((L,)*4); masks=[((idx.sum(axis=0)%2==q)&occ) for q in (0,1)]
    cone=0.5
    for s in range(nsweep):
        ar=[]
        for mask in masks:
            prop=psi+cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop/=np.linalg.norm(prop,axis=-1,keepdims=True)
            wo=np.ones(psi.shape[:4]); wn=np.ones(psi.shape[:4])
            for ax in range(4):
                for sg in (1,-1):
                    nb=np.roll(psi,sg,ax); nocc=np.roll(occ,sg,ax)
                    ov_o=np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    ov_n=np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
                    wo*=np.where(nocc, ov_o, 1.0)     # unrecorded neighbour: no weight
                    wn*=np.where(nocc, ov_n, 1.0)
            a=(rng.random(psi.shape[:4])<np.clip(wn/np.maximum(wo,1e-300),0,1))&mask
            psi[a]=prop[a]; ar.append(a[mask].mean() if mask.any() else 0.5)
        if s%100==99:
            m=np.mean(ar); cone*=1.15 if m>0.55 else (0.87 if m<0.35 else 1.0)
            cone=min(max(cone,0.02),4.0)
    rho=np.einsum('...i,...j->...ij',psi,np.conj(psi))[occ]
    return np.linalg.norm(rho.mean(axis=0)-np.eye(n)/n)

print("CP^3 on Z^4 at the Born point, a fraction p of sites carrying records.")
print("ORDERED = L-independent ; disordered = falls with L")
print("(Z^4 site-percolation threshold is ~0.20; ordering needs more than")
print(" connectivity, so the ordering threshold should be higher.)\n")
print(f"{'p':>5s}  {'L=6':>17s}  {'L=8':>17s}   L6/L8   trend")
for p in (0.30, 0.50, 0.70, 0.85, 1.00):
    vals=[]
    for L in (6,8):
        c=run(p,L,True); h=run(p,L,False); vals.append((c,h))
    r=vals[0][0]/max(vals[1][0],1e-12)
    print(f"{p:5.2f}  " + "  ".join(f"{c:7.4f}/{h:<7.4f}" for c,h in vals)
          + f"  {r:6.2f}   {'ORDERED' if r < 1.4 else 'falls -> disordered'}")

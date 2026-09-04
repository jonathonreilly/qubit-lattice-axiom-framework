"""
T260 - does R179's threshold survive CORRELATED record growth?

R179 found ordering needs p in (0.50, 0.70) for RANDOM dilution, and flagged
that a real recorded set -- records FORM and are PERMANENT, so the set grows --
would be correlated, not random.  A connected cluster is locally dense (p = 1
inside it), so it may order at any global fraction, making random dilution the
worst case rather than the relevant one.

Compares, at identical global p on Z^4:
   RANDOM    : p fraction of sites chosen independently
   CLUSTERED : a single connected cluster grown by Eden growth from one seed
"""
import numpy as np, time
n = 4

def eden(L, target, rng):
    """grow one connected cluster to `target` sites"""
    occ = np.zeros((L,)*4, dtype=bool)
    seed = tuple(rng.integers(0, L, 4)); occ[seed] = True
    frontier = set()
    def nbrs(c):
        for ax in range(4):
            for d in (1,-1):
                q = list(c); q[ax] = (q[ax]+d) % L; yield tuple(q)
    for q in nbrs(seed): frontier.add(q)
    count = 1
    while count < target and frontier:
        c = list(frontier)[rng.integers(0, len(frontier))]
        frontier.discard(c)
        if occ[c]: continue
        occ[c] = True; count += 1
        for q in nbrs(c):
            if not occ[q]: frontier.add(q)
    return occ

def run(occ, L, cold, nsweep=2000, seed=457):
    rng = np.random.default_rng(seed)
    if cold:
        z0 = rng.normal(size=n)+1j*rng.normal(size=n); z0/=np.linalg.norm(z0)
        psi = np.broadcast_to(z0,(L,)*4+(n,)).copy()
    else:
        psi = rng.normal(size=(L,)*4+(n,))+1j*rng.normal(size=(L,)*4+(n,))
        psi/=np.linalg.norm(psi,axis=-1,keepdims=True)
    idx=np.indices((L,)*4); masks=[((idx.sum(axis=0)%2==q)&occ) for q in (0,1)]
    cone=0.5
    for s in range(nsweep):
        ar=[]
        for mask in masks:
            if not mask.any(): continue
            prop=psi+cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop/=np.linalg.norm(prop,axis=-1,keepdims=True)
            wo=np.ones(psi.shape[:4]); wn=np.ones(psi.shape[:4])
            for ax in range(4):
                for sg in (1,-1):
                    nb=np.roll(psi,sg,ax); nocc=np.roll(occ,sg,ax)
                    wo*=np.where(nocc, np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2, 1.0)
                    wn*=np.where(nocc, np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2, 1.0)
            a=(rng.random(psi.shape[:4])<np.clip(wn/np.maximum(wo,1e-300),0,1))&mask
            psi[a]=prop[a]; ar.append(a[mask].mean())
        if s%100==99 and ar:
            m=np.mean(ar); cone*=1.15 if m>0.55 else (0.87 if m<0.35 else 1.0)
            cone=min(max(cone,0.02),4.0)
    rho=np.einsum('...i,...j->...ij',psi,np.conj(psi))[occ]
    return np.linalg.norm(rho.mean(axis=0)-np.eye(n)/n)

print("CP^3 on Z^4, Born point.  order parameter over RECORDED sites only.")
print("ORDERED = L-independent between L=6 and L=8\n")
print(f"{'p':>5s} {'dilution':>10s}  {'L=6 (cold/hot)':>17s}  {'L=8 (cold/hot)':>17s}  L6/L8  trend")
for p in (0.20, 0.30, 0.50):
    for kind in ("random","clustered"):
        vals=[]
        for L in (6,8):
            rng = np.random.default_rng(1000+L)
            occ = (rng.random((L,)*4) < p) if kind=="random" else eden(L, int(p*L**4), rng)
            c=run(occ,L,True); h=run(occ,L,False); vals.append((c,h))
        r=vals[0][0]/max(vals[1][0],1e-12)
        print(f"{p:5.2f} {kind:>10s}  " + "  ".join(f"{c:7.4f}/{h:<7.4f}" for c,h in vals)
              + f" {r:6.2f}  {'ORDERED' if r < 1.4 else 'falls -> disordered'}")

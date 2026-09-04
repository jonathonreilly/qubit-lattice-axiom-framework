"""
T250 - control for T249: is the rank-2 Born point genuinely disordered, or did
the run fail to find the ordered state?

T249 started from random frames and stayed disordered with the proposal cone
pinned at its cap.  A COLD START settles it: initialise every site to the SAME
frame (perfect order) and see whether it melts.  If it melts, disorder is real.
If it stays ordered, T249 was stuck and its verdict is worthless.

Also compares rank 1 and rank 2 under identical treatment, so the difference is
attributable to the rank and not to the machinery.
"""
import numpy as np, time

def make(n, k, L, rng, cold):
    if cold:
        A = rng.normal(size=(n,k)) + 1j*rng.normal(size=(n,k))
        Q0,_ = np.linalg.qr(A)
        return np.broadcast_to(Q0, (L,)*4+(n,k)).copy()
    A = rng.normal(size=(L,)*4+(n,k)) + 1j*rng.normal(size=(L,)*4+(n,k))
    return orth(A)

def orth(A):
    k = A.shape[-1]
    cols = []
    for j in range(k):
        v = A[...,j]
        for u in cols:
            v = v - np.sum(np.conj(u)*v, axis=-1, keepdims=True)*u
        v = v/np.maximum(np.linalg.norm(v,axis=-1,keepdims=True),1e-300)
        cols.append(v)
    return np.stack(cols, axis=-1)

def wt(Q, Nb):
    U = np.einsum('...ik,...il->...kl', np.conj(Q), Nb)
    return np.real(np.einsum('...kl,...kl->...', np.conj(U), U))

def run(n, k, L, cold, nsweep=2500, seed=307):
    rng = np.random.default_rng(seed)
    Q = make(n, k, L, rng, cold)
    idx = np.indices((L,)*4); masks=[(idx.sum(axis=0)%2==p) for p in (0,1)]
    cone = 0.5
    hist = []
    for t in range(nsweep):
        acc_r = []
        for mask in masks:
            nbs=[]
            for ax in range(4):
                nbs.append(np.roll(Q,1,ax)); nbs.append(np.roll(Q,-1,ax))
            prop = orth(Q + cone*(rng.normal(size=Q.shape)+1j*rng.normal(size=Q.shape)))
            wo=np.ones(Q.shape[:4]); wn=np.ones(Q.shape[:4])
            for nb in nbs:
                wo *= wt(Q,nb); wn *= wt(prop,nb)
            a=(rng.random(Q.shape[:4])<np.clip(wn/np.maximum(wo,1e-300),0,1))&mask
            Q[a]=prop[a]; acc_r.append(a[mask].mean())
        if t%100==99:
            m=np.mean(acc_r)
            cone *= 1.15 if m>0.55 else (0.87 if m<0.35 else 1.0)
            cone = min(max(cone,0.02),4.0)
        if t%250==249 or t==nsweep-1:
            P = np.einsum('...ik,...jk->...ij', Q, np.conj(Q))
            hist.append(np.linalg.norm(P.mean(axis=(0,1,2,3)) - np.eye(n)*k/n))
    return hist, cone

L=8
print(f"L={L}, Z^4, Born point.  order parameter |<P> - (k/n)I|_F")
print("perfect order for rank k in M_n(C) is |P0 - (k/n)I|_F = sqrt(k(1-k/n))\n")
print("contrast of the Born weight  Tr(P P'):  max = k, mean = k^2/n, so max/mean = n/k")
for (n,k) in ((4,1),(4,2),(8,2),(12,3)):
    print(f"   M{n}(C) rank {k}:  max/mean = {n/k:.1f}")
print()
for (n,k) in ((4,1),(4,2),(8,2),(12,3)):
    ideal = np.sqrt(k*(1-k/n))
    for cold in (True, False):
        t0=time.time(); h,c = run(n,k,L,cold)
        print(f"  M{n}(C) rank {k}, {'COLD start (ordered)' if cold else 'hot start (random)'}:")
        print(f"     order parameter over time: " + " ".join(f"{v:.4f}" for v in h))
        print(f"     final {h[-1]:.4f}  vs perfect order {ideal:.4f}   cone {c:.3f}"
              f"   [{time.time()-t0:.0f}s]")

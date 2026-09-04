"""
T249 - the first simulation of a rank-k record field.
Rank-2 records in M4(C) (the Grassmannian Gr(2,4)) on Z^4, Born point.
Same diagnostics as R149 so the numbers are directly comparable.
"""
import numpy as np, sys, time

n, k = 4, 2
def rand_frames(shape, rng):
    A = rng.normal(size=shape+(n,k)) + 1j*rng.normal(size=shape+(n,k))
    # Gram-Schmidt on the two columns
    q0 = A[...,0]; q0 = q0/np.linalg.norm(q0,axis=-1,keepdims=True)
    q1 = A[...,1] - np.sum(np.conj(q0)*A[...,1],axis=-1,keepdims=True)*q0
    q1 = q1/np.linalg.norm(q1,axis=-1,keepdims=True)
    return np.stack([q0,q1], axis=-1)

def weight(Q, Nb):
    """Tr(P P') = tr(U^dag U) with U = Q^dag Q'"""
    U = np.einsum('...ik,...il->...kl', np.conj(Q), Nb)
    return np.real(np.einsum('...kl,...kl->...', np.conj(U), U))

def run(L, nwarm, nmeas, seed=229):
    rng = np.random.default_rng(seed)
    Q = rand_frames((L,)*4, rng)
    idx = np.indices((L,)*4); masks=[(idx.sum(axis=0)%2==p) for p in (0,1)]
    cone=[0.6]
    def half(mask):
        nbs = []
        for ax in range(4):
            nbs.append(np.roll(Q,1,ax)); nbs.append(np.roll(Q,-1,ax))
        prop = Q + cone[0]*(rng.normal(size=Q.shape)+1j*rng.normal(size=Q.shape))
        p0 = prop[...,0]; p0 = p0/np.linalg.norm(p0,axis=-1,keepdims=True)
        p1 = prop[...,1] - np.sum(np.conj(p0)*prop[...,1],axis=-1,keepdims=True)*p0
        p1 = p1/np.linalg.norm(p1,axis=-1,keepdims=True)
        prop = np.stack([p0,p1],axis=-1)
        wo = np.ones(Q.shape[:4]); wn = np.ones(Q.shape[:4])
        for nb in nbs:
            wo *= weight(Q, nb); wn *= weight(prop, nb)
        acc = (rng.random(Q.shape[:4]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
        Q[acc] = prop[acc]
        return acc[mask].mean()
    for t in range(nwarm):
        a = 0.5*(half(masks[0])+half(masks[1]))
        if t%100==99:
            cone[0] *= 1.15 if a>0.55 else (0.87 if a<0.35 else 1.0)
            cone[0] = min(max(cone[0],0.02),4.0)
    Ssl = np.zeros((L,L,L)); nsamp=0; mags=[]
    for t in range(nmeas):
        half(masks[0]); half(masks[1])
        if t%4==0:
            Pr = np.einsum('...ik,...jk->...ij', Q, np.conj(Q))   # rank-2 projector
            mags.append(np.linalg.norm(Pr.mean(axis=(0,1,2,3)) - np.eye(n)*k/n))
            for s in range(L):
                f = np.fft.fftn(Pr[:,:,:,s,:,:], axes=(0,1,2))
                Ssl += np.sum(np.abs(f)**2, axis=(-2,-1))
            nsamp += 1
    return Ssl/(nsamp*L), np.mean(mags), cone[0]

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv)>1 else 10
    t0=time.time(); Ssl, mag, cone = run(L, 4000, 5000)
    kn = 2*np.pi*np.arange(1,6)/L; kh2 = 4*np.sin(kn/2)**2
    s = np.array([(Ssl[m,0,0]+Ssl[0,m,0]+Ssl[0,0,m])/3 for m in range(1,6)])
    a = s*kh2; b = s*np.sqrt(kh2)
    print(f"=== Gr(2,4) records on Z^4, Born point, L={L} "
          f"[{time.time()-t0:.0f}s, cone {cone:.3f}] ===")
    print(f"  order parameter |<P> - (k/n)I|_F = {mag:.5f}   "
          f"({'ORDERED' if mag > 0.05 else 'disordered'})")
    print(f"  3D slice:")
    print(f"     S*khat^2 spread = {a.max()/a.min():5.2f}x  (flat => eta=0, classical 3D)")
    print(f"     S*khat   spread = {b.max()/b.min():5.2f}x  (flat => eta=1, relativistic)")
    print(f"  compare R149 at rank 1 (CP^3): S*khat spread 1.10x-1.12x")

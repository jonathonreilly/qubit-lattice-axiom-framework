"""
T242 - counting the massless modes directly, to settle R159.

Diagonalises the 15x15 equal-time correlation matrix of the gauge-invariant
order parameter rho = |psi><psi| in the ordered phase, mode by mode.  A massless
mode has S(k) ~ 1/k^2 (so S*khat^2 approaches a constant); a massive one has
S(k) -> const (so S*khat^2 -> 0 like k^2).
"""
import numpy as np, time

def gens(n):
    B = []
    for i in range(n):
        for j in range(i+1, n):
            E = np.zeros((n,n),dtype=complex); E[i,j]=1; E[j,i]=1; B.append(E/np.sqrt(2))
            F = np.zeros((n,n),dtype=complex); F[i,j]=-1j; F[j,i]=1j; B.append(F/np.sqrt(2))
    for k in range(1, n):
        d = np.zeros(n); d[:k]=1; d[k]=-k
        B.append(np.diag(d).astype(complex)/np.sqrt(k*k+k))
    return B
T = gens(4); M = len(T)

def run(L, nwarm=4000, nsamp=200, gap=3, seed=113):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,)*4+(4,)) + 1j*rng.normal(size=(L,)*4+(4,))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,)*4); masks = [(idx.sum(axis=0)%2==p) for p in (0,1)]
    cone = [0.6]
    def sweep():
        for mask in masks:
            prop = psi + cone[0]*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
            wo = np.ones(psi.shape[:4]); wn = np.ones(psi.shape[:4])
            for ax in range(4):
                for sg in (1,-1):
                    nb = np.roll(psi, sg, ax)
                    wo *= np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn *= np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            acc = (rng.random(psi.shape[:4]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
            psi[acc] = prop[acc]
    for _ in range(nwarm): sweep()
    NK = 4
    C = np.zeros((NK, M, M), dtype=complex); n = 0
    for _ in range(nsamp):
        for _ in range(gap): sweep()
        rho = np.einsum('...i,...j->...ij', psi, np.conj(psi))
        # FRAME FIX: the condensate direction diffuses between configurations, so
        # averaging correlations in the lab frame mixes Goldstone and massive
        # directions.  Rotate each configuration so its own condensate is
        # diagonal, putting every sample in a common frame.
        rbar = rho.mean(axis=(0,1,2,3))
        w_, Uc = np.linalg.eigh(rbar)
        Uc = Uc[:, ::-1]                       # largest eigenvalue first
        rho = np.einsum('ai,...ij,jb->...ab', Uc.conj().T, rho, Uc)
        c = np.stack([np.real(np.einsum('...ij,ji->...', rho, t.conj().T))
                      for t in T], axis=-1)                       # (L,L,L,L,15)
        c = c - c.mean(axis=(0,1,2,3), keepdims=True)
        f = np.fft.fftn(c, axes=(0,1,2,3))
        for m in range(1, NK+1):
            v = (f[m,0,0,0] + f[0,m,0,0] + f[0,0,m,0] + f[0,0,0,m])/4
            C[m-1] += np.outer(v, np.conj(v))
        n += 1
    return C/n

if __name__ == "__main__":
    L = 10; t0 = time.time()
    C = run(L)
    kn = 2*np.pi*np.arange(1,5)/L; kh2 = 4*np.sin(kn/2)**2
    print(f"Z^4 CP^3 record field at the Born point, L={L}  [{time.time()-t0:.0f}s]")
    print(f"15 modes of rho = |psi><psi|; eigenvalues of the correlation matrix\n")
    # TRACK the modes: fix the eigenbasis at the smallest k and project every k
    # onto it.  Comparing SORTED eigenvalues across k compares different modes.
    Csym = [0.5*(C[m]+C[m].conj().T) for m in range(4)]
    w0, V = np.linalg.eigh(Csym[0])
    S = np.array([[np.real(V[:,i].conj() @ Csym[m] @ V[:,i]) for i in range(M)]
                  for m in range(4)])                     # (k, mode)
    print("   S(k) per tracked mode; fit 1/S = (khat^2 + m^2)/A  ->  m^2\n")
    print("   mode        S(n=1)      S(n=4)     S*khat^2 flat?        m^2")
    m2s = []
    for i in range(M):
        y = 1.0/np.maximum(S[:, i], 1e-300)
        A_ = np.vstack([kh2, np.ones(4)]).T
        c, *_ = np.linalg.lstsq(A_, y, rcond=None)
        m2 = c[1]/c[0] if c[0] != 0 else np.nan
        m2s.append(m2)
        flat = (S[0,i]*kh2[0])/(S[3,i]*kh2[3])
        print(f"   {i+1:3d}   {S[0,i]:12.4f}  {S[3,i]:10.4f}   {flat:12.3f}   {m2:12.5f}")
    m2s = np.array(m2s)
    thr = 0.05
    nm = int(np.sum(np.abs(m2s) < thr))
    print(f"\n   massless (|m^2| < {thr}): {nm}     massive: {M-nm}")
    print(f"   sorted m^2: " + " ".join(f"{v:+.4f}" for v in np.sort(m2s)))
    print(f"\n   PREDICTION was 6 massless, 9 massive -> "
          f"{'CONFIRMED' if nm == 6 else 'NOT confirmed'}")

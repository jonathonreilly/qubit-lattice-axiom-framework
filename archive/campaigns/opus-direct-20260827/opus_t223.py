"""
T223 - the other half: is the DISPERSION of the Z^4 record field relativistic?

T222 showed the 3D slice of the Z^4 record field has eta = 1 (relativistic
equal-time correlations), fixing exactly the defect R140 measured on Z^3.
Equal-time correlations are necessary but not sufficient -- the dispersion must
also be E ~ |k| (z=1) rather than k^2 (z=2).

Reading the 4th lattice direction as time, E(k3) is the decay rate of a spatial
Fourier mode along x4:
      C(k3, t) = < v_{k3}(0) . v_{k3}(t)* >  ~  cosh(E(k3)(t - L/2))
extracted with the standard lattice effective mass
      E = arccosh[ (C(t-1) + C(t+1)) / (2 C(t)) ].

PRE-REGISTERED: for a massless 4D lattice field  4 sinh^2(E/2) = khat3^2,
so E = 2 arcsinh(|khat3|/2) -> |khat3| at small k, i.e. E/|khat3| -> 1: z = 1.
CONTROL: the same estimator on the Z^3 field's own axis must NOT give z=1.
"""
import numpy as np, time
from opus_t222 import run as run4d

def dispersion(v_samples, L):
    """C(k3,t) for k3 along axis 0, correlated along x4."""
    nk = 4
    acc = np.zeros((nk, L))
    for v in v_samples:
        # spatial FT within each x4 slice, momentum along axis 0
        f = np.fft.fftn(v, axes=(0,1,2))          # (L,L,L,L,3)
        for m in range(1, nk+1):
            a = f[m,0,0,:,:]                       # (L,3) as a function of x4
            g = np.fft.fft(a, axis=0)
            acc[m-1] += np.sum(np.abs(g)**2, axis=-1)
    C = np.fft.ifft(acc, axis=1).real
    return C/C[:, :1]

def effmass(C, L):
    out = []
    for m in range(C.shape[0]):
        es = []
        for t in range(1, L//2):
            num = C[m, t-1] + C[m, t+1]
            if C[m, t] > 0 and num/(2*C[m, t]) >= 1.0:
                es.append(np.arccosh(num/(2*C[m, t])))
        out.append(np.median(es[:max(1,len(es)//2)]) if es else np.nan)
    return np.array(out)

if __name__ == "__main__":
    L, lam = 12, 1.0
    print(f"Z^4 record field, L={L}, lam={lam}; 4th direction read as time\n")
    rng = np.random.default_rng(5)
    v = rng.normal(size=(L,)*4+(3,)); v /= np.linalg.norm(v,axis=-1,keepdims=True)
    idx = np.indices((L,)*4); A = (idx.sum(axis=0)%2==0); B = ~A
    def half(mask, cone):
        nb = []
        for ax in range(4):
            nb.append(np.roll(v,1,ax)); nb.append(np.roll(v,-1,ax))
        prop = v + cone*rng.normal(size=v.shape)
        prop /= np.linalg.norm(prop,axis=-1,keepdims=True)
        wo = np.ones(v.shape[:4]); wn = np.ones(v.shape[:4])
        for n in nb:
            wo *= 1 + lam*np.sum(v*n,axis=-1); wn *= 1 + lam*np.sum(prop*n,axis=-1)
        acc = (rng.random(v.shape[:4]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
        v[acc] = prop[acc]; return acc[mask].mean()
    cone = 1.0
    for t in range(4000):
        a = 0.5*(half(A,cone)+half(B,cone))
        if t%100==99:
            cone *= 1.15 if a>0.55 else (0.87 if a<0.35 else 1.0)
            cone = min(max(cone,0.05),4.0)
    t0=time.time(); samples=[]
    for t in range(6000):
        half(A,cone); half(B,cone)
        if t%6==0: samples.append(v.copy())
    C = dispersion(samples, L)
    E = effmass(C, L)
    kn = 2*np.pi*np.arange(1,5)/L
    kh = 2*np.sin(kn/2)
    print("  n     k      khat     E(k)      E/khat     E/khat^2   free-field 2asinh(khat/2)")
    for m in range(4):
        pred = 2*np.arcsinh(kh[m]/2)
        print(f"  {m+1}  {kn[m]:6.4f}  {kh[m]:6.4f}  {E[m]:8.5f}  {E[m]/kh[m]:9.4f}  "
              f"{E[m]/kh[m]**2:9.4f}   {pred:8.5f}")
    r1 = E/kh; r2 = E/kh**2
    print(f"\n  E/khat   spread = {np.nanmax(r1)/np.nanmin(r1):5.2f}x   (flat => z=1 RELATIVISTIC)")
    print(f"  E/khat^2 spread = {np.nanmax(r2)/np.nanmin(r2):5.2f}x   (flat => z=2 diffusive)")
    print(f"  [{time.time()-t0:.0f}s]")

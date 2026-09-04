"""
T263 - is R182's failure a NORMALISATION artefact or a REAL breakdown?

R182: with D from lambda_1, V(s) = (4 pi D s)^1.5 K/N does not go to 1 at
p = 0.70, and localisation does NOT explain it (the modes are extended).
Two candidates were left untested: a scale-dependent D, and lambda_1 = D khat^2
being an overestimate on a tortuous giant component.

Decisive test: do NOT assume the exponent.  Fit  log K = a + b log s.
   b ~ -3/2  -> the s^{-3/2} form HOLDS; only the normalisation (D) was wrong
               -> artefact, and the gravity machinery may yet transfer
   b != -3/2 -> the form itself fails -> real breakdown

Also measures D_n = lambda_n / khat_n^2 for several n, testing scale-dependence
of D directly.
"""
import numpy as np
L = 16
def build(p, seed=487):
    rng = np.random.default_rng(seed)
    occ = (rng.random((L,L,L)) < p) if p < 1.0 else np.ones((L,L,L), bool)
    sites=np.argwhere(occ); idx=-np.ones((L,L,L),int); idx[occ]=np.arange(len(sites))
    N=len(sites); A=np.zeros((N,N))
    for a,(i,j,k) in enumerate(sites):
        for di,dj,dk in ((1,0,0),(0,1,0),(0,0,1)):
            q=((i+di)%L,(j+dj)%L,(k+dk)%L)
            if occ[q]:
                b=idx[q]; A[a,b]-=1; A[b,a]-=1; A[a,a]+=1; A[b,b]+=1
    return A,N

print("=== 1. fit the EXPONENT: log K = a + b log s  (b = -1.5 if the form holds) ===")
print(f"{'p':>5s} {'N':>6s} {'fitted b':>10s} {'vs -1.5':>9s} {'rms resid':>10s}")
store={}
for p in (1.00, 0.70, 0.50):
    A,N = build(p); ev=np.sort(np.maximum(np.linalg.eigvalsh(A),0)); store[p]=(ev,N)
    s = np.geomspace(2.0, 8.0, 12)                    # inside the valid window for D~1
    K = np.array([np.sum(np.exp(-si*ev)) for si in s])
    M = np.vstack([np.ones_like(s), np.log(s)]).T
    c,*_ = np.linalg.lstsq(M, np.log(K), rcond=None)
    r = np.sqrt(np.mean((M@c-np.log(K))**2))
    print(f"{p:5.2f} {N:6d} {c[1]:10.4f} {c[1]+1.5:+9.4f} {r:10.5f}")

print("\n=== 2. is D scale dependent?  D_n = lambda_n / khat_n^2 ===")
print("   (khat_n^2 = 4 sin^2(pi n/L); on the pure lattice D_n = 1 for all n)")
print(f"{'p':>5s}  " + "  ".join(f"n={n}" for n in (1,2,3,4,6,8)))
for p in (1.00, 0.70, 0.50):
    ev,N = store[p]
    nz = ev[ev>=1e-9]
    row=[]
    for n in (1,2,3,4,6,8):
        kh2 = 4*np.sin(np.pi*n/L)**2
        # the n-th shell: use the eigenvalue at the position matching the pure-lattice count
        idx = min(int(round(N*(4/3*np.pi*(n**3))/L**3)), len(nz)-1)
        row.append(nz[max(idx,0)]/kh2)
    print(f"{p:5.2f}  " + "  ".join(f"{q:5.3f}" for q in row))

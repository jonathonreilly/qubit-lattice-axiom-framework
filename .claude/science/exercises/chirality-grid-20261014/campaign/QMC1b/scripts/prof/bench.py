import time, numpy as np
from scipy.linalg import blas
rng = np.random.default_rng(0)
for L in (4, 6):
    N, Dd = L*L, 32; Nd = N*Dd; m = Nd
    X = rng.normal(size=(Nd, m)) + 1j*rng.normal(size=(Nd, m))
    coords = np.array(list(np.ndindex(L, L))); ks = coords * (2*np.pi/L)
    Fm = np.exp(-1j * ks @ coords.T); Fi = Fm.conj().T / N
    t = time.time()
    for _ in range(5):
        Xk = np.fft.fftn(X.reshape(L, L, Dd, m), axes=(0, 1)).reshape(N, Dd, m)
    t1 = (time.time()-t)/5
    t = time.time()
    for _ in range(5):
        Xk2 = (Fm @ X.reshape(N, Dd*m)).reshape(N, Dd, m)
    t2 = (time.time()-t)/5
    print(f"L{L} fft {t1*1e3:.1f} ms  dft-matmul {t2*1e3:.1f} ms  maxdiff {np.abs(Xk-Xk2).max():.1e}")
    A = rng.normal(size=(Nd, 32)) + 1j*rng.normal(size=(Nd, 32)); B = rng.normal(size=(32, Nd)) + 1j*rng.normal(size=(32, Nd))
    G = X.copy(); t = time.time()
    for _ in range(10): G -= A @ B
    ta = (time.time()-t)/10
    G2 = X.copy(); t = time.time()
    for _ in range(10):
        r = blas.zgemm(-1.0, B.T, A.T, beta=1.0, c=G2.T, overwrite_c=1)
    tb = (time.time()-t)/10
    print(f"L{L} update numpy {ta*1e3:.2f} ms  zgemm-inplace {tb*1e3:.2f} ms  shares {np.shares_memory(r, G2)}  diff {np.abs(G-G2).max():.1e}")

"""Design calculation (not a test): aggregate overlap A = sqrt(sum_{r!=0}|K(r)|^2)/K(0), K = FT of f^2,
and max neighbour overlap, for 1D filter families vanishing at k = 0; plus the 3D X2 filters (K1 B2/B3 cross-check)."""
import numpy as np
def ov1d(f, N=4096):
    k = 2*np.pi*np.arange(N)/N; F2 = f(k)**2
    K = np.fft.ifft(F2).real; K0 = K[0]; Ka = np.abs(K.copy()); Ka[0] = 0
    return np.sqrt((Ka**2).sum())/K0, Ka.max()/K0, int((np.abs(K) > 1e-12).sum())
fams = {"star (1-c)/2": lambda k: (1-np.cos(k))/2,
        "proj-limit f=1 (k!=0)": None}
for b in [0.0, 0.2, 0.3, 0.4, 0.5, 0.6]:
    fams[f"flat b={b}: (1-c)(1+b c)/2"] = (lambda b: (lambda k: (1-np.cos(k))*(1+b*np.cos(k))/2))(b)
for n in [1.5, 2, 2.5, 3]:
    fams[f"peak n={n}: ((1-c)/2)^n"] = (lambda n: (lambda k: ((1-np.cos(k))/2)**n))(n)
for b in [-0.2, -0.4, -0.6]:
    fams[f"peak b={b}: (1-c)(1+b c)/2"] = (lambda b: (lambda k: (1-np.cos(k))*(1+b*np.cos(k))/2))(b)
for name, f in fams.items():
    if f is None: continue
    A, m, s = ov1d(f); print(f"{name:34s} A = {A:.4f}  max|K(r)|/K0 = {m:.4f}  support = {s}")
# 3D cross-check of K1 numbers
N = 32; k = 2*np.pi*np.arange(N)/N; p = np.stack(np.meshgrid(k, k, k, indexing='ij'))
fNN = (1-np.cos(p).sum(0))/2
s2, c2 = np.sin(p/2)**2, np.cos(p/2)**2
fF1 = 1-(s2[0]*c2[1]*c2[2]+s2[1]*c2[0]*c2[2]+s2[2]*c2[0]*c2[1])
for nm, F in [("3D f_NN", fNN), ("3D f_F1", fF1)]:
    F2 = F**2; K = np.fft.ifftn(F2).real; Ka = np.abs(K.copy()); Ka[0,0,0] = 0
    print(nm, "A =", round(np.sqrt((Ka**2).sum())/K[0,0,0], 4), "max =", round(Ka.max()/K[0,0,0], 4))

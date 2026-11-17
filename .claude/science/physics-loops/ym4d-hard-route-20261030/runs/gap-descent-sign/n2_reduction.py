"""GUIDE for step 5 (n = 2): B = D A D on l^2(N), A(n,m) = a_n a_m (I_{n-m} - I_{n+m})(beta), a_n = I_n/I_1,
D = exp(-t c/2), c_n = (n^2-1)/2 (N = 2 C). Reports r(1) = phi_1(1)/phi_0(1), sign pattern of r^2-1,
n_1-n_0, the bound nu_1 - 2 n_0, third/second cumulant of c in the vacuum, and min 2x2 minor sign."""
import numpy as np
from scipy.special import ive
NM = 60
n = np.arange(1, NM+1)
c = (n**2 - 1) / 2.0
def run(beta, t):
    a = ive(n, beta) / ive(1, beta)
    Kk = ive(np.abs(n[:, None]-n[None, :]), beta) - ive(n[:, None]+n[None, :], beta)
    d = a * np.exp(-t*c/2)
    B = d[:, None]*Kk*d[None, :]
    w, V = np.linalg.eigh(B)
    p0, p1 = V[:, -1], V[:, -2]
    if p0[0] < 0: p0 = -p0
    if p1[0] < 0: p1 = -p1
    keep = p0**2 > 1e-24
    r = p1[keep]/p0[keep]
    mono = bool(np.all(np.diff(r) < 0))
    h = r**2 - 1
    sg = np.sign(h); pat = ''.join('+' if s > 0 else '-' for s in sg[np.r_[True, np.diff(sg) != 0]])
    P = p0**2
    n0 = P@c; n1 = (p1**2)@c
    k2 = P@(c-n0)**2; k3 = P@(c-n0)**3
    return r[0], mono, pat, n0, n1, k3/k2 if k2 > 1e-14 else float('nan'), np.log(w[-1]/w[-2])
print("beta t r(1) r_monotone pattern(r^2-1) n0 n1 n1-n0 1.5-2n0 k3/k2 m")
for beta in (0.5, 1, 2, 3, 4, 6, 8, 12, 16):
    for t in (0.0, 0.05, 0.2, 0.6, 1.5):
        r1, mono, pat, n0, n1, sk, m = run(beta, t)
        print(f"{beta:5.1f} {t:4.2f} {r1:7.4f} {mono} {pat:4s} {n0:8.4f} {n1:8.4f} {n1-n0:8.4f} {1.5-2*n0:8.4f} {sk:8.4f} {m:8.5f}")

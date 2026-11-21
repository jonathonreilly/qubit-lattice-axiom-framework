# GUIDE only. One-plaquette 2+1 toy: class functions of one SU(2) variable, basis chi_n, n = 2j+1 = 1..N.
# T_hat(bt, bs) = M^{1/2} K_hat M^{1/2},  M = exp(-bs (1 - cos th)),  K_hat = diag((I_n(bt)/I_1(bt))^4).
# Checks (AN): prod_{i<k} lam_i(T_hat(bt', theta bs)) <= (prod_{i<k} lam_i(T_hat(bt, bs)))^theta,
# theta = min_{n>=2} eps_n(bt')/eps_n(bt), eps_n = -log(I_n/I_1).  Also prints gap rates on the isotropic line.
import numpy as np
from scipy.special import ive
N = 60
n = np.arange(1, N + 1)
def eps(b):
    return -(np.log(ive(n, b)) - np.log(ive(1, b)))          # eps_1 = 0
def Mmat(bs):
    d = np.abs(n[:, None] - n[None, :]); s = n[:, None] + n[None, :]
    return ive(d, bs) - ive(s, bs)                           # e^{-bs}[I_{|n-n'|} - I_{n+n'}]
def That(bt, bs):
    w, V = np.linalg.eigh(Mmat(bs)); w = np.clip(w, 0, None)
    Mh = (V * np.sqrt(w)) @ V.T
    K = np.diag(np.exp(-4 * eps(bt)))
    return Mh @ K @ Mh
def lev(bt, bs, k=6):
    lam = np.sort(np.linalg.eigvalsh(That(bt, bs)))[::-1][:k]
    return -np.log(lam)                                      # E_hat_i >= 0
worst = -1e9
for bt, btp, bs in [(0.5, 0.8, 0.5), (1.0, 1.5, 1.0), (2.0, 2.3, 2.0), (2.3, 2.6, 2.3), (2.3, 4.0, 3.0), (1.0, 6.0, 5.0)]:
    e0, e1 = eps(bt), eps(btp)
    th = np.min(e1[1:] / e0[1:])
    A = np.cumsum(lev(btp, th * bs)); B = th * np.cumsum(lev(bt, bs))
    worst = max(worst, np.max(B - A))
    print(f"bt={bt} bt'={btp} bs={bs} theta={th:.4f}  min_k[KyFan'(k) - theta*KyFan(k)] = {np.min(A - B):.3e}")
print("largest violation of (AN) over the cases (should be <= 0 up to rounding):", f"{worst:.2e}")
print("isotropic line: s, E0, gap1, gap2, K1 = -dlog(gap1)/ds, K_el = max_n(-dlog eps_n/ds)")
h = 1e-4
for s in [0.3, 0.6, 1.0, 1.5, 2.0, 2.3, 2.6, 3.0, 4.0]:
    E = lev(s, s); Ep = lev(s + h, s + h); Em = lev(s - h, s - h)
    g1 = E[1] - E[0]; K1 = -(np.log(Ep[1] - Ep[0]) - np.log(Em[1] - Em[0])) / (2 * h)
    Kel = np.max(-(np.log(eps(s + h)[1:]) - np.log(eps(s - h)[1:])) / (2 * h))
    print(f"s={s:4.1f}  E0={E[0]:.4f}  gap1={g1:.4f}  gap2={E[2]-E[0]:.4f}  K1={K1:+.4f}  K_el={Kel:.4f}")

"""T3 (pre-registered in ../PREREG.md): GW defect of finite-auxiliary (rational) approximants to the
overlap, free 4D Wilson kernel (r = 1), and the number of auxiliary fields needed.

Free Wilson-Dirac: D_W(p) = (W - M) + i gamma.s,  W = sum(1 - cos p), s_mu = sin p_mu (normal operator).
|H_W| = sqrt(s^2 + (W-M)^2)  (H_W = g5 D_W).
Shamir DWF kernel H_T = g5 D_W (2 + D_W)^{-1}; |H_T| = |d| / |2 + d|, d = (W-M) + i|s|.
Shamir effective eps_N = tanh(N artanh H_T): GW defect max|1 - eps_N^2| = sech^2(N artanh lam_T,min).
Zolotarev best rational approx of sign on [k,1] (after scaling by lam_max), n poles:
   error ~ 4 exp(-n pi K(k')/K(k)),  k = lam_min/lam_max.
Also a direct check that the Shamir eps_N is a rational function of the kernel (Schur complement of a
nearest-neighbour 5D operator) is NOT re-derived here (comparator: Neuberger 1998; Borici; Edwards-Heller-Narayanan).
"""
import numpy as np
from scipy.special import ellipk

Ng = 36
ps = 2 * np.pi * np.arange(Ng) / Ng
c = np.cos(ps)
s = np.sin(ps)
# build 4D grids by broadcasting (Ng^4 = 1.68M points, float64 -> ~13 MB per array)
C = [c.reshape([-1 if i == j else 1 for i in range(4)]) for j in range(4)]
S = [s.reshape([-1 if i == j else 1 for i in range(4)]) for j in range(4)]
W = sum(1 - Ci for Ci in C)
s2 = sum(Si**2 for Si in S)
targets = {"1e-35 (EW, U(1)_em exact)": 1e-35, "1e-88 (photon-mass bound)": 1e-88}
print(f"grid {Ng}^4 (includes all 16 corners and p=0)")
for M in (0.5, 1.0, 1.5, 1.8):
    Wm = W - M
    lamW = np.sqrt(s2 + Wm**2)
    lamW_min, lamW_max = lamW.min(), lamW.max()
    d_abs = np.sqrt(Wm**2 + s2)
    two_d_abs = np.sqrt((2 + Wm)**2 + s2)
    lamT = d_abs / two_d_abs
    lamT_min = lamT.min()
    cS = 2 * np.arctanh(lamT_min)
    k = lamW_min / lamW_max
    kp = np.sqrt(1 - k * k)
    cZ = np.pi * ellipk(kp**2) / ellipk(k**2)
    print(f"M={M}: lam_W in [{lamW_min:.4f},{lamW_max:.4f}]  lam_T,min={lamT_min:.4f}  "
          f"Shamir rate/layer={cS:.3f}  Zolotarev rate/pole={cZ:.3f}")
    for name, dlt in targets.items():
        NS = np.log(4 / dlt) / cS
        NZ = np.log(4 / dlt) / cZ
        print(f"    delta={name}: Shamir N_req={NS:7.1f}   Zolotarev n_req={NZ:6.1f}")
# reading against PREREG: best N_req at delta=1e-35
print("note: free theory only; gauge backgrounds reduce lam_min (lower bound on price).")

"""Integrated autocorrelation time (Sokal window, c = 5) of S10(Q0) and G_m(beta/2) per run, and the error
inflation sqrt(2 tau_int) relative to the naive error.  python3 autocorr.py runs/L4_*.npz runs/L6_*.npz"""
import sys
import numpy as np


def tau_int(x, c=5.0):
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    n = len(x)
    if n < 8:
        return np.nan
    x = x - x.mean()
    v = np.dot(x, x) / n
    if v == 0:
        return np.nan
    t = 0.5
    for k in range(1, n // 2):
        rho = np.dot(x[:-k], x[k:]) / (n - k) / v
        t += rho
        if k >= c * t:
            break
    return max(t, 0.5)


for p in sys.argv[1:]:
    z = np.load(p, allow_pickle=True)
    s10 = z["SX0"].sum(1) + z["SY0"].sum(1)
    nt = z["gt_mirror"].shape[1]
    gm = z["gt_mirror"][:, nt // 2, :, 0].mean(1)
    t1, t2 = tau_int(s10), tau_int(gm)
    print(f"{p.split('/')[-1]:28s} n={len(s10):3d}  tau_int(S10) = {t1:5.2f} sweeps  tau_int(G_m(beta/2)) = {t2:5.2f}  "
          f"naive-error inflation for S10 sqrt(2 tau) = {np.sqrt(2 * t1):.2f}")

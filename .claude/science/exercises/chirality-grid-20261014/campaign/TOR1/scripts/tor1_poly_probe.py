"""TOR-1 diagnostic (F3): integrand vs the Polyakov variable chi_0 at fixed plane nodes, Fourier decay, for mod/O/vec0 and the
separate charge-1 / charge-2 dets.  usage: python3 tor1_poly_probe.py"""
import numpy as np
from tor1_geom import *
S = Torus(4, 4); z = np.load('pool_TOR1_Lt4_k6_s3101.npz'); U = [{'x': z['ux'][i], 't': z['ut'][i]} for i in range(len(z['ux']))]
for (a, b) in ((0, 0), (0, 3), (2, 5)):
    A, w = entry_fields(S, U[a], U[b], 1, 128)          # n = 1 plane rule (4 nodes per plane), 128 Polyakov points
    l1, g1 = vec_logdet(S, A, 0.0, 1); l2, g2 = vec_logdet(S, A, 0.0, 2); lo, _ = vec_logdet(S, A, 0.05, 1)
    nP = len(w) // 128
    for nm, l in (('D1', l1.real), ('D2', l2.real), ('mod', 2 * l1.real + 0.5 * l2.real), ('O', lo.real)):
        f = np.exp(l - l.max()).reshape(nP, 128)
        c = np.abs(np.fft.rfft(f, axis=1)) / np.abs(np.fft.rfft(f, axis=1))[:, :1]
        print(f"({a},{b}) {nm:3s}: min_chi f/max {f.min(1).min():.2e}  Fourier |c_m/c_0| m=1..12: " + " ".join(f"{v:.1e}" for v in c.max(0)[1:13]) + f" ; m=24 {c.max(0)[24]:.1e} m=48 {c.max(0)[48]:.1e}; min gap1 {g1.min():.3f} gap2 {g2.min():.3f}")

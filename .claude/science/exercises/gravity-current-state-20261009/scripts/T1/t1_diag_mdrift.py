"""Diagnose the slow m-drift of the a2 continuum split: which ingredient (Gaussian dispersion, Wilson mass,
propagator weight) causes it, and from which |q| region. Radial profile of the Delta integrand."""
import numpy as np
from t1_loop import coeffs
from t1_selftest_collins import sph_grid
k = 16 * np.pi ** 2

def build(m, s, r, disp_gauss, wilson, weight):
    qv, W = sph_grid(500, 32, 32, 14.0 / s, 1e-4 * m)
    q2 = (qv ** 2).sum(0); g = np.exp(-s * s * q2 / 2)
    dg = -s * s * qv[0] * g; d2g = (-s * s + s ** 4 * qv[0] ** 2) * g
    ex = np.zeros_like(qv); ex[0] = 1.0
    if disp_gauss:
        S = qv * g; dS = ex * g + qv * dg; d2S = 2 * ex * dg + qv * d2g
        w2 = m * m + (2 / s ** 2) * (1 - g); dw2 = 2 * S[0]
    else:
        S = qv.copy(); dS = ex.copy(); d2S = np.zeros_like(qv); w2 = m * m + q2; dw2 = 2 * qv[0]
    if wilson:
        M = m + (r / s) * (1 - g); dM = -(r / s) * dg; d2M = -(r / s) * d2g
    else:
        M = m + 0 * g; dM = 0 * g; d2M = 0 * g
    one, zero = np.ones_like(g), np.zeros_like(g)
    f, df, d2f = (g, dg, d2g) if weight else (one, zero, zero)
    o = coeffs(W, dict(S=S, M=M, dS=dS, d2S=d2S, dM=dM, d2M=d2M, fF=f, dfF=df, d2fF=d2f),
               dict(w2=w2, dw2=dw2, fB=f, dfB=df))
    qn = np.sqrt(q2)
    return o, qn

for name, dg_, wl, wt in [("relativistic disp, no Wilson, weight f (Collins both)", False, False, True),
                          ("relativistic disp, Wilson r=1, weight f", False, True, True),
                          ("Gaussian disp, Wilson r=1, weight f (a2)", True, True, True)]:
    print(name)
    for ms in (0.1, 0.02, 0.005):
        o, qn = build(ms, 1.0, 1.0, dg_, wl, wt)
        d = k * (o["_ipsi"] - o["_iphi"])
        bands = [0, 3 * ms, 30 * ms, 0.3, 1.0, 3.0, 20]
        prof = [d[(qn >= lo) & (qn < hi)].sum() for lo, hi in zip(bands[:-1], bands[1:])]
        print(f"  m*s={ms:5.3f} Delta={o['Delta']:+.4f} dc_psi={k*o['dc_psi']:+.4f} dc_phi={k*o['dc_phi']:+.4f}  by |q| band "
              + " ".join(f"[{lo:.3g},{hi:.3g}):{p:+.3f}" for lo, hi, p in zip(bands[:-1], bands[1:], prof)))

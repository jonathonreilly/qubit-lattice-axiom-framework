"""T1 variant (a2), continuum limit (images dropped: lattice corrections are O(exp(-pi^2 s^2/2)) times f^2).
Gaussian dispersion (R2 kernel's continuum symbol) for both species + Collins-form Gaussian propagator weight:
  g(q) = exp(-s^2 q^2/2);  w2 = m^2 + (2/s^2)(1-g);  S = q g;  M = m + (r/s)(1-g);  fF = fB = g.
Dimensionless result depends only on (m s, r): scale invariance in s is exact here.
Also reports the literal-kernel flat-band estimate Delta_flat = -16pi^2 s^3/(2 sqrt2 (r+sqrt2)^2).
"""
import numpy as np
from t1_loop import coeffs
from t1_selftest_collins import sph_grid


def run(m, s=1.0, r=1.0, weight=True, twisted=False):
    qv, W = sph_grid(500, 48, 48, 14.0 / s, 1e-4 * m)
    q2 = (qv ** 2).sum(0)
    g = np.exp(-s * s * q2 / 2)
    dg = -s * s * qv[0] * g
    d2g = (-s * s + s ** 4 * qv[0] ** 2) * g
    S = qv * g
    ex = np.zeros_like(qv); ex[0] = 1.0
    dS = ex * g + qv * dg
    d2S = 2 * ex * dg + qv * d2g
    m0 = 0.0 if twisted else m
    M = m0 + (r / s) * (1 - g); dM = -(r / s) * dg; d2M = -(r / s) * d2g
    one, zero = np.ones_like(g), np.zeros_like(g)
    f, df, d2f = (g, dg, d2g) if weight else (one, zero, zero)
    F = dict(S=S, M=M, dS=dS, d2S=d2S, dM=dM, d2M=d2M, fF=f, dfF=df, d2fF=d2f)
    B = dict(w2=m * m + (2 / s ** 2) * (1 - g), dw2=2 * S[0], fB=f, dfB=df)
    return coeffs(W, F, B, mt=(m if twisted else 0.0))


if __name__ == "__main__":
    k = 16 * np.pi ** 2
    for r in (1.0, 0.5, 2.0):
        print(f"continuum a2, r={r}")
        for ms in (0.4, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005):
            o = run(ms, 1.0, r)
            print(f"  m*s={ms:6.3f}  16pi^2 dc_psi={k*o['dc_psi']:+.5f}  16pi^2 dc_phi={k*o['dc_phi']:+.5f}  Delta={o['Delta']:+.5f}")
    for r in (1.0, 0.5, 2.0):
        print(f"continuum a2, r={r}, TWISTED IR mass (no 2mW cross term)")
        for ms in (0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.0025):
            o = run(ms, 1.0, r, twisted=True)
            print(f"  m*s={ms:6.4f}  16pi^2 dc_psi={k*o['dc_psi']:+.5f}  16pi^2 dc_phi={k*o['dc_phi']:+.5f}  Delta={o['Delta']:+.5f}")
    print("scale check (r=1, m*s=0.1): s=1,2,3 ->", [round(run(0.1 / s, s)['Delta'], 8) for s in (1.0, 2.0, 3.0)])
    for r in (0.5, 1.0, 2.0):
        print(f"literal-kernel flat-band estimate r={r}: Delta_flat(s) =", {s: round(-k * s ** 3 / (2 * np.sqrt(2) * (r + np.sqrt(2)) ** 2), 2) for s in (1, 1.5, 2, 2.5, 3)})

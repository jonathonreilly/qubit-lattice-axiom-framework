"""A34 c2: A30's 'speed-only' capture law A = 2u/(1+u) at Gamma = 2t -- general or special?

Own code (not A30's). Semi-infinite chain j = 1, 2, ... with hopping -t, on-site V_j, wall psi_0 = 0,
capture -i Gamma/2 on site 1. Exact stationary scattering by 2-site transfer matrices; flux-normalized.
Cases:
  (a) uniform chain (m = 0): closed form 2 t G s/(t^2 + G^2/4 + t G s), s = sin k;
  (b) staggered mass, A30's termination  V_j = m(-1)^j  (surface site on the -m sublattice), upper band;
  (c) the other termination             V_j = -m(-1)^j (surface site on +m), upper band;
  (d) lower band for both terminations;
For each: A at Gamma = 2t vs 2u/(1+u) (u = v/2t), and the best Gamma and best A at fixed energy.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import signal
import numpy as np
signal.alarm(28)
t = 1.0

def absorb(E, V, G):
    """V: function j -> on-site potential. Returns captured fraction for a wave incident from the right."""
    psi1 = 1.0 + 0j
    psi2 = (V(1) - 0.5j * G - E) * psi1 / t          # from -t psi0 + (V1 - iG/2) psi1 - t psi2 = E psi1, psi0 = 0
    M = lambda j: np.array([[(V(j) - E) / t, -1.0], [1.0, 0.0]], complex)   # [psi_{j+1}, psi_j] = M_j [psi_j, psi_{j-1}]
    C = M(3) @ M(2)                                    # maps [psi_2, psi_1] -> [psi_4, psi_3]
    lam, W = np.linalg.eig(C)
    if not np.allclose(abs(lam), 1, atol=1e-9):
        return np.nan
    cur = np.array([2 * t * np.imag(np.conj(W[1, i]) * W[0, i]) for i in range(2)])   # J_{1->2} = 2t Im(psi1* psi2)
    i_in = int(np.argmin(cur)); i_out = 1 - i_in
    a, b = np.linalg.solve(W, np.array([psi2, psi1]))[[i_in, i_out]]
    R2 = abs(b) ** 2 * abs(cur[i_out]) / (abs(a) ** 2 * abs(cur[i_in]))
    return 1 - R2

def speed(E, m):
    # bands E = +-sqrt(m^2 + 4 t^2 cos^2 k); group speed |dE/dk| = 4 t^2 |cos k sin k| / |E|
    c2 = (E * E - m * m) / (4 * t * t)
    if c2 < 0 or c2 > 1:
        return np.nan
    return 4 * t * t * np.sqrt(c2 * (1 - c2)) / abs(E)

print("(a) uniform chain check vs closed form")
for k in (0.4, 1.0, 1.4):
    E = -2 * t * np.cos(k); s = np.sin(k)
    for G in (0.5, 2.0, 5.0):
        print(f"   k={k} G={G}: own {absorb(E, lambda j: 0.0, G):.12f}  closed {2*t*G*s/(t*t+G*G/4+t*G*s):.12f}")

Gs = np.linspace(0.01, 12, 4800)
for label, sgn in (("(b) A30 termination V_j = m(-1)^j", 1), ("(c) other termination V_j = -m(-1)^j", -1)):
    print(label)
    for m in (0.2, 0.6):
        V = lambda j, m=m: sgn * m * (-1) ** j
        for band in (+1, -1):
            worst_law = 0.0; rows = []
            for frac in (0.05, 0.3, 0.6, 0.9):          # position in the band: E^2 = m^2 + frac*4t^2
                E = band * np.sqrt(m * m + frac * 4 * t * t)
                u = speed(E, m) / (2 * t)
                A2 = absorb(E, V, 2.0)
                As = np.array([absorb(E, V, G) for G in Gs])
                i = int(np.nanargmax(As))
                worst_law = max(worst_law, abs(A2 - 2 * u / (1 + u)))
                rows.append(f"E={E:+.3f} u={u:.3f}: A(G=2t)={A2:.4f} vs 2u/(1+u)={2*u/(1+u):.4f}; best G={Gs[i]:.3f}, best A={As[i]:.4f}")
            print(f"   m={m} {'upper' if band > 0 else 'lower'} band: max|A(2t) - 2u/(1+u)| = {worst_law:.2e}")
            for r in rows:
                print("      " + r)

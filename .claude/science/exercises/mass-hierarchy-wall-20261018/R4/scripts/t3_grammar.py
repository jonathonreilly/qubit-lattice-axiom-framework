"""T3: density of the formula grammar c * alpha_s(v)^p used for main's staircase/atlas readings."""
from fractions import Fraction
import numpy as np
from common import ALPHA_SV

rng = np.random.default_rng(3)
P = sorted({Fraction(a, b) for b in range(1, 7) for a in range(1, 4 * b + 1)})
C = [1, 2, 3, 6, 1/2, 1/3, 1/6, 2**.5, 3**.5, 6**.5, 2**-.5, 3**-.5, 6**-.5, 4/3, 3/4, 5/6, 6/5]
G = np.array([c * ALPHA_SV ** float(p) for p in P for c in C])
G = np.unique(np.round(np.log(G), 12))
print(f"alpha_s(v) = {ALPHA_SV:.5f}; exponents {len(P)}, prefactors {len(C)}, distinct values {len(G)}")
x = rng.uniform(np.log(1e-4), 0.0, size=200000)
idx = np.searchsorted(G, x)
d = np.minimum(np.abs(x - G[np.clip(idx - 1, 0, len(G) - 1)]), np.abs(G[np.clip(idx, 0, len(G) - 1)] - x))
for tol in (0.013, 0.03, 0.033, 0.186):
    print(f"P(random target in [1e-4,1] matched within {100*tol:.1f}%) = {np.mean(d <= np.log(1 + tol)):.3f}")
print("main readings (comparators): alpha/2 =", round(ALPHA_SV / 2, 5), "vs m_d/m_s 0.0500;",
      "sqrt(alpha/2) =", round((ALPHA_SV / 2) ** .5, 4), "vs |Vus| 0.2243;",
      "alpha/sqrt6 =", round(ALPHA_SV / 6 ** .5, 5), "vs |Vcb| 0.0410")
# restricted grammar: integer exponents only, prefactors {1, 1/2, 1/sqrt2, 1/sqrt6, 1/6}
G2 = np.unique([np.log(c * ALPHA_SV ** p) for p in (0.5, 1, 1.5, 2, 2.5, 3) for c in (1, 1/2, 2**-.5, 6**-.5, 1/6, 1/3, 3**-.5)])
idx = np.searchsorted(G2, x)
d2 = np.minimum(np.abs(x - G2[np.clip(idx - 1, 0, len(G2) - 1)]), np.abs(G2[np.clip(idx, 0, len(G2) - 1)] - x))
print(f"small grammar ({len(G2)} values: half-integer powers, 7 prefactors): P(match within 3.3%) = {np.mean(d2 <= np.log(1.033)):.3f}, within 1.3% = {np.mean(d2 <= np.log(1.013)):.3f}")

"""K4: is R4's Koide joint chance right?  R4 multiplied P(Q hit) by the UNCONDITIONAL P(delta hit).
At Q = 2/3 (r = sqrt2) positive roots confine delta to [0, pi/12]; the observed delta = 2/9 sits near
the edge where m1 -> 0, which a log-uniform null favours.  Measure P(delta hit | Q near 2/3)."""
from fractions import Fraction
import numpy as np
rng = np.random.default_rng(41)
me, mt = 0.4866e-3, 172.1           # R4's N1 range [m_e, m_t]
eps_d = 8.3e-6                      # R4's delta window
# R4's delta grammar (63 values in [0, pi/3])
DG_rad = sorted({Fraction(a, b) for b in range(1, 13) for a in range(0, 2 * b) if a / b <= np.pi / 3})
DG_pi = sorted({Fraction(a, b) for b in range(1, 13) for a in range(0, b + 1) if a / b <= 1 / 3})
dg = np.unique(np.concatenate([[float(x) for x in DG_rad], [np.pi * float(x) for x in DG_pi]]))
def koide_brannen(M):
    v = np.sqrt(M); a0 = v.mean(-1)
    z = (v * np.exp(-2j * np.pi * np.arange(3) / 3)).sum(-1) / 3
    d = np.mod(np.angle(z), 2 * np.pi / 3); d = np.where(d > np.pi / 3, 2 * np.pi / 3 - d, d)
    return (v ** 2).sum(-1) / v.sum(-1) ** 2, d
hw = 2e-3                           # conditioning window on Q
dsel, dall = [], []
for _ in range(30):                 # 30 x 2e5 samples, chunked (low memory)
    M = np.exp(rng.uniform(np.log(me), np.log(mt), size=(200_000, 3)))
    Q, d = koide_brannen(M)
    dsel.append(d[np.abs(Q - 2 / 3) < hw]); dall.append(d[:40_000])
dsel = np.concatenate(dsel); dall = np.concatenate(dall)
print(f"samples with |Q-2/3| < {hw}: {len(dsel)}; their delta range [{dsel.min():.4f}, {dsel.max():.4f}] (pi/12 = {np.pi/12:.4f})")
bw = 0.004
def dens(x, at): return np.mean(np.abs(x - at) < bw / 2) / bw
rc, ru = dens(dsel, 2 / 9), dens(dall, 2 / 9)
print(f"density of delta at 2/9: conditional on Q~2/3 {rc:.2f}/rad; unconditional {ru:.2f}/rad; ratio {rc/ru:.1f}")
pc = sum(dens(dsel, g) * 2 * eps_d for g in dg)
pu = sum(dens(dall, g) * 2 * eps_d for g in dg)
n_in = np.sum(dg <= np.pi / 12)
print(f"P(delta within {eps_d:.1e} of any of {len(dg)} grammar values): unconditional {pu:.2e} (R4: 8.41e-04); "
      f"conditional on Q~2/3 {pc:.2e}  [{n_in} grammar values lie in the allowed range]")
pQ30 = 5.95e-4; pQ1 = 1.60e-5
print(f"joint x3 sectors: R4 {3*pQ30*8.41e-4:.1e};  corrected (30 Q targets) {3*pQ30*pc:.1e};  "
      f"Q as the single 1983-predicted target {3*pQ1*pc:.1e}")
for T in (63, 300, 1000):
    print(f"   if the honest delta grammar had {T} values at the same conditional density: joint (30 Q) ~ {3*pQ30*pc*T/len(dg):.1e}")

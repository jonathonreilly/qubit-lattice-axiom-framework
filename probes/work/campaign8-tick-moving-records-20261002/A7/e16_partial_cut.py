"""E16: triangle family with a PARTIAL cut of A's possibilities at A's readable time-1
position (weight lam: rho -> (1-lam) rho + lam * sum_a Pi_a rho Pi_a).  For which lam do the
triangle intervals for P(a1 != a3) overlap for every pair of B choices theta0, theta1 and
every A rotation phi?  (Necessary condition for no-signalling; grid scan.)
"""
import numpy as np
th = np.linspace(0, np.pi, 181)
ph = np.linspace(0, np.pi, 181)
def worst_gap(lam):
    worst = -1.0
    for p in ph:
        d1 = np.sin(th) ** 2
        e3 = (1 - lam) * np.sin(p - th) ** 2 + lam * (d1 * np.cos(p) ** 2 + (1 - d1) * np.sin(p) ** 2)
        lo = np.abs(d1 - e3)
        hi = np.minimum(d1 + e3, 2 - d1 - e3)
        worst = max(worst, lo.max() - hi.min())     # > 0 means no common P(a1 != a3)
    return worst
for lam in [0.0, 0.1, 0.2, 0.25, 0.29, 0.3, 0.4, 0.5, 0.586, 0.7, 1.0]:
    print(f"lam={lam:5.3f}: worst triangle gap over settings = {worst_gap(lam):+.4f}")
lo, hi = 0.0, 1.0
for _ in range(40):
    mid = (lo + hi) / 2
    if worst_gap(mid) > 1e-12: lo = mid
    else: hi = mid
print(f"threshold lam* (triangle family, grid 1 deg) ~ {hi:.4f};  1 - 1/sqrt2 = {1-1/np.sqrt(2):.4f}")

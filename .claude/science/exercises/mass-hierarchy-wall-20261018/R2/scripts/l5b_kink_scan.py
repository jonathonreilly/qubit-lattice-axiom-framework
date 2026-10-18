"""R2 / L5b: distribution of |Vcb|/|Vus| for kink (sech^p) zero-mode overlaps in the clustered limit,
two cluster sizes to check convergence; also with the Q cluster equally spaced."""
import numpy as np
rng = np.random.default_rng(4)
t = np.linspace(-40, 40, 8001); dt = t[1] - t[0]
prof = lambda p, c: np.cosh(t - c) ** (-p)
def run(scale, xq, xu, xd, pQ, pu, pd, cu, cd, ku, kd):
    PQ = np.array([prof(pQ, scale * x) for x in xq])
    Pu = np.array([prof(pu, scale * ku * x + cu) for x in xu]); Pd = np.array([prof(pd, scale * kd * x + cd) for x in xd])
    Uu = np.linalg.svd(PQ @ Pu.T * dt)[0]; Ud = np.linalg.svd(PQ @ Pd.T * dt)[0]
    V = np.abs(Uu.T @ Ud); return V[0, 1] / V[1, 2], V
for label, eq in [("random Q shapes", False), ("equally spaced Q", True)]:
    r, drift = [], []
    for trial in range(250):
        xq = np.array([-1.0, 0.0, 1.0]) if eq else np.sort(rng.normal(size=3))
        xu, xd = [np.sort(rng.normal(size=3)) for _ in range(2)]
        pQ, pu, pd = rng.uniform(0.5, 3.0, size=3); cu, cd = rng.uniform(-1.5, 1.5, size=2)
        ku, kd = rng.uniform(0.5, 2, size=2)
        a, _ = run(0.01, xq, xu, xd, pQ, pu, pd, cu, cd, ku, kd)
        b, _ = run(0.005, xq, xu, xd, pQ, pu, pd, cu, cd, ku, kd)
        r.append(b); drift.append(abs(a / b - 1))
    r = np.array(r)
    print(f"{label}: |Vcb|/|Vus| percentiles 1/5/50/95 = {np.percentile(r,[1,5,50,95]).round(3)}; "
          f"fraction <= 0.55: {np.mean(r<=0.55):.3f}; fraction <= 0.3: {np.mean(r<=0.3):.3f}; median drift delta 0.01->0.005: {np.median(drift):.2e}")

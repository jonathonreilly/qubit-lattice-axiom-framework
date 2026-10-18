import numpy as np, sys
sys.path.insert(0, '.')
from fifth import null5, R
Qe, Mh = R.regge(np.eye(4)); HC = R.HC; U = np.ones(4)
vec = lambda h: np.array([h[x, y] for (x, y) in HC], complex)
def gauge_metric(q):   # continuum gauge directions in metric variables: h = q xi + xi q
    return np.array([vec(np.outer(q, e) + np.outer(e, q)) for e in np.eye(4)]).T
rng = np.random.default_rng(1)
for t in range(5):
    q = rng.standard_normal(4)*(0.02 if t < 3 else 0.4)
    f, _, _ = null5(q); M = Mh(q); a, *_ = np.linalg.lstsq(M, f, rcond=None)
    G = gauge_metric(q); P = np.eye(10) - G @ np.linalg.pinv(G)
    # metric inner product weights: off-diagonal vars count twice in tr(hh)
    W = np.diag([1, 1, 1, 1, 2, 2, 2, 2, 2, 2.0])
    x = P @ a; best = None
    for name, H in {'uu-2d': np.outer(U, U) - 2*np.eye(4), 'uu': np.outer(U, U), 'delta': np.eye(4)}.items():
        y = P @ vec(H)
        c = abs(np.conj(x) @ W @ y)/np.sqrt(abs(np.conj(x) @ W @ x)*abs(np.conj(y) @ W @ y))
        print(f"  |q|={np.linalg.norm(q):.3f} cos(fifth metric part mod gauge, {name}) = {c:.6f}")

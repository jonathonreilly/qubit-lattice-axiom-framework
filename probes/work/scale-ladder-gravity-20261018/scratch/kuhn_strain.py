"""Kuhn complex, hypercubic lengths: does a relative-strain least-squares site metric (over its 15 edge classes,
all site-site) see the fifth zero-action direction?"""
import sys, numpy as np
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4
HC = R.HC; D15 = [np.array(v, float) for v in R4.DIRS15]; I4 = np.eye(4); U = np.ones(4)
Dm = np.array([[v[a]*v[b]*(2 if a != b else 1) for a, b in HC] for v in D15])
def readings(k, w):
    """per-cell metric from edge variables delta l (Bloch, anchor phases): delta(l^2) = 2 l dl; weights w on relative strain."""
    l = np.array([np.linalg.norm(v) for v in D15]); Rm = np.diag(2*l)       # Bloch: each class once per cell
    W = np.diag(w/(l**2))
    return np.linalg.pinv(W @ Dm) @ (W @ Rm)
Qe, Mh = R.regge(I4)
def gauge(k):
    G = np.zeros((15, 4), complex)
    for c, v in enumerate(D15): G[c] = (np.exp(1j*k @ v) - 1)*v/np.linalg.norm(v)
    return G
def fifth(k):
    _, _, vh = np.linalg.svd(Qe(k)); N = vh[-5:].conj().T; G = gauge(k)
    r = N - G @ np.linalg.pinv(G) @ N; return np.linalg.svd(r)[0][:, 0]
nn = np.array([np.sum(v) for v in D15])            # 1..4 (edge "order")
for name, w in {'uniform relative strain': np.ones(15), 'axis only weight': (nn == 1)*1.0 + 1e-9, 'equal per class order': 1/np.array([4, 6, 4, 1])[nn.astype(int)-1]}.items():
    out = []
    for q in [np.array([0.02, 0.01, -0.015, 0.012]), np.array([0.02, 0, 0, 0.0]), np.array([0.3, -0.2, 0.25, 0.1])]:
        f = fifth(q); L = readings(q, w)
        out.append(np.linalg.norm(L @ f))
    print(f"{name:24s}: |L f| = " + ", ".join(f"{x:.3e}" for x in out))
# the fifth mode's edge pattern at small q (per edge order)
f = fifth(np.array([0.002, 0.001, -0.0015, 0.0012])); f = f/f[np.argmax(abs(f))]
print("fifth mode edge pattern (normalised) by edge:", [(tuple(v.astype(int)), round(abs(f[c]), 3)) for c, v in enumerate(D15)])

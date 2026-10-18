import numpy as np, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import fem
    from regge_project import build
from fem import SIMPLICES, simplex_geom
def scalar_hol(k, g0):
    gi = np.linalg.inv(g0); S = 0j
    for vs in SIMPLICES:
        E, vol = simplex_geom(vs, g0)
        gp = np.linalg.solve(E, np.array([np.exp(1j*k@v) for v in vs])[1:] - np.exp(1j*k@vs[0]))
        gm = np.linalg.solve(E, np.array([np.exp(-1j*k@v) for v in vs])[1:] - np.exp(-1j*k@vs[0]))
        S += vol * gm @ gi @ gp
    return S
def newton_root(f, w0):
    w = w0
    for _ in range(60):
        h = 1e-7*max(abs(w), 1); d = (f(w+h)-f(w-h))/(2*h); step = f(w)/d; w -= step
        if abs(step) < 1e-15: break
    return w
rng = np.random.default_rng(11)
U = np.ones(4)
for b in [0.3, -0.15, 0.0]:
    g0 = np.eye(4) + b*np.outer(U, U)
    _, Qe = build(g0)
    for trial in range(4):
        n = rng.standard_normal(3); n /= np.linalg.norm(n); km = rng.uniform(0.2, 1.4)
        ks = km*n
        # scalar root in complex omega: S(ks, k_t) = 0 with k_t complex (b != 0 gives complex root)
        f = lambda kt: scalar_hol(np.array([*ks, kt]), g0)
        kt = newton_root(f, 1j*km)
        p = np.array([*ks, kt])
        sr = np.sort(np.linalg.svd(Qe(p), compute_uv=False)); sr /= sr[-1]
        po = np.array([*ks, kt*1.01]); so = np.sort(np.linalg.svd(Qe(po), compute_uv=False)); so /= so[-1]
        print(f"b={b:+.2f} k={km:.2f} kt={kt:.6f} |S|={abs(f(kt)):.0e} regge sv5..8 {np.array2string(sr[4:8],precision=1)} off {np.array2string(so[5:7],precision=1)}")

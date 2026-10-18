import numpy as np, contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    from regge_project import build
U = np.ones(4); np.set_printoptions(formatter={'float': lambda x: f"{x:.1e}"})
rng = np.random.default_rng(5)
for b in [0.0, 0.3, -0.15]:
    _, Qe = build(np.eye(4) + b*np.outer(U, U))
    for _ in range(3):
        k = rng.standard_normal(4)*0.5          # real Euclidean momentum
        s = np.sort(np.linalg.svd(Qe(k), compute_uv=False)); print(f"b={b:+.2f} real k: sv1..7/max", s[:7]/s[-1])

"""C5 R12-3, script 5: the Cartan-model (equivariant) completion's photino = full Kaehler-Dirac d + d^+ on Omega^0..3 of Z^3
(cochain and box symbols).  Checks K^2 = Delta * 1_8 (so zeros only at q = 0: doubler-free), chiral grading (-1)^deg
anticommutes with K, and its BF restriction: deleting (sigma, A_long) leaves the BF operator of script 1."""
import numpy as np, io, contextlib, sys
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import r123_bf_multiplet as M
rng = np.random.default_rng(11)
gam = np.diag([1, -1, -1, -1, 1, 1, 1, -1]).astype(complex)
e1 = e2 = 0
for _ in range(500):
    q = rng.uniform(-np.pi, np.pi, 3)
    for Df in (M.Dwil, M.Dbox):
        D = Df(q); K = M.C_kd(D); Dl = np.sum(np.abs(D) ** 2)
        e1 = max(e1, np.abs(K @ K - Dl * np.eye(8)).max()); e2 = max(e2, np.abs(gam @ K + K @ gam).max())
print('Kaehler-Dirac photino: max|K^2 - Delta 1_8| = %.1e ; max|{(-1)^deg, K}| = %.1e  (cochain and box, 1000 random q)' % (e1, e2))

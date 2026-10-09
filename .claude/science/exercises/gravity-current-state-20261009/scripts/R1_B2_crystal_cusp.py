"""B2: jittered square crystal (30x30), T2g shear, adjacency frozen vs re-triangulated.
Pre-stated: 'cusp' iff E_retri(eps) - E_retri(0) is ~ -s|eps| (slope ratio at eps and 2 eps ~ 2)."""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("B", "B_liquid_glass_crystal.py")
src = open("B_liquid_glass_crystal.py").read().split("which = sys.argv")[0]
ns = {}; exec(src, ns)
rng = np.random.default_rng(7)
m = 30; g1 = np.arange(m) + 0.5
from itertools import product
X = np.array(list(product(g1, repeat=2)), float) + 1e-3 * rng.standard_normal((m*m, 2))
A0 = m * np.eye(2); S = np.array([[0, 1.0], [1.0, 0]])
vid0, voff0 = ns["periodic_delaunay"](X, A0)
for e in (-0.02, -0.01, -0.005, 0.0, 0.005, 0.01, 0.02):
    M = ns["expm_sym"](S, e); Y, A = X @ M.T, A0 @ M.T
    Ef = ns["E_vac"](ns["stiffness"](Y, A, vid0, voff0))[0] / len(X)
    v, o = ns["periodic_delaunay"](Y, A)
    Er = ns["E_vac"](ns["stiffness"](Y, A, v, o))[0] / len(X)
    print(f"eps={e:+.3f}  E_frozen={Ef:.7f}  E_retri={Er:.7f}")

"""Vertices of the sign-correct Fierz polygon (lambda1 = 0): which families can be dropped (det factorisation check)."""
import sys, os, itertools, io, contextlib
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
fm = FlavourModel("spin10")
with contextlib.redirect_stdout(io.StringIO()):
    kap, info = fm.fierz(verbose=lambda *a: None)
names, K, k0, sgn = info["names"], info["kernel"].T, info["k0"], info["sgn"]
s = np.array([sgn[n] for n in names], float)
for zero in itertools.combinations(range(4), 2):
    # solve k0 + K x with components in `zero` set to 0
    A = K[list(zero)]; b = -k0[list(zero)]
    x = np.linalg.solve(A, b)
    kv = k0 + K @ x
    ok = np.all(s * kv >= -1e-12)
    print(f"families set to 0: {[names[i] for i in zero]} -> kappa {dict(zip(names, np.round(kv, 6).tolist()))}; sign-correct {ok}")

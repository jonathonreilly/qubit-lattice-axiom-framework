"""Resumable long L-BFGS at range r=2 from the E3-truncated seed; track F(evaluations)."""
import os
import sys
import time
import numpy as np
from scipy.optimize import minimize

sys.argv = [sys.argv[0], "2", "0"]
exec(open("run5_search.py").read().split("# seed (a)")[0])
t0 = time.time()
fn = "r2_state.npz"
if os.path.exists(fn):
    st = np.load(fn)
    x, nev, hist = st["x"], int(st["nev"]), list(st["hist"])
else:
    Nf = 32
    U3, _ = E3(grid(Nf))
    C = np.fft.fftn(U3.reshape(Nf, Nf, Nf, 2, 2), axes=(0, 1, 2)) / Nf ** 3
    A0 = np.array([C[int(v[0]) % Nf, int(v[1]) % Nf, int(v[2]) % Nf].reshape(4) for v in vs])
    x, nev, hist = pack(A0), 0, []
while time.time() - t0 < 42:
    res = minimize(F_and_grad, x, jac=True, method="L-BFGS-B",
                   options={"maxiter": 10 ** 6, "maxfun": 10000, "ftol": 1e-30, "gtol": 1e-18, "maxcor": 50})
    x = res.x
    nev += res.nfev
    hist.append((nev, res.fun, np.linalg.norm(res.jac)))
    print(f"  evals {nev:7d}: F = {res.fun:.4e}  |grad| = {np.linalg.norm(res.jac):.2e}", flush=True)
np.savez(fn, x=x, nev=nev, hist=np.array(hist))
report("current", x)

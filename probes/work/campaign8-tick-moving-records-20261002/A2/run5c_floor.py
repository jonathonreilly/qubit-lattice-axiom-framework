"""Does the unitarity defect of a W3 != 0 strictly local map saturate at a positive floor?
Long L-BFGS from the E3-truncated seed at range r; print F along the way, then W3 and smin.
"""
import sys
import time
import numpy as np
from scipy.optimize import minimize

sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else "2", "0"]
src = open("run5_search.py").read().split("# seed (a)")[0]
exec(src)

t0 = time.time()
Nf = 32
Kf = grid(Nf)
U3, _ = E3(Kf)
C = np.fft.fftn(U3.reshape(Nf, Nf, Nf, 2, 2), axes=(0, 1, 2)) / Nf ** 3
A0 = np.array([C[int(v[0]) % Nf, int(v[1]) % Nf, int(v[2]) % Nf].reshape(4) for v in vs])
x = pack(A0)
hist = []
for block in range(6):
    res = minimize(F_and_grad, x, jac=True, method="L-BFGS-B",
                   options={"maxiter": 100000, "maxfun": 8000, "ftol": 1e-30, "gtol": 1e-16, "maxcor": 30})
    x = res.x
    hist.append(res.fun)
    print(f"  after block {block}: F = {res.fun:.4e}  ({res.message})", flush=True)
    if time.time() - t0 > 40:
        break
report("final", x)
print(f"time {time.time()-t0:.1f}s")

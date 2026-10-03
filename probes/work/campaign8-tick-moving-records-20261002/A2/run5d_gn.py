"""Second-order polish (Levenberg-Marquardt, normal equations) of the range-2 W3=-1 near-unitary
map: does the residual go to zero (=> exact unitary with W3=-1, contradicting the theorem) or
stall at a positive stationary value (gradient -> 0 with F > 0)?
"""
import sys
import time
import numpy as np
from scipy.optimize import minimize

sys.argv = [sys.argv[0], "2", "0"]
exec(open("run5b_lm.py").read().split("rows = []")[0])
from models import E3

t0 = time.time()
Nf = 32
Kf32 = grid(Nf)
U3, _ = E3(Kf32)
C = np.fft.fftn(U3.reshape(Nf, Nf, Nf, 2, 2), axes=(0, 1, 2)) / Nf ** 3
A0 = np.array([C[int(v[0]) % Nf, int(v[1]) % Nf, int(v[2]) % Nf].reshape(4) for v in vs])
x = np.concatenate([A0.real.ravel(), A0.imag.ravel()])
x = minimize(F_and_grad, x, jac=True, method="L-BFGS-B",
             options={"maxiter": 100000, "maxfun": 12000, "ftol": 1e-30, "gtol": 1e-16, "maxcor": 30}).x
e = resid(x)
print(f"start LM: 0.5|e|^2={0.5*e@e:.4e}  ({time.time()-t0:.1f}s)", flush=True)
lam = 1e-6
for it in range(40):
    J = jacfun(x)
    g = J.T @ e
    H = J.T @ J
    while True:
        dx = -np.linalg.solve(H + lam * np.diag(np.diag(H)) + 1e-300 * np.eye(len(x)), g)
        e_new = resid(x + dx)
        if e_new @ e_new < e @ e:
            x, e = x + dx, e_new
            lam = max(lam / 3, 1e-12)
            break
        lam *= 4
        if lam > 1e8:
            break
    print(f"  it {it:2d}: 0.5|e|^2={0.5*e@e:.4e}  |J^T e|={np.linalg.norm(g):.2e}  lam={lam:.1e}"
          f"  ({time.time()-t0:.1f}s)", flush=True)
    if time.time() - t0 > 48 or lam > 1e8:
        break
ev = np.linalg.eigvalsh(H)
print(f"J^T J eigenvalues: min {ev.min():.2e}, 5th {ev[4]:.2e}, max {ev.max():.2e}")
print("final (sup defect, min sing val, W3):", measure(x))

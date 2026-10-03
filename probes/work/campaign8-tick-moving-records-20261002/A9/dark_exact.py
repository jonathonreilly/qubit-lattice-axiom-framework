"""Deterministic check of the dark-state claim in magnon_toy variant A (no sampling):
P(no record ever) = lim_T ||(K0 U)^T psi0||^2 should equal |<uniform|psi0>|^2."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "magnon_toy.py")).read()
exec(src.split("# exact checks")[0])
x0 = N // 2
U = change(np.zeros(N, int))
sF, s1 = MATS[("A", UNL, UNL)]
K0 = [np.eye(N, dtype=complex) for _ in range(3)]
for r in range(3):
    for x in range(r, N, 3):
        idx = [(x - 1) % N, x, (x + 1) % N]
        K0[r][np.ix_(idx, idx)] = s1
step = K0[2] @ K0[1] @ K0[0] @ U
uni = np.ones(N) / np.sqrt(N)
cases = {"one site": np.eye(N)[x0].astype(complex)}
for k, sig in ((0.3, 3.0), (0.0, 6.0), (1.2, 3.0)):
    v = np.exp(1j * k * np.arange(N) - (np.arange(N) - x0) ** 2 / (2 * sig ** 2)); cases[f"k={k} w={sig}"] = v / np.linalg.norm(v)
for name, psi0 in cases.items():
    w = psi0.copy(); out = []
    for T in range(1, 3001):
        w = step @ w
        if T in (100, 1000, 3000):
            out.append(np.vdot(w, w).real)
    dark = abs(np.vdot(uni, psi0)) ** 2
    print(f"{name:12s}: P(no record by T=100,1000,3000) = {out[0]:.8f}, {out[1]:.8f}, {out[2]:.8f}; "
          f"|<u|psi0>|^2 = {dark:.8f}; diff at 3000 = {out[2]-dark:.1e}")

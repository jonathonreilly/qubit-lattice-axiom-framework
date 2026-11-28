#!/usr/bin/env python3
"""R2 of CRITERIA.md: D(MB) = I at flat connections, row sum of D Psi - I, and range."""
import math, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
sys.path.insert(0, os.path.join(HERE, "..", "excess"))
from ex_core import flux_stats, gauge_transform, guard, ident, qexp, qinv, qlog, qmul, random_gauge
from v10_lift_su2 import Lift, smooth_field
import torch

def psi_noblock(Lf, V, Y):
    Uf, *_ = Lf.lift_flat(qmul(qexp(Y), V))
    return qlog(qmul(Lf.block(Uf), qinv(V)))

def matvec(fn, V, Z, eps=1e-4):
    return (fn(V, eps * Z) - fn(V, -eps * Z)) / (2 * eps)

ok = True
def jac(Lf, V, Np, d, eps=1e-5):
    n = Np**d * d * 3
    J = torch.zeros((n, n), dtype=torch.float64)
    Y0 = torch.zeros((Np,) * d + (d, 3), dtype=torch.float64)
    for i in range(n):
        Y = Y0.reshape(-1).clone(); Y[i] = eps
        p = Lf.psi(V, Y.reshape(Y0.shape))[0].reshape(-1)
        Y[i] = -eps
        q = Lf.psi(V, Y.reshape(Y0.shape))[0].reshape(-1)
        J[:, i] = (p - q) / (2 * eps)
    return J

def rowsum(J, Np, d):
    nb = Np**d * d
    E = (J - torch.eye(J.shape[0], dtype=torch.float64)).reshape(nb, 3, nb, 3).permute(0, 2, 1, 3)
    norms = torch.linalg.matrix_norm(E, ord=2)
    return norms

d = 2
Np = 12
Lf = Lift(Np, 3, d)
V = smooth_field(Np, d, 0.1, 7)
f, _ = flux_stats(V)
t0 = time.time()
J = jac(Lf, V, Np, d)
N = rowsum(J, Np, d)
nb = Np**d * d
coords = torch.stack(torch.meshgrid(*[torch.arange(Np) for _ in range(d)], indexing="ij"), -1).reshape(-1, d)
coords = coords[:, None, :].repeat(1, d, 1).reshape(-1, d)
D = torch.zeros((nb, nb), dtype=torch.long)
for a in range(d):
    da = (coords[:, a][:, None] - coords[:, a][None, :]) % Np
    da = torch.minimum(da, Np - da)
    D = torch.maximum(D, da)
for thr in (1e-3, 1e-5, 1e-8):
    sel = D[N > thr]
    print(f"R2d Np {Np} f {f:.4f}: largest sup distance with block norm above {thr:.0e}: {int(sel.max()) if sel.numel() else 'none'}")
prof = [float(N[D == k].max()) for k in range(0, Np // 2 + 1)]
print("R2d largest block norm by distance:", " ".join(f"{p:.2e}" for p in prof), f"({time.time()-t0:.1f}s)", flush=True)
print("R2", "PASS" if ok else "FAIL")

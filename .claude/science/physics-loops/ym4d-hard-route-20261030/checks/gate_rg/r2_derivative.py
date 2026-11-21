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
for d, Np in ((2, 8), (3, 8), (4, 4)):
    t0 = time.time()
    Lf = Lift(Np, 3, d)
    shape = (Np,) * d + (d, 3)
    g = torch.Generator().manual_seed(11 + d)
    Z = torch.randn(shape, generator=g, dtype=torch.float64)
    Z = Z / Z.norm(dim=-1, keepdim=True)
    V1 = ident((Np,) * d + (d,))
    Vg = gauge_transform(V1, random_gauge((Np,) * d, d, seed=3))
    psi = lambda V, Y: Lf.psi(V, Y)[0]
    e1 = float((matvec(psi, V1, Z) - Z).norm(dim=-1).max())
    eg = float((matvec(psi, Vg, Z) - Z).norm(dim=-1).max())
    # gauge direction: Z = dlambda at V = 1
    lam = torch.randn((Np,) * d + (3,), generator=g, dtype=torch.float64)
    Zg = torch.stack([torch.roll(lam, -1, dims=mu) * 0 + lam - torch.roll(lam, -1, dims=mu) for mu in range(d)], d)
    eh = float((matvec(psi, V1, Zg) - Zg).norm(dim=-1).max())
    ectl = float((matvec(lambda V, Y: psi_noblock(Lf, V, Y), V1, Z) - Z).norm(dim=-1).max())
    a_ok = e1 < 1e-6 and eg < 1e-6 and eh < 1e-6
    b_ok = ectl > 1e-2
    ok &= a_ok and b_ok
    print(f"R2a d {d} Np {Np}: V=1 {e1:.2e}, pure gauge V {eg:.2e}, gauge Z {eh:.2e} {'PASS' if a_ok else 'FAIL'}; R2b control, no block gauge {ectl:.3e} {'PASS' if b_ok else 'FAIL'} ({time.time()-t0:.1f}s)", flush=True)
    guard()

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

d, Np = 2, 8
Lf = Lift(Np, 3, d)
rows = []
for amp in (0.2, 0.1, 0.05):
    V = smooth_field(Np, d, amp, 7)
    f, _ = flux_stats(V)
    t0 = time.time()
    J = jac(Lf, V, Np, d)
    N = rowsum(J, Np, d)
    rs = float(N.sum(1).max())
    rows.append((f, rs))
    print(f"R2c f {f:.4f}: max row sum {rs:.4f}, row sum/f {rs/f:.3f} ({time.time()-t0:.1f}s)", flush=True)
    guard()
c_ok = max(r[1] / r[0] for r in rows) <= 2 * min(r[1] / r[0] for r in rows) and all(rows[i][1] / rows[i + 1][1] >= 1.5 for i in range(2))
ok &= c_ok
print("R2c", "PASS" if c_ok else "FAIL", flush=True)

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
    print(f"R2d Np {Np} f {f:.4f}: largest sup distance with block norm above {thr:.0e}: {int(D[N > thr].max())}")
prof = [float(N[D == k].max()) for k in range(0, Np // 2 + 1)]
print("R2d largest block norm by distance:", " ".join(f"{p:.2e}" for p in prof), f"({time.time()-t0:.1f}s)", flush=True)
print("R2", "PASS" if ok else "FAIL")

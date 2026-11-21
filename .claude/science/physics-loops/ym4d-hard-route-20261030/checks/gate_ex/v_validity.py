#!/usr/bin/env python3
"""V1 to V4 of CRITERIA.md."""
import importlib.util, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *

# V1: covariance
ch = Chain(2, 3, 4, 1)
t = 0.15 * torch.randn(ch.n, ch.n, ch.n, ch.n, 4, 3, generator=torch.Generator().manual_seed(1))
U = qexp(t)
g = random_gauge((ch.n,) * 4, 4, seed=2)
Ug = gauge_transform(U, g)
V, Vg = ch.top(U), ch.top(Ug)
b = ch.levels[0]
gc = g[tuple(b.base[i] % ch.n for i in range(4))].reshape(2, 2, 2, 2, 4)
pred = gauge_transform(V, gc)
print("V1 covariance residual", float((pred - Vg).abs().max()))

# V3: abelian wave, N' = 2 and 3
def abelian_wave(Np, P, a, colour=2, amp=0.02, d=4):
    x = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64)] * d, indexing="ij")
    ph = sum(2 * np.pi * P[i] / Np * x[i] for i in range(d))
    t = torch.zeros((Np,) * d + (d, 3))
    for mu in range(d):
        t[..., mu, colour] = amp * a[mu] * torch.cos(ph)
    return qexp(t)

spec = importlib.util.spec_from_file_location("exc", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hard-core--mapped_excess.py"))
sys.argv = ["x"]
exc = importlib.util.module_from_spec(spec); spec.loader.exec_module(exc)

for Np, P, a in [(2, (1, 0, 0, 0), (0, 1, 0, 0)), (3, (1, 0, 0, 0), (0, 1, 0, 0)), (3, (1, 1, 0, 0), (1, -1, 1, 0))]:
    ch = Chain(Np, 3, 4, 1)
    V = abelian_wave(Np, P, a)
    pb = Problem(ch, V)
    t0 = time.time()
    U, lam, gn, rn = pb.solve(pb.initial(), verbose=True)
    e = float(wilson(U) - wilson(V))
    f, E = flux_stats(V)
    I = float(I_grad(V))
    Pv = 2 * np.pi * np.array(P, float) / Np
    Phat = 2 * np.sin(Pv / 2)
    # forms returns (Min, E) in the transverse basis
    Min, En = exc.forms(Pv, 3, 1, 4)[:2]
    u = Phat / np.linalg.norm(Phat)
    av = np.array(a, float)
    ap = av - u * (u @ av)
    Perp = np.linalg.svd(np.eye(4) - np.outer(u, u))[0][:, :3]
    c = Perp.T @ ap
    gP = float(c @ Min @ c / (c @ c))
    print(f"V3 N'={Np} P={P}: e/E={e/E:.6f} I/E={I/E:.5f} e/I={e/I:.5f} g-1={gP-1:.6f} f={f:.4f} g,r={gn:.1e},{rn:.1e} t={time.time()-t0:.1f}s", flush=True)

    # V4: tangent perturbations do not lower S
    S0 = float(wilson(U))
    worst = 1e9
    for s in range(20):
        v = 1e-3 * torch.randn(pb.shape, generator=torch.Generator().manual_seed(s))
        # project approximately onto ker J at the flat preconditioner, then fix the constraint by Newton in the normal direction
        w = qmul(qexp(v - pb.kinv(pb.jt(U, pb.g0inv(pb.j(U, v))))), U)
        for _ in range(4):
            r = pb.resid(w)
            w = qmul(qexp(-pb.kinv(pb.jt(w, pb.g0inv(r)))), w)
        worst = min(worst, float(wilson(w)) - S0)
    print("V4 min S change over feasible perturbations", worst, "final resid", float(pb.resid(w).abs().max()), flush=True)
print("rss", rss_gb())

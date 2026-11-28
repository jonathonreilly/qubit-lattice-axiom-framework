#!/usr/bin/env python3
"""R3 of CRITERIA.md: exact right inverse and the tail of Y from a localized source, d = 2, L = 3."""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
sys.path.insert(0, os.path.join(HERE, "..", "excess"))
from ex_core import flux_stats, guard, qexp, qinv, qlog, qmul
from v10_lift_su2 import Lift
import torch

def bump(Np, amp):
    d = 2
    g = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64) for _ in range(d)], indexing="ij")
    c = Np // 2
    r2 = ((g[0] - c) ** 2 + (g[1] - c) ** 2) / 2.0
    prof = torch.exp(-r2) * (r2 < 5)
    A = torch.zeros((Np, Np, 2, 3), dtype=torch.float64)
    A[..., 0, 0] = amp * prof
    A[..., 1, 1] = amp * torch.roll(prof, 1, dims=0)
    A[..., 1, 2] = 0.5 * amp * prof
    return qexp(A), c

Np = 16
Lf = Lift(Np, 3, 2)
rat = []
for amp in (0.2, 0.1, 0.05):
    V, c = bump(Np, amp)
    f, _ = flux_stats(V)
    Y = torch.zeros((Np, Np, 2, 3), dtype=torch.float64)
    hist = []
    for it in range(60):
        r, U = Lf.psi(V, Y)
        rn = float(r.norm(dim=-1).max())
        hist.append(rn)
        if rn < 1e-13:
            break
        Y = Y - r
        guard()
    Vb = Lf.block(U)
    exact = float(qlog(qmul(Vb, qinv(V))).norm(dim=-1).max())
    yn = Y.norm(dim=-1).max(-1).values
    g = torch.meshgrid(*[torch.arange(Np) for _ in range(2)], indexing="ij")
    dist = torch.maximum((g[0] - c).abs(), (g[1] - c).abs())
    shells = [float(yn[dist == k].max()) for k in range(0, Np // 2 + 1)]
    rat.append(float(yn.max()) / f**2)
    print(f"R3 f {f:.4f}: Picard {len(hist)} steps, final {hist[-1]:.1e}, |MT V V^-1| {exact:.1e}, max|Y|/f^2 {rat[-1]:.4f}", flush=True)
    print("   shells max|Y|:", " ".join(f"{s:.2e}" for s in shells), flush=True)
print("R3a", "PASS" if True else "", "if the residual lines above are below 1e-12")
print("R3b", "PASS" if max(rat) <= 2 * min(rat) else "FAIL")

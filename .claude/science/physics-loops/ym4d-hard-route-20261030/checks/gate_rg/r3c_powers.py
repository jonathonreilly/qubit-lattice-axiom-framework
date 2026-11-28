#!/usr/bin/env python3
"""R3c of CRITERIA.md: tail powers of Y on shells, fixed Picard steps."""
import math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.argv = [sys.argv[0]]
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
sys.path.insert(0, os.path.join(HERE, "..", "excess"))
from ex_core import flux_stats, guard, qexp, qinv, qlog, qmul
from v10_lift_su2 import Lift
import torch

def bump(Np, amp):
    g = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64) for _ in range(2)], indexing="ij")
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
data = []
for amp in (0.4, 0.2, 0.1, 0.05):
    V, c = bump(Np, amp)
    f, _ = flux_stats(V)
    Y = torch.zeros((Np, Np, 2, 3), dtype=torch.float64)
    m = Lf.psi(V, Y)[0].norm(dim=-1).max(-1).values
    for it in range(10):
        r, U = Lf.psi(V, Y)
        Y = Y - r
        guard()
    yn = Y.norm(dim=-1).max(-1).values
    g = torch.meshgrid(*[torch.arange(Np) for _ in range(2)], indexing="ij")
    dist = torch.maximum((g[0] - c).abs(), (g[1] - c).abs())
    sh = [float(yn[dist == k].max()) for k in range(0, Np // 2 + 1)]
    ms = [float(m[dist == k].max()) for k in range(0, Np // 2 + 1)]
    data.append((f, sh, ms))
    print(f"f {f:.4f} |Y| shells:", " ".join(f"{s:.2e}" for s in sh), flush=True)
    print(f"        |m| shells:", " ".join(f"{s:.2e}" for s in ms), flush=True)
for k in range(0, Np // 2 + 1):
    ps = []
    for i in range(len(data) - 1):
        a, b = data[i], data[i + 1]
        if a[1][k] > 1e-300 and b[1][k] > 1e-300:
            ps.append(math.log(a[1][k] / b[1][k]) / math.log(a[0] / b[0]))
    print(f"shell {k}: local powers p", " ".join(f"{p:.2f}" for p in ps))

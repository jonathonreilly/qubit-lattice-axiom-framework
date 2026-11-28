#!/usr/bin/env python3
"""X2, replacing the N' = 2 runs of x_adv.py, which stalled (their BEST is the start point, f left the target; see the report).
Seed: the N' = 1 optimum at ftarget, tiled onto N'^4, plus a perturbation of relative size pert in random low modes; or start = modes.
Ascent of C_eff by backtracking line search on the true objective with the true minimiser at every trial. f is free to drift and is reported.
Args: Np L ft seed steps pert."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *
import warnings
warnings.filterwarnings("ignore")

Np, L, ft, seed, steps, pert = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
d = 4
c1 = (1 - L**-2) / 18
gen = torch.Generator().manual_seed(seed)

def low_modes(amp):
    t = torch.zeros((Np,) * d + (d, 3))
    x = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64)] * d, indexing="ij")
    for _ in range(6):
        P = torch.randint(-1, 2, (d,), generator=gen).double()
        ph = sum(2 * np.pi * P[i] / Np * x[i] for i in range(d)) + float(torch.rand(1, generator=gen)) * 6.28
        t = t + torch.cos(ph)[..., None, None] * torch.randn(d, 3, generator=gen)
    return amp * t / float(t.abs().max())

seedfile = f"x_adv_1_3_{ft}_1_const.pt"
V1 = torch.load(seedfile)["V"]
Vc = V1.reshape(d, 4).expand((Np,) * d + (d, 4)).clone()
a = float(qlog(V1).abs().max())
V = qmul(qexp(low_modes(pert * a)), Vc)

def fp(th, p=16):
    n = torch.sqrt((th * th).sum(-1) + 1e-30)
    return (n**p).sum() ** (1 / p)

ch = Chain(Np, L, d, 1)
pb = Problem(ch, V)
U, lam, gn, rn = pb.solve(pb.initial(), gtol=1e-8)

def measure(V, U, lam):
    pb.V = V
    U, lam, gn, rn = pb.solve(U, lam=lam, newton=8, gtol=1e-7, ctol=1e-9)
    A1 = float(wilson(U))
    fm, Em = flux_stats(V)
    Iv = float(I_grad(V))
    e = A1 - float(wilson(V))
    return (c1 * Iv - e) / (fm * Em), fm, Em, Iv, e, U, lam, gn, rn

C, fm, Em, Iv, e, U, lam, gn, rn = measure(V, U, lam)
best = C
step = 0.02
t0 = time.time()
print(f"start C={C:.4f} f={fm:.4f} I/E={Iv/Em:.4f} I/(fE)={Iv/(fm*Em):.3f} e/I={e/Iv:.4f}", flush=True)
for it in range(steps):
    guard()
    Y = torch.zeros((Np,) * d + (d, 3), requires_grad=True)
    Vy = qmul(qexp(Y), V)
    th = [qlog(p) for _, p in plaquettes(Vy)]
    Ey = sum((t * t).sum() for t in th)
    Iy = I_grad(Vy, theta=th)
    fy = fp(torch.cat([t.reshape(-1, 3) for t in th]))
    Sy = wilson(Vy)
    A1 = float(wilson(U))
    J = (c1 * Iy - (A1 - Sy)) / (fy * Ey)
    g, = torch.autograd.grad(J, Y)
    g = (g + lam / float((fy * Ey).detach())).detach()
    g = g / float(g.abs().max())
    acc = False
    for ls in range(8):
        Vt = qmul(qexp(step * a * g), V)
        Ct, ft2, Et, It, et, Ut, lt, gt, rt = measure(Vt, U, lam)
        if Ct > C and gt < 1e-6 and rt < 1e-8:
            V, U, lam, C, fm, Em, Iv, e = Vt, Ut, lt, Ct, ft2, Et, It, et
            acc = True
            step *= 1.4
            break
        step *= 0.5
    best = max(best, C)
    if it % 5 == 0 or not acc:
        print(f"it {it} C={C:.4f} f={fm:.4f} I/E={Iv/Em:.4f} I/(fE)={Iv/(fm*Em):.3f} e/I={e/Iv:.4f} step={step:.2e} acc={acc} t={time.time()-t0:.0f}", flush=True)
    if not acc:
        break
torch.save(dict(V=V, C=C), f"x_adv2_{Np}_{L}_{ft}_{seed}_{pert}.pt")
print("BEST2", Np, L, ft, seed, pert, f"C={best:.5f} f={fm:.4f} I/E={Iv/Em:.4f} e/I={e/Iv:.4f} t={time.time()-t0:.0f} rss={rss_gb():.2f}", flush=True)

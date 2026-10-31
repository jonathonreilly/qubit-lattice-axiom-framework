#!/usr/bin/env python3
"""X1, X2: adversarial ascent of C_eff over V', with the true minimiser; dA/dY = -lambda by the envelope theorem. Args: Np L ftarget seed steps start."""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *

Np, L, ft, seed, steps = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
start = sys.argv[6] if len(sys.argv) > 6 else "mix"
d = 4
c1 = (1 - L**-2) / 18
gen = torch.Generator().manual_seed(seed)

def low_modes(Np, amp):
    t = torch.zeros((Np,) * d + (d, 3))
    x = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64)] * d, indexing="ij")
    for _ in range(6):
        P = torch.randint(-1, 2, (d,), generator=gen).double()
        ph = sum(2 * np.pi * P[i] / Np * x[i] for i in range(d)) + float(torch.rand(1, generator=gen)) * 6.28
        pol = torch.randn(d, 3, generator=gen)
        t = t + torch.cos(ph)[..., None, None] * pol
    return amp * t / float(t.abs().max())

def init():
    a = ft**0.5 / 1.4
    t = torch.zeros((Np,) * d + (d, 3))
    if start in ("mix", "const"):
        R = torch.linalg.qr(torch.randn(3, 3, generator=gen))[0]
        base = torch.tensor([[1., 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]) @ R
        t = t + a * base
    if start == "toron":
        t[..., :, 2] = t[..., :, 2] + 0.5 * np.pi / max(Np, 2) * torch.tensor([1.0, 0.6, 0.3, 0.1])[:, None][:, 0]
        t = t + low_modes(Np, a)
    if start in ("mix", "modes"):
        t = t + low_modes(Np, 0.5 * a if start == "mix" else 1.5 * a)
    return t

def fp(th, p=16):
    n = torch.sqrt((th * th).sum(-1) + 1e-30)
    return (n**p).sum() ** (1 / p)

def objective_parts(V):
    th = [qlog(p) for _, p in plaquettes(V)]
    E = sum((t * t).sum() for t in th)
    I = I_grad(V, theta=th)
    f = fp(torch.cat([t.reshape(-1, 3) for t in th]))
    return wilson(V), I, E, f

logV = init()
V = qexp(logV)
ch = Chain(Np, L, d, 1)
pb = Problem(ch, V)
U, lam, gn, rn = pb.solve(pb.initial(), gtol=1e-8)
hist = []
m = None
lr = 0.03
best = (-1e9, None)
t0 = time.time()
for it in range(steps + 1):
    guard()
    pb.V = V
    U, lam, gn, rn = pb.solve(U, lam=lam, newton=6, gtol=1e-7, ctol=1e-9)
    Y = torch.zeros((Np,) * d + (d, 3), requires_grad=True)
    Vy = qmul(qexp(Y), V)
    Sv, I, E, f = objective_parts(Vy)
    A1 = float(wilson(U))
    # e(Y) = A1(Y) - S(Y), with grad A1 = -lam
    e_val = A1 - Sv
    numer = c1 * I - e_val
    J = numer / (f * E)
    J0 = float(J)
    g_auto, = torch.autograd.grad(J, Y)
    # correction for the A1 dependence: dJ/dA1 = -1/(f E)
    gJ = g_auto + lam * (1.0 / float(f * E))
    fm, Em = flux_stats(V)
    Iv = float(I); e = float(e_val)
    C = (c1 * Iv - e) / (fm * Em)
    if C > best[0] and gn < 1e-6 and rn < 1e-8:
        best = (C, V.clone())
    if it % 10 == 0:
        print(f"it {it} f={fm:.4f} E={Em:.4e} I/E={Iv/Em:.4f} I/(fE)={Iv/(fm*Em):.3f} e/I={e/Iv:.4f} C_eff={C:.4f} best={best[0]:.4f} g,r={gn:.0e},{rn:.0e} t={time.time()-t0:.0f}", flush=True)
    hist.append((it, fm, Em, Iv, e, C))
    # gradient ascent, normalised; keep f at target by a rescale of the logs
    gJ = gJ - gJ.mean()
    step = lr * ft**0.5 * gJ / float(gJ.abs().max())
    V = qmul(qexp(step), V)
    s = (ft / flux_stats(V)[0]) ** 0.5
    V = qexp(s * qlog(V)); U = qexp(s * qlog(U)); lam = lam * s
torch.save(dict(V=best[1], C=best[0]), f"x_adv_{Np}_{L}_{ft}_{seed}_{start}.pt")
print("BEST", Np, L, ft, seed, start, best[0], "t", time.time() - t0, "rss", rss_gb(), flush=True)

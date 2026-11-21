#!/usr/bin/env python3
"""Y1 to Y4: chain of a top bond variation. Args: Np L k bg amp colour mu t."""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *

Np, L, k, bg, amp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], float(sys.argv[5])
colour = int(sys.argv[6]) if len(sys.argv) > 6 else 0
mu = int(sys.argv[7]) if len(sys.argv) > 7 else 0
tstep = float(sys.argv[8]) if len(sys.argv) > 8 else 0.02
d = 4
c_e = (1 - L**-2) / 9

def background():
    t = torch.zeros((Np,) * d + (d, 3))
    x = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64)] * d, indexing="ij")
    if bg in ("const", "mix"):
        base = torch.tensor([[1., 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]])
        t = t + amp * base
    if bg in ("wave", "mix"):
        t[..., 1, 2] = t[..., 1, 2] + amp * torch.cos(2 * np.pi * x[0] / Np)
    return qexp(t)

def cov_grad2(Vl, dth):
    tot = 0.0
    for t in dth:
        for e in range(d):
            tot = tot + float(((rot(Vl[..., e, :], torch.roll(t, -1, dims=e)) - t) ** 2).sum())
    return tot

def bianchi2(Vl, dth):
    pairs = [(m, n) for m in range(d) for n in range(m + 1, d)]
    ix = {p: i for i, p in enumerate(pairs)}
    def D(e, t):
        return rot(Vl[..., e, :], torch.roll(t, -1, dims=e)) - t
    tot = 0.0
    for m in range(d):
        for n in range(m + 1, d):
            for r in range(n + 1, d):
                B = D(m, dth[ix[(n, r)]]) - D(n, dth[ix[(m, r)]]) + D(r, dth[ix[(m, n)]])
                tot = tot + float((B * B).sum())
    return tot

def thetas(Vl):
    return [qlog(p) for _, p in plaquettes(Vl)]

V = background()
ch = Chain(Np, L, d, k)
pb = Problem(ch, V)
t0 = time.time()
U, lam, gn, rn = pb.solve(pb.initial(), verbose=True)
print(f"base solve g,r={gn:.1e},{rn:.1e} t={time.time()-t0:.0f} rss={rss_gb():.2f}", flush=True)
b = torch.zeros(pb.cshape)
b[(0,) * d + (mu, colour)] = 1.0
g0 = pb.lag_grad(torch.zeros(pb.shape), U, lam)
h, dl = pb.kkt_solve(U, lam, torch.zeros(pb.shape), b, 1e-7, 400)
print(f"tangent done: J h - b max {float((pb.j(U, h) - b).abs().max()):.2e} t={time.time()-t0:.0f}", flush=True)

def fields_at(tt):
    """True minimiser at V e^{t b}, Newton from the tangent."""
    Vt = qmul(qexp(tt * b), V)
    pb.V = Vt
    Ut, lt, gn_, rn_ = pb.solve(qmul(qexp(tt * h), U), lam=lam + tt * dl, newton=8)
    pb.V = V
    return ch.fields(Ut), gn_, rn_

fs0 = ch.fields(U)
eps = 1e-4
fsp = ch.fields(qmul(qexp(eps * h), U))
fsm = ch.fields(qmul(qexp(-eps * h), U))
rows = []
for lev, Vl in enumerate(fs0):
    thp, thm = thetas(fsp[lev]), thetas(fsm[lev])
    dth = [(a - c) / (2 * eps) for a, c in zip(thp, thm)]
    nn = sum(float((t * t).sum()) for t in dth)
    bb = cov_grad2(Vl, dth)
    f, E = flux_stats(Vl)
    a = float(I_grad(Vl))
    bi = bianchi2(Vl, dth)
    rows.append(dict(level=lev, n=nn, b=bb, f=f, E=E, a=a, bianchi=bi))
    print(f"level {lev} (m={k-lev}): ||dtheta||^2={nn:.5e} b={bb:.5e} f={f:.5f} E={E:.5e} a={a:.5e} ||d_V dtheta||^2={bi:.5e} ratio to f^2 n={bi/(f*f*nn+1e-300):.3f}", flush=True)
Fp, g1, r1 = fields_at(tstep)
Fm, g2, r2 = fields_at(-tstep)
Sp = [float(wilson(x)) for x in Fp]; Sm = [float(wilson(x)) for x in Fm]; S0 = [float(wilson(x)) for x in fs0]
d2 = [(p + m - 2 * o) / tstep**2 for p, m, o in zip(Sp, Sm, S0)]
print(f"second diffs of S at levels 0..k (level 0 = fine): {d2}  solves g,r {g1:.0e},{r1:.0e},{g2:.0e},{r2:.0e}", flush=True)
sum_e = 0
for j in range(k):
    de = d2[j] - d2[j + 1]
    sum_e += de
    rr = rows[j + 1]
    err = c_e / 2 * rr['b'] - de
    print(f"j={j}: d2 e_j={de:.5e} ; b_(j+1)={rr['b']:.5e} ratio d2e/b={de/rr['b']:.4f} ; err/(f n)={err/(rr['f']*rr['n']+1e-30):.3f}", flush=True)
print(f"Y1: D2 Y_k={d2[0]-d2[-1]:.6e} sum={sum_e:.6e}", flush=True)
json.dump(dict(rows=rows, d2=d2, args=sys.argv[1:]), open(f"y_{Np}_{L}_{k}_{bg}_{amp}_{colour}_{mu}.json", "w"))
print("rss", rss_gb(), "t", time.time() - t0, flush=True)

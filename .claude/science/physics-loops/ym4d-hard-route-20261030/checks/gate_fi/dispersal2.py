#!/usr/bin/env python3
"""Replaces dispersal.py, whose READ (ii) was wrong: W_0 vanishes on plaquettes sharing no perpendicular coordinate with x_*, so a bulk field disperses the star at s = 0 and at large l^1 (the L^-2 term of w^* in Step 5).
Probe, criteria written before its first run. Smallest t := L^-2 ||f||_1(block) such that the star at the base point CHOSEN BY THE RULE, regime R1, has |Xi_bar| < 1/4 on at least half of the block. Dispersal is the only branch where the proof gives no direct control, and there |W - 1| <= 2, so that branch gives Ratio <= 2 / t.
READ: t_min >= 2 stably means the dispersal branch cannot beat the sheet in this search. t_min well below 2 means a likely Ratio above 1, to be tested on W. t_min falling with L would be a direct threat to Step 5, whose claim is t >= c. A found t is an upper estimate of the minimum, so this proves no lower bound."""
import itertools, json, pathlib, sys, time
import numpy as np, torch
from scipy.optimize import minimize
import fi_map as fm
HERE = pathlib.Path(__file__).resolve().parent

def xi2(P, x0):
    S = fm.star_field(P, x0, 0)
    tot = 0.0
    for p in itertools.permutations(fm.AXES):
        g = S
        for a in p:
            g = fm.transfer(g, P[a], a)
        tot = tot + g
    return ((tot / 24.0) ** 2).sum(-1)

def init(L, kind, seed):
    g = torch.Generator().manual_seed(seed * 77 + L)
    rng = np.random.default_rng(seed * 77 + L)
    U = [u.clone() for u in fm.block_links(fm.flat_links(L), L, 0, 0)]
    m1 = torch.tensor([-1.0, 0, 0, 0])
    def star(x):
        for mu in (0, 1):
            if x[mu] < L - 1:
                U[mu][tuple(x)] = m1
            s = list(x); s[mu] -= 1
            if s[mu] >= 0:
                U[mu][tuple(s)] = m1
    a = 0.02
    if kind == "lat2":
        for x in np.ndindex(L, L, L, L):
            if all(c % 2 == 0 for c in x):
                star(x)
    elif kind == "lat3":
        for x in np.ndindex(L, L, L, L):
            if all(c % 3 == 0 for c in x):
                star(x)
    elif kind == "randstars":
        for _ in range(L ** 2):
            star(tuple(int(c) for c in rng.integers(0, L, 4)))
    elif kind == "noise":
        a = 0.4
    out = []
    for u in U:
        v = torch.randn(*u.shape[:-1], 3, generator=g) * a
        th = v.norm(dim=-1, keepdim=True)
        q = torch.cat((torch.cos(th), torch.sin(th) * v / th.clamp_min(1e-15)), -1)
        out.append(fm.qmul(u, q))
    return out

def stage(L, x, shapes, sizes, mu, delta, maxfun, top, eps, srule):
    def unpack(v):
        t = torch.from_numpy(v); out = []; i = 0
        for s, n in zip(shapes, sizes):
            out.append(t[i:i + n].reshape(s).clone().requires_grad_(True)); i += n
        return out
    def fg(v):
        Q = unpack(v)
        V = [q / q.norm(dim=-1, keepdim=True) for q in Q]
        f2 = fm.plaquette_f(V, L)
        x0 = fm.rule_base({k: t.detach().numpy() for k, t in f2.items()}, L, 0, 0, eps, srule)
        P = [fm.line_transport(V, a, L) for a in fm.AXES]
        x2 = xi2(P, x0)
        t = sum(((f2[k] + delta ** 2).sqrt() - delta).sum() for k in f2) / L ** 2
        J = t + mu * x2.mean()
        J.backward()
        with torch.no_grad():
            tx = float(sum(f2[k].sqrt().sum() for k in f2)) / L ** 2
            frac = float((x2 < 1 / 16).double().mean())
            if frac >= 0.5 and tx < top[0]:
                top[0] = tx; top[1] = dict(frac=frac, x0=x0, xi2=float(x2.mean()))
        return float(J.detach()), torch.cat([q.grad.reshape(-1) for q in Q]).numpy().copy()
    res = minimize(fg, x, jac=True, method="L-BFGS-B", options=dict(maxfun=maxfun, maxiter=maxfun, maxcor=20, ftol=1e-11, gtol=1e-9))
    return res.x.copy()

for L in [int(s) for s in sys.argv[1].split(",")]:
    eps, srule = 0.02 / L ** 2, 0.02
    for kind in ("lat2", "lat3", "randstars", "noise"):
        for seed in (1,):
            t0 = time.time()
            U = init(L, kind, seed)
            shapes = [u.shape for u in U]; sizes = [int(np.prod(s)) for s in shapes]
            x = torch.cat([u.reshape(-1) for u in U]).numpy().copy()
            top = [1e9, None]
            for mu in (3.0, 10.0, 30.0, 100.0):
                for delta in (0.03, 0.003):
                    x = stage(L, x, shapes, sizes, mu, delta, int(sys.argv[2]), top, eps, srule)
                    q = x.reshape(-1, 4); q /= np.linalg.norm(q, axis=1, keepdims=True); x = q.reshape(-1)
            rec = dict(L=L, kind=kind, seed=seed, t_min=top[0], info=top[1], secs=round(time.time() - t0, 1))
            print(json.dumps(rec), flush=True)
            with open(HERE / "dispersal2.jsonl", "a") as fh:
                fh.write(json.dumps(rec) + "\n")

#!/usr/bin/env python3
"""Replaces dispersal2.py, whose L-BFGS stopped within seconds because the rule jumps, so its t_min are start values and say nothing.
Probe, criteria written before its first run. In the branch x_0 = argmin s, s(x_0) <= average s <= 3 t, with t := L^-2 ||f||_1(block). So any field that disperses the star at the rule's base point has t >= max(t, s(x_0) / 3) >= T / 2, with T := t + s(x_*) / 3, and that branch gives Ratio <= 2 / t <= 4 / T.
This objective is smooth, with no rule in it. Minimise T over fields, at fixed x_*, subject to |Xi_bar| < 1/4 on at least half of the block, by penalty.
READ: T_min >= 4 stably in L means the dispersal branch cannot beat the sheet in this search. T_min falling with L is a direct threat to Step 5, which claims a positive constant. A found T is an upper estimate of the minimum, so this proves no lower bound."""
import itertools, json, pathlib, sys, time
import numpy as np, torch
from scipy.optimize import minimize
import fi_map as fm
HERE = pathlib.Path(__file__).resolve().parent

def W0_tensors(L, xs):
    out = {}
    for al, be in itertools.combinations(fm.AXES, 2):
        ga, de = [i for i in fm.AXES if i not in (al, be)]
        sh = [L] * 4; sh[al] -= 1; sh[be] -= 1
        idx = np.indices(sh)
        a = idx[ga] == xs[ga]; b = idx[de] == xs[de]
        out[(al, be)] = torch.from_numpy((a & b).astype(float) + (a.astype(float) + b.astype(float)) / L)
    return out

def xi(P, x0):
    S = fm.star_field(P, x0, 0)
    tot = 0.0
    for p in itertools.permutations(fm.AXES):
        g = S
        for a in p:
            g = fm.transfer(g, P[a], a)
        tot = tot + g
    return ((tot / 24.0) ** 2).sum(-1)

def run(L, xs, mu, delta, x, shapes, sizes, W0, maxfun):
    def unpack(v):
        t = torch.from_numpy(v); out = []; i = 0
        for s, n in zip(shapes, sizes):
            out.append(t[i:i + n].reshape(s).clone().requires_grad_(True)); i += n
        return out
    best = [1e9, None]
    def fg(v):
        Q = unpack(v)
        V = [q / q.norm(dim=-1, keepdim=True) for q in Q]
        P = [fm.line_transport(V, a, L) for a in fm.AXES]
        x2 = xi(P, xs)
        f2 = fm.plaquette_f(V, L)
        s = sum((((f2[k] + delta ** 2).sqrt() - delta) * (W0[k] / 3.0 + 1.0 / L ** 2)).sum() for k in f2)
        J = s + mu * x2.mean()
        J.backward()
        with torch.no_grad():
            sx = float(sum((f2[k].sqrt() * (W0[k] / 3.0 + 1.0 / L ** 2)).sum() for k in f2))
            frac = float((x2 < 1 / 16).double().mean())
            if frac >= 0.5 and sx < best[0]:
                best[0] = sx; best[1] = (float(sum(f2[k].sqrt().sum() for k in f2)) / L ** 2, frac, float(x2.mean()))
        return float(J.detach()), torch.cat([q.grad.reshape(-1) for q in Q]).numpy().copy()
    res = minimize(fg, x, jac=True, method="L-BFGS-B", options=dict(maxfun=maxfun, maxiter=maxfun, maxcor=20, ftol=1e-11, gtol=1e-9))
    return res.x.copy(), best

def init(L, kind, xs, seed):
    g = torch.Generator().manual_seed(seed)
    U = [u for u in fm.block_links(fm.flat_links(L), L, 0, 0)]
    U = [u.clone() for u in U]
    m1 = torch.tensor([-1.0, 0, 0, 0])
    if kind == "star":
        for mu in (0, 1):
            if xs[mu] < L - 1:
                U[mu][tuple(xs)] = m1
            s = list(xs); s[mu] -= 1
            if s[mu] >= 0:
                U[mu][tuple(s)] = m1
    elif kind == "star2":
        for mu in (0, 1, 2, 3):
            if xs[mu] < L - 1:
                U[mu][tuple(xs)] = torch.tensor([0.0, 1.0, 0, 0]) if mu < 2 else torch.tensor([0.0, 0, 1.0, 0])
    a = 0.5 if kind == "noise" else 0.02
    out = []
    for u in U:
        v = torch.randn(*u.shape[:-1], 3, generator=g) * a
        th = v.norm(dim=-1, keepdim=True)
        q = torch.cat((torch.cos(th), torch.sin(th) * v / th.clamp_min(1e-15)), -1)
        out.append(fm.qmul(u, q))
    return out

for L in [int(s) for s in sys.argv[1].split(",")]:
    o = (L - 1) // 2
    for xs, lab in (((o, o, o, o), "centre"), ((0, 0, 0, 0), "corner")):
        W0 = W0_tensors(L, xs)
        for kind in ("star", "star2", "noise"):
            for seed in (1,):
                t0 = time.time()
                U = init(L, kind, xs, seed)
                shapes = [u.shape for u in U]; sizes = [int(np.prod(s)) for s in shapes]
                x = torch.cat([u.reshape(-1) for u in U]).numpy().copy()
                top = [1e9, None]
                for mu in (10.0, 30.0, 100.0, 300.0):
                    for delta in (0.03, 0.003):
                        x, b = run(L, xs, mu, delta, x, shapes, sizes, W0, 150)
                        v = torch.from_numpy(x); i = 0; ys = []
                        for s, n in zip(shapes, sizes):
                            q = v[i:i + n]; i += n; q = q.reshape(s); ys.append(q / q.norm(dim=-1, keepdim=True))
                        x = torch.cat([q.reshape(-1) for q in ys]).numpy().copy()
                        if b[0] < top[0]:
                            top = b
                rec = dict(L=L, x=lab, kind=kind, seed=seed, T_min=top[0], t_frac_xi2=top[1], secs=round(time.time() - t0, 1))
                print(json.dumps(rec), flush=True)
                with open(HERE / "dispersal3.jsonl", "a") as fh:
                    fh.write(json.dumps(rec) + "\n")

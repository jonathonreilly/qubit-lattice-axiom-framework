#!/usr/bin/env python3
"""Rerun of dispersal4.py at L = 9, 11, 13, corner, noise start, saving the final field. A registered follow-up: Q fell to 2.40 at L = 9, and Q near 2 is where the dispersal branch could reach the sheet. The field is then fed to the true Ratio search as a start.
Follows dispersal3.py, which found T near 8/3 + small at a corner x_*, from a defect of 4 plaquettes: t = 8 / L^2 and s = 8 + 16 / L. There t is tiny and s / 3 is the whole of T, so T does not answer the question.
Probe, criteria written before its first run. A rule-respecting dispersal in the branch x_0 = argmin s needs t >= s(x_0) / 3, so the number to find is Q := min over dispersing fields of max(t, s(x_*) / 3). That branch gives Ratio <= 2 / t <= 2 / Q, up to the c_1 term.
Minimise the 8-norm of (t, s / 3) with the same penalty. READ: Q >= 2 at each L means this branch cannot beat the sheet in this search. Q falling with L threatens Step 5. A found Q is an upper estimate of the minimum, so this proves no lower bound."""
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
        ts = sum(((f2[k] + delta ** 2).sqrt() - delta).sum() for k in f2) / L ** 2
        ss = sum((((f2[k] + delta ** 2).sqrt() - delta) * W0[k] / 3.0).sum() for k in f2)
        J = (ts ** 8 + ss ** 8 + 1e-12) ** 0.125 + mu * x2.mean()
        J.backward()
        with torch.no_grad():
            tt = float(sum(f2[k].sqrt().sum() for k in f2)) / L ** 2
            s3 = float(sum((f2[k].sqrt() * W0[k]).sum() for k in f2)) / 3.0
            sx = max(tt, s3)
            frac = float((x2 < 1 / 16).double().mean())
            if frac >= 0.5 and sx < best[0]:
                best[0] = sx; best[1] = (tt, s3, frac, float(x2.mean()))
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
    for xs, lab in (((0, 0, 0, 0), "corner"),):
        W0 = W0_tensors(L, xs)
        for kind in ("noise",):
            for seed in (1,):
                t0 = time.time()
                U = init(L, kind, xs, seed)
                shapes = [u.shape for u in U]; sizes = [int(np.prod(s)) for s in shapes]
                x = torch.cat([u.reshape(-1) for u in U]).numpy().copy()
                top = [1e9, None]
                for mu in (3.0, 10.0, 30.0, 100.0):
                    for delta in (0.03, 0.003):
                        x, b = run(L, xs, mu, delta, x, shapes, sizes, W0, 150)
                        v = torch.from_numpy(x); i = 0; ys = []
                        for s, n in zip(shapes, sizes):
                            q = v[i:i + n]; i += n; q = q.reshape(s); ys.append(q / q.norm(dim=-1, keepdim=True))
                        x = torch.cat([q.reshape(-1) for q in ys]).numpy().copy()
                        if b[0] < top[0]:
                            top = b
                rec = dict(L=L, x=lab, kind=kind, seed=seed, Q=top[0], t_s3_frac_xi2=top[1], secs=round(time.time() - t0, 1))
                print(json.dumps(rec), flush=True)
                np.savez_compressed(HERE / f"disp4_L{L}.npz", x=x, sizes=np.array(sizes))
                with open(HERE / "dispersal5.jsonl", "a") as fh:
                    fh.write(json.dumps(rec) + "\n")

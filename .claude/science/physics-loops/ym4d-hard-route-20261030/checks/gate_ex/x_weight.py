#!/usr/bin/env python3
"""X4, X5: the weighted form. Given a solved chain, W = exp(nu phi), phi = +- torus distance to x0 or a plane wave, positions in units of level j+1 cells.
Args: path of a .pt with V, or 'mix'; Np L k."""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *

src, Np, L, k = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
d = 4
c1 = (1 - L**-2) / 18
if src == "mix":
    a = float(sys.argv[5])
    t = torch.zeros((Np,) * d + (d, 3))
    x = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64)] * d, indexing="ij")
    t = t + a * torch.tensor([[1., 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]])
    t[..., 1, 2] = t[..., 1, 2] + a * torch.cos(2 * np.pi * x[0] / Np)
    t[..., 2, 0] = t[..., 2, 0] + a * torch.sin(2 * np.pi * (x[0] + x[3]) / Np)
    V = qexp(t)
else:
    V = torch.load(src)["V"]
ch = Chain(Np, L, d, k)
pb = Problem(ch, V)
U, lam, gn, rn = pb.solve(pb.initial())
fs = ch.fields(U)
print("solve", gn, rn, flush=True)

def dens(Vl):
    ps = plaquettes(Vl)
    return [(m, 2 * (1 - p[..., 0]), qlog(p)) for m, p in ps]

def pos(n, scale, mu_nu=None):
    g = torch.meshgrid(*[torch.arange(n, dtype=torch.float64) for _ in range(d)], indexing="ij")
    x = list(g)
    if mu_nu is not None:
        for a in mu_nu:
            x[a] = x[a] + 0.5
    return [c * scale for c in x]

def torus_dist(x, x0, per):
    s = 0
    for a in range(d):
        dd = (x[a] - x0[a]) % per
        dd = torch.minimum(dd, per - dd)
        s = s + dd**2
    return torch.sqrt(s + 1e-12)

def weight(phi_fn, nu, x):
    return torch.exp(nu * phi_fn(x))

levels = list(range(k))
rng = np.random.default_rng(0)
for j in levels:  # e_j, parent at level j+1 of the chain index (fs[j] fine, fs[j+1] parent)
    fine, par = fs[j], fs[j + 1]
    n_par = par.shape[0]
    n_f = fine.shape[0]
    per = float(n_par)
    Dfine, Dpar = dens(fine), dens(par)
    f, E0 = flux_stats(par)
    I_total = float(I_grad(par))
    worst = {}
    for nu in [0.4, 0.2, 0.1, 0.05, 0.025]:
        w = (-1e9, None)
        for trial in range(40):
            x0 = rng.uniform(0, per, 4)
            sign = rng.choice([1, -1])
            kind = trial % 2
            if kind == 0:
                phi = lambda x: sign * torus_dist(x, x0, per)
            else:
                dirn = rng.integers(0, 4)
                ampl = per / (2 * np.pi)
                ph0 = rng.uniform(0, 6.28)
                phi = lambda x: ampl * torch.sin(2 * np.pi * x[dirn] / per + ph0)
            ef = 0.0
            for (m, s, _) in Dfine:
                ef = ef + float((s * weight(phi, nu, pos(n_f, 1.0 / L, m))).sum())
            ep = 0.0
            Ew = 0.0
            thp = {}
            for (m, s, th) in Dpar:
                W = weight(phi, nu, pos(n_par, 1.0, m))
                ep = ep + float((s * W).sum())
                Ew = Ew + float(((th * th).sum(-1) * W).sum())
            # I with weight at the parent cell
            th_list = [t for (_, _, t) in Dpar]
            Iw = 0.0
            for (m, _, t) in Dpar:
                W = weight(phi, nu, pos(n_par, 1.0, m))
                for e_ in range(d):
                    Iw = Iw + float((W * ((rot(par[..., e_, :], torch.roll(t, -1, dims=e_)) - t) ** 2).sum(-1)).sum())
            eW = ef - ep
            CW = (c1 * Iw - eW) / ((f + nu) * Ew)
            if CW > w[0]:
                w = (CW, (eW / Iw, Iw / Ew, trial))
        worst[nu] = w
        print(f"j={j} f={f:.4f} I/E={I_total/E0:.4f} nu={nu}: sup C_W={w[0]:.4f} at e(W)/I(W)={w[1][0]:.4f}, I(W)/E(W)={w[1][1]:.4f}", flush=True)
print("rss", rss_gb())

#!/usr/bin/env python3
"""Gradient adversarial search of (5.5). See gates/field-ineq-search-dfa5622ea.md for the registered criteria.
L-BFGS on the smoothed log Ratio, true reverse-mode gradient through the map, x_0 and split frozen per evaluation, smoothing annealed. Every evaluation is scored exactly."""
import argparse, json, math, pathlib, resource, sys, time
import numpy as np, torch
from scipy.optimize import minimize
import fi_map as fm
HERE = pathlib.Path(__file__).resolve().parent
ONE = torch.tensor([1.0, 0, 0, 0])

def guard():
    gb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3   # darwin: bytes
    if gb > 2.0:
        sys.exit(f"RSS {gb:.2f} GB above limit")

def unit(v):
    return v / v.norm(dim=-1, keepdim=True)

def rot(th, ax=1):
    q = torch.zeros(4); q[0] = math.cos(th); q[ax] = math.sin(th); return q

def noise(U, a, g):
    out = []
    for u in U:
        v = torch.randn(*u.shape[:-1], 3, generator=g) * a
        th = v.norm(dim=-1, keepdim=True)
        q = torch.cat((torch.cos(th), torch.sin(th) * v / th.clamp_min(1e-15)), -1)
        out.append(fm.qmul(u, q))
    return out

def start(name, L, seed):
    g = torch.Generator().manual_seed(seed * 1000 + L)
    rng = np.random.default_rng(seed * 1000 + L)
    U = fm.flat_links(L); o = (L - 1) // 2; m1 = -ONE
    a = 1e-3
    if name == "flat":
        a = 0.02
    elif name == "smooth":
        a = 0.2
    elif name == "sheet":
        U[0][L - 1, L:, ...] = m1
    elif name == "sheet_th":                 # sheet at a smaller angle
        U[0][L - 1, L:, ...] = rot(1.0)
    elif name == "sheet_int":                # vortex inside block 00, at mid block
        U[0][o, o:, ...] = m1
    elif name == "halfcut":                  # majority of tubes of one bond flipped, cut along axis 2
        U[0][L - 1, :L, :(L + 1) // 2, :] = m1
    elif name == "halfcut2":                 # two bonds, orthogonal axes of the quaternion
        U[0][L - 1, :L, :(L + 1) // 2, :] = rot(math.pi / 2, 1)
        U[1][L, L - 1, :, :(L + 1) // 2] = rot(math.pi / 2, 2)
    elif name == "tri":                      # three phases on the face of a bond, so the mean is small
        i1, i2 = L // 3, 2 * L // 3
        U[0][L - 1, :L, :i1 + 1, :] = rot(2.1, 1)
        U[0][L - 1, :L, i2:, :] = rot(2.1, 2)
    elif name == "patch":
        r = min(2, o + 1)
        h = unit(torch.randn(r, r, r, r, 4, generator=g))
        for mu in range(4):
            sl = (slice(o, o + r),) * 4
            U[mu][sl] = h
    elif name == "star":                     # TUNED2 at y of block 00
        for mu in (0, 1):
            U[mu][o, o, o, o] = m1
            s = [o, o, o, o]; s[mu] -= 1
            U[mu][tuple(s)] = m1
    elif name == "starlat":                  # the same defect at a sublattice of block 00, so that every x_0 sits near one
        st = 2 if L <= 5 else 3
        for x in np.ndindex(L, L, L, L):
            if all(c % st == 0 for c in x):
                for mu in (0, 1):
                    if x[mu] < L - 1:
                        U[mu][x] = m1
                    s = list(x); s[mu] -= 1
                    if s[mu] >= 0:
                        U[mu][tuple(s)] = m1
    elif name == "gas":                      # random Dirac slabs of block 00, about L^2 vortex plaquettes
        for _ in range(3):
            mu = int(rng.integers(4)); c = int(rng.integers(L - 1))
            lo = rng.integers(0, L, 4); hi = np.minimum(lo + rng.integers(1, L + 1, 4), L)
            sl = [slice(int(l), int(h)) for l, h in zip(lo, hi)]; sl[mu] = c
            U[mu][tuple(sl)] = m1
    else:
        raise SystemExit("start " + name)
    return noise(U, a, g)

class Search:
    def __init__(self, L, eps, s_rule, base, tag):
        self.L, self.eps, self.s_rule, self.base, self.tag = L, eps, s_rule, base, tag
        self.best = dict(ratio_c=0.0, ratio_a=0.0); self.bestU = None; self.nev = 0
        self.shapes = [u.shape for u in fm.flat_links(L)]
        self.sizes = [int(np.prod(s)) for s in self.shapes]

    def pack(self, U):
        return torch.cat([u.reshape(-1) for u in U]).numpy().copy()

    def unpack(self, x, grad=False):
        t = torch.from_numpy(x); out = []; i = 0
        for s, n in zip(self.shapes, self.sizes):
            q = t[i:i + n].reshape(s); i += n
            if grad:
                q = q.clone().requires_grad_(True)
            out.append(q)
        return out

    def fg(self, x, delta):
        self.nev += 1
        L = self.L
        Q = self.unpack(x, True)
        V = [q / q.norm(dim=-1, keepdim=True) for q in Q]
        f2t = fm.plaquette_f(V, L)
        f2 = {k: v.detach().numpy() for k, v in f2t.items()}
        o = (L - 1) // 2
        bases = {ab: (o, o, o, o) if self.base == "fixed" else fm.rule_base(f2, L, *ab, self.eps, self.s_rule)
                 for ab in ((0, 0), (1, 0), (0, 1), (1, 1))}
        W, r = fm.coarse_W(V, L, bases)
        w2 = ((W - ONE) ** 2).sum()
        ft = torch.cat([v.reshape(-1) for v in f2t.values()])
        fv = np.sqrt(ft.detach().numpy())
        ra, rc, t = fm.splits(fv, L, self.eps)
        w1 = float(w2.detach()) ** 0.5
        rat_c = w1 / rc if rc > 1e-9 else 0.0; rat_a = w1 / ra if ra > 1e-9 else 0.0
        if rat_c > self.best["ratio_c"]:
            self.best = dict(ratio_c=rat_c, ratio_a=max(rat_a, self.best["ratio_a"]), w1=w1, rhs_c=rc, rhs_a=ra, min_m=r,
                             nrough=int((fv > self.eps).sum()), l1_scaled=float(fv.sum()) / L ** 2, bases={str(k): v for k, v in bases.items()}, at_ev=self.nev)
            self.bestU = [v.detach().clone() for v in V]
        irr = torch.from_numpy(fv > t if t >= 0 else np.ones_like(fv, dtype=bool))
        rhs = ((ft[irr] + delta ** 2).sqrt() - delta).sum() / L ** 2 + (ft[~irr].sum() + delta ** 2).sqrt()
        J = -(0.5 * torch.log(w2 + 1e-14) - torch.log(rhs + 1e-12))
        J.backward()
        g = torch.cat([q.grad.reshape(-1) for q in Q]).numpy().copy()
        return float(J.detach()), g

    def run(self, U, evals):
        deltas = [0.1, 0.03, 0.01, 0.003, 0.001]
        x = self.pack(U)
        for d in deltas:
            res = minimize(self.fg, x, args=(d,), jac=True, method="L-BFGS-B",
                           options=dict(maxfun=evals // len(deltas), maxiter=evals // len(deltas), maxcor=20, ftol=1e-10, gtol=1e-9))
            x = res.x.copy()
            for i, q in enumerate(self.unpack(x)):      # renormalise links
                q = q / q.norm(dim=-1, keepdim=True)
            x = self.pack([q / q.norm(dim=-1, keepdim=True) for q in self.unpack(x)])
            guard()
        return x

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, required=True); ap.add_argument("--regime", required=True)
    ap.add_argument("--starts", default="flat,smooth,sheet,sheet_th,sheet_int,halfcut,halfcut2,tri,patch,star,starlat,gas")
    ap.add_argument("--seeds", type=int, default=1); ap.add_argument("--evals", type=int, default=400)
    ap.add_argument("--out", default="runs.jsonl")
    a = ap.parse_args()
    L = a.L
    eps, s_rule, base = {"R1": (0.02 / L ** 2, 0.02, "rule"), "R2": (0.05, 0.25, "rule"), "PC": (0.02 / L ** 2, 0.02, "fixed")}[a.regime]
    overall = 0.0
    for name in a.starts.split(","):
        for seed in range(1, a.seeds + 1):
            t0 = time.time()
            S = Search(L, eps, s_rule, base, name)
            U0 = start(name, L, seed)
            e0 = fm.evaluate(U0, L, eps, s_rule, base)
            S.run(U0, a.evals)
            b = S.best
            rec = dict(L=L, regime=a.regime, start=name, seed=seed, r0=e0["ratio_c"], secs=round(time.time() - t0, 1), nev=S.nev, **b)
            with open(HERE / a.out, "a") as fh:
                fh.write(json.dumps(rec) + "\n")
            print(f"L={L} {a.regime} {name:10s} seed {seed} start Ratio_C {e0['ratio_c']:.3f} best Ratio_C {b['ratio_c']:.4f} Ratio_A {b['ratio_a']:.4f} w1 {b.get('w1',0):.3f} rhs_c {b.get('rhs_c',0):.4f} min|m| {b.get('min_m',0):.3f} nrough {b.get('nrough',0)} evals {S.nev} {rec['secs']}s", flush=True)
            if b["ratio_c"] > overall and S.bestU is not None:
                overall = b["ratio_c"]
                np.savez_compressed(HERE / f"best_{a.regime}_L{L}.npz", **{f"U{i}": u.numpy().astype(np.float64) for i, u in enumerate(S.bestU)})
    print(f"L={L} {a.regime} overall best Ratio_C {overall:.4f}", flush=True)

if __name__ == "__main__":
    main()

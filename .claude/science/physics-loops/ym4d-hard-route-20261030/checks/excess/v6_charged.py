#!/usr/bin/env python3
"""T6 of CRITERIA.md: charged field at small flux, d = 4, SU(2), L = 3, true fibre minimiser.

Background: constant abelian flux (n12, n34) on a fine torus, second Chern number 2 n12 n34.
Perturbation: smooth non-abelian modes plus one localised bump. V := M(U0), then the fibre minimiser from U0.
"""
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from ex_core import Chain, I_grad, Problem, flux_stats, guard, ident, plaquettes, qexp, qinv, qlog, qmul, rss_gb, wilson  # noqa: E402

import torch  # noqa: E402

d = 4


def const_flux(n, n12, n34):
    th12 = 2 * math.pi * n12 / n**2
    th34 = 2 * math.pi * n34 / n**2
    A = torch.zeros((n,) * d + (d, 3), dtype=torch.float64)
    g = torch.meshgrid(*[torch.arange(n, dtype=torch.float64) for _ in range(d)], indexing="ij")
    # A_2 = th x_1, twist on x_1 = n-1
    A[..., 1, 2] = th12 * g[0]
    A[..., 0, 2] = -th12 * n * g[1] * (g[0] == n - 1)
    A[..., 3, 2] = th34 * g[2]
    A[..., 2, 2] = -th34 * n * g[3] * (g[2] == n - 1)
    return qexp(A)


def charge(V):
    """Plaquette charge, four-corner symmetrised (clover) with links ignored on a smooth field: (1/2 pi^2) sum (t12.t34 - t13.t24 + t14.t23)."""
    ps = dict(plaquettes(V))
    th = {k: qlog(v) for k, v in ps.items()}

    def clover(a, b):
        t = th[(a, b)]
        return 0.25 * (t + torch.roll(t, 1, dims=a) + torch.roll(t, 1, dims=b) + torch.roll(t, (1, 1), dims=(a, b)))

    c = {k: clover(*k) for k in th}
    q = (c[(0, 1)] * c[(2, 3)]).sum() - (c[(0, 2)] * c[(1, 3)]).sum() + (c[(0, 3)] * c[(1, 2)]).sum()
    return float(q) / (2 * math.pi**2)


def perturbation(n, amp, bump, seed):
    g = torch.Generator().manual_seed(seed)
    grids = torch.meshgrid(*[torch.arange(n, dtype=torch.float64) for _ in range(d)], indexing="ij")
    A = torch.zeros((n,) * d + (d, 3), dtype=torch.float64)
    for m in range(5):
        k = torch.randint(-1, 2, (d,), generator=g)
        ph = torch.rand(1, generator=g).item() * 2 * math.pi
        c = torch.randn((d, 3), generator=g, dtype=torch.float64)
        wave = torch.cos(sum(2 * math.pi * int(k[a]) * grids[a] / n for a in range(d)) + ph)
        A = A + c * wave[..., None, None]
    A = amp * A / 5
    if bump > 0:
        r2 = sum(((grids[a] - n / 2 + n / 2) % n - n / 2) ** 2 for a in range(d))
        s2 = (n / 6.0) ** 2
        c = torch.randn((d, 3), generator=g, dtype=torch.float64)
        A = A + bump * c * torch.exp(-r2 / (2 * s2))[..., None, None]
    return A


def contours(B, U, base):
    d = B.d
    m = base.shape[1]
    n = B.n
    if not hasattr(B, "groups"):
        B._setup()
    no = len(B.offs)
    G_vals = [ident((m, 1))]
    G_idx = [torch.tensor([B.i0])]
    pos = {B.i0: (0, 0)}
    for io, ip, pv, ax, s in B.groups:
        sites = base[:, :, None] + pv[:, None, :]
        if s < 0:
            sites = sites.clone()
            sites[ax] -= 1
        step = U[tuple(sites[i] % n for i in range(d)) + (ax,)]
        if s < 0:
            step = qinv(step)
        par = torch.stack([G_vals[pos[int(i)][0]][:, pos[int(i)][1]] for i in ip], 1)
        val = qmul(par, step)
        gi = len(G_vals)
        G_vals.append(val)
        G_idx.append(io)
        for t, i in enumerate(io):
            pos[int(i)] = (gi, t)
    G = torch.cat(G_vals, 1)
    order = torch.argsort(torch.cat(G_idx))
    return G[:, order]


def parent_links(B, U, base, mu):
    """M(U) on parent bonds (y, mu) for y in base (d x m)."""
    d, L, n = B.d, B.L, B.n
    G = contours(B, U, base)
    e = torch.zeros_like(base)
    e[mu] = L
    Gp = contours(B, U, base + e)
    sites0 = base[:, :, None] + B.offt[:, None, :]
    ln = U[tuple(sites0[i] % n for i in range(d)) + (mu,)]
    for t in range(1, L):
        sites = sites0.clone()
        sites[mu] += t
        ln = qmul(ln, U[tuple(sites[i] % n for i in range(d)) + (mu,)])
    Om = qmul(qmul(G, ln), qinv(Gp))
    O0 = Om[:, B.i0, :]
    v = qlog(qmul(Om, qinv(O0)[:, None, :]))
    A = v.mean(1)
    return qmul(qexp(A), O0)


class LightProblem(Problem):
    """Same problem; the constraint Jacobian by central differences, so no double backward (memory)."""

    def j(self, U0, v):
        nrm = float(v.abs().max())
        if nrm == 0:
            return torch.zeros(self.cshape)
        eps = 1e-5 / nrm
        rp = self.resid(qmul(qexp(eps * v), U0))
        rm = self.resid(qmul(qexp(-eps * v), U0))
        return (rp - rm) / (2 * eps)

    def _constraint_grad(self, H0, U0, lam, chunk=256):
        """Gradient in H at H0 of <lam, resid>, summed over chunks of parents, so the graph stays small."""
        B = self.chain.levels[0]
        if not hasattr(B, "groups"):
            B._setup()
        total = torch.zeros(self.shape)
        idxs = torch.arange(B.base.shape[1])
        tgt = self.V.reshape(-1, B.d, 4)
        lam_f = lam.reshape(-1, B.d, 3)
        for mu in range(B.d):
            for start in range(0, len(idxs), chunk):
                sel = idxs[start:start + chunk]
                base = B.base[:, sel]
                H = H0.clone().requires_grad_(True)
                Up = qmul(qexp(H), U0)
                r = qlog(qmul(parent_links(B, Up, base, mu), qinv(tgt[sel, mu])))
                val = (lam_f[sel, mu] * r).sum()
                g, = torch.autograd.grad(val, H)
                total += g
                del H, Up, r, val, g
        return total

    def _wilson_grad(self, H0, U0):
        H = H0.clone().requires_grad_(True)
        val = wilson(qmul(qexp(H), U0))
        g, = torch.autograd.grad(val, H)
        return g

    def lag_grad(self, H, U0, lam):
        H = H.detach()
        return self._wilson_grad(H, U0) + self._constraint_grad(H, U0, lam)

    def jt(self, U0, lam):
        return self._constraint_grad(torch.zeros(self.shape), U0, lam)


def report(tag, U, V, chain):
    fV, EV = flux_stats(V)
    fU, EU = flux_stats(U)
    IV = I_grad(V)
    IU = I_grad(U)
    out = dict(tag=tag, fV=fV, EV=EV, fU=fU, EU=EU, e=EU - EV, Igrad=float(IV), Ifine=float(IU), QV=charge(V), QU=charge(U))
    out["e_over_I"] = out["e"] / out["Igrad"]
    out["C_eff_810"] = (out["Igrad"] / 810 - out["e"]) / (fV * EV)
    print(json.dumps(out), flush=True)
    return out


def main():
    Np = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    L = 3
    n = Np * L
    res = []
    chain = Chain(Np, L, d, 1)
    for amp, bump, seed, nn in ((0.0, 0.0, 0, 1), (0.01, 0.0, 1, 1), (0.01, 0.015, 2, 1)):
        t0 = time.time()
        U0 = qmul(qexp(perturbation(n, amp, bump, seed)), const_flux(n, nn, nn))
        V = chain.top(U0)
        rec0 = report(f"U0 amp {amp} bump {bump}", U0, V, chain)
        if amp == 0.0:
            res.append(rec0)
            continue
        P = LightProblem(chain, V)
        U, lam, gn, rn = P.solve(U0, newton=6, gtol=1e-7, ctol=1e-9, verbose=True)
        rec = report(f"min amp {amp} bump {bump}", U, V, chain)
        rec.update(gn=gn, rn=rn, secs=time.time() - t0, rss=rss_gb())
        print(" solver", gn, rn, "secs", time.time() - t0, "rss", rss_gb(), flush=True)
        res.append(rec)
        with open(os.path.join(HERE, f"v6_charged_{Np}.json"), "w") as fh:
            json.dump(res, fh, indent=1)
        guard()


if __name__ == "__main__":
    main()

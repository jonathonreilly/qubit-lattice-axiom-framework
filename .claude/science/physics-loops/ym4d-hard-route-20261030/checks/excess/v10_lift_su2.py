#!/usr/bin/env python3
"""T10 of CRITERIA.md: the non-abelian lift of Section 2.2 in SU(2), d = 2, 3, L = 3."""
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from ex_core import Block, I_grad, flux_stats, guard, ident, plaquettes, qexp, qinv, qlog, qmul  # noqa: E402

import numpy as np  # noqa: E402
import torch  # noqa: E402
from v8_lift1d import build  # noqa: E402


def line_kernels(L):
    n, Nc, T0, R0 = build(L)
    dz = np.roll(T0, -1, axis=0) - T0
    eta = np.zeros((n, Nc))
    for j in range(Nc):
        for s in range(1, Nc // 2):
            eta[:, j] += dz[:, (j + s) % Nc]
        for xx in range(n):
            dist = ((xx - L * j - L / 2 + n / 2) % n) - n / 2
            if abs(dist) > 6.5 * L:
                eta[xx, j] = 0

    def zeta(x, w):
        """kernel of parent site w (parent units) at fine x, both relative to a parent at 0."""
        return T0[(x - w * L) % n, 0]

    def eta_f(x, w):
        return eta[(x - w * L) % n, 0]

    return zeta, eta_f


class Lift:
    def __init__(self, Np, L, d, R=3):
        self.Np, self.L, self.d, self.R = Np, L, d, R
        self.n = Np * L
        self.block = Block(self.n, L, d)
        self.r = (L - 1) // 2
        self.win = list(itertools.product(range(-R, R + 1), repeat=d))
        self.windex = {w: i for i, w in enumerate(self.win)}
        self.offs = list(itertools.product(range(-self.r, self.r + 1), repeat=d))
        self.oindex = {o: i for i, o in enumerate(self.offs)}
        self.inner = [w for w in self.win if max(abs(a) for a in w) <= R - 1]
        z, e = line_kernels(L)
        # K0[o, w]: T_0 at fine offset o of parent site w; Ke[mu][o, w]: T_1 on component mu
        self.K0 = torch.zeros((len(self.offs), len(self.inner)), dtype=torch.float64)
        self.Ke = [torch.zeros((len(self.offs), len(self.inner)), dtype=torch.float64) for _ in range(d)]
        for i, o in enumerate(self.offs):
            for j, w in enumerate(self.inner):
                self.K0[i, j] = float(np.prod([z(o[a], w[a]) for a in range(d)]))
                for mu in range(d):
                    self.Ke[mu][i, j] = float(np.prod([e(o[a], w[a]) if a == mu else z(o[a], w[a]) for a in range(d)]))
        self.par = {}
        for w in self.win:
            if all(a == 0 for a in w):
                continue
            ax = max(a for a in range(d) if w[a] != 0)
            s = 1 if w[ax] > 0 else -1
            p = list(w)
            p[ax] -= s
            self.par[w] = (tuple(p), ax, s)
        self.order = sorted(self.par, key=lambda w: (max(i for i in range(d) if w[i] != 0), sum(abs(a) for a in w)))

    def transports(self, V):
        """T[w]: tensor over parent y of the comb transport from y to y + w L."""
        d = self.d
        T = {tuple([0] * d): ident((self.Np,) * d)}
        for w in self.order:
            p, ax, s = self.par[w]
            sh = tuple(-a for a in p)
            if s > 0:
                link = torch.roll(V[..., ax, :], shifts=sh, dims=tuple(range(d)))
            else:
                sh2 = list(sh)
                sh2[ax] += 1
                link = qinv(torch.roll(V[..., ax, :], shifts=tuple(sh2), dims=tuple(range(d))))
            T[w] = qmul(T[p], link)
        return T

    def lift_flat(self, V):
        d, L, Np = self.d, self.L, self.Np
        n = self.n
        T = self.transports(V)
        # v^(y) on inner bonds, stacked
        v = {}
        for w in self.inner:
            sh = tuple(-a for a in w)
            for mu in range(d):
                w2 = list(w)
                w2[mu] += 1
                link = torch.roll(V[..., mu, :], shifts=sh, dims=tuple(range(d)))
                v[(w, mu)] = qlog(qmul(qmul(T[w], link), qinv(T[tuple(w2)])))
        A = {}
        for mu in range(d):
            stack = torch.stack([v[(w, mu)] for w in self.inner], -2)  # (Np^d, nw, 3)
            A[mu] = torch.einsum("oi,...ic->...oc", self.Ke[mu], stack)  # (Np^d, no, 3)
        Uf = ident((n,) * d + (d,))
        centres = torch.meshgrid(*[torch.arange(Np) for _ in range(d)], indexing="ij")
        for mu in range(d):
            for o in self.offs:
                io = self.oindex[o]
                site = [(centres[a] * L + o[a]) % n for a in range(d)]
                a_ = A[mu][..., io, :]
                if o[mu] < self.r:
                    val = qexp(a_)
                else:
                    # crossing bond to the parent y' := y + e_mu at offset o' with o'_mu = -r
                    op = list(o)
                    op[mu] = -self.r
                    iop = self.oindex[tuple(op)]
                    emu = [0] * d
                    emu[mu] = 1
                    # lambda(y'') on the window around y', with y'' = y' + w L, in frame y
                    lam = []
                    for w in self.inner:
                        w1 = tuple(w[a] + emu[a] for a in range(d))
                        Ty = T[w1]
                        Typ = torch.roll(T[w], shifts=tuple(-e for e in emu), dims=tuple(range(d)))
                        gam = qmul(Ty, qinv(Typ))
                        gam0 = T[tuple(emu)]
                        lam.append(qlog(qmul(gam, qinv(gam0))))
                    lam = torch.stack(lam, -2)
                    t0 = torch.einsum("i,...ic->...c", self.K0[iop], lam)
                    val = qmul(qmul(qexp(a_), qexp(t0)), T[tuple(emu)])
                Uf[tuple(site) + (mu,)] = val
        return Uf, A, T

    def lift0(self, V):
        d, L, Np, n = self.d, self.L, self.Np, self.n
        Uf, A, T = self.lift_flat(V)
        from v6_charged import contours

        B = self.block
        if not hasattr(B, "groups"):
            B._setup()
        G = contours(B, Uf, B.base)
        phi = qlog(G).mean(1).reshape((Np,) * d + (3,))
        # fine gauge constant on blocks
        idx = [((torch.arange(n) + self.r) // L) % Np for _ in range(d)]
        g = torch.meshgrid(*idx, indexing="ij")
        gf = qexp(-phi[g])
        out = Uf.clone()
        for mu in range(d):
            out[..., mu, :] = qmul(qmul(gf, Uf[..., mu, :]), qinv(torch.roll(gf, -1, dims=mu)))
        return out, Uf, A, T

    def check_C(self, V, Uf, T):
        """(c): block-internal plaquettes of the frame-y field against T_2 of theta' in frame y."""
        d, L = self.d, self.L
        z, e = line_kernels(L)
        hol = dict(plaquettes(V))
        worst = 0.0
        for (mu, nu), P in hol.items():
            th = []
            for w in self.inner:
                sh = tuple(-a for a in w)
                Pw = torch.roll(P, shifts=sh, dims=tuple(range(d)))
                th.append(qlog(qmul(qmul(T[w], Pw), qinv(T[w]))))
            th = torch.stack(th, -2)
            th_f = qlog(dict(plaquettes(Uf))[(mu, nu)])
            for o in self.offs:
                if o[mu] >= self.r or o[nu] >= self.r:
                    continue
                k = torch.tensor([float(np.prod([e(o[a], w[a]) if a in (mu, nu) else z(o[a], w[a]) for a in range(d)])) for w in self.inner], dtype=torch.float64)
                pred = torch.einsum("i,...ic->...c", k, th)
                site = torch.meshgrid(*[torch.arange(self.Np) * L + o[a] for a in range(d)], indexing="ij")
                got = th_f[tuple(s_ % self.n for s_ in site)]
                worst = max(worst, float((got - pred).norm(dim=-1).max()))
        return worst

    def psi(self, V, Y):
        Vy = qmul(qexp(Y), V)
        U, *_ = self.lift0(Vy)
        return qlog(qmul(self.block(U), qinv(V))), U


def smooth_field(N, d, amp, seed):
    g = torch.Generator().manual_seed(seed)
    grids = torch.meshgrid(*[torch.arange(N, dtype=torch.float64) for _ in range(d)], indexing="ij")
    A = torch.zeros((N,) * d + (d, 3), dtype=torch.float64)
    for m in range(5):
        k = torch.randint(-1, 2, (d,), generator=g)
        ph = torch.rand(1, generator=g).item() * 2 * math.pi
        c = torch.randn((d, 3), generator=g, dtype=torch.float64)
        wave = torch.cos(sum(2 * math.pi * int(k[a]) * grids[a] / N for a in range(d)) + ph)
        A = A + c * wave[..., None, None]
    return qexp(amp * A / 5)


def main():
    L, Np = 3, 8
    for d in (2, 3):
        Lf = Lift(Np, L, d)
        print(f"d {d}: window nonzero check K0 {float(Lf.K0.abs().sum(0).min()):.2e}", flush=True)
        # (e) constant abelian flux
        n = Np
        th = 2 * math.pi / Np**2
        g = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64) for _ in range(d)], indexing="ij")
        Ac = torch.zeros((Np,) * d + (d, 3), dtype=torch.float64)
        Ac[..., 1, 2] = th * g[0]
        Ac[..., 0, 2] = -th * Np * g[1] * (g[0] == Np - 1)
        Vc = qexp(Ac)
        m, _ = Lf.psi(Vc, torch.zeros_like(Ac))
        print(f" constant flux f {th:.4f}: max|m| {float(m.abs().max()):.3e}", flush=True)
        prev = {}
        for amp in (0.8, 0.4, 0.2):
            V = smooth_field(Np, d, amp, 7)
            f, E = flux_stats(V)
            Y = torch.zeros((Np,) * d + (d, 3), dtype=torch.float64)
            m0, U0 = Lf.psi(V, Y)
            hist = []
            for it in range(40):
                r, U = Lf.psi(V, Y)
                rn = float(r.norm(dim=-1).max())
                hist.append(rn)
                if rn < 1e-12:
                    break
                Y = Y - r
                guard()
            mrat = float(m0.norm(dim=-1).max()) / f**2
            _, Uf0, _, T0 = Lf.lift0(V)
            crat = Lf.check_C(V, Uf0, T0) / f**2
            Ii = float(I_grad(V))
            fU, EU = flux_stats(U)
            # (c): block-internal plaquettes of the unflattened field against T_2
            print(f" d {d} amp {amp}: f {f:.4f} max|m|/f^2 {mrat:.4f} (C)/f^2 {crat:.4f} picard its {len(hist)} final {hist[-1]:.2e} first {hist[0]:.2e} | fU {fU:.4f} fU L^2/f {fU*L**2/f:.3f} excess {EU-E:.4e} I {Ii:.4e} ratio {(EU-E)/Ii:.4f} I_fine/I {float(I_grad(U))/Ii:.4f}", flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""T0-T5 of CRITERIA.md: variance identity, remainder order, Bianchi transverse bound, on the real comb map."""
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from ex_core import Block, flux_stats, guard, ident, plaquettes, qexp, qinv, qlog, qmul, rot  # noqa: E402

import torch  # noqa: E402

d = 4


def tau(L):
    r = (L - 1) // 2
    ts = list(range(-r, r + L))
    return {t: sum(1 for a in range(-r, r + 1) if a <= t <= a + L - 1) for t in ts}


def kernel(L, n, mu, nu, d=4):
    """chi_0(z) on an n^d torus, centred at site 0, orientation (mu, nu)."""
    r = (L - 1) // 2
    t = tau(L)
    axes = []
    for a in range(d):
        v = torch.zeros(n, dtype=torch.float64)
        if a in (mu, nu):
            for s, c in t.items():
                v[s % n] += c
        else:
            for s in range(-r, r + 1):
                v[s % n] += 1
        axes.append(v)
    out = axes[0]
    for a in range(1, d):
        out = out.unsqueeze(-1) * axes[a]
    return out / L**6


def transport_from(U, y, d=4):
    """T(z): holonomy from y to z along the comb axis 0, then 1, ... with the seam opposite y. Shape (n^d, 4). Then Ad(T(z)) sends a quantity at z to y."""
    n = U.shape[0]
    T = ident((n,) * d)
    half = n // 2
    for ax in range(d - 1, -1, -1):
        # build by sweeping along ax for sites whose later axes are at y
        pass
    # explicit: order of offsets; path goes axis 0, 1, 2, 3 with signed steps.
    # Implement by dynamic programming on offsets in [-half, n-half-1]^d.
    offs = [torch.arange(-half, n - half) for _ in range(d)]
    G = torch.meshgrid(*offs, indexing="ij")
    res = ident((n,) * d)
    # stage a: for sites with offsets zero in axes > a, step along axis a from the site with offset zero in axis a
    filled = torch.zeros((n,) * d, dtype=torch.bool)
    idx0 = tuple(y)
    res[idx0] = ident(())
    filled[idx0] = True
    for a in range(d):
        for sgn in (1, -1):
            for dist in range(1, (n - half if sgn > 0 else half + 1)):
                mask = torch.ones((n,) * d, dtype=torch.bool)
                for b in range(a + 1, d):
                    mask &= G[b] == 0
                mask &= G[a] == sgn * dist
                idxs = mask.nonzero()
                # site of offset o -> absolute (y + o) mod n
                src = idxs.clone()
                offv = torch.stack([G[b][mask] for b in range(d)], 1)
                abso = (offv + torch.tensor(y)) % n
                prev = offv.clone()
                prev[:, a] -= sgn
                absp = (prev + torch.tensor(y)) % n
                if sgn > 0:
                    step = U[tuple(absp[:, b] for b in range(d)) + (a,)]
                else:
                    step = qinv(U[tuple(abso[:, b] for b in range(d)) + (a,)])
                val = qmul(res[tuple(absp[:, b] for b in range(d))], step)
                res[tuple(abso[:, b] for b in range(d))] = val
    return res


def make_field(n, amp, seed, kind="smooth", d=4):
    g = torch.Generator().manual_seed(seed)
    grids = torch.meshgrid(*[torch.arange(n, dtype=torch.float64) for _ in range(d)], indexing="ij")
    A = torch.zeros((n,) * d + (d, 3), dtype=torch.float64)
    if kind == "white":
        A = amp * torch.randn(A.shape, generator=g, dtype=torch.float64)
    else:
        for m in range(6):
            k = torch.randint(-1, 2, (d,), generator=g)
            ph = torch.rand(1, generator=g).item() * 2 * math.pi
            c = torch.randn((d, 3), generator=g, dtype=torch.float64)
            wave = torch.cos(sum(2 * math.pi * int(k[a]) * grids[a] / n for a in range(d)) + ph)
            A = A + c * wave[..., None, None]
        A = amp * A / 6
    return qexp(A)


def abelianise(U):
    Z = U.clone()
    Z[..., 1:3] = 0
    return Z / torch.sqrt((Z * Z).sum(-1, keepdim=True))


def all_quantities(U, L):
    n = U.shape[0]
    b = Block(n, L, 4)
    V = b(U)
    Np = n // L
    th_f = {p: qlog(q) for p, q in plaquettes(U)}
    th_c = {p: qlog(q) for p, q in plaquettes(V)}
    kers = {p: kernel(L, n, p[0], p[1]) for p in th_f}
    ys = list(itertools.product(range(Np), repeat=4))
    var_sum = 0.0
    cross = 0.0
    rmax = 0.0
    rec = []
    for yc in ys:
        y = tuple(c * L for c in yc)
        T = transport_from(U, y)
        for p, th in th_f.items():
            F = rot(T, th)
            chi = torch.roll(kers[p], shifts=y, dims=(0, 1, 2, 3))
            m = (chi[..., None] * F).sum((0, 1, 2, 3))
            second = (chi * (F * F).sum(-1)).sum()
            var = second - (m * m).sum()
            tc = th_c[p][yc]
            r = tc - L**2 * m
            var_sum += L**4 * float(var)
            cross += float(2 * (tc * r).sum() - (r * r).sum())
            nl = float(((torch.abs(chi) > 0) * (th * th).sum(-1)).sum())
            rmax = max(rmax, float(r.norm()))
            rec.append((float(r.norm()), nl))
        guard()
    E0 = sum(float((t * t).sum()) for t in th_f.values())
    E1 = sum(float((t * t).sum()) for t in th_c.values())
    return dict(E0=E0, E1=E1, var=var_sum, cross=cross, rmax=rmax, rec=rec, V=V)


def bianchi_and_grad(V):
    th = {p: qlog(q) for p, q in plaquettes(V)}
    d = V.shape[-2]

    def get(a, b):
        return th[(a, b)] if a < b else -th[(b, a)]

    def nabla(e, X):
        return rot(V[..., e, :], torch.roll(X, -1, dims=e)) - X

    P = T = B2 = 0.0
    for mu, nu in itertools.combinations(range(d), 2):
        t = th[(mu, nu)]
        for e in range(d):
            s = float((nabla(e, t) ** 2).sum())
            if e in (mu, nu):
                P += s
            else:
                T += s
    for mu, nu, rho in itertools.combinations(range(d), 3):
        B = nabla(rho, get(mu, nu)) + nabla(mu, get(nu, rho)) + nabla(nu, get(rho, mu))
        B2 += float((B * B).sum())
    E = sum(float((t * t).sum()) for t in th.values())
    f = max(float(torch.sqrt((t * t).sum(-1)).max()) for t in th.values())
    return dict(P=P, T=T, B2=B2, E=E, f=f)


def main():
    print("T0")
    for L in (3, 5):
        n = 3 * L
        for p in ((0, 1), (1, 3)):
            k = kernel(L, n, *p)
            print(" L", L, "mass-1", float(k.sum()) - 1, end=" ")
            tot = torch.zeros_like(k)
            for s in itertools.product(range(3), repeat=4):
                tot += torch.roll(k, shifts=tuple(a * L for a in s), dims=(0, 1, 2, 3))
            print("pou err", float((tot - L**-4).abs().max()))
        t = tau(L)
        ov = sum(min(t.get(s, 0), t.get(s - L, 0)) for s in range(-L, 2 * L)) / L**2
        print(" overlap", ov, "formula", (1 - L**-2) / 4)
    L, n = 3, 9
    print("T1 abelian")
    U = abelianise(make_field(n, 0.05, 1, "white"))
    Q = all_quantities(U, L)
    print(" E0-E1", Q["E0"] - Q["E1"], "var", Q["var"], "rel", (Q["E0"] - Q["E1"] - Q["var"]) / Q["var"])
    print("T2 remainder order and identity, white and smooth")
    for kind, amps in (("white", (0.04, 0.02, 0.01)), ("smooth", (0.4, 0.2, 0.1))):
        for amp in amps:
            U = make_field(n, amp, 2, kind)
            Q = all_quantities(U, L)
            ratio = max(a / max(b, 1e-30) for a, b in Q["rec"] if b > 0)
            print(f" {kind} amp {amp}: rmax {Q['rmax']:.4e} rmax/amp^2 {Q['rmax']/amp**2:.4e} max r/n {ratio:.4e}; E0-E1 {Q['E0']-Q['E1']:.5e} var {Q['var']:.5e} cross {Q['cross']:.3e} id-err {(Q['E0']-Q['E1'])-(Q['var']-Q['cross']):.2e}")
            B = bianchi_and_grad(Q["V"])
            f, E = B["f"], B["E"]
            print(f"   V: f {f:.4f} E {E:.4e} P {B['P']:.4e} T {B['T']:.4e} T/P {B['T']/B['P']:.3f} B2/(f^2 E) {B['B2']/(f*f*E):.3f} (T-2P)/(fE) {(B['T']-2*B['P'])/(f*E):.3f}; excess-based c: (E0-E1)/(I) {(Q['E0']-Q['E1'])/(B['P']+B['T']):.4f}")
    print("T4 sharpness")
    N = 24
    for k in (1,):
        grids = torch.meshgrid(*[torch.arange(N, dtype=torch.float64) for _ in range(4)], indexing="ij")
        phase = sum(2 * math.pi * k * grids[a] / N for a in range(3))
        A = torch.zeros((N,) * 4 + (4, 3), dtype=torch.float64)
        A[..., 3, 2] = 0.01 * torch.sin(phase)
        B = bianchi_and_grad(qexp(A))
        print(" T/P", B["T"] / B["P"])


if __name__ == "__main__":
    main()

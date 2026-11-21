#!/usr/bin/env python3
"""T11 of CRITERIA.md: Lemma TL at a variation, block-local gauge."""
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from v1_identity import kernel, make_field, transport_from  # noqa: E402
from ex_core import Block, guard, plaquettes, qexp, qlog, qmul, rot  # noqa: E402

import torch  # noqa: E402

dt = 1e-4


def frames(U, L, y):
    """Plaquette angles of U in the axial gauge at y (fine, dict), parent angles in that gauge at all parents (dict)."""
    n = U.shape[0]
    Np = n // L
    T = transport_from(U, y)
    th = {p: rot(T, qlog(q)) for p, q in plaquettes(U)}
    V = Block(n, L, 4)(U)
    idx = tuple(torch.arange(Np) * L for _ in range(4))
    Tc = T[torch.meshgrid(*idx, indexing="ij")]
    thc = {p: rot(Tc, qlog(q)) for p, q in plaquettes(V)}
    return th, thc


def run(amp, Hamp, seed, L=3, Np=3):
    n = L * Np
    U = make_field(n, amp, seed, "smooth")
    g = torch.Generator().manual_seed(seed + 100)
    grids = torch.meshgrid(*[torch.arange(n, dtype=torch.float64) for _ in range(4)], indexing="ij")
    H = torch.zeros((n,) * 4 + (4, 3), dtype=torch.float64)
    for m in range(4):
        k = torch.randint(-1, 2, (4,), generator=g)
        ph = torch.rand(1, generator=g).item() * 2 * math.pi
        c = torch.randn((4, 3), generator=g, dtype=torch.float64)
        wave = torch.cos(sum(2 * math.pi * int(k[a]) * grids[a] / n for a in range(4)) + ph)
        H = H + c * wave[..., None, None]
    H = Hamp * H / 4
    Up = qmul(qexp(dt * H), U)
    Um = qmul(qexp(-dt * H), U)
    kers = {p: kernel(L, n, p[0], p[1]) for p in itertools.combinations(range(4), 2)}
    w = math.ceil(L / 4)
    eps = (1 - L**-2) / 4
    worst_t = worst_i = 0.0

    def Gq(th, a, b):
        return th[(a, b)] if a < b else -th[(b, a)]

    for yc in itertools.product(range(Np), repeat=4):
        y = tuple(c * L for c in yc)
        thp, tcp = frames(Up, L, y)
        thm, tcm = frames(Um, L, y)
        Fd = {p: (thp[p] - thm[p]) / (2 * dt) for p in thp}
        Td = {p: (tcp[p] - tcm[p]) / (2 * dt) for p in tcp}

        def sig(a, b, yy):
            p = (a, b) if a < b else (b, a)
            chi = torch.roll(kers[p], shifts=tuple((c * L) % n for c in yy), dims=(0, 1, 2, 3))
            m = (chi[..., None] * Fd[p]).sum((0, 1, 2, 3))
            sec = (chi * (Fd[p] ** 2).sum(-1)).sum()
            return float(torch.sqrt(torch.clamp(sec - (m * m).sum(), min=0)))

        def shift(yy, e):
            z = list(yy)
            z[e] = (z[e] + 1) % Np
            return tuple(z)

        for mu, nu, rho in itertools.permutations(range(4), 3):
            a = Gq(Td, mu, nu)
            xdot = float((a[shift(yc, rho)] - a[yc]).norm())
            rhs = (1 - w / L) ** -1 * L**2 * (
                (L / w) ** 0.5 * (sig(mu, nu, yc) + sig(mu, nu, shift(yc, rho)))
                + (4 * w / (3 * L)) ** 0.5 * (sig(nu, rho, yc) + sig(nu, rho, shift(yc, mu)) + sig(rho, mu, yc) + sig(rho, mu, shift(yc, nu)))
            )
            worst_t = max(worst_t, xdot / max(rhs, 1e-14))
        for mu, nu in itertools.permutations(range(4), 2):
            a = Gq(Td, mu, nu)
            xdot = float((a[shift(yc, mu)] - a[yc]).norm())
            rhs = L**2 * eps**-0.5 * (sig(mu, nu, yc) + sig(mu, nu, shift(yc, mu)))
            worst_i = max(worst_i, xdot / max(rhs, 1e-14))
        guard()
    return worst_t, worst_i


def main():
    for amp in (0.2, 0.1, 0.05, 0.0):
        for Hamp in (1.0,):
            wt, wi = run(amp, Hamp, 3)
            print(f"amp {amp} H {Hamp}: max ratio transverse {wt:.4f} in-plane {wi:.4f}", flush=True)


if __name__ == "__main__":
    main()

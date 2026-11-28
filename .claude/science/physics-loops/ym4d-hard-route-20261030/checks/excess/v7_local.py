#!/usr/bin/env python3
"""T7 of CRITERIA.md: pointwise in-plane and transverse bounds by local variances."""
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "gate_ex"))
from v1_identity import abelianise, kernel, make_field, transport_from  # noqa: E402
from ex_core import Block, guard, plaquettes, qlog, rot  # noqa: E402

import torch  # noqa: E402


def sigmas(U, L):
    """sigma[(mu,nu)][yc] with gauge at y."""
    n = U.shape[0]
    Np = n // L
    th = {p: qlog(q) for p, q in plaquettes(U)}
    kers = {p: kernel(L, n, p[0], p[1]) for p in th}
    sig = {p: torch.zeros((Np,) * 4, dtype=torch.float64) for p in th}
    for yc in itertools.product(range(Np), repeat=4):
        y = tuple(c * L for c in yc)
        T = transport_from(U, y)
        for p, t in th.items():
            F = rot(T, t)
            chi = torch.roll(kers[p], shifts=y, dims=(0, 1, 2, 3))
            m = (chi[..., None] * F).sum((0, 1, 2, 3))
            second = (chi * (F * F).sum(-1)).sum()
            sig[p][yc] = torch.sqrt(torch.clamp(second - (m * m).sum(), min=0))
        guard()
    return sig


def test(U, L):
    V = Block(U.shape[0], L, 4)(U)
    th = {p: qlog(q) for p, q in plaquettes(V)}

    def get(a, b):
        return th[(a, b)] if a < b else -th[(b, a)]

    sig = sigmas(U, L)

    def S(a, b):
        return sig[(a, b)] if a < b else sig[(b, a)]

    def sh(x, e):
        return torch.roll(x, -1, dims=e)

    def nabla(e, X):
        return rot(V[..., e, :], torch.roll(X, -1, dims=e)) - X

    w = math.ceil(L / 4)
    eps = (1 - L**-2) / 4
    worst_t = worst_i = -1e9
    ratio_t = ratio_i = 0.0
    for mu, nu, rho in itertools.permutations(range(4), 3):
        lhs = nabla(rho, get(mu, nu)).norm(dim=-1)
        rhs = (1 - w / L) ** -1 * L**2 * (
            (L / w) ** 0.5 * (S(mu, nu) + sh(S(mu, nu), rho))
            + (4 * w / (3 * L)) ** 0.5 * (S(nu, rho) + sh(S(nu, rho), mu) + S(rho, mu) + sh(S(rho, mu), nu))
        )
        worst_t = max(worst_t, float((lhs - rhs).max()))
        ratio_t = max(ratio_t, float((lhs / rhs.clamp(min=1e-14)).max()))
    for mu, nu in itertools.permutations(range(4), 2):
        lhs = nabla(mu, get(mu, nu)).norm(dim=-1)
        rhs = L**2 * eps**-0.5 * (S(mu, nu) + sh(S(mu, nu), mu))
        worst_i = max(worst_i, float((lhs - rhs).max()))
        ratio_i = max(ratio_i, float((lhs / rhs.clamp(min=1e-14)).max()))
    return worst_t, ratio_t, worst_i, ratio_i


def main():
    for L, Np, cases in ((3, 3, (("white", 0.03, 1), ("smooth", 0.2, 2))), (5, 3, (("white", 0.01, 3),))):
        n = L * Np
        for kind, amp, seed in cases:
            U = abelianise(make_field(n, amp, seed, kind))
            print(f"abelian L {L} {kind} amp {amp}: worst excess T {{:.3e}} max ratio T {{:.4f}} worst excess I {{:.3e}} ratio I {{:.4f}}".format(*test(U, L)), flush=True)
    L, Np = 3, 3
    n = L * Np
    for kind, amps in (("white", (0.04, 0.02, 0.01)), ("smooth", (0.2, 0.1, 0.05))):
        for amp in amps:
            U = make_field(n, amp, 5, kind)
            print(f"nonabelian L {L} {kind} amp {amp}: worst excess T {{:.3e}} max ratio T {{:.4f}} worst excess I {{:.3e}} ratio I {{:.4f}}".format(*test(U, L)), flush=True)


if __name__ == "__main__":
    main()

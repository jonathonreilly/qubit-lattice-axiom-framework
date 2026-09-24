#!/usr/bin/env python3
"""Independent check: field energy is the clocked energy of a uniform background."""
from fractions import Fraction as F
import itertools


def sites(n=3):
    return list(itertools.product(range(n), repeat=3))


def bonds(n=3):
    S = sites(n)
    out = []
    for x in S:
        for a in range(3):
            y = list(x)
            y[a] = (y[a] + 1) % n
            out.append((x, tuple(y)))
    return out


def main():
    n = 3
    S = sites(n)
    B = bonds(n)
    phi = {x: F(1 + x[0] + 2 * x[1] + 3 * x[2], 4) for x in S}
    bond_sum = sum((phi[x] - phi[y]) ** 2 for x, y in B)
    # (phi Lambda phi 1)_x = phi_x * sum_y~x (phi_x - phi_y)
    acc = F(0)
    nbrs = {x: [] for x in S}
    for x, y in B:
        nbrs[x].append(y)
        nbrs[y].append(x)
    for x in S:
        lap = sum(phi[x] - phi[y] for y in nbrs[x])
        acc += phi[x] * lap
    ok = acc == bond_sum
    # zero mode
    inv = {x: 1 / phi[x] for x in S}
    zero = True
    for x in S:
        applied = phi[x] * sum(phi[x] * inv[x] - phi[y] * inv[y] for y in nbrs[x])
        zero &= applied == 0
    # pinning: min_eta cs(eps+eta)^2 + mu eta^2 = c mu s eps^2 / (c s + mu)
    c, s, mu, eps = F(2), F(3), F(5), F(7)
    # quadratic in eta: (c*s)(eps+eta)^2 + mu eta^2
    # derivative: 2 cs (eps+eta) + 2 mu eta = 0 => eta = -cs eps / (cs+mu)
    eta = -c * s * eps / (c * s + mu)
    value = c * s * (eps + eta) ** 2 + mu * eta ** 2
    want = c * mu * s * eps ** 2 / (c * s + mu)
    ok &= value == want
    print(f"gram {acc==bond_sum} zero_mode {zero} pinned {value}={want}")
    if ok and zero:
        print(
            "HIT: confirmed - on the 3^3 torus the bond sum equals <1|phi Lambda phi|1>, "
            "phi Lambda phi (1/phi) is 0, and a pinning mu gives stiffness c mu s/(c s+mu)"
        )
        print(
            "SUMMARY: confirmed the rewriting and the zero-energy background; "
            "the chiral-sea numerics were not recomputed"
        )
    else:
        print("SUMMARY: fails at the Gram identity or the pinning formula")


if __name__ == "__main__":
    main()

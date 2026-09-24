#!/usr/bin/env python3
"""Independent check of J:attack-e:PR8664.

The soft factor (3/4)(1+ab/3) is 1 when the neighbour agrees and 1/2 when it
disagrees, so a condition is determined by how many neighbours are +1 and how
many are -1. Orders on a short path are enumerated with Fractions, not bit shifts.
"""
from fractions import Fraction as Fr
from itertools import permutations, product


def kernel(a, vals):
    mass = Fr(1, 2)
    for b in vals:
        mass *= 1 if a == b else Fr(1, 2)
    return mass


def total(n_plus, n_minus):
    # a=+1 meets n_minus disagreements; a=-1 meets n_plus
    return Fr(1, 2) ** (1 + n_minus) + Fr(1, 2) ** (1 + n_plus)


def path_law(n, rule, alphabet=(1, -1)):
    sites = tuple(range(n))
    nb = {i: {j for j in sites if abs(i - j) == 1} for i in sites}
    ref = None
    for order in permutations(sites):
        layer = {(): Fr(1)}
        for step, s in enumerate(order):
            idx = [i for i in range(step) if order[i] in nb[s]]
            nxt = {}
            for part, mass in layer.items():
                vals = [part[i] for i in idx]
                for a in alphabet:
                    m = rule(a, vals)
                    if m:
                        nxt[part + (a,)] = nxt.get(part + (a,), 0) + mass * m
            layer = nxt
        where = {s: i for i, s in enumerate(order)}
        law = {tuple(part[where[s]] for s in sites): m for part, m in layer.items()}
        if ref is None:
            ref = law
        elif law != ref:
            raise SystemExit("order dependence")
    return ref


def main():
    # closed form versus the product formula, every count pair
    for n in range(7):
        for p in range(n + 1):
            m = n - p
            vals = (1,) * p + (-1,) * m
            prod = sum(Fr(1, 2) * __import__("math").prod(
                Fr(3, 4) * (1 + Fr(a * b, 3)) for b in vals) for a in (1, -1))
            if prod != total(p, m):
                raise SystemExit(f"formula {p} {m}")
    masses = {(p, n - p): total(p, n - p) for n in range(7) for p in range(n + 1)}
    if masses[(0, 0)] != 1:
        raise SystemExit("empty")
    if max(masses[(p, m)] for p, m in masses if p + m >= 1) != Fr(3, 4):
        raise SystemExit("one neighbour")
    if masses[(3, 3)] != Fr(1, 8):
        raise SystemExit("min")
    if masses[(6, 0)] != Fr(65, 128) or masses[(0, 6)] != Fr(65, 128):
        raise SystemExit("65")
    six = {masses[(p, 6 - p)] for p in range(7)}
    if max(six) != Fr(65, 128) or min(six) != Fr(1, 8):
        raise SystemExit("six")
    if Fr(65, 128) in (max(masses.values()), min(masses.values())):
        raise SystemExit("extremum")
    print("P6 FOLLOWS from the count formula: total mass is (2^{-m}+2^{-p})/2. "
          "Empty is 1, one formed neighbour is 3/4, three +1 and three -1 is 1/8, "
          "and 65/128 is only the maximum among the six-neighbour lists")

    law = path_law(5, kernel)
    Z = sum(law.values())
    if Z != Fr(3, 4) ** 4:
        raise SystemExit(f"completion {Z}")
    cond = {c: m / Z for c, m in law.items()}
    corr = [sum(p * c[0] * c[d] for c, p in cond.items()) for d in range(1, 5)]
    if corr != [Fr(1, 3 ** d) for d in range(1, 5)]:
        raise SystemExit(f"corr {corr}")
    print(f"PATH FOLLOWS: soft rule on a 5-site path, all 120 orders, one law, "
          f"completion (3/4)^4 = {Z}, correlations 3^{{-d}}")

    six_alpha = tuple(range(6))

    def reject6(a, vals):
        return Fr(0) if a in vals else Fr(1, 6)

    law6 = path_law(4, reject6, alphabet=six_alpha)
    Z6 = sum(law6.values())
    agree = [sum(m for c, m in law6.items() if c[0] == c[d]) / Z6 for d in range(4)]
    want = [Fr(1, 6) * (1 + 5 * Fr(-1, 5) ** d) for d in range(4)]
    if Z6 != Fr(5, 6) ** 3 or agree != want:
        raise SystemExit(f"six {Z6} {agree}")
    print(f"SIX FOLLOWS: rejection on a 4-site path, all 24 orders, completion {Z6}, "
          f"agreement {agree}")

    print("SUMMARY: confirmed - 65/128 is the soft-rule total only when all six neighbours "
          "agree; over every neighbour condition the total runs from 1/8 to 1, and is 3/4 "
          "with one formed neighbour")
    print("HIT: confirmed - PR #8664's label of 65/128 as the worst case of K=(3/4)(1+ab/3) "
          "on every neighbour condition is too narrow: the minimum is 1/8 at three +1 and "
          "three -1, and 65/128 is only the maximum among six-neighbour conditions")


if __name__ == "__main__":
    main()

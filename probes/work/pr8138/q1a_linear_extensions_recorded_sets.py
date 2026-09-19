#!/usr/bin/env python3
"""J:attack-g:PR8138 — brute-force Q1a: linear extensions of the 2x2x2 product order.

Note (declared objects / Q1a): a box B = {0,...,n1} x {0,...,n2} x {0,...,n3}
with the product order; the predecessor set A_x = {x - e_i : x_i >= 1}; a
linear extension records neighbors already written. Executed: 'the 48 linear
extensions of the 2x2x2 product order share one recorded-set family, the
predecessor sets'.

Literal check on the 2x2x2 cube ({0,1}^3, eight sites): enumerate every
permutation of the sites, keep those that are linear extensions of the
product order, and for each compute the recorded-set family (nearest-neighbor
bonds whose other end is earlier in the order). HIT if the count is not 48
or if some extension's recorded sets differ from the predecessor family.
"""
from __future__ import annotations

from itertools import permutations, product


SITES = tuple(product((0, 1), repeat=3))  # 8 sites of the 2x2x2 cube


def leq(x, y) -> bool:
    return all(a <= b for a, b in zip(x, y))


def neighbors(x):
    out = []
    for i in range(3):
        for d in (-1, 1):
            y = list(x)
            y[i] += d
            y = tuple(y)
            if y in SITES:
                out.append(y)
    return out


def predecessors(x):
    out = []
    for i in range(3):
        if x[i] >= 1:
            y = list(x)
            y[i] -= 1
            out.append(tuple(y))
    return tuple(sorted(out))


def is_linear_extension(perm) -> bool:
    pos = {s: i for i, s in enumerate(perm)}
    for x in SITES:
        for y in SITES:
            if x != y and leq(x, y) and pos[x] > pos[y]:
                return False
    return True


def recorded_family(perm):
    pos = {s: i for i, s in enumerate(perm)}
    return tuple(tuple(sorted(y for y in neighbors(x) if pos[y] < pos[x])) for x in SITES)


def main():
    expected = tuple(predecessors(x) for x in SITES)
    exts = [p for p in permutations(SITES) if is_linear_extension(p)]
    families = {recorded_family(e) for e in exts}
    n = len(exts)
    print(f"sites={len(SITES)} permutations_tested={len(SITES)}! linear_extensions={n}")
    print(f"recorded-set families={len(families)}")
    print(f"predecessor family among them: {expected in families}")
    print(f"families == {{predecessors}}: {families == {expected}}")

    if n == 48 and families == {expected}:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on Q1a linear extensions of the "
            "2x2x2 product order (PR #8138): all 48 topological sorts share one "
            "recorded-set family, exactly the predecessor sets A_x; pattern has "
            "purchase and the step holds as written"
        )
    else:
        print(
            f"HIT: Q1a claims 48 linear extensions of the 2x2x2 product order "
            f"with unique recorded-set family equal to the predecessor sets; "
            f"enumeration gives n={n} families={len(families)} "
            f"predecessor_only={families == {expected}}"
        )
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on Q1a 2x2x2 linear extensions "
            f"(PR #8138): count={n} (stated 48), recorded-set families={len(families)}"
        )


if __name__ == "__main__":
    main()

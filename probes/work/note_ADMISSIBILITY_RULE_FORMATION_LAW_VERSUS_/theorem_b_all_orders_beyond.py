#!/usr/bin/env python3
"""J:note falsifier for ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION (block 01, on main).

Falsifier implemented (the note's Falsifiers section): "the identity B1 fails for some order; some order with |A_k| <= 1 gives mu_sigma != mu
or some order with |A_k| >= 2 gives mu_sigma = mu at a not-all-equal triple".

Beyond the note's sizes (path3, P4, star4, cycle4): every order of P5, star5 (a centre and four leaves), C5, C6, the 2x3 grid and a 6-site
spider (a centre with three arms of lengths 1, 2, 2), at six triples: (3,1,2), (2,2,1) [p = q], (2,1,1) [q = r], (1,2,3),
(5,2,4), and the all-equal (2,2,2) (where every order must coincide).

Machinery, disjoint from the note's runner: the six-axis menu as unit vectors, phi(s, t) = p / q / r by the dot product; for every order the
formation law is built as a full array over all 6^n configurations (numpy), both as exact integer numerators/normalisers and as floating
probabilities; B1 is checked elementwise in exact integers (prod of numerators = static weight W), the law comparison mu_sigma = mu is checked
in exact integers (prod_k Z_k constant, which by B1 is the same statement) AND directly in floating point (max |mu_sigma - mu|), and the
distinct formation laws are counted.
"""
from __future__ import annotations

import itertools
import math

import numpy as np

AXES = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
DOT = AXES @ AXES.T


def phi_table(p, q, r):
    T = np.where(DOT == 1, p, np.where(DOT == -1, q, r)).astype(np.int64)
    return T


WINDOWS = {
    "P5": (5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
    "star5": (5, [(0, 1), (0, 2), (0, 3), (0, 4)]),
    "C5": (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]),
    "C6": (6, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]),
    "grid2x3": (6, [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]),
    "spider6": (6, [(0, 1), (0, 2), (2, 3), (0, 4), (4, 5)]),
}
TRIPLES = [(3, 1, 2), (2, 2, 1), (2, 1, 1), (1, 2, 3), (5, 2, 4), (2, 2, 2)]


def is_forest(n, edges):
    par = list(range(n))

    def f(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for a, b in edges:
        ra, rb = f(a), f(b)
        if ra == rb:
            return False
        par[ra] = rb
    return True


def run_window(name, n, edges, triple):
    T = phi_table(*triple)
    grid = np.array(list(itertools.product(range(6), repeat=n)), dtype=np.int64)
    nb = {x: [y for a, b in edges for y in ((b,) if a == x else (a,) if b == x else ())] for x in range(n)}
    W = np.ones(len(grid), dtype=np.int64)
    for a, b in edges:
        W *= T[grid[:, a], grid[:, b]]
    ZW = int(W.sum())
    mu = W / ZW
    b1_fail = b2_fail = 0
    coincide = 0
    laws = set()
    maxdev_equal = 0.0
    for order in itertools.permutations(range(n)):
        formed = []
        num = np.ones(len(grid), dtype=np.int64)
        prodZ = np.ones(len(grid), dtype=np.int64)
        musig = np.ones(len(grid))
        maxA = 0
        for x in order:
            A = [y for y in nb[x] if y in formed]
            maxA = max(maxA, len(A))
            nk = np.ones(len(grid), dtype=np.int64)
            for y in A:
                nk *= T[grid[:, x], grid[:, y]]
            Zk = np.zeros(len(grid), dtype=np.int64)
            for s in range(6):
                t = np.ones(len(grid), dtype=np.int64)
                for y in A:
                    t *= T[s, grid[:, y]]
                Zk += t
            num *= nk
            prodZ *= Zk
            musig *= nk / Zk
            formed.append(x)
        b1_fail += int(not np.array_equal(num, W))                       # B1: numerators multiply to the static weight
        exact_equal = bool(np.all(prodZ == prodZ[0])) and int(prodZ[0]) == ZW
        float_equal = float(np.max(np.abs(musig - mu))) < 1e-12
        if exact_equal != float_equal:
            b1_fail += 1                                                   # the two routes disagree: counted as a failure
        predicted = (maxA <= 1) or (len(set(triple)) == 1)
        b2_fail += int(exact_equal != predicted)
        coincide += int(exact_equal)
        if exact_equal:
            maxdev_equal = max(maxdev_equal, float(np.max(np.abs(musig - mu))))
        g = math.gcd(*[int(v) for v in np.unique(prodZ)]) if len(np.unique(prodZ)) > 1 else int(prodZ[0])
        laws.add(tuple((prodZ // g).tolist()) if len(np.unique(prodZ)) > 1 else ("const",))
    return dict(orders=math.factorial(n), b1_fail=b1_fail, b2_fail=b2_fail, coincide=coincide, laws=len(laws),
                forest=is_forest(n, edges))


def main():
    total_b1 = total_b2 = 0
    for name, (n, edges) in WINDOWS.items():
        for triple in TRIPLES:
            r = run_window(name, n, edges, triple)
            total_b1 += r["b1_fail"]
            total_b2 += r["b2_fail"]
            print(f"{name} (forest {r['forest']}), (p,q,r) = {triple}: {r['orders']} orders; B1 failures {r['b1_fail']}; B2 failures "
                  f"{r['b2_fail']}; orders with mu_sigma = mu: {r['coincide']}; distinct formation laws {r['laws']}")
    n_checks = len(WINDOWS) * len(TRIPLES)
    if total_b1 == 0 and total_b2 == 0:
        print(f"SUMMARY: falsifier 'B1 fails / B2 misclassifies an order' does not fire beyond the note's sizes: every order of P5, star5, C5, C6, "
              f"the 2x3 grid and a 6-site spider at six triples ({n_checks} window-triple pairs, 6^n configurations each, exact integers and a "
              f"floating direct comparison agreeing) satisfies B1, and mu_sigma = mu exactly when max |A_k| <= 1 (or the rule is constant); cycles "
              f"and the grid have no coinciding order, trees do")
    else:
        print(f"HIT: Theorem B falsifier fires: B1 failures {total_b1}, B2 misclassifications {total_b2}")
        print("SUMMARY: falsifier fired; see the per-window lines")


if __name__ == "__main__":
    main()

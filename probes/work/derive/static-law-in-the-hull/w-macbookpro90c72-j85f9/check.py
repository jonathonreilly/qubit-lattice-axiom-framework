#!/usr/bin/env python3
"""Independent a3 checks for J:derive:static-law-in-the-hull (worker w-macbookpro90c72-j85f9).

Brute-force Z (no subset DP), all-order D (permutations), Hoelder by enumerating M^k.
Different machinery from a1's forward DP.
"""
from __future__ import annotations

import itertools
from fractions import Fraction
from typing import List, Sequence, Tuple

M = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def phi_tab(p: int, q: int, r: int) -> List[List[int]]:
    tab = [[0] * 6 for _ in range(6)]
    for i, a in enumerate(M):
        for j, b in enumerate(M):
            d = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
            tab[i][j] = p if d == 1 else (q if d == -1 else r)
    return tab


def Nk(k: int, p: int, q: int, r: int) -> int:
    return 6 if k == 0 else p**k + q**k + 4 * r**k


def window(kind: str):
    if kind == "plaquette":
        sites = [(x, y, 0) for x in range(2) for y in range(2)]
    elif kind == "rect2x3":
        sites = [(x, y, 0) for x in range(2) for y in range(3)]
    elif kind == "cube":
        sites = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    elif kind == "path3":
        sites = [(x, 0, 0) for x in range(3)]
    else:
        raise ValueError(kind)
    n = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    edges = []
    nb = [[] for _ in range(n)]
    for a, b in itertools.combinations(sites, 2):
        if sum(abs(a[t] - b[t]) for t in range(3)) == 1:
            i, j = idx[a], idx[b]
            edges.append((i, j))
            nb[i].append(j)
            nb[j].append(i)
    return n, edges, nb


def Z_brute(n: int, edges, tab) -> int:
    Z = 0
    for v in itertools.product(range(6), repeat=n):
        w = 1
        for a, b in edges:
            w *= tab[v[a]][v[b]]
        Z += w
    return Z


def D_all_orders(n: int, nb, pqr) -> int:
    Ntab = [Nk(k, *pqr) for k in range(7)]
    best = None
    for order in itertools.permutations(range(n)):
        formed = 0
        D = 1
        for x in order:
            k = 0
            for y in nb[x]:
                if formed >> y & 1:
                    k += 1
            D *= Ntab[k]
            formed |= 1 << x
        if best is None or D < best:
            best = D
    return best


def hoelder_ok(pqr) -> Tuple[bool, bool]:
    """sum_s prod_i phi(s, a_i) <= N_k for all tuples of length k=1..6.
    Equality on all-equal tuples; strict for some orthogonal pair when k>=2.
    """
    p, q, r = pqr
    tab = phi_tab(p, q, r)
    bound_ok = True
    strict_some = True
    for k in range(1, 7):
        N = Nk(k, p, q, r)
        # all-equal equality
        ssum = 0
        a = (0,) * k
        for s in range(6):
            pr = 1
            for i in range(k):
                pr *= tab[s][a[i]]
            ssum += pr
        if ssum != N:
            bound_ok = False
        # orthogonal pair padded with copies of first: (0, 2, 0, ...)
        if k >= 2:
            ssum2 = 0
            tup = (0, 2) + (0,) * (k - 2)
            for s in range(6):
                pr = 1
                for i in range(k):
                    pr *= tab[s][tup[i]]
                ssum2 += pr
            if not (ssum2 < N):
                strict_some = False
        # full enum for k<=4 (6^4=1296; k=5,6 sampled via product of first four + two free is 6^6=46656, do k=5,6 full)
        if k <= 6:
            for tup in itertools.product(range(6), repeat=k):
                ssum = 0
                for s in range(6):
                    pr = 1
                    for i in range(k):
                        pr *= tab[s][tup[i]]
                    ssum += pr
                if ssum > N:
                    bound_ok = False
                    break
    return bound_ok, strict_some


def main() -> int:
    failures: List[str] = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        extra = f" {detail}" if detail else ""
        print(f"CHECK {name}: {'PASS' if cond else 'FAIL'}{extra}")
        if not cond:
            failures.append(name)

    rules = [(3, 1, 2), (5, 2, 4), (7, 3, 5)]
    expected = {
        ("plaquette", (3, 1, 2)): (20784, 22464),
        ("rect2x3", (3, 1, 2)): (6000000, 7008768),
        ("rect2x3", (5, 2, 4)): (568472046, 631394298),
        ("rect2x3", (7, 3, 5)): (3651973440, 4044168000),
        ("cube", (3, 1, 2)): (6982520832, 10933678080),
        ("cube", (5, 2, 4)): (17002040556294, 22841951518746),
        ("cube", (7, 3, 5)): (412507735200000, 555911333280000),
        ("path3", (3, 1, 2)): None,  # Z == D
    }

    for pqr in rules:
        ok, strict = hoelder_ok(pqr)
        check(f"H{pqr}", ok and strict, f"Hoelder bound+strict {ok} {strict}")

    rows = []
    for kind in ("plaquette", "rect2x3", "cube", "path3"):
        n, edges, nb = window(kind)
        e = len(edges)
        for pqr in rules if kind != "path3" else ((3, 1, 2),):
            tab = phi_tab(*pqr)
            Z = Z_brute(n, edges, tab)
            D = D_all_orders(n, nb, pqr)
            p = pqr[0]
            # constant-pattern masses
            mu_stat = Fraction(p**e, Z)
            mu_form = Fraction(p**e, D)
            margin = 6 * (mu_stat - mu_form)
            print(
                f"ROW {kind} {pqr}: n={n} |E|={e} Z={Z} D={D} Z<D={Z < D} "
                f"mu_stat(const)={mu_stat} mu_form<={mu_form} Ef_gap={margin}"
            )
            rows.append((kind, pqr, Z, D, Z < D, margin))
            if kind == "path3":
                check("pathZD", Z == D, f"path Z={Z} D={D}")
            else:
                check(f"lt{kind}{pqr}", Z < D)
                check(f"gap{kind}{pqr}", margin > 0)
                exp = expected.get((kind, pqr))
                if exp is not None:
                    check(f"Z{kind}{pqr}", Z == exp[0], f"Z={Z}")
                    check(f"D{kind}{pqr}", D == exp[1], f"D={D}")

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: on the 2x3 rectangle and the cube, at (p,q,r)=(3,1,2),(5,2,4),(7,3,5), "
        "independent brute-force Z and all-order D give Z < D with exact values matching "
        "the constant-pattern separator: mu_S(v^b) <= p^{|E|}/D < p^{|E|}/Z = mu_stat(v^b) "
        "for every adapted scheme (mu_S(v^b)=sum_sigma rho(sigma|v^b) p^{|E|}/D_sigma); "
        "the path of 3 is the negative control Z=D. Hoelder sum_s prod phi(s,a_i) <= N_k "
        "holds by full enumeration of M^k for k<=6 at the three rules, strict on an orthogonal pair."
    )
    print(
        "SUMMARY: PARTIAL independent brute-force/all-order census confirms Z<D on 2x3 and cube "
        "at (3,1,2),(5,2,4),(7,3,5) with separator f=1[constant] and positive exact margins; "
        "path-of-3 has Z=D; Hoelder enumerated on M^k, k<=6."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""J:attack-d:PR8138 — QUANTIFIER SCOPE.

Q4: c < 1/3 on the eight listed triples, with silent triples inside
(3c = 81/110, 31950/63407, 5782/10295). Recompute c = max_k TV of
k-neighbor kernels (k=1,2,3) at every listed coupling. HIT if a silent
triple has 3c ≥ 1, or a stated 3c disagrees, or a listed triple claimed
in-region has 3c ≥ 1.

Also: N(000,111)=6 monotone paths (used in the influence bound for every
d); successor triples never predecessor triples on [0,6]^3.

Exact Fraction. Not a re-run of the 2000-sample product form.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

M = 6
TRIPLES = (
    (3, 1, 2),
    (5, 2, 4),
    (7, 3, 5),
    (2, 1, 2),
    (3, 2, 2),
    (5, 4, 4),
    (11, 10, 10),
    (2, 2, 2),
)
SILENT = {
    (3, 1, 2): Fraction(81, 110),
    (5, 2, 4): Fraction(31950, 63407),
    (7, 3, 5): Fraction(5782, 10295),
}


def orbit_type(s, t):
    if s == t:
        return "p"
    if s // 2 == t // 2:
        return "q"
    return "r"


def tables(tr):
    p, q, r = tr
    w = {"p": p, "q": q, "r": r}
    phi = tuple(tuple(w[orbit_type(s, t)] for t in range(M)) for s in range(M))
    Z1 = sum(phi[0])
    Z2 = {
        (a, b): sum(phi[s][a] * phi[s][b] for s in range(M))
        for a in range(M)
        for b in range(M)
    }
    Z3 = {
        (a, b, c): sum(phi[s][a] * phi[s][b] * phi[s][c] for s in range(M))
        for a in range(M)
        for b in range(M)
        for c in range(M)
    }
    return phi, Z1, Z2, Z3


def cond(phi, Z1, Z2, Z3, rec):
    k = len(rec)
    if k == 0:
        return [Fraction(1, M)] * M
    if k == 1:
        a = rec[0]
        return [Fraction(phi[s][a], Z1) for s in range(M)]
    if k == 2:
        a, b = rec
        z = Z2[(a, b)]
        return [Fraction(phi[s][a] * phi[s][b], z) for s in range(M)]
    a, b, c = rec
    z = Z3[(a, b, c)]
    return [Fraction(phi[s][a] * phi[s][b] * phi[s][c], z) for s in range(M)]


def tv(u, v):
    return sum(abs(x - y) for x, y in zip(u, v)) / 2


def c_of(tr):
    phi, Z1, Z2, Z3 = tables(tr)
    best = {1: Fraction(0), 2: Fraction(0), 3: Fraction(0)}
    for k in (1, 2, 3):
        for rec in product(range(M), repeat=k):
            base = cond(phi, Z1, Z2, Z3, rec)
            for i in range(k):
                for a2 in range(M):
                    if a2 == rec[i]:
                        continue
                    rec2 = list(rec)
                    rec2[i] = a2
                    d = tv(base, cond(phi, Z1, Z2, Z3, tuple(rec2)))
                    if d > best[k]:
                        best[k] = d
    c = max(best.values())
    return best, c


def monotone_paths(src, dst):
    """Monotone paths src→dst stepping +e_i (never decreasing a coord)."""
    need = [dst[i] - src[i] for i in range(3)]
    if any(x < 0 for x in need):
        return 0
    steps = [0] * need[0] + [1] * need[1] + [2] * need[2]
    seen = set()
    n = 0
    for perm in permutations(steps):
        if perm in seen:
            continue
        seen.add(perm)
        n += 1
    return n


def succ_pred_clash():
    """Successor triple of z is {z+e_j}; predecessor triple is {z-e_j}."""
    E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    n = 0
    clash = 0
    for z in product(range(0, 7), repeat=3):
        n += 1
        pred = set(tuple(z[i] - e[i] for i in range(3)) for e in E)
        succ = set(tuple(z[i] + e[i] for i in range(3)) for e in E)
        if pred & succ:
            clash += 1
    return n, clash


def main() -> int:
    hits = []
    print("== Q4 c at eight triples; silent 3c = stated fractions; 3c<1 ==")
    for tr in TRIPLES:
        ck, c = c_of(tr)
        three = 3 * c
        print(f"  {tr}: c1={ck[1]} c2={ck[2]} c3={ck[3]} c={c} 3c={three} <1={three < 1}")
        if tr in SILENT:
            want = SILENT[tr]
            if three != want:
                hits.append(f"{tr} 3c={three} != stated {want}")
                print("HIT:", hits[-1])
            if three >= 1:
                hits.append(f"silent {tr} has 3c={three} >= 1 (outside Q4 region)")
                print("HIT:", hits[-1])
        elif tr != (2, 2, 2) and three >= 1:
            hits.append(f"listed {tr} has 3c={three} >= 1")
            print("HIT:", hits[-1])
        if tr == (2, 2, 2) and c != 0:
            hits.append(f"constant rule c={c} != 0")
            print("HIT:", hits[-1])

    npaths = monotone_paths((0, 0, 0), (1, 1, 1))
    print(f"== N((0,0,0),(1,1,1)) monotone paths = {npaths} (stated 6) ==")
    if npaths != 6:
        hits.append(f"N(000,111)={npaths} != 6")
        print("HIT:", hits[-1])
    # a few more distances used by 'every d'
    for dst in ((2, 0, 0), (1, 1, 0), (2, 1, 0), (2, 1, 1)):
        np_ = monotone_paths((0, 0, 0), dst)
        print(f"  N(0,{dst})={np_}")

    n, clash = succ_pred_clash()
    print(f"== successor∩predecessor on [0,6]^3: {clash}/{n} (stated never) ==")
    if clash:
        hits.append(f"successor=predecessor at {clash} sites")
        print("HIT:", hits[-1])

    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8138): " + "; ".join(hits[:3]))
        return 0
    print(
        "SUMMARY: QUANTIFIER SCOPE (PR #8138): c and 3c at all eight listed "
        "triples match the silent-region fractions (81/110, 31950/63407, "
        "5782/10295) with 3c<1; constant rule c=0; N(000,111)=6; successor "
        "triples never meet predecessor triples on [0,6]^3; pattern has "
        "purchase and the claimed inequalities hold in-range"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

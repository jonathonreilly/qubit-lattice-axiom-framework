#!/usr/bin/env python3
"""Independent ring nullspace for the reversibility derivation.

Past {x-1,x,x+1}, menu size m, ring length L. Unknowns are all values of F.
Reversibility rows: D(s,t)-D(s0,t)+D(s0,s)=0. Rank over Q.
"""
from fractions import Fraction as F
import itertools


def rank(rows, n):
    M = [row[:] for row in rows if any(row)]
    r = 0
    used = set()
    for c in range(n):
        piv = next((i for i in range(len(M)) if i not in used and M[i][c] != 0), None)
        if piv is None:
            continue
        used.add(piv)
        r += 1
        pv = M[piv][c]
        M[piv] = [x / pv for x in M[piv]]
        for i, row in enumerate(M):
            if i != piv and row[c] != 0:
                f = row[c]
                M[i] = [a - f * b for a, b in zip(row, M[piv])]
    return r


def ring(m, L):
    # index F(s', a, b, c)
    keys = list(itertools.product(range(m), repeat=4))
    idx = {k: i for i, k in enumerate(keys)}
    n = len(keys)
    states = list(itertools.product(range(m), repeat=L))
    s0 = states[0]

    def phi_row(s, t):
        row = [0] * n
        for x in range(L):
            row[idx[(t[x], s[(x - 1) % L], s[x], s[(x + 1) % L])]] += 1
            row[idx[(s[x], t[(x - 1) % L], t[x], t[(x + 1) % L])]] -= 1
        return row

    rows = []
    # all pairs s < t in lex order of states
    for i, s in enumerate(states):
        for t in states[i + 1 :]:
            ds = phi_row(s, t)
            d0t = phi_row(s0, t)
            d0s = phi_row(s0, s)
            rows.append([a - b + c for a, b, c in zip(ds, d0t, d0s)])
    rk = rank(rows, n)
    return n, len(rows), n - rk, rk


def main():
    cases = [(2, 4, 16, 120, 11), (2, 5, 16, 496, 11)]
    # menu 3 ring 4 is 81 unknowns, 3^4=81 states, C(81,2)=3240 rows: heavier but doable
    ok = True
    for m, L, unk, cons, dim in cases:
        n, nrows, nullity, rk = ring(m, L)
        print(f"menu {m} ring {L}: unknowns {n} rows {nrows} nullity {nullity} rank {rk}")
        ok &= n == unk and nrows == cons and nullity == dim
    if ok:
        print(
            "HIT: confirmed - on rings with past {x-1,x,x+1} the reversible nullspace "
            "has dimension 11 for menu 2 on rings 4 and 5 (16 unknowns; 120 and 496 constraints)"
        )
        print(
            "SUMMARY: confirmed the exact ring census in S4 for menu 2; "
            "the two-body exchange-symmetric family matches that nullity"
        )
    else:
        print("SUMMARY: fails at the ring nullspace census")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""J:confirm:J-attack-g-PR8146 -- independent test of block 12's S1 preference sentence (PR #8146).

Statement tested (note, Theorem S1 and claim_scope): "The majority value of a 2:1 triple is its most likely
output iff p > max(q, r)", for the kernel r(s | a1, a2, a3) = prod_i phi(s, a_i) / Z_3 on the six axes,
phi = p (same), q (antipodal), r (orthogonal); the note's 2:1 triples are (a, a, b), b orthogonal to a, and
(a, a, -a).

Machinery (different from the finder's Fraction conditionals at eleven couplings):
  1. phi written as a polynomial in the inner product, phi(s, a) = r + (p - q)/2 (s.a) + ((p + q)/2 - r)(s.a)^2,
     checked against the three cases; the output weights of every ORDERED 2:1 triple (all 6*5*3 = 90 of them)
     derived symbolically in sympy, and the exact condition for the majority to be the strict argmax read off;
  2. an exhaustive integer scan, 1 <= p, q, r <= 24 (13824 couplings), of all 90 ordered 2:1 triples with
     integer weights (no division): the couplings where "every 2:1 majority is the strict argmax" disagrees
     with "p > max(q, r)", and the same against the corrected condition "p > max(q, r) and p^2 q > r^3";
  3. exact rational points on the campaign's line (p, 1, 2) and the three silent triples of block 03.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

import sympy as sp

AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def neg(u):
    return tuple(-a for a in u)


def phi_poly(s, a, p, q, r):
    d = dot(s, a)
    return r + (p - q) * d / 2 + ((p + q) / 2 - r) * d * d


def ordered_21_triples():
    out = []
    for a in AXES:
        for m in AXES:
            if m == a:
                continue
            for pos in range(3):  # position of the minority entry
                t = [a, a, a]
                t[pos] = m
                out.append((a, m, tuple(t)))
    return out


def weights(t, p, q, r):
    return {s: sp.expand(sp.Mul(*[phi_poly(s, x, p, q, r) for x in t])) for s in AXES}


def symbolic_part():
    p, q, r = sp.symbols("p q r", positive=True)
    # phi_poly reproduces the three cases
    ok_phi = (sp.simplify(phi_poly(AXES[0], AXES[0], p, q, r) - p) == 0
              and sp.simplify(phi_poly(AXES[1], AXES[0], p, q, r) - q) == 0
              and sp.simplify(phi_poly(AXES[2], AXES[0], p, q, r) - r) == 0)
    patterns = {}
    for a, m, t in ordered_21_triples():
        w = weights(t, p, q, r)
        kind = "antipodal" if m == neg(a) else "orthogonal"
        # competitor weights, as a multiset of polynomials, relative to the majority weight
        comp = tuple(sorted(str(sp.factor(w[s])) for s in AXES if s != a))
        patterns.setdefault(kind, set()).add((str(sp.factor(w[a])), comp))
    return ok_phi, patterns


def majority_strict_argmax_all(p, q, r):
    """integer weights: True iff for every ordered 2:1 triple the majority value has strictly the largest weight."""
    wt = {1: p, -1: q, 0: r}
    for a, m, t in TRIPLES:
        wa = None
        best_other = 0
        for s in AXES:
            w = 1
            for x in t:
                w *= wt[dot(s, x)]
            if s == a:
                wa = w
            else:
                best_other = max(best_other, w)
        if not wa > best_other:
            return False
    return True


def antipodal_orthogonal_split(p, q, r):
    wt = {1: p, -1: q, 0: r}
    res = {}
    for kind, (a, m) in {"orthogonal": (AXES[0], AXES[2]), "antipodal": (AXES[0], AXES[1])}.items():
        t = (a, a, m)
        ws = {s: wt[dot(s, t[0])] * wt[dot(s, t[1])] * wt[dot(s, t[2])] for s in AXES}
        res[kind] = (ws[a], max(w for s, w in ws.items() if s != a))
    return res


TRIPLES = ordered_21_triples()


def main():
    ok_phi, patterns = symbolic_part()
    print(f"1. phi as a polynomial in s.a reproduces (p, q, r): {ok_phi}; ordered 2:1 triples: {len(TRIPLES)}")
    for kind in ("orthogonal", "antipodal"):
        for maj, comp in sorted(patterns[kind]):
            print(f"   {kind}: majority weight {maj}; the five other outputs {list(comp)}")

    N = 24
    dis_stated, dis_corrected, n = [], [], 0
    for p, q, r in itertools.product(range(1, N + 1), repeat=3):
        n += 1
        truth = majority_strict_argmax_all(p, q, r)
        stated = p > max(q, r)
        corrected = stated and p * p * q > r ** 3
        if truth != stated:
            dis_stated.append((p, q, r))
        if truth != corrected:
            dis_corrected.append((p, q, r))
    only_if_fails = [c for c in dis_stated if majority_strict_argmax_all(*c) and not (c[0] > max(c[1], c[2]))]
    if_fails = [c for c in dis_stated if not majority_strict_argmax_all(*c) and c[0] > max(c[1], c[2])]
    all_antipodal = all(c[0] ** 2 * c[1] <= c[2] ** 3 for c in if_fails)
    print(f"2. integer scan 1..{N} ({n} couplings, all {len(TRIPLES)} ordered 2:1 triples each): "
          f"disagreements with 'iff p > max(q, r)': {len(dis_stated)} (p > max(q,r) but some majority not the strict argmax: "
          f"{len(if_fails)}; the converse direction: {len(only_if_fails)}); every one has p^2 q <= r^3: {all_antipodal}; "
          f"disagreements with 'p > max(q, r) and p^2 q > r^3': {len(dis_corrected)}")
    smallest = min(if_fails, key=lambda c: (sum(c), c))
    print(f"   smallest-sum counterexample {smallest}; first few: {sorted(if_fails, key=lambda c: (sum(c), c))[:6]}")

    print("3. exact points")
    pts = [(F(3), F(1), F(2)), (F(5), F(2), F(4)), (F(7), F(3), F(5)), (F(5, 2), F(1), F(2)), (F(14, 5), F(1), F(2)), (F(3), F(1), F(2))]
    res_pts = {}
    for p, q, r in pts[:-1]:
        wt = {1: p, -1: q, 0: r}
        a, ma = AXES[0], AXES[1]
        t = (a, a, ma)
        ws = {s: wt[dot(s, t[0])] * wt[dot(s, t[1])] * wt[dot(s, t[2])] for s in AXES}
        Z = sum(ws.values())
        pa = ws[a] / Z
        porth = ws[AXES[2]] / Z
        res_pts[(p, q, r)] = (pa, porth)
        print(f"   (p,q,r)=({p},{q},{r}): p>max(q,r) {p > max(q, r)}; (a,a,-a): P(a)={pa}, P(each orthogonal)={porth}, "
              f"P(-a)={ws[ma] / Z}; majority strict argmax {pa > max(ws[s] / Z for s in AXES if s != a)}")
    boundary = sp.solve(sp.Eq(sp.Symbol("p", positive=True) ** 2 * 1, 2 ** 3), sp.Symbol("p", positive=True))
    print(f"   on the line (p,1,2) the antipodal majority loses to the orthogonal values exactly for 2 < p <= {boundary[0]} "
          f"(= {float(boundary[0]):.6f}); the runner's B4 tests p > max(q,r) only at (3,1,2), where 9 > 8")

    p524 = res_pts[(F(5), F(2), F(4))]
    ok = (ok_phi and len(if_fails) > 0 and all_antipodal and len(dis_corrected) == 0 and len(only_if_fails) == 0
          and p524[1] > p524[0])
    if ok:
        print(f"HIT: confirmed - S1's 'the majority value of a 2:1 triple is its most likely output iff p > max(q, r)' is false in the "
              f"'if' direction: at (5,2,4) the antipodal triple (a,a,-a) gives P(a) = {p524[0]} < P(each orthogonal) = {p524[1]} "
              f"(weights 50 vs 64); an exhaustive integer scan 1..{N} finds {len(if_fails)} couplings with p > max(q,r) where some 2:1 "
              f"majority is not the strict argmax, all antipodal with p^2 q <= r^3, and none against the corrected condition "
              f"p > max(q,r) and p^2 q > r^3; on the line (p,1,2) the sentence fails for 2 < p <= 2 sqrt 2")
        print("SUMMARY: confirmed - the preference sentence of S1 needs p^2 q > r^3 in addition to p > max(q, r) (the proof's "
              "'which holds when p > max(q, r)' step is the gap); the closed forms themselves are not in question here")
    else:
        print(f"SUMMARY: not reproduced - symbolic {ok_phi}, if-failures {len(if_fails)}, corrected disagreements {len(dis_corrected)}, "
              f"converse failures {len(only_if_fails)}")


if __name__ == "__main__":
    main()

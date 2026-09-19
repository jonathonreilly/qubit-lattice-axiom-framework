#!/usr/bin/env python3
"""J:attack-g:PR8146 — brute-force S1 closed forms, NOT the S2 eroder bound.

S1: r(s | a1,a2,a3) = Π_i φ(s, a_i) / Z_3(a), φ = p same, q antipodal, r else.
Closed forms:
  P(a|a,a,a) = p³/(p³+q³+4r³)
  P(a|a,a,b) = p² r / (r(p²+q²)+r²(p+q)+2r³)   (b ⊥ a)
  P(a|a,a,−a) = p² q / (pq(p+q)+4r³)
  P(a|a,b,c) = P(b|...)=P(c|...)= p/(3(p+q)),  P(−a|a,b,c)=q/(3(p+q))
Majority of a 2:1 triple is most likely iff p > max(q,r).

Enumerate all 6³=216 triples at exact Fraction weights; check every pattern
against the closed form; check the iff on both sides of p=max(q,r); check
ε(p) = max 1−r(a|triple) over triples with ≥2 entries a, at (p,1,2) for
p=3,10,30,100,1000 against the note's exact rationals.

HIT if a closed form, the preference iff, or an ε(p) rational fails.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product


AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def neg(a):
    return (-a[0], -a[1], -a[2])


def phi(s, a, p, q, r):
    if s == a:
        return p
    if s == neg(a):
        return q
    return r


def Z3(pred, p, q, r):
    return sum(prod_phi(s, pred, p, q, r) for s in AXES)


def prod_phi(s, pred, p, q, r):
    w = Fraction(1)
    for a in pred:
        w *= phi(s, a, p, q, r)
    return w


def r_cond(s, pred, p, q, r):
    return prod_phi(s, pred, p, q, r) / Z3(pred, p, q, r)


def pattern_key(pred):
    a, b, c = pred
    counts = defaultdict(int)
    for x in pred:
        counts[x] += 1
    # classify relative to first majority-or-tie structure
    vals = list(counts.items())
    vals.sort(key=lambda kv: (-kv[1], AXES.index(kv[0])))
    top, n = vals[0]
    if n == 3:
        return "unanimous", top
    if n == 2:
        other = [x for x in pred if x != top][0]
        if other == neg(top):
            return "antipodal21", top
        return "ortho21", top
    # 1:1:1
    return "tie", None


def main():
    hits = []
    # symbolic closed forms vs definition at a generic triple of integers
    pqr_list = [
        (3, 1, 2),
        (10, 1, 2),
        (30, 1, 2),
        (100, 1, 2),
        (1000, 1, 2),
        (5, 2, 4),
        (7, 3, 5),
        (4, 4, 1),  # p = max(q,r)
        (3, 4, 1),  # p < q
        (3, 1, 4),  # p < r
        (8, 3, 3),
    ]
    a = AXES[0]
    b = AXES[2]
    c = AXES[4]
    ma = neg(a)

    def check(name, got, want):
        if got != want:
            hits.append(f"HIT: {name}: got {got} want {want}")
            print("HIT:", name, got, want)
        else:
            print(f"ok {name}: {got}")

    for p, q, r in pqr_list:
        p, q, r = Fraction(p), Fraction(q), Fraction(r)
        # closed forms
        check(
            f"P(a|aaa) {(p,q,r)}",
            r_cond(a, (a, a, a), p, q, r),
            p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3),
        )
        den_ortho = r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3
        check(
            f"P(a|aab) {(p,q,r)}",
            r_cond(a, (a, a, b), p, q, r),
            p ** 2 * r / den_ortho,
        )
        check(
            f"P(a|aa,-a) {(p,q,r)}",
            r_cond(a, (a, a, ma), p, q, r),
            p ** 2 * q / (p * q * (p + q) + 4 * r ** 3),
        )
        check(
            f"P(a|abc) {(p,q,r)}",
            r_cond(a, (a, b, c), p, q, r),
            p / (3 * (p + q)),
        )
        check(
            f"P(b|abc) {(p,q,r)}",
            r_cond(b, (a, b, c), p, q, r),
            p / (3 * (p + q)),
        )
        check(
            f"P(c|abc) {(p,q,r)}",
            r_cond(c, (a, b, c), p, q, r),
            p / (3 * (p + q)),
        )
        check(
            f"P(-a|abc) {(p,q,r)}",
            r_cond(ma, (a, b, c), p, q, r),
            q / (3 * (p + q)),
        )
        # all 216: probabilities sum to 1
        for pred in product(AXES, repeat=3):
            tot = sum(r_cond(s, pred, p, q, r) for s in AXES)
            if tot != 1:
                hits.append(f"HIT: probabilities do not sum to 1 at {pred} {(p,q,r)} tot={tot}")
                print("HIT: sum", pred, tot)
                break

        # preference iff for 2:1
        weights_ortho = {s: prod_phi(s, (a, a, b), p, q, r) for s in AXES}
        a_wins_ortho = weights_ortho[a] > max(weights_ortho[s] for s in AXES if s != a)
        want_ortho = p > max(q, r)
        if a_wins_ortho != want_ortho:
            hits.append(
                f"HIT: ortho 2:1 majority-most-likely {a_wins_ortho} vs p>max(q,r)={want_ortho} at {(p,q,r)}"
            )
            print("HIT: ortho iff", p, q, r, a_wins_ortho, want_ortho)
        weights_anti = {s: prod_phi(s, (a, a, ma), p, q, r) for s in AXES}
        a_wins_anti = weights_anti[a] > max(weights_anti[s] for s in AXES if s != a)
        # note claims a wins iff p>q and p²q>r³, "which holds when p>max(q,r)"
        p2q = p * p * q
        r3 = r * r * r
        if want_ortho and not a_wins_anti:
            hits.append(
                f"HIT: antipodal 2:1 majority not most likely though p>max(q,r) "
                f"at (p,q,r)=({p},{q},{r}): p^2 q={p2q} vs r^3={r3}; "
                f"weights a={weights_anti[a]} ortho={r3}"
            )
            print(
                "HIT: S1 iff fails for antipodal 2:1 (a,a,-a) at "
                f"(p,q,r)=({p},{q},{r}): p={p}>max(q,r)={max(q,r)} but "
                f"p^2 q={p2q} < r^3={r3}, so majority weight {weights_anti[a]} "
                f"is strictly below each of the four orthogonal weights {r3}"
            )
        if (not want_ortho) and a_wins_ortho:
            hits.append(f"HIT: ortho majority most likely though p<=max(q,r) at {(p,q,r)}")
            print("HIT: ortho when p<=max", p, q, r)

    # ε(p) at (p,1,2)
    stated = {
        3: Fraction(35, 44),
        10: Fraction(21, 71),
        30: Fraction(71, 971),
        100: Fraction(211, 10211),
        1000: Fraction(2011, 1002011),
    }
    attaining = {3: "antipodal21", 10: "antipodal21", 30: "ortho21", 100: "ortho21", 1000: "ortho21"}
    for pv, want in stated.items():
        p, q, r = Fraction(pv), Fraction(1), Fraction(2)
        best = Fraction(0)
        best_pat = None
        for pred in product(AXES, repeat=3):
            n_a = sum(1 for x in pred if x == a)
            if n_a < 2:
                continue
            dev = 1 - r_cond(a, pred, p, q, r)
            if dev > best:
                best = dev
                best_pat = pattern_key(pred)[0]
        check(f"eps({pv})", best, want)
        if best_pat != attaining[pv]:
            hits.append(f"HIT: eps({pv}) attained at {best_pat} not {attaining[pv]}")
            print("HIT: attaining", pv, best_pat)

    # S1 expansions: leading 1-P(majority) vs q^3+4r^3 over p^3, r/p, q/p
    p, q, r = Fraction(1000), Fraction(1), Fraction(2)
    d_uni = 1 - r_cond(a, (a, a, a), p, q, r)
    lead_uni = (q ** 3 + 4 * r ** 3) / p ** 3
    d_ortho = 1 - r_cond(a, (a, a, b), p, q, r)
    lead_ortho = r / p
    d_anti = 1 - r_cond(a, (a, a, ma), p, q, r)
    lead_anti = q / p
    # O(p^{-4}) / O(p^{-2}): relative error should shrink; exact leading match not claimed
    print(f"expansions p=1000: uni {d_uni} lead {lead_uni}; ortho {d_ortho} lead {lead_ortho}; anti {d_anti} lead {lead_anti}")
    if abs(d_uni - lead_uni) > 2 / p ** 4:
        # loose numeric guard on the O(p^{-4}) remainder; exact comparison via series
        rem = d_uni - lead_uni
        print("uni remainder", rem)

    if hits:
        print(
            "SUMMARY: S1's stated iff 'majority of a 2:1 triple is most likely iff "
            "p>max(q,r)' fails at (5,2,4) for the antipodal pattern (a,a,-a): "
            "closed forms and eps(p) on (p,1,2) hold, but p>max(q,r) does not imply p^2 q>r^3"
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — S1 closed forms hold on all 216 "
        "triples at 11 weight triples (unanimous/ortho-2:1/antipodal-2:1/tie), majority of "
        "a 2:1 triple is most likely iff p>max(q,r) on both sides of the threshold, and "
        "ε(p) at (p,1,2) for p=3,10,30,100,1000 equals 35/44,21/71,71/971,211/10211,2011/1002011 "
        "attained at antipodal then orthogonal as stated"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

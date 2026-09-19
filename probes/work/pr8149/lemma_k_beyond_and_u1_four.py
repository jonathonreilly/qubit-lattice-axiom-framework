#!/usr/bin/env python3
"""J:falsifier:PR8149 — B2 normalizer lemma beyond k<=6, and U1/B1
reconstruction beyond three sites.

Not the known U2/U4 216-env HIT.

Falsifiers: 'a k<=6 at which the Lemma's closed form fails (B2)';
'a positive three-site law not recovered from its conditionals (B1)'.
Machinery disjoint from the runner (no Rule class, no star 6^7 pass):
integer φ, K=φ/Z1 as Fraction, K_k = Σ_s Π K. Beyond the note: Lemma at
k=7..12 and extra triples; Brook–Besag reconstruction on four sites
(6^4) from one-site conditionals of a non-product positive law.
HIT if a closed form disagrees or reconstruction fails.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

VALS = (0, 1, 2, 3, 4, 5)  # 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def orbit(s, t):
    if s == t:
        return "p"
    if s // 2 == t // 2:
        return "q"
    return "r"


def tables(p, q, r):
    w = {"p": p, "q": q, "r": r}
    phi = [[w[orbit(s, t)] for t in range(6)] for s in range(6)]
    Z1 = p + q + 4 * r
    K = [[F(phi[s][a], Z1) for s in range(6)] for a in range(6)]
    return Z1, K


def Kk(K, rec):
    tot = F(0)
    for s in range(6):
        pr = F(1)
        for a in rec:
            pr *= K[a][s]
        tot += pr
    return tot


def lemma_anti(p, q, r, k):
    Z1, K = tables(p, q, r)
    b, mb = 0, 1  # +x, -x
    rec_same = (b,) * k
    rec_anti = (mb,) + (b,) * (k - 1)
    lhs = Kk(K, rec_same) - Kk(K, rec_anti)
    rhs = ((p - q) / Z1) * ((p / Z1) ** (k - 1) - (q / Z1) ** (k - 1))
    return lhs, rhs


def lemma_orth(p, q, r, k):
    Z1, K = tables(p, q, r)
    b, c = 0, 2  # +x, +y
    rec_same = (b,) * k
    rec_orth = (c,) + (b,) * (k - 1)
    lhs = Kk(K, rec_same) - Kk(K, rec_orth)
    rhs = (
        (p - r) * (p ** (k - 1) - r ** (k - 1))
        + (q - r) * (q ** (k - 1) - r ** (k - 1))
    ) / Z1 ** k
    return lhs, rhs


def check_lemma() -> None:
    print("== B2 Lemma closed form beyond k=2..6 ==")
    triples = [(3, 1, 2), (5, 2, 4), (2, 1, 2), (2, 2, 1), (7, 3, 5), (4, 4, 1)]
    for tr in triples:
        p, q, r = (F(x) for x in tr)
        for k in range(2, 13):
            la, ra = lemma_anti(p, q, r, k)
            lo, ro = lemma_orth(p, q, r, k)
            if k in (2, 6, 7, 12) or tr == (3, 1, 2) and k <= 3:
                print(f"  {tr} k={k}: anti {la} vs {ra}; orth {lo} vs {ro}")
            if la != ra:
                hit(f"Lemma anti at {tr} k={k}: {la} != {ra}")
            if lo != ro:
                hit(f"Lemma orth at {tr} k={k}: {lo} != {ro}")
            # nonzero iff as stated
            if p != q and la == 0:
                hit(f"Lemma anti vanishes at nonconstant p≠q {tr} k={k}")
            if len({p, q, r}) > 1 and lo == 0:
                hit(f"Lemma orth vanishes at nonconstant {tr} k={k}")
            if p == q == r and (la != 0 or lo != 0):
                hit(f"Lemma nonzero at constant rule {tr} k={k}")


def reconstruct_four() -> None:
    """U1/B1 beyond three sites: a positive law on 6^4 configs, not a
    product of φ, recovered from one-site conditionals via Brook–Besag."""
    print("== U1 reconstruction on four sites (beyond executed three) ==")
    # weights: integer, strictly positive, not a product kernel
    # w(a,b,c,d) = 1 + a + 2*b + 3*c + 5*d + a*d  (sites in 0..5)
    sites = 4

    def wgt(v):
        a, b, c, d = v
        return 1 + a + 2 * b + 3 * c + 5 * d + a * d

    Z = 0
    law = {}
    for v in product(range(6), repeat=sites):
        ww = wgt(v)
        law[v] = ww
        Z += ww
    # one-site conditionals
    def cond(x, rest):
        # rest is the 4-tuple with x's slot to fill
        nums = []
        for s in range(6):
            vv = list(rest)
            vv[x] = s
            nums.append(law[tuple(vv)])
        tot = sum(nums)
        return [F(n, tot) for n in nums]

    # reconstruct from vacuum 0000 along a,b,c,d
    vac = (0, 0, 0, 0)
    rec = {}
    for v in product(range(6), repeat=sites):
        ratio = F(1)
        for i in range(sites):
            wprev = list(v[:i]) + list(vac[i:])
            wnext = list(v[: i + 1]) + list(vac[i + 1 :])
            if wprev[i] == wnext[i]:
                continue
            ctab = cond(i, tuple(wprev))
            ratio *= ctab[wnext[i]] / ctab[wprev[i]]
        rec[v] = ratio

    # rec[v] = μ(v)/μ(vac); recover probabilities
    # μ(vac) = 1 / Σ rec
    srec = sum(rec.values())
    n_off = 0
    for v, ww in law.items():
        got = rec[v] / srec
        want = F(ww, Z)
        if got != want:
            n_off += 1
            if n_off <= 2:
                hit(f"U1 four-site reconstruct {v}: {got} != {want}")
    print(f"  6^4={len(law)} configs, mismatches={n_off}, Z={Z}")
    if n_off == 0:
        print("  Brook–Besag recovers the four-site law exactly")


def main() -> int:
    check_lemma()
    reconstruct_four()
    if HITS:
        print("SUMMARY: FALSIFIER (PR #8149): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: FALSIFIER (PR #8149): B2 Lemma anti/orth closed forms hold "
        "for k=2..12 at six triples including beyond executed k<=6; U1 "
        "Brook–Besag reconstructs a non-product positive law on all 6^4 "
        "four-site configs (beyond executed three sites); not the 216-env "
        "HIT; falsifier does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

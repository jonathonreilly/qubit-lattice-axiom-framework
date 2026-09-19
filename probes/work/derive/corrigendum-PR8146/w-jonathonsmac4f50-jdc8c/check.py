#!/usr/bin/env python3
"""Corrigendum packet for PR #8146 (block 12, S1's majority-preference clause): the checks behind ATTEMPT.md.

Objects (block 12's note at 3acd27d2): the six-axis menu {+-e1, +-e2, +-e3}, the covariant product rule
r(s | u, v, w) proportional to phi(s, u) phi(s, v) phi(s, w) with phi = p (equal), q (antipodal), r (orthogonal), p, q, r > 0.
S1's clause: 'The majority value of a 2:1 triple is its most likely output iff p > max(q, r).'

 A1  the output weights of the two 2:1 patterns: (a, a, b): p^2 r (a), q^2 r (-a), p r^2 (b), q r^2 (-b), r^3 (each of +-c);
     (a, a, -a): p^2 q (a), p q^2 (-a), r^3 (each of the four orthogonal values); against a direct evaluation of the rule
 A2  the corrected statement: the majority of (a, a, b) is the strict argmax iff p > max(q, r); of (a, a, -a) iff p > q and p^2 q > r^3,
     equivalently p > P*(q, r) := max(q, sqrt(r^3/q)); both 2:1 patterns iff p > P*(q, r); P* = max(q, r) iff q >= r
     (exact: symbolic reductions, and the direct argmax against the condition on every integer triple in {1..24}^3 and on a rational grid)
 A3  the original's failure set: q < r and r < p <= sqrt(r^3/q); the witness (5, 2, 4): P(a | a,a,-a) = 25/163 < 32/163 = P(c | a,a,-a)
     for each of the four orthogonal c; the count of integer triples in {1..24}^3 where the original's 'iff' fails
 A4  the four campaign lines: (p,1,2) band (2, 2 sqrt 2], (p,1,1) none, (p,2,4) (4, 4 sqrt 2], (p,1,3) (3, 3 sqrt 3]; block 12's executed
     couplings p = 3, 10, 30, 100, 1000 on (p, 1, 2) lie outside the band; the runner's B4 test points (3,1,2), (2,1,3), (1,2,1), (2,2,1)
     get the same verdict under the original and the corrected condition (B4 cannot see the defect)
 A5  what does not use the clause: the deviations' expansions (q^3 + 4r^3)/p^3, r/p, q/p (S1), S3's epsilon (a maximum of deviations),
     S6's epsilon(p) = max(q, r)/p + O(p^-2) (symbolic)
"""
import itertools
import math
import sys
import time
from fractions import Fraction as F

import sympy as sp

FAILS = []
T0 = time.time()


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi(s, u, w):
    p, q, r = w
    d = sum(a * b for a, b in zip(s, u))
    return p if d == 1 else (q if d == -1 else r)


def weights(tr, w):
    return {s: phi(s, tr[0], w) * phi(s, tr[1], w) * phi(s, tr[2], w) for s in AX}


def majority_strict_argmax(tr, w):
    W = weights(tr, w)
    a = tr[0]
    return all(W[a] > W[s] for s in AX if s != a)


def main():
    a, b, c = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    ma = (-1, 0, 0)
    p, q, r = sp.symbols("p q r", positive=True)
    # A1
    Wab = weights((a, a, b), (p, q, r))
    Wam = weights((a, a, ma), (p, q, r))
    ok1 = (Wab[a] == p ** 2 * r and Wab[ma] == q ** 2 * r and Wab[b] == p * r ** 2 and Wab[(0, -1, 0)] == q * r ** 2
           and Wab[c] == r ** 3 and Wab[(0, 0, -1)] == r ** 3)
    ok1 &= Wam[a] == p ** 2 * q and Wam[ma] == p * q ** 2 and all(Wam[s] == r ** 3 for s in (b, (0, -1, 0), c, (0, 0, -1)))
    ok1 &= sp.simplify(Wam[a] / sum(Wam.values()) - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)) == 0
    ok1 &= sp.simplify(Wab[a] / sum(Wab.values()) - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)) == 0
    check("A1", ok1, "the six output weights of (a, a, b) are p^2 r, q^2 r, p r^2, q r^2, r^3, r^3 and of (a, a, -a) are p^2 q, p q^2 and r^3 (x4), "
          "reproducing S1's closed forms p^2 r/(r(p^2+q^2) + r^2(p+q) + 2r^3) and p^2 q/(pq(p+q) + 4r^3)")

    # A2: the corrected statement, symbolic reductions + exhaustive integer grid + rational grid
    red = []
    red.append(sp.factor(Wab[a] - Wab[ma]) == r * (p - q) * (p + q))
    red.append(sp.factor(Wab[a] - Wab[b]) == p * r * (p - r))
    red.append(sp.factor(Wab[a] - Wab[c]) == r * (p - r) * (p + r))
    red.append(sp.factor(Wam[a] - Wam[ma]) == p * q * (p - q))
    ok2 = all(red)

    def Pstar_gt(pp, qq, rr):          # p > max(q, sqrt(r^3/q)), exactly: p > q and p^2 q > r^3
        return pp > qq and pp * pp * qq > rr ** 3

    def orth_ok(pp, qq, rr):
        return pp > max(qq, rr)
    n_bad_orth = n_bad_anti = n_bad_both = 0
    fail_orig = 0
    for pp, qq, rr in itertools.product(range(1, 25), repeat=3):
        o = majority_strict_argmax((a, a, b), (pp, qq, rr))
        m = majority_strict_argmax((a, a, ma), (pp, qq, rr))
        n_bad_orth += (o != orth_ok(pp, qq, rr))
        n_bad_anti += (m != Pstar_gt(pp, qq, rr))
        n_bad_both += ((o and m) != Pstar_gt(pp, qq, rr))
        fail_orig += ((o and m) != (pp > max(qq, rr)))
    rat_ok = True
    grid = [F(k, 4) for k in range(1, 41)]
    for pp in grid:
        for qq in (F(1, 2), F(1), F(2), F(3)):
            for rr in (F(1, 2), F(1), F(2), F(4)):
                rat_ok &= (majority_strict_argmax((a, a, b), (pp, qq, rr)) and majority_strict_argmax((a, a, ma), (pp, qq, rr))) == Pstar_gt(pp, qq, rr)
    # P* = max(q, r) iff q >= r
    ok2 &= n_bad_orth == 0 and n_bad_anti == 0 and n_bad_both == 0 and rat_ok
    check("A2", ok2, "orthogonal 2:1: W(a) - W(-a) = r(p - q)(p + q), W(a) - W(b) = pr(p - r), W(a) - W(c) = r(p - r)(p + r) (and W(a) > W(-b) = q r^2 "
          "follows), so strict argmax iff p > max(q, r); antipodal 2:1: W(a) - W(-a) = pq(p - q), W(a) - W(c) = p^2 q - r^3, so strict argmax iff "
          "p > q and p^2 q > r^3, i.e. p > P* = max(q, sqrt(r^3/q)); every 2:1 triple iff p > P* (p^2 q > r^3 with p > q forces p > r); direct "
          "argmax = condition on all 13824 integer triples in {1..24}^3 (0 mismatches for each pattern and for both) and on a 640-point rational grid")
    # A3
    w = (5, 2, 4)
    Wm = weights((a, a, ma), w)
    Z = sum(Wm.values())
    ok3 = F(Wm[a], Z) == F(25, 163) and all(F(Wm[s], Z) == F(32, 163) for s in (b, (0, -1, 0), c, (0, 0, -1))) and 5 > max(2, 4)
    ok3 &= majority_strict_argmax((a, a, b), w) and not majority_strict_argmax((a, a, ma), w)
    check("A3", ok3, f"the original's failure set is q < r and r < p <= sqrt(r^3/q); witness (5, 2, 4): p = 5 > max(q, r) = 4 but "
          f"P(a | a,a,-a) = 25/163 < P(c | a,a,-a) = 32/163 for each of the four orthogonal c (the orthogonal pattern's majority is the argmax); "
          f"on the integer box {{1..24}}^3 the original 'iff' fails for {fail_orig} of 13824 triples")
    # A4
    lines = {(1, 2): None, (1, 1): None, (2, 4): None, (1, 3): None}
    txt = []
    ok4 = True
    for (qq, rr) in lines:
        lo = max(qq, rr)
        hi = max(qq, math.sqrt(rr ** 3 / qq))
        band = (lo, hi) if hi > lo else None
        # exact endpoints: p^2 q = r^3 at p = sqrt(r^3/q)
        txt.append(f"(p,{qq},{rr}): " + (f"({lo}, sqrt({F(rr ** 3, qq)})] = ({lo}, {hi:.4f}]" if band else "no band"))
        if band:
            mid = F(round((lo + hi) / 2 * 1000), 1000)
            ok4 &= majority_strict_argmax((a, a, b), (mid, qq, rr)) and not majority_strict_argmax((a, a, ma), (mid, qq, rr))
    ok4 &= all(Pstar_gt(pp, 1, 2) for pp in (3, 10, 30, 100, 1000)) and all(pp * pp > 8 for pp in (3, 10, 30, 100, 1000))
    b4 = [(3, 1, 2), (2, 1, 3), (1, 2, 1), (2, 2, 1)]
    ok4 &= all((pp > max(qq, rr)) == Pstar_gt(pp, qq, rr) for pp, qq, rr in b4)
    check("A4", ok4, "failure bands on the campaign's lines: " + "; ".join(txt) + " (a point inside each band checked exactly); block 12's executed "
          "couplings p = 3, 10, 30, 100, 1000 on (p, 1, 2) satisfy p^2 > 8 (outside the band); the runner's B4 points (3,1,2), (2,1,3), (1,2,1), "
          "(2,2,1) get the same verdict under the original and the corrected condition, so B4 passes under either")
    # A5: what does not use the clause
    eps = sp.Symbol("epsilon", positive=True)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    s1 = sp.series(d1.subs(p, 1 / eps), eps, 0, 4).removeO()
    s2 = sp.series(d2.subs(p, 1 / eps), eps, 0, 2).removeO()
    s3 = sp.series(d3.subs(p, 1 / eps), eps, 0, 2).removeO()
    ok5 = sp.simplify(s1 - (q ** 3 + 4 * r ** 3) * eps ** 3) == 0 and sp.simplify(s2 - q * eps) == 0 and sp.simplify(s3 - r * eps) == 0
    check("A5", ok5, "the parts of S1, S3 and S6 that do not use the clause: deviations (q^3 + 4r^3)/p^3, q/p (antipodal), r/p (orthogonal) to leading "
          "order (series in 1/p), hence S3's epsilon = max of the deviations and S6's epsilon(p) = max(q, r)/p + O(p^-2), unaffected")
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("corrigendum for PR #8146: S1's last clause is corrected to 'the majority value of every 2:1 triple is its strictly most likely output "
            "iff p > max(q, sqrt(r^3/q))' (orthogonal pattern iff p > max(q, r), antipodal iff p > q and p^2 q > r^3); the original holds for every p "
            "exactly when q >= r and fails for q < r on r < p <= sqrt(r^3/q) (witness (5,2,4): 25/163 < 32/163; " + str(fail_orig) + " of 13824 "
            "integer triples in {1..24}^3; bands (2, 2 sqrt 2] on (p,1,2), (4, 4 sqrt 2] on (p,2,4), (3, 3 sqrt 3] on (p,1,3), none on (p,1,1)); "
            "block 12's executed couplings, S3's epsilon, S6's asymptotics and the later blocks (25, 30: closed forms and coupling only) are "
            "unaffected; the uses needing repair are block 12's claim_scope, S1 statement and proof, B4, the steelman and the falsifier lines")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S6; finite facts CHECKED here) " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())

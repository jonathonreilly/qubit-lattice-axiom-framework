#!/usr/bin/env python3
# checks/nd1b_hnorm.py -- POST-HOC probe for check nd1 (T55-P, NQ_DEF.md).
# Run AFTER nd1_qrow.py's result was seen.  Labelled post-hoc under brief rule 3; it carries no
# pre-registered verdict and nothing in NQ_DEF.md sec.D1-D2 depends on it.
#
# Purpose: nd1 measured ||h|| = 8/3 at (L,d) = (3,4).  Theorem NQ-1's constant is claimed for general
# (L odd >= 3, d >= 2) as q0 = 1 + d(L+1)/(2L), which rests on ||h|| = d(L^2-1)/(4L) for general (L,d)
# and on ||Q_str|| = L.  This probe tests both formulas away from L = 3, so that the L-dependence of q0
# is not an L = 3 artefact.  Exact integer/Fraction arithmetic, plain python, no numpy, no BLAS, no lock.

from fractions import Fraction
from itertools import permutations, product
import sys

def e(D, mu):
    v = [0]*D; v[mu] = 1; return tuple(v)

def axial_path(start, end, sigma):
    cur = list(start); out = []
    for c in sigma:
        while cur[c] < end[c]:
            out.append(((tuple(cur), c), 1)); cur[c] += 1
        while cur[c] > end[c]:
            cur[c] -= 1; out.append(((tuple(cur), c), -1))
    return out

def h_norm(L, D):
    half = (L-1)//2
    block = [tuple(v) for v in product(range(-half, half+1), repeat=D)]
    orders = list(permutations(range(D)))
    w = Fraction(1, len(orders)*(L**D))
    row = {}
    origin = tuple([0]*D)
    for sigma in orders:
        for y in block:
            for link, s in axial_path(origin, y, sigma):
                row[link] = row.get(link, 0) + w*s
    return sum(abs(v) for v in row.values()), len([v for v in row.values() if v != 0])

def qstr_norm(L, D, mu=0):
    half = (L-1)//2
    block = [tuple(v) for v in product(range(-half, half+1), repeat=D)]
    w = Fraction(1, L**D)
    row = {}
    for y in block:
        for j in range(L):
            p = tuple(a + j*b for a, b in zip(y, e(D, mu)))
            row[(p, mu)] = row.get((p, mu), 0) + w
    return sum(abs(v) for v in row.values())

def main():
    lines = []
    def say(s):
        lines.append(s); print(s)
    say("POST-HOC probe nd1b: ||h|| =? d(L^2-1)/(4L)  and  ||Q_str|| =? L,  away from L = 3.")
    say("")
    say("   L   d   ||h|| measured   d(L^2-1)/(4L)   match   ||Q_str||   L   match   q0 = 1+d(L+1)/(2L)")
    ok = True
    for (L, D) in [(3,2), (3,3), (3,4), (5,2), (5,3), (5,4), (7,3), (7,4), (9,3)]:
        hv, nnz = h_norm(L, D)
        pred = Fraction(D*(L*L-1), 4*L)
        qs = qstr_norm(L, D)
        q0 = 1 + Fraction(D*(L+1), 2*L)
        m1 = (hv == pred); m2 = (qs == L)
        ok &= m1 and m2
        say("  %2d  %2d   %-13s   %-13s   %-5s   %-9s  %2d   %-5s   %s = %.4f"
            % (L, D, str(hv), str(pred), m1, str(qs), L, m2, str(q0), float(q0)))
    say("")
    say("ALL FORMULAS MATCH: %s" % ok)
    say("")
    say("Designed-FAIL control for this probe: the predicted value with (L+1) in place of (L^2-1),")
    say("i.e. d(L+1)/(4L), which must NOT match for any L > 1.")
    bad = 0
    for (L, D) in [(3,4), (5,4), (7,4)]:
        hv, _ = h_norm(L, D)
        wrong = Fraction(D*(L+1), 4*L)
        if hv != wrong:
            bad += 1
        say("   L=%d d=%d: measured %s vs wrong-formula %s -> %s" % (L, D, hv, wrong,
            "differs (control fires)" if hv != wrong else "AGREES -> control did not fire"))
    say("control fired in %d of 3 cases" % bad)
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()

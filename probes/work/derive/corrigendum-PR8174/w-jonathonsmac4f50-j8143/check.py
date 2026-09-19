#!/usr/bin/env python3
"""Corrigendum packet for PR #8174 (block 30, T1(a) 'd_1 <= max(d_2, d_3)'): the checks behind ATTEMPT.md.

Objects (block 30 at cc7662e1): six-axis menu, product rule phi = p, q, r (equal, antipodal, orthogonal), K(s | a1, a2, a3) proportional to
prod phi(s, a_j); d_1 = 1 - K(a|a,a,a), d_2 = 1 - K(a|a,a,-a), d_3 = 1 - K(a|a,a,b); the two-level automaton eta' with eps_1 = d_1 and
amplification noise eps_2.
 A1  closed forms of d_1, d_2, d_3 against the conditional computed from the menu (symbolic and at weight triples)
 A2  exact signs: d_2 - d_1 = p^2 (p - q)(p q^2 + q^3 + 4 r^3)/[(p^3 + q^3 + 4 r^3)(p^2 q + p q^2 + 4 r^3)];
     d_3 - d_1 = p^2 g/[(p^3 + q^3 + 4 r^3)(p^2 + p r + q^2 + q r + 2 r^2)], g = p^2 r + p q^2 + p q r + 2 p r^2 - q^3 - 4 r^3;
     so d_1 <= d_2 iff p >= q, d_1 <= d_3 iff g >= 0, and d_1 <= max(d_2, d_3) iff p >= q or g >= 0
 A3  the original's failure: (1, 2, 1): d_1 = 12/13 > max(d_2, d_3) = 9/10 (and g = -3 < 0: the proof's d_1 <= d_3 fails too); 127 failing integer
     triples in {1..7}^3, 194 in {1..8}^3, all with q > p; a reachable state of T1(b)'s coupling at (1, 2, 1) where the site-wise inequality fails
 A4  the corrected statement: with eps_2* = max(d_1, d_2, d_3) every predecessor triple with at least two entries a dissents with probability
     <= eps_2* and the all-a triple with probability d_1 = eps_1 (all 216 triples, at the counterexamples and at the certificate points)
 A5  every weight point used by blocks 30-33 (the four lines at their certificates and floors) has p >= q, so eps_2* = max(d_2, d_3) there
"""
import itertools
import sys
from fractions import Fraction as F

import sympy as sp

FAILS = []


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi(i, j, w):
    d = sum(x * y for x, y in zip(AX[i], AX[j]))
    return w[0] if d == 1 else (w[1] if d == -1 else w[2])


def K(s, trip, w):
    ws = [phi(v, trip[0], w) * phi(v, trip[1], w) * phi(v, trip[2], w) for v in range(6)]
    return F(ws[s]) / sum(ws) if not isinstance(ws[0], sp.Basic) else ws[s] / sum(ws)


def dev(w):
    a, ma, b = 0, 1, 2
    return 1 - K(a, (a, a, a), w), 1 - K(a, (a, a, ma), w), 1 - K(a, (a, a, b), w)


def main():
    p, q, r = sp.symbols("p q r", positive=True)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    # A1
    sd = dev((p, q, r))
    ok = all(sp.simplify(x - y) == 0 for x, y in zip(sd, (d1, d2, d3)))
    for w in ((1, 2, 1), (5, 2, 4), (3, 1, 2)):
        ok &= tuple(dev(w)) == tuple(sp.Rational(x.subs({p: w[0], q: w[1], r: w[2]})) for x in (d1, d2, d3))
    check("A1", ok, "d_1, d_2, d_3 = 1 - K(a | a,a,a), 1 - K(a | a,a,-a), 1 - K(a | a,a,b) equal block 30's closed forms (symbolic, and exactly at (1,2,1), (5,2,4), (3,1,2))")
    # A2
    g = p ** 2 * r + p * q ** 2 + p * q * r + 2 * p * r ** 2 - q ** 3 - 4 * r ** 3
    e21 = sp.simplify(d2 - d1 - p ** 2 * (p - q) * (p * q ** 2 + q ** 3 + 4 * r ** 3) / ((p ** 3 + q ** 3 + 4 * r ** 3) * (p ** 2 * q + p * q ** 2 + 4 * r ** 3)))
    e31 = sp.simplify(d3 - d1 - p ** 2 * g / ((p ** 3 + q ** 3 + 4 * r ** 3) * (p ** 2 + p * r + q ** 2 + q * r + 2 * r ** 2)))
    check("A2", e21 == 0 and e31 == 0, "d_2 - d_1 = p^2 (p - q)(pq^2 + q^3 + 4r^3)/[(p^3+q^3+4r^3)(p^2 q+pq^2+4r^3)] and d_3 - d_1 = p^2 g/[(p^3+q^3+4r^3)(p^2+pr+q^2+qr+2r^2)] "
          "with g = p^2 r + pq^2 + pqr + 2pr^2 - q^3 - 4r^3 (exact identities; denominators positive): d_1 <= d_2 iff p >= q; d_1 <= d_3 iff g >= 0; "
          "d_1 <= max(d_2, d_3) iff p >= q or g >= 0")
    # A3
    D = dev((1, 2, 1))
    gv = g.subs({p: 1, q: 2, r: 1})
    ok = D == (F(12, 13), F(4, 5), F(9, 10)) and gv == -3
    counts = {}
    allq = True
    for N in (7, 8):
        bad = [(P, Q, R) for P in range(1, N + 1) for Q in range(1, N + 1) for R in range(1, N + 1) if dev((P, Q, R))[0] > max(dev((P, Q, R))[1:])]
        counts[N] = len(bad)
        allq &= all(Q > P for P, Q, R in bad)
        # the exact characterization reproduces the census
        ok &= all((dev((P, Q, R))[0] > max(dev((P, Q, R))[1:])) == (P < Q and g.subs({p: P, q: Q, r: R}) < 0)
                  for P in range(1, N + 1) for Q in range(1, N + 1) for R in range(1, N + 1))
    ok &= counts == {7: 127, 8: 194} and allq
    # reachable failure of T1(b)'s site-wise inequality at (1,2,1): an eta'-one at y with xi_y = 0 exists with positive probability (eta' amplifies
    # with eps_2 = max(d_2, d_3) = 9/10 where xi's predecessors are (a, a, -a), dissenting only with d_2 = 4/5); a successor x of y whose other two
    # predecessors are a in both processes then has P(xi_x = 1) = d_1 = 12/13 > P(eta'_x = 1) = 9/10: no monotone coupling at x
    eps2 = max(D[1:])
    ok &= D[1] < eps2 and D[0] > eps2
    check("A3", ok, f"(1, 2, 1): d_1 = 12/13 > max(d_2, d_3) = max(4/5, 9/10) = 9/10, and g = {gv} < 0 (so the proof's 'd_1 <= d_3' also fails); failing "
          f"integer triples: {counts[7]} in {{1..7}}^3, {counts[8]} in {{1..8}}^3, all with q > p, exactly the set p < q and g < 0; T1(b)'s coupling "
          f"reaches (with positive probability) an eta'-one y with xi_y = 0 (amplification {eps2} against xi's dissent {D[1]} at (a,a,-a)), after "
          f"which a successor with both other predecessors a needs P(xi = 1) = 12/13 <= P(eta' = 1) = 9/10, false")
    # A4: the corrected eps_2
    ok = True
    pts = [(1, 2, 1), (1, 3, 1), (2, 5, 2), (5, 2, 4), (4165, 1, 2), (2085, 1, 1), (8330, 2, 4), (6247, 1, 3)]
    for w in pts:
        e1, e2s = dev(w)[0], max(dev(w))
        for trip in itertools.product(range(6), repeat=3):
            na = sum(1 for v in trip if v == 0)
            dv = 1 - K(0, trip, w)
            if na == 3:
                ok &= dv == e1
            elif na == 2:
                ok &= dv <= e2s
    check("A4", ok, "with eps_2* = max(d_1, d_2, d_3): at every weight point tested (the counterexamples (1,2,1), (1,3,1), (2,5,2), and (5,2,4) and the four "
          "certificate points), every one of the 216 predecessor triples with exactly two entries a dissents with probability <= eps_2* and the all-a "
          "triple with d_1 = eps_1; the triples with at least two a's are (a,a,a), (a,a,-a), (a,a,b) up to the rule's symmetry, so T1(b)'s coupling "
          "holds for every positive weight triple with eps_2 := max(d_1, d_2, d_3)")
    # A5: the weights used by blocks 30-33
    used = [(4165, 1, 2), (2085, 1, 1), (8330, 2, 4), (6247, 1, 3), (4150, 1, 2), (453, 1, 2), (368, 1, 2), (2921, 1, 2), (1464, 1, 1), (5841, 2, 4),
            (4380, 1, 3), (405, 1, 2), (11, 1, 2)]
    ok = all(P >= Q for P, Q, R in used) and all(dev(w)[0] <= max(dev(w)[1:]) for w in used)
    check("A5", ok, "every weight point used by blocks 30-33 (certificates 4165/2085/8330/6247, ceiling 4150, stakes 453/368, block 33's 2921/1464/5841/4380/405, "
          "and (11, 1, 2)) has p >= q, hence d_1 <= d_2 <= max(d_2, d_3) = max(d_1, d_2, d_3): the four lines' results are unaffected; on the whole "
          "lines (p, 1, 1), (p, 1, 2), (p, 1, 3) for p >= 1 and (p, 2, 4) for p >= 2 the same holds by A2")
    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("corrigendum for PR #8174: T1(a) 'd_1 <= max(d_2, d_3)' holds exactly on {p >= q} U {g >= 0}, g = p^2 r + pq^2 + pqr + 2pr^2 - q^3 - 4r^3 "
            "(d_2 - d_1 has the sign of p - q, d_3 - d_1 that of g); it fails at (1,2,1) (12/13 > 9/10) and on 127 of {1..7}^3, all with q > p; T1(b)'s "
            "coupling is repaired for every positive weight triple by eps_2 := max(d_1, d_2, d_3), which equals max(d_2, d_3) whenever p >= q; every weight "
            "point of blocks 30-33 has p >= q, so their certificates, ceilings and stakes are unaffected; the lines to change are block 30's T1 "
            "statement, proof, eps_2 definitions and runner B2")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S5; finite facts CHECKED here) " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())

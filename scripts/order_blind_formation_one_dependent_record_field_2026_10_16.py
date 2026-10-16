#!/usr/bin/env python3
"""Order-blind positive formation: consistent marginals, static = formation, 1-dependence.

Exhibit rule: the soldered 48-point chiral-pair rule of the 2026-09-22
order-blind note, r(a|N) = r0(a) prod_d (1 + kappa X_d(a) X_{-d}(b_d)) with
X_d(a) = chi(a) when a.d = 3 and 0 otherwise, r0 uniform, kappa = 1/2.
Each point of the 48-point alphabet has exactly one coordinate equal to +-3,
so X depends only on the class (axis direction of that coordinate, chirality);
the twelve classes of four points each carry mass 1/12. All checks are exact.
"""

from __future__ import annotations

import sys
from fractions import Fraction as Fr
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    'docs/ORDER_BLIND_POSITIVE_FORMATION_IS_A_ONE_DEPENDENT_GIBBS_FIELD_BOUNDED_THEOREM_NOTE_2026-10-16.md',
)

DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
KAPPA = Fr(1, 2)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def neg(d):
    return tuple(-x for x in d)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


# ---- the 48-point alphabet and its class compression (independent rebuild) ----
def proper_cubic():
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                   - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                   + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
            if det == 1:
                out.append(M)
    return out


def mv(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


O = proper_cubic()
A24 = sorted({mv(M, (1, 2, 3)) for M in O})
A48 = sorted(set(A24) | {mv(M, (1, 2, -3)) for M in O})
CHI = {a: (1 if a in set(A24) else -1) for a in A48}


def X(d, a):
    return CHI[a] if sum(x * y for x, y in zip(a, d)) == 3 else 0


def cls(a):
    d = next(dd for dd in DIRS if sum(x * y for x, y in zip(a, dd)) == 3)
    return (d, CHI[a])


CLASSES = sorted({cls(a) for a in A48})
R0 = {k: Fr(sum(1 for a in A48 if cls(a) == k), 48) for k in CLASSES}


def Xc(d, k):
    return k[1] if k[0] == d else 0


def phi(d, a, b):
    """Bond factor for site value a with a neighbour at direction d holding b."""
    return 1 + KAPPA * Xc(d, a) * Xc(neg(d), b)


def rule(a, N):
    p = R0[a]
    for d, b in N.items():
        p *= phi(d, a, b)
    return p


def edges(sites):
    S = set(sites)
    return [(s, add(s, d), d) for s in sites for d in DIRS if add(s, d) in S and d in DIRS[0::2]]


def product_form(sites, cfg):
    val = dict(zip(sites, cfg))
    p = Fr(1)
    for s in sites:
        p *= R0[val[s]]
    for s, t, d in edges(sites):
        p *= phi(d, val[s], val[t])
    return p


def finished_law(sites, order):
    law = {}
    for cfg in product(CLASSES, repeat=len(sites)):
        val = dict(zip(sites, cfg))
        formed = {}
        p = Fr(1)
        for s in order:
            N = {d: formed[add(s, d)] for d in DIRS if add(s, d) in formed}
            p *= rule(val[s], N)
            formed[s] = val[s]
        law[cfg] = p
    return law


def marginal(sites, law, keep):
    idx = [sites.index(k) for k in keep]
    out = {}
    for cfg, p in law.items():
        key = tuple(cfg[i] for i in idx)
        out[key] = out.get(key, 0) + p
    return out


def main() -> int:
    ck = Checks()
    ck.check('48-point alphabet = two proper orbits of 24; twelve classes of four points',
             len(A48) == 48 and len(CLASSES) == 12 and all(v == Fr(1, 12) for v in R0.values()))
    ck.check('X depends only on the class', all(X(d, a) == Xc(d, cls(a)) for d in DIRS for a in A48))
    # normalisation on every neighbour condition (Theorem 2 identity, recomputed)
    # the rule depends on a neighbour b at direction d only through X_{-d}(b) in {-1,0,1},
    # and an absent neighbour acts as X = 0, so 3^6 representative conditions are exhaustive
    def rep(d, x):
        return next(b for b in CLASSES if Xc(neg(d), b) == x)
    ck.check('each value x in {-1,0,1} of X_{-d} is realised by some class (representatives exist)',
             all(any(Xc(neg(d), b) == x for b in CLASSES) for d in DIRS for x in (-1, 0, 1)))
    norm_ok = all(sum(rule(a, {d: rep(d, x) for d, x in zip(DIRS, xs)}) for a in CLASSES) == 1
                  for xs in product((-1, 0, 1), repeat=6))
    ck.check('rule normalised on every neighbour condition (all 3^6 X-patterns)', norm_ok)
    ck.check('rule strictly positive', all(rule(a, {d: b for d in DIRS}) > 0 for a in CLASSES for b in CLASSES))
    ck.check('bond symmetry phi_d(a,b) = phi_{-d}(b,a)',
             all(phi(d, a, b) == phi(neg(d), b, a) for d in DIRS for a in CLASSES for b in CLASSES))

    # Theorem 1: finished law = product form on every window and order (plaquette, all 24 orders)
    PLAQ = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    laws = [finished_law(PLAQ, list(o)) for o in permutations(PLAQ)]
    pf = {cfg: product_form(PLAQ, cfg) for cfg in product(CLASSES, repeat=4)}
    ck.check('plaquette: every one of the 24 formation orders gives the product-form law', all(L == pf for L in laws))
    ck.check('plaquette: total mass 1', sum(pf.values()) == 1)

    # Theorem 1 (consistency): marginal of a window law is the law of the subwindow
    m12 = marginal(PLAQ, pf, [PLAQ[0], PLAQ[1]])
    ck.check('plaquette marginal on an edge = two-site product form',
             all(m12[k] == product_form([PLAQ[0], PLAQ[1]], k) for k in m12))
    m13 = marginal(PLAQ, pf, [PLAQ[0], PLAQ[2]])
    ck.check('plaquette marginal on the diagonal = r0 x r0 (independent although joined by two paths)',
             all(m13[(a, b)] == R0[a] * R0[b] for a in CLASSES for b in CLASSES))

    # Theorem 2: static reading = formation reading (full conditional equals the rule)
    cond_ok = True
    for cfg, p in pf.items():
        rest = sum(pf[(a,) + cfg[1:]] for a in CLASSES)
        N = {(1, 0, 0): cfg[1], (0, 1, 0): cfg[3]}
        if p / rest != rule(cfg[0], N):
            cond_ok = False
            break
    ck.check('plaquette: conditional of a site given the other three records equals the rule', cond_ok)

    # Theorem 3: joint 1-dependence of sets with no edge between them (5-site path)
    P5 = [(0, 0, z) for z in range(5)]
    L5 = finished_law(P5, [P5[2], P5[0], P5[4], P5[1], P5[3]])
    pf5 = {cfg: product_form(P5, cfg) for cfg in product(CLASSES, repeat=5)}
    ck.check('5-site path: finished law (middle-first order) = product form', L5 == pf5)
    mAB = marginal(P5, pf5, [P5[0], P5[1], P5[3], P5[4]])
    mA = marginal(P5, pf5, [P5[0], P5[1]])
    mB = marginal(P5, pf5, [P5[3], P5[4]])
    ck.check('5-site path: law of {0,1} u {3,4} = law({0,1}) x law({3,4}) (edge-disjoint sets independent)',
             all(mAB[k] == mA[k[:2]] * mB[k[2:]] for k in mAB))
    pair = marginal(P5, pf5, [P5[0], P5[1]])
    ck.check('edge-joined pair is genuinely correlated (rule varies)',
             any(pair[(a, b)] != R0[a] * R0[b] for a in CLASSES for b in CLASSES))

    # Corollary: two-point function and structure factor of X_z
    def E(law, sites, f):
        return sum(p * f(dict(zip(sites, c))) for c, p in law.items())
    ez, mz = (0, 0, 1), (0, 0, -1)
    C0 = E(pf5, P5, lambda v: Xc(ez, v[P5[0]]) ** 2) - E(pf5, P5, lambda v: Xc(ez, v[P5[0]])) ** 2
    C1 = E(pf5, P5, lambda v: Xc(ez, v[P5[0]]) * Xc(mz, v[P5[1]]))
    C2 = E(pf5, P5, lambda v: Xc(ez, v[P5[0]]) * Xc(mz, v[P5[2]]))
    C3 = E(pf5, P5, lambda v: Xc(ez, v[P5[0]]) * Xc(mz, v[P5[3]]))
    ck.check('<X_z X_-z> on a z-bond = kappa/36 = 1/72', C1 == KAPPA / 36)
    ck.check('<X_z X_-z> at distance 2 and 3 vanish exactly', C2 == 0 and C3 == 0)
    ck.check('single-site variance of X_z = 1/6', C0 == Fr(1, 6))
    print(f'structure factor along z: S(q) = {C0} + 2*({C1}) cos q   (a degree-one trigonometric polynomial)')

    print(f"TOTAL: PASS={ck.passed} FAIL={ck.failed}")
    return 0 if ck.failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

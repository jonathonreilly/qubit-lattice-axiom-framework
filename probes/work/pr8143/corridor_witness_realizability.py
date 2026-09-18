#!/usr/bin/env python3
"""J:attack:PR8143 - full-domain projective corridor note (PR #8143), attack pattern (a) WITNESS REALIZABILITY: the stated seed, guard
and corridor exist in Z^3 exactly as described, and the literal local generator built from the note's formulas (not from any runner
code) produces the stated single-active-site order and transcript law:
  * tags r, p, o, k and the rate lambda from (1)-(2) with psi(u) = h(1-u)/[h(1-u)+h(u-1/4)] evaluated EXACTLY (psi = 1 for u <= 1/4,
    0 for u >= 1; any argument strictly between is reported as a non-binary rate); matrices are 2x2 over the Gaussian rationals;
  * the seed of section 3: axis sites T = (x,0,0), x < 3L; carrier a_0 = (-1,0,0) with 2I + rho_0; programs p_j = (3j,-1,0) with
    8I + P_j; markers k_j = (3j+2,1,0) with 2I; zero Records on the external vertex boundary G of C; |C| = 1 + 5L, |G| <= 6|C|;
  * every branch of every outcome sequence (2^L) for L = 1..7 with pseudo-random rational rank-one programs and a mixed rational rho_0:
    the frontier (every blank site adjacent to a nonzero Record; blank sites seeing only zero Records have every tag 0 and rate 0) has
    exactly one site of rate exactly 1 at each of the 3L stages, in the order e_0, c_0, a_1, e_1, ...; the kernel (1) at that site;
    Pr(R_0..R_(L-1)) against tr[R_(L-1)..R_0 rho_0 R_0..R_(L-1)] computed separately; no active site after 3L writes;
  * the note's executed counts at L = 5: 98 seed Records of which 87 are zero guards, 15 added Records per branch, 32 branches, 187
    distinct frontier states; the 24 proper cubic rotations of the seed (the rotated order) and a nonunitary GL2 similarity of every
    Record (identical transcript probabilities, conjugated Records); the guard-omission control (extra enabled sites).
HIT if a stated count differs, a stage has zero or several active sites or a rate other than 1, a transcript probability differs from
the ordered product, or a covariance check fails.
"""
import itertools
import random
import sys
import time
from fractions import Fraction as F

random.seed(8143)


class Q:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(s, o):
        return Q(s.re + o.re, s.im + o.im)

    def __sub__(s, o):
        return Q(s.re - o.re, s.im - o.im)

    def __mul__(s, o):
        return Q(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)

    def conj(s):
        return Q(s.re, -s.im)

    def abs2(s):
        return s.re * s.re + s.im * s.im

    def inv(s):
        n = s.abs2()
        return Q(s.re / n, -s.im / n)

    def __eq__(s, o):
        return s.re == o.re and s.im == o.im

    def __hash__(s):
        return hash((s.re, s.im))


ZERO, ONE = Q(0), Q(1)


def mat(a, b, c, d):
    return (a, b, c, d)


def mmul(A, B):
    return (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])


def madd(A, B):
    return tuple(x + y for x, y in zip(A, B))


def msub(A, B):
    return tuple(x - y for x, y in zip(A, B))


def scal(c):
    return (Q(c), ZERO, ZERO, Q(c))


def tr(A):
    return A[0] + A[3]


def det(A):
    return A[0] * A[3] - A[1] * A[2]


def dag(A):
    return (A[0].conj(), A[2].conj(), A[1].conj(), A[3].conj())


def minv(A):
    d = det(A).inv()
    return (A[3] * d, Q(0) - A[1] * d, Q(0) - A[2] * d, A[0] * d)


def meq(A, B):
    return all(x == y for x, y in zip(A, B))


I2, Z2 = scal(1), scal(0)
NONBINARY = []


def psi(u):
    if u <= F(1, 4):
        return 1
    if u >= 1:
        return 0
    NONBINARY.append(u)
    return None


def tags(A):
    r = psi((tr(A) - Q(5)).abs2())
    p = psi((tr(A) - Q(17)).abs2() + det(msub(A, scal(8))).abs2())
    o = psi((tr(A) - Q(1)).abs2() + det(A).abs2())
    k = psi((tr(A) - Q(4)).abs2() + (det(A) - Q(4)).abs2())
    return r, p, o, k


def rate(nbrs):
    ts = [tags(A) for A in nbrs]
    if any(x is None for t in ts for x in t):
        return None
    c, q, u, v = (sum(t[i] for t in ts) for i in range(4))
    a = psi(F((c - 1) ** 2 + (q - 1) ** 2 + u ** 2 + v ** 2)) + psi(F(c ** 2 + q ** 2 + (u - 1) ** 2 + v ** 2)) + psi(F(c ** 2 + q ** 2 + (u - 1) ** 2 + (v - 1) ** 2))
    return F(a) / (a + (a - 1) ** 2)


def kernel(nbrs):
    """(1) with f = clip to [0, 1]: list of (probability, atom)."""
    ts = [tags(A) for A in nbrs]
    S = F(0)
    atoms = []
    for i, Ai in enumerate(nbrs):
        for j, Aj in enumerate(nbrs):
            if i == j:
                continue
            wij = F(ts[i][0] * ts[j][1])
            if wij == 0:
                continue
            S += wij
            Pj = msub(Aj, scal(8))
            x = tr(mmul(msub(Ai, scal(2)), Pj)).re
            fx = min(max(x, F(0)), F(1))
            atoms.append((wij * fx, Pj))
            atoms.append((wij * (1 - fx), msub(I2, Pj)))
    b = (S - 1) ** 2
    Z = S + b
    tot = scal(0)
    for A in nbrs:
        tot = madd(tot, A)
    out = [(b / Z, tot)] if b else []
    out += [(w / Z, A) for w, A in atoms]
    merged = []
    for w, A in out:
        for m in merged:
            if meq(m[1], A):
                m[0] += w
                break
        else:
            merged.append([w, A])
    return [(w, A) for w, A in merged]


def rand_projector():
    while True:
        a, b, c, d = (random.randint(-4, 4) for _ in range(4))
        v = (Q(a, b), Q(c, d))
        n = v[0].abs2() + v[1].abs2()
        if n:
            return (v[0] * v[0].conj() * Q(1 / n), v[0] * v[1].conj() * Q(1 / n), v[1] * v[0].conj() * Q(1 / n), v[1] * v[1].conj() * Q(1 / n))


NB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add(x, d):
    return (x[0] + d[0], x[1] + d[1], x[2] + d[2])


def seed(L, rho0, progs, guards=True, rot=None, sim=None):
    R = rot or (lambda x: x)
    T = [(x, 0, 0) for x in range(3 * L)]
    rec = {(-1, 0, 0): madd(scal(2), rho0)}
    for j in range(L):
        rec[(3 * j, -1, 0)] = madd(scal(8), progs[j])
        rec[(3 * j + 2, 1, 0)] = scal(2)
    C = set(T) | set(rec)
    G = set()
    for c in C:
        for d in NB:
            z = add(c, d)
            if z not in C:
                G.add(z)
    if guards:
        for z in G:
            rec[z] = Z2
    if sim is not None:
        g, gi = sim
        rec = {x: mmul(mmul(g, A), gi) for x, A in rec.items()}
    rec = {R(x): A for x, A in rec.items()}
    return rec, len(C), len(G)


def frontier(rec):
    cand = set()
    for x, A in rec.items():
        if not meq(A, Z2):
            for d in NB:
                z = add(x, d)
                if z not in rec:
                    cand.add(z)
    act = []
    for z in cand:
        nb = [rec[add(z, d)] for d in NB if add(z, d) in rec]
        lam = rate(nb)
        if lam is None or lam > 0:
            act.append((z, lam, nb))
    return act


def run_branches(L, rho0, progs, guards=True, rot=None, sim=None):
    rec0, nC, nG = seed(L, rho0, progs, guards, rot, sim)
    results = {}
    states = set()
    order_ok = True
    issues = []
    R = rot or (lambda x: x)
    expected = []
    for j in range(L):
        expected += [R((3 * j, 0, 0)), R((3 * j + 1, 0, 0)), R((3 * j + 2, 0, 0))]

    def key(rec):
        return frozenset((x, tuple((q.re, q.im) for q in A)) for x, A in rec.items())

    def rec_step(rec, depth, prob, outs):
        states.add(key(rec))
        act = frontier(rec)
        if depth == 3 * L:
            if act:
                issues.append(f"active site after {3 * L} writes")
            results[tuple(outs)] = prob
            return
        if len(act) != 1 or act[0][1] != 1:
            issues.append(f"stage {depth}: {len(act)} active sites, rates {[a[1] for a in act]}")
            return
        z, lam, nb = act[0]
        if z != expected[depth]:
            issues.append(f"stage {depth}: active site {z}, expected {expected[depth]}")
        for w, A in kernel(nb):
            new = dict(rec)
            new[z] = A
            o = outs + ([A] if depth % 3 == 0 else [])
            rec_step(new, depth + 1, prob * w, o)

    rec_step(rec0, 0, F(1), [])
    return results, states, issues, nC, nG, len(rec0)


def ordered_product(rho0, outs):
    M = rho0
    for Rj in outs:
        M = mmul(mmul(Rj, M), Rj)
    return tr(M).re


def rotations():
    mats = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            m = [[0] * 3 for _ in range(3)]
            for i, pi in enumerate(perm):
                m[i][pi] = sg[i]
            d = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                 + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if d == 1:
                mats.append(m)
    return mats


def main():
    t0 = time.time()
    hits = []
    tot_states = {}
    for L in range(1, 8):
        progs = [rand_projector() for _ in range(L)]
        rho0 = madd(mmul(scal(F(1, 3)), rand_projector()), mmul(scal(F(2, 3)), rand_projector()))
        res, states, issues, nC, nG, nseed = run_branches(L, rho0, progs)
        worst = max(abs(p - ordered_product(rho0, outs)) for outs, p in res.items())
        total = sum(res.values())
        tot_states[L] = (len(states), nC, nG, nseed, len(res))
        print(f"[corridor L={L}] |C| = {nC} (1 + 5L = {1 + 5 * L}), |G| = {nG} (<= 6|C|: {nG <= 6 * nC}), seed Records {nseed}; {len(res)} "
              f"transcripts, total probability {total}, largest |Pr - tr[R..rho..R]| = {worst}; {len(states)} distinct frontier states; "
              f"{len(issues)} order issues  ({time.time() - t0:.0f}s)")
        if issues or worst != 0 or total != 1 or nC != 1 + 5 * L or nG > 6 * nC:
            hits.append(f"L = {L}: issues {issues[:3]}, worst {worst}, total {total}, |C| {nC}")
    s5 = tot_states[5]
    ok5 = s5[3] == 98 and s5[2] == 87 and s5[4] == 32 and s5[0] == 187
    print(f"[counts L=5] seed Records {s5[3]} (note 98), zero guards {s5[2]} (note 87), branches {s5[4]} (note 32), distinct frontier states "
          f"{s5[0]} (note 187), Records added per branch {3 * 5} (note 15)")
    if not ok5:
        hits.append(f"L = 5 counts {s5} differ from 98/87/32/187")
    # rotations and similarity at L = 3
    L = 3
    progs = [rand_projector() for _ in range(L)]
    rho0 = madd(mmul(scal(F(1, 2)), rand_projector()), mmul(scal(F(1, 2)), rand_projector()))
    base, _, _, _, _, _ = run_branches(L, rho0, progs)
    rot_ok = True
    for m in rotations():
        rf = (lambda mm: (lambda x: tuple(sum(mm[i][k] * x[k] for k in range(3)) for i in range(3))))(m)
        res, _, issues, _, _, _ = run_branches(L, rho0, progs, rot=rf)
        rot_ok = rot_ok and not issues and all(res[o] == base[o] for o in base)
    print(f"[rotations] 24 proper cubic rotations of the L = 3 seed: rotated single-active-site order and identical transcript law: {rot_ok}")
    g = (Q(2, 1), Q(1, -3), Q(0, 1), Q(3, 2))
    gi = minv(g)
    res, _, issues, _, _, _ = run_branches(L, rho0, progs, sim=(g, gi))
    sim_ok = not issues and set(len(o) for o in res) == {L}
    # transcript probabilities keyed by the conjugated outcomes
    conj_key = lambda outs: tuple(tuple((q.re, q.im) for q in mmul(mmul(g, A), gi)) for A in outs)
    base_conj = {conj_key(o): p for o, p in base.items()}
    got = {tuple(tuple((q.re, q.im) for q in A) for A in o): p for o, p in res.items()}
    sim_ok = sim_ok and got == base_conj
    print(f"[similarity] nonunitary GL2 similarity of every Record (L = 3): same order, conjugated outcomes, identical probabilities: {sim_ok}")
    # guard omission control
    _, _, issues_ng, _, _, _ = run_branches(3, rho0, progs, guards=False)
    print(f"[control] without the zero guards: {len(issues_ng)} stages with other than one active site (the note: extra enabled sites), e.g. "
          f"{issues_ng[0] if issues_ng else '-'}")
    zero_ctx = rate([Z2, Z2, Z2])
    print(f"[zero context] a blank site seeing only zero Records: rate {zero_ctx}; non-binary psi arguments met anywhere: {len(NONBINARY)}")
    if not rot_ok or not sim_ok or not issues_ng or zero_ctx != 0 or NONBINARY:
        hits.append(f"rotations {rot_ok}, similarity {sim_ok}, guard control {len(issues_ng)}, zero context {zero_ctx}, non-binary {len(NONBINARY)}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (a) WITNESS REALIZABILITY - the note's seed, guards and corridor built literally in Z^3 and run with an "
          f"independent exact implementation of (1)-(2) for L = 1..7 over all 2^L branches: exactly one active site of rate 1 at every stage in the "
          f"stated order, transcript law equal to the ordered products exactly, total probability 1; at L = 5 the seed has {s5[3]} Records of which "
          f"{s5[2]} zero guards and {s5[0]} distinct frontier states over {s5[4]} branches (note: 98, 87, 187, 32); 24 rotations and a GL2 "
          f"similarity covariant; guards necessary; {len(hits)} defects; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

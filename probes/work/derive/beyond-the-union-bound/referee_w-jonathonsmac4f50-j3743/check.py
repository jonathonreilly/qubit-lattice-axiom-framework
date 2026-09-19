#!/usr/bin/env python3
"""Referee of J:derive:beyond-the-union-bound:a2 (author w-macbookpro90c72-ja988, grok-4.6); referee w-jonathonsmac4f50-j3743
(claude-opus-5). Independent code (Fractions, sympy); nothing from the author's check.py. Disclosure: this referee's model family
wrote another attempt on this problem (w-jonathonsmac4f50-jae8a, the history-count certificates the attempt mentions); a2 takes a
different route and does not build on it.

Block 30's dominating automaton eta' in level time on Z^3: predecessors z - e_j; a site with N 1-predecessors is 1 with
probability 1 (N >= 2), eps_2 (N = 1), eps_1 (N = 0), independently given the previous level; forks are e_i - e_j.

G1  on (p,1,2): d1 = 33/(p^3+33), d2 = (p+32)/(p^2+p+32), d3 = (2p+11)/(p^2+2p+11) from the six-axis kernel directly;
    d2 - d3 = p^2(21-p)/[(p^2+p+32)(p^2+2p+11)]; p = 11: d2 = 43/164 > d3 = 3/14
G2  the three predecessors of a site are pairwise forks, so P(N >= 2) <= 3r
G3  isolated pair u, v = u + e1 - e2: one common successor w = u + e1 = v + e2, four one-parent children, all four fork-adjacent to
    w, three child-child forks among the four: seven fork pairs among the five children
G4  given the pair (children only): P(some child pair both 1) = 1 - (1 - eps2)^4, E[# child pairs both 1] = 4 eps2 + 3 eps2^2
    (sympy over the 16 amplification patterns); < 1 iff eps2 < (-2+sqrt7)/3; on (p,1,2) first at p = 13 (d2(12) = 11/47,
    d2(13) = 45/214)
G5  scope: w has two more fork neighbours with no parent in {u, v}, which are 1 with probability eps1; counting every next-level
    fork pair that contains a child (23 pairs), the mean is 1.0469 at p = 13 and 0.9241 at p = 14, so for the full pair count
    the first integer below 1 is p = 14
G6  step 5: the 5-predecessor atom sum's r-coefficient A_r (configurations containing a fork pair, weighted by f(N_u) f(N_v)) is
    > 10 at p = 200, 84, 13, 11 and tends to 10 = #{N_u >= 2, N_v >= 2} as eps -> 0
G7  eps = 0 on the depth-2 cone: each of the 9 base fork pairs gives exactly one mid-level 1 and a top 0; 32 of the 64 base masks
    force the top
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import sympy as sp

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
FORKS = [tuple(E[a][i] - E[b][i] for i in range(3)) for a in range(3) for b in range(3) if a != b]
add = lambda x, y: tuple(a + b for a, b in zip(x, y))
sub = lambda x, y: tuple(a - b for a, b in zip(x, y))
fork = lambda x, y: sub(y, x) in FORKS
M = range(6)


def kernel_dev(p, trip):
    W = [[p if a == b else (1 if b == (a ^ 1) else 2) for b in M] for a in M]
    ws = [W[s][trip[0]] * W[s][trip[1]] * W[s][trip[2]] for s in M]
    return 1 - F(ws[0], sum(ws))


def d1(p):
    return F(33, p ** 3 + 33)


def d2(p):
    return F(p + 32, p * p + p + 32)


def d3(p):
    return F(2 * p + 11, p * p + 2 * p + 11)


def main():
    ok = all(kernel_dev(p, (0, 0, 0)) == d1(p) and kernel_dev(p, (0, 0, 1)) == d2(p) and kernel_dev(p, (0, 0, 2)) == d3(p)
             for p in (3, 5, 11, 13, 84, 200))
    ps = sp.symbols("p", positive=True)
    D2 = (ps + 32) / (ps ** 2 + ps + 32)
    D3 = (2 * ps + 11) / (ps ** 2 + 2 * ps + 11)
    ok &= sp.simplify(D2 - D3 - ps ** 2 * (21 - ps) / ((ps ** 2 + ps + 32) * (ps ** 2 + 2 * ps + 11))) == 0
    ok &= d2(11) == F(43, 164) and d3(11) == F(3, 14)
    check("G1", ok, "d1, d2, d3 equal the kernel's deviation at p = 3, 5, 11, 13, 84, 200; d2 - d3 identity; p = 11: 43/164 > 3/14")

    z = (0, 0, 0)
    pr = [sub(z, e) for e in E]
    check("G2", all(fork(a, b) for a, b in itertools.permutations(pr, 2)), "the three predecessors are pairwise forks")

    u = (0, 0, 0)
    v = add(u, sub(E[0], E[1]))
    succ = lambda x: [add(x, e) for e in E]
    kids = set(succ(u)) | set(succ(v))
    npar = lambda x: sum(1 for e in E if sub(x, e) in (u, v))
    w = [k for k in kids if npar(k) == 2]
    amps = sorted(k for k in kids if npar(k) == 1)
    kid_pairs = [(a, b) for a, b in itertools.combinations(sorted(kids), 2) if fork(a, b)]
    wa = sum(1 for a, b in kid_pairs if w[0] in (a, b))
    check("G3", len(w) == 1 and w[0] == add(u, E[0]) == add(v, E[1]) and len(amps) == 4 and len(kid_pairs) == 7 and wa == 4,
          f"w = {w}, four amplification children, {len(kid_pairs)} child fork pairs ({wa} with w)")

    eps = sp.symbols("e", positive=True)
    Pany = 0
    Emean = 0
    for bits in itertools.product((0, 1), repeat=4):
        pw = sp.Integer(1)
        for b in bits:
            pw *= eps if b else (1 - eps)
        on = {w[0]} | {a for a, b in zip(amps, bits) if b}
        cnt = sum(1 for a, b in kid_pairs if a in on and b in on)
        Pany += pw * (1 if cnt else 0)
        Emean += pw * cnt
    thr = (-2 + sp.sqrt(7)) / 3
    first = next(p for p in range(2, 40) if 4 * max(d2(p), d3(p)) + 3 * max(d2(p), d3(p)) ** 2 < 1)
    ok = (sp.expand(Pany - (1 - (1 - eps) ** 4)) == 0 and sp.expand(Emean - (4 * eps + 3 * eps ** 2)) == 0
          and sp.expand(3 * (eps - thr) * (eps - (-2 - sp.sqrt(7)) / 3) - (3 * eps ** 2 + 4 * eps - 1)) == 0
          and first == 13 and d2(12) == F(11, 47) and d2(13) == F(45, 214))
    check("G4", ok, f"P(some child pair) = 1 - (1-e)^4, mean 4e + 3e^2 (16 patterns); threshold (-2+sqrt7)/3 = {float(thr):.5f}; "
          f"first integer p with mean < 1: {first} (d2(12) = {d2(12)}, d2(13) = {d2(13)})")

    def full_mean(p):
        e1, e2 = d1(p), max(d2(p), d3(p))
        P = lambda x: F(1) if npar(x) >= 2 else (e2 if npar(x) == 1 else e1)
        pairs = {tuple(sorted((k, add(k, f)))) for k in kids for f in FORKS}
        return sum((P(a) * P(b) for a, b in pairs), F(0)), len(pairs)
    m13, n13 = full_mean(13)
    m14, _ = full_mean(14)
    ok = m13 > 1 > m14 and n13 == 23
    check("G5", ok, f"counting every next-level fork pair that contains a child ({n13} pairs): mean {float(m13):.4f} at p = 13, "
          f"{float(m14):.4f} at p = 14")

    A, B, C = sub(u, E[0]), sub(u, E[1]), sub(u, E[2])
    Dd, Ee = sub(v, E[1]), sub(v, E[2])
    assert B == sub(v, E[0])
    five = [A, B, C, Dd, Ee]
    fk = [(i, j) for i, j in itertools.combinations(range(5), 2) if fork(five[i], five[j])]
    f = lambda n, e1, e2: F(1) if n >= 2 else (e2 if n == 1 else e1)
    rows, ok = [], len(fk) == 7
    for p in (200, 84, 13, 11):
        e1, e2 = d1(p), max(d2(p), d3(p))
        Ar = F(0)
        for bits in itertools.product((0, 1), repeat=5):
            S = {i for i in range(5) if bits[i]}
            if any(i in S and j in S for i, j in fk):
                Ar += f(bits[0] + bits[1] + bits[2], e1, e2) * f(bits[1] + bits[3] + bits[4], e1, e2)
        ok &= Ar > 10
        rows.append(f"p = {p}: {float(Ar):.4f}")
    lim = sum(1 for bits in itertools.product((0, 1), repeat=5) if bits[0] + bits[1] + bits[2] >= 2 and bits[1] + bits[3] + bits[4] >= 2)
    check("G6", ok and lim == 10, f"{len(fk)} fork pairs among the five predecessors; A_r " + ", ".join(rows) + f"; eps -> 0 limit {lim}")

    top = (0, 0, 0)
    mids = [sub(top, e) for e in E]
    base = sorted({sub(m, e) for m in mids for e in E})
    bp = [(i, j) for i, j in itertools.combinations(range(6), 2) if fork(base[i], base[j])]

    def run(bits):
        on = {base[i] for i in range(6) if bits[i]}
        mon = {m for m in mids if sum(1 for e in E if sub(m, e) in on) >= 2}
        return sum(1 for e in E if sub(top, e) in mon) >= 2, len(mon)
    ok = len(base) == 6 and len(bp) == 9
    for i, j in bp:
        bits = [0] * 6
        bits[i] = bits[j] = 1
        t, nm = run(bits)
        ok &= (not t) and nm == 1
    forced = sum(1 for bits in itertools.product((0, 1), repeat=6) if run(bits)[0])
    check("G7", ok and forced == 32, f"{len(bp)} base fork pairs, each -> one mid 1 and top 0 at eps = 0; {forced} of 64 masks force the top")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - beyond-the-union-bound a2: the isolated fork-pair kernel of block 30's automaton (one majority child, "
          "four amplification children, seven child fork pairs; P(some child pair both 1) = 1 - (1 - eps2)^4, mean 4 eps2 + 3 eps2^2, "
          "below 1 iff eps2 < (-2+sqrt7)/3, first at p = 13 on (p,1,2)), the eps = 0 two-step eroder on the depth-2 cone, and the "
          "atom-sum no-go (A_r > 10) recomputed with independent geometry. Scope correction: counting also the next-level fork pairs "
          "between a child and a seed site (23 pairs in all), the pair mean is 1.0469 at p = 13 and first drops below 1 at p = 14")
    print("SUMMARY: confirmed with a scope correction - the child-only kernel and threshold p = 13 are exact as defined; the full "
          "pair count moves the threshold to p = 14; the attempt's route fails at its step 5 as it says")
    return 0


if __name__ == "__main__":
    sys.exit(main())

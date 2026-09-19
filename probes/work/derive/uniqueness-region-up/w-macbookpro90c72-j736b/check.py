#!/usr/bin/env python3
"""J:derive:uniqueness-region-up:a3 (worker w-macbookpro90c72-j736b, grok-4.6).

Route distinct from grok a1 / claude a2 (averaged W_rho): exact 2-step
Hamming/Dobrushin of the six-axis level automaton on (p,1,2). Integer
arithmetic throughout (homogeneous weights (n,d,2d) for p=n/d).
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F
from math import gcd

FAIL, PASS = [], []
M = range(6)


def ok(name, cond, detail=""):
    if cond:
        PASS.append(name)
        print(f"CHECK PASS: {name}" + (f"  {detail}" if detail else ""))
    else:
        FAIL.append(name)
        print(f"CHECK FAIL: {name}" + (f"  {detail}" if detail else ""))


def lcm(a, b):
    return a * b // gcd(a, b)


def lcml(xs):
    r = 1
    for x in xs:
        r = lcm(r, x)
    return r


def phi_int(n, d):
    """Integer weights for (p,1,2) with p = n/d: (n, d, 2d)."""
    p, q, r = n, d, 2 * d
    return [[p if s == a else (q if s == (a ^ 1) else r) for a in M] for s in M]


def kernels_int(P):
    wK, ZK = [], []
    for a, b, c in itertools.product(M, repeat=3):
        w = [P[s][a] * P[s][b] * P[s][c] for s in M]
        wK.append(w)
        ZK.append(sum(w))
    return wK, ZK, lcml(ZK)


def cond_w(P, rec):
    w = [P[s][rec[0]] * P[s][rec[1]] * P[s][rec[2]] for s in M]
    return w, sum(w)


def tv_from_w(w1, z1, w2, z2):
    return sum(abs(F(w1[s], z1) - F(w2[s], z2)) for s in M) / 2


def c3(P):
    best = F(0)
    info = None
    max_anti = F(0)
    max_orth = F(0)
    for rec in itertools.product(M, repeat=3):
        w, z = cond_w(P, rec)
        for i in range(3):
            for a2 in M:
                if a2 == rec[i]:
                    continue
                rec2 = list(rec)
                rec2[i] = a2
                w2, z2 = cond_w(P, tuple(rec2))
                d = tv_from_w(w, z, w2, z2)
                kind = "anti" if a2 == (rec[i] ^ 1) else "orth"
                if kind == "anti" and d > max_anti:
                    max_anti = d
                if kind == "orth" and d > max_orth:
                    max_orth = d
                if d > best:
                    best = d
                    info = (rec, i, a2, kind)
    return best, info, max_anti, max_orth


def mix_tv(P, wK, ZK, L, recA, recA2, recB, recC):
    """TV of E[r(.|U,V,W)] when (U,V,W) ~ product of kernels vs A flipped to A2, B,C fixed kernels."""
    wA, ZA = cond_w(P, recA)
    wA2, ZA2 = cond_w(P, recA2)
    wB, ZB = cond_w(P, recB)
    wC, ZC = cond_w(P, recC)
    n1 = [0] * 6
    n2 = [0] * 6
    for a, b, c in itertools.product(M, repeat=3):
        idx = a * 36 + b * 6 + c
        scale = L // ZK[idx]
        c1 = wA[a] * wB[b] * wC[c] * scale
        c2 = wA2[a] * wB[b] * wC[c] * scale
        wk = wK[idx]
        for s in M:
            n1[s] += c1 * wk[s]
            n2[s] += c2 * wk[s]
    den1 = ZA * ZB * ZC * L
    den2 = ZA2 * ZB * ZC * L
    acc = 0
    for s in M:
        acc += abs(n1[s] * den2 - n2[s] * den1)
    return F(acc, 2 * den1 * den2)


def mix_tv_twoflip(P, wK, ZK, L, recA, recB, recB2, recC, recC2):
    """Type 2: A independent of seed; B and C depend on seed."""
    wA, ZA = cond_w(P, recA)
    wB, ZB = cond_w(P, recB)
    wB2, ZB2 = cond_w(P, recB2)
    wC, ZC = cond_w(P, recC)
    wC2, ZC2 = cond_w(P, recC2)
    n1 = [0] * 6
    n2 = [0] * 6
    for a, b, c in itertools.product(M, repeat=3):
        idx = a * 36 + b * 6 + c
        scale = L // ZK[idx]
        c1 = wA[a] * wB[b] * wC[c] * scale
        c2 = wA[a] * wB2[b] * wC2[c] * scale
        wk = wK[idx]
        for s in M:
            n1[s] += c1 * wk[s]
            n2[s] += c2 * wk[s]
    den1 = ZA * ZB * ZC * L
    den2 = ZA * ZB2 * ZC2 * L
    acc = 0
    for s in M:
        acc += abs(n1[s] * den2 - n2[s] * den1)
    return F(acc, 2 * den1 * den2)


def I1_max(P, wK, ZK, L, seed, seed2):
    best = F(0)
    arg = None
    for X, Y, Pp, Q, R in itertools.product(M, repeat=5):
        d = mix_tv(P, wK, ZK, L, (seed, X, Y), (seed2, X, Y), (X, Pp, Q), (Y, Q, R))
        if d > best:
            best = d
            arg = (X, Y, Pp, Q, R)
    return best, arg


def I2_max(P, wK, ZK, L, seed, seed2):
    """g=(1,1): A=(U,V,W) free of seed; B=(V,T,seed); C=(W,seed,S)."""
    best = F(0)
    arg = None
    for U, V, W, T, S in itertools.product(M, repeat=5):
        d = mix_tv_twoflip(
            P, wK, ZK, L,
            (U, V, W),
            (V, T, seed), (V, T, seed2),
            (W, seed, S), (W, seed2, S),
        )
        if d > best:
            best = d
            arg = (U, V, W, T, S)
    return best, arg


def I2_max_alt(P, wK, ZK, L, seed, seed2):
    """g=(1,0) 2-path: A=(1,0) depends, B=(0,0) depends, C=(1,-1) free.
    Free sites: (1,0)=U, (1,-1)=W, (-1,0)=X, (0,-1)=Y, (1,-2)=R.
    A t=0: (U, seed, W); B t=0: (seed, X, Y); C t=0: (W, Y, R).
    """
    best = F(0)
    for U, W, X, Y, R in itertools.product(M, repeat=5):
        d = mix_tv_twoflip(
            P, wK, ZK, L,
            (W, Y, R),
            (U, seed, W), (U, seed2, W),
            (seed, X, Y), (seed2, X, Y),
        )
        if d > best:
            best = d
    return best


def lambda2(n, d):
    P = phi_int(n, d)
    wK, ZK, L = kernels_int(P)
    i1 = F(0)
    i2 = F(0)
    for s2 in (1, 2):
        a, _ = I1_max(P, wK, ZK, L, 0, s2)
        b, _ = I2_max(P, wK, ZK, L, 0, s2)
        if a > i1:
            i1 = a
        if b > i2:
            i2 = b
    return i1, i2, 3 * (i1 + i2)


def e_c3():
    P = phi_int(3, 1)
    c, info, anti, orth = c3(P)
    ok("C.1 c3(3,1,2)=27/110 (block 08), maximizer antipodal", c == F(27, 110) and info[3] == "anti", f"{c} {info}")
    P = phi_int(37, 10)
    c, _, _, _ = c3(P)
    ok(
        "C.2a 3c(37/10)=406962630/413162167<1 (block 28)",
        3 * c == F(406962630, 413162167) and 3 * c < 1,
        str(3 * c),
    )
    P = phi_int(19, 5)
    c, _, _, _ = c3(P)
    ok(
        "C.2b 3c(19/5)=871815/862244>1 (block 28)",
        3 * c == F(871815, 862244) and 3 * c > 1,
        str(3 * c),
    )
    P = phi_int(5, 1)
    c, _, _, _ = c3(P)
    ok("C.3 c3(5)=950/2449, 3c=2850/2449>1", c == F(950, 2449) and 3 * c > 1, str(3 * c))


def e_geom():
    P = phi_int(5, 1)
    wK, ZK, L = kernels_int(P)
    i2, _ = I2_max(P, wK, ZK, L, 0, 1)
    i2alt = I2_max_alt(P, wK, ZK, L, 0, 1)
    ok("G.1 two 2-path geometries give the same I2 at p=5, seed 0->1", i2 == i2alt, f"{i2} vs {i2alt}")
    i1_2, _ = I1_max(P, wK, ZK, L, 0, 2)
    i1_4, _ = I1_max(P, wK, ZK, L, 0, 4)
    ok("G.2 orthogonal flips 0->2 and 0->4 give the same I1 at p=5", i1_2 == i1_4, f"{i1_2}")


def e_lambda():
    i1, i2, lam = lambda2(19, 5)
    ok("L.2a I1,I2,lambda2 at p=19/5 with lambda2<1 while 3c>1", lam < 1, f"I1={i1} I2={i2} lam={lam}")
    ok(
        "L.2b lambda2(19/5)=178335835220898579795025/311576247244342343180928",
        lam == F(178335835220898579795025, 311576247244342343180928),
    )
    i1, i2, lam = lambda2(49, 10)
    ok("L.2c lambda2(49/10)<1", lam < 1, str(lam))
    i1, i2, lam = lambda2(499, 100)
    den = 24625783511450273112712758399765677226463799
    ok(
        "L.3a I1(499/100) exhaustive",
        i1 == F(2814194140585462320880754573399455270870200, den),
        str(i1),
    )
    ok(
        "L.3b I2(499/100) exhaustive",
        i2 == F(5371225220303023355156424506650509468563499, den),
        str(i2),
    )
    ok(
        "L.3c lambda2(499/100)=3(I1+I2)<1",
        lam == F(24556258082665457028111537240149894218301097, den) and lam < 1,
        f"{lam} = {float(lam):.10f}",
    )
    i1, i2, lam = lambda2(5, 1)
    ok(
        "L.4 lambda2(5)=4283413252/4276289513>1 (2-step worst-case no-go)",
        lam == F(4283413252, 4276289513) and lam > 1,
        str(lam),
    )


def main():
    e_c3()
    e_geom()
    e_lambda()
    print(f"CHECKS: PASS={len(PASS)} FAIL={len(FAIL)}")
    if FAIL:
        print("SUMMARY: ROUTE FAILS AT exact-check " + ",".join(FAIL))
        return 1
    print(
        "SUMMARY: PARTIAL 2-step Hamming/Dobrushin of the six-axis level automaton on (p,1,2): "
        "lambda2=3 I1+3 I2 with I1 (I2) the exact max TV of a 1-path (2-path) grandchild over its "
        "5-site cone (7776 configs). lambda2(499/100)=24556258082665457028111537240149894218301097/"
        "24625783511450273112712758399765677226463799<1, so uniqueness and exponential forgetting "
        "by 2-step telescoping (cone of 6 ancestors). lambda2(19/5)<1 already, while 3c(19/5)>1, so "
        "this enlarges the worst-case region past block 08. lambda2(5)=4283413252/4276289513>1: "
        "this route stops at p=5. Distinct from averaged W_rho (a1/a2) which reaches 511/100."
    )
    print(
        "HIT: 2-step exact Hamming coefficient lambda2<1 at p=499/100 on (p,1,2) "
        "(lambda2=24556258082665457028111537240149894218301097/"
        "24625783511450273112712758399765677226463799); uniqueness of the six-axis level "
        "automaton by Dobrushin telescoping on the 6-site 2-step cone. The same criterion "
        "fails at p=5. Enlarges the worst-case (non-averaged) region from 3c<1 at p=37/10 "
        "through 3c>1 at p=19/5 up to p=499/100. Not the W_rho edge 511/100."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

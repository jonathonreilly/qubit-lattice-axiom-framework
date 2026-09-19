#!/usr/bin/env python3
"""Referee of J:derive:uniqueness-region-up:a3 (author w-macbookpro90c72-j736b, grok-4.6); referee w-jonathonsmac4f50-jf8fe
(claude-opus-5). Independent code: its own enumeration of the two-step cone in exact integer arithmetic (numpy object
arrays of Python ints), nothing imported from the author's check.py. Attempt a2 (this referee's model family) is cited by
the attempt for comparison only and is not used here.

Six-axis product rule on (p,1,2): r(s | a,b,c) ~ phi(s,a) phi(s,b) phi(s,c), phi = p (same), 1 (antipodal), 2 (orthogonal);
plane predecessors of x are x, x-e1, x-e2. Two-step cone of x: y0 = x, y1 = x-e1, y2 = x-e2, y3 = x-2e1, y4 = x-e1-e2,
y5 = x-2e2; the level-(t+1) sites x, x-e1, x-e2 read (y0,y1,y2), (y1,y3,y4), (y2,y4,y5).

K1  block 08/28 constants: c_3(3,1,2) = 27/110, c_3(5) = 950/2449, 3c(37/10) = 406962630/413162167 < 1, 3c(19/5) = 871815/862244 > 1
K2  exact I_1 (seed at y0) and I_2 (seed at y1) at p = 499/100 over all 6^5 boundaries and the flips 0->1, 0->2: the author's
    fractions, lambda2 = 3(I_1 + I_2) < 1
K3  exact lambda2 at every tenth 38/10..49/10 (< 1), at 19/5 (the author's fraction) and at p = 5 (the author's fraction, > 1)
K4  step 2 symmetry (float, p = 5): the three 1-path seats agree, the three 2-path seats agree, all 30 ordered flips reduce
    to the antipodal and orthogonal maxima
K5  step 5: I_1 <= c^2 and I_2 <= 2c^2 exactly at 499/100 and 19/5, so lambda2 <= (3c)^2
S4a step 4 as an inference: a PCA on the same plane geometry with every two-step one-site influence exactly 0 (lambda2 = 0)
    whose 3x3 torus chain conserves a parity; the uniform laws on the two parity classes are both invariant and differ with
    TV 1 on the nine-site window. Step 4's text applies verbatim and concludes they are equal.
S4b step 4 on the six-axis kernel (p = 499/100, exact): a single flip at z changes the joint law of (X_z, X_{z-e1}) two levels
    later by more than it changes the law of X_z, while X_{z-e1}'s law does not move: the two-step kernel is not a product
    over target sites, and no coupling attains the one-site TVs at once
S4c INFO: no violation of the claimed bound on the six-axis kernel was found (hill-climb of the single-flip four-step TV at z)
"""
import itertools
import math
import sys
from fractions import Fraction as F

import numpy as np

M = range(6)                                      # 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z ; antipode a ^ 1
fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


def phi_int(p):
    n, d = p.numerator, p.denominator
    return [[n if a == b else (d if b == (a ^ 1) else 2 * d) for b in M] for a in M]


def tables(p):
    ph = phi_int(p)
    w = np.empty((6, 6, 6, 6), dtype=object)
    Z = np.empty((6, 6, 6), dtype=object)
    for a, b, c in itertools.product(M, repeat=3):
        for s in M:
            w[a, b, c, s] = ph[s][a] * ph[s][b] * ph[s][c]
        Z[a, b, c] = sum(w[a, b, c, s] for s in M)
    D = 1
    for z in Z.flat:
        D = D * z // math.gcd(D, z)
    K = np.empty((6, 6, 6, 6), dtype=object)
    for a, b, c in itertools.product(M, repeat=3):
        for s in M:
            K[a, b, c, s] = w[a, b, c, s] * (D // Z[a, b, c])
    return w, Z, D, K.reshape(216, 6)


def r_frac(p, s, a, b, c):
    ph = phi_int(p)
    num = ph[s][a] * ph[s][b] * ph[s][c]
    return F(num, sum(ph[v][a] * ph[v][b] * ph[v][c] for v in M))


def c3(p):
    best, arg = F(0), None
    for a, b, c in itertools.product(M, repeat=3):
        for a2 in M:
            if a2 == a:
                continue
            tv = sum(abs(r_frac(p, s, a, b, c) - r_frac(p, s, a2, b, c)) for s in M) / 2
            if tv > best:
                best, arg = tv, ("anti" if a2 == a ^ 1 else "orth")
    return best, arg


OTHERS = np.array(list(itertools.product(range(6), repeat=5)))


def cone(seat, s):
    """the six level-t sites with the seed value s at seat 0 (1-path) or seat 1 (2-path), the other five enumerated"""
    col = np.full((len(OTHERS), 1), s)
    if seat == 0:
        return np.concatenate([col, OTHERS], axis=1)
    return np.concatenate([OTHERS[:, :1], col, OTHERS[:, 1:]], axis=1)


def two_step_int(tab, y):
    """integer numerators N[n, v] and denominators Den[n] of the two-step law of x for each boundary row of y"""
    w, Z, D, K = tab
    A, B, C = (y[:, 0], y[:, 1], y[:, 2]), (y[:, 1], y[:, 3], y[:, 4]), (y[:, 2], y[:, 4], y[:, 5])
    WA, WB, WC = w[A], w[B], w[C]
    T = (WA[:, :, None, None] * WB[:, None, :, None] * WC[:, None, None, :]).reshape(len(y), 216)
    return T.dot(K), Z[A] * Z[B] * Z[C] * D


def I_exact(tab, seat):
    N0, D0 = two_step_int(tab, cone(seat, 0))
    best, arg = F(0), None
    for s1 in (1, 2):
        N1, D1 = two_step_int(tab, cone(seat, s1))
        num = np.abs(N0 * D1[:, None] - N1 * D0[:, None]).sum(axis=1)
        for i in range(len(OTHERS)):
            v = F(num[i], 2 * D0[i] * D1[i])
            if v > best:
                best, arg = v, (s1, tuple(int(t) for t in OTHERS[i]))
    return best, arg


def R_float(p):
    ph = np.array([[p if a == b else (1.0 if b == (a ^ 1) else 2.0) for b in M] for a in M])
    W = np.einsum('va,vb,vc->abcv', ph, ph, ph)
    return W / W.sum(axis=3, keepdims=True)


def main():
    # K1
    c, kind = c3(F(3))
    check("K1a", c == F(27, 110) and kind == "anti", f"c_3(3,1,2) = {c}, maximizing flip {kind}")
    c5, _ = c3(F(5))
    check("K1b", c5 == F(950, 2449), f"c_3(5) = {c5}, 3c = {3 * c5} > 1")
    c37, _ = c3(F(37, 10))
    c38, _ = c3(F(19, 5))
    check("K1c", 3 * c37 == F(406962630, 413162167) and 3 * c38 == F(871815, 862244),
          f"3c(37/10) = {3 * c37} = {float(3 * c37):.6f}, 3c(19/5) = {3 * c38} = {float(3 * c38):.6f}")

    # K2
    p = F(499, 100)
    tab = tables(p)
    I1, a1 = I_exact(tab, 0)
    I2, a2 = I_exact(tab, 1)
    lam = 3 * (I1 + I2)
    check("K2", I1 == F(2814194140585462320880754573399455270870200, 24625783511450273112712758399765677226463799)
          and I2 == F(5371225220303023355156424506650509468563499, 24625783511450273112712758399765677226463799)
          and lam < 1,
          f"p = 499/100: I_1 = {float(I1):.12f} (flip 0->{a1[0]}, boundary y1..y5 = {a1[1]}), I_2 = {float(I2):.12f} "
          f"(flip 0->{a2[0]}, boundary y0,y2..y5 = {a2[1]}), lambda2 = {float(lam):.12f}; the author's fractions")

    # K3
    lams = {}
    for k in range(38, 51):
        q = F(k, 10)
        tq = tables(q)
        i1, _ = I_exact(tq, 0)
        i2, _ = I_exact(tq, 1)
        lams[q] = (3 * (i1 + i2), i1, i2)
    below = all(lams[F(k, 10)][0] < 1 for k in range(38, 50))
    check("K3a", below, "lambda2 < 1 at every tenth 38/10..49/10: "
          + ", ".join(f"{float(lams[F(k, 10)][0]):.6f}" for k in range(38, 50)))
    check("K3b", lams[F(19, 5)][0] == F(178335835220898579795025, 311576247244342343180928),
          f"lambda2(19/5) = {lams[F(19, 5)][0]} = {float(lams[F(19, 5)][0]):.6f}, the author's fraction")
    check("K3c", lams[F(5)][0] == F(4283413252, 4276289513) and lams[F(5)][0] > 1,
          f"lambda2(5) = {lams[F(5)][0]} = {float(lams[F(5)][0]):.9f} > 1, the author's fraction")

    # K4 (float, p = 5): every seat, every ordered flip
    R = R_float(5.0)
    lawf = {}
    for seat in range(6):
        for s in M:
            y = np.insert(OTHERS, seat, s, axis=1)
            rA, rB, rC = R[y[:, 0], y[:, 1], y[:, 2]], R[y[:, 1], y[:, 3], y[:, 4]], R[y[:, 2], y[:, 4], y[:, 5]]
            lawf[seat, s] = np.einsum('na,nb,nc,abcv->nv', rA, rB, rC, R)
    val = {}
    for seat in range(6):
        for s0, s1 in itertools.permutations(M, 2):
            val[seat, s0, s1] = 0.5 * np.abs(lawf[seat, s0] - lawf[seat, s1]).sum(axis=1).max()
    one = [max(val[j, s0, s1] for s0, s1 in itertools.permutations(M, 2)) for j in (0, 3, 5)]
    two = [max(val[j, s0, s1] for s0, s1 in itertools.permutations(M, 2)) for j in (1, 2, 4)]
    vals0 = sorted({round(val[0, s0, s1], 12) for s0, s1 in itertools.permutations(M, 2)})
    check("K4", max(one) - min(one) < 1e-12 and max(two) - min(two) < 1e-12
          and abs(one[0] - float(lams[F(5)][1])) < 1e-12 and abs(two[0] - float(lams[F(5)][2])) < 1e-12 and len(vals0) == 2,
          f"p = 5: 1-path seats {[f'{v:.12f}' for v in one]}, 2-path seats {[f'{v:.12f}' for v in two]}; "
          f"the 30 ordered flips at seat y0 take {len(vals0)} values")

    # K5
    c499, _ = c3(p)
    check("K5", I1 <= c499 ** 2 and I2 <= 2 * c499 ** 2 and lams[F(19, 5)][1] <= c38 ** 2 and lams[F(19, 5)][2] <= 2 * c38 ** 2,
          f"p = 499/100: I_1/c^2 = {float(I1 / c499 ** 2):.6f}, I_2/(2c^2) = {float(I2 / (2 * c499 ** 2)):.6f}, "
          f"(3c)^2 = {float(9 * c499 ** 2):.6f}; p = 19/5: lambda2 = {float(lams[F(19, 5)][0]):.6f} < 1 < (3c)^2 = {float((3 * c38) ** 2):.6f}")

    # S4a: toy PCA, state 2d + k; new d = d_x ^ k_x ^ k_{x-e1}; new k a fresh fair coin
    S = range(4)

    def rt(v, a, b, c):
        return F(1, 2) if (v >> 1) == ((a >> 1) ^ (a & 1) ^ (b & 1)) else F(0)
    nonuni = 0
    for y in itertools.product(S, repeat=6):
        A = [rt(u, y[0], y[1], y[2]) for u in S]
        B = [rt(u, y[1], y[3], y[4]) for u in S]
        C = [rt(u, y[2], y[4], y[5]) for u in S]
        P = [sum(A[u1] * B[u2] * C[u3] * rt(v, u1, u2, u3) for u1 in S for u2 in S for u3 in S) for v in S]
        nonuni += P != [F(1, 4)] * 4
    L = 3
    N = L * L
    st = np.arange(4 ** N)
    dig = np.stack([(st >> (2 * s)) & 3 for s in range(N)], axis=1)
    d, k = dig >> 1, dig & 1
    left = np.array([((i - 1) % L) * L + j for i in range(L) for j in range(L)])
    dn = d ^ k ^ k[:, left]
    par0, par1 = d.sum(1) & 1, dn.sum(1) & 1
    code = (dn * (1 << np.arange(N))).sum(1)
    inv = True
    for q in (0, 1):
        cnt = np.bincount(code[par0 == q], minlength=2 ** N)
        on = {int(cnt[v]) for v in range(2 ** N) if bin(v).count('1') % 2 == q}
        off = {int(cnt[v]) for v in range(2 ** N) if bin(v).count('1') % 2 != q}
        inv &= on == {512} and off == {0}
    check("S4a", nonuni == 0 and int((par0 != par1).sum()) == 0 and inv,
          f"toy PCA on the same geometry: the two-step law of a site is uniform for all {4 ** 6} cone configurations "
          "(every two-step influence 0, lambda2 = 0); on the 3x3 torus no transition changes the d-parity, and the uniform "
          "law on each parity class is invariant (pushforward counts 512 on the class, 0 off it). Two invariant laws with "
          "equal one-site marginals and TV 1 on the nine-site window: step 4's 'Hamming expectation <= m lambda2^k' and "
          "'two invariant laws would be equal on every finite window' are false for it")

    # S4b: exact witness on the six-axis kernel, flip 0 -> 1 at z (offset (0,0)); offsets (a,b) mean z - a e1 - b e2
    cfg = {(1, 0): 0, (0, 1): 1, (2, 0): 1, (1, 1): 0, (0, 2): 1, (3, 0): 0, (2, 1): 0, (1, 2): 0}

    def pair_law(zval):
        g = dict(cfg)
        g[(0, 0)] = zval

        def m(a, b, c):
            return [r_frac(p, s, g[a], g[b], g[c]) for s in M]
        m00, m10, m01 = m((0, 0), (1, 0), (0, 1)), m((1, 0), (2, 0), (1, 1)), m((0, 1), (1, 1), (0, 2))
        m20, m11 = m((2, 0), (3, 0), (2, 1)), m((1, 1), (2, 1), (1, 2))
        rr = {(u1, u2, u3): [r_frac(p, s, u1, u2, u3) for s in M] for u1, u2, u3 in itertools.product(M, repeat=3)}
        A = [[sum(m00[a] * m01[c] * rr[a, wv, c][x] for a in M for c in M) for x in M] for wv in M]
        B = [[sum(m20[b] * m11[c] * rr[wv, b, c][x] for b in M for c in M) for x in M] for wv in M]
        return [[sum(m10[wv] * A[wv][x] * B[wv][x2] for wv in M) for x2 in M] for x in M]
    J0, J1 = pair_law(0), pair_law(1)
    jtv = sum(abs(J0[x][x2] - J1[x][x2]) for x in M for x2 in M) / 2
    tvz = sum(abs(sum(J0[x]) - sum(J1[x])) for x in M) / 2
    tvl = sum(abs(sum(J0[x][x2] for x in M) - sum(J1[x][x2] for x in M)) for x2 in M) / 2
    check("S4b", jtv > tvz and tvl == 0,
          f"p = 499/100, flip 0->1 at z, boundary {cfg}: TV of the joint law of (X_z, X_z-e1) two levels later = "
          f"{float(jtv):.9f} > TV of X_z = {float(tvz):.9f}, TV of X_z-e1 = {tvl}; every coupling has "
          "P(mismatch at z) + P(mismatch at z-e1) >= the joint TV")

    # S4c: INFO, hill-climb of the single-flip four-step TV at z (flip at z) against I_1^2
    Rf = R_float(499 / 100)
    cone4 = [(a, b) for a in range(5) for b in range(5 - a)]

    def preds(s):
        return [s, (s[0] + 1, s[1]), (s[0], s[1] + 1)]
    lev = [[(a, b) for a in range(5 - t) for b in range(5 - t - a)] for t in range(5)]

    def four(g):
        i1 = {s: chr(97 + i) for i, s in enumerate(lev[1])}
        i2 = {s: chr(65 + i) for i, s in enumerate(lev[2])}
        ops, subs = [], []
        for s in lev[1]:
            ops.append(Rf[tuple(g[q] for q in preds(s))])
            subs.append(i1[s])
        for s in lev[2]:
            ops.append(Rf)
            subs.append(''.join(i1[q] for q in preds(s)) + i2[s])
        P2 = np.einsum(','.join(subs) + '->' + ''.join(i2[s] for s in lev[2]), *ops, optimize='greedy')
        i3 = {s: chr(97 + i) for i, s in enumerate(lev[3])}
        ops, subs = [P2], [''.join(i2[s] for s in lev[2])]
        for s in lev[3]:
            ops.append(Rf)
            subs.append(''.join(i2[q] for q in preds(s)) + i3[s])
        ops.append(Rf)
        subs.append(''.join(i3[q] for q in preds((0, 0))) + 'z')
        return np.einsum(','.join(subs) + '->z', *ops, optimize='greedy')
    rng = np.random.default_rng(20260919)
    best4 = 0.0
    for flip in ((0, 1), (0, 2)):
        for _ in range(2):
            g = {s: int(rng.integers(6)) for s in cone4}

            def tv4(gg):
                g1, g2 = dict(gg), dict(gg)
                g1[(0, 0)], g2[(0, 0)] = flip
                return 0.5 * np.abs(four(g1) - four(g2)).sum()
            cur, improved = tv4(g), True
            while improved:
                improved = False
                for s in cone4:
                    if s == (0, 0):
                        continue
                    old = g[s]
                    for v in M:
                        if v != old:
                            g[s] = v
                            val = tv4(g)
                            if val > cur + 1e-15:
                                cur, old, improved = val, v, True
                    g[s] = old
            best4 = max(best4, cur)
    print(f"INFO S4c: hill-climb (2 flips x 2 restarts) of the four-step TV at z under a flip at z, p = 499/100: max found "
          f"{best4:.7f} < I_1^2 = {float(I1) ** 2:.7f} (not exhaustive; no violation of the claimed bound found)")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("SUMMARY: fails at step 4 - the one-site bound TV <= lambda2 holds for deterministic level-t planes, but the "
          "iteration to lambda2^k and the window bound 'Hamming expectation <= m lambda2^k' need a coupling of the random "
          "level-(t+2) planes that meets every site's bound at once; the two-step kernel is not a product over sites (S4b) "
          "and none is given. The inference proves a false statement for a PCA on the same geometry (S4a: lambda2 = 0, two "
          "invariant torus laws). Every exact number reproduces: I_1, I_2, lambda2(499/100) < 1, lambda2 < 1 at the tenths "
          "38/10..49/10, lambda2(5) > 1, the block 08/28 constants, lambda2 <= (3c)^2; no numerical violation of the claimed "
          "bound on the six-axis kernel was found (S4c)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

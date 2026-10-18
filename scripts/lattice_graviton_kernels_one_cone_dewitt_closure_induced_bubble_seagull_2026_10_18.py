#!/usr/bin/env python3
"""Lattice graviton kernels: one TT cone, DeWitt closure, and the induced-bubble seagull (2026-10-18).

Self-contained consolidated runner for the gravity lane of the scale-ladder campaign
(.claude/science/physics-loops/scale-ladder-campaign-20261018/B4_*, B4b_*). Code adapted from the
campaign's B4_check/check_a_forms.py, B4_check/check_c_closure.py and B4b_check/*.py.
Supplied models only; no physical identification is made here.

PART A (exact, QQ / sympy). Two-derivative quadratic forms S(k,h) on symmetric h:
  A1 invariant and gauge-invariant counts under S4, B4, B3xZ2 (d=4), no symmetry (d=4, d=3);
  A2 every gauge-invariant form in d=4 is L_M = eps eps M k k h h (rank 10); L_I = -(flat Fierz-Pauli);
     L_M = -det(M) * FierzPauli about the background g0 = M (sampled rational M, symbolic k, h);
  A3 S4 / B4 / B3xZ2 gauge-invariant spaces are spanned by L_I, L_J / L_I / L_I, L_E33;
  A4 one cone: in temporal gauge h_{t mu} = 0, for symbolic M and k,
       det(spatial block) = -16 w^8 Q^2,  Q = k^T adj(M) k,
     proved by three symbolic identities (temporal reduction to eps3 eps3 N with N = B^T M B;
     det N = w^4 Q; det of the Sym3 form = -16 det(N)^2).
PART B (exact, QQ). Curvature member of the 09-24 note, generalised to the cubic ultralocal
  inverse-kinetic family dH/dP_jj = a P_jj + b tr P, dH/dP_ij = f P_ij:
  B1 eps3 = 0 for the supplied kinetic term alpha tr h'^2 + beta (tr h')^2 (supplied, not derived);
  B2 R1 is relabelling invariant;
  B3 the closing set of (a,b,f) for generic lapse pairs on 3^3, 4^3, 5^3 tori (face timing = mean of
     four corners or of either opposite pair) is the single DeWitt ray (2,-1,1), eps3 = 0, c = 1/2;
  B4 caveats: special lapse pairs close for every form or fix c only; single-corner timing closes nothing;
  B5 eps3 label correction for the campaign script's float points (exact rationals).
PART C (numerical). The 2026-06-08 staggered Kahler-Dirac induced-graviton bubble, vertex D:
  C1 kernel reconstruction (two constructions of D(P); D D^dag = Delta; operator Ward telescope;
     reproduction of the dispersion runner-cache constant C_time(N=6) = 0.08961606);
  C2 vertex S is not Brillouin-zone periodic, vertex D is;
  C3 khat.Pi_bubble equals a sum of one-propagator (tadpole-type) loops (exact identity);
  C4 B4 symbol space dim 9, Ward map rank 8, unique gauge invariant = linearised EH;
  C5 the measured K^2 symbol lies in the B4 space and violates the Ward identity at O(1);
  C6 lattice Ward residual scaling K^1 / K^3 and its removal by a local nearest-neighbour seagull;
     the seagull's EH coefficient is unconstrained (a_EH not fixed by the bubble);
  C7 mass insensitivity of the symbol-level ratio;
  C8 the repo's 2-component transverse-seagull scheme has the same O(1) symbol-level violation.

Thresholds were fixed before the run from the campaign reports. Runtime: a few minutes on 4 cores.
"""
import itertools
import os
import random
import sys
import time
from fractions import Fraction as Fr
from functools import reduce
from math import gcd
from itertools import product
from multiprocessing import get_context

import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.sdm import SDM

T0 = time.time()
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""), flush=True)


def section(t):
    print(f"\n== {t}  (t = {time.time() - T0:.0f}s)", flush=True)


# =====================================================================================================
# PART A: two-derivative quadratic forms on symmetric h (exact)
# =====================================================================================================
def monomials(d):
    hc = [(a, b) for a in range(d) for b in range(a, d)]
    hh = [(I, J) for I in range(len(hc)) for J in range(I, len(hc))]
    kk = [(e, f) for e in range(d) for f in range(e, d)]
    return hc, [(x, y) for x in hh for y in kk]


def act(g, mon, hc, hci):
    perm, sgn = g
    (I, J), (e, f) = mon
    s = 1
    newh = []
    for X in (I, J):
        a, b = hc[X]
        s *= sgn[a] * sgn[b]
        newh.append(hci[tuple(sorted((perm[a], perm[b])))])
    s *= sgn[e] * sgn[f]
    return (tuple(sorted(newh)), tuple(sorted((perm[e], perm[f])))), s


def group(d, kind):
    """signed permutations (perm, signs) acting on coordinate indices."""
    if kind == "trivial":
        return [(tuple(range(d)), (1,) * d)]
    if kind == "B3xZ2":  # permute/sign the d-1 spatial axes, sign the time axis (last index)
        return [(p + (d - 1,), s) for p in itertools.permutations(range(d - 1))
                for s in itertools.product((1, -1), repeat=d)]
    out = []
    for p in itertools.permutations(range(d)):
        for s in (itertools.product((1, -1), repeat=d) if kind == "B" else [(1,) * d]):
            out.append((p, s))
    return out


def gauge_variation(d, hc, mons):
    """Exact linear map: form coefficients -> coefficients of d/dt S(k, h + t(k xi^T + xi k^T))."""
    rows, ent = {}, {}
    for col, ((I, J), (e, f)) in enumerate(mons):
        for (A, B) in ((I, J), (J, I)):
            a, b = hc[A]
            for (x, y) in ((a, b), (b, a)):
                key = (B, tuple(sorted((e, f, x))), y)
                r = rows.setdefault(key, len(rows))
                ent[(r, col)] = ent.get((r, col), 0) + 1
    return len(rows), ent


def sparse_dm(ent, shape):
    sd = {}
    for (r, c), v in ent.items():
        if v != 0:
            sd.setdefault(r, {})[c] = QQ(v)
    return DomainMatrix.from_rep(SDM(sd, shape, QQ))


def counts(d, kind):
    hc, mons = monomials(d)
    hci = {x: i for i, x in enumerate(hc)}
    idx = {m: i for i, m in enumerate(mons)}
    G = group(d, kind)
    nrows, ent = gauge_variation(d, hc, mons)
    V = sparse_dm(ent, (nrows, len(mons)))
    if kind == "trivial":
        return len(mons), len(mons), len(mons) - V.rank()
    cols = set()
    for m in mons:
        acc = {}
        for g in G:
            mm, s = act(g, m, hc, hci)
            acc[idx[mm]] = acc.get(idx[mm], 0) + s
        vec = sorted((i, v) for i, v in acc.items() if v != 0)
        if vec:
            sgn = 1 if vec[0][1] > 0 else -1
            g0 = vec[0][1] * sgn
            cols.add(tuple((i, Fr(v * sgn, g0)) for i, v in vec))
    cols = sorted(cols)
    bent = {}
    for j, vec in enumerate(cols):
        for i, v in vec:
            bent[(i, j)] = QQ(v.numerator, v.denominator)
    sd = {}
    for (i, j), v in bent.items():
        sd.setdefault(i, {})[j] = v
    B = DomainMatrix.from_rep(SDM(sd, (len(mons), len(cols)), QQ))
    rB = B.rank()
    return len(mons), rB, rB - (V * B).rank()


def levi(n):
    E = {}
    for p in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        E[p] = -1 if inv % 2 else 1
    return E


E4 = levi(4)
E3 = levi(3)


def LM_vec(M, d, hc, idx):
    """coefficient vector of L_M = eps^{a c e al} eps^{b d f be} M_{al be} k_e k_f h_ab h_cd."""
    hci = {x: i for i, x in enumerate(hc)}
    vec = {}
    for (a, c, e, al), s1 in E4.items():
        for (b, dd, f, be), s2 in E4.items():
            co = s1 * s2 * M[al][be]
            if co == 0:
                continue
            I = hci[tuple(sorted((a, b)))]
            J = hci[tuple(sorted((c, dd)))]
            key = ((min(I, J), max(I, J)), tuple(sorted((e, f))))
            vec[idx[key]] = vec.get(idx[key], 0) + co
    return {i: v for i, v in vec.items() if v != 0}


def run_part_A():
    section("PART A1: invariant / gauge-invariant two-derivative forms (exact, orbit sums over QQ)")
    expected = {(4, "S"): (38, 2), (4, "B"): (9, 1), (4, "B3xZ2"): (26, 2), (4, "trivial"): (550, 10),
                (3, "trivial"): (126, 1)}
    names = {"S": "S4 (Kuhn-complex permutations)", "B": "B4 (hyperoctahedral)", "B3xZ2": "B3 x Z2 (space cube x time sign)",
             "trivial": "no symmetry"}
    for (d, kind), (ninv, ngi) in expected.items():
        amb, m, g = counts(d, kind)
        check(f"A1 d={d} {names[kind]}: {ninv} invariant forms, {ngi} gauge-invariant",
              (m, g) == (ninv, ngi), f"[ambient {amb}, invariant {m}, gauge-invariant {g}]")

    section("PART A2: the gauge-invariant forms in d=4 are exactly L_M = eps eps M k k h h")
    hc, mons = monomials(4)
    hci = {x: i for i, x in enumerate(hc)}
    idx = {m: i for i, m in enumerate(mons)}
    nrows, ent = gauge_variation(4, hc, mons)
    V = sparse_dm(ent, (nrows, len(mons)))
    sym_basis = [(i, j) for i in range(4) for j in range(i, 4)]
    Lent = {}
    for col, (i, j) in enumerate(sym_basis):
        M = [[0] * 4 for _ in range(4)]
        M[i][j] = M[j][i] = 1
        for r, v in LM_vec(M, 4, hc, idx).items():
            Lent[(r, col)] = v
    L = sparse_dm(Lent, (len(mons), 10))
    rk = L.rank()
    gv = (V * L).rank()
    nul = len(mons) - V.rank()
    check("A2a the ten L_M (M symmetric) are independent, gauge invariant, and span the full gauge-invariant space",
          rk == 10 and gv == 0 and nul == 10, f"[rank L = {rk}, rank(V L) = {gv}, dim gauge-invariant = {nul}]")

    # L_M versus Fierz-Pauli about the background g0 = M (contractions with G = M^{-1})
    k = sp.symbols("k0:4")
    hv = sp.symbols("h0:10")
    H = sp.Matrix(4, 4, lambda a, b: hv[hci[tuple(sorted((a, b)))]])
    K = sp.Matrix(k)

    def LM_poly(M):
        out = 0
        for (a, c, e, al), s1 in E4.items():
            for (b, dd, f, be), s2 in E4.items():
                if M[al, be] != 0:
                    out += s1 * s2 * M[al, be] * k[e] * k[f] * H[a, b] * H[c, dd]
        return sp.expand(out)

    def FP_poly(Mg):
        G = Mg.inv()
        k2 = (K.T * G * K)[0]
        GH = G * H
        return sp.expand(k2 * (GH * GH).trace() - 2 * (K.T * G * H * G * H * G * K)[0]
                         + 2 * (K.T * G * H * G * K)[0] * GH.trace() - k2 * GH.trace() ** 2)

    ok_I = sp.expand(LM_poly(sp.eye(4)) + FP_poly(sp.eye(4))) == 0
    check("A2b L_I = -(flat Fierz-Pauli) = -(linearised EH symbol about delta), exact polynomial identity", ok_I)
    rnd = random.Random(7)
    oks = []
    for t in range(2):
        A = sp.Matrix(4, 4, lambda i, j: sp.Rational(rnd.randint(-3, 3), rnd.randint(1, 2)))
        M = (A + A.T) / 2 + sp.diag(0, 0, 0, -5)
        if M.det() == 0:
            M = M + sp.eye(4)
        oks.append(sp.expand(LM_poly(M) + M.det() * FP_poly(M)) == 0)
    check("A2c L_M = -det(M) x Fierz-Pauli about the background metric g0 = M (two random rational M, indefinite "
          "and definite blocks; symbolic k, h)", all(oks), f"[{oks}]")

    section("PART A3: symmetry-restricted gauge-invariant spaces are spanned by L_M")
    I4 = [[int(i == j) for j in range(4)] for i in range(4)]
    J4 = [[1] * 4 for _ in range(4)]
    E33 = [[int(i == j == 3) for j in range(4)] for i in range(4)]
    for kind, Ms, label in (("S", (I4, J4), "L_I, L_J  (backgrounds I + c(J - I))"),
                            ("B", (I4,), "L_I"),
                            ("B3xZ2", (I4, E33), "L_I, L_E33  (backgrounds diag(1,1,1,s))")):
        G = group(4, kind)
        vecs = [LM_vec(Mx, 4, hc, idx) for Mx in Ms]
        inv_ok = True
        for vec in vecs:
            for g in G[:: max(1, len(G) // 48)]:
                img = {}
                for i, v in vec.items():
                    mm, s = act(g, mons[i], hc, hci)
                    img[idx[mm]] = img.get(idx[mm], 0) + s * v
                img = {i: v for i, v in img.items() if v != 0}
                inv_ok &= img == vec
        Ls = sparse_dm({(r, c): v for c, vec in enumerate(vecs) for r, v in vec.items()}, (len(mons), len(vecs)))
        _, _, g_dim = counts(4, kind)
        check(f"A3 {kind}: {label} are group invariant, gauge invariant, independent and number dim = {g_dim}",
              inv_ok and (V * Ls).rank() == 0 and Ls.rank() == g_dim == len(vecs))

    section("PART A4: one characteristic cone for every gauge-invariant form (temporal gauge, symbolic proof)")
    w, n1, n2, n3 = sp.symbols("w n1 n2 n3")
    kk = [n1, n2, n3, w]            # time = index 3
    msym = {}
    for i in range(4):
        for j in range(i, 4):
            msym[(i, j)] = msym[(j, i)] = sp.Symbol(f"m{i}{j}")
    Ms = sp.Matrix(4, 4, lambda i, j: msym[(i, j)])
    hs = sp.symbols("s0:6")
    hc3 = [(a, b) for a in range(3) for b in range(a, 3)]
    Hs = sp.Matrix(3, 3, lambda a, b: hs[hc3.index(tuple(sorted((a, b))))])
    # (i) temporal reduction
    Lsp = 0
    for (a, c, e, al), s1 in E4.items():
        if a == 3 or c == 3:
            continue
        for (b, dd, f, be), s2 in E4.items():
            if b == 3 or dd == 3:
                continue
            Lsp += s1 * s2 * Ms[al, be] * kk[e] * kk[f] * Hs[a, b] * Hs[c, dd]
    Bm = sp.zeros(4, 3)
    for s in range(3):
        Bm[s, s] = w
        Bm[3, s] = -kk[s]
    N = (Bm.T * Ms * Bm).applyfunc(sp.expand)

    def F3(Nm, Hm):
        out = 0
        for (a, c, s), s1 in E3.items():
            for (b, dd, t), s2 in E3.items():
                out += s1 * s2 * Nm[s, t] * Hm[a, b] * Hm[c, dd]
        return out

    ok_i = sp.expand(Lsp - F3(N, Hs)) == 0
    check("A4i temporal gauge: L_M restricted to spatial h equals eps3 eps3 N h h with N = B^T M B, "
          "B = [w e_s - k_s e_t] (symbolic M, k, h)", ok_i)
    Q = sp.expand((sp.Matrix(kk).T * Ms.adjugate() * sp.Matrix(kk))[0])
    ok_ii = sp.expand(N.det() - w ** 4 * Q) == 0
    check("A4ii det N = w^4 Q with Q = k^T adj(M) k (Cauchy-Binet; symbolic M, k)", ok_ii)
    nsym = sp.symbols("q0:6")
    Nn = sp.Matrix(3, 3, lambda a, b: nsym[hc3.index(tuple(sorted((a, b))))])
    F = sp.expand(F3(Nn, Hs))
    S6 = sp.Matrix(6, 6, lambda i, j: sp.diff(F, hs[i], hs[j]) / 2)
    dS = sp.expand(S6.det(method="berkowitz"))
    c0 = dS.subs({nsym[0]: 1, nsym[1]: 0, nsym[2]: 0, nsym[3]: 1, nsym[4]: 0, nsym[5]: 1})
    ok_iii = sp.expand(dS + 16 * Nn.det() ** 2) == 0
    check("A4iii the Sym3 quadratic form eps3 eps3 N h h has determinant -16 det(N)^2 (symbolic N)", ok_iii,
          f"[det at N = I: {c0}]")
    check("A4 => det(temporal-gauge spatial block of L_M) = -16 w^8 Q^2 for every symmetric M (any signature, "
          "degenerate included): the only non-trivial characteristic is Q = 0, double: one cone for both TT "
          "polarisations, no leading-order birefringence", ok_i and ok_ii and ok_iii)
    # direct cross-check (checker's path) for random rational M and fixed spatial direction
    rnd = random.Random(7)
    sp_idx = [i for i, (a, b) in enumerate(hc) if a != 3 and b != 3]
    good = []
    for t in range(2):
        A = sp.Matrix(4, 4, lambda i, j: sp.Rational(rnd.randint(-4, 4), rnd.randint(1, 3)))
        M = (A + A.T) / 2 + sp.diag(0, 0, 0, -6)
        kn = [sp.Rational(1), sp.Rational(2), sp.Rational(-1), w]
        Lp = 0
        for (a, c, e, al), s1 in E4.items():
            for (b, dd, f, be), s2 in E4.items():
                if M[al, be] != 0:
                    Lp += s1 * s2 * M[al, be] * kn[e] * kn[f] * H[a, b] * H[c, dd]
        Lp = sp.expand(Lp)
        S = sp.Matrix(10, 10, lambda i, j: sp.diff(Lp, hv[i], hv[j]) / 2)
        det = sp.expand(S.extract(sp_idx, sp_idx).det())
        Qn = sp.expand((sp.Matrix(kn).T * M.adjugate() * sp.Matrix(kn))[0])
        good.append(sp.expand(det + 16 * w ** 8 * Qn ** 2) == 0)
    check("A4 direct: det(spatial block) = -16 w^8 Q^2 for two random rational M (independent direct expansion)",
          all(good), f"[{good}]")


# =====================================================================================================
# PART B: curvature member, constraint closure over the cubic ultralocal inverse-kinetic family (exact)
# =====================================================================================================
PAIRS = ((0, 1), (0, 2), (1, 2))


def unit(j):
    return tuple(int(k == j) for k in range(3))


def build(n):
    sites = list(product(range(n), repeat=3))
    sidx = {x: i for i, x in enumerate(sites)}

    def sh(x, v, s=1):
        return tuple((x[k] + s * v[k]) % n for k in range(3))
    comps = [("d", x, j) for x in sites for j in range(3)] + [("f", y, p) for y in sites for p in PAIRS]
    cidx = {c: i for i, c in enumerate(comps)}
    D = {}

    def add(r, c, v):
        D[(r, c)] = D.get((r, c), 0) + v
    for x in sites:
        for j in range(3):
            col = 3 * sidx[x] + j
            add(cidx[("d", x, j)], col, 2)                       # delta h_jj(z) = 2(xi_j(z) - xi_j(z - e_j))
            add(cidx[("d", sh(x, unit(j)), j)], col, -2)
            for (p, q) in PAIRS:                                  # delta h_pq(y) = forward differences on faces
                if j == q:
                    add(cidx[("f", sh(x, unit(p), -1), (p, q))], col, 1)
                    add(cidx[("f", x, (p, q))], col, -1)
                if j == p:
                    add(cidx[("f", sh(x, unit(q), -1), (p, q))], col, 1)
                    add(cidx[("f", x, (p, q))], col, -1)
    return sites, sh, comps, cidx, D, (len(comps), 3 * len(sites))


def r1_grad(N, sites, sh, comps, cidx):
    """dR1[N]/dh for R1 = p^2 tr h - p.h.p (block-62 placement: diagonal on sites, off-diagonal on faces)."""
    r = [Fr(0)] * len(comps)
    for x in sites:
        lap = [N[sh(x, unit(i))] - 2 * N[x] + N[sh(x, unit(i), -1)] for i in range(3)]
        for j in range(3):
            r[cidx[("d", x, j)]] = -sum(lap[i] for i in range(3) if i != j)
    for y in sites:
        for (i, j) in PAIRS:
            mixed = N[y] - N[sh(y, unit(i))] - N[sh(y, unit(j))] + N[sh(sh(y, unit(i)), unit(j))]
            r[cidx[("f", y, (i, j))]] = 2 * mixed
    return r


def timing(M, y, i, j, sh, kind):
    c = [y, sh(y, unit(i)), sh(y, unit(j)), sh(sh(y, unit(i)), unit(j))]
    if kind == "mean4":
        return sum(M[z] for z in c) / 4
    if kind == "opp_a":
        return (M[c[0]] + M[c[3]]) / 2
    if kind == "opp_b":
        return (M[c[1]] + M[c[2]]) / 2
    if kind == "corner":
        return M[c[0]]
    raise ValueError(kind)


def bracket_parts(N, M, sites, sh, comps, cidx, kind):
    rN = r1_grad(N, sites, sh, comps, cidx)
    rM = r1_grad(M, sites, sh, comps, cidx)
    Ba, Bb, Bf = ([Fr(0)] * len(comps) for _ in range(3))
    for x in sites:
        trN = sum(rN[cidx[("d", x, j)]] for j in range(3))
        trM = sum(rM[cidx[("d", x, j)]] for j in range(3))
        for j in range(3):
            I = cidx[("d", x, j)]
            Ba[I] = M[x] * rN[I] - N[x] * rM[I]
            Bb[I] = M[x] * trN - N[x] * trM
    for y in sites:
        for (i, j) in PAIRS:
            I = cidx[("f", y, (i, j))]
            Bf[I] = timing(M, y, i, j, sh, kind) * rN[I] - timing(N, y, i, j, sh, kind) * rM[I]
    return Ba, Bb, Bf


_BUILD = {}


def closure_space(n, N, M, kind):
    """exact subspace of (a,b,f) with a Ba + b Bb + f Bf in range(D) (span of all relabellings)."""
    if n not in _BUILD:
        sites, sh, comps, cidx, D, shape = build(n)
        Dm = sparse_dm(D, shape).to_dense()
        Y = Dm.transpose().nullspace()      # rows y with y D = 0
        _BUILD[n] = (sites, sh, comps, cidx, D, shape, Dm.rank(), Y)
    sites, sh, comps, cidx, D, shape, rk, Y = _BUILD[n]
    parts = bracket_parts(N, M, sites, sh, comps, cidx, kind)
    Bmat = DomainMatrix([[QQ(v.numerator, v.denominator) for v in row] for row in zip(*parts)], (len(comps), 3), QQ)
    sol = (Y * Bmat).nullspace().to_Matrix()
    rays = []
    for i in range(sol.rows):
        r = list(sol.row(i))
        den = reduce(lambda u, v: u * v // gcd(u, v), [int(sp.Rational(x).q) for x in r], 1)
        r = [int(sp.Rational(x) * den) for x in r]
        g = reduce(gcd, [abs(x) for x in r if x != 0])
        first = next(x for x in r if x != 0)
        rays.append(tuple((x // g) * (1 if first > 0 else -1) for x in r))
    return rk, rays


def run_part_B():
    section("PART B1: the supplied rotation-invariant kinetic term has eps3 = 0 (supplied, not derived)")
    al, be = sp.symbols("alpha beta", nonzero=True)
    M1, M2, M3 = al + be, 2 * be, 2 * al     # alpha h'_ij h'_ij + beta (tr h')^2 in the cube-only family
    eps3 = sp.simplify(M3 / (2 * M1 - M2) - 1)
    check("B1a alpha tr h'^2 + beta (tr h')^2: M1 = alpha + beta, M2 = 2 beta, M3 = 2 alpha => eps3 = 0 identically",
          eps3 == 0, f"[eps3 = {eps3}]")
    # inverse kinetic map: P_jj = 2 alpha h'_jj + 2 beta tr h' ; P_ij = 4 alpha h'_ij (i<j, counted once)
    c = be / (al + 3 * be)
    a_, b_, f_ = 1 / (2 * al), -c / (2 * al), 1 / (4 * al)
    ray = [sp.simplify(x.subs(be, -al) / (1 / (4 * al))) for x in (a_, b_, f_)]
    check("B1b in (a,b,f) coordinates beta = -alpha (c = beta/(alpha+3 beta) = 1/2, the 09-24 closing ratio) is the "
          "DeWitt ray (2,-1,1); generally eps3 = a/(2f) - 1", ray == [2, -1, 1] and sp.simplify(c.subs(be, -al)) == sp.Rational(1, 2),
          f"[ray {ray}]")

    section("PART B2-B4: exact lattice closure {C[N],C[M]} in span(relabellings), cubic family (a,b,f)")
    sites, sh, comps, cidx, D, shape = build(3)
    rnd = random.Random(11)
    Nl = {x: Fr(rnd.randint(-3, 3)) for x in sites}
    r = r1_grad(Nl, sites, sh, comps, cidx)
    DT_r = {}
    for (row, col), v in D.items():
        DT_r[col] = DT_r.get(col, 0) + v * r[row]
    check("B2 R1[N] is exactly relabelling invariant on the 3^3 torus (D^T dR1 = 0)", all(v == 0 for v in DT_r.values()))

    rnd = random.Random(11)
    dewitt = [(2, -1, 1)]
    generic_ok = []
    caveat = {}
    for n in (3, 4, 5):
        sts = list(product(range(n), repeat=3))
        e0 = (0, 0, 0)
        lap = {
            "delta(0),delta(e1)": ({x: Fr(int(x == e0)) for x in sts}, {x: Fr(int(x == (1, 0, 0))) for x in sts}),
            "random ints": ({x: Fr(rnd.randint(-5, 5)) for x in sts}, {x: Fr(rnd.randint(-5, 5)) for x in sts}),
            "delta(0),delta(e1+e2)": ({x: Fr(int(x == e0)) for x in sts}, {x: Fr(int(x == (1, 1, 0))) for x in sts}),
        }
        kinds = ("mean4", "opp_a", "opp_b", "corner") if n == 3 else ("mean4", "corner")
        for kind in kinds:
            for lname, (Nl, Ml) in lap.items():
                if n == 5 and lname != "random ints":
                    continue
                rk, rays = closure_space(n, Nl, Ml, kind)
                print(f"   n={n} timing={kind:6s} lapses={lname:22s} rank D = {rk}: closing (a,b,f) dim {len(rays)} {rays}",
                      flush=True)
                if lname != "delta(0),delta(e1+e2)" and kind != "corner":
                    generic_ok.append(rays == dewitt)
                caveat[(n, kind, lname)] = rays
    check("B3 generic lapse pairs, face timing mean4 / opp_a / opp_b, tori 3^3, 4^3, 5^3: the closing set is exactly "
          "the DeWitt ray (2,-1,1)  (eps3 = 0 and c = 1/2)", all(generic_ok) and len(generic_ok) == 9,
          f"[{sum(generic_ok)}/{len(generic_ok)} cases]")
    check("B4a caveat: the lapse pair delta(0), delta(e1+e2) closes for every (a,b,f) (closure must be required "
          "for all lapse pairs)", len(caveat[(3, "mean4", "delta(0),delta(e1+e2)")]) == 3
          and len(caveat[(4, "mean4", "delta(0),delta(e1+e2)")]) == 3)
    corner_generic = [caveat[(n, "corner", "random ints")] for n in (3, 4, 5)] + \
                     [caveat[(n, "corner", "delta(0),delta(e1)")] for n in (3, 4)]
    check("B4b caveat: single-corner face timing closes for no nonzero (a,b,f) at generic lapse pairs",
          all(len(x) == 0 for x in corner_generic))

    section("PART B5: eps3 label correction for the campaign script's float kinetic points (exact rationals)")
    labels = {}
    for ratio in (Fr(11, 10), Fr(4, 5)):
        # alpha_d = ratio * alpha_f with c = 1/2: a = 1/(2 alpha_d), f = 1/(4 alpha_f): eps3 = a/(2f) - 1 = 1/ratio - 1
        labels[ratio] = 1 / ratio - 1
    check("B5 alpha_d = 1.1 alpha_f has eps3 = -1/11 (labelled +0.1 in the campaign script) and alpha_d = 0.8 alpha_f "
          "has eps3 = +1/4 (labelled -0.2); the closure conclusion is unaffected",
          labels[Fr(11, 10)] == Fr(-1, 11) and labels[Fr(4, 5)] == Fr(1, 4), f"[{labels}]")


# =====================================================================================================
# PART C: the 06-08 staggered Kahler-Dirac induced-graviton bubble (vertex D)
# =====================================================================================================
CORN = list(itertools.product((0, 1), repeat=4))
CI = {c: i for i, c in enumerate(CORN)}


def build_hops():
    """fine-lattice staggered (D chi)(x) = m chi + sum_mu eta_mu(x)/2 [chi(x+mu) - chi(x-mu)] blocked on 2^4 cubes."""
    hops = {}
    for A in CORN:
        x = np.array(A)
        eta = [(-1) ** int(x[:mu].sum()) for mu in range(4)]
        for mu in range(4):
            for s in (+1, -1):
                y = x.copy()
                y[mu] += s
                X = tuple(int(v) for v in np.floor_divide(y, 2))
                B = tuple(int(v) for v in np.mod(y, 2))
                hops.setdefault(X, np.zeros((16, 16)))
                hops[X][CI[A], CI[B]] += 0.5 * s * eta[mu]
    return np.array([X for X in hops], float), np.array([hops[X] for X in hops])


XS, HS = build_hops()


def Dop(P, m):
    ph = np.exp(1j * P @ XS.T)
    return m * np.eye(16)[None] + np.einsum("nh,hab->nab", ph, HS)


def Dop_alt(P, m):
    """second construction: the 06-08 runners' corner-flip form D = m + sum_mu [H0 + Hm e^{-iP} + Hp e^{iP}]."""
    H0 = np.zeros((4, 16, 16)); Hm = np.zeros((4, 16, 16)); Hp = np.zeros((4, 16, 16))
    for A in CORN:
        a = CI[A]
        for mu in range(4):
            Bc = list(A); Bc[mu] ^= 1
            b = CI[tuple(Bc)]
            e = (-1) ** sum(A[nu] for nu in range(mu))
            if A[mu] == 0:
                H0[mu, a, b] += 0.5 * e; Hm[mu, a, b] += -0.5 * e
            else:
                Hp[mu, a, b] += 0.5 * e; H0[mu, a, b] += -0.5 * e
    out = m * np.eye(16)[None].astype(complex) + H0.sum(0)[None]
    out = out + np.einsum("nm,mab->nab", np.exp(-1j * P), Hm) + np.einsum("nm,mab->nab", np.exp(1j * P), Hp)
    return out


def Vel(P):
    ph = np.exp(1j * P @ XS.T)
    return np.einsum("nh,hm,hab->mnab", ph, 1j * XS, HS)


def Delta(P, m):
    return m * m + np.sum(np.sin(P / 2) ** 2, axis=-1)


def Gp(P, m):
    return np.conj(np.swapaxes(Dop(P, m), 1, 2)) / Delta(P, m)[:, None, None]


def grid(N, window0=False):
    p = -np.pi + np.arange(N) * 2 * np.pi / N
    P = np.stack(np.meshgrid(p, p, p, p, indexing="ij"), -1).reshape(-1, 4)
    if window0:                       # same nodes mod 2 pi, window [0, 2 pi)
        P = np.where(P < 0, P + 2 * np.pi, P)
    return P


def fD(x):
    return np.sin(x)


def fS(x):
    return np.sin(x / 2)


def bubble(K, N, m, vertex="D", window0=False, chunk=4096):
    """Pi[mu,nu,rho,sig](K) = N^-4 sum_P tr[G(P) V_mn(Pb) G(P+K) V_rs(Pb)], V_mn = 1/2(Vel_m f_n + Vel_n f_m)."""
    f = fD if vertex == "D" else fS
    K = np.asarray(K, float)
    Pg = grid(N, window0)
    J = np.zeros((4, 4, 4, 4), complex)
    for s in range(0, len(Pg), chunk):
        P = Pg[s:s + chunk]
        Pb = P + K / 2
        G0, G1, V = Gp(P, m), Gp(P + K, m), Vel(Pb)
        A = np.einsum("nab,mnbc->mnac", G0, V)
        B = np.einsum("nab,mnbc->mnac", G1, V)
        t = np.einsum("mnab,rnba->nmr", A, B)
        F = f(Pb)
        J += np.einsum("nmr,nx,ny->mxry", t, F, F)
    J /= len(Pg)
    return 0.25 * (J + J.transpose(1, 0, 2, 3) + J.transpose(0, 1, 3, 2) + J.transpose(1, 0, 3, 2))


def tadpole_contact(K, N, m, chunk=4096):
    """one-propagator form of khat.Pi_bubble (B4b_check identity), vertex D."""
    K = np.asarray(K, float)
    Pg = grid(N)
    R = np.zeros((4, 4, 4), complex)
    for s in range(0, len(Pg), chunk):
        P = Pg[s:s + chunk]
        Pb = P + K / 2
        G0, G1, V = Gp(P, m), Gp(P + K, m), Vel(Pb)
        D0d = np.conj(np.swapaxes(Dop(P, m), 1, 2))
        D1d = np.conj(np.swapaxes(Dop(P + K, m), 1, 2))
        F = fD(Pb)
        Vrs = 0.5 * (np.einsum("rnab,ns->rsnab", V, F) + np.einsum("snab,nr->rsnab", V, F))
        t1 = 0.5 * np.einsum("nx,nab,rsnba->xrs", F, G0 - G1, Vrs)
        X = np.einsum("nab,xnbc,ncd->xnad", G0, V, D1d) - np.einsum("nab,xnbc,ncd->xnad", D0d, V, G1)
        R += t1 + np.einsum("xnab,rsnba->xrs", X, Vrs)
    return R / len(Pg)


def khat(K):
    return 2 * np.sin(np.asarray(K, float) / 2)


def ward(T, K):
    return np.einsum("m,mnrs->nrs", khat(K), T)


def _job(args):
    K, N, m, vertex, window0 = args
    return bubble(np.array(K, float), N, m, vertex, window0)


def eval_many(jobs):
    try:
        with get_context("fork").Pool(min(4, os.cpu_count() or 1)) as pool:
            return pool.map(_job, jobs)
    except Exception as exc:  # fall back to serial
        print(f"   (pool unavailable: {exc}; serial)")
        return [_job(j) for j in jobs]


def symm6(T):
    T = (T + T.transpose(1, 0, 2, 3, 4, 5)) / 2
    T = (T + T.transpose(0, 1, 3, 2, 4, 5)) / 2
    T = (T + T.transpose(0, 1, 2, 3, 5, 4)) / 2
    return (T + T.transpose(2, 3, 0, 1, 4, 5)) / 2


def ward_coef(T):
    C = T.transpose(1, 2, 3, 0, 4, 5)          # n r s | m a b ; symmetrise over (m, a, b)
    return sum(C.transpose(0, 1, 2, *p) for p in itertools.permutations((3, 4, 5))) / 6


def eh_symbol():
    d = np.eye(4)
    return symm6(0.5 * np.einsum("ac,bd,ef->abcdef", d, d, d) - np.einsum("ae,cf,bd->abcdef", d, d, d)
                 + 0.5 * (np.einsum("ab,ce,df->abcdef", d, d, d) + np.einsum("cd,ae,bf->abcdef", d, d, d))
                 - 0.5 * np.einsum("ab,cd,ef->abcdef", d, d, d))


def b4_basis():
    G = []
    for perm in itertools.permutations(range(4)):
        for sg in itertools.product((1, -1), repeat=4):
            G.append((np.array(perm), np.array(sg, float)))
    rng = np.random.default_rng(1)
    vecs = []
    for _ in range(24):
        T = symm6(rng.normal(size=(4,) * 6))
        acc = np.zeros_like(T)
        for perm, sg in G:              # (R T)_{a..f} = s_a..s_f T[perm a, .., perm f]
            sgn = np.einsum("a,b,c,d,e,f->abcdef", sg, sg, sg, sg, sg, sg)
            acc += sgn * T[np.ix_(perm, perm, perm, perm, perm, perm)]
        vecs.append((acc / len(G)).ravel())
    U, s, Vt = np.linalg.svd(np.array(vecs), full_matrices=False)
    r = int((s > 1e-8 * s[0]).sum())
    return Vt[:r].reshape(r, *(4,) * 6), G


def run_part_C():
    m0 = 0.7
    section("PART C1: kernel reconstruction (vertex D of the 06-08 dispersion / telescope runners)")
    rng = np.random.default_rng(7)
    P = rng.uniform(-np.pi, np.pi, (40, 4))
    K = rng.uniform(-np.pi, np.pi, 4)
    D1, D2 = Dop(P, m0), Dop_alt(P, m0)
    check("C1a two independent constructions of the 16x16 block staggered D(P) agree", np.abs(D1 - D2).max() < 1e-12,
          f"[max diff {np.abs(D1 - D2).max():.1e}]")
    e1 = np.abs(D1 @ np.conj(np.swapaxes(D1, 1, 2)) - Delta(P, m0)[:, None, None] * np.eye(16)).max()
    e2 = np.abs(np.einsum("m,mnab->nab", khat(K), Vel(P + K / 2)) - (Dop(P + K, m0) - Dop(P, m0))).max()
    check("C1b D D^dag = (m^2 + sum sin^2(P/2)) I and operator Ward telescope khat.Vel(Pbar) = D(P+K) - D(P)",
          e1 < 1e-12 and e2 < 1e-12, f"[{e1:.1e}, {e2:.1e}]")
    k6 = 2 * np.pi / 6
    jobs = [((0, 0, 0, 0), 6, m0, "D", False), ((k6, 0, 0, 0), 6, m0, "D", False), ((0, k6, 0, 0), 6, m0, "D", False),
            ((0, k6, 0, 0), 6, m0, "D", True), ((0, 0, 0, 0), 6, m0, "D", True),
            ((0, k6, 0, 0), 6, m0, "S", False), ((0, 0, 0, 0), 6, m0, "S", False),
            ((0, k6, 0, 0), 6, m0, "S", True), ((0, 0, 0, 0), 6, m0, "S", True)]
    R = eval_many(jobs)
    Ct = 4 * (R[1][2, 3, 2, 3] - R[0][2, 3, 2, 3]).real / k6 ** 2
    Cx = 4 * (R[2][2, 3, 2, 3] - R[0][2, 3, 2, 3]).real / k6 ** 2
    check("C1c reproduces the repo dispersion runner-cache constant C_time(N=6) = 0.08961606 (= C_space)",
          abs(Ct - 0.08961606) < 1e-7 and abs(Cx - Ct) < 1e-10, f"[C_t = {Ct:.8f}, C_x = {Cx:.8f}]")

    section("PART C2: Brillouin-zone periodicity of the two repo vertex variants (N = 6)")
    dD = np.abs((R[2] - R[0]) - (R[3] - R[4])).max() / np.abs(R[2] - R[0]).max()
    dS = np.abs((R[5] - R[6]) - (R[7] - R[8])).max() / np.abs(R[5] - R[6]).max()
    check("C2 vertex D (f = sin Pbar) is window independent; vertex S (f = sin(Pbar/2)) changes at O(1) with the "
          "BZ window, so it is not a periodic lattice kernel; the theorem uses vertex D", dD < 1e-10 and dS > 1e-2,
          f"[D: {dD:.1e}, S: {dS:.2f}]")

    section("PART C3: khat.Pi_bubble is a sum of one-propagator loops (exact identity, N = 8, on-grid K)")
    Kg = 2 * np.pi / 8 * np.array([1, 2, 0, -1])
    lhs = ward(bubble(Kg, 8, m0), Kg)
    rhs = tadpole_contact(Kg, 8, m0)
    err = np.abs(lhs - rhs).max() / np.abs(lhs).max()
    check("C3 khat.Pi_bubble(K) equals the one-propagator (seagull-tadpole-shaped) contact loops", err < 1e-10,
          f"[relative error {err:.1e}, |khat.Pi| = {np.abs(lhs).max():.3e}]")

    section("PART C4: B4-invariant two-derivative symbols and their Ward map")
    B, G4 = b4_basis()
    r = B.shape[0]
    Wm = np.array([ward_coef(b).ravel() for b in B]).T
    sw = np.linalg.svd(Wm, compute_uv=False)
    EH = eh_symbol()
    nullv = np.linalg.svd(Wm)[2][-1]
    Tinv = np.tensordot(nullv, B, 1)
    cos = abs(np.vdot(Tinv.ravel(), EH.ravel())) / np.linalg.norm(Tinv) / np.linalg.norm(EH)
    ehw = np.abs(ward_coef(EH)).max()
    check("C4 B4 symbol space has dim 9 (= exact count A1), the Ward map has rank 8, and its one-dim kernel is "
          "linearised EH", r == 9 and sw[-1] < 1e-10 * sw[0] and sw[-2] > 1e-3 * sw[0] and cos > 1 - 1e-10 and ehw < 1e-14,
          f"[dim {r}; sv min {sw[-1]:.1e}, next {sw[-2]:.2e}; |cos(null, EH)| = {cos:.12f}; EH Ward {ehw:.0e}]")

    section("PART C5-C7: measured K^2 symbol (m = 0.7, N = 12) and the seagull (parallel bubbles)")
    N = 12
    fit_dirs = [np.array([1.0, 0.37, 0.61, -0.23]), np.array([0.2, 1.0, -0.5, 0.8]), np.array([0.3, -0.1, 0.9, 0.4])]
    fit_dirs = [v / np.linalg.norm(v) for v in fit_dirs]
    ntest = np.array([0.3, 0.8, -0.4, 0.33]); ntest /= np.linalg.norm(ntest)
    kaps = (0.4, 0.2, 0.1)
    jobs = [((0, 0, 0, 0), N, m0, "D", False)]
    for v in fit_dirs:
        jobs += [(tuple(0.1 * v), N, m0, "D", False), (tuple(0.05 * v), N, m0, "D", False)]
    jobs += [(tuple(k * ntest), N, m0, "D", False) for k in kaps]
    for mm in (1.0, 0.5):
        v = fit_dirs[0]
        jobs += [((0, 0, 0, 0), N, mm, "D", False), (tuple(0.1 * v), N, mm, "D", False), (tuple(0.05 * v), N, mm, "D", False)]
    t1 = time.time()
    R = eval_many(jobs)
    print(f"   {len(jobs)} bubbles at N = {N} in {time.time() - t1:.0f}s", flush=True)
    P0 = R[0]

    def rich(P0_, Pa, Pb):
        return (4 * (Pb - P0_) / 0.0025 - (Pa - P0_) / 0.01).real / 3

    M2s = [rich(P0, R[1 + 2 * i], R[2 + 2 * i]) for i in range(3)]
    rows = [np.einsum("iabcdef,e,f->abcdi", B, v, v).reshape(-1, r) for v in fit_dirs]
    A = np.vstack(rows)
    y = np.concatenate([M.ravel() for M in M2s])
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    fit_res = np.linalg.norm(A @ c - y) / np.linalg.norm(y)
    Tm = np.tensordot(c, B, 1)
    # out-of-fit direct symbol (Richardson from kappa = 0.2, 0.1)
    Pt = [R[7], R[8], R[9]]
    Mt = (4 * (Pt[2] - P0).real / 0.01 - (Pt[1] - P0).real / 0.04) / 3
    pred = np.einsum("abcdef,e,f->abcd", Tm, ntest, ntest)
    oof = np.abs(Mt - pred).max() / np.abs(Mt).max()
    check("C5a the measured symbol lies in the 9-dim B4 space: 3-direction fit residual < 1e-3 and the fit predicts "
          "an out-of-fit direction to < 1e-2", np.linalg.matrix_rank(A) == 9 and fit_res < 1e-3 and oof < 1e-2,
          f"[fit residual {fit_res:.1e}; out-of-fit deviation {oof:.1e}]")

    def wratio(T, v):
        M = np.einsum("abcdef,e,f->abcd", T, v, v)
        return np.abs(np.einsum("m,mnrs->nrs", v, M)).max() / np.abs(M).max()

    direct = [np.abs(np.einsum("m,mnrs->nrs", v, M)).max() / np.abs(M).max() for v, M in zip(fit_dirs, M2s)]
    rs = np.random.default_rng(3)
    samp = [v / np.linalg.norm(v) for v in rs.normal(size=(400, 4))]
    samp += [np.eye(4)[i] for i in range(4)] + [np.array(x, float) / np.linalg.norm(x) for x in
                                                 ((1, 1, 0, 0), (0, 1, 1, 0), (1, 1, 1, 0), (0, 1, 1, 1), (1, 1, 1, 1))]
    wr = [wratio(Tm, v) for v in samp]
    five = [wratio(Tm, v / np.linalg.norm(v)) for v in (np.array([1.0, 0.37, 0.61, -0.23]), np.array([0.2, 1.0, -0.5, 0.8]),
                                                        np.array([1.0, 1.0, 0, 0]), np.array([0.3, -0.1, 0.9, 0.4]),
                                                        np.array([1.0, 0, 0, 0]))]
    check("C5b Ward identity k.M2(k) = 0 is violated at O(1) by the K^2 symbol in every direction (ratio > 0.05)",
          min(wr) > 0.05 and min(direct) > 0.05,
          f"[direct along fit dirs {np.round(direct, 4).tolist()}; over the checker's five dirs "
          f"{min(five):.3f}-{max(five):.3f}; over {len(samp)} sampled dirs {min(wr):.3f}-{max(wr):.3f}]")
    a_eh = np.vdot(EH.ravel(), Tm.ravel()) / np.vdot(EH.ravel(), EH.ravel())
    fr = np.linalg.norm(Tm - a_eh * EH) / np.linalg.norm(Tm)
    check("C5c the symbol is not linearised EH: Frobenius EH projection a_EH ~ 0.0288, non-EH fraction > 0.5 "
          "(both norm dependent)", fr > 0.5 and abs(a_eh - 0.028815) < 1e-3, f"[a_EH = {a_eh:.6f}, non-EH fraction {fr:.3f}]")

    CT = a_eh * EH - Tm
    res = []
    for k, Pk in zip(kaps, Pt):
        K = k * ntest
        kh = khat(K)
        S = np.einsum("abcdef,e,f->abcd", CT, kh, kh)
        S2 = np.einsum("abcdef,e,f->abcd", CT + 0.05 * EH, kh, kh)
        res.append((np.abs(ward(Pk, K)).max(), np.abs(ward(Pk - P0, K)).max(), np.abs(ward(Pk - P0 + S, K)).max(),
                    np.abs(ward(Pk - P0 + S2, K) - ward(Pk - P0 + S, K)).max()))
        print(f"   kappa {k:.2f}: |khat.Pi| = {res[-1][0]:.3e}  |khat.(Pi-Pi0)| = {res[-1][1]:.3e}  "
              f"|khat.(Pi-Pi0+S)| = {res[-1][2]:.3e}", flush=True)
    pw = [np.polyfit(np.log(kaps), np.log([x[j] for x in res]), 1)[0] for j in range(3)]
    check("C6a lattice Ward residual (out-of-fit direction): unsubtracted ~ K^1, Pi(0)-subtracted ~ K^3 (so the K^2 "
          "symbol itself violates Ward)", abs(pw[0] - 1) < 0.2 and abs(pw[1] - 3) < 0.2, f"[powers {pw[0]:.2f}, {pw[1]:.2f}]")
    check("C6b a local nearest-neighbour B4 K^2 seagull S(K) = (a EH - T)[khat, khat] removes the violation "
          "(residual power >= 4.5, and smaller by > 10x at kappa = 0.1)", pw[2] >= 4.5 and res[-1][2] < 0.1 * res[-1][1],
          f"[power {pw[2]:.2f}; at kappa 0.1: {res[-1][1]:.1e} -> {res[-1][2]:.1e}]")
    check("C6c the seagull's EH coefficient is unconstrained by the Ward identity (changing a leaves the residual "
          "unchanged): Ward fixes 8 of the 9 B4 seagull coefficients and leaves a_EH free",
          max(x[3] for x in res) < 1e-12, f"[max change {max(x[3] for x in res):.1e}]")

    rm = {}
    for i, mm in enumerate((1.0, 0.5)):
        P0m, Pa, Pb = R[10 + 3 * i], R[11 + 3 * i], R[12 + 3 * i]
        M = rich(P0m, Pa, Pb)
        rm[mm] = np.abs(np.einsum("m,mnrs->nrs", fit_dirs[0], M)).max() / np.abs(M).max()
    rm[0.7] = direct[0]
    spread = (max(rm.values()) - min(rm.values())) / np.mean(list(rm.values()))
    check("C7 the symbol-level Ward ratio along a fixed direction is mass insensitive (m = 1.0, 0.7, 0.5: spread < 15%)",
          spread < 0.15 and min(rm.values()) > 0.05, "[" + ", ".join(f"m={k}: {v:.4f}" for k, v in sorted(rm.items())) + "]")

    section("PART C8: the repo's 2-component 'transverse seagull' scheme (06-08 note), symbol level")
    s = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], complex)

    def G2(q, m):
        return np.linalg.inv(1j * np.einsum("ni,iab->nab", np.sin(q), s) + m * np.eye(2))

    def Vc(q, k):
        u = 1j * np.einsum("ni,iab->inab", np.cos(q + k / 2), s)
        sb = 0.5 * (np.sin(q) + np.sin(q + k))
        return 0.5 * (np.einsum("cnab,nd->cdnab", u, sb) + np.einsum("dnab,nc->cdnab", u, sb))

    def Pi2(k, N2, m):
        p = np.linspace(-np.pi, np.pi, N2, endpoint=False)
        q = np.stack(np.meshgrid(p, p, p, indexing="ij"), -1).reshape(-1, 3)
        A_ = np.einsum("nab,ijnbc->ijnac", G2(q, m), Vc(q, k))
        B_ = np.einsum("nab,klnbc->klnac", G2(q + k, m), Vc(q + k, -k))
        return np.einsum("ijnab,klnba->ijkl", A_, B_) / len(q)

    P02 = Pi2(np.zeros(3), 24, 1.0)
    rat = []
    for k0 in (0.2, 0.1):
        kv = np.array([k0, 0, 0])
        Pk = Pi2(kv, 24, 1.0) - P02
        resid = np.abs(np.einsum("i,ijkl->jkl", 2 * np.sin(kv / 2), Pk)).max()
        tt = Pk[1, 2, 1, 2].real / (2 - 2 * np.cos(k0))
        rat.append(resid / k0 ** 3 / abs(tt))
    check("C8 with its K-independent seagull (equivalent to subtracting Pi(0)) the 2-component scheme's O(k^3) "
          "residual is O(1) relative to k x (TT k^2 slope): the leading symbol is not transverse",
          min(rat) > 0.1 and abs(rat[0] - rat[1]) / rat[1] < 0.1, f"[ratio {rat[0]:.3f} (k=0.2), {rat[1]:.3f} (k=0.1)]")


if __name__ == "__main__":
    print("Lattice graviton kernels: one TT cone, DeWitt closure, induced-bubble seagull (2026-10-18)")
    run_part_A()
    run_part_B()
    run_part_C()
    print(f"\nelapsed {time.time() - T0:.0f}s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    sys.exit(0 if FAIL == 0 else 1)

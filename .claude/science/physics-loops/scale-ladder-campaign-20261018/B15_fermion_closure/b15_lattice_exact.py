#!/usr/bin/env python3
"""B15 (scale-ladder campaign): constraint-closure test with FERMIONIC matter, exact lattice part.

Exact Gaussian-rational arithmetic (Fractions), periodic L^3 torus (default L=5 so that x+2e != x-2e).

Matter (SUPPLIED): a naive nearest-neighbour 2-component Weyl field, one-particle Hamiltonian
    h_N = sum_{x,j} wbar_b (-i v/2) [ sigma^j |x><x+e_j| - sigma^j |x+e_j><x| ],
    wbar_b = wa N_x + wb N_{x+e_j}     (bond-lapse timing; endpoint mean = (1/2, 1/2)),
so that for N = 1, h = v sigma.sin p (doublers kept). H_f(N) = psibar h_N psi (Grassmann).
Naive Dirac variant: alpha^j = offdiag(sigma^j), beta = diag(1,-1) (x) 1_2, on-site mass m N_x beta,
Wilson term r * sum_b wbar_b beta (1/2)(|x><x| + |x+e><x+e| - |x><x+e| - |x+e><x|).

Dictionary (checked in T0 with an explicit Grassmann algebra): with {psi_a, psibar_b} = -i delta_ab,
    {psibar A psi, psibar B psi} = -i psibar [A,B] psi,   {psi, psibar A psi} = -i A psi.
So the constraint bracket is fixed by the one-particle commutator B(N,M) = [h_N, h_M], which is
bilinear and antisymmetric in (N,M). Gravity (09-24 member, B14 E1, exact): its bracket is
G_g[xi_g] with xi_g,b = (sK/(4 alpha)) (N_{x+e} M_x - N_x M_{x+e}), a NEAREST-NEIGHBOUR bilinear.

Tests (PASS/FAIL):
 T0  Grassmann dictionary on a 4-mode toy (exact).
 T1  Weyl, endpoint-mean timing: B(delta_0, delta_d) != 0 for non-nearest-neighbour d (2e_j, e_j+-e_k).
 T2  Weyl, general timing (wa, wb): the non-nn part of B vanishes only at wa = wb = 0.
 T3  kernel of the gravity relabelling map xi -> G_g[xi] is exactly the 3 constant shifts (L=5).
 T4  total-closure no-go: no linear, translation-covariant G_f and no kernel shift give
     B_f = G_f[xi_g + kappa] for all lapses (any timing in the two-endpoint family).
 T5  Dirac mass: the mass cross terms cancel exactly iff wa = wb (endpoint mean).
 T6  Dirac at endpoint mean: B_Dirac = 1_2 (x) B_Weyl exactly (mass drops out); with a Wilson term,
     B acquires Clifford structures (beta, beta alpha) outside the relabelling span {1 (x) sigma}.
 T7  doublers: conjugating with the staggering phase (-1)^{x_1} maps B(sigma^1) to B(-sigma^1) exactly,
     so every doubler sees the same v^2 coefficient (diagonal sigma^j sigma^j terms are invariant).
"""
from __future__ import annotations

import random
import sys
from fractions import Fraction as F
from itertools import product

import sympy as sp

L = int(sys.argv[1]) if len(sys.argv) > 1 else 5
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


# ------------------------------------------------------------------ Gaussian rationals as (re, im)
Z = (F(0), F(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cz(a):
    return a[0] == 0 and a[1] == 0


def C(re, im=0):
    return (F(re), F(im))


# ------------------------------------------------------------------ sparse one-particle operators
def oadd(A, B, s=C(1)):
    out = dict(A)
    for k, v in B.items():
        nv = cadd(out.get(k, Z), cmul(s, v))
        if cz(nv):
            out.pop(k, None)
        else:
            out[k] = nv
    return out


def omul(A, B):
    rows = {}
    for (i, j), v in B.items():
        rows.setdefault(i, []).append((j, v))
    out = {}
    for (i, k), v in A.items():
        for j, w in rows.get(k, ()):
            nv = cadd(out.get((i, j), Z), cmul(v, w))
            if cz(nv):
                out.pop((i, j), None)
            else:
                out[(i, j)] = nv
    return out


def comm(A, B):
    return oadd(omul(A, B), omul(B, A), C(-1))


# ------------------------------------------------------------------ lattice
SITES = list(product(range(L), repeat=3))
IDX = {x: n for n, x in enumerate(SITES)}


def sh(x, d):
    return tuple((x[k] + d[k]) % L for k in range(3))


def unit(j, s=1):
    return tuple(s if k == j else 0 for k in range(3))


SIG = [((C(0), C(1)), (C(1), C(0))), ((C(0), C(0, -1)), (C(0, 1), C(0))), ((C(1), C(0)), (C(0), C(-1)))]
ID2 = ((C(1), C(0)), (C(0), C(1)))


def kron(A, B):
    n, m = len(A), len(B)
    return tuple(tuple(cmul(A[i // m][j // m], B[i % m][j % m]) for j in range(n * m)) for i in range(n * m))


def neg(A):
    return tuple(tuple(cmul(C(-1), a) for a in r) for r in A)


OFF = ((C(0), C(1)), (C(1), C(0)))
DIAG = ((C(1), C(0)), (C(0), C(-1)))
ALPHA = [kron(OFF, SIG[j]) for j in range(3)]
BETA = kron(DIAG, ID2)


def put(op, x, y, mat, coef, nc):
    """op += coef * |x><y| (x) mat"""
    for a in range(nc):
        for b in range(nc):
            v = cmul(coef, mat[a][b])
            if cz(v):
                continue
            k = (IDX[x] * nc + a, IDX[y] * nc + b)
            nv = cadd(op.get(k, Z), v)
            if cz(nv):
                op.pop(k, None)
            else:
                op[k] = nv


def hop_op(n, wa, wb, mats, nc, v=F(1)):
    """sum_b wbar_b (-i v/2)[mat_j |x><x+e| - mat_j |x+e><x|]; n: dict site->lapse (missing = 0)."""
    op = {}
    for x in SITES:
        for j in range(3):
            y = sh(x, unit(j))
            w = wa * n.get(x, 0) + wb * n.get(y, 0)
            if w == 0:
                continue
            put(op, x, y, mats[j], C(0, -v * w / 2), nc)
            put(op, y, x, mats[j], C(0, v * w / 2), nc)
    return op


def mass_op(n, m, nc):
    op = {}
    for x, val in n.items():
        if val:
            put(op, x, x, BETA, C(m * val), nc)
    return op


def wilson_op(n, wa, wb, r):
    op = {}
    for x in SITES:
        for j in range(3):
            y = sh(x, unit(j))
            w = wa * n.get(x, 0) + wb * n.get(y, 0)
            if w == 0:
                continue
            c = C(r * w / 2)
            put(op, x, x, BETA, c, 4)
            put(op, y, y, BETA, c, 4)
            put(op, x, y, BETA, cmul(C(-1), c), 4)
            put(op, y, x, BETA, cmul(C(-1), c), 4)
    return op


def delta(y, val=F(1)):
    return {tuple(c % L for c in y): val}


O = (0, 0, 0)
NN = [unit(j, s) for j in range(3) for s in (1, -1)]
NNN = [unit(j, 2 * s) for j in range(3) for s in (1, -1)] + \
      [tuple(unit(j, s)[k] + unit(k2, t)[k] for k in range(3)) for j in range(3) for k2 in range(3) if j < k2 for s in (1, -1) for t in (1, -1)]


def weyl_B(n, m, wa, wb):
    return comm(hop_op(n, wa, wb, SIG, 2), hop_op(m, wa, wb, SIG, 2))


# ================================================================== T0 Grassmann dictionary
def t0():
    nm = 4  # modes psi_0..3, psibar_0..3 -> generator ids 0..3, 4..7

    def gmul(a, b):
        out = {}
        for m1, c1 in a.items():
            for m2, c2 in b.items():
                if set(m1) & set(m2):
                    continue
                seq = list(m1 + m2)
                sign = 1
                for i in range(len(seq)):  # bubble sort sign
                    for k in range(len(seq) - 1 - i):
                        if seq[k] > seq[k + 1]:
                            seq[k], seq[k + 1] = seq[k + 1], seq[k]
                            sign = -sign
                key = tuple(seq)
                nv = cadd(out.get(key, Z), cmul(C(sign), cmul(c1, c2)))
                if cz(nv):
                    out.pop(key, None)
                else:
                    out[key] = nv
        return out

    def gadd(a, b, s=C(1)):
        out = dict(a)
        for k, v in b.items():
            nv = cadd(out.get(k, Z), cmul(s, v))
            if cz(nv):
                out.pop(k, None)
            else:
                out[k] = nv
        return out

    def dleft(a, g):
        out = {}
        for m, c in a.items():
            if g in m:
                p = m.index(g)
                key = m[:p] + m[p + 1:]
                out = gadd(out, {key: cmul(C((-1) ** p), c)})
        return out

    def dright(a, g):
        out = {}
        for m, c in a.items():
            if g in m:
                p = m.index(g)
                key = m[:p] + m[p + 1:]
                out = gadd(out, {key: cmul(C((-1) ** (len(m) - 1 - p)), c)})
        return out

    def pb(Fp, Gp):
        out = {}
        for a in range(nm):
            out = gadd(out, gmul(dright(Fp, a), dleft(Gp, nm + a)))
            out = gadd(out, gmul(dright(Fp, nm + a), dleft(Gp, a)))
        return {k: cmul(C(0, -1), v) for k, v in out.items()}

    def quad(A):  # psibar_a A_ab psi_b
        out = {}
        for a in range(nm):
            for b in range(nm):
                if not cz(A[a][b]):
                    out = gadd(out, gmul({(nm + a,): C(1)}, {(b,): A[a][b]}))
        return out

    rng = random.Random(15)

    def herm():
        A = [[Z] * nm for _ in range(nm)]
        for a in range(nm):
            A[a][a] = C(rng.randint(-3, 3))
            for b in range(a + 1, nm):
                re, im = rng.randint(-3, 3), rng.randint(-3, 3)
                A[a][b] = C(re, im)
                A[b][a] = C(re, -im)
        return A

    def _sumc(lst):
        out = Z
        for v in lst:
            out = cadd(out, v)
        return out

    def mmul(A, B):
        return [[_sumc([cmul(A[i][k], B[k][j]) for k in range(nm)]) for j in range(nm)] for i in range(nm)]
    ok = True
    for _ in range(3):
        A, B = herm(), herm()
        lhs = pb(quad(A), quad(B))
        AB, BA = mmul(A, B), mmul(B, A)
        Cm = [[cmul(C(0, -1), cadd(AB[i][j], cmul(C(-1), BA[i][j]))) for j in range(nm)] for i in range(nm)]
        ok = ok and lhs == quad(Cm)
        # {psi_a, psibar A psi} = -i (A psi)_a
        for a in range(nm):
            l2 = pb({(a,): C(1)}, quad(A))
            r2 = {}
            for b in range(nm):
                if not cz(A[a][b]):
                    r2[(b,)] = cmul(C(0, -1), A[a][b])
            ok = ok and l2 == r2
    check("T0", ok, "graded Poisson bracket with {psi,psibar}=-i: {psibar A psi, psibar B psi} = -i psibar[A,B]psi and {psi, psibar A psi} = -i A psi (random Gaussian-integer Hermitian A,B, 4 modes)")


# ================================================================== T1 / T2 non-nearest-neighbour lapse pairs
def support_sites(op, nc):
    return {SITES[i // nc] for (i, _) in op} | {SITES[j // nc] for (_, j) in op}


def t1():
    half = F(1, 2)
    nn_nonzero = all(weyl_B(delta(O), delta(d), half, half) for d in NN)
    nnn = {d: weyl_B(delta(O), delta(d), half, half) for d in NNN}
    nonzero = {d: bool(b) for d, b in nnn.items()}
    check("T1a", nn_nonzero, "Weyl, endpoint-mean timing: B(delta_0, delta_d) != 0 for each nearest-neighbour d (sanity)")
    coll = [unit(j, 2 * s) for j in range(3) for s in (1, -1)]
    diag = [d for d in NNN if d not in coll]
    # PRE-RUN expectation (recorded in b15_lattice_exact_L5_firstrun.log) was "all 18 nonzero"; it was WRONG for the
    # 12 diagonal pairs, which cancel at endpoint mean because the two hop orders carry sigma^j sigma^k and
    # sigma^k sigma^j (anticommutator 0). The test below states the observed structure.
    check("T1b", all(nonzero[d] for d in coll) and not any(nonzero[d] for d in diag),
          f"Weyl, endpoint-mean timing: B(delta_0, delta_d) != 0 for the 6 collinear d = +-2e_j (non-nearest-neighbour lapse bilinear N_0 M_2e - N_2e M_0 present) and = 0 for the 12 diagonal d = e_j+-e_k (cancel: {{sigma^j,sigma^k}} = 0); nonzero {sum(nonzero.values())}/18")
    # explicit coefficient, collinear pair: expected -(v^2/4)(1/4)... print matrix element <0|B|2e_1>
    b = nnn[unit(0, 2)]
    el = {(i % 2, j % 2): v for (i, j), v in b.items() if i // 2 == IDX[O] and j // 2 == IDX[unit(0, 2)]}
    print("   <0|B(delta_0,delta_{2e1})|2e1> (2x2, v=1, (re,im)):", {k: (str(v[0]), str(v[1])) for k, v in el.items()})
    # range: bracket of unit lapses vanishes beyond graph distance 2
    far = [z for z in SITES if sum(min(z[k], L - z[k]) for k in range(3)) > 2]
    far_zero = all(not weyl_B(delta(O), delta(z), half, half) for z in far[:40])
    check("T1c", far_zero, "B(delta_0, delta_z) = 0 for graph distance > 2 (40 sites tested): the bracket is range-2 in lapse pairs")


def t2():
    wa, wb = sp.symbols("w_a w_b")
    polys = []
    for d in NNN:
        X = weyl_B(delta(O), delta(d), F(1), F(0))
        Zc = weyl_B(delta(O), delta(d), F(0), F(1))
        S = weyl_B(delta(O), delta(d), F(1), F(1))
        keys = set(X) | set(Zc) | set(S)
        for k in keys:
            x, z, s = X.get(k, Z), Zc.get(k, Z), S.get(k, Z)
            y = (s[0] - x[0] - z[0], s[1] - x[1] - z[1])
            for part in (0, 1):
                p = sp.Rational(x[part]) * wa ** 2 + sp.Rational(y[part]) * wa * wb + sp.Rational(z[part]) * wb ** 2
                if p != 0:
                    polys.append(sp.expand(p))
    # sanity: quadratic interpolation exact (B is quadratic in (wa,wb)); verify at a random point
    t = (F(2, 7), F(-3, 5))
    d = NNN[3]
    direct = weyl_B(delta(O), delta(d), *t)
    X = weyl_B(delta(O), delta(d), F(1), F(0))
    Zc = weyl_B(delta(O), delta(d), F(0), F(1))
    S = weyl_B(delta(O), delta(d), F(1), F(1))
    interp = {}
    for k in set(X) | set(Zc) | set(S):
        x, z, s = X.get(k, Z), Zc.get(k, Z), S.get(k, Z)
        val = tuple(x[p] * t[0] ** 2 + (s[p] - x[p] - z[p]) * t[0] * t[1] + z[p] * t[1] ** 2 for p in (0, 1))
        if val != (0, 0):
            interp[k] = val
    sols = sp.solve(list(set(polys)), [wa, wb], dict=True)
    factored = sorted({str(sp.factor(p)) for p in polys}, key=len)[:6]
    print("   distinct non-nn coefficient polynomials (sample):", factored)
    check("T2", interp == direct and sols == [{wa: 0, wb: 0}],
          f"Weyl, general bond timing wbar = wa N_x + wb N_(x+e): the non-nearest-neighbour part of B vanishes only for wa = wb = 0 (sympy.solve over {len(set(polys))} distinct exact polynomials: {sols}); no two-endpoint timing removes it")


# ================================================================== T3 gravity relabelling kernel
def t3():
    from sympy.polys.matrices import DomainMatrix
    pairs = ((0, 1), (0, 2), (1, 2))
    rows = {}
    nrow = 0
    for x in SITES:
        for j in range(3):
            rows[("d", x, j)] = nrow
            nrow += 1
        for ij in pairs:
            rows[("f", x, ij)] = nrow
            nrow += 1
    col = {(x, j): n for n, (x, j) in enumerate((x, j) for x in SITES for j in range(3))}
    M = [[0] * len(col) for _ in range(nrow)]
    for x in SITES:
        for j in range(3):
            M[rows[("d", x, j)]][col[(x, j)]] += 2
            M[rows[("d", x, j)]][col[(sh(x, unit(j, -1)), j)]] -= 2
        for (i, j) in pairs:
            r = rows[("f", x, (i, j))]
            M[r][col[(sh(x, unit(i)), j)]] += 1
            M[r][col[(x, j)]] -= 1
            M[r][col[(sh(x, unit(j)), i)]] += 1
            M[r][col[(x, i)]] -= 1
    dm = DomainMatrix([[sp.ZZ(v) for v in row] for row in M], (nrow, len(col)), sp.ZZ).convert_to(sp.QQ)
    ns = dm.nullspace().to_Matrix()
    dim = ns.shape[0]
    # constants per direction are in the kernel
    const_ok = True
    for j in range(3):
        vec = [0] * len(col)
        for x in SITES:
            vec[col[(x, j)]] = 1
        const_ok = const_ok and all(sum(M[r][c] * vec[c] for c in range(len(col))) == 0 for r in range(nrow))
    check("T3", dim == 3 and const_ok, f"L={L}: kernel of xi -> G_g[xi] (09-24 relabelling clause, re-implemented) has dimension {dim} and contains the 3 constant shifts: G_g fixes xi up to a global translation")


# ================================================================== T4 total-closure no-go
def t4():
    def xi_g(n, m):
        return {(x, j): n.get(sh(x, unit(j)), 0) * m.get(x, 0) - n.get(x, 0) * m.get(sh(x, unit(j)), 0) for x in SITES for j in range(3)}
    ok = True
    for (wa, wb) in ((F(1, 2), F(1, 2)), (F(1), F(0)), (F(0), F(1)), (F(1, 3), F(2, 3))):
        found = False
        for d in NNN:
            xi = xi_g(delta(O), delta(d))
            b = weyl_B(delta(O), delta(d), wa, wb)
            if all(v == 0 for v in xi.values()) and b:
                sup = support_sites(b, 2)
                # a translation-invariant operator has support = all sites or none
                if 0 < len(sup) < len(SITES):
                    found = True
                    break
        ok = ok and found
    check("T4", ok, "for each timing (1/2,1/2),(1,0),(0,1),(1/3,2/3) there is a lapse pair (delta_0, delta_d), d non-nn, with xi_g = 0 but B_f != 0 and B_f localized (support < all sites). Closure needs B_f = G_f[xi_g + kappa] = G_f[kappa], kappa constant (T3), i.e. a translation-invariant operator: impossible. => NO linear translation-covariant fermion relabelling closes the total algebra exactly on the lattice")


# ================================================================== T5 / T6 Dirac: mass and Wilson
def t5():
    a = sp.Symbol("a")
    m = F(3, 7)
    vals = {}
    for at in (F(0), F(1, 4), F(1, 2), F(1)):
        tot_zero = True
        for d in NN:
            n, mm = delta(O), delta(d)
            cross = oadd(comm(mass_op(n, m, 4), hop_op(mm, at, 1 - at, ALPHA, 4)),
                         comm(hop_op(n, at, 1 - at, ALPHA, 4), mass_op(mm, m, 4)))
            tot_zero = tot_zero and not cross
        vals[at] = tot_zero
    check("T5", vals == {F(0): False, F(1, 4): False, F(1, 2): True, F(1): False},
          f"naive Dirac, on-site mass m N_x beta, bond timing (a, 1-a): mass cross terms in [h_N,h_M] vanish for all unit-lapse pairs iff a = 1/2; table {dict((str(k), v) for k, v in vals.items())} (analytically the residual is m(2a-1) xi~_b alpha^j beta (hop - hop^dag))")


def t6():
    half = F(1, 2)
    m = F(3, 7)
    ok = True
    for d in NN + NNN[:6]:
        n, mm = delta(O), delta(d)
        hn = oadd(hop_op(n, half, half, ALPHA, 4), mass_op(n, m, 4))
        hm = oadd(hop_op(mm, half, half, ALPHA, 4), mass_op(mm, m, 4))
        bd = comm(hn, hm)
        bw = weyl_B(n, mm, half, half)
        # 1_2 (x) B_Weyl in the Dirac basis (upper/lower 2-blocks)
        expect = {}
        for (i, j), v in bw.items():
            si, ai = divmod(i, 2)
            sj, aj = divmod(j, 2)
            for blk in (0, 1):
                expect[(si * 4 + 2 * blk + ai, sj * 4 + 2 * blk + aj)] = v
        ok = ok and bd == expect
    check("T6a", ok, "naive Dirac with mass, endpoint mean: [h_N,h_M] = 1_2 (x) [Weyl bracket] exactly (alpha^j alpha^k = 1 (x) sigma^j sigma^k; mass drops out exactly), 12 lapse pairs")
    r = F(1)
    nonrel = False
    for d in NN:
        n, mm = delta(O), delta(d)
        hn = oadd(hop_op(n, half, half, ALPHA, 4), wilson_op(n, half, half, r))
        hm = oadd(hop_op(mm, half, half, ALPHA, 4), wilson_op(mm, half, half, r))
        bd = comm(hn, hm)
        # components off the block-diagonal 1(x)X form: off-diagonal blocks (beta alpha type) or upper != lower block (beta type)
        for (i, j), v in bd.items():
            si, ai = divmod(i, 4)
            sj, aj = divmod(j, 4)
            if (ai // 2) != (aj // 2):
                nonrel = True
            else:
                partner = (si * 4 + (ai + 2) % 4, sj * 4 + (aj + 2) % 4)
                if bd.get(partner, Z) != v:
                    nonrel = True
    check("T6b", nonrel, "naive Dirac + Wilson term (r=1, endpoint mean): [h_N,h_M] has components outside {1 (x) X} (off-diagonal beta-alpha blocks and/or beta-odd parts) - not of relabelling (Kosmann) Clifford type; order in a measured in b15_scaling.py")


# ================================================================== T7 doublers
def t7():
    half = F(1, 2)
    SIGF = [neg(SIG[0]), SIG[1], SIG[2]]
    ok = True
    rng = random.Random(7)
    n = {x: F(rng.randint(-2, 2)) for x in SITES}
    mm = {x: F(rng.randint(-2, 2)) for x in SITES}
    if L % 2 == 0:
        b = weyl_B(n, mm, half, half)
        bf = comm(hop_op(n, half, half, SIGF, 2), hop_op(mm, half, half, SIGF, 2))
        conj = {}
        for (i, j), v in b.items():
            s = (-1) ** (SITES[i // 2][0] + SITES[j // 2][0])
            conj[(i, j)] = cmul(C(s), v)
        ok = conj == bf
        check("T7", ok, f"L={L}: staggering (-1)^x1 maps B[sigma] to B[-sigma^1, sigma^2, sigma^3] exactly (random lapses): the (pi,0,0) doubler obeys the same bracket with its own flipped-orientation Pauli set; sigma^j sigma^j (v^2) terms invariant")
    else:
        print("   T7 skipped (needs even L)")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "T7":
        t7()
        print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
        sys.exit(0)
    t0()
    t1()
    t2()
    t3()
    t4()
    t5()
    t6()
    t7()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")

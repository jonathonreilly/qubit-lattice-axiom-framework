#!/usr/bin/env python3
"""Independent check of B15 (fermion closure) by EXACT MOMENTUM-SPACE SYMBOL CALCULUS.

Different path from the B15 runners (which use position-space sparse matrices and Taylor-expanded functions):
every operator h_N with plane-wave lapse N = e^{ik.x} acting on psi = e^{ip.x} u is a Laurent polynomial in
X_j = e^{i a k_j}, P_j = e^{i a p_j} with matrix coefficients.  The bracket symbol is
    B(k,q;p) = H(k; q+p) H(q; p) - H(q; k+p) H(k; p),       [h_N, h_M] e^{ipx}u = e^{i(k+q+p)x} B u.
Any TRANSLATION-COVARIANT linear relabelling G_f (ANY range, even non-local) acting on gravity's bond field
xi~_j = N_{x+e}M_x - N_x M_{x+e}  (symbol X_j - Y_j)  has symbol  sum_j (X_j - Y_j) g_j(XY, P).  So exact closure
needs B, after Y = Z/X, to contain only the X-monomials X_j^{+-1} with coef(X_j^{-1}) = -Z_j coef(X_j).

Conventions (B14): {field, G[xi]} = L_xi field for every sector; {psi,psibar} = -i so {psibar A psi, psibar B psi}
= -i psibar[A,B]psi and G_f[u] = psibar (i L_u) psi; gravity {C_g(N),C_g(M)} = G_g[(sK/4alpha) xi~].
Checks (PASS/FAIL), expectations stated before running and justified analytically in the report:
  S0  Fock-space (Jordan-Wigner) check of the bracket dictionary, both statistics-independent pieces.
  S1  continuum symbol: [h_N,h_M] = -v^2 L_w exactly, Kosmann spin coefficient i/4, w = N grad M - M grad N.
  S1b Clifford-signature control: gamma^j = i sigma^j (anti-Hermitian) gives +v^2 L_w (opposite sign).
  S2  closure arithmetic with gravity: v^2 = -sK/(4 alpha).
  S3  exact lattice: X-monomial content of B (range-2 collinear present, diagonal cancel iff wa^2 = wb^2),
      coefficient of the range-2 monomial, and the any-range translation-covariant no-go.
"""
from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


I = sp.I
v, wa, wb, m, r = sp.symbols("v w_a w_b m r")
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
SIG = [s1, s2, s3]
E2 = sp.eye(2)


# ------------------------------------------------------------------ S0 dictionary via Jordan-Wigner
def s0():
    n = 3
    Zm = np.diag([1, -1]).astype(complex); Id = np.eye(2); lo = np.array([[0, 1], [0, 0]], complex)
    cs = []
    for j in range(n):
        ops = [Zm] * j + [lo] + [Id] * (n - j - 1)
        M = ops[0]
        for o in ops[1:]:
            M = np.kron(M, o)
        cs.append(M)
    rng = np.random.default_rng(3)
    ok = True
    for _ in range(3):
        A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); A = A + A.conj().T
        B = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); B = B + B.conj().T
        Q = lambda X: sum(X[a, b] * cs[a].conj().T @ cs[b] for a in range(n) for b in range(n))
        ok &= np.allclose(Q(A) @ Q(B) - Q(B) @ Q(A), Q(A @ B - B @ A))
        # [c_a, Q(B)] = (B c)_a
        for a_ in range(n):
            ok &= np.allclose(cs[a_] @ Q(B) - Q(B) @ cs[a_], sum(B[a_, b] * cs[b] for b in range(n)))
    check("S0", ok, "Fock space (Jordan-Wigner, 3 modes): [Q_A,Q_B] = Q_[A,B], [c, Q_B] = B c; with {.,.} <-> -i[.,.] "
          "this gives {psibar A psi, psibar B psi} = -i psibar[A,B]psi and {psi, psibar B psi} = -i B psi, so "
          "G_f[u] = psibar (i L_u) psi. (Same identity holds for commuting fields: statistics plays no role.)")


# ------------------------------------------------------------------ continuum symbols
def cont_tests():
    k = sp.Matrix(sp.symbols("k1:4")); q = sp.Matrix(sp.symbols("q1:4")); p = sp.Matrix(sp.symbols("p1:4"))

    def Hc(kk, pp, G):  # h_N = -i v gamma^j (N d_j + d_jN/2)  ->  v gamma.(p + k/2)  (for gamma = sigma)
        return sum(((-I * v) * G[j] * (I * pp[j] + I * kk[j] / 2) for j in range(3)), sp.zeros(2, 2))

    def kos(kk, qq, pp, b=I / 4, spin=SIG):  # L_w symbol, w = i(q-k) e^{i(k+q)x}
        w = I * (qq - kk); Kt = kk + qq
        div = (I * Kt).dot(w)
        curl = (I * Kt).cross(w)
        out = (w.dot(I * pp) + div / 2) * E2
        for j in range(3):
            out += b * curl[j] * spin[j]
        return out
    G = SIG
    Bc = (Hc(k, q + p, G) * Hc(q, p, G) - Hc(q, k + p, G) * Hc(k, p, G)).applyfunc(sp.expand)
    diff = (Bc + v**2 * kos(k, q, p)).applyfunc(sp.expand)
    check("S1", diff == sp.zeros(2, 2), "continuum symmetric Weyl operator (plane-wave symbols, exact polynomial identity): "
          "[h_N,h_M] = -v^2 L_w, L_w = w.grad + div w/2 + (i/4)(curl w).sigma")
    # Kosmann coefficient independently: rigid rotation xi = omega x x; L_xi must commute with sigma.p
    bb = sp.Symbol("b")
    om = sp.Matrix(sp.symbols("o1:4")); X = sp.Matrix(sp.symbols("x1:4"))
    # on plane waves use operator form: L_xi = (omega x x).grad + 2 b omega.sigma (div = 0, curl = 2 omega)
    # [ (omega x x).grad , sigma.grad ] = -(omega x grad).sigma ... check via explicit action on f(x)u
    f = sp.Function("f")(*X)
    u = sp.Matrix(sp.symbols("u1:3"))
    xi = om.cross(X)
    def Lxi(psi):
        return sum((xi[j] * psi.diff(X[j]) for j in range(3)), sp.zeros(2, 1)) + 2 * bb * sum((om[j] * SIG[j] for j in range(3)), sp.zeros(2, 2)) * psi
    def D(psi):
        return sum((SIG[j] * psi.diff(X[j]) for j in range(3)), sp.zeros(2, 1))
    cm = (Lxi(D(f * u)) - D(Lxi(f * u))).applyfunc(sp.expand)
    sol = sp.solve(list(cm), bb, dict=True)
    check("S1a", sol == [{bb: I / 4}], f"rotation invariance [L_xi, sigma.grad] = 0 for xi = omega x x fixes b = {sol} "
          "(spin generator sigma/2 with L = x x (-i grad); Kosmann value)")
    # Clifford-signature control
    Ga = [I * s for s in SIG]
    Bg = (Hc(k, q + p, Ga) * Hc(q, p, Ga) - Hc(q, k + p, Ga) * Hc(k, p, Ga)).applyfunc(sp.expand)
    # for gamma = i sigma: gamma^j gamma^k = -(delta + i eps sigma) ; spin part in terms of sigma
    diffg = (Bg - v**2 * kos(k, q, p)).applyfunc(sp.expand)
    check("S1b", diffg == sp.zeros(2, 2), "control: with anti-Hermitian Clifford generators gamma^j = i sigma^j (negative "
          "signature, h_N non-Hermitian) the bracket is +v^2 L_w: the sign of the coefficient IS the Clifford signature, "
          "and Hermitian generators square to +1")
    # S2: closure arithmetic. gravity: total xi = (sK/4alpha) xi~ (+const), xi~ symbol X-Y ~ i a (k - q) = -a w-symbol
    s, K, al = sp.symbols("s K alpha")
    a = sp.Symbol("a")
    kk = sp.Symbol("kk"); qq = sp.Symbol("qq")
    xit = sp.series(sp.exp(I * a * kk) - sp.exp(I * a * qq), a, 0, 2).removeO()
    wsym = I * (qq - kk)
    lead = sp.simplify(xit / a)
    # fermion: {H_f(N),H_f(M)} = -i psibar[h_N,h_M]psi = -i psibar(-v^2 L_w)psi = G_f[v^2 w]; gravity: G_g[(sK/4al) xi~/a]
    v2 = sp.Symbol("v2")
    sol2 = sp.solve(sp.Eq(v2 * wsym, (s * K / (4 * al)) * lead), v2)
    check("S2", sp.simplify(lead + wsym) == 0 and sol2 == [-s * K / (4 * al)],
          f"xi~/a -> -w at leading order; closure requires v^2 = {sol2[0]} (identical to B14's c = -sK/(4alpha)); "
          "v real and K, alpha > 0 => s = -1")


# ------------------------------------------------------------------ exact lattice symbols (Laurent polynomials)
# exponent vector: (X1,X2,X3, Y1,Y2,Y3, P1,P2,P3); ops = dict exps -> Matrix
OFF = {"k": 0, "q": 3, "p": 6}


def madd(D, e, M):
    if e in D:
        D[e] = D[e] + M
    else:
        D[e] = M


def clean(D):
    out = {}
    for e, M in D.items():
        M2 = M.applyfunc(sp.expand)
        if M2 != sp.zeros(*M2.shape):
            out[e] = M2
    return out


def pexp(psi_mom, j, n):
    e = [0] * 9
    for lbl in psi_mom:
        e[OFF[lbl] + j] += n
    return e


def H_op(lap, psi_mom, mats, beta=None, wil=False, mass=False, dim=2):
    """lattice symbol of h_N (lapse momentum label lap) acting on a plane wave with momentum sum psi_mom; a = 1."""
    D = {}
    lo = OFF[lap]
    for j in range(3):
        c = -I * v / 2
        for (xe, pe, coef) in ((0, 1, wa), (1, 1, wb), (-1, -1, -wa), (0, -1, -wb)):
            e = pexp(psi_mom, j, pe); e[lo + j] += xe
            madd(D, tuple(e), c * coef * mats[j])
        if wil:
            # (r/2) beta [ (wa + wb X)(1 - P) + (wa X^-1 + wb)(1 - P^-1) ]
            for (xe, pe, coef) in ((0, 0, wa), (1, 0, wb), (0, 1, -wa), (1, 1, -wb),
                                   (-1, 0, wa), (0, 0, wb), (-1, -1, -wa), (0, -1, -wb)):
                e = pexp(psi_mom, j, pe); e[lo + j] += xe
                madd(D, tuple(e), r / 2 * coef * beta)
    if mass:
        madd(D, tuple([0] * 9), m * beta)
    return clean(D)


def omul(A, B):
    D = {}
    for e1, M1 in A.items():
        for e2, M2 in B.items():
            madd(D, tuple(x + y for x, y in zip(e1, e2)), M1 * M2)
    return clean(D)


def osub(A, B):
    D = dict(A)
    for e, M in B.items():
        madd(D, e, -M)
    return clean(D)


def bracket(**kw):
    return osub(omul(H_op("k", ["q", "p"], **kw), H_op("q", ["p"], **kw)),
                omul(H_op("q", ["k", "p"], **kw), H_op("k", ["p"], **kw)))


def to_XZ(B):
    """Y = Z/X: X-exponent = eX - eY, Z-exponent = eY; group by X-exponent -> {zx-key: {(Z,P) exps: M}}"""
    G = {}
    for e, M in B.items():
        ex = tuple(e[j] - e[3 + j] for j in range(3))
        rest = tuple(e[3:6]) + tuple(e[6:9])
        G.setdefault(ex, {})
        madd(G[ex], rest, M)
    return {k: clean(vv) for k, vv in G.items() if clean(vv)}


def s3():
    dim = 2
    B = bracket(mats=SIG)
    G = to_XZ(B)
    units = {tuple((1 if i == j else 0) * s for i in range(3)) for j in range(3) for s in (1, -1)}
    xkeys = sorted(G)
    print("   X-exponents present in B (general wa, wb):", xkeys)
    coll = {tuple((2 if i == j else 0) * s for i in range(3)) for j in range(3) for s in (1, -1)}
    diag = {k for k in G if sum(abs(x) for x in k) == 2 and k not in coll}
    # coefficients of the non-nn X monomials as polynomials in wa, wb (collect all matrix entries)
    def coefpolys(keyset):
        ps = set()
        for kx in keyset:
            for ee, M in G[kx].items():
                for ent in M:
                    if ent != 0:
                        ps.add(sp.factor(sp.expand(ent / v**2)))
        return ps
    pc = coefpolys(coll & set(G)); pd = coefpolys(diag)
    print("   collinear (X_j^{+-2}) coefficients / v^2:", sorted(map(str, pc))[:6])
    print("   diagonal (X_jX_k^{+-1}) coefficients / v^2 (sample):", sorted(map(str, pd))[:6])
    ok_coll = coll <= set(G) and all(sp.expand(pp).has(wa) and sp.expand(pp).has(wb) and sp.expand(pp.subs(wa, wb)) != 0 for pp in pc)
    # PRE-RUN expectation (first run, chk_b15_symbols_firstrun.log) was "all 12 diagonal X_jX_k^(+-1) present with
    # coefficient ~ wa^2 - wb^2"; WRONG in detail: the 6 same-sign pairs +-(e_j+e_k) (forward-forward paths, weight wa*wb on
    # both orderings) cancel through {sigma^j,sigma^k} = 0 for EVERY timing; only the 6 mixed pairs +-(e_j-e_k)
    # (forward-backward paths, weights wb^2 and wa^2) survive, with coefficient ~ wa^2 - wb^2.
    mixed = {k for k in diag if sorted(k) == [-1, 0, 1]}
    ok_diag = len(diag) == 6 and diag == mixed and all(sp.expand(pp.subs(wa, wb)) == 0 for pp in pd) and all(sp.expand(pp.subs(wa, -wb)) == 0 for pp in pd)
    others = set(G) - units - coll - diag
    check("S3a", ok_coll and ok_diag and not others,
          f"exact symbol, general (wa,wb): X-monomials of B are the 6 nn units, the 6 collinear X_j^(+-2) (coefficient "
          f"+-wa*wb/4 v^2, spin-independent) and only the 6 mixed diagonal X_j X_k^(-1) (coefficient ~ (wa^2-wb^2)/4 v^2); the "
          f"same-sign diagonal X_jX_k are absent for every timing; nothing else ({len(others)} other)")
    # explicit range-2 monomial at endpoint mean, position space: coefficient of |x><x+2e_1| with lapse pair (N_x M_{x+2e})
    half = {wa: sp.Rational(1, 2), wb: sp.Rational(1, 2)}
    # monomial X_1^0 Y_1^2 ... : N_x M_{x+2e} term in <x|B|x+2e>: psi momentum enters as P^2 at the right, lapse M at x+2e
    # In symbol language: e^{i(k+q+p)x} coefficient of X^a Y^b P^c  <-> sum_x N_{x+a} M_{x+b} psi_{x+c} ... (shift form)
    tgt = {}
    for e, M in B.items():
        if e[6:9] == (2, 0, 0):
            tgt[e[:6]] = M.subs(half)
    # non-nn lapse pair inside <x|B|x+2e1>: (N_x M_{x+2e}) -> X^0 Y^(2,0,0) ; (N_{x+2e} M_x) -> X^(2,0,0) Y^0
    c1 = tgt.get((0, 0, 0, 2, 0, 0)); c2 = tgt.get((2, 0, 0, 0, 0, 0))
    print("   <x|B|x+2e1> coefficient of N_x M_{x+2e1}:", c1, " of N_{x+2e1} M_x:", c2)
    okm = c1 == -v**2 / 16 * E2 and c2 == v**2 / 16 * E2
    tgt2 = {e[:6]: M.subs(half) for e, M in B.items() if e[6:9] == (-2, 0, 0)}
    # <x|B|x-2e>: N_x M_{x-2e}: X^0 Y^(-2)
    c3 = tgt2.get((0, 0, 0, -2, 0, 0))
    okm = okm and c3 == -v**2 / 16 * E2   # from +(v^2/16) f_{x-2e}|x><x-2e|, f_{x-2e} = N_{x-2e}M_x - N_x M_{x-2e}
    check("S3b", okm, "endpoint mean: non-nn part of <x|[h_N,h_M]|x+2e> is -(v^2/16)(N_x M_{x+2e} - N_{x+2e} M_x) * 1_2 and "
          "<x+2e|..|x> the negative (anti-Hermitian), i.e. -(v^2/16) f_x (|x><x+2e| - h.c.), spin-independent")
    # no-go for ANY translation-covariant linear G_f: needs X-monomials only +-units, coef(X^-1) = -Z coef(X)
    Gh = to_XZ({e: M.subs(half) for e, M in B.items()})
    bad = [kx for kx in Gh if kx not in units]
    rel_ok = True
    for j in range(3):
        up = tuple(1 if i == j else 0 for i in range(3)); dn = tuple(-1 if i == j else 0 for i in range(3))
        A = Gh.get(up, {}); Bd = Gh.get(dn, {})
        # -Z_j * A  should equal Bd
        shifted = {}
        for ee, M in A.items():
            e2 = list(ee); e2[j] += 1
            madd(shifted, tuple(e2), -M)
        rel_ok &= clean(shifted) == clean(Bd)
    check("S3c", bad and set(bad) == coll and rel_ok,
          f"endpoint mean, ANY-range translation-covariant G_f: the nn part satisfies the xi~ relation coef(X^-1) = -Z coef(X) "
          f"exactly, but X-monomials {sorted(bad)} lie outside span_j (X_j - Y_j) g_j(XY,P): no translation-covariant linear "
          f"G_f of any range (and no constant kernel shift, which lives only at K = 0) closes the bracket exactly")
    return B


def s3_timings(B):
    """the obstruction exists for every two-endpoint timing: the non-nn X-monomials vanish only at wa = wb = 0"""
    G = to_XZ(B)
    units = {tuple((1 if i == j else 0) * s for i in range(3)) for j in range(3) for s in (1, -1)}
    polys = set()
    for kx, D in G.items():
        if kx in units:
            continue
        for ee, M in D.items():
            for ent in M:
                if ent != 0:
                    polys.add(sp.expand(ent))
    sol = sp.solve(list(polys), [wa, wb], dict=True)
    check("S3d", sol == [{wa: 0, wb: 0}], f"general timing wbar = wa N_x + wb N_(x+e): non-nn part vanishes only at {sol}")


if __name__ == "__main__":
    s0()
    cont_tests()
    B = s3()
    s3_timings(B)
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")

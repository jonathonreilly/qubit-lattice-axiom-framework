#!/usr/bin/env python3
"""Independent check of B15: orders of the obstruction against the MOST GENERAL translation-covariant G_f,
mass/Wilson timing, doublers, gravity kernel, and a no-go for NON-translation-covariant linear G_f.

Method: exact lattice symbols (Laurent polynomials in X=e^{iak}, Y=e^{iaq}, P=e^{iap}) expanded in a with
k = K/2 + kappa, q = K/2 - kappa (K: total lapse-pair momentum, kappa: relative momentum, exact rational K, p,
symbolic kappa). A translation-covariant linear G_f acting on gravity's bond field has symbol
    sum_j [(X_j - Y_j)/a] g_j(K,p;a) = sum_j [2i e^{iaK_j/2} sin(a kappa_j)/a] g_j,
so order by order (B = sum_n a^n B_n, s_j = sin(a kappa_j)/a = kappa_j - a^2 kappa_j^3/6 + ...):
    B_0, B_1 must be LINEAR in kappa;  B_2 + sum_j kappa_j^3 g_j0/6 linear in kappa, g_j0 = dB_0/dkappa_j; ...
'Absorbable at O(a^n)' = these hold with g_j(K,p) ARBITRARY matrices (any range, any Clifford structure).
'Kosmann-class' = additionally g_j confined to the relabelling Clifford span (Weyl: all 2x2; Dirac: 1 (x) X).
"""
from __future__ import annotations

import random
import sys
from itertools import product

import numpy as np
import sympy as sp

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


I = sp.I
A = sp.Symbol("a")
kap = sp.symbols("c1:4")  # relative momentum kappa
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
SIG = [s1, s2, s3]
E2 = sp.eye(2)
OFFD = sp.Matrix([[0, 1], [1, 0]]); DG = sp.Matrix([[1, 0], [0, -1]])
ALP = [sp.kronecker_product(OFFD, s) for s in SIG]
BET = sp.kronecker_product(DG, E2)
OFF = {"k": 0, "q": 3, "p": 6}


def madd(D, e, M):
    D[e] = D[e] + M if e in D else M


def clean(D):
    out = {}
    for e, M in D.items():
        M2 = M.applyfunc(sp.expand)
        if any(x != 0 for x in M2):
            out[e] = M2
    return out


def pexp(psi_mom, j, n):
    e = [0] * 9
    for lbl in psi_mom:
        e[OFF[lbl] + j] += n
    return e


def H_op(lap, psi_mom, mats, v, wa, wb, beta=None, r=0, mass=0, dim=2):
    """symbol of h_N; each term tagged with its power of 1/a in a 10th slot"""
    D = {}
    lo = OFF[lap]
    for j in range(3):
        for (xe, pe, coef) in ((0, 1, wa), (1, 1, wb), (-1, -1, -wa), (0, -1, -wb)):
            e = pexp(psi_mom, j, pe); e[lo + j] += xe
            madd(D, tuple(e) + (1,), (-I * v / 2) * coef * mats[j])
        if r:
            for (xe, pe, coef) in ((0, 0, wa), (1, 0, wb), (0, 1, -wa), (1, 1, -wb),
                                   (-1, 0, wa), (0, 0, wb), (-1, -1, -wa), (0, -1, -wb)):
                e = pexp(psi_mom, j, pe); e[lo + j] += xe
                madd(D, tuple(e) + (1,), sp.Rational(r) / 2 * coef * beta)
    if mass:
        madd(D, tuple([0] * 9) + (0,), mass * beta)
    return clean(D)


def omul(P, Q):
    D = {}
    for e1, M1 in P.items():
        for e2, M2 in Q.items():
            madd(D, tuple(x + y for x, y in zip(e1, e2)), M1 * M2)
    return clean(D)


def osub(P, Q):
    D = dict(P)
    for e, M in Q.items():
        madd(D, e, -M)
    return clean(D)


def bracket(**kw):
    return osub(omul(H_op("k", ["q", "p"], **kw), H_op("q", ["p"], **kw)),
                omul(H_op("q", ["k", "p"], **kw), H_op("k", ["p"], **kw)))


def expand_a(B, K, p, nmax, flip=(1, 1, 1)):
    """B = sum_n a^n B_n, n = -2..nmax; K, p rational 3-vectors; flip: doubler P_j -> flip_j P_j."""
    dim = next(iter(B.values())).shape[0]
    out = {n: sp.zeros(dim, dim) for n in range(-2, nmax + 1)}
    for e, M in B.items():
        eX, eY, eP, pw = e[0:3], e[3:6], e[6:9], e[9]
        sign = 1
        for j in range(3):
            if flip[j] == -1 and eP[j] % 2:
                sign = -sign
        th = sum(sp.Rational(eX[j] + eY[j], 2) * K[j] + eP[j] * p[j] for j in range(3))
        lam = sum((eX[j] - eY[j]) * kap[j] for j in range(3))
        # coefficient a^{-pw} * exp(i a (th + lam)) = sum_n (i)^n (th+lam)^n a^{n-pw}/n!
        for nn in range(0, nmax + pw + 1):
            order = nn - pw
            out[order] += sign * M * sp.expand((I * (th + lam)) ** nn / sp.factorial(nn))
    return {n: Mx.applyfunc(sp.expand) for n, Mx in out.items()}


def kdeg_parts(Mx):
    """split matrix polynomial in kappa by total kappa-degree"""
    parts = {}
    for idx, ent in enumerate(Mx):
        if ent == 0:
            continue
        pol = sp.Poly(ent, *kap)
        for mon, c in pol.terms():
            d = sum(mon)
            parts.setdefault(d, sp.zeros(*Mx.shape))
            parts[d][idx] += c * sp.prod([kap[i] ** mon[i] for i in range(3)])
    return parts


def is_zero(Mx):
    return all(sp.expand(x) == 0 for x in Mx)


def nonlinear_part(Mx):
    P = kdeg_parts(Mx)
    out = sp.zeros(*Mx.shape)
    for d, Q in P.items():
        if d != 1:
            out += Q
    return out


def kosmann(K, p, v, spin, dim=2):
    """continuum -v^2 L_w symbol at k = K/2 + kappa, q = K/2 - kappa: w = i(q-k) = -2i kappa"""
    kv = sp.Matrix(kap)
    Kv = sp.Matrix(K); pv = sp.Matrix(p)
    w = -2 * I * kv
    div = (I * Kv).dot(w); curl = (I * Kv).cross(w)
    L = (w.dot(I * pv) + div / 2) * sp.eye(2)
    for j in range(3):
        L += I / 4 * curl[j] * spin[j]
    L = L.applyfunc(sp.expand)
    if dim == 4:
        L = sp.kronecker_product(E2, L)
    return (-v**2 * L).applyfunc(sp.expand)


def g0_cubic(B0):
    """sum_j kappa_j^3 g_j0 / 6 with g_j0 = d B_0 / d kappa_j (B_0 linear in kappa)"""
    return sum((B0.diff(kap[j]) * kap[j] ** 3 / 6 for j in range(3)), sp.zeros(*B0.shape)).applyfunc(sp.expand)


def even_part(Mx):
    X = (Mx[0:2, 0:2] + Mx[2:4, 2:4]) / 2
    return sp.kronecker_product(E2, X).applyfunc(sp.expand)


def clifford_odd(Mx):
    """Dirac 4x4: part outside {1_2 (x) X}: off-diagonal blocks, and (upper - lower)/2 of diagonal blocks"""
    U, Lo = Mx[0:2, 0:2], Mx[2:4, 2:4]
    return not (is_zero(Mx[0:2, 2:4]) and is_zero(Mx[2:4, 0:2]) and is_zero(U - Lo))


rng = random.Random(1518)
def rq():
    return sp.Rational(rng.randint(-9, 9), rng.randint(1, 7))


V = sp.Rational(4, 5)
HALF = sp.Rational(1, 2)
PTS = [([rq() for _ in range(3)], [rq() for _ in range(3)]) for _ in range(2)]


def weyl_orders():
    Bh = bracket(mats=SIG, v=V, wa=HALF, wb=HALF)
    B1 = bracket(mats=SIG, v=V, wa=sp.Integer(1), wb=sp.Integer(0))
    ok_lead = ok_h1 = ok_h2dev = ok_h2obs = ok_t1dev = ok_t1lin = ok_t1obs = True
    ok_t1obs2 = True
    for (K, p) in PTS:
        eh = expand_a(Bh, K, p, 2)
        e1 = expand_a(B1, K, p, 2)
        kos = kosmann(K, p, V, SIG)
        ok_lead &= is_zero(eh[-2]) and is_zero(eh[-1]) and is_zero(eh[0] - kos) and is_zero(e1[0] - kos)
        ok_h1 &= is_zero(eh[1])
        ok_h2dev &= not is_zero(eh[2])
        ok_h2obs &= not is_zero(nonlinear_part(eh[2] + g0_cubic(eh[0])))
        ok_t1dev &= not is_zero(e1[1])
        ok_t1lin &= is_zero(nonlinear_part(e1[1]))
        ok_t1obs &= not is_zero(nonlinear_part(e1[2] + g0_cubic(e1[0])))
    check("O1", ok_lead, "Weyl, timings (1/2,1/2) and (1,0): O(a^-2), O(a^-1) vanish and O(a^0) = -v^2 L_w (Kosmann, sigma) exactly")
    check("O2", ok_h1 and ok_h2dev and ok_h2obs,
          "endpoint mean: O(a) part = 0; O(a^2) part nonzero and NOT absorbable by any translation-covariant G_f "
          "(any range, any 2x2 structure): kappa-cubic part != -sum kappa_j^3 g_j0/6 -> genuine O(a^2) obstruction")
    check("O3", ok_t1dev and ok_t1lin,
          "one-endpoint timing (1,0): O(a) deviation from the symmetric Kosmann relabelling is nonzero BUT LINEAR in kappa, "
          "i.e. of the form sum_j kappa_j g_j1(K,p): it IS absorbable by an O(a)-corrected translation-covariant G_f "
          "(B15's 'O(a) obstruction' for t != 1/2 is only an O(a) deviation from the symmetric G_f)")
    check("O4", ok_t1obs, "one-endpoint timing: after O(a) absorption the O(a^2) part is still non-absorbable (obstruction O(a^2))")
    return Bh


def weyl_O1_structure():
    """identify the absorbable O(a) term at t = 1: is it -v^2 L_{delta u} with delta u_j = c d_j u_j (bond placement)?"""
    B1 = bracket(mats=SIG, v=V, wa=sp.Integer(1), wb=sp.Integer(0))
    cs = sp.Symbol("cc")
    ok = True
    for (K, p) in PTS:
        e1 = expand_a(B1, K, p, 1)
        # delta u_j = cc * d_j u_j with u = w = -2i kappa e^{iKx}: d_j -> i K_j ; Kosmann L of a general u-symbol:
        Kv, pv = sp.Matrix(K), sp.Matrix(p)
        w = -2 * I * sp.Matrix(kap)
        du = sp.Matrix([cs * I * K[j] * w[j] for j in range(3)])
        div = (I * Kv).dot(du); curl = (I * Kv).cross(du)
        Ld = (du.dot(I * pv) + div / 2) * E2
        for j in range(3):
            Ld += I / 4 * curl[j] * SIG[j]
        res = (e1[1] + V**2 * Ld).applyfunc(sp.expand)
        sol = sp.solve([x for x in res if x != 0], cs, dict=True)
        ok &= len(sol) == 1
        csol = sol[0][cs] if sol else None
    check("O3b", ok, f"the t=1 O(a) term equals -v^2 L_(delta u), delta u_j = c d_j u_j with c = {csol}: a half-bond shift of where "
          "the bond field is placed (one-sided relabelling), the fermionic analogue of B14-check caveat 2")


def doublers():
    Bh = bracket(mats=SIG, v=V, wa=HALF, wb=HALF)
    ok = True
    ok2 = True
    for flip in product((1, -1), repeat=3):
        if flip == (1, 1, 1):
            continue
        sigp = [flip[j] * SIG[j] for j in range(3)]
        nflip = sum(1 for f in flip if f == -1)
        tau = [(-1 if nflip % 2 else 1) * s for s in sigp]  # proper (orientation-preserving) set
        # exact: staggering = P_j -> -P_j equals the bracket with sigma'
        Bp = bracket(mats=sigp, v=V, wa=HALF, wb=HALF)
        for (K, p) in PTS[:1]:
            ed = expand_a(Bh, K, p, 2, flip=flip)
            ep = expand_a(Bp, K, p, 2)
            ok &= all(is_zero(ed[n] - ep[n]) for n in ed)
            ok &= is_zero(ed[0] - kosmann(K, p, V, tau)) and is_zero(ed[1])
            ok2 &= not is_zero(ed[0] - kosmann(K, p, V, SIG))
    check("O5", ok, "all 7 doublers (P_j -> -P_j): bracket = bracket with sigma' = (+-sigma^j) exactly; leading order -v^2 L_w "
          "with the doubler's own proper spin set tau (sigma' or -sigma'), O(a) = 0: same v^2 for every doubler")
    check("O5b", ok2, "but tau != sigma: at every doubler the O(a^0) spin term differs from an on-site (i/4)(curl xi).sigma "
          "relabelling; a lattice G_f must carry momentum-dependent spin structure (e.g. via cos(a p_j)) to close on doublers")


def dirac():
    m = sp.Rational(13, 10)
    ok_eq = True
    for (wa, wb) in ((HALF, HALF),):
        Bd = bracket(mats=ALP, v=V, wa=wa, wb=wb, beta=BET, mass=m, dim=4)
        Bw = bracket(mats=SIG, v=V, wa=wa, wb=wb)
        ex = {e: sp.kronecker_product(E2, M) for e, M in Bw.items()}
        # mass-only terms carry power 0/1 tags; compare after merging tags into exponent-free form
        def untag(D):
            out = {}
            for e, M in D.items():
                madd(out, e[:9], M)
            return clean(out)
        ok_eq &= untag(Bd) == untag(ex)
    check("O6", ok_eq, "naive Dirac + on-site mass m N beta, endpoint mean: exact symbol identity [h_N,h_M] = 1_2 (x) [Weyl bracket]: mass drops out exactly")
    # general timing: mass cross terms
    t = sp.Symbol("t")
    Bd = bracket(mats=ALP, v=V, wa=t, wb=1 - t, beta=BET, mass=m, dim=4)
    Bw = bracket(mats=ALP, v=V, wa=t, wb=1 - t, dim=4)
    cross = osub(Bd, Bw)
    # exact form check: cross symbol == sum_j (X_j - Y_j) g_j(XY,P)?  (Y = Z/X; only X^{+-1} with relation)
    G = {}
    for e, M in cross.items():
        ex = tuple(e[j] - e[3 + j] for j in range(3)); rest = tuple(e[3:9]) + (e[9],)
        G.setdefault(ex, {}); madd(G[ex], rest, M)
    G = {k: clean(D) for k, D in G.items() if clean(D)}
    units = {tuple((1 if i == j else 0) * s for i in range(3)) for j in range(3) for s in (1, -1)}
    form_ok = set(G) <= units
    for j in range(3):
        up = tuple(1 if i == j else 0 for i in range(3)); dn = tuple(-1 if i == j else 0 for i in range(3))
        sh = {}
        for ee, M in G.get(up, {}).items():
            e2 = list(ee); e2[j] += 1; madd(sh, tuple(e2), -M)
        form_ok &= clean(sh) == G.get(dn, {})
    vanish = {tv: not clean({e: M.subs(t, tv) for e, M in cross.items()}) for tv in (0, sp.Rational(1, 4), HALF, 1)}
    odd = all(is_zero(even_part(M.subs(t, 0))) for M in cross.values()) and any(clifford_odd(M.subs(t, 0)) for M in cross.values())
    check("O7", vanish == {0: False, sp.Rational(1, 4): False, HALF: True, 1: False} and form_ok and odd,
          f"Dirac mass cross terms: vanish iff t = 1/2 ({vanish}); for t != 1/2 they are EXACTLY of the form "
          "sum_j xi~_j g_j (gravity's nn bond field, prop. (2t-1)) with Clifford-odd g_j (alpha beta type): an obstruction only "
          "relative to a Clifford-even (Kosmann-class) G_f; a G_f with an m-dependent alpha^j beta term would absorb them exactly")
    # Wilson
    Bwil = bracket(mats=ALP, v=V, wa=HALF, wb=HALF, beta=BET, r=1, dim=4)
    okw = True; oklin = True; okobs = True; okodd = True
    for (K, p) in PTS[:1]:
        e = expand_a(Bwil, K, p, 2)
        okw &= is_zero(e[0] - kosmann(K, p, V, SIG, dim=4)) and not is_zero(e[1])
        okodd &= clifford_odd(e[1])
        oklin &= is_zero(nonlinear_part(e[1]))
        okobs &= not is_zero(nonlinear_part(e[2] + g0_cubic(e[0])))
    check("O8", okw and okodd and oklin,
          "Dirac + Wilson (r=1, endpoint mean): O(a^0) = Kosmann; O(a) term nonzero and Clifford-odd (obstruction for a "
          "Kosmann-class G_f) BUT linear in kappa: absorbable at O(a) by a G_f with a Clifford-odd (beta-type) O(a) correction")
    check("O8b", okobs, "Dirac + Wilson: O(a^2) part non-absorbable by any translation-covariant G_f")


# ------------------------------------------------------------------ position space: gravity kernel, general linear G_f
def gravity_kernel(L):
    S = list(product(range(L), repeat=3)); SI = {x: i for i, x in enumerate(S)}
    PAIRS = [(0, 1), (0, 2), (1, 2)]
    def sh(x, j, s=1):
        y = list(x); y[j] = (y[j] + s) % L; return tuple(y)
    nb = 3 * len(S)
    rows = []
    for x in S:   # diag h_jj(x) = 2 (xi(x,j) - xi(x-e_j,j))   (B14 convention)
        for j in range(3):
            r = np.zeros(nb); r[3 * SI[x] + j] += 2; r[3 * SI[sh(x, j, -1)] + j] -= 2; rows.append(r)
        for (i, j) in PAIRS:  # face (x,ij): xi(x+e_i,j) - xi(x,j) + xi(x+e_j,i) - xi(x,i)
            r = np.zeros(nb)
            r[3 * SI[sh(x, i)] + j] += 1; r[3 * SI[x] + j] -= 1; r[3 * SI[sh(x, j)] + i] += 1; r[3 * SI[x] + i] -= 1
            rows.append(r)
    Mx = np.array(rows)
    return nb - np.linalg.matrix_rank(Mx)


def general_linear_nogo(L, wa, wb):
    """B(delta_z, delta_{z+d}) for all z and the non-nn d with xi_g = 0 must lie in span{G_f[kappa]} (dim <= 3)."""
    S = list(product(range(L), repeat=3)); SI = {x: i for i, x in enumerate(S)}
    n = len(S)
    sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    def sh(x, d):
        return tuple((x[i] + d[i]) % L for i in range(3))
    def hop(lap):
        Hm = np.zeros((2 * n, 2 * n), complex)
        for x in S:
            for j in range(3):
                e = tuple(1 if i == j else 0 for i in range(3)); y = sh(x, e)
                w = wa * lap.get(x, 0) + wb * lap.get(y, 0)
                if w:
                    a_, b_ = 2 * SI[x], 2 * SI[y]
                    Hm[a_:a_ + 2, b_:b_ + 2] += (-0.5j) * w * sig[j]
                    Hm[b_:b_ + 2, a_:a_ + 2] += (0.5j) * w * sig[j]
        return Hm
    vecs = []
    ds = [(2, 0, 0), (0, 2, 0), (0, 0, 2)] if wa == wb else [(1, -1, 0), (0, 1, -1), (1, 0, -1)]
    for z in S[: n // 2]:
        for d in ds:
            hn, hm = hop({z: 1.0}), hop({sh(z, d): 1.0})
            vecs.append((hn @ hm - hm @ hn).ravel())
    Vm = np.array(vecs)
    return len(vecs), np.linalg.matrix_rank(Vm, tol=1e-9)


if __name__ == "__main__":
    weyl_orders()
    weyl_O1_structure()
    doublers()
    dirac()
    ks = {L: gravity_kernel(L) for L in (3, 4, 5)}
    check("K1", all(k == 3 for k in ks.values()), f"gravity relabelling kernel dimension {ks} (B14 G_g convention, own build); "
          "symbol argument: (1 - e^{-iK_j}) xi_j = 0 and faces force xi = 0 unless K = 0, so ker = constants for every L")
    for (wa, wb, lbl) in ((0.5, 0.5, "endpoint mean, d = 2e_j"), (1.0, 0.0, "one-endpoint, d = e_j - e_k")):
        nv, rk = general_linear_nogo(5, wa, wb)
        check("K2" + ("a" if wa == wb else "b"), rk == nv and rk > 3,
              f"L=5, {lbl}: {nv} lapse pairs with xi_g = 0 give brackets of rank {rk} > 3 = dim of G_f[constants] for ANY "
              "linear G_f (no translation covariance, any range): exact closure impossible for every linear G_f")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")

#!/usr/bin/env python3
"""check.py -- same-family referee of block 161 T4 (links carrying the lengths' connection add (1/8) eps.C)
and block 159 T4 (relabelling consistency and the curvature member's jet).  Exact arithmetic throughout:
sympy / Fractions for every finite claim; linear-algebra ranks are computed modulo the prime 2^31-1
(rank mod p <= rank over Q, so full rank mod p proves full rank over Q).
Sources (pushed branches, read-only): origin/physics-loop/admissibility-induced-law-block161-... and block159-...
"""
import itertools
import random
from fractions import Fraction
import numpy as np
import sympy as sp
from sympy import Matrix, Rational as Rt, I, eye, zeros, symbols, LeviCivita, Function, diff, exp

import random
import sympy as sp
from sympy import Matrix, Rational as Rt, I, eye, zeros, symbols, LeviCivita

sig = [Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]
ID2 = eye(2)


def sdot(v):
    return sum((v[a] * sig[a] for a in range(3)), zeros(2, 2))


def rnd_rat(rng, lo=-5, hi=5, den=7):
    return Rt(rng.randint(lo, hi), rng.randint(1, den))


def frame_data(rng, near_identity=False, symmetric=False):
    """Em[j,a]=E^j_a (3x3), dE[k] = d_k E (3 matrices). Exact rationals."""
    while True:
        if near_identity:
            Em = eye(3) + Matrix(3, 3, lambda i, j: rnd_rat(rng, -2, 2, 5) / 5)
        else:
            Em = Matrix(3, 3, lambda i, j: rnd_rat(rng))
        if symmetric:
            Em = (Em + Em.T) / 2
        if Em.det() != 0:
            break
    dE = []
    for k in range(3):
        D = Matrix(3, 3, lambda i, j: rnd_rat(rng))
        if symmetric:
            D = (D + D.T) / 2
        dE.append(D)
    return Em, dE


def geometry(Em, dE):
    """e (co-frame e^a_k), d_k e, g, d_k g, g^-1, Gamma^k_{jl}, omega_{j a b}."""
    e = Em.inv()                      # sum_k e[a,k] E[k,b] = delta_ab
    de = [-(e * dE[k] * e) for k in range(3)]
    g = e.T * e
    dg = [de[k].T * e + e.T * de[k] for k in range(3)]
    ginv = g.inv()
    Gam = [[[sum(ginv[k, m] * (dg[j][m, l] + dg[l][m, j] - dg[m][j, l]) for m in range(3)) / 2
             for l in range(3)] for j in range(3)] for k in range(3)]
    om = [[[sum(e[a, k] * (dE[j][k, b] + sum(Gam[k][j][l] * Em[l, b] for l in range(3)))
                for k in range(3)) for b in range(3)] for a in range(3)] for j in range(3)]
    return e, de, g, dg, ginv, Gam, om


def eps_dot_C(Em, de):
    """epsilon.C = eps^{abc} E^i_b E^j_c (d_i e^a_j - d_j e^a_i)   (block 158 definition)."""
    s = 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                lc = LeviCivita(a, b, c)
                if lc == 0:
                    continue
                for i in range(3):
                    for j in range(3):
                        s += lc * Em[i, b] * Em[j, c] * (de[i][a, j] - de[j][a, i])
    return s


def link_angles(om):
    """a_{j,c} = 1/2 eps_{cab} omega_{jab}"""
    return [[sum(LeviCivita(c, a, b) * om[j][a][b] for a in range(3) for b in range(3)) / 2
             for c in range(3)] for j in range(3)]


def comparator_minus_framed(Em, dE):
    """Return (Q - Qf), H_c psi = -i s_a E^j_a d_j psi + Q psi, H_f psi = -i s_a E^j_a d_j psi + Qf psi."""
    e, de, g, dg, ginv, Gam, om = geometry(Em, dE)
    dlogg = [sum(ginv[l, m] * dg[j][l, m] for l in range(3) for m in range(3)) for j in range(3)]
    Gspin = []
    for j in range(3):
        M = zeros(2, 2)
        for a in range(3):
            for b in range(3):
                M += Rt(1, 8) * om[j][a][b] * (sig[a] * sig[b] - sig[b] * sig[a])
        Gspin.append(M)
    Q = zeros(2, 2)
    for j in range(3):
        for a in range(3):
            Q += -I * Em[j, a] * sig[a] * (Gspin[j] - Rt(1, 4) * dlogg[j] * ID2)
    Qf = zeros(2, 2)
    for a in range(3):
        Qf += -I / 2 * sum(dE[j][j, a] for j in range(3)) * sig[a]
    return (Q - Qf).applyfunc(sp.nsimplify), Q, Qf, (e, de, om)


EPS = symbols('eps', real=True)


def lattice_operator_order1(Em, dE, a_links):
    """First-order continuum limit of the lattice walk with links.

    (H psi)(x) = sum_j (1/2i) [ B+ psi(x+eps e_j) - B-^dagger psi(x-eps e_j) ] / eps,
    B+ = 1/2 (E^j(x).s W + W E^j(x+eps e_j).s),  B- = 1/2 (E^j(x-eps e_j).s W + W E^j(x).s),
    W = 1 + (i/2) eps a_j.s   (the O(eps^2) part of W cannot enter the eps^1 coefficient).
    Returns (P[j] multiplying d_j psi, Q multiplying psi(0)) of the eps^1 coefficient, and the eps^0 part.
    """
    eps = EPS
    u = symbols('u0 u1')
    uj = [symbols('v%d_0 v%d_1' % (j, j)) for j in range(3)]
    psi0 = Matrix(u)
    psij = [Matrix(x) for x in uj]

    def Evec(j, shift):  # E^j(x + shift*eps*e_j).sigma  (only d_j E^j enters at this order)
        v = [Em[j, a] + shift * eps * dE[j][j, a] for a in range(3)]
        return sdot(v)

    res = zeros(2, 1)
    for j in range(3):
        aj = a_links[j]
        W = ID2 + I / 2 * eps * sdot(aj)
        Bp = (Evec(j, 0) * W + W * Evec(j, 1)) / 2
        Bm = (Evec(j, -1) * W + W * Evec(j, 0)) / 2
        Bmd = Bm.H
        br = Bp * (psi0 + eps * psij[j]) - Bmd * (psi0 - eps * psij[j])
        res += (1 / (2 * I)) * br
    res = res.applyfunc(sp.expand)
    c1 = res.applyfunc(lambda x: x.coeff(eps, 1))
    c0 = res.applyfunc(lambda x: x.coeff(eps, 0))
    P = [Matrix(2, 2, lambda r, c: sp.diff(c1[r], uj[j][c])) for j in range(3)]
    Q = Matrix(2, 2, lambda r, c: sp.diff(c1[r], u[c]))
    return P, Q, c0



import itertools
import random
from fractions import Fraction
import numpy as np
import sympy as sp
from sympy import Rational as Rt, symbols, Function, Matrix, diff, exp, I

T, X, Y, Z = symbols('t x y z', real=True)
COORDS = [T, X, Y, Z]


# ---------------------------------------------------------------- B1: static comparator density
def conformal_density_identity():
    """N sqrt(g) R for g = e^{2 lam} delta, N = e^u  ==  -4 div(e^{u+lam} grad lam)
       + 4 e^u [ e^lam grad u.grad lam + (e^lam/2) |grad lam|^2 ]   (exact, generic functions)."""
    x = [X, Y, Z]
    lam = Function('lam')(*x)
    u = Function('u')(*x)
    g = sp.diag(*[exp(2 * lam)] * 3)
    ginv = g.inv()
    n = 3
    Gam = [[[sum(ginv[k, m] * (diff(g[m, j], x[l]) + diff(g[m, l], x[j]) - diff(g[j, l], x[m]))
                 for m in range(n)) / 2 for l in range(n)] for j in range(n)] for k in range(n)]

    def Ric(j, l):
        s = 0
        for k in range(n):
            s += diff(Gam[k][j][l], x[k]) - diff(Gam[k][j][k], x[l])
            for m in range(n):
                s += Gam[k][k][m] * Gam[m][j][l] - Gam[k][l][m] * Gam[m][j][k]
        return s

    R = sum(ginv[j, l] * Ric(j, l) for j in range(n) for l in range(n))
    sqrtg = exp(3 * lam)
    lhs = exp(u) * sqrtg * R
    grad = lambda f: [diff(f, xi) for xi in x]
    div = lambda v: sum(diff(v[i], x[i]) for i in range(n))
    dl, du = grad(lam), grad(u)
    rhs = (-4 * div([exp(u + lam) * c for c in dl])
           + 4 * exp(u) * (exp(lam) * sum(du[i] * dl[i] for i in range(n))
                            + exp(lam) / 2 * sum(c * c for c in dl)))
    return sp.simplify(lhs - rhs) == 0


# ---------------------------------------------------------------- the quadratic action S2
def build_S2():
    """Return fields, Lagrangian density L2 = 1/4[tr Hd^2 - (tr Hd)^2] + n R1 + R2 (block 157's S2),
    with R1 = d_i d_j h_ij - Lap tr h, R2 = Fierz-Pauli form fixed below."""
    names_h = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    fh = {p: Function('h%d%d' % (p[0] + 1, p[1] + 1))(*COORDS) for p in names_h}
    fN = [Function('N%d' % (i + 1))(*COORDS) for i in range(3)]
    fn = Function('n')(*COORDS)
    h = Matrix(3, 3, lambda i, j: fh[(min(i, j), max(i, j))])
    sp_x = [X, Y, Z]
    d = lambda f, i: diff(f, sp_x[i])
    trh = sum(h[i, i] for i in range(3))
    R1 = sum(d(d(h[i, j], i), j) for i in range(3) for j in range(3)) - sum(d(d(trh, i), i) for i in range(3))
    # Fierz-Pauli quadratic part of sqrt(gamma) R (static; modulo total derivatives)
    R2 = (-Rt(1, 4) * sum(d(h[i, j], k) ** 2 for i in range(3) for j in range(3) for k in range(3))
          + Rt(1, 2) * sum(d(h[i, j], i) * d(h[k, j], k) for i in range(3) for j in range(3) for k in range(3))
          - Rt(1, 2) * sum(d(h[i, j], i) * d(trh, j) for i in range(3) for j in range(3))
          + Rt(1, 4) * sum(d(trh, k) ** 2 for k in range(3)))
    Hd = Matrix(3, 3, lambda i, j: diff(h[i, j], T) - d(fN[i], j) - d(fN[j], i))
    trHd = sum(Hd[i, i] for i in range(3))
    kin = Rt(1, 4) * (sum(Hd[i, j] * Hd[j, i] for i in range(3) for j in range(3)) - trHd ** 2)
    L2 = kin + fn * R1 + R2
    fields = [fh[p] for p in names_h] + fN + [fn]
    return fields, L2, h, fN, fn, names_h, R1, R2


def euler_ops(fields, L):
    """Euler-Lagrange expressions E_A = delta S / delta phi_A for a Lagrangian with up to 2nd derivatives."""
    out = []
    for f in fields:
        e = diff(L, f)
        for c in COORDS:
            e -= diff(diff(L, diff(f, c)), c)
        # second-derivative terms
        for c1, c2 in itertools.combinations_with_replacement(range(4), 2):
            dd = diff(f, COORDS[c1], COORDS[c2])
            e += diff(diff(L, dd), COORDS[c1], COORDS[c2])
        out.append(sp.expand(e))
    return out


def gauge_vars():
    xi = [Function('xi%d' % (i + 1))(*COORDS) for i in range(3)]
    xi0 = Function('xi0')(*COORDS)
    return xi, xi0


def gauge_variation(names_h, xi, xi0):
    """delta phi_A for spatial relabelling xi^i and time relabelling xi0 (block 157's linear laws)."""
    sx = [X, Y, Z]
    dh = [diff(xi[q], sx[p]) + diff(xi[p], sx[q]) for (p, q) in names_h]
    dN = [diff(xi[i], T) - diff(xi0, sx[i]) for i in range(3)]
    dn = [diff(xi0, T)]
    return dh + dN + dn


def symbol_matrices(fields, E):
    """Symbol Ehat_AB(p): E_A applied to plane waves c_B e^{i p.x} (p_mu, mu=0 time). Real (i^2=-1 kept)."""
    p = symbols('p0:4', real=True)
    cs = symbols('c0:10')
    pw = exp(I * sum(p[m] * COORDS[m] for m in range(4)))
    subs = {fields[B]: cs[B] * pw for B in range(10)}
    Eh = sp.zeros(10, 10)
    for A in range(10):
        ex = E[A].subs(subs).doit()
        ex = sp.expand(sp.simplify(ex / pw))
        for B in range(10):
            Eh[A, B] = sp.expand(ex.coeff(cs[B]))
    return Eh, p


def gauge_symbol(names_h):
    """Lam_{B,mu}(r): delta phi_B = i * Lam(r) xi   (i dropped); parameter order (xi1,xi2,xi3,xi0)."""
    r = symbols('r0:4', real=True)
    Lam = sp.zeros(10, 4)
    for k, (pq) in enumerate(names_h):
        pp, qq = pq
        # delta h_pq = d_p xi_q + d_q xi_p
        Lam[k, qq] += r[pp + 1]
        Lam[k, pp] += r[qq + 1]
    for i in range(3):
        Lam[6 + i, i] += r[0]          # N_i : d_t xi_i
        Lam[6 + i, 3] += -r[i + 1]     # N_i : - d_i xi0
    Lam[9, 3] += r[0]                  # n : d_t xi0
    return Lam, r



import random
from fractions import Fraction
import numpy as np
import sympy as sp


PRIME = 2147483647


def poly_table(M, vars_):
    """sympy matrix of polynomials -> list of lists of (Fraction coeff, exponent tuple) terms."""
    out = []
    for i in range(M.rows):
        row = []
        for j in range(M.cols):
            e = sp.expand(M[i, j])
            if e == 0:
                row.append([])
                continue
            P = sp.Poly(e, *vars_)
            row.append([(Fraction(int(c.p), int(c.q)), mon) for mon, c in P.terms()])
        out.append(row)
    return out


def eval_table(tab, vals):
    rows = len(tab)
    cols = len(tab[0])
    out = [[Fraction(0)] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            s = Fraction(0)
            for c, mon in tab[i][j]:
                t = c
                for v, k in zip(vals, mon):
                    if k:
                        t *= v ** k
                s += t
            out[i][j] = s
    return out


def matvec(Mx, v):
    return [sum(Mx[i][j] * v[j] for j in range(len(v))) for i in range(len(Mx))]


def modp(fr):
    return (fr.numerator % PRIME) * pow(fr.denominator % PRIME, PRIME - 2, PRIME) % PRIME


def rank_mod_p(rows):
    A = np.array(rows, dtype=np.int64) % PRIME
    nr, nc = A.shape
    rk = 0
    for c in range(nc):
        nzr = np.nonzero(A[rk:, c])[0]
        if nzr.size == 0:
            continue
        piv = rk + int(nzr[0])
        if piv != rk:
            A[[rk, piv]] = A[[piv, rk]]
        inv = pow(int(A[rk, c]), PRIME - 2, PRIME)
        A[rk] = (A[rk] * inv) % PRIME
        col = A[:, c].copy()
        col[rk] = 0
        idx = np.nonzero(col)[0]
        if idx.size:
            A[idx] = (A[idx] - np.outer(col[idx], A[rk])) % PRIME
        rk += 1
        if rk == nr:
            break
    return rk


PAIRS = [(B, C) for B in range(10) for C in range(B, 10)]      # 55 monomials
COLS = [(A, k) for A in range(10) for k in range(len(PAIRS))]    # 550 unknowns


def sample_row(Eh_tab, Lam_tab, pv, qv, a, b, xi, rng):
    """One linear equation in the 550 unknown F-coefficients: E.F'Lambda (momentum space) = 0."""
    rv = [-(pv[m] + qv[m]) for m in range(4)]
    Ep = eval_table(Eh_tab, pv)
    Eq = eval_table(Eh_tab, qv)
    Lr = eval_table(Lam_tab, rv)
    Ea = matvec(Ep, a)
    Eb = matvec(Eq, b)
    ell = matvec(Lr, xi)
    row = []
    for A in range(10):
        for (B, C) in PAIRS:
            if B == C:
                val = 2 * (Ea[A] * b[B] * ell[B] + Eb[A] * a[B] * ell[B])
            else:
                val = Ea[A] * (b[C] * ell[B] + b[B] * ell[C]) + Eb[A] * (a[C] * ell[B] + a[B] * ell[C])
            row.append(modp(Fraction(val)))
    return row


def build_symbols():
    fields, L2, h, fN, fn, names_h, R1, R2 = build_S2()
    E = euler_ops(fields, L2)
    Eh, p = symbol_matrices(fields, E)
    Lam, r = gauge_symbol(names_h)
    return Eh, p, Lam, r, names_h, (fields, L2, E)


# =====================================================================================================
# MAIN
# =====================================================================================================
import sys
import time as _time

_T0 = _time.time()
RESULTS = []


def check(name, cond, detail=''):
    ok = bool(cond)
    RESULTS.append(ok)
    print(('PASS ' if ok else 'FAIL ') + name + (('  [' + detail + ']') if detail else ''), flush=True)
    return ok


def zero2(M):
    return M.applyfunc(lambda z: sp.nsimplify(sp.expand(z))) == sp.zeros(2, 2)


def part_A():
    print('--- Part A: block 161 T4 (links carrying the lengths connection) ---', flush=True)
    # A1: the algebra of the bond:  1/2 (E.s (i/2)a.s + (i/2) a.s E.s) = (i/2)(E.a) 1   (E_x = E_y)
    Es = sp.symbols('E0:3'); As = sp.symbols('a0:3')
    lhs = (sdot(Es) * (I / 2) * sdot(As) + (I / 2) * sdot(As) * sdot(Es)) / 2
    rhs = (I / 2) * sum(Es[k] * As[k] for k in range(3)) * ID2
    check('A1 bond algebra: 1/2(E.s W1 + W1 E.s) with W1=(i/2)a.s equals (i/2)(E.a) times identity', (lhs - rhs).applyfunc(sp.expand) == sp.zeros(2, 2))

    # exact frames: general (large strain, non-symmetric) and symmetric near-identity (the lengths' frame)
    rng = random.Random(20260926)
    frames = [('general', frame_data(rng)) for _ in range(5)]
    frames += [('symmetric near-identity', frame_data(rng, near_identity=True, symmetric=True)) for _ in range(3)]
    a2 = a3 = a4 = a5 = a6 = a7 = a8 = True
    detail = []
    for tag, (Em, dE) in frames:
        dQ, Q, Qf, (e, de, om) = comparator_minus_framed(Em, dE)
        ec = eps_dot_C(Em, de)
        alinks = link_angles(om)
        scal = sum(Em[j, c] * alinks[j][c] for j in range(3) for c in range(3)) / 2
        Pw, Qw, c0w = lattice_operator_order1(Em, dE, alinks)
        P0, Q0, c00 = lattice_operator_order1(Em, dE, [[0, 0, 0]] * 3)
        Pm, Qm, _ = lattice_operator_order1(Em, dE, [[-x for x in row] for row in alinks])
        Pc = [sum((-I * Em[j, aa] * sig[aa] for aa in range(3)), sp.zeros(2, 2)) for j in range(3)]
        # A2: no links: lattice limit is the framed walk H_f
        a2 = a2 and all((P0[j] - Pc[j]).applyfunc(sp.expand) == sp.zeros(2, 2) for j in range(3)) \
            and (Q0 - Qf).applyfunc(sp.expand) == sp.zeros(2, 2) and c00 == sp.zeros(2, 1)
        # A3: links add exactly (1/2) sum_j E^j.a_j times the identity (no coin-vector part, no principal part)
        a3 = a3 and all((Pw[j] - P0[j]).applyfunc(sp.expand) == sp.zeros(2, 2) for j in range(3)) \
            and (Qw - Q0 - scal * ID2).applyfunc(sp.expand) == sp.zeros(2, 2)
        # A4: (1/2) sum_j E^j.a_j = (1/8) eps.C   exactly
        a4 = a4 and sp.nsimplify(scal - ec / 8) == 0
        # A5: comparator minus framed walk = (1/8) eps.C times identity (exact, generic frame)
        a5 = a5 and (dQ - ec / 8 * ID2).applyfunc(sp.nsimplify) == sp.zeros(2, 2)
        # A6: the lattice walk with these links has the comparator's first-order operator exactly
        a6 = a6 and (Qw - Q).applyfunc(sp.expand) == sp.zeros(2, 2) and all((Pw[j] - Pc[j]).applyfunc(sp.expand) == sp.zeros(2, 2) for j in range(3))
        # A7: control: reversed orientation of the links gives the opposite scalar, so it misses by -eps.C/4
        a7 = a7 and (Qm - Q + (ec / 4) * ID2).applyfunc(sp.expand) == sp.zeros(2, 2)
        # A8: control: eps.C is nonzero on these frames except the lengths' frame at first order
        a8 = a8 and (ec != 0)
        detail.append('%s epsC/8=%s' % (tag, sp.nsimplify(ec / 8)))
    check('A2 lattice walk without links -> framed walk H_f = -i s_a E^j_a d_j - (i/2)(d_j E^j_a) s_a (8 exact frames)', a2)
    check('A3 links W=1+(i/2)eps a_j.s add exactly (1/2) sum_j E^j.a_j times identity: scalar only (8 exact frames)', a3)
    check('A4 with a_{j,c} = (1/2) eps_cab omega_jab: (1/2) sum_j E^j.a_j = (1/4) eps_abc omega_abc = (1/8) eps.C, exactly (any strain)', a4, '; '.join(detail[:2]))
    check('A5 comparator H_c = g^{1/4}[-i s_a E^j_a (d_j + Gamma_j)]g^{-1/4} equals H_f + (1/8) eps.C times identity, exactly (any strain)', a5)
    check('A6 the lattice walk with the connection links has exactly the comparator\'s first-order operator (8 exact frames)', a6)
    check('A7 control: reversed link orientation misses the comparator by -(1/4) eps.C (sign is load-bearing)', a7)
    check('A8 control: eps.C != 0 on every tested frame, so the no-link walk does miss (frames are not degenerate)', a8)

    # A9: lengths' frame e = 1 + t*eta (eta symmetric): eps.C = 0 at O(t), = B := 2 eps_abc eta_ad d_b eta_cd at O(t^2)
    t = sp.symbols('t')
    s = {}
    eta0 = Matrix(3, 3, lambda i, j: sp.Symbol('s%d%d' % (min(i, j), max(i, j))))
    deta = [Matrix(3, 3, lambda i, j, k=k: sp.Symbol('d%d_%d%d' % (k, min(i, j), max(i, j)))) for k in range(3)]
    E0 = (eye(3) + t * eta0).inv()
    E0 = E0.applyfunc(lambda z: sp.series(z, t, 0, 3).removeO())
    de = [t * deta[k] for k in range(3)]                       # d_k e^a_j
    ecC = 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                lc = LeviCivita(a, b, c)
                if lc == 0:
                    continue
                for i in range(3):
                    for j in range(3):
                        ecC += lc * E0[i, b] * E0[j, c] * (de[i][a, j] - de[j][a, i])
    ecC = sp.expand(ecC)
    c1 = sp.expand(ecC.coeff(t, 1)); c2 = sp.expand(ecC.coeff(t, 2))
    Bq = sum(2 * LeviCivita(a, b, c) * eta0[a, d] * deta[b][c, d] for a in range(3) for b in range(3) for c in range(3) for d in range(3))
    check('A9 lengths\' frame (symmetric strain): eps.C vanishes at first order and equals 2 eps_abc eta_ad d_b eta_cd at second', c1 == 0 and sp.expand(c2 - Bq) == 0)


def part_B_identities():
    print('--- Part B: block 159 T4 identities ---', flush=True)
    check('B1 N sqrt(g) R for g=e^{2 lam}delta, N=e^u equals -4 div(e^{u+lam} grad lam) + 4 e^u [e^lam grad u.grad lam + (e^lam/2)|grad lam|^2], generic functions', conformal_density_identity())
    # B2: the family jets: A=e^lam, C=e^lam/2, D=0  and block 60's curvature member written in (u, lam)
    lam, u, k = sp.symbols('lam u k')
    Afun, Cfun = sp.exp(lam), sp.exp(lam) / 2
    A0, A1 = Afun.subs(lam, 0), sp.diff(Afun, lam).subs(lam, 0)
    C0, C1 = Cfun.subs(lam, 0), sp.diff(Cfun, lam).subs(lam, 0)
    check('B2 comparator static density has jets A(0)=1,C(0)=1/2,D(0)=0 and (A1,C1,D1)=(1,1/2,0); it lies on the plane 4A1-2C1-6D1=3',
          (A0, C0, A1, C1) == (1, Rt(1, 2), 1, Rt(1, 2)) and 4 * A1 - 2 * C1 - 6 * 0 == 3)
    # B2b: block 60's landed curvature member F=-8K sum (N_y-N_x)(chi_y-chi_x), N=w chi, chi=sqrt(l): long-wave form
    #      -8K grad N.grad chi with chi=e^{lam/2}, w=e^u equals -4K e^u [e^lam grad u.grad lam + (e^lam/2)|grad lam|^2]
    #      (1-D representative: gradients -> d/dx of profiles)
    xx = sp.symbols('xx'); lf = Function('lf')(xx); uf = Function('uf')(xx)
    chi = sp.exp(lf / 2); Nn = sp.exp(uf) * chi
    block60 = -8 * sp.diff(Nn, xx) * sp.diff(chi, xx)
    fam = -4 * sp.exp(uf) * (sp.exp(lf) * sp.diff(uf, xx) * sp.diff(lf, xx) + sp.exp(lf) / 2 * sp.diff(lf, xx) ** 2)
    check('B2b block 60 curvature member (landed form) = family with A=e^lam, C=e^lam/2, D=0 at K_family=4K, pointwise', sp.simplify(block60 - fam) == 0)


def dictionary_dependence():
    print('--- Part B7: dictionary dependence of the third-order jet ---', flush=True)
    x = sp.symbols('x'); c1, c2 = sp.symbols('c1 c2')
    mu = Function('mu')(x); v = Function('v')(x)
    lam_ = mu + c1 * mu ** 2          # lengths field redefinition (zero derivatives, quadratic)
    u_ = v + c2 * mu ** 2             # rates field redefinition that keeps weight one (v -> v + const is still a symmetry)
    Lag = exp(u_) * (exp(lam_) * diff(u_, x) * diff(lam_, x) + exp(lam_) / 2 * diff(lam_, x) ** 2)
    Lq = sp.expand(sp.simplify(Lag * exp(-v)))
    vp, mp, M = sp.symbols('vp mp M')
    Lq = sp.expand(Lq.subs({diff(v, x): vp, diff(mu, x): mp}).subs(mu, M))
    A = sp.expand(Lq.coeff(vp, 1).coeff(mp, 1)); Cc = sp.expand(Lq.coeff(vp, 0).coeff(mp, 2)); D = sp.expand(Lq.coeff(vp, 2).coeff(mp, 0))
    A1 = sp.diff(A, M).subs(M, 0); C1 = sp.diff(Cc, M).subs(M, 0); D1 = sp.diff(D, M).subs(M, 0)
    ok0 = (A.subs(M, 0) == 1) and (Cc.subs(M, 0) == Rt(1, 2)) and (D == 0)
    check('B7a after the redefinition lam=mu+c1 mu^2, u=v+c2 mu^2 the density is again of the weight-one family with A(0)=1,C(0)=1/2,D=0', ok0)
    check('B7b its jets are (A1,C1,D1) = (1+2 c1, 1/2+2 c1+2 c2, 0): the third-order jet is NOT invariant under zero-derivative redefinitions', sp.expand(A1 - (1 + 2 * c1)) == 0 and sp.expand(C1 - (Rt(1, 2) + 2 * c1 + 2 * c2)) == 0 and D1 == 0)
    P = sp.expand(4 * A1 - 2 * C1 - 6 * D1)
    check('B7c the bend plane value 4A1-2C1-6D1 becomes 3+4(c1-c2): redefinitions with c1 = c2 slide along the plane, so the plane does not select the point', sp.expand(P - (3 + 4 * (c1 - c2))) == 0)
    # the map (c1,c2) -> (A1,C1) is invertible: every (A1,C1,0) jet is a redefinition of the curvature member
    Jm = sp.Matrix([[2, 0], [2, 2]])
    check('B7d the map (c1,c2) -> (A1,C1) has determinant 4 != 0: every jet (A1,C1,0) is the curvature member in redefined variables', Jm.det() == 4)
    # a jet with D1 != 0 is not reachable
    check('B7e D1 stays 0 under these redefinitions (so D1 != 0 members are a different class)', D1 == 0)


# --------------------------------------------------------------------------- modular linear algebra
def part_B_lemmas():
    print('--- Part B3-B6: zero-derivative redefinitions, and strictly invariant redefinition vertices ---', flush=True)
    fields, L2, h, fN, fn, names_h, R1, R2 = build_S2()
    E = euler_ops(fields, L2)
    xi, xi0 = gauge_vars()
    dphi = gauge_variation(names_h, xi, xi0)
    noether = sp.expand(sum(E[A] * dphi[A] for A in range(10)))
    gp = list(xi) + [xi0]
    ok = True
    for q in gp:
        eq = diff(noether, q)
        for c in COORDS:
            eq -= diff(diff(noether, diff(q, c)), c)
        ok = ok and sp.expand(eq) == 0
    check('B5a S2 = 1/4[tr Hd^2-(tr Hd)^2] + n R1 + R2 (comparator\'s quadratic part, FP form of R2) is invariant under block 157\'s linear laws (symbolic, all 10 fields, 4 parameters)', ok)

    # negative control: flip the sign of n R1 (time-relabelling invariance ties n R1 to the kinetic term)
    Lbad = L2 - 2 * fn * R1
    Ebad = euler_ops(fields, Lbad)
    nb = sp.expand(sum(Ebad[A] * dphi[A] for A in range(10)))
    okb = True
    for q in gp:
        eq = diff(nb, q)
        for c in COORDS:
            eq -= diff(diff(nb, diff(q, c)), c)
        okb = okb and sp.expand(eq) == 0
    check('B5b control: with the sign of n R1 flipped the invariance FAILS (the test has power)', not okb)

    # normalisation of R2: fixed by the exact Ricci scalar of the conformally flat mode, not by gauge invariance
    lamf = Function('lamc')(X, Y, Z)
    conf = {fields[0]: 2 * lamf, fields[3]: 2 * lamf, fields[5]: 2 * lamf}
    zero_fields = {fields[1]: 0, fields[2]: 0, fields[4]: 0}
    R2c = R2.subs(conf).subs(zero_fields).doit()
    R1c = R1.subs(conf).subs(zero_fields).doit()
    # 2nd-order part of sqrt(g) R at h = (e^{2 lam} - 1) delta :  -(4 lam Lap lam + 2 |grad lam|^2)
    exact2 = -(4 * lamf * sum(diff(lamf, c, 2) for c in (X, Y, Z)) + 2 * sum(diff(lamf, c) ** 2 for c in (X, Y, Z)))

    def EL(Lg):
        e = diff(Lg, lamf)
        for c in (X, Y, Z):
            e -= diff(diff(Lg, diff(lamf, c)), c)
        for c1_, c2_ in itertools.combinations_with_replacement((X, Y, Z), 2):
            e += diff(diff(Lg, diff(lamf, c1_, c2_)), c1_, c2_)
        return sp.expand(e)
    check('B5e R2 at the conformal mode h=2 lam delta has the same Euler-Lagrange expression as the exact 2nd-order part of sqrt(g)R (fixes sign and scale of R2; the h->(e^{2lam}-1) nonlinearity enters only through the divergence R1)', sp.expand(EL(R2c) - EL(exact2)) == 0 and sp.expand(EL(R1c)) == 0)

    Eh, p = symbol_matrices(fields, E)
    Lam, r = gauge_symbol(names_h)
    Lp = Lam.subs({r[i]: p[i] for i in range(4)})
    check('B5c symbol of the linearised equations annihilates pure gauge (E(p) Lambda(p)=0), is symmetric and even in p', sp.expand(Eh * Lp) == sp.zeros(10, 4) and sp.expand(Eh - Eh.T) == sp.zeros(10, 10))
    rng0 = random.Random(3)
    vals = {p[i]: rng0.randint(1, 6) for i in range(4)}
    check('B5d the symbol E(p) has generic rank 6 = 10 fields - 4 gauge parameters', Eh.subs(vals).rank() == 6)

    Eh_tab = poly_table(Eh, p); Lam_tab = poly_table(Lam, r)
    rng = random.Random(5)

    def rv(n, lo=-4, hi=4):
        return [Fraction(rng.randint(lo, hi)) for _ in range(n)]

    def rows_for(kind, N):
        rows = []
        for _ in range(N):
            pv = rv(4); qv = rv(4)
            if kind == 'unif':
                qv = [qv[0]] + [-pv[1], -pv[2], -pv[3]]
            a = rv(10); b = rv(10)
            xi_ = rv(3) + [Fraction(0)] if kind == 'spatial' else [Fraction(0)] * 3 + rv(1)
            rows.append(sample_row(Eh_tab, Lam_tab, pv, qv, a, b, xi_, rng))
        return rows

    NS = 620
    Rs = rows_for('spatial', NS); Rtm = rows_for('time', NS); Ru = rows_for('unif', NS)
    kdim = lambda rows: 550 - rank_mod_p(rows)
    ks = kdim(Rs)
    # control: the spatial-only kernel is exactly the 10 redefinitions F_A = c_A n^2 (n is invariant under spatial relabellings)
    n2cols = [A * 55 + PAIRS.index((9, 9)) for A in range(10)]
    ker_ok = True
    for col in n2cols:
        vec = np.zeros(550, dtype=np.int64); vec[col] = 1
        res = (np.array(Rs, dtype=np.int64) @ vec) % PRIME
        ker_ok = ker_ok and not res.any()
    check('B6a spatial relabellings alone leave a kernel of dimension 10, exactly the redefinitions F_A = c_A n^2 (control: the rank test detects kernels and explains them)', ks == 10 and ker_ok, 'kernel dim %d' % ks)
    kall = kdim(Rs + Rtm)
    kun = kdim(Rs + Ru)
    check('B6b E.F\'Lambda = 0 (mod total derivatives) for ALL spatial and ALL time relabellings forces F = 0 over all 10 fields (rank 550 mod p, hence over Q)', kall == 0, 'kernel dim %d' % kall)
    check('B6c the same with relabellings in time only for spatially uniform clock profiles (xi0 = xi0(t))', kun == 0, 'kernel dim %d' % kun)

    # B3/B4: law-level statements with jets
    from_t4 = law_level_ranks()
    check('B3a field-level: a zero-derivative quadratic redefinition of (h,n) keeps the first-order laws only if F=0 (196 coefficients, rank 196)', from_t4['hn'] == 196)
    check('B3b same with the shift N_i included (550 coefficients, rank 550)', from_t4['all'] == 550)
    check('B4  even with field-dependent redefinitions of the gauge parameters xi -> xi + M(phi) xi (160 more coefficients), the laws are kept only if F=0 and M=0 (rank 710)', from_t4['with_M'] == 710)


def Lam_of(deta):
    names_h_ = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    out = []
    for (p_, q_) in names_h_:
        out.append(deta[q_][p_ + 1] + deta[p_][q_ + 1])
    for i in range(3):
        out.append(deta[i][0] - deta[3][i + 1])
    out.append(deta[3][0])
    return out


def law_level_ranks():
    rng = random.Random(11)
    rows = []
    for _ in range(110):
        phi = [rng.randint(-4, 4) for _ in range(10)]
        dphi = [[rng.randint(-4, 4) for _ in range(10)] for _ in range(4)]
        xi_ = [rng.randint(-4, 4) for _ in range(4)]
        dxi = [[rng.randint(-4, 4) for _ in range(4)] for _ in range(4)]
        lam = Lam_of(dxi)
        mcols = []
        for s_ in range(4):
            for r_ in range(4):
                for B in range(10):
                    d = [[0] * 4 for _ in range(4)]
                    for mu_ in range(4):
                        d[s_][mu_] = dphi[mu_][B] * xi_[r_] + phi[B] * dxi[r_][mu_]
                    mcols.append(Lam_of(d))
        for A in range(10):
            row = [0] * 550
            for k_, (B, C) in enumerate(PAIRS):
                row[A * 55 + k_] = 2 * lam[B] * phi[B] if B == C else lam[B] * phi[C] + phi[B] * lam[C]
            row += [mc[A] for mc in mcols]
            rows.append([x % PRIME for x in row])
    out = {}
    out['with_M'] = rank_mod_p(rows)
    out['all'] = rank_mod_p([r_[:550] for r_ in rows])
    hn_idx = [j for j, (A, k_) in enumerate(COLS) if A in (0, 1, 2, 3, 4, 5, 9) and PAIRS[k_][0] in (0, 1, 2, 3, 4, 5, 9) and PAIRS[k_][1] in (0, 1, 2, 3, 4, 5, 9)]
    rows_hn = [[r_[j] for j in hn_idx] for r_ in rows if True]
    out['hn'] = rank_mod_p(rows_hn)
    assert len(hn_idx) == 196
    return out


def recovery_json():
    pass


def main():
    part_A()
    part_B_identities()
    dictionary_dependence()
    part_B_lemmas()
    npass = sum(RESULTS); nfail = len(RESULTS) - npass
    print('TOTAL: PASS=%d FAIL=%d' % (npass, nfail))
    print('runtime %.1f s' % (_time.time() - _T0))
    if nfail == 0:
        print('HIT: block 161 T4 confirmed with exact arithmetic at any strain (links W=1+(i/2)eps a.s with a the frame\'s own connection add exactly (1/8) eps.C, sign fixed, and the lattice limit is the comparator\'s operator); block 159 T4(c) closes (a redefinition vertex that is strictly invariant is zero) but it lands on (1,1/2,0) only through the metric-and-lapse dictionary, since zero-derivative redefinitions move the jets (1+2c1, 1/2+2c1+2c2, 0)')
    print('SUMMARY: exact checks that the connection-carrying links add (1/8) eps.C with the stated sign, that the lattice limit is the comparator, that 159 T4(c) has no gap from strictly invariant redefinition vertices (kernel 0), and that its landing on (1,1/2,0) rests on the metric/lapse dictionary')
    sys.exit(0 if nfail == 0 else 1)


if __name__ == '__main__':
    main()

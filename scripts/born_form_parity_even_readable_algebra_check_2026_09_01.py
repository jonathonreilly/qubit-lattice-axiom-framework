#!/usr/bin/env python3
"""The Born form on the parity-even readable algebra, checked exactly.

Class-A finite-dimensional runner for the readable-algebra repair: under the
declared grading hypothesis the readable one-site content is the parity-even
content, and the Born form there is a one-parameter Bernoulli weight, while the
effect-versus-projective structure and the noncommutative trace form appear at
two sites in the even sector.

Declared objects (all exact; sympy only, no floats, no sampling):

  * Pauli matrices s1, s2, s3, the unit one = eye(2), and the matrix units
    E00, E01 = |0><1|, E10, E11 of M_2(C), with n = E11;
  * the parity grading Ad(s3) of the site algebra: even = span{E00, E11},
    odd = span{E01, E10};
  * the one-site even effect algebra E_even = {a(1-n) + b n : a, b in [0,1]}
    and the dyadic grid a, b in {k/8 : k = 0..8};
  * two sites on C^4 in the basis |00>, |01>, |10>, |11>, with total parity
    P = s3 (x) s3, even block {|00>, |11>} and odd block {|01>, |10>};
  * n_0 = n (x) one, n_1 = one (x) n, and the sixteen two-site Pauli strings;
  * the pseudo-qubit operators t1, t2, t3 of the odd block and the three
    coplanar unit vectors at 120 degrees in the (1,3)-plane.

Check groups:

  A  one site: the parity-even part is span{1, n}, the even effects are exactly
     a(1-n) + b n with a, b in [0,1], the even rank-one projectors are exactly
     n and 1-n, every effect-additive normalized functional on the even effects
     is the one-parameter trace form, there is no even trine, and the rogue
     frame function agrees with the trace form on the even directions;
  B  two sites: the even subalgebra is M_2(C) (+) M_2(C) of dimension 8, the
     positive normalized functionals on it are exactly the parity-diagonal
     trace forms, a genuinely noncommutative even Born value exists, and the
     trine reappears inside the odd-parity block as even non-projective
     effects;
  C  records versus reconstructions: parity-diagonal marginals are diagonal
     with vanishing odd part, a locked record gives Born values 1 and 0, and
     every parity-diagonal two-site state annihilates every odd Pauli string.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

import itertools
import sys

import sympy as sp
from sympy import I, Matrix, eye, zeros, symbols, sqrt, Rational

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one exact check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ---------------------------------------------------------------- notation

s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
one = eye(2)
SIG = [s1, s2, s3]

E00 = Matrix([[1, 0], [0, 0]])
E01 = Matrix([[0, 1], [0, 0]])
E10 = Matrix([[0, 0], [1, 0]])
E11 = Matrix([[0, 0], [0, 1]])
UNITS = [E00, E01, E10, E11]
n = E11

I4 = eye(4)
Z4 = zeros(4, 4)
Z2 = zeros(2, 2)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return Matrix(out)


def zero(M):
    return all(sp.expand(e) == 0 for e in M)


def eq(A, B):
    return zero(A - B)


def rows_of(mats):
    return Matrix([[e for e in M] for M in mats])


def herm(name, dim):
    """A symbolic Hermitian dim x dim matrix in real parameters."""
    d = symbols(name + "_d0:%d" % dim, real=True)
    x = {}
    y = {}
    for i in range(dim):
        for j in range(i + 1, dim):
            x[(i, j)] = sp.Symbol("%s_x%d%d" % (name, i, j), real=True)
            y[(i, j)] = sp.Symbol("%s_y%d%d" % (name, i, j), real=True)
    M = zeros(dim, dim)
    for i in range(dim):
        M[i, i] = d[i]
        for j in range(i + 1, dim):
            M[i, j] = x[(i, j)] + I * y[(i, j)]
            M[j, i] = x[(i, j)] - I * y[(i, j)]
    return M, list(d) + [x[k] for k in sorted(x)] + [y[k] for k in sorted(y)]


# ================================================== A: one site, even sector

# --- A1a: the parity-even part of M_2(C) is exactly span{1, n}

Xg = Matrix(2, 2, symbols("g0:4"))
a1_sol = sp.solve(list(Xg * s3 - s3 * Xg), list(symbols("g0:4")), dict=True)
Xev = Xg.subs(a1_sol[0])
a1_free = sorted(Xev.free_symbols, key=sp.default_sort_key)
check("A1a even part of M_2(C) = commutant of s3 = span{1,n}, complex dimension 2",
      len(a1_sol) == 1
      and len(a1_free) == 2
      and eq(Xev, a1_free[0] * (one - n) + a1_free[1] * n)
      and rows_of([one, n]).rank() == 2
      and eq(s3 * (one - n) * s3, one - n) and eq(s3 * n * s3, n)
      and eq(s3 * E01 * s3, -E01) and eq(s3 * E10 * s3, -E10))

# --- A1b: the even effects are exactly a(1-n) + b n with a, b in [0,1]

av, bv = symbols("av bv", real=True)
Xab = av * (one - n) + bv * n
a1b = (eq(Xab.H, Xab)
       and eq(Xab * s3 - s3 * Xab, Z2)
       and set(Xab.eigenvals().keys()) == {av, bv}
       and set((one - Xab).eigenvals().keys()) == {1 - av, 1 - bv}
       and eq(Xab.subs({av: Rational(1, 3), bv: Rational(3, 4)}),
              Matrix([[Rational(1, 3), 0], [0, Rational(3, 4)]])))
check("A1b even Hermitian X = a(1-n)+bn has spec {a,b}, and 1-X has spec {1-a,1-b}: "
      "0 <= X <= 1 exactly when a, b are in [0,1]",
      a1b)

# --- A2: the even rank-one projectors are exactly n and 1-n

pq = symbols("p0:4")
Pg = Matrix(2, 2, pq)
a2_eqs = (list(Pg * Pg - Pg) + list(Pg.H - Pg) + list(Pg * s3 - s3 * Pg))
a2_sols = sp.solve(a2_eqs, list(pq), dict=True)
a2_mats = [Pg.subs(s) for s in a2_sols]
a2_rank1 = [M for M in a2_mats if M.rank() == 1]
check("A2 P = P^2 = P^dagger with [P,s3] = 0 has exactly four solutions; "
      "the rank-one ones are exactly n and 1-n",
      len(a2_sols) == 4
      and len(a2_rank1) == 2
      and any(eq(M, n) for M in a2_rank1)
      and any(eq(M, one - n) for M in a2_rank1)
      and any(eq(M, Z2) for M in a2_mats)
      and any(eq(M, one) for M in a2_mats))

# --- A3a: the one-parameter trace form is additive, normalized, positive

pp = sp.Symbol("pp", real=True)
rho1 = (1 - pp) * (one - n) + pp * n


def mform(a, b):
    return a * (1 - pp) + b * pp


GRID = [Rational(k, 8) for k in range(9)]
a3a = eq(sp.expand(Matrix([[mform(av, bv)]])),
         Matrix([[sp.expand((rho1 * (av * (one - n) + bv * n)).trace())]]))
a3a = a3a and sp.simplify(mform(1, 1) - 1) == 0
for a1v in GRID:
    for b1v in GRID:
        for a2v in GRID:
            for b2v in GRID:
                if a1v + a2v <= 1 and b1v + b2v <= 1:
                    d = sp.expand(mform(a1v + a2v, b1v + b2v)
                                  - mform(a1v, b1v) - mform(a2v, b2v))
                    a3a = a3a and d == 0
for a1v in GRID:
    for b1v in GRID:
        for pv in GRID:
            a3a = a3a and mform(a1v, b1v).subs({pp: pv}) >= 0
check("A3a m(a(1-n)+bn) = a(1-p)+bp = Tr(diag(1-p,p) E): additive on every grid pair "
      "with E+F <= 1, normalized at m(1) = 1, nonnegative on the grid",
      a3a)

# --- A3b: converse, additivity on the dyadic grid forces that form

msym = {}
for j in range(9):
    for k in range(9):
        msym[(j, k)] = sp.Symbol("m_%d_%d" % (j, k))
step_eqs = []
for j in range(8):
    for k in range(9):
        step_eqs.append(msym[(j + 1, k)] - msym[(j, k)] - msym[(1, 0)])
for j in range(9):
    for k in range(8):
        step_eqs.append(msym[(j, k + 1)] - msym[(j, k)] - msym[(0, 1)])
step_eqs.append(msym[(8, 8)] - 1)
unk = [msym[(j, k)] for j in range(9) for k in range(9)]
b_sol = sp.solve(step_eqs, unk, dict=True)
a3b = len(b_sol) == 1
if a3b:
    sub = b_sol[0]
    vals = {key: sp.expand(msym[key].subs(sub)) for key in msym}
    freev = set()
    for v in vals.values():
        freev |= v.free_symbols
    pfree = vals[(0, 8)]
    a3b = a3b and len(freev) == 1
    for j in range(9):
        for k in range(9):
            want = Rational(j, 8) * (1 - pfree) + Rational(k, 8) * pfree
            a3b = a3b and sp.expand(vals[(j, k)] - want) == 0
# every full additivity instance is satisfied by that one-parameter family
full_ok = True
for j1 in range(9):
    for k1 in range(9):
        for j2 in range(9 - j1):
            for k2 in range(9 - k1):
                d = sp.expand(mform(Rational(j1 + j2, 8), Rational(k1 + k2, 8))
                              - mform(Rational(j1, 8), Rational(k1, 8))
                              - mform(Rational(j2, 8), Rational(k2, 8)))
                full_ok = full_ok and d == 0
check("A3b converse on the dyadic grid: additivity plus m(1) = 1 determines m at every "
      "grid point from m(n) alone, one free parameter",
      a3b and full_ok
      and sp.expand(mform(0, 1) - pp) == 0
      and sp.expand(mform(1, 0) - (1 - pp)) == 0
      and sp.expand(mform(0, 1) + mform(1, 0) - 1) == 0)

# --- A4a: the M_2(C) trine leaves the even algebra at one site

TRI = [(0, 0, 1),
       (sqrt(3) / 2, 0, Rational(-1, 2)),
       (-sqrt(3) / 2, 0, Rational(-1, 2))]


def proj(v):
    return sp.expand((one + v[0] * s1 + v[1] * s2 + v[2] * s3) / 2)


tri1 = [sp.expand(Rational(2, 3) * proj(v)) for v in TRI]
even_flags = [eq(M * s3 - s3 * M, Z2) for M in tri1]
check("A4a one site: the trine (2/3)P(n_k) resolves 1 in M_2(C), each rank one and no "
      "projector, and exactly one of the three is parity-even",
      eq(sp.expand(tri1[0] + tri1[1] + tri1[2]), one)
      and all(M.rank() == 1 and not eq(M * M, M) and eq(M.H, M) for M in tri1)
      and all(sp.simplify(sum(c * c for c in v) - 1) == 0 for v in TRI)
      and sum(1 for f in even_flags if f) == 1)

# --- A4b: no even trine, by enumeration on a rational grid

CG = [Rational(k, 6) for k in range(1, 7)]
sols = []
for c0 in CG:
    for c1 in CG:
        for c2 in CG:
            for d in itertools.product([0, 1], repeat=3):
                tot = Z2
                for cc, dd in zip((c0, c1, c2), d):
                    tot = tot + cc * (n if dd else one - n)
                if eq(tot, one):
                    sols.append(((c0, c1, c2), d))
a4b = len(sols) > 0
for (cs, d) in sols:
    a4b = a4b and len(set(d)) <= 2
    a4b = a4b and (d[0] == d[1] or d[0] == d[2] or d[1] == d[2])
check("A4b no even trine: every rational triple of scaled even rank-one effects summing "
      "to 1 repeats a direction (%d solutions, none with three distinct directions)" % len(sols),
      a4b)

# --- A4c: the rogue frame function agrees with the trace form on even directions

def g_rogue(v):
    return sp.Rational(1, 2) + v[2] ** 3 / 2


nz = sp.Symbol("nz", real=True)
rho_up = E00
a4c = sp.expand(g_rogue((0, 0, nz)) + g_rogue((0, 0, -nz)) - 1) == 0
for v, want in ((0, 0, 1), 1), ((0, 0, -1), 0):
    a4c = (a4c
           and sp.simplify(g_rogue(v) - want) == 0
           and sp.simplify((rho_up * proj(v)).trace() - want) == 0)
voff = (sqrt(3) / 2, 0, Rational(1, 2))
a4c = (a4c
       and sp.simplify(sum(c * c for c in voff) - 1) == 0
       and sp.simplify(g_rogue(voff) - Rational(9, 16)) == 0
       and sp.simplify((rho_up * proj(voff)).trace() - Rational(3, 4)) == 0)
check("A4c the rogue g = 1/2 + n_z^3/2 obeys g(n) + g(-n) = 1, equals Tr(diag(1,0)P(n)) "
      "at the even directions +-z (1 and 0), and differs off them (9/16 against 3/4)",
      a4c)

# =========================================== B: two sites, the even sector

P2 = kron(s3, s3)
n0 = kron(n, one)
n1 = kron(one, n)
EVEN_IDX = [0, 3]
ODD_IDX = [1, 2]


def unit4(i, j):
    M = Z4.copy()
    M[i, j] = 1
    return M


EVEN_BASIS = ([unit4(i, j) for i in EVEN_IDX for j in EVEN_IDX]
              + [unit4(i, j) for i in ODD_IDX for j in ODD_IDX])

# --- B1a: the even subalgebra has dimension 8 and is block diagonal

Yg = Matrix(4, 4, symbols("y0:16"))
b1_sol = sp.solve(list(Yg * P2 - P2 * Yg), list(symbols("y0:16")), dict=True)
Yev = Yg.subs(b1_sol[0])
b1_free = sorted(Yev.free_symbols, key=sp.default_sort_key)
cross = [(i, j) for i in EVEN_IDX for j in ODD_IDX] + [(i, j) for i in ODD_IDX for j in EVEN_IDX]
check("B1a the commutant of P = s3(x)s3 has complex dimension 8, vanishes on all eight "
      "cross-block entries, and is spanned by the eight in-block matrix units",
      len(b1_sol) == 1
      and len(b1_free) == 8
      and all(sp.expand(Yev[i, j]) == 0 for (i, j) in cross)
      and rows_of(EVEN_BASIS).rank() == 8
      and rows_of(EVEN_BASIS + [Yev.subs({t: 1 for t in b1_free})]).rank() == 8)

# --- B1b: the even subalgebra is M_2(C) (+) M_2(C) in the parity basis

Ap, Bp = Matrix(2, 2, symbols("A0:4")), Matrix(2, 2, symbols("B0:4"))
Aq, Bq = Matrix(2, 2, symbols("C0:4")), Matrix(2, 2, symbols("D0:4"))


def emb(Xp, Xm):
    M = Z4.copy()
    for u, i in enumerate(EVEN_IDX):
        for v, j in enumerate(EVEN_IDX):
            M[i, j] = Xp[u, v]
    for u, i in enumerate(ODD_IDX):
        for v, j in enumerate(ODD_IDX):
            M[i, j] = Xm[u, v]
    return M


b1b = (eq(emb(Ap, Bp) * emb(Aq, Bq), emb(sp.expand(Ap * Aq), sp.expand(Bp * Bq)))
       and eq(emb(Ap, Bp) + emb(Aq, Bq), emb(Ap + Aq, Bp + Bq))
       and eq(emb(one, one), I4)
       and eq(emb(Ap, Bp).H, emb(Ap.H, Bp.H))
       and eq(emb(Ap, Bp) * P2 - P2 * emb(Ap, Bp), Z4))
check("B1b the parity-basis block map M_2(C)(+)M_2(C) -> commutant(P) is a unital *-isomorphism "
      "onto the even subalgebra (multiplicative, additive, adjoint-compatible, symbolic blocks)",
      b1b)

# --- B2a: parity-diagonal states, and additivity, normalization, positivity

Sg, Spar = herm("sg", 4)
b2_sol = sp.solve(list(Sg * P2 - P2 * Sg), Spar, dict=True)
Sev = Sg.subs(b2_sol[0])
b2a = (len(b2_sol) == 1
       and all(sp.expand(Sev[i, j]) == 0 for (i, j) in cross)
       and len(sorted(Sev.free_symbols, key=sp.default_sort_key)) == 8)
Ac, Bc = Matrix(2, 2, symbols("ac0:4")), Matrix(2, 2, symbols("bc0:4"))
lhs = sp.expand((Ac * Ac.H * Bc * Bc.H).trace())
rhs = sp.expand(sum(e * sp.conjugate(e) for e in (Bc.H * Ac)))
b2a = b2a and sp.expand(lhs - rhs) == 0
Eg, Fg = Matrix(4, 4, symbols("eg0:16")), Matrix(4, 4, symbols("fg0:16"))
b2a = b2a and sp.expand(((Sev * (Eg + Fg)).trace()
                         - (Sev * Eg).trace() - (Sev * Fg).trace())) == 0
b2a = b2a and sp.expand((Sev * I4).trace() - Sev.trace()) == 0
Ep, Em = Matrix(2, 2, symbols("ep0:4")), Matrix(2, 2, symbols("em0:4"))
Sp2, Sm2 = Matrix(2, 2, symbols("sp0:4")), Matrix(2, 2, symbols("sm0:4"))
b2a = b2a and sp.expand((emb(Sp2, Sm2) * emb(Ep, Em)).trace()
                        - (Sp2 * Ep).trace() - (Sm2 * Em).trace()) == 0
check("B2a parity-diagonal Hermitian sigma is exactly sigma_+ (+) sigma_-, 8 real "
      "parameters; E -> Tr(sigma E) is additive, gives Tr(sigma) at E = 1, splits as "
      "Tr(s_+ E_+) + Tr(s_- E_-), and Tr(AA^d BB^d) = sum |(B^d A)_ij|^2 >= 0",
      b2a)

# --- B2b: every linear functional on the even algebra is a unique even trace form

fsym = symbols("f0:8")
Tg, Tpar = herm("tg", 4)
Tev = Tg.subs(sp.solve(list(Tg * P2 - P2 * Tg), Tpar, dict=True)[0])
Ug = Matrix(4, 4, symbols("u0:16"))
Uev = Ug.subs(sp.solve(list(Ug * P2 - P2 * Ug), list(symbols("u0:16")), dict=True)[0])
Ufree = sorted(Uev.free_symbols, key=sp.default_sort_key)
b2b_eqs = [sp.expand((Uev * EVEN_BASIS[i]).trace()) - fsym[i] for i in range(8)]
b2b_sol = sp.solve(b2b_eqs, Ufree, dict=True)
b2b = (len(b2b_sol) == 1
       and len(b2b_sol[0]) == 8
       and all(sp.expand(v).has(*fsym) for v in b2b_sol[0].values()))
Ustar = Uev.subs(b2b_sol[0])
b2b = b2b and all(sp.expand((Ustar * EVEN_BASIS[i]).trace() - fsym[i]) == 0 for i in range(8))
b2b = b2b and len(sorted(Ustar.free_symbols, key=sp.default_sort_key)) == 8
check("B2b every linear functional on the 8-dimensional even algebra is Tr(sigma .) for "
      "exactly one even sigma: the 8-by-8 trace-pairing system has a unique solution",
      b2b)

# --- B2c: positivity on the rank-one even projectors forces each block PSD

r, s_, x, y = symbols("r s_ x y", real=True)
z1, z2, tt = symbols("z1 z2 tt", real=True)
blk = Matrix([[r, x + I * y], [x - I * y, s_]])
vz = Matrix([1, z1 + I * z2])
Q = sp.expand((vz.H * blk * vz)[0, 0])
b2c = sp.expand(sp.im(Q)) == 0
Qr = sp.expand(sp.re(Q))
b2c = b2c and sp.expand(Qr - (r + 2 * (x * z1 - y * z2) + s_ * (z1 ** 2 + z2 ** 2))) == 0
b2c = b2c and sp.simplify(Qr.subs({z1: -x / s_, z2: y / s_}) - (r * s_ - x ** 2 - y ** 2) / s_) == 0
b2c = b2c and sp.expand(s_ * Qr - ((s_ * z1 + x) ** 2 + (s_ * z2 - y) ** 2
                                   + (r * s_ - x ** 2 - y ** 2))) == 0
b2c = b2c and sp.expand(Qr.subs({s_: 0, z1: -tt * x, z2: tt * y})
                        - (r - 2 * tt * (x ** 2 + y ** 2))) == 0
b2c = b2c and sp.expand(Qr.subs({z1: 0, z2: 0}) - r) == 0
e1v = Matrix([0, 1])
b2c = b2c and sp.expand((e1v.H * blk * e1v)[0, 0] - s_) == 0
check("B2c rank-one test on a block: Q = r + 2(x z1 - y z2) + s(z1^2 + z2^2) and "
      "s Q = (s z1 + x)^2 + (s z2 - y)^2 + (rs - x^2 - y^2), so Q >= 0 for every v is "
      "exactly r, s >= 0 with rs >= x^2 + y^2",
      b2c)

# --- B3: a genuinely noncommutative even Born value at two sites

vbell = Matrix([0, 1, 1, 0]) / sqrt(2)
Qproj = sp.expand(vbell * vbell.H)
r01 = unit4(1, 1)
r00 = unit4(0, 0)
b3 = (eq(Qproj * Qproj, Qproj) and eq(Qproj.H, Qproj) and Qproj.rank() == 1
      and eq(Qproj * P2 - P2 * Qproj, Z4)
      and sp.expand((Qproj * Qproj).trace()) == 1
      and sp.expand((r01 * Qproj).trace()) == Rational(1, 2)
      and sp.expand((r00 * Qproj).trace()) == 0
      and not zero(Qproj * r01 - r01 * Qproj)
      and rows_of(EVEN_BASIS + [Qproj]).rank() == 8)
check("B3 the even projector Q onto (|01>+|10>)/sqrt2 commutes with P, gives Born values "
      "1, 1/2, 0 in the states Q, |01><01|, |00><00|, and fails to commute with |01><01|",
      b3)

# --- B4a: the trine relocates into the odd-parity block

t1 = unit4(1, 2) + unit4(2, 1)
t2 = -I * unit4(1, 2) + I * unit4(2, 1)
t3 = unit4(1, 1) - unit4(2, 2)
Ib = unit4(1, 1) + unit4(2, 2)
TT = [t1, t2, t3]
def bproj(v):
    out = Ib
    for k in range(3):
        out = out + v[k] * TT[k]
    return sp.expand(out / 2)


tri2 = [sp.expand(Rational(2, 3) * bproj(v)) for v in TRI]
b4a = eq(sp.expand(tri2[0] + tri2[1] + tri2[2]), Ib)
for M in tri2:
    b4a = (b4a
           and eq(M * P2 - P2 * M, Z4)
           and eq(M.H, M)
           and M.rank() == 1
           and set(M.eigenvals().keys()) == {0, Rational(2, 3)}
           and rows_of(EVEN_BASIS + [M]).rank() == 8)
for i in range(3):
    for j in range(i + 1, 3):
        b4a = b4a and rows_of([tri2[i], tri2[j]]).rank() == 2
check("B4a the trine relocates: (2/3)P(n_k) built inside the odd-parity block are even "
      "effects of spectrum {0,2/3}, pairwise non-proportional, resolving that block's 1",
      b4a)

# --- B4b: those effects are not projectors and not one-site

iot0 = [kron(U, one) for U in UNITS]
iot1 = [kron(one, U) for U in UNITS]
b4b = rows_of(iot0 + iot1).rank() == 7
for M in tri2:
    b4b = (b4b
           and not eq(M * M, M)
           and rows_of(iot0 + iot1 + [M]).rank() == 8
           and any(not zero(M * K - K * M) for K in tri2))
check("B4b none of the three even effects is a projector, and none lies in the span of "
      "the one-site images (rank 7 -> 8): the effect-projector gap is two-site content",
      b4b)

# ==================================== C: records versus reconstructions

# --- C1: the one-site marginal of a parity-diagonal state


def ptrace0(M):
    return Matrix(2, 2, lambda j, jp: sum(M[2 * i + j, 2 * i + jp] for i in range(2)))


def ptrace1(M):
    return Matrix(2, 2, lambda i, ip: sum(M[2 * i + j, 2 * ip + j] for j in range(2)))


Snorm = Sev.subs({sorted(Sev.free_symbols, key=sp.default_sort_key)[0]:
                  1 - sum(sorted(Sev.free_symbols, key=sp.default_sort_key)[1:4])})
m1 = sp.expand(ptrace0(Snorm))
m0 = sp.expand(ptrace1(Snorm))
p1 = sp.expand((Snorm * n1).trace())
p0 = sp.expand((Snorm * n0).trace())
c1 = (sp.expand(m1[0, 1]) == 0 and sp.expand(m1[1, 0]) == 0
      and sp.expand(m0[0, 1]) == 0 and sp.expand(m0[1, 0]) == 0
      and eq(m1, (1 - p1) * (one - n) + p1 * n)
      and eq(m0, (1 - p0) * (one - n) + p0 * n)
      and sp.expand((m1 * s1).trace()) == 0 and sp.expand((m1 * s2).trace()) == 0
      and sp.expand((m0 * s1).trace()) == 0 and sp.expand((m0 * s2).trace()) == 0
      and sp.expand(Snorm.trace()) == 1)
check("C1 for every parity-diagonal trace-one sigma the marginal at each site is "
      "diag(1-p,p) with p = Tr(sigma n_x), and its odd part vanishes (s1, s2 zero)",
      c1)

# --- C2: a locked record gives Kronecker-delta Born values

Rg, Rpar = herm("rg", 4)
c2 = True
for nx in (n0, n1):
    sol = sp.solve(list(nx * Rg - Rg) + [Rg.trace() - 1], Rpar, dict=True)
    c2 = c2 and len(sol) == 1
    Rl = Rg.subs(sol[0])
    c2 = (c2
          and eq(nx * Rl, Rl) and eq(Rl * nx, Rl)
          and sp.expand((Rl * nx).trace()) == 1
          and sp.expand((Rl * (I4 - nx)).trace()) == 0
          and sp.expand(Rl.trace()) == 1)
lock = unit4(1, 1)
c2 = (c2 and eq(n1 * lock, lock)
      and sp.expand((lock * n1).trace()) == 1
      and sp.expand((lock * (I4 - n1)).trace()) == 0)
check("C2 a record locking n_x = 1 (n_x sigma = sigma, Tr sigma = 1) gives Born value "
      "exactly 1 on n_x and exactly 0 on 1 - n_x: a Kronecker delta on the even readout",
      c2)

# --- C3: parity superselection recomputed on two sites

Pplus = sp.expand((I4 + P2) / 2)
Pminus = sp.expand((I4 - P2) / 2)
Xs = Matrix(4, 4, symbols("xs0:16"))
Ys = Matrix(4, 4, symbols("ys0:16"))
rho2 = sp.expand(Pplus * Xs * Pplus + Pminus * Ys * Pminus)
odd_strings = []
even_strings = []
for u, v in itertools.product(range(4), repeat=2):
    S = kron([one, s1, s2, s3][u], [one, s1, s2, s3][v])
    if sum(1 for w in (u, v) if w in (1, 2)) % 2 == 1:
        odd_strings.append(S)
    else:
        even_strings.append(S)
c3 = len(odd_strings) == 8 and len(even_strings) == 8
for O in odd_strings:
    c3 = c3 and eq(O * P2 + P2 * O, Z4)
    c3 = c3 and sp.expand((rho2 * O).trace()) == 0
c3 = c3 and any(sp.expand((rho2 * S).trace()) != 0 for S in even_strings)
c3 = c3 and eq(rho2 * P2 - P2 * rho2, Z4)
check("C3 every parity-diagonal sigma = P+ X P+ + P- Y P- annihilates all eight odd "
      "two-site Pauli strings (odd s1/s2 count) while even strings take nonzero values",
      c3)

print("SUMMARY: at one site the parity-even readable algebra carries a one-parameter "
      "Bernoulli Born form with no trine and no rogue; the effect structure and the "
      "noncommutative trace form live at two sites.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)

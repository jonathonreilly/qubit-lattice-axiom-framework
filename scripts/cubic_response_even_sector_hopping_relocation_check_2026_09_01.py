#!/usr/bin/env python3
"""The cubic neighbor response under the grading: scalar at one site, hopping in
the directed-edge channel.

Class-A finite-dimensional runner for the cubic-response repair: the proper-cubic
classification of neighbor responses is recomputed from scratch, the effect of a
declared parity grading on its conditional record-faithfulness corollary is
computed, and the first-order directed response is relocated to the hopping
channel of the graded product on a seven-site star, a ring, and a 3x3x3 block.

Declared objects (all exact; sympy only, no floats, no sampling):

  * the Pauli matrices s1, s2, s3 used as Gamma_1, Gamma_2, Gamma_3, with
    {Gamma_mu, Gamma_nu} = 2 delta_{mu nu} 1, the unit one = eye(2), and
    n = E11, so that Herm(2) = R 1 (+) R^3 Gamma;
  * the parity grading Ad(s3) of the site algebra, even = span{E00, E11};
  * the six directed unit vectors d in {+e_1, -e_1, +e_2, -e_2, +e_3, -e_3},
    indexed 0..5 in that order, and the six real neighbor sensitivities c_d;
  * the proper cubic rotations, the closure of Rz and Rx as integer matrices of
    determinant +1, and the induced 6x6 permutation matrices Pi_R;
  * the seven-site star {0} u {+-e_mu} with the center indexed 0 and the
    neighbor d indexed 1+d, its 7x7 matrix units E_{i,j}, and the twelve
    hopping units E_{0,1+d}, E_{1+d,0};
  * the Jordan-Wigner modes of the three-site line {-e_1, 0, +e_1} on C^8;
  * the L = 3 and L = 4 rings and the 3x3x3 block of 27 sites with open
    boundary, both in their single-particle sectors.

Check groups:

  A  the classification recomputed at one site: the 24 rotations and their
     directed-neighbor permutation group, the exactly two-dimensional space of
     equivariant real-linear maps R^6 -> Herm(2), and the parity of the
     spectral projectors of the realized response;
  B  the corollary under the declared grading hypothesis: even faithfulness
     plus cubic equivariance forces b = 0, and the surviving scalar point is a
     graph-Laplacian-type multiple of 1 with no rank-one content;
  C  relocation to hopping bilinears: the Jordan-Wigner check that c_0^dag c_d
     restricts to a matrix unit on the one-particle subspace, the equivariant
     classification in the twelve-dimensional hopping span, the ring symbols
     2 sin k and 2 cos k, and the failure of a Clifford relation on the block.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

import sys

import sympy as sp
from sympy import I, Matrix, eye, zeros, symbols, Rational

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


def zero(M):
    return all(sp.expand(e) == 0 for e in M)


def eqm(A, B):
    return zero(A - B)


def rows_of(vecs):
    return Matrix([list(v) for v in vecs])


def nullbasis(eqs, unks):
    """Real basis of the solution space of a homogeneous linear system."""
    A, rhs = sp.linear_eq_to_matrix(eqs, unks)
    if any(sp.expand(e) != 0 for e in rhs):
        return None
    return A.nullspace()


def same_multiset(xs, ys):
    ys = list(ys)
    if len(xs) != len(ys):
        return False
    for x in xs:
        hit = -1
        for k, y in enumerate(ys):
            if sp.simplify(x - y) == 0:
                hit = k
                break
        if hit < 0:
            return False
        ys.pop(hit)
    return True


# ---------------------------------------------------------------- notation

s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])
one = eye(2)
Z2 = zeros(2, 2)
SIG = [s1, s2, s3]
E00 = Matrix([[1, 0], [0, 0]])
E11 = Matrix([[0, 0], [0, 1]])
n = E11

DIRS = [Matrix([1, 0, 0]), Matrix([-1, 0, 0]),
        Matrix([0, 1, 0]), Matrix([0, -1, 0]),
        Matrix([0, 0, 1]), Matrix([0, 0, -1])]

Rz = Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
Rx = Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])


def close(gens):
    G = [eye(3)]
    frontier = [eye(3)]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                X = g * M
                if not any(X == Y for Y in G):
                    G.append(X)
                    nxt.append(X)
        frontier = nxt
    return G


def didx(v):
    for i, w in enumerate(DIRS):
        if v == w:
            return i
    return -1


def perm6(R):
    P = zeros(6, 6)
    img = []
    for d in range(6):
        j = didx(R * DIRS[d])
        img.append(j)
        if j >= 0:
            P[j, d] = 1
    return P, img


# ==================================== A: the classification, recomputed

# --- A1: the 24 proper cubic rotations and their directed-neighbor permutations

ROT = close([Rz, Rx])
a1 = len(ROT) == 24
PIS = []
for R in ROT:
    a1 = (a1 and R.det() == 1 and eqm(R * R.T, eye(3))
          and all(e.is_Integer for e in R))
    P, img = perm6(R)
    a1 = a1 and sorted(img) == list(range(6))
    PIS.append(P)
PSET = {tuple(P) for P in PIS}
a1 = a1 and len(PSET) == 24
for i in range(24):
    for j in range(24):
        a1 = a1 and tuple(PIS[i] * PIS[j]) in PSET
        a1 = a1 and perm6(ROT[i] * ROT[j])[0] == PIS[i] * PIS[j]
check("A1 the closure of Rz, Rx is 24 integer rotations of determinant +1; each permutes "
      "the six directed unit vectors, and R -> Pi_R is an injective homomorphism onto a "
      "6x6 permutation group of order 24",
      a1)

PZ, _ = perm6(Rz)
PX, _ = perm6(Rx)
GENS = [(Rz, PZ), (Rx, PX)]

# --- A2a: the equivariant maps R^6 -> Herm(2) form a 2-dimensional space

al = symbols("al0:6", real=True)
be = symbols("be0:18", real=True)
alpha = Matrix(1, 6, list(al))
beta = Matrix(3, 6, list(be))
eqs_a2 = []
for R, P in GENS:
    eqs_a2 += list(alpha * P - alpha)
    eqs_a2 += list(beta * P - R * beta)
ns_a2 = nullbasis(eqs_a2, list(al) + list(be))
Dm = Matrix(3, 6, lambda i, d: DIRS[d][i])
w_scalar = [1] * 6 + [0] * 18
w_vector = [0] * 6 + [Dm[i, j] for i in range(3) for j in range(6)]
cliff = all(eqm(SIG[u] * SIG[v] + SIG[v] * SIG[u],
                (2 if u == v else 0) * one) for u in range(3) for v in range(3))
a2a = (ns_a2 is not None and len(ns_a2) == 2 and cliff
       and rows_of([w_scalar, w_vector]).rank() == 2
       and rows_of([list(v) for v in ns_a2] + [w_scalar, w_vector]).rank() == 2)
check("A2a equivariant real-linear L(c) = alpha(c)1 + beta(c).Gamma with Gamma_mu = s_mu "
      "(24 real unknowns, {Gamma_mu,Gamma_nu} = 2 delta 1): the solution space has real "
      "dimension exactly 2 and is spanned by alpha = (1,...,1), beta = 0 and alpha = 0, "
      "beta = the direction matrix",
      a2a)

# --- A2b: both displayed maps are equivariant for all 24 rotations

ones6 = Matrix(1, 6, [1] * 6)
a2b = True
for k, R in enumerate(ROT):
    a2b = a2b and eqm(ones6 * PIS[k], ones6) and eqm(Dm * PIS[k], R * Dm)
csym = symbols("c0:6", real=True)
cv = Matrix(6, 1, list(csym))
av, bv = symbols("av bv", real=True)


def F(a, b, c):
    out = a * sum(c) * one
    for mu in range(3):
        out = out + b * (c[2 * mu] - c[2 * mu + 1]) * SIG[mu]
    return sp.expand(out)


a2b = a2b and eqm(F(av, bv, list(csym)),
                  av * (ones6 * cv)[0, 0] * one
                  + bv * sum(((Dm * cv)[mu, 0] * SIG[mu] for mu in range(3)), Z2))
check("A2b both displayed maps are equivariant for all 24 rotations: (1,...,1) Pi_R = "
      "(1,...,1) and D Pi_R = R D, where the columns of D are the six directions, so "
      "F(c) = a[sum_d c_d]1 + b sum_mu (c_{+mu} - c_{-mu}) Gamma_mu",
      a2b)

# --- A3a: general parity of the spectral projectors

n1, n2, n3, mm, tt = symbols("n1 n2 n3 mm tt", real=True)
NG = n1 * s1 + n2 * s2 + n3 * s3
Pp = sp.expand((one + NG) / 2)
Pm = sp.expand((one - NG) / 2)
Fs = mm * one + tt * NG
nn = n1 ** 2 + n2 ** 2 + n3 ** 2
a3a = (eqm(NG * s3 - s3 * NG, 2 * I * (n2 * s1 - n1 * s2))
       and eqm(NG * NG, nn * one)
       and eqm(Pp * Pp - Pp, ((nn - 1) / 4) * one)
       and eqm(Pm * Pm - Pm, ((nn - 1) / 4) * one)
       and eqm(Pp + Pm, one)
       and eqm(Pp * s3 - s3 * Pp, I * (n2 * s1 - n1 * s2))
       and eqm(sp.expand((Fs - (mm - tt) * one) / (2 * tt)), Pp)
       and eqm(sp.expand((Fs - (mm + tt) * one) / (-2 * tt)), Pm)
       and eqm(sp.expand((mm + tt) * Pp + (mm - tt) * Pm), Fs))
check("A3a spectral projectors of F = m1 + t(n_hat.Gamma), t nonzero: P_pm = (1 pm "
      "n_hat.Gamma)/2 are polynomials in F and F is their combination, and [P_pm, s3] = "
      "pm i(n2 s1 - n1 s2) vanishes exactly when n1 = n2 = 0, i.e. the vector part is "
      "parallel to e_3",
      a3a)

# --- A3b: the two directed witnesses

c_p1 = [1, 0, 0, 0, 0, 0]
c_p3 = [0, 0, 0, 0, 1, 0]
F1 = F(av, bv, c_p1)
F3 = F(av, bv, c_p3)
Q1p = sp.expand((one + s1) / 2)
Q1m = sp.expand((one - s1) / 2)
a3b = (eqm(F1, av * one + bv * s1) and eqm(F3, av * one + bv * s3)
       and eqm(Q1p * Q1p, Q1p) and Q1p.rank() == 1 and Q1m.rank() == 1
       and eqm(Q1p + Q1m, one)
       and eqm(sp.expand((av + bv) * Q1p + (av - bv) * Q1m), F1)
       and not zero(Q1p * s3 - s3 * Q1p)
       and not zero(Q1m * s3 - s3 * Q1m)
       and eqm(sp.expand((av + bv) * E00 + (av - bv) * E11), F3)
       and zero(E00 * s3 - s3 * E00) and zero(E11 * s3 - s3 * E11)
       and E00.rank() == 1 and E11.rank() == 1)
check("A3b witnesses: at c = e_{+1} the projectors of F are (1 pm s1)/2, rank one and "
      "NOT commuting with s3; at c = e_{+3} they are E00, E11, rank one and commuting "
      "with s3",
      a3b)

# ==================================== B: the corollary under the hypothesis

# --- B1: even faithfulness forces b = 0

sols = []
for cw in (c_p1, [0, 0, 1, 0, 0, 0]):
    Fw = F(av, bv, cw)
    sols.append(sp.solve(list(Fw * s3 - s3 * Fw), [bv], dict=True))
b1 = (len(sols[0]) == 1 and sols[0][0] == {bv: 0}
      and len(sols[1]) == 1 and sols[1][0] == {bv: 0}
      and eqm(F(av, 0, list(csym)), av * sum(csym) * one)
      and eqm(F(av, bv, list(csym)).subs({bv: 0}), av * sum(csym) * one))
gen_b = sp.solve(list(F(av, bv, list(csym)) * s3 - s3 * F(av, bv, list(csym))),
                 [bv], dict=True)
b1 = b1 and len(gen_b) == 1
check("B1 even faithfulness: requiring the nontrivial rank-one spectral projectors to be "
      "parity-even at c = e_{+1} and c = e_{+2} gives b(c_{+1}-c_{-1}) = 0 and "
      "b(c_{+2}-c_{-2}) = 0, whose unique solution is b = 0, leaving F(c) = a[sum_d c_d]1",
      b1)

# --- B2: the scalar point has no rank-one content

uu = symbols("u0:7", real=True)
c_lap = [uu[1 + d] - uu[0] for d in range(6)]
Fsc = F(-1, 0, c_lap)
lap = sum(uu[1:]) - 6 * uu[0]
xv, yv = symbols("xv yv", real=True)
Xev = xv * (one - n) + yv * n
ev = Fsc.eigenvals()
b2 = (sp.expand(sum(c_lap) - lap) == 0
      and eqm(Fsc, -lap * one)
      and zero(Fsc * s3 - s3 * Fsc)
      and zero(Fsc * Xev - Xev * Fsc)
      and len(ev) == 1 and list(ev.values()) == [2]
      and eqm(Fsc + lap * one, Z2)
      and one.rank() == 2)
check("B2 scalar point (a,b) = (-1,0) with c_d = u_d - u_0: F = -[sum_d c_d]1 = -(graph "
      "Laplacian at the center)1, commuting with s3 and with every even x(1-n)+yn; it has "
      "a single eigenvalue of multiplicity 2, so its spectral projector is 1 of rank 2 and "
      "carries no rank-one content",
      b2)

# ==================================== C: relocation to hopping bilinears

# --- C1: Jordan-Wigner on the three-site line {-e_1, 0, +e_1}


def kron(*ms):
    out = ms[0]
    for M in ms[1:]:
        out = sp.kronecker_product(out, M)
    return Matrix(out)


ann = Matrix([[0, 1], [0, 0]])
I8 = eye(8)
cJW = [kron(ann, one, one), kron(s3, ann, one), kron(s3, s3, ann)]
c1 = True
for i in range(3):
    for j in range(3):
        c1 = c1 and eqm(cJW[i] * cJW[j].H + cJW[j].H * cJW[i],
                        (1 if i == j else 0) * I8)
        c1 = c1 and eqm(cJW[i] * cJW[j] + cJW[j] * cJW[i], zeros(8, 8))
vac = zeros(8, 1)
vac[0, 0] = 1
onep = [cJW[j].H * vac for j in range(3)]
P3 = kron(s3, s3, s3)
Nop = sum((cJW[j].H * cJW[j] for j in range(3)), zeros(8, 8))
hops = {(1, 0): cJW[1].H * cJW[0], (1, 2): cJW[1].H * cJW[2]}
for (i, j), h in hops.items():
    c1 = c1 and zero(h * P3 - P3 * h) and zero(h * Nop - Nop * h)
    red = zeros(3, 3)
    for b in range(3):
        img = h * onep[b]
        for a in range(3):
            red[a, b] = (onep[a].H * img)[0, 0]
        rest = img - sum((red[a, b] * onep[a] for a in range(3)), zeros(8, 1))
        c1 = c1 and zero(rest)
    want = zeros(3, 3)
    want[i, j] = 1
    c1 = c1 and eqm(red, want)
check("C1 Jordan-Wigner on {-e_1, 0, +e_1} (indices 0,1,2, center 1): the CAR hold on "
      "C^8, the hopping bilinears c_1^dag c_0 and c_1^dag c_2 commute with the total "
      "parity s3(x)s3(x)s3 and with the number operator, and on the one-particle subspace "
      "they are exactly the matrix units E_{1,0} and E_{1,2}",
      c1)

# --- C2a: the equivariant hopping maps, dimension reported honestly


def E7(i, j):
    M = zeros(7, 7)
    M[i, j] = 1
    return M


def star_perm(P6):
    U = zeros(7, 7)
    U[0, 0] = 1
    for a in range(6):
        for b in range(6):
            U[1 + a, 1 + b] = P6[a, b]
    return U


xs = symbols("x0:36", real=True)
ys = symbols("y0:36", real=True)
Xm = Matrix(6, 6, list(xs))
Ym = Matrix(6, 6, list(ys))


def Mmap(X, Y, c):
    cvv = Matrix(6, 1, list(c))
    z = X * cvv + I * (Y * cvv)
    zb = X * cvv - I * (Y * cvv)
    out = zeros(7, 7)
    for d in range(6):
        out[0, 1 + d] = z[d, 0]
        out[1 + d, 0] = zb[d, 0]
    return out


unks = list(xs) + list(ys)
eqs_c2 = set()
for R, P in GENS:
    U = star_perm(P)
    for e in range(6):
        ce = [1 if k == e else 0 for k in range(6)]
        cr = [P[k, e] for k in range(6)]
        Delta = Mmap(Xm, Ym, cr) - U * Mmap(Xm, Ym, ce) * U.T
        for expr in Delta:
            re_, im_ = sp.expand(expr).as_real_imag()
            for piece in (sp.expand(re_), sp.expand(im_)):
                if piece != 0:
                    eqs_c2.add(piece)
ns_c2 = nullbasis(sorted(eqs_c2, key=sp.default_sort_key), unks)
Sinv = Matrix(6, 6, lambda a, b: 1 if b == (a + 1 if a % 2 == 0 else a - 1) else 0)
Jall = Matrix(6, 6, lambda a, b: 1)
COMM = [eye(6), Sinv, Jall]
eqs_cm = []
for R, P in GENS:
    eqs_cm += list(Xm * P - P * Xm)
ns_cm = nullbasis(eqs_cm, list(xs))


def flat(X, Y):
    return [X[a, b] for a in range(6) for b in range(6)] + \
           [Y[a, b] for a in range(6) for b in range(6)]


exp6 = [flat(K, zeros(6, 6)) for K in COMM] + [flat(zeros(6, 6), K) for K in COMM]
c2a = (ns_c2 is not None and len(ns_c2) == 6
       and ns_cm is not None and len(ns_cm) == 3
       and rows_of(exp6).rank() == 6
       and rows_of([list(v) for v in ns_c2] + exp6).rank() == 6
       and rows_of([[K[a, b] for a in range(6) for b in range(6)]
                    for K in COMM]).rank() == 3
       and rows_of([list(v) for v in ns_cm]
                   + [[K[a, b] for a in range(6) for b in range(6)]
                      for K in COMM]).rank() == 3)
check("C2a equivariant real-linear M : R^6 -> Herm(7) valued in the 12-dimensional "
      "hopping span (72 real unknowns): the solution space has real dimension exactly 6, "
      "NOT 2; the real commutant of the directed-neighbor permutation rep is span{1, S, J} "
      "of dimension 3 (S the inversion d -> -d, J all-ones) and it acts in both the "
      "symmetric and the directed channel",
      c2a)

# --- C2b: H_A and H_T are Hermitian, equivariant members of that space


def H_A(c):
    return Mmap(eye(6), zeros(6, 6), c)


def H_T(c):
    return Mmap(zeros(6, 6), eye(6), c)


c2b = True
for build in (H_A, H_T):
    Mc = build(list(csym))
    c2b = c2b and eqm(Mc.H, Mc)
    for k, R in enumerate(ROT):
        U = star_perm(PIS[k])
        c2b = c2b and eqm(build(list(PIS[k] * cv)), U * Mc * U.T)
c2b = (c2b
       and eqm(H_A(list(csym)), sum((csym[d] * (E7(0, 1 + d) + E7(1 + d, 0))
                                     for d in range(6)), zeros(7, 7)))
       and eqm(H_T(list(csym)), I * sum((csym[d] * (E7(0, 1 + d) - E7(1 + d, 0))
                                         for d in range(6)), zeros(7, 7))))
check("C2b H_A(c) = sum_d c_d (E_{0,d} + E_{d,0}) and H_T(c) = i sum_d c_d (E_{0,d} - "
      "E_{d,0}) are Hermitian and equivariant for all 24 rotations, and both lie in the "
      "6-dimensional solution space",
      c2b)

# --- C2c: the honest parity statement for the two channels

HA = H_A(list(csym))
HT = H_T(list(csym))
cS = list(Sinv * cv)
sym_in = [csym[0], csym[0], csym[2], csym[2], csym[4], csym[4]]
ant_in = [csym[0], -csym[0], csym[2], -csym[2], csym[4], -csym[4]]
c2c = (eqm(HA.T, HA) and eqm(HT.T, -HT)
       and eqm(H_A(sym_in), H_A(list(Sinv * Matrix(6, 1, sym_in))))
       and eqm(H_T(ant_in), -H_T(list(Sinv * Matrix(6, 1, ant_in))))
       and not zero(H_A(cS) - HA)
       and not zero(H_T(cS) + HT))
check("C2c edge reversal E_{0,d} <-> E_{d,0} is transposition: H_A(c)^T = H_A(c) is even "
      "and H_T(c)^T = -H_T(c) is odd. Under the input inversion S alone, with the site "
      "labels held fixed, neither is even or odd on all of R^6; H_A is even on "
      "S-symmetric inputs and H_T odd on S-antisymmetric inputs",
      c2c)

# --- C3a: the directed input gives the first-order difference at the center

psi = symbols("p0:7", real=True)
pv = Matrix(7, 1, list(psi))
c_dir = [1, -1, 0, 0, 0, 0]
outT = H_T(c_dir) * pv
outA = H_A(c_dir) * pv
c3a = (eqm(H_T(c_dir), I * (E7(0, 1) - E7(1, 0) - E7(0, 2) + E7(2, 0)))
       and sp.expand(outT[0, 0] - I * (psi[1] - psi[2])) == 0
       and sp.expand(outT[1, 0] + I * psi[0]) == 0
       and sp.expand(outT[2, 0] - I * psi[0]) == 0
       and all(sp.expand(outT[k, 0]) == 0 for k in range(3, 7))
       and sp.expand(outA[0, 0] - (psi[1] - psi[2])) == 0)
check("C3a directed input c = e_{+1} - e_{-1}: H_T(c) = i(E_{0,+1} - E_{+1,0} - E_{0,-1} "
      "+ E_{-1,0}) and (H_T psi)_0 = i(psi_{+1} - psi_{-1}), the centered first-order "
      "difference along direction 1, with no internal Clifford factor",
      c3a)

# --- C3b: the ring symbols 2 sin k and 2 cos k

c3b = True
for L in (3, 4):
    Dr = zeros(L, L)
    Ar = zeros(L, L)
    for j in range(L):
        k = (j + 1) % L
        Dr[j, k] += I
        Dr[k, j] += -I
        Ar[j, k] += 1
        Ar[k, j] += 1
    dvals = []
    for lam, mult in Dr.eigenvals().items():
        dvals += [lam] * mult
    avals = []
    for lam, mult in Ar.eigenvals().items():
        avals += [lam] * mult
    c3b = (c3b and eqm(Dr.H, Dr) and eqm(Ar.H, Ar)
           and same_multiset(dvals, [2 * sp.sin(2 * sp.pi * m / L) for m in range(L)])
           and same_multiset(avals, [2 * sp.cos(2 * sp.pi * m / L) for m in range(L)]))
for m in range(4):
    wave = Matrix(4, 1, [I ** (m * j) for j in range(4)])
    Dr4 = zeros(4, 4)
    Ar4 = zeros(4, 4)
    for j in range(4):
        k = (j + 1) % 4
        Dr4[j, k] += I
        Dr4[k, j] += -I
        Ar4[j, k] += 1
        Ar4[k, j] += 1
    c3b = (c3b
           and zero(sp.expand(Dr4 * wave + 2 * sp.sin(sp.pi * m / 2) * wave))
           and zero(sp.expand(Ar4 * wave - 2 * sp.cos(sp.pi * m / 2) * wave)))
check("C3b ring symbols: on the L = 3 and L = 4 rings the directed hop i sum_j (E_{j,j+1} "
      "- E_{j+1,j}) has eigenvalue multiset {2 sin(2 pi m/L)} and the symmetric hop sum_j "
      "(E_{j,j+1} + E_{j+1,j}) has {2 cos(2 pi m/L)}; on L = 4 the plane wave i^{mj} has "
      "eigenvalues -2 sin(pi m/2) and 2 cos(pi m/2)",
      c3b)

# --- C4: no Clifford relation from the hopping channels alone

NS = 27


def sidx(x, y, z):
    return 9 * x + 3 * y + z


def Dop(mu):
    M = zeros(NS, NS)
    for x in range(3):
        for y in range(3):
            for z in range(3):
                q = [x, y, z]
                q[mu] += 1
                if q[mu] <= 2:
                    a = sidx(x, y, z)
                    b = sidx(q[0], q[1], q[2])
                    M[a, b] += I
                    M[b, a] += -I
    return M


DOPS = [Dop(mu) for mu in range(3)]
c4 = all(eqm(D.H, D) for D in DOPS)
for mu in range(3):
    for nu in range(mu + 1, 3):
        c4 = c4 and zero(DOPS[mu] * DOPS[nu] - DOPS[nu] * DOPS[mu])
        c4 = c4 and not zero(DOPS[mu] * DOPS[nu] + DOPS[nu] * DOPS[mu])
Qsum = DOPS[0] ** 2 + DOPS[1] ** 2 + DOPS[2] ** 2
diagvals = {sp.expand(Qsum[k, k]) for k in range(NS)}
c4 = (c4 and diagvals == {sp.Integer(k) for k in (3, 4, 5, 6)}
      and sp.expand(Qsum.trace()) == 108
      and not eqm(Qsum, sp.Rational(1, NS) * Qsum.trace() * eye(NS)))
check("C4 3x3x3 block, 27-site single-particle sector, open boundary: the three first-"
      "difference operators D_mu = i sum_x (E_{x,x+e_mu} - E_{x+e_mu,x}) are Hermitian, "
      "commute pairwise, have nonvanishing anticommutators, and D_1^2 + D_2^2 + D_3^2 is "
      "not a multiple of 1, its diagonal being the four coordination numbers 3, 4, 5, 6 "
      "of the open block with trace 108, so no Clifford relation arises from the hopping "
      "channels alone",
      c4)

print("SUMMARY: the two-parameter cubic classification is reconfirmed at one site; under "
      "the declared grading hypothesis even faithfulness forces b = 0 and leaves a "
      "graph-Laplacian-type scalar with no rank-one content; the first-order directed "
      "response reappears in the hopping channel, whose equivariant space has real "
      "dimension 6 rather than 2, carries sin k per direction with no internal Clifford "
      "factor, and yields commuting D_mu on the cube.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)

#!/usr/bin/env python3
"""Parity-odd couplings under the 24 proper rotations only.

Exact arithmetic throughout (sympy rationals / Gaussian integers as Python or
int64 integers with an explicit overflow bound).  No floating point is used for
any claim.  Sections:
  A1  nearest-neighbour hermitian covariant generators (block 54 T1(a) re-derived)
  A2  inversions that commute with the 24 rotations; parity table of a0, a, beta
  A3  loop-trace obstruction: a chiral closed 8-step loop with odd part -a^3 beta^5
  A4  observable: a chiral rate field and its mirror image give different tr((wH)^L)
  A5  blind completion of the scalar hop; Theta-Pi covariance of completions
  A6  supplied clauses (walk with rates, frame, twist) are Theta-Pi covariant
  B1  field energy: O versus O_h invariant counts (parity-odd sector)
  B2  the unique odd frame density eps.T is not blind at zero strain
  C   the sense of the top level is sign(a*beta)
"""
import itertools, sys
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

FAIL = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)

# ---------------------------------------------------------------- group data
def signed_perms():
    out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3, 3)
            for i in range(3):
                M[i, p[i]] = sg[i]
            out.append(M)
    return out
OH = signed_perms()                       # 48 elements: O_h
O24 = [g for g in OH if g.det() == 1]     # 24 proper rotations
check("A0 |O_h| = 48 and |O| = 24", len(OH) == 48 and len(O24) == 24)

s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
SIG = [s1, s2, s3]; I2 = sp.eye(2)

# ------------------------------------------------------------------------ A1
# A_e = x0 + x.sigma (complex x's) for e in {0, +-e_j}; covariance Ad_R(A_e) = A_{Re},
# Ad_R(x0, x) = (x0, R x) (the adjoint action of any SU(2) lift of R); hermiticity
# A_{-e} = A_e^dagger.  Unknowns: real and imaginary parts, 7*4*2 = 56 reals.
E = [(0, 0, 0)] + [tuple(int(v) for v in s * sp.eye(3)[:, j]) for j in range(3) for s in (1, -1)]
idx = {e: k for k, e in enumerate(E)}
nvar = 7 * 4 * 2
def var(e, comp, part):          # comp 0..3 (x0, x1, x2, x3); part 0 re, 1 im
    return (idx[e] * 4 + comp) * 2 + part
rows = []
def add_row(pairs):
    r = [0] * nvar
    for k, v in pairs:
        r[k] += v
    rows.append(r)
for R in O24:
    for e in E:
        Re_ = tuple(int(v) for v in R * sp.Matrix(e))
        for part in (0, 1):
            add_row([(var(Re_, 0, part), 1), (var(e, 0, part), -1)])
            for c in range(3):
                d = [(var(Re_, c + 1, part), 1)]
                for c2 in range(3):
                    if R[c, c2] != 0:
                        d.append((var(e, c2 + 1, part), -int(R[c, c2])))
                add_row(d)
for e in E:
    me = tuple(-v for v in e)
    for comp in range(4):          # x(-e) = conj x(e) componentwise (sigma hermitian)
        add_row([(var(me, comp, 0), 1), (var(e, comp, 0), -1)])
        add_row([(var(me, comp, 1), 1), (var(e, comp, 1), 1)])
Msys = sp.Matrix(rows)
ns = Msys.nullspace()
check("A1 covariant hermitian nearest-neighbour generators: real dimension 3 (block 54 T1(a))", len(ns) == 3)
# the three solutions are a0 (on-site scalar), a (scalar hop), beta (x_j on +-e_j imaginary, odd in e)
span = sp.Matrix.hstack(*ns)
# expected family: A_0 = a0, A_{+-e_j} = a -+ (i beta/2) sigma_j in the convention (H psi)(x) = sum_e A_e psi(x+e)
a0s, as_, bs = sp.symbols('a0 a beta', real=True)
fam = [0] * nvar
fam[var((0, 0, 0), 0, 0)] = a0s
for j in range(3):
    ep = E[1 + 2 * j]; em = E[2 + 2 * j]
    fam[var(ep, 0, 0)] = as_; fam[var(em, 0, 0)] = as_
    fam[var(ep, j + 1, 1)] = -bs / 2; fam[var(em, j + 1, 1)] = bs / 2
fam = sp.Matrix(fam)
check("A1 the family A_0 = a0, A_{+-e_j} = a -+ (i beta/2) sigma_j solves every condition", (Msys * fam).expand() == sp.zeros(Msys.rows, 1))
check("A1 and spans the solution space", sp.Matrix.hstack(span, fam.subs({a0s: 1, as_: 2, bs: 3})).rank() == 3
      and sp.Matrix.hstack(span, fam.subs({a0s: 5, as_: -1, bs: 7})).rank() == 3)

# ------------------------------------------------------------------------ A2
# linear V commuting with the lifts (1 - i sigma_c)/sqrt2  <=>  [V, sigma_c] = 0
vv = sp.symbols('v0:8', real=True)
V = sp.Matrix([[vv[0] + sp.I * vv[1], vv[2] + sp.I * vv[3]], [vv[4] + sp.I * vv[5], vv[6] + sp.I * vv[7]]])
eqs = []
for c in range(3):
    C = (V * SIG[c] - SIG[c] * V)
    eqs += [sp.re(x) for x in C] + [sp.im(x) for x in C]
Ml = sp.Matrix([[sp.diff(eq, x) for x in vv] for eq in eqs])
check("A2 linear coin maps commuting with the 24 lifts: only scalars (dim 2 real = C)", len(Ml.nullspace()) == 2)
eqs = []
for c in range(3):
    C = (V * SIG[c].conjugate() + SIG[c] * V)       # V conj(U) = U V for U = (1 - i s)/sqrt2
    eqs += [sp.re(x) for x in C] + [sp.im(x) for x in C]
Ma = sp.Matrix([[sp.diff(eq, x) for x in vv] for eq in eqs])
nsa = Ma.nullspace()
Vs = sp.Matrix([[nsa[0][0] + sp.I * nsa[0][1], nsa[0][2] + sp.I * nsa[0][3]], [nsa[0][4] + sp.I * nsa[0][5], nsa[0][6] + sp.I * nsa[0][7]]])
check("A2 antilinear coin maps V K commuting with the 24 lifts: only multiples of sigma_2",
      len(nsa) == 2 and sp.simplify(Vs[0, 0]) == 0 and sp.simplify(Vs[1, 1]) == 0 and sp.simplify(Vs[0, 1] + Vs[1, 0]) == 0)
inv_n = []
for n in itertools.product((0, 1), repeat=3):
    if all(all(((sp.Matrix(n).T * R)[i] - n[i]) % 2 == 0 for i in range(3)) for R in O24):
        inv_n.append(n)
check("A2 site-sign patterns (-1)^{n.x} kept by the 24 rotations: n = 000 and 111 only", inv_n == [(0, 0, 0), (1, 1, 1)])
# symbol-level action.  (H psi)(x) = sum_e A_e psi(x+e)  ->  h(k) = sum_e A_e exp(i k.e)
k1, k2, k3 = sp.symbols('k1:4', real=True); K = (k1, k2, k3)
def symb(a0, a, b):
    return a0 * I2 + sum(((2 * a * sp.cos(K[j])) * I2 + b * sp.sin(K[j]) * SIG[j] for j in range(3)), sp.zeros(2, 2))
h = symb(a0s, as_, bs)
# check the family's symbol against the blocks
hb = sp.zeros(2, 2)
hb += a0s * I2
for j in range(3):
    hb += (as_ * I2 - sp.I * bs / 2 * SIG[j]) * sp.exp(sp.I * K[j]) + (as_ * I2 + sp.I * bs / 2 * SIG[j]) * sp.exp(-sp.I * K[j])
check("A2 symbol of the family = a0 + 2a sum cos k + beta sum sigma_j sin k", (hb - h).applyfunc(lambda z: sp.simplify(sp.expand_complex(z.rewrite(sp.cos)))) == sp.zeros(2, 2))
neg = {k1: -k1, k2: -k2, k3: -k3}; shift = {k1: k1 + sp.pi, k2: k2 + sp.pi, k3: k3 + sp.pi}
def Pi(M): return M.subs(neg, simultaneous=True)
def Eps(M): return M.subs(shift, simultaneous=True)
def Theta(M): return s2 * M.subs(neg, simultaneous=True).conjugate() * s2   # sigma_2 K in position space
maps = {"Pi (linear)": (lambda M: Pi(M), +1), "eps Pi (linear)": (lambda M: Eps(Pi(M)), +1),
        "Theta Pi (antilinear)": (lambda M: Theta(Pi(M)), -1), "Theta eps Pi (antilinear)": (lambda M: Theta(Eps(Pi(M))), -1)}
table = {}
for name, (f, sgn) in maps.items():
    row = []
    for (x0, x1, x2) in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        t = symb(x0, x1, x2)
        d = sp.simplify(f(t) - sgn * t)
        row.append('keeps' if d == sp.zeros(2, 2) else 'breaks')
    table[name] = row
for name, row in table.items():
    print("     %-28s a0: %-6s a: %-6s beta: %s" % (name, *row))
check("A2 parity table: Pi keeps a0,a breaks beta; eps Pi keeps a0,beta breaks a; Theta Pi keeps beta breaks a0,a; Theta eps Pi keeps a breaks a0,beta",
      table == {"Pi (linear)": ['keeps', 'keeps', 'breaks'], "eps Pi (linear)": ['keeps', 'breaks', 'keeps'],
                "Theta Pi (antilinear)": ['breaks', 'breaks', 'keeps'], "Theta eps Pi (antilinear)": ['breaks', 'keeps', 'breaks']})

# ------------------------------------------------------------------------ A3
Bsym = {}
for j in range(3):
    e = [0, 0, 0]; e[j] = 1; Bsym[tuple(e)] = as_ * I2 - sp.I * bs / 2 * SIG[j]
    e = [0, 0, 0]; e[j] = -1; Bsym[tuple(e)] = as_ * I2 + sp.I * bs / 2 * SIG[j]
def tau(seq):
    M = I2
    for e in seq:
        M = M * Bsym[e]
    return sp.expand(M.trace())
gam = [(1, 0, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (-1, 0, 0), (0, 0, -1)]
check("A3 gamma* is a closed 8-step loop", tuple(map(sum, zip(*gam))) == (0, 0, 0))
t_g = tau(gam); t_m = tau([tuple(-c for c in e) for e in gam])
print("     tau(gamma*)      =", sp.factor(t_g))
print("     tau(-gamma*)     =", sp.factor(t_m))
check("A3 tau(gamma*) - tau(-gamma*) = -a^3 beta^5", sp.expand(t_g - t_m + as_**3 * bs**5) == 0)
check("A3 loop traces real (tau = conj tau) for real a, beta", sp.expand(t_g - sp.conjugate(t_g)) == 0 and sp.im(t_g) == 0)
cov = all(sp.expand(tau([tuple(int(v) for v in R * sp.Matrix(e)) for e in gam]) - t_g) == 0 for R in O24)
check("A3 tau(R gamma*) = tau(gamma*) for all 24 rotations (so every improper image has tau = tau(-gamma*))", cov)
# no closed 6-step loop has an odd part: Gaussian-integer arithmetic with 2*A_e, a = 1, beta = 1, 2, 3
def gmul(A, B):
    # 2x2 matrices of Gaussian integers as ((re,im),...) row-major
    out = []
    for i in range(2):
        for j in range(2):
            re_ = im_ = 0
            for k in range(2):
                ar, ai = A[2 * i + k]; br, bi = B[2 * k + j]
                re_ += ar * br - ai * bi; im_ += ar * bi + ai * br
            out.append((re_, im_))
    return tuple(out)
def gblocks(a, b):   # 2*A_e = 2a -+ i b sigma_j
    Bl = {}
    for j in range(3):
        for sg in (1, -1):
            e = [0, 0, 0]; e[j] = sg
            M = []
            for r in range(2):
                for c in range(2):
                    sv = complex(SIG[j][r, c])
                    re_ = (2 * a if r == c else 0) + int(sg * b * sv.imag)      # -+ i b s  ->  real part +- b*Im(s)
                    im_ = int(-sg * b * sv.real)
                    M.append((re_, im_))
            Bl[tuple(e)] = tuple(M)
    return Bl
ID = ((1, 0), (0, 0), (0, 0), (1, 0))
def closed_walks(L):
    steps = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    out = []
    def rec(pos, seq):
        r = L - len(seq)
        if abs(pos[0]) + abs(pos[1]) + abs(pos[2]) > r:
            return
        if r == 0:
            out.append(tuple(seq)); return
        for e in steps:
            rec((pos[0] + e[0], pos[1] + e[1], pos[2] + e[2]), seq + [e])
    rec((0, 0, 0), [])
    return out
W6 = closed_walks(6)
odd6 = 0
for b in (1, 2, 3):
    Bl = gblocks(1, b)
    for w in W6:
        M = ID; Mm = ID
        for e in w:
            M = gmul(M, Bl[e]); Mm = gmul(Mm, Bl[tuple(-c for c in e)])
        if (M[0][0] + M[3][0], M[0][1] + M[3][1]) != (Mm[0][0] + Mm[3][0], Mm[0][1] + Mm[3][1]):
            odd6 += 1
check("A3 no closed 6-step loop (%d walks) has a mirror-odd trace at beta/a = 1, 2, 3 (hence none for any a, beta)" % len(W6), odd6 == 0)
W8 = closed_walks(8); Bl = gblocks(1, 2); odd8 = 0
for w in W8:
    M = ID; Mm = ID
    for e in w:
        M = gmul(M, Bl[e]); Mm = gmul(Mm, Bl[tuple(-c for c in e)])
    if (M[0][0] + M[3][0]) != (Mm[0][0] + Mm[3][0]):
        odd8 += 1
print("     closed 8-step walks: %d, with a mirror-odd trace at a=1, beta=2: %d" % (len(W8), odd8))
check("A3 some closed 8-step walks are chiral (odd trace)", odd8 > 0)

# ------------------------------------------------------------------------ A4
N = 4; sites = list(itertools.product(range(N), repeat=3)); sidx = {x: i for i, x in enumerate(sites)}; n2 = 2 * len(sites)
def ham_int(a, b):
    """2H with (H psi)(x) = sum_e A_e psi(x+e), A_{+-e_j} = a -+ (i b/2) sigma_j: blocks 2a -+ i b sigma_j (Gaussian integers)."""
    X = np.zeros((n2, n2), dtype=np.int64); Y = np.zeros((n2, n2), dtype=np.int64)
    Bl = gblocks(a, b)
    for x in sites:
        for e, M in Bl.items():
            y = tuple((x[i] + e[i]) % N for i in range(3))
            for r in range(2):
                for c in range(2):
                    X[2 * sidx[x] + r, 2 * sidx[y] + c] += M[2 * r + c][0]
                    Y[2 * sidx[x] + r, 2 * sidx[y] + c] += M[2 * r + c][1]
    return X, Y
def wfield(f):
    return np.array([f(x) for x in sites for _ in range(2)], dtype=np.int64)
w = wfield(lambda x: 1 + ((7 * x[0] + 5 * x[1] * x[1] + 3 * x[2] + 2 * x[0] * x[1] * x[2] + x[1] * x[2]) % 3))
# mirror image by definition: w_m(x) = w(-x mod N)
w_mir = wfield(lambda x: int(w[2 * sidx[tuple((-c) % N for c in x)]]))
Rq = O24[5]
Rinv = Rq.T
w_rot = wfield(lambda x: int(w[2 * sidx[tuple(int(v) % N for v in (Rinv * sp.Matrix(x)))]]))
def traces(a, b, wv, Lmax=8):
    X, Y = ham_int(a, b)
    X = wv[:, None] * X; Y = wv[:, None] * Y
    A = np.abs(X) + np.abs(Y)
    # overflow guard: entries (and partial sums) of (X+iY)^L are bounded by those of A^L
    Af = A.astype(object); P = Af.copy(); bound = 0
    for _ in range(Lmax - 1):
        P = P.dot(Af)
    bound = max(max(r) for r in P.tolist())
    assert bound < 2**62, "int64 bound"
    out = []; PX, PY = X.copy(), Y.copy()
    out.append((int(np.trace(PX)), int(np.trace(PY))))
    for L in range(2, Lmax + 1):
        PX, PY = PX @ X - PY @ Y, PX @ Y + PY @ X
        out.append((int(np.trace(PX)), int(np.trace(PY))))
    return out
res = {}
for (a, b) in ((1, 2), (0, 2), (1, 0)):
    res[(a, b)] = (traces(a, b, w), traces(a, b, w_mir), traces(a, b, w_rot))
for key, (t0, tm, tr) in res.items():
    diffs = [L + 1 for L in range(8) if t0[L] != tm[L]]
    print("     a=%d beta=%d: tr((2wH)^L) differ from the mirror field at L = %s; rotated field equal: %s"
          % (key[0], key[1], diffs, t0 == tr))
t0, tm, tr = res[(1, 2)]
check("A4 rotated rate field: all eight moments equal (covariance control)", all(res[k][0] == res[k][2] for k in res))
check("A4 a=0 (the walk) and beta=0: moments of the field and of its mirror image equal", res[(0, 2)][0] == res[(0, 2)][1] and res[(1, 0)][0] == res[(1, 0)][1])
check("A4 a*beta != 0: moments equal for L <= 7 and differ at L = 8", t0[:7] == tm[:7] and t0[7] != tm[7])
check("A4 all moments real (imaginary parts zero)", all(v[1] == 0 for k in res for T in res[k] for v in T))
print("     a=1 beta=2, L=8: tr((2wH)^8) = %d, mirror field %d, difference %d" % (t0[7][0], tm[7][0], t0[7][0] - tm[7][0]))

# ------------------------------------------------------------------------ A5, A6 (3x3x3 torus, sympy exact)
N3 = 3; S3 = list(itertools.product(range(N3), repeat=3)); ix3 = {x: i for i, x in enumerate(S3)}; d3 = 2 * len(S3)
def shiftop(j, s=1):
    T = sp.zeros(d3, d3)
    for x in S3:
        y = list(x); y[j] = (y[j] + s) % N3
        for c in range(2):
            T[2 * ix3[x] + c, 2 * ix3[tuple(y)] + c] = 1     # (T psi)(x) = psi(x + e_j)
    return T
Tj = [shiftop(j) for j in range(3)]
Sj = [(Tj[j] - Tj[j].T) / (2 * sp.I) for j in range(3)]
Cj = [(Tj[j] + Tj[j].T) / 2 for j in range(3)]
def coin(c):     # sigma_c at every site
    return sp.diag(*([SIG[c]] * len(S3)))
def sitediag(f):   # f(x) -> 2x2 matrix
    return sp.diag(*[f(x) for x in S3])
Wk = sum((coin(j) * Sj[j] for j in range(3)), sp.zeros(d3, d3))
Ck = sum((2 * Cj[j] for j in range(3)), sp.zeros(d3, d3))          # sum (T + T^dag): symbol 2 sum cos k
rnd = [Fr(3, 7), Fr(-1, 2), Fr(5, 3), Fr(2, 9), Fr(-4, 5), Fr(1, 3), Fr(7, 4), Fr(-2, 3), Fr(1, 6)]
def th(x, c):
    return sp.Rational(rnd[(x[0] + 2 * x[1] + 4 * x[2] + 3 * c + x[0] * x[2]) % 9].numerator, rnd[(x[0] + 2 * x[1] + 4 * x[2] + 3 * c + x[0] * x[2]) % 9].denominator) + c * x[1] * sp.Rational(1, 5)
thS = sitediag(lambda x: sum((th(x, c) * SIG[c] for c in range(3)), sp.zeros(2, 2)))
def comp_(X, thetaS):
    return (-sp.I / 2) * (thetaS * X - X * thetaS)
def bondS(j, g):   # S_j[v]: (1/2i)(v(x) psi(x+e_j) - v(x-e_j) psi(x-e_j)), v a 2x2 matrix-valued bond function g(x)
    M = sp.zeros(d3, d3)
    for x in S3:
        y = list(x); y[j] = (y[j] + 1) % N3; y = tuple(y)
        z = list(x); z[j] = (z[j] - 1) % N3; z = tuple(z)
        gx = g(x); gz = g(z)
        for r in range(2):
            for c in range(2):
                M[2 * ix3[x] + r, 2 * ix3[y] + c] += gx[r, c] / (2 * sp.I)
                M[2 * ix3[x] + r, 2 * ix3[z] + c] -= gz[r, c] / (2 * sp.I)
    return M
def grad_th_sigma(j):
    def g(x):
        y = list(x); y[j] = (y[j] + 1) % N3; y = tuple(y)
        return sum(((th(y, c) - th(x, c)) * SIG[c] for c in range(3)), sp.zeros(2, 2))
    return g
lhs = comp_(Ck, thS)
rhs = -sum((bondS(j, grad_th_sigma(j)) for j in range(3)), sp.zeros(d3, d3))
check("A5 -(i/2)[theta.sigma, sum_j (T_j + T_j^dag)] = - sum_j S_j[(d_j theta).sigma] (coin-vector hop, all three coin components)", sp.simplify(lhs - rhs) == sp.zeros(d3, d3))
check("A5 the completion is hermitian", sp.simplify(rhs - rhs.H) == sp.zeros(d3, d3))
# block 65 T1 in these conventions: -(i/2)[theta.sigma, W] = 1/2 sum {(theta x e_j).sigma, S_j} + 1/2 sum C_j[d_j theta_j]
def bondC(j, v):
    M = sp.zeros(d3, d3)
    for x in S3:
        y = list(x); y[j] = (y[j] + 1) % N3; y = tuple(y)
        z = list(x); z[j] = (z[j] - 1) % N3; z = tuple(z)
        for c in range(2):
            M[2 * ix3[x] + c, 2 * ix3[y] + c] += v(x) / 2
            M[2 * ix3[x] + c, 2 * ix3[z] + c] += v(z) / 2
    return M
def cross_e(j):
    def f(x):
        t = [th(x, c) for c in range(3)]
        e = [0, 0, 0]; e[j] = 1
        cr = [t[1] * e[2] - t[2] * e[1], t[2] * e[0] - t[0] * e[2], t[0] * e[1] - t[1] * e[0]]
        return sum((cr[c] * SIG[c] for c in range(3)), sp.zeros(2, 2))
    return sitediag(f)
b65 = sum(((cross_e(j) * Sj[j] + Sj[j] * cross_e(j)) / 2 for j in range(3)), sp.zeros(d3, d3))
b65 += sum((bondC(j, (lambda jj: (lambda x: th(tuple((x[i] + (1 if i == jj else 0)) % N3 for i in range(3)), jj) - th(x, jj)))(j)) / 2 for j in range(3)), sp.zeros(d3, d3))
check("A5 block 65 T1 reproduced in these conventions (frame rotation + twist hop)", sp.simplify(comp_(Wk, thS) - b65) == sp.zeros(d3, d3))
# Theta Pi on operators: X -> (sigma2 (x) 1) P conj(X) P (sigma2 (x) 1), P: psi(x) -> psi(-x)
Pm = sp.zeros(d3, d3)
for x in S3:
    y = tuple((-c) % N3 for c in x)
    for c in range(2):
        Pm[2 * ix3[x] + c, 2 * ix3[y] + c] = 1
S2 = coin(1)
def TP(X):
    return S2 * Pm * X.conjugate() * Pm * S2
thS_m = sitediag(lambda x: sum((th(tuple((-c) % N3 for c in x), cc) * SIG[cc] for cc in range(3)), sp.zeros(2, 2)))
Ha = Ck + comp_(Ck, thS); Ha_m = Ck + comp_(Ck, thS_m)
Hw = Wk + comp_(Wk, thS); Hw_m = Wk + comp_(Wk, thS_m)
check("A5 Theta Pi: completed scalar hop -> + (completed scalar hop in the mirror twist): odd relative to the walk", sp.simplify(TP(Ha) - Ha_m) == sp.zeros(d3, d3))
check("A6 Theta Pi: completed walk -> - (completed walk in the mirror twist)", sp.simplify(TP(Hw) + Hw_m) == sp.zeros(d3, d3))
phi = sitediag(lambda x: (1 + sp.Rational((x[0] + 2 * x[1] * x[1] + x[2] * x[0]) % 5, 3)) * I2)
phi_m = sitediag(lambda x: (1 + sp.Rational(((-x[0]) % N3 + 2 * ((-x[1]) % N3) ** 2 + ((-x[2]) % N3) * ((-x[0]) % N3)) % 5, 3)) * I2)
check("A6 Theta Pi: clocked walk phi W phi -> -(phi' W phi'), phi' the mirror clock field", sp.simplify(TP(phi * Wk * phi) + phi_m * Wk * phi_m) == sp.zeros(d3, d3))
check("A5 Theta Pi: clocked scalar hop phi C phi -> + phi' C phi'", sp.simplify(TP(phi * Ck * phi) - phi_m * Ck * phi_m) == sp.zeros(d3, d3))
def frameH(Ef):
    return sum(((Ef(j) * Sj[j] + Sj[j] * Ef(j)) / 2 for j in range(3)), sp.zeros(d3, d3))
def Efield(sgn):
    def Ej(j):
        def f(x):
            xx = tuple((sgn * c) % N3 for c in x)
            return sum(((sp.Rational((xx[0] + 2 * xx[1] + 3 * xx[2] + j + c) % 4, 2) + (1 if c == j else 0)) * SIG[c] for c in range(3)), sp.zeros(2, 2))
        return sitediag(f)
    return Ej
check("A6 Theta Pi: frame walk H[E] -> -H[E'], E'(x) = E(-x)", sp.simplify(TP(frameH(Efield(1))) + frameH(Efield(-1))) == sp.zeros(d3, d3))

# ------------------------------------------------------------------------ B1
# characters over O and O_h.  V: vector; A: axial (det g) g; T-space: V (x) Lambda^2 V (curl of a co-frame).
def chiV(g): return g.trace()
def chiA(g): return g.det() * g.trace()
def chiL2(g): return (chiV(g) ** 2 - chiV(g * g)) / 2
def lin_inv(chi):
    return {G: sp.nsimplify(sum(chi(g) for g in grp) / len(grp)) for G, grp in (("O", O24), ("Oh", OH))}
def sym2_inv(chi):
    return {G: sp.nsimplify(sum((chi(g) ** 2 + chi(g * g)) / 2 for g in grp) / len(grp)) for G, grp in (("O", O24), ("Oh", OH))}
chiT = lambda g: chiV(g) * chiL2(g)
rep = {
    "T (one derivative, linear)": lin_inv(chiT),
    "T T (two derivatives, quadratic)": sym2_inv(chiT),
    "dT (two derivatives, linear)": lin_inv(lambda g: chiV(g) * chiT(g)),
    "d theta, u d theta, (du) theta": lin_inv(lambda g: chiV(g) * chiA(g)),
    "d d theta": lin_inv(lambda g: (chiV(g) ** 2 + chiV(g * g)) / 2 * chiA(g)),
    "theta theta": sym2_inv(chiA),
    "theta d theta": lin_inv(lambda g: chiA(g) * chiV(g) * chiA(g)),
    "(d theta)(d theta)": sym2_inv(lambda g: chiV(g) * chiA(g)),
    "theta d d theta": lin_inv(lambda g: chiA(g) * (chiV(g) ** 2 + chiV(g * g)) / 2 * chiA(g)),
    "(du)(d theta)": lin_inv(lambda g: chiV(g) * chiV(g) * chiA(g)),
    "u d d theta": lin_inv(lambda g: (chiV(g) ** 2 + chiV(g * g)) / 2 * chiA(g)),
}
odd = {}
for k_, v in rep.items():
    odd[k_] = v["O"] - v["Oh"]
    print("     %-34s O-invariants %s, O_h-invariants %s, parity-odd %s" % (k_, v["O"], v["Oh"], odd[k_]))
check("B1 frame class: parity-odd invariants at <= 2 derivatives: exactly one (linear in T); none quadratic, none in dT",
      odd["T (one derivative, linear)"] == 1 and odd["T T (two derivatives, quadratic)"] == 0 and odd["dT (two derivatives, linear)"] == 0)
check("B1 T T: 4 invariants under O (one more than SO(3)'s 3), all even", rep["T T (two derivatives, quadratic)"] == {"O": 4, "Oh": 4})
check("B1 separate rotation field: odd invariants = div theta, u div theta / grad u.theta, theta.curl theta; none at two derivatives",
      odd["d theta, u d theta, (du) theta"] == 1 and odd["theta d theta"] == 1 and odd["d d theta"] == 0 and odd["theta theta"] == 0
      and odd["(d theta)(d theta)"] == 0 and odd["theta d d theta"] == 0 and odd["(du)(d theta)"] == 0 and odd["u d d theta"] == 0)
# the O-invariant linear form on T is eps
epsT = lambda i, a, b: sp.LeviCivita(i, a, b)
inv_ok = True
for g in OH:
    # form L(T) = sum eps_{iab} T^i_{ab};  invariance: L(gT) = det(g) L(T) for all T  <=> eps_{iab} g g g = det g eps
    for (i, a, b) in itertools.product(range(3), repeat=3):
        lhs_ = sum(epsT(i2, a2, b2) * g[i2, i] * g[a2, a] * g[b2, b] for i2 in range(3) for a2 in range(3) for b2 in range(3))
        if lhs_ != g.det() * epsT(i, a, b):
            inv_ok = False
check("B1 the invariant is eps.T = eps_{jab} T^j_{ab}: kept by the 24, reversed by every improper element", inv_ok)

# ------------------------------------------------------------------------ B2
X = sp.symbols('x1:4', real=True)
thf = [sp.Function('th%d' % c)(*X) for c in range(3)]
Bm = sp.Matrix(3, 3, lambda b, j: -sum(sp.LeviCivita(b, j, m) * thf[m] for m in range(3)))   # B_b^j antisymmetric: a rotation by theta
def Tlin(Bmat):
    return {(j, a, b): sp.diff(Bmat[b, j], X[a]) - sp.diff(Bmat[a, j], X[b]) for j in range(3) for a in range(3) for b in range(3)}
Tl = Tlin(Bm)
epsdotT = sp.simplify(sum(sp.LeviCivita(j, a, b) * Tl[(j, a, b)] for j in range(3) for a in range(3) for b in range(3)))
divth = sum(sp.diff(thf[c], X[c]) for c in range(3))
check("B2 at zero strain a coin rotation theta(x) changes eps.T by -4 div theta (block 65 T4)", sp.simplify(epsdotT + 4 * divth) == 0)
Vb = [sum(Tl[(a, a, b)] for a in range(3)) for b in range(3)]
check("B2 ... and changes the c4 density d_b V_b by 0, det e by tr(B) = 0", sp.simplify(sum(sp.diff(Vb[b], X[b]) for b in range(3))) == 0 and sp.simplify(Bm.trace()) == 0)
Bsym_ = sp.Matrix(3, 3, lambda b, j: sp.Function('h%d' % min(b * 3 + j, j * 3 + b))(*X))
Ts = Tlin(Bsym_)
check("B2 eps.T vanishes at first order for every symmetric strain", sp.simplify(sum(sp.LeviCivita(j, a, b) * Ts[(j, a, b)] for j in range(3) for a in range(3) for b in range(3))) == 0)

# ------------------------------------------------------------------------ C
ok = True
for a in (1, -1):
    for b in (1, -1):
        levels = {n: 2 * a * (3 - 2 * sum(n)) for n in itertools.product((0, 1), repeat=3)}
        top = max(levels.values()); ntop = [n for n, v in levels.items() if v == top]
        sense = lambda n: (1 if b > 0 else -1) * (-1) ** sum(n)       # sign det(beta D_n)
        ok &= len(ntop) == 1 and sense(ntop[0]) == (1 if a * b > 0 else -1)
        # mirror image (Pi): beta -> -beta
        ok &= (-1 if b > 0 else 1) * (-1) ** sum(ntop[0]) == -sense(ntop[0])
check("C one species on the top level +6|a|; its sense is sign(a beta); the mirror image reverses it", ok)

print()
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + FAIL[0])
    sys.exit(1)
print("SUMMARY: PARTIAL generator: the scalar hop a is the one term of the 24-covariant nearest-neighbour family that every "
      "walk-keeping inversion reverses; it survives local-tick timing and blindness (conjugation completion); for a*beta != 0 no "
      "inversion composed with any site-local unitary or antiunitary is a symmetry (chiral 8-loop: tau - tau_mirror = -a^3 beta^5; "
      "a chiral rate field and its mirror image differ first at tr((wH)^8)); field energy: the odd sector at <= 2 derivatives under "
      "the 24 is eps.T alone (plus theta-terms if the rotation is a separate field) and blindness removes all of it")
print("HIT: a parity-odd (Theta-Pi-odd) term survives per-tick timing and blindness: block 54's scalar hop a, with blind "
      "completion -a sum_j S_j[(d_j theta).sigma]; for a*beta != 0 it tells the two mirror classes apart (exact chiral-loop "
      "invariant -a^3 beta^5, exact mirror-field spectral moments); in the field energy no parity-odd term survives blindness")

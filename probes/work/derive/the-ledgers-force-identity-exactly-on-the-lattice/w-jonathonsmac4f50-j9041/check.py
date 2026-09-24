#!/usr/bin/env python3
"""The ledger's force identity exactly on the lattice (attempt 2).

Exact arithmetic only (sympy rationals, Gaussian rationals).  Sections:
  A  content side, reach two (S_j): T3(a),(b) re-checked; exact bond form of the force density;
     exact split  f = (site energies x exact differences of u) + R  with R bilinear in (d phi, d chi);
     support no-go: f_j(x) is not a combination of site energy densities e(y) (reach-2 matrix elements)
  B  field side: a per-tick ledger built from curls, F = sum_x w_x D_x(curls): the exact lattice identity
     is sum_b E_b (d xi)_b = 0 for EVERY rate field; carried rates change F by sum U du only;
     continuum control: a curl-only ledger fails block 66 T1 at second order (the order of the fall)
  D  reach three (P_j = S_j C_j): same statements over 2-bonds, reach-3 support
"""
import itertools, sys
import sympy as sp

FAIL = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)

I2 = sp.eye(2); Z2 = sp.zeros(2, 2)
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]

# ------------------------------------------------------------------ sparse block operators
DIMS = (7, 3, 3)
SITES = list(itertools.product(*[range(n) for n in DIMS]))
def sh(x, j, s):
    y = list(x); y[j] = (y[j] + s) % DIMS[j]; return tuple(y)
def tdist(p, q):
    return sum(min((p[i] - q[i]) % DIMS[i], (q[i] - p[i]) % DIMS[i]) for i in range(3))
def clean(A):
    return {k: v for k, v in A.items() if v != Z2}
def add(*ops):
    out = {}
    for A in ops:
        for k, v in A.items():
            out[k] = out.get(k, Z2) + v
    return clean(out)
def scale(A, c):
    return clean({k: c * v for k, v in A.items()})
def mul(A, B):
    rows = {}
    for (p, q), v in B.items():
        rows.setdefault(p, []).append((q, v))
    out = {}
    for (x, z), a in A.items():
        for (y, b) in rows.get(z, []):
            out[(x, y)] = out.get((x, y), Z2) + a * b
    return clean(out)
def adj(A):
    return {(q, p): v.H for (p, q), v in A.items()}
def sym(A):
    return scale(add(A, adj(A)), sp.Rational(1, 2))
def simp(A):
    return clean({k: v.applyfunc(lambda z: sp.nsimplify(sp.expand(z))) for k, v in A.items()})
def eq(A, B):
    return simp(add(A, scale(B, -1))) == {}
def T(j):
    return {(x, sh(x, j, 1)): I2 for x in SITES}
def diag(f):
    return clean({(x, x): f(x) * I2 for x in SITES})
def proj(x):
    return {(x, x): I2}
def coin_times(M, A):
    return clean({k: M * v for k, v in A.items()})
Tj = [T(j) for j in range(3)]
Sj = [scale(add(Tj[j], scale(adj(Tj[j]), -1)), 1 / (2 * sp.I)) for j in range(3)]
Cj = [scale(add(Tj[j], adj(Tj[j])), sp.Rational(1, 2)) for j in range(3)]
H = add(*[coin_times(SIG[j], Sj[j]) for j in range(3)])
# a generic positive rational clock field phi = sqrt(w)
def phiv(x):
    return 1 + sp.Rational((3 * x[0] * x[0] + 5 * x[1] + 7 * x[2] + x[0] * x[1] * x[2] + 2 * x[0] * x[2]) % 11, 7)
PHI = diag(phiv)
PHIinv = diag(lambda x: 1 / phiv(x))
HW = mul(mul(PHI, H), PHI)
J = 0; e = [1, 0, 0]
def Cw(j, v, step=1):   # (C[v] chi)(x) = 1/2 (v(x) chi(x+step e_j) + v(x-step e_j) chi(x-step e_j))
    out = {}
    for x in SITES:
        out[(x, sh(x, j, step))] = out.get((x, sh(x, j, step)), Z2) + v(x) / 2 * I2
        xm = sh(x, j, -step)
        out[(x, xm)] = out.get((x, xm), Z2) + v(xm) / 2 * I2
    return clean(out)
dphi = lambda x: phiv(sh(x, J, 1)) - phiv(x)

# ---------------------------------------------------------------------------------- A
comm = add(mul(PHI, Sj[J]), scale(mul(Sj[J], PHI), -1))
check("A T3(a): i[phi, S_j] = -C_j[d_j phi] (block 66)", eq(scale(comm, sp.I), scale(Cw(J, dphi), -1)))
# T3(b) with a generic real xi
def xiv(x, j):
    return sp.Rational((x[0] + 2 * x[1] + 3 * x[2] + 5 * j + x[0] * x[2]) % 7, 3) - 1
XI = [diag(lambda x, j=j: xiv(x, j)) for j in range(3)]
G = add(*[scale(add(mul(XI[j], Sj[j]), mul(Sj[j], XI[j])), sp.Rational(1, 2)) for j in range(3)])
Lam = add(*[scale(add(mul(XI[j], Cw(j, lambda x, j=j: phiv(sh(x, j, 1)) - phiv(x))),
                      mul(Cw(j, lambda x, j=j: phiv(sh(x, j, 1)) - phiv(x)), XI[j])), sp.Rational(1, 2)) for j in range(3)])
lhs = scale(add(mul(HW, G), scale(mul(G, HW), -1)), sp.I)
iHG = scale(add(mul(H, G), scale(mul(G, H), -1)), sp.I)
rhs = add(mul(mul(PHI, iHG), PHI), scale(add(mul(mul(Lam, H), PHI), mul(mul(PHI, H), Lam)), -1))
check("A T3(b): i[H_w, G_xi] = phi i[H,G_xi] phi - (Lam H phi + phi H Lam) (block 66)", eq(lhs, rhs))

X0 = (2, 1, 1)
Cv = Cw(J, dphi)
Mx = mul(add(mul(proj(X0), Cv), mul(Cv, proj(X0))), mul(H, PHI))
Fx = sym(Mx)                                 # f_j(x) = <psi| Fx |psi>
LamJ = scale(add(mul(XI[J], Cv), mul(Cv, XI[J])), sp.Rational(1, 2))
check("A the force density's form: sum_x xi_j(x) F_x = Lam_j H phi + phi H Lam_j (so -<Lam H phi + phi H Lam> = -sum xi f, T3(c))",
      eq(add(*[scale(sym(mul(add(mul(proj(x), Cv), mul(Cv, proj(x))), mul(H, PHI))), xiv(x, J)) for x in SITES]),
         add(mul(mul(LamJ, H), PHI), mul(mul(PHI, H), LamJ))))
def Ey(y):
    return sym(mul(proj(y), HW))            # e(y) = Re psi(y)^dag (H_w psi)(y)
def beta(y):   # bond cross energy  Re[psi(y)^dag (H chi)(y+e) + psi(y+e)^dag (H chi)(y)], chi = phi psi
    yp = sh(y, J, 1)
    return sym(add(mul(mul(proj(y), Tj[J]), mul(H, PHI)), mul(mul(proj(yp), adj(Tj[J])), mul(H, PHI))))
xm = sh(X0, J, -1)
bond_form = add(scale(beta(X0), dphi(X0) / 2), scale(beta(xm), dphi(xm) / 2))
check("A1 exact bond form: f_j(x) = 1/2 [ (d_j phi)(x) beta(x) + (d_j phi)(x-e) beta(x-e) ]", eq(Fx, bond_form))
def Rop(y):
    yp = sh(y, J, 1)
    Dy = mul(proj(y), add(mul(Tj[J], PHI), scale(PHI, -1)))                       # chi(y+e) - chi(y) into slot y
    Ay = mul(proj(y), add(scale(mul(H, PHI), 1 / phiv(yp)), scale(mul(mul(Tj[J], H), PHI), -1 / phiv(y))))
    return scale(sym(mul(adj(Dy), Ay)), dphi(y))
def split(y):
    yp = sh(y, J, 1)
    c1 = dphi(y) / phiv(y)          # = exp(du/2) - 1
    c2 = dphi(y) / phiv(yp)         # = 1 - exp(-du/2)
    return add(scale(Ey(yp), c1), scale(Ey(y), c2), Rop(y))
check("A2 exact split of each bond: (d phi) beta = e(y+e)(e^{du/2}-1) + e(y)(1-e^{-du/2}) + R_y",
      eq(scale(beta(X0), dphi(X0)), split(X0)) and eq(scale(beta(xm), dphi(xm)), split(xm)))
# support: energy densities are nearest-neighbour forms; F_x reaches two steps along j
nn_only = all(tdist(p, q) == 1 for y in SITES for (p, q) in Ey(y))
check("A3 every site energy density e(y) is a form on nearest-neighbour pairs only (all %d sites)" % len(SITES), nn_only)
blk = simp(Fx).get((X0, sh(X0, J, 2)), Z2)
print("     block of F_x at (x, x+2e_j):", list(blk), " (d_j phi)(x) =", dphi(X0))
check("A3 F_x has a non-zero block at (x, x+2e_j) when (d_j phi)(x) != 0: no identity f_j(x) = sum_y c_y e(y) exists",
      dphi(X0) != 0 and blk != Z2)
check("A3 the weight part (site energies x exact differences of u) has no such block; R carries it",
      simp(add(scale(Ey(sh(X0, J, 1)), 1), scale(Ey(X0), 1))).get((X0, sh(X0, J, 2)), Z2) == Z2
      and simp(scale(add(Rop(X0), Rop(xm)), sp.Rational(1, 2))).get((X0, sh(X0, J, 2)), Z2) == blk)

# ---------------------------------------------------------------------------------- D (reach three)
Pj = mul(Sj[J], Cj[J])
T2 = mul(Tj[J], Tj[J])
check("D P_j = S_j C_j = (T^2 - T^-2)/(4i) (block 69)", eq(Pj, scale(add(T2, scale(adj(T2), -1)), 1 / (4 * sp.I))))
d2phi = lambda x: phiv(sh(x, J, 2)) - phiv(x)
commP = scale(add(mul(PHI, Pj), scale(mul(Pj, PHI), -1)), sp.I)
check("D i[phi, P_j] = -(1/2) C2_j[d2_j phi], C2 the symmetric two-step hop", eq(commP, scale(Cw(J, d2phi, 2), -sp.Rational(1, 2))))
C2v = Cw(J, d2phi, 2)
FPx = sym(mul(add(mul(proj(X0), C2v), mul(C2v, proj(X0))), mul(H, PHI)))
FPx = scale(FPx, sp.Rational(1, 2))
def beta2(y):
    yp = sh(y, J, 2)
    return sym(add(mul(mul(proj(y), T2), mul(H, PHI)), mul(mul(proj(yp), adj(T2)), mul(H, PHI))))
xm2 = sh(X0, J, -2)
check("D1 exact 2-bond form: fP_j(x) = 1/4 [ (d2 phi)(x) beta2(x) + (d2 phi)(x-2e) beta2(x-2e) ]",
      eq(FPx, add(scale(beta2(X0), d2phi(X0) / 4), scale(beta2(xm2), d2phi(xm2) / 4))))
blk3 = simp(FPx).get((X0, sh(X0, J, 3)), Z2)
check("D3 FP_x has a non-zero block at (x, x+3e_j): no identity fP_j(x) = sum_y c_y e(y) exists", d2phi(X0) != 0 and blk3 != Z2)

# ---------------------------------------------------------------------------------- B (field side, lattice)
L3 = (3, 3, 3); S3 = list(itertools.product(range(3), repeat=3))
def s3(x, j, s=1):
    y = list(x); y[j] = (y[j] + s) % 3; return tuple(y)
Bs = {(x, a, j): sp.Symbol('B_%d%d%d_%d%d' % (x + (a, j))) for x in S3 for a in range(3) for j in range(3)}
def curl(Bf, x, a, b, j):
    return (Bf(s3(x, a), b, j) - Bf(x, b, j)) - (Bf(s3(x, b), a, j) - Bf(x, a, j))
xiF = lambda x, j: sp.Rational((2 * x[0] + x[1] * x[1] + 3 * x[2] + j) % 5, 2)
Bplus = lambda x, a, j: Bs[(x, a, j)] + (xiF(s3(x, a), j) - xiF(x, j))
Bplain = lambda x, a, j: Bs[(x, a, j)]
inv = all(sp.expand(curl(Bplus, x, a, b, j) - curl(Bplain, x, a, b, j)) == 0 for x in S3 for a in range(3) for b in range(3) for j in range(3))
check("B curls unchanged by B -> B + d xi (block 64 T1)", inv)
coef = [sp.Rational(k % 7 - 3, k % 5 + 1) for k in range(200)]
def Dx(Bf, x):
    cs = [curl(Bf, x, a, b, j) for (a, b) in ((0, 1), (0, 2), (1, 2)) for j in range(3)]
    V = [sum(curl(Bf, x, a, b, a) for a in range(3)) for b in range(3)]
    Q = sum(coef[3 * i + k] * cs[i] * cs[k] for i in range(9) for k in range(i, 9))
    return Q + coef[190] * sum(V[b] for b in range(3)) + coef[191] * cs[0] * V[1]
wv = lambda x: 1 + sp.Rational((x[0] + 2 * x[1] * x[2] + x[2]) % 4, 3)
Fplain = sum(wv(x) * Dx(Bplain, x) for x in S3)
Fplus = sum(wv(x) * Dx(Bplus, x) for x in S3)
check("B a per-tick curl ledger F = sum_x w_x D_x(curls), non-uniform w: F(B + d xi) = F(B) exactly",
      sp.expand(Fplus - Fplain) == 0)
Evar = {k: sp.diff(Fplain, s) for k, s in Bs.items()}
ident = sp.expand(sum(Evar[(x, a, j)] * (xiF(s3(x, a), j) - xiF(x, j)) for x in S3 for a in range(3) for j in range(3)))
check("B hence sum_b E_b (d xi)_b = 0 identically in B: the lattice identity has NO rates' term, whatever w", ident == 0)
Uvar = {x: wv(x) * Dx(Bplain, x) for x in S3}     # U_x = dF/du_x
print("     U at a site (a polynomial in B, generically non-zero):", sp.Poly(Uvar[(0, 0, 0)], *Bs.values()).total_degree(), "degree")

# ---------------------------------------------------------------------------------- B (continuum control)
X = sp.symbols('x1:4'); t = sp.Symbol('t')
jets = {}
def jetsym(name):
    if name not in jets:
        jets[name] = sp.Symbol(name)
    return jets[name]
Bj = [[jetsym('B%d%d' % (j, a)) for a in range(3)] for j in range(3)]                  # B^j_a
dB = [[[jetsym('B%d%d_%d' % (j, a, c)) for c in range(3)] for a in range(3)] for j in range(3)]
ddB = {}
for j in range(3):
    for a in range(3):
        for c in range(3):
            for d in range(c, 3):
                ddB[(j, a, c, d)] = jetsym('B%d%d_%d%d' % (j, a, c, d))
def dd(j, a, c, d):
    return ddB[(j, a, min(c, d), max(c, d))]
W = jetsym('w')
# linear torsion T^j_ab = d_a B^j_b - d_b B^j_a ; V_b = T^a_ab ; curl-only density: c4 d_b V_b + q(T)
Tl = lambda j, a, b: dB[j][b][a] - dB[j][a][b]
dV = sum(sum(dd(a, b, a, b) - dd(a, a, b, b) for a in range(3)) for b in range(3))
qT = sum(Tl(j, a, b) ** 2 for j in range(3) for a in range(3) for b in range(3)) / 4 + Tl(0, 0, 1) * Tl(1, 0, 1) / 2
Lag = W * (-2 * dV + qT)
fld_B = [[t * (sp.Rational(a + 1, 3) * X[0] * X[1] + sp.Rational(j - a, 2) * X[2] ** 2 + (j + 2 * a) * X[0] * X[2] / 5 + (1 if a == j else 0) * X[1] ** 2 / 3)
          for a in range(3)] for j in range(3)]
fld_w = 1 + t * (X[0] ** 2 / 2 + X[1] * X[2] / 3 + X[0] / 4)
def subs_fields(expr):
    rep = {W: fld_w}
    for j in range(3):
        for a in range(3):
            rep[Bj[j][a]] = fld_B[j][a]
            for c in range(3):
                rep[dB[j][a][c]] = sp.diff(fld_B[j][a], X[c])
                for d in range(c, 3):
                    rep[ddB[(j, a, c, d)]] = sp.diff(fld_B[j][a], X[c], X[d])
    return expr.subs(rep)
def t1_residual(Lag, dens):
    E = [[None] * 3 for _ in range(3)]
    for j in range(3):
        for a in range(3):
            ex = subs_fields(sp.diff(Lag, Bj[j][a]))
            ex -= sum(sp.diff(subs_fields(sp.diff(Lag, dB[j][a][c])), X[c]) for c in range(3))
            ex += sum(sp.diff(subs_fields(sp.diff(Lag, ddB[(j, a, c, d)])), X[c], X[d]) for c in range(3) for d in range(c, 3))
            E[j][a] = sp.expand(ex)
    Dn = subs_fields(dens)
    res = []
    for b in range(3):
        Rb = sum(E[j][a] * sp.diff(fld_B[j][a], X[b]) for j in range(3) for a in range(3))
        Rb -= sum(sp.diff(E[j][a] * ((1 if j == b else 0) + fld_B[j][b]), X[a]) for j in range(3) for a in range(3))
        Rb += Dn * sp.diff(fld_w, X[b])                 # U d_b u = (w D) d_b log w = D d_b w
        res.append(sp.expand(Rb.subs(pt)))
    return E, res
pt = {X[0]: sp.Rational(1, 3), X[1]: sp.Rational(-1, 2), X[2]: sp.Rational(2, 5)}
ematrix = sp.Matrix(3, 3, lambda j, a: (1 if j == a else 0) + Bj[j][a])
_, res0 = t1_residual(W * ematrix.det(), ematrix.det())
check("B control: the volume density w det e satisfies block 66 T1 exactly in this code (all orders at the point)", all(r == 0 for r in res0))
E, res = t1_residual(Lag, -2 * dV + qT)
divE = [sp.expand(sum(sp.diff(E[j][a], X[a]) for a in range(3))) for j in range(3)]
check("B continuum control: a curl-only per-tick density has d_a E_j^a = 0 identically (all j)", all(dv == 0 for dv in divE))
lead = [sp.Poly(r, t).coeff_monomial(t ** 2) for r in res]
print("     block 66 T1 residual for the curl-only density, t^2 coefficients at a point:", lead)
check("B ... and block 66 T1 FAILS for it at second order in the fields (the order of the fall)",
      any(c != 0 for c in lead) and all(sp.Poly(r, t).coeff_monomial(t) == 0 for r in res))

print()
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + FAIL[0]); sys.exit(1)
print("SUMMARY: PARTIAL content side: f_j(x) = 1/2 sum over the two j-bonds of (d phi) x (bond cross energy), exactly; "
      "= site energies x exact differences (e^{du/2}-1, 1-e^{-du/2}) + a remainder bilinear in (d phi, d chi); no identity "
      "f_j(x) = sum_y c_y e(y) exists (f reaches two steps, every e(y) one); reach three: the same over 2-bonds, reach 3. "
      "Field side: for a per-tick ledger built from curls the exact lattice identity is sum E.(d xi) = 0 for every rate "
      "field; carried rates change F by sum U du and never enter it; a curl-only density fails block 66 T1 at second order")
print("HIT: the per-tick ledger F = sum_x w_x D_x(curls) owes NO weight on the lattice at any order (its exact identity "
      "div dF/dB = 0 holds in every rate field), while the walk's exact balance has force density f = e.du at leading "
      "order: at the order of the fall a static solution needs the strains' force to cancel f site by site; block 66 T1's "
      "weight term comes from non-curl terms (curl-only densities fail T1 at second order, exact); and f is not a "
      "combination of site energies at any order (reach-2 support), only at long wavelength")

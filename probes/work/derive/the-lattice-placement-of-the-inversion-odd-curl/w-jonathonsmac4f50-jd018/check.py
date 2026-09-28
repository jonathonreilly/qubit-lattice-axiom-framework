"""Which lattice placement of block 158's (1/8) eps.C gives each of the walk's eight species its own compensator?

Conventions (block 158, block 70 as landed):
  co-frame e[a][j] = e^a_j, frame E = e^{-1} with E[j][a] = E^j_a; eps.C = eps_abc E^i_b E^j_c (d_i e^a_j - d_j e^a_i).
  Species at the corner A = pi n, D_d = cos A_d = (-1)^{n_d}, s = D1 D2 D3, rho = s D (block 70).
  Block 70 T1(a)/T2: the site-sign map U_n turns a hop along a by D_a; V_n H[E] V_n = s H[rho E rho].
Exact sections A-D (sympy, integers, rationals); section E floating point, labelled.
"""
import sys, time, itertools, random
import sympy as sp

T0 = time.time()
FAILS = []
def want(ok, label):
    print(("PASS " if ok else "FAIL ") + label, flush=True)
    if not ok:
        FAILS.append(label)
eps3 = lambda a, b, c: sp.LeviCivita(a, b, c)
R3 = range(3)
CORNERS = list(itertools.product((1, -1), repeat=3))       # D = (cos A_1, cos A_2, cos A_3)

# ---------------------------------------------------------------------------------------------
# A. The exchange maps on a 4^3 torus (exact integer matrices; block 70 T1(a) re-checked)
# ---------------------------------------------------------------------------------------------
print("== A. site-sign maps on hops of every displacement (exact, 4^3 torus)")
Lt = 4
sites = list(itertools.product(range(Lt), repeat=3))
ok = True
for n in itertools.product((0, 1), repeat=3):
    sign = lambda p: (-1)**(n[0] * p[0] + n[1] * p[1] + n[2] * p[2])
    D = [(-1)**nk for nk in n]
    for m in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 1, 1), (2, 0, 0), (2, 1, 0), (1, 2, 1)]:
        chi_m = D[0]**(m[0] % 2) * D[1]**(m[1] % 2) * D[2]**(m[2] % 2)
        for p in sites:          # entry (p, p+m) of the hop is multiplied by sign(p) sign(p+m) under U_n . U_n
            q = tuple((p[k] + m[k]) % Lt for k in R3)
            ok &= sign(p) * sign(q) == chi_m
    ok &= all(sign(p) * sign(p) == 1 for p in sites)          # site potentials: diagonal entries unchanged
want(ok, "A1 U_n (hop by m with any bond weights) U_n = prod_d D_d^(m_d mod 2) (hop by m); site potentials are unchanged (all 8 n, 9 displacements)")
print("   [A took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# B. What each species needs (exact, generic frame jets at a point)
# ---------------------------------------------------------------------------------------------
print("== B. the compensator each corner needs (exact, generic jets)")
def epsC(e, de, E=None):
    E = e.inv() if E is None else E
    return sp.simplify(sum(eps3(a, b, c) * E[i, b] * E[j, c] * (de[i][a, j] - de[j][a, i])
                           for a in R3 for b in R3 for c in R3 for i in R3 for j in R3))
def Xd(e, de, d, E=None):
    E = e.inv() if E is None else E
    return sp.simplify(2 * sum(eps3(a, b, c) * E[d, b] * E[j, c] * de[d][a, j] for a in R3 for b in R3 for c in R3 for j in R3))
de_sym = [sp.Matrix(3, 3, lambda a, j, i=i: sp.Symbol(f'p{i}{a}{j}')) for i in R3]     # d_i e^a_j, generic
ok1 = ok2 = ok3 = True
for trial in range(4):
    e0 = sp.Matrix(3, 3, lambda a, j: sp.Rational(random.randint(-5, 5), random.randint(1, 4)) + (3 if a == j else 0))
    X = [Xd(e0, de_sym, d) for d in R3]
    C_ = epsC(e0, de_sym)
    ok1 &= sp.simplify(sum(X) - C_) == 0
    for D in CORNERS:
        s = D[0] * D[1] * D[2]; rho = [s * Dk for Dk in D]
        # frame the species sees through V_n (block 70 T2): s * H[rho E rho]; its effective frame is Et = rho E D
        eP = sp.Matrix(3, 3, lambda a, j: rho[a] * e0[a, j] * rho[j]); deP = [sp.Matrix(3, 3, lambda a, j, i=i: rho[a] * de_sym[i][a, j] * rho[j]) for i in R3]
        eT = sp.Matrix(3, 3, lambda a, j: rho[a] * e0[a, j] * D[j]); deT = [sp.Matrix(3, 3, lambda a, j, i=i: rho[a] * de_sym[i][a, j] * D[j]) for i in R3]
        need = sum(D[d] * X[d] for d in R3)
        ok2 &= sp.simplify(s * epsC(eP, deP) - need) == 0
        ok3 &= sp.simplify(epsC(eT, deT) - need) == 0
want(ok1, "B1 eps.C = X_1 + X_2 + X_3 with X_d = 2 eps_abc E^d_b E^j_c d_d e^a_j (the part whose derivative is along d)")
want(ok2, "B2 for every corner, s eps.C[rho E rho] = sum_d cos(A_d) X_d: the species' compensator (1/8) s eps.C of its own frame is N_A = (1/8) sum_d cos A_d X_d")
want(ok3, "B3 equivalently its effective frame rho E D weights the derivatives by cos A_d: eps.C[rho E D] = sum_d cos(A_d) X_d")
print("   [A-B took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# C. Which placement serves which corners (exact)
# ---------------------------------------------------------------------------------------------
print("== C. placements against corners (exact)")
x1, x2, x3 = sp.symbols('X1 X2 X3')
Xs = (x1, x2, x3)
classes = list(itertools.product((0, 1), repeat=3))
W = {c: sp.Symbol('W_%d%d%d' % c) for c in classes}   # long-wavelength weight in displacement-parity class c
def chi(D, c): return D[0]**c[0] * D[1]**c[1] * D[2]**c[2]
def need(D): return sum(D[d] * Xs[d] for d in R3) / 8
sol = sp.solve([sum(chi(D, c) * W[c] for c in classes) - need(D) for D in CORNERS], list(W.values()), dict=True)
want(len(sol) == 1 and all(sp.simplify(sol[0][W[c]] - (Xs[c.index(1)] / 8 if sum(c) == 1 else 0)) == 0 for c in classes),
     "C1 a coin-scalar placement serves all eight corners iff its weight sits only on hops with an odd displacement along exactly one axis d, "
     "totalling X_d/8 there (unique): the per-axis split of eps.C, placed like block 65's twist hop")
def served(weights):
    out = []
    for D in CORNERS:
        p = sum(chi(D, c) * weights.get(c, 0) for c in classes)
        if sp.expand(p - need(D)) == 0: out.append(D)
    return out
total = sum(Xs) / 8
place = {
    'site potential (1/8) eps.C': {(0, 0, 0): total},
    'face-diagonal hops C_1C_2 with weight (1/8) eps.C': {(1, 1, 0): total},
    'body-diagonal C_1C_2C_3 with weight (1/8) eps.C': {(1, 1, 1): total},
    'per-axis hops, axis d carrying X_d/8': {(1, 0, 0): x1 / 8, (0, 1, 0): x2 / 8, (0, 0, 1): x3 / 8},
}
expect = {'site potential (1/8) eps.C': [(1, 1, 1)],
          'face-diagonal hops C_1C_2 with weight (1/8) eps.C': [(1, 1, 1)],
          'body-diagonal C_1C_2C_3 with weight (1/8) eps.C': [(1, 1, 1), (-1, -1, -1)],
          'per-axis hops, axis d carrying X_d/8': CORNERS}
for name, wts in place.items():
    got = served(wts)
    want(sorted(got) == sorted(expect[name]), f"C2 {name}: serves {len(got)} corner(s) {got} for independent X_1, X_2, X_3")
# X_1, X_2, X_3 are independent on the lengths' own frame e = 1 + eta at second order (so 'generic' is attained)
t = sp.Symbol('t')
eta0 = sp.Matrix(3, 3, lambda a, b: sp.Symbol('h%d%d' % (min(a, b), max(a, b))))
deta = [sp.Matrix(3, 3, lambda a, b, k=k: sp.Symbol('g%d_%d%d' % (k, min(a, b), max(a, b)))) for k in R3]
eS = sp.eye(3) + t * eta0; deS = [t * deta[k] for k in R3]
ES = sp.eye(3) - t * eta0 + t**2 * eta0 * eta0            # (1 + t eta)^-1 through t^2
def series2(expr):
    ex = sp.expand(expr)
    return sum(ex.coeff(t, k) * t**k for k in range(3))
Xser = [sp.expand(Xd(eS, deS, d, ES)) for d in R3]
X2 = [Xser[d].coeff(t, 2) for d in R3]
X1o = [Xser[d].coeff(t, 1) for d in R3]
B158 = sp.expand(2 * sum(eps3(a, b, c) * eta0[a, d] * deta[b][c, d] for a in R3 for b in R3 for c in R3 for d in R3))
want(all(v == 0 for v in X1o) and sp.expand(sum(X2) - B158) == 0,
     "C3 lengths' frame e = 1 + eta: every X_d vanishes at first order, and X_1 + X_2 + X_3 = 2 eps_abc eta_ad d_b eta_cd at second (block 158 T1(b))")
jets = []
syms = sorted(set().union(*[v.free_symbols for v in X2]), key=str)
random.seed(7)
for _ in range(3):
    jets.append({sy: sp.Rational(random.randint(-3, 3)) for sy in syms})
Mx = sp.Matrix([[X2[d].subs(j) for d in R3] for j in jets])
want(Mx.det() != 0, f"C4 three lengths' jets give X^(2) values with determinant {Mx.det()} != 0: X_1, X_2, X_3 are independent")
print("   [A-C took %.0f s]" % (time.time() - T0), flush=True)

# ---------------------------------------------------------------------------------------------
# D. Block 161's links as a per-axis placement (exact)
# ---------------------------------------------------------------------------------------------
print("== D. block 161's links, per bond direction (exact)")
# comparator's connection: omega_jab = e^a_k (d_j E^k_b + Gamma^k_jl E^l_b); link scalar per direction L_j = (1/4) E^j_a eps_abc omega_jbc
xs = sp.symbols('y1 y2 y3')
etaF = eta0 + sum((xs[k] * deta[k] for k in R3), sp.zeros(3, 3))          # symmetric eta(x) with the jets above
eF = sp.eye(3) + t * etaF
EF = sp.eye(3) - t * etaF + t**2 * etaF * etaF                       # through t^2
g = eF.T * eF
gi = sp.eye(3) - 2 * t * etaF + 3 * t**2 * etaF * etaF               # (1 + t eta)^-2, eta symmetric
def at0(expr): return expr.subs({xs[0]: 0, xs[1]: 0, xs[2]: 0})
Gam = [[[at0(sum(gi[k, mm] * (sp.diff(g[mm, l], xs[j]) + sp.diff(g[mm, j], xs[l]) - sp.diff(g[j, l], xs[mm])) for mm in R3) / 2)
         for l in R3] for j in R3] for k in R3]
E0 = at0(EF); e0F = at0(eF)
dE = [at0(sp.diff(EF, xs[j])) for j in R3]
def omega(j, a, b):
    return sum(e0F[a, k] * (dE[j][k, b] + sum(Gam[k][j][l] * E0[l, b] for l in R3)) for k in R3)
Lj = [series2(sum(E0[j, a] * eps3(a, b, c) * omega(j, b, c) for a in R3 for b in R3 for c in R3) / 4) for j in R3]
deF = [at0(sp.diff(eF, xs[i])) for i in R3]
epsC_t = series2(epsC(e0F, deF, E0))
want(sp.expand(sum(Lj) - epsC_t / 8) == 0, "D1 the links' scalars sum to (1/8) eps.C through second order (block 161 T4(b) re-derived)")
L1 = [sp.expand(Lj[j].coeff(t, 1)) for j in R3]
L1_expect = [sp.expand(sum(eps3(j, b, c) * deta[c][b, j] for b in R3 for c in R3) / 2) for j in R3]
want(all(sp.expand(L1[j] - L1_expect[j]) == 0 for j in R3) and any(v != 0 for v in L1),
     "D2 at first order the link scalar along axis j is L_j = (1/2) sum_bc eps_jbc d_c eta_bj: nonzero, though the three sum to zero")
free = set().union(*[v.free_symbols for v in L1])
def jetv(name):
    j = {sy: 0 for sy in free}; j[sp.Symbol(name)] = 1
    return [L1[k].subs(j) for k in R3]
va = jetv('g2_01')   # d_3 eta_12 = 1 (symbols are 0-indexed)
vb = jetv('g0_12')   # d_1 eta_23 = 1
err = {D: (sum(D[d] * va[d] for d in R3), sum(D[d] * vb[d] for d in R3)) for D in CORNERS}
spared = [D for D in CORNERS if err[D] == (0, 0)]
want(va == [sp.Rational(1, 2), sp.Rational(-1, 2), 0] and vb == [0, sp.Rational(1, 2), sp.Rational(-1, 2)] and sorted(spared) == sorted([(1, 1, 1), (-1, -1, -1)]),
     f"D3 jets d_3 eta_12 = 1 and d_1 eta_23 = 1 give L = {va} and {vb}; the links' first-order scalar at corner A, sum_d cos A_d L_d = "
     f"(D1 - D3) L_1 + (D2 - D3) L_2, is {dict((str(D), err[D]) for D in CORNERS)}: zero for every jet only at k = 0 and (pi,pi,pi), "
     "whereas every species needs zero at first order")

# ---------------------------------------------------------------------------------------------
# E. FLOATING POINT: the range-1 per-axis hop reproduces X_d/8 at long wavelength
# ---------------------------------------------------------------------------------------------
print("== E. FLOATING POINT: nearest-neighbour per-axis hop v_d = (1/4) eps_abc Ebar^d_b Ebar^j_c (e^a_j(x+e_d) - e^a_j(x))")
import numpy as np
rng = np.random.default_rng(3)
Acoef = rng.normal(size=(3, 3, 3)); Bcoef = rng.normal(size=(3, 3, 3))
def e_field(x, ell):
    return np.eye(3) + 0.3 * np.einsum('ajk,k->aj', Acoef, np.sin(x / ell)) + 0.2 * np.einsum('ajk,k->aj', Bcoef, np.cos(2 * x / ell))
EPS = np.zeros((3, 3, 3))
for a, b, c in itertools.permutations(R3): EPS[a, b, c] = float(sp.LeviCivita(a, b, c))
def X_cont(x, ell, d, hh=1e-6):
    E = np.linalg.inv(e_field(x, ell)); dv = np.zeros(3); dv[d] = hh
    de = (e_field(x + dv, ell) - e_field(x - dv, ell)) / (2 * hh)
    return 2 * np.einsum('abc,b,jc,aj->', EPS, E[d, :], E, de)
def v_lat(x, ell, d):
    dv = np.zeros(3); dv[d] = 1.0
    Eb = 0.5 * (np.linalg.inv(e_field(x, ell)) + np.linalg.inv(e_field(x + dv, ell)))
    return 0.25 * np.einsum('abc,b,jc,aj->', EPS, Eb[d, :], Eb, e_field(x + dv, ell) - e_field(x, ell))
x0 = np.array([0.37, -1.2, 2.05])
errs = []
for ell in (10.0, 20.0, 40.0):
    rel = max(abs(v_lat(x0 * ell, ell, d) - X_cont(x0 * ell + 0.5 * np.eye(3)[d], ell, d) / 8) / abs(X_cont(x0 * ell, ell, d) / 8) for d in R3)
    errs.append(rel); print(f"   ell = {ell}: max relative error of v_d against X_d/8 at the bond midpoint {rel:.2e}")
want(errs[1] < errs[0] / 3 and errs[2] < errs[1] / 3, "E1 the range-1 per-axis hop matches X_d/8 with error falling as ell^-2 (a smooth frame of scale ell)")

print("   [total %.0f s]" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PROVED at long wavelength: the species at corner A needs N_A = (1/8) sum_d cos(A_d) X_d, X_d = 2 eps_abc E^d_b E^j_c d_d e^a_j "
      "(the d-derivative part of eps.C); a coin-scalar placement serves all eight corners iff its weight lies only on hops odd along exactly one axis d, "
      "totalling X_d/8 (unique; realised at range 1 by per-axis hops like block 65's twist hop); a site potential or face-diagonal hops serve only k = 0; "
      "the body-diagonal C1C2C3 serves k = 0 and (pi,pi,pi); block 161's links, split by the connection, also serve only those two and add a first-order "
      "coin scalar sum_d cos A_d L_d to the six mixed species")
print("HIT: exact answer for all eight corners: needed N_A = (1/8) sum_d cos A_d X_d; the unique serving placement is per-axis hops carrying the "
      "d-derivative part X_d/8 of eps.C (range 1); site potential and face diagonals serve only k=0, body diagonal and block 161's connection links serve "
      "only k=0 and (pi,pi,pi), and the links give the six mixed species a spurious first-order scalar (e.g. -(d_3 eta_12 - d_2 eta_13) at (pi,0,0))")

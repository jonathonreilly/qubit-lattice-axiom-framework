#!/usr/bin/env python3
"""The neutral scale and the reflection-positivity bound beyond six axes.  Worked computation, run 2 of 2.

Setting (block 39, landed #8530; block 40, landed #8546; the moving-records reading and the value c = c_0 are SUPPLIED, not adopted).
A site is empty or carries one record with content a in a menu; two neighbouring records weigh c*omega(a,b); a bond with an empty end weighs 1.
Bond kernel with the empty state: B = [[1, 1^T], [1, c*omega]].  Since B(empty, empty) = 1 > 0, B >= 0 exactly when the complement
c*omega - J >= 0 (Schur), J the all-ones kernel.  Block 39 T5: B >= 0 gives reflection positivity through bond planes.
Menus: six axes (reference), eight cube corners, twelve edge midpoints, the 26 directions of a cube, the sphere.  Pair weights: any function of
the symmetry class of the pair (the 'shape parameters'), and the exponential family omega = exp(beta s.s') with unit vectors s.
Exact: sympy (class matrices, their joint eigenvalues, the sphere's Funk-Hecke eigenvalues, the 26-direction quotient).  numpy only for the
cross-checks named 'N'.
"""
import itertools
import numpy as np
import sympy as sp

def out(s): print(s, flush=True)

beta = sp.symbols('beta', real=True)

def menu(name):
    if name == "six axes":
        v = [tuple(s * (i == j) for j in range(3)) for i in range(3) for s in (1, -1)]
    elif name == "eight cube corners":
        v = list(itertools.product((1, -1), repeat=3))
    elif name == "twelve edge midpoints":
        v = sorted({tuple(p) for a in (1, -1) for b in (1, -1) for p in itertools.permutations((a, b, 0))})
    elif name == "26 directions":
        v = [t for t in itertools.product((-1, 0, 1), repeat=3) if any(t)]
    return [sp.Matrix(t) / sp.sqrt(sum(x * x for x in t)) for t in v]

def dots(vs):
    return [[sp.nsimplify(sp.simplify(a.dot(b))) for b in vs] for a in vs]

# ------------------------------------------------------------------ menus on which the symmetry group acts transitively: classes and spectrum
summary_bits = []
for name in ("six axes", "eight cube corners", "twelve edge midpoints"):
    vs = menu(name); N = len(vs); D = dots(vs)
    classes = sorted({D[i][j] for i in range(N) for j in range(N)}, reverse=True)
    counts = [sum(1 for j in range(N) if D[0][j] == t) for t in classes]
    # the class of a pair is its dot product (checked: each value is one orbit of pairs under the cube group, see the class counts below)
    A = [sp.Matrix(N, N, lambda i, j: 1 if D[i][j] == t else 0) for t in classes]
    rows_const = all(all(sum(A[k].row(i)) == counts[k] for i in range(N)) for k in range(len(A)))
    comm = all((A[i] * A[j] - A[j] * A[i]).is_zero_matrix for i in range(len(A)) for j in range(len(A)))
    # joint eigenvalues: a generic integer combination separates the eigenspaces
    # a generic integer combination separates the eigenspaces; checked: every class matrix acts as one scalar on each whole eigenspace
    w = sp.symbols('w0:%d' % len(A))
    for coeffs in ([1, 7, 61, 523, 4099, 32771], [3, 101, 1009, 10007, 100003, 1000003]):
        M = sum((cf * a for cf, a in zip(coeffs, A)), sp.zeros(N, N))
        spec = []; good = True
        for mu, mult in M.eigenvals().items():
            basis = (M - mu * sp.eye(N)).nullspace()
            v = basis[0]; k = next(i for i in range(N) if v[i] != 0)
            lam = [sp.nsimplify((A[c] * v)[k] / v[k]) for c in range(len(A))]
            good &= len(basis) == mult and all((A[c] * b - lam[c] * b).is_zero_matrix for c in range(len(A)) for b in basis)
            spec.append((mult, lam))
        if good:
            break
    out("X %s: joint eigenspaces of the class matrices: dimensions %s, each class matrix a scalar on each: %s"
        % (name, sorted(m for m, _ in spec), "PASS" if good else "FAIL"))
    spec.sort(key=lambda t: (t[0] != 1 or t[1] != counts, t[0]))
    const = [s for s in spec if s[1] == counts]
    others = [s for s in spec if s[1] != counts]
    lab = ", ".join("w%d (dot %s, %d per row)" % (i, classes[i], counts[i]) for i in range(len(classes)))
    out("X %s: N = %d; pair classes %s; every row has the same class counts: %s; the class matrices commute: %s"
        % (name, N, lab, "PASS" if rows_const else "FAIL", "PASS" if comm else "FAIL"))
    R = sum(ci * wi for ci, wi in zip(counts, w))
    out("X %s: (1) row sum R = %s for every content a, so c_0 = N/R = %d/(%s) does not depend on a" % (name, R, N, R))
    forms = []
    for mult, lam in others:
        f = sp.expand(sum(l * wi for l, wi in zip(lam, w)))
        forms.append((mult, f))
    out("X %s: (2) spectrum of omega: %s on the constant vector (where J has N = %d); on its complement (J = 0): %s. Hence B >= 0 exactly when "
        "c >= c_0 and every complement eigenvalue is >= 0; if one is negative, no scale makes B >= 0"
        % (name, R, N, "; ".join("%s (x%d)" % (f, m) for m, f in forms)))
    # exponential family
    ws = [sp.exp(beta * t) for t in classes]
    Rb = sp.simplify(sum(ci * wi for ci, wi in zip(counts, ws)))
    fb = [(m, sp.simplify(f.subs(dict(zip(w, ws))))) for m, f in forms]
    fb_fact = [(m, sp.factor(sp.simplify(f.rewrite(sp.exp)))) for m, f in fb]
    out("X %s, omega = exp(beta s.s'): c_0 = %d/(%s); complement eigenvalues %s"
        % (name, N, Rb, "; ".join("%s (x%d)" % (f, m) for m, f in fb_fact)))
    # signs of the exponential family's complement eigenvalues on a grid of beta (exact values at rational beta)
    grid = [sp.Rational(k, 4) for k in range(-12, 13) if k != 0]
    pos_ok = all(all(sp.N(f.subs(beta, b), 30) > 0 for _, f in fb) for b in grid if b > 0)
    neg_bad = all(any(sp.N(f.subs(beta, b), 30) < 0 for _, f in fb) for b in grid if b < 0)
    out("X %s, omega = exp(beta s.s'): at beta = +-1/4 .. +-3 (step 1/4) every complement eigenvalue is > 0 for beta > 0: %s; some is < 0 for "
        "beta < 0: %s" % (name, "PASS" if pos_ok else "FAIL", "PASS" if neg_bad else "FAIL"))
    # (3) formation-rate multipliers next to two records b1, b2 at c_0: Z/N = c_0^2 (omega^2)(b1,b2)/N (one neighbour: c_0 R/N = 1)
    O = sp.Matrix(N, N, lambda i, j: w[classes.index(D[i][j])])
    O2 = O * O
    c0 = N / R
    rel = {}
    i0 = 0
    for tag, t in (("agreeing", classes[0]), ("opposite", classes[-1])):
        j = next(j for j in range(N) if D[i0][j] == t); rel[tag] = (t, sp.factor(sp.simplify(c0 ** 2 * O2[i0, j] / N)))
    t_orth = 0 if 0 in classes else classes[1]
    j = next(j for j in range(N) if D[i0][j] == t_orth)
    rel["orthogonal" if t_orth == 0 else "nearest (dot %s)" % t_orth] = (t_orth, sp.factor(sp.simplify(c0 ** 2 * O2[i0, j] / N)))
    one = sp.simplify(c0 * R / N)
    out("X %s: (3) at c_0 the formation rate next to one record over its empty-space value is %s; next to two records: %s"
        % (name, one, "; ".join("%s: %s" % (k, v[1]) for k, v in rel.items())))
    relb = {k: sp.simplify(v[1].subs(dict(zip(w, ws)))) for k, v in rel.items()}
    out("X %s, omega = exp(beta s.s'): (3) multipliers %s; at beta = 1: %s; at beta = 3: %s"
        % (name, "; ".join("%s: %s" % (k, v) for k, v in relb.items()),
           ", ".join("%s %.6f" % (k, float(sp.N(v.subs(beta, 1)))) for k, v in relb.items()),
           ", ".join("%s %.6f" % (k, float(sp.N(v.subs(beta, 3)))) for k, v in relb.items())))
    # numerical cross-check: min eigenvalue of B at c_0 (1 -+ 1e-6) for random shape parameters inside and outside the cone
    rng = np.random.default_rng(len(name))
    Dn = np.array([[float(x) for x in row] for row in D])
    ok_n = True
    for trial in range(200):
        wv = rng.uniform(0.05, 3.0, len(classes))
        lamc = [float(sum(l * x for l, x in zip(lam, wv))) for _, lam in others]
        On = np.zeros((N, N))
        for k, t in enumerate(classes): On[np.isclose(Dn, float(t))] = wv[k]
        Rn = On[0].sum(); c0n = N / Rn
        for c, sgn in ((c0n * (1 + 1e-6), +1), (c0n * (1 - 1e-6), -1)):
            Bm = np.ones((N + 1, N + 1)); Bm[1:, 1:] = c * On
            m = np.linalg.eigvalsh(Bm).min()
            expect_psd = (min(lamc) >= 0) and sgn > 0
            if (m > -1e-9) != expect_psd: ok_n = False
    out("N %s: 200 random shape parameters: B >= 0 at c_0 (1 + 1e-6) exactly when the complement eigenvalues are >= 0, and never at c_0 (1 - 1e-6): %s"
        % (name, "PASS" if ok_n else "FAIL"))
    summary_bits.append((name, N, R, forms))

# ------------------------------------------------------------------ the 26 directions: three orbits, row sums not constant
vs = menu("26 directions"); N = len(vs); D = dots(vs)
orbit = lambda t: sum(1 for x in t if x != 0)                       # 1 face, 2 edge, 3 corner (number of nonzero coordinates)
raw = [t for t in itertools.product((-1, 0, 1), repeat=3) if any(t)]
orbs = {1: [i for i, t in enumerate(raw) if orbit(t) == 1], 2: [i for i, t in enumerate(raw) if orbit(t) == 2], 3: [i for i, t in enumerate(raw) if orbit(t) == 3]}
names = {1: "face", 2: "edge", 3: "corner"}
Bq = sp.Matrix(3, 3, lambda X, Y: sp.simplify(sum(sp.exp(beta * D[orbs[X + 1][0]][j]) for j in orbs[Y + 1])))
# check that the quotient is well defined: every member of an orbit has the same sums into each orbit
wd = all(sp.simplify(sum(sp.exp(beta * D[i][j]) for j in orbs[Y]) - Bq[X - 1, Y - 1]) == 0 for X in (1, 2, 3) for i in orbs[X] for Y in (1, 2, 3))
Rs = [sp.simplify(sum(Bq.row(X))) for X in range(3)]
out("X 26 directions (6 face, 12 edge, 8 corner), omega = exp(beta s.s'): sums into the orbits well defined: %s; row sums face %s | edge %s | corner %s"
    % ("PASS" if wd else "FAIL", Rs[0], Rs[1], Rs[2]))
ser = [sp.series(R_, beta, 0, 6).removeO() for R_ in Rs]
out("X 26 directions: (1) row sums to order beta^4: face %s; edge %s; corner %s: equal through beta^2 (the second moment is isotropic), "
    "DIFFERENT at beta^4, so c_0(a) = 26/R(a) depends on the orbit of a" % tuple(sp.expand(s) for s in ser))
uvec = sp.symbols('u1:4')
# c* = 1^T omega^{-1} 1: omega^{-1} 1 is invariant, so it is sum_Y u_Y 1_Y with Bq u = 1
sizes = [len(orbs[1]), len(orbs[2]), len(orbs[3])]
out("X 26 directions: (2) omega is positive semidefinite for beta >= 0 (sum of Schur powers of the Gram kernel) and for beta < 0 the odd vector "
    "v(a) = a_x has v.omega.v(beta) = -v.omega.v(-beta) < 0 with v orthogonal to 1, so B is never >= 0 for beta < 0; for beta > 0, "
    "B >= 0 exactly when c >= c* = 1^T omega^-1 1 = sum_Y |Y| u_Y, Bq u = 1 (omega^-1 1 is invariant under the cube group)")
rows = []
for bv in (sp.Rational(1, 2), 1, 2, 4):
    Bv = Bq.subs(beta, bv); uu = Bv.LUsolve(sp.Matrix([1, 1, 1]))
    cstar = sum(sz * uu[k] for k, sz in enumerate(sizes))
    c0s = [sp.N(26 / R_.subs(beta, bv), 20) for R_ in Rs]
    cbar = sp.N(26 * 26 / sum(sz * R_.subs(beta, bv) for sz, R_ in zip(sizes, Rs)), 20)
    rows.append((bv, sp.N(cstar, 20), c0s, cbar))
    out("X 26 directions, beta = %s: c* = %.10f; c_0(face) = %.10f, c_0(edge) = %.10f, c_0(corner) = %.10f; 26^2/(sum of omega over all pairs) = %.10f "
        "(c* is at least this, Cauchy-Schwarz: %s); c* between min and max of c_0(a): %s; 26 u_Y, omega^-1 1 = sum_Y u_Y 1_Y, for face, edge, corner = %s; the sphere's "
        "beta/sinh(beta) = %.10f" % (bv, float(sp.N(cstar, 20)), float(c0s[0]), float(c0s[1]), float(c0s[2]), float(cbar),
                                      "PASS" if sp.N(cstar, 20) >= cbar else "FAIL", "yes" if min(c0s) <= sp.N(cstar, 20) <= max(c0s) else "no",
                                      ", ".join("%.6f" % float(sp.N(x * 26, 12)) for x in uu), float(sp.N(bv / sp.sinh(bv), 20))))
# numerical cross-check of c* by the smallest eigenvalue of B
Dn = np.array([[float(x) for x in row] for row in D])
chk = []
for bv, cstar, _, _ in rows:
    On = np.exp(float(bv) * Dn)
    ms = []
    for f in (1 - 1e-6, 1 + 1e-6):
        Bm = np.ones((N + 1, N + 1)); Bm[1:, 1:] = float(cstar) * f * On; ms.append(np.linalg.eigvalsh(Bm).min())
    chk.append(ms[0] < 0 < ms[1] or (ms[0] < 0 and abs(ms[1]) < 1e-12))
out("N 26 directions: the smallest eigenvalue of B changes sign at c* for beta = 1/2, 1, 2, 4: %s" % ("PASS" if all(chk) else "FAIL"))
# (3) formation multipliers at c*: next to one record of each orbit, and next to two records (face pairs) agreeing / orthogonal / opposite
bv = 1; Bv = Bq.subs(beta, bv); uu = Bv.LUsolve(sp.Matrix([1, 1, 1])); cst = float(sum(sz * uu[k] for k, sz in enumerate(sizes)))
On = np.exp(bv * Dn)
one = {names[X]: cst * On[orbs[X][0]].sum() / N for X in (1, 2, 3)}
f0 = orbs[1][0]
def pairmult(i, j, c): return c * c * (On[:, i] * On[:, j]).sum() / N
ex = raw.index((1, 0, 0)); ey = raw.index((0, 1, 0)); emx = raw.index((-1, 0, 0))
two = {"agreeing": pairmult(ex, ex, cst), "orthogonal": pairmult(ex, ey, cst), "opposite": pairmult(ex, emx, cst)}
out("N 26 directions, beta = 1, at c*: formation rate next to one record over its empty-space value: %s (not 1: an empty site is not a record of "
    "random content for every orbit); next to two face records: %s"
    % (", ".join("%s %.6f" % kv for kv in one.items()), ", ".join("%s %.6f" % kv for kv in two.items())))

# ------------------------------------------------------------------ the sphere, omega = exp(beta s.s'), uniform normalized measure
t = sp.symbols('t', real=True)
bp = sp.symbols('b', positive=True)          # the integrals below are entire in beta; identities proved for beta > 0 extend to all real beta
mean = sp.simplify(sp.integrate(sp.exp(bp * t), (t, -1, 1)) / 2).subs(bp, beta)
out("X sphere: (1) mean over b of exp(beta a.b) = %s for every a (rotation invariance), so c_0 = beta/sinh(beta): %s"
    % (mean, "PASS" if sp.simplify(1 / mean - beta / sp.sinh(beta)) == 0 else "FAIL"))
okl = True
for l in range(0, 7):
    lam = sp.integrate(sp.exp(bp * t) * sp.legendre(l, t), (t, -1, 1)) / 2
    rod = bp ** l / (2 ** (l + 1) * sp.factorial(l)) * sp.integrate(sp.exp(bp * t) * (1 - t * t) ** l, (t, -1, 1))
    if sp.simplify(sp.expand(lam - rod)) != 0:
        okl = False
out("X sphere: (2) Funk-Hecke eigenvalue on degree-l harmonics lambda_l = (1/2) int exp(beta t) P_l(t) dt = beta^l/(2^(l+1) l!) int exp(beta t) "
    "(1 - t^2)^l dt (Rodrigues, l integrations by parts) for l = 0..6: %s; so lambda_l > 0 for all l when beta > 0 and lambda_l < 0 for odd l when "
    "beta < 0: B >= 0 exactly when beta >= 0 and c >= 1/lambda_0 = beta/sinh(beta)" % ("PASS" if okl else "FAIL"))
c0s = beta / sp.sinh(beta)
m2 = lambda uabs: sp.simplify(c0s ** 2 * (sp.sinh(beta * uabs) / (beta * uabs) if uabs != 0 else 1))
agree, orth, opp = m2(2), m2(sp.sqrt(2)), m2(0)
Up = sp.Symbol('U', positive=True)
chk_int = sp.simplify((sp.integrate(sp.exp(bp * Up * t), (t, -1, 1)) / 2 - sp.sinh(bp * Up) / (bp * Up)).rewrite(sp.exp)) == 0
out("X sphere: (3) at c_0 the rate next to one record is c_0 sinh(beta)/beta = 1; next to two records b1, b2 it is c_0^2 sinh(beta|b1+b2|)/(beta|b1+b2|) "
    "(int over a of exp(beta a.u) = sinh(beta|u|)/(beta|u|): %s): agreeing %s, orthogonal %s, opposite %s; at beta = 1: %.6f, %.6f, %.6f; at beta = 3: "
    "%.6f, %.6f, %.6f" % ("PASS" if chk_int else "FAIL", sp.simplify(agree), orth, opp,
                         *[float(sp.N(x.subs(beta, 1))) for x in (agree, orth, opp)], *[float(sp.N(x.subs(beta, 3))) for x in (agree, orth, opp)]))
# numerical cross-check: a fine discretization of the sphere (Fibonacci points, equal weights) gives the constant-mode bound near beta/sinh(beta)
nfib = 4000; gidx = np.arange(nfib) + 0.5; zf = 1 - 2 * gidx / nfib; ph = np.pi * (1 + 5 ** 0.5) * gidx
P = np.stack([np.sqrt(1 - zf ** 2) * np.cos(ph), np.sqrt(1 - zf ** 2) * np.sin(ph), zf], 1)
for bv in (1.0, 3.0):
    rs = np.exp(bv * P @ P.T).mean(1)
    out("N sphere, beta = %.0f: 4000 Fibonacci points: mean of omega over b = %.6f .. %.6f against sinh(beta)/beta = %.6f"
        % (bv, rs.min(), rs.max(), np.sinh(bv) / bv))

out("")
out("SUMMARY: for every menu on which the cube (or rotation) group acts transitively on contents (six axes, eight corners, twelve edge midpoints, the "
    "sphere) omega has constant row sums and the kernel with the empty state is positive semidefinite exactly when c >= c_0 = N/R AND omega is "
    "positive semidefinite on the complement of the constant vector (linear conditions on the class weights, listed; for omega = exp(beta s.s') "
    "exactly beta >= 0; sphere c_0 = beta/sinh(beta) confirmed); the 26 directions are three orbits, their exp(beta s.s') row sums differ at order "
    "beta^4, so c_0(a) depends on the orbit (face > edge > corner) and the exact floor is c* = 1^T omega^-1 1, which lies between the smallest and the largest "
    "c_0(a) and above 1/(mean of all omega), and is within %s of the sphere's beta/sinh(beta) at beta = 1/2, 1, 2, 4; at c* an empty site next to one "
    "record forms at %s of the empty-space rate at beta = 1" % (", ".join("%.1e" % abs(float(r_[1] - sp.N(r_[0] / sp.sinh(r_[0]), 20))) for r_ in rows),
                                                                 ", ".join("%.5f (%s)" % (v_, k_) for k_, v_ in one.items())))

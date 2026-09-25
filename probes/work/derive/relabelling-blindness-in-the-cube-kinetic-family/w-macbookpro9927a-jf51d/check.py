#!/usr/bin/env python3
"""J:derive:relabelling-blindness-in-the-cube-kinetic-family:a2 -- worker w-macbookpro9927a-jf51d (Claude Opus 5.5).

Exact (sympy) checks.  Block 62 as landed: metric strain h (symmetric), rates' multiplier u, lattice symbols p_j (real),
R1 = p^2 tr h - p.h.p, R2 = -(p^2/4) tr h^2 + |h p|^2/2 - (p.h.p) tr h/2 + (p^2/4)(tr h)^2, Lagrangian
L = T(h') + K (u R1 + R2) (w = 1), cube family T = M1 sum h'_jj^2 + M2 sum_{i<j} h'_ii h'_jj + M3 sum_{i<j} h'_ij^2.
Frame E = 1 + eps (E[j,a]: bond j, coin a), h = -(eps + eps^T), omega = antisymmetric part of eps (coin rotation).
A relabelling xi acts on the frame as d eps = -xi p^T (d h = p xi^T + xi p^T, d omega = (p xi^T - xi p^T)/2).
'Symmetry' = the change of L is a total time derivative for all field histories: only-if via the Euler operator
(which annihilates total derivatives), if via an explicit Lambda."""
import itertools, time
import sympy as sp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"{tag} {'PASS' if ok else 'FAIL'}: {msg}", flush=True)


t = sp.symbols('t')
p1, p2, p3, K = sp.symbols('p1 p2 p3 K', real=True)
M1, M2, M3, N = sp.symbols('M1 M2 M3 N', real=True)
cs = sp.symbols('c0:4', real=True)            # multiplier shift coefficients
b1, b2, b3 = sp.symbols('b1 b2 b3', real=True)
P = sp.Matrix([p1, p2, p3])
PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
OFF = [(0, 1), (0, 2), (1, 2)]
hf = {ij: sp.Function('h%d%d' % (ij[0] + 1, ij[1] + 1))(t) for ij in PAIRS}
wf = {ij: sp.Function('w%d%d' % (ij[0] + 1, ij[1] + 1))(t) for ij in OFF}
u = sp.Function('u')(t)
z = sp.Function('zeta')(t)


def sym(f):
    H = sp.zeros(3)
    for (i, j), v in f.items():
        H[i, j] = v; H[j, i] = v
    return H


def asym(f):
    W = sp.zeros(3)
    for (i, j), v in f.items():
        W[i, j] = v; W[j, i] = -v
    return W


H, W = sym(hf), asym(wf)


def R1(H):
    return P.dot(P) * H.trace() - (P.T * H * P)[0]


def R2(H):
    q = P.dot(P); hp = H * P
    return -q / 4 * (H * H).trace() + hp.dot(hp) / 2 - (P.T * H * P)[0] * H.trace() / 2 + q / 4 * H.trace() ** 2


def Tcube(Hd):
    return (M1 * sum(Hd[j, j] ** 2 for j in range(3)) + M2 * sum(Hd[i, i] * Hd[j, j] for i, j in OFF)
            + M3 * sum(Hd[i, j] ** 2 for i, j in OFF))


def Lag(H, u, W):
    Wd = W.diff(t)
    return Tcube(H.diff(t)) + N * sum(Wd[i, j] ** 2 for i, j in OFF) + K * (u * R1(H) + R2(H))


FIELDS = list(hf.values()) + list(wf.values()) + [u, z]


def euler(expr, f, order=4):
    e = sp.diff(expr, f)
    for n in range(1, order + 1):
        e += (-1) ** n * sp.diff(sp.diff(expr, sp.diff(f, t, n)), t, n)
    return sp.expand(e)


def conditions(dL, extra_syms=()):
    """coefficients (in field derivatives, p and extra symbols) of every Euler derivative of dL"""
    derivs = [sp.diff(g, t, n) for g in FIELDS for n in range(8, -1, -1)]
    reps = {d: sp.Symbol('D%d' % k) for k, d in enumerate(derivs)}
    eqs = set()
    for f in FIELDS:
        E = euler(dL, f).subs(reps)
        if E == 0:
            continue
        for cf in sp.Poly(E, *reps.values()).coeffs():
            for cc in sp.Poly(sp.expand(cf), p1, p2, p3, *extra_syms).coeffs():
                eqs.add(cc)
    return list(eqs)


du = sum(cs[n] * sp.diff(z, t, n) for n in range(4))
L0 = Lag(H, u, W)

# ---------------------------------------------------------------- A: forms in h' (block 124 T5's family) and the rotation part
xi_g = P * z / 2                                  # gradient relabelling: d h = p p^T zeta (d eps = -xi p^T symmetric)
dL = sp.expand(Lag(H + P * xi_g.T + xi_g * P.T, u + du, W) - L0)
eq_g = conditions(dL)
sol_g = sp.solve(eq_g, [M1, M2, M3, N] + list(cs), dict=True)
c = sp.Symbol('c')
lam = sp.expand(dL.subs({M1: 0, M2: c, M3: -c, cs[0]: 0, cs[1]: 0, cs[2]: c / K, cs[3]: 0}))
Lam = c * z.diff(t) * R1(H)                        # explicit total-derivative witness
ok = sol_g == [{M1: 0, M2: K * cs[2], M3: -K * cs[2], cs[0]: 0, cs[1]: 0, cs[3]: 0}] and sp.simplify(lam - Lam.diff(t)) == 0
check("A1", ok, "gradient relabelling h -> h + p p^T zeta(t) with u -> u + sum_n c_n zeta^(n): a symmetry iff "
      "(M1, M2, M3) = (0, c, -c) and u -> u + (c/K) zeta'' (c_0 = c_1 = c_3 = 0), N free; change = d(c zeta' R1)/dt")

xi_t = P.cross(sp.Matrix([b1, b2, b3])) * z        # transverse: xi = (p x b) zeta(t)
dom = (P * xi_t.T - xi_t * P.T) / 2               # omega's change from d eps = -xi p^T
dL = sp.expand(Lag(H + P * xi_t.T + xi_t * P.T, u + du, W + dom) - L0)
eq_t = conditions(dL, (b1, b2, b3))
sol_t = sp.solve(eq_t, [M2, M3, N] + list(cs), dict=True)
ok = sol_t == [{M2: 2 * M1, M3: 0, N: 0, cs[0]: 0, cs[1]: 0, cs[2]: 0, cs[3]: 0}]
dL0 = sp.expand(Lag(H + P * xi_t.T + xi_t * P.T, u, W + dom).subs({M2: 2 * M1, M3: 0, N: 0}) - L0.subs({M2: 2 * M1, M3: 0, N: 0}))
check("A2", ok and dL0 == 0, "transverse relabelling xi = (p x b) zeta(t): a symmetry iff (M1, M2, M3) = (M, 2M, 0), N = 0 and no "
      "multiplier shift; then the Lagrangian is exactly unchanged (the pure trace term M (tr h')^2)")
both = sp.solve(eq_g + eq_t, [M1, M2, M3, N] + list(cs), dict=True)
check("A3", both == [{M1: 0, M2: 0, M3: 0, N: 0, cs[0]: 0, cs[1]: 0, cs[2]: 0, cs[3]: 0}],
      "both relabelling demands together (the union of all Euler-operator conditions): only the zero kinetic term")

# ---------------------------------------------------------------- B: the frame's full rate with the cube's symmetry
V = sp.Matrix(3, 3, sp.symbols('v0:9'))
vec = list(V)
Q = sp.Matrix(9, 9, lambda i, j: sp.Symbol('q_%d_%d' % (min(i, j), max(i, j))))
qs = sorted(Q.free_symbols, key=str)
R4 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])          # quarter turn about e3
R3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])           # third turn about (1,1,1)
Pi = sp.Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])        # inversion
eqs = []
for R in (R4, R3, Pi):
    Vr = list(R * V * R.T)
    A = sp.Matrix(9, 9, lambda i, j: sp.diff(Vr[i], vec[j]))  # linear action on the 9 components
    eqs += list(A.T * Q * A - Q)
solQ = sp.solve(eqs, qs, dict=True)[0]
Qg = Q.subs(solQ)
free = sorted(Qg.free_symbols, key=str)
S_ = (V + V.T) / 2; A_ = (V - V.T) / 2
basis = [sum(V[j, j] ** 2 for j in range(3)), sum(V[i, i] * V[j, j] for i, j in OFF),
         sum(S_[i, j] ** 2 for i, j in OFF), sum(A_[i, j] ** 2 for i, j in OFF)]
form = sp.expand((sp.Matrix([vec]) * Qg * sp.Matrix(vec))[0])
cb = sp.symbols('k0:4')
match = sp.solve(sp.Poly(sp.expand(form - sum(k * bb for k, bb in zip(cb, basis))), *vec).coeffs(), cb + tuple(free), dict=True)
ok = len(free) == 4 and len(match) == 1 and all(match[0].get(k) is not None for k in cb) and len(set(match[0][k] for k in cb)) == 4
check("B1", ok, "quadratic forms in the frame's full rate V (9 components) invariant under the cube group (V -> R V R^T): "
      "exactly 4 numbers, sum V_jj^2, sum V_ii V_jj, sum sym(V)_ij^2 and sum antisym(V)_ij^2; no cross term (T1g vs T2g)")
Om = asym({ij: sp.Symbol('o%d%d' % ij) for ij in OFF})
n1, n2, n3, n4 = sp.symbols('n1:5')
Qn = n1 * basis[0] + n2 * basis[1] + n3 * basis[2] + n4 * basis[3]
shift = sp.expand(Qn.subs({vec[k]: (V + Om)[k] for k in range(9)}, simultaneous=True) - Qn)
okb = sp.solve(sp.Poly(shift, *vec, *Om.free_symbols).coeffs(), [n1, n2, n3, n4], dict=True) == [{n4: 0}]
check("B2", okb, "blindness to coin rotations in time (V -> V + antisymmetric, arbitrary at each tick; block 124 T1): iff the "
      "antisymmetric number vanishes; the other three are free (block 62's cube family), so a count of two needs T1's metric premise")
check("B3", sol_g[0].get(N, N) == N and sol_t[0][N] == 0,
      "with the rotation part N: the gradient demand leaves N free (a gradient relabelling does not rotate the frame); the "
      "transverse demand forces N = 0; rotation blindness + gradient -> (0, c, -c, 0) = block 62's member at beta = -alpha")

# ---------------------------------------------------------------- C: modes of the survivors
X = sp.Symbol('X')
al = sp.Symbol('alpha', positive=True)
qv = list(hf.values()) + [u] + list(wf.values())
sub = {M1: 0, M2: -2 * al, M3: 2 * al}
Lk = sp.expand(Tcube(H.diff(t)).subs(sub) + N * sum(W.diff(t)[i, j] ** 2 for i, j in OFF))
Lp = sp.expand(K * (u * R1(H) + R2(H)))
dq = [sp.diff(q, t) for q in qv]
A = sp.Matrix(10, 10, lambda i, j: sp.diff(Lk, dq[i], dq[j]))
C = sp.Matrix(10, 10, lambda i, j: sp.diff(Lp, qv[i], qv[j]))
spec = {}
PV = ((1, 2, 2), (sp.Rational(2, 5), sp.Rational(1, 3), -sp.Rational(3, 7)))
for pv in PV:
    rep = {p1: pv[0], p2: pv[1], p3: pv[2], K: 1, al: 1}
    Mx = (X * A + C).subs(rep)
    Mh = Mx[:7, :7]                                # (h, u) block; the rotation block decouples
    r = Mh.rank()
    g = 0
    for rows in itertools.combinations(range(7), r):
        for cols in itertools.combinations(range(7), r):
            g = sp.gcd(g, Mh.extract(list(rows), list(cols)).det())
    spec[pv] = (r, sp.factor(g), Mx[7:, :7].is_zero_matrix and Mx[:7, 7:].is_zero_matrix, sp.factor(Mx[7:, 7:].det()))
ok = True
for pv in PV:
    r, g, dec, rot = spec[pv]
    q2 = sum(v ** 2 for v in pv)
    roots = sp.roots(sp.Poly(g, X))
    ok &= r == 6 and dec and roots.get(sp.Rational(q2, 4)) == 2 and set(roots) <= {0, sp.Rational(q2, 4)}
    ok &= sp.simplify(rot - 8 * N ** 3 * X ** 3) == 0
check("C1", ok, "survivor (0, c, -c), c = -2 alpha, K = alpha = 1, at p = (1,2,2) and (2/5,1/3,-3/7): the (h, u) pencil X A + C "
      "has normal rank 6 (one gauge direction) and the gcd of its 6x6 minors is " + str(spec[PV[0]][1]) + " at the first p: "
      "roots X = p^2/4 twice (the travelling pair) and X = 0; the rotation block decouples with det (2 N X)^3")
# the travelling pair is transverse traceless; the gradient direction is null at every X
pv = (1, 2, 2); rep = {p1: 1, p2: 2, p3: 2, K: 1, al: 1, N: 1}
Mx = (X * A + C).subs(rep)
gvec = sp.Matrix([1, 4, 4, 2, 2, 4, 0, 0, 0, 0])      # h = p p^T at p = (1,2,2)
gvec[6] = 2 * X                                      # u = 2 alpha X / K
ns = Mx.subs(X, sp.Rational(9, 4)).nullspace()
NS = sp.Matrix.hstack(*ns)
# transverse traceless vectors with u = 0 and no rotation, inside the null space
y = sp.symbols('y0:%d' % len(ns))
v = NS * sp.Matrix(y)
Hv = sp.Matrix(3, 3, lambda i, j: v[PAIRS.index((min(i, j), max(i, j)))])
cons = list(Hv * sp.Matrix(pv)) + [Hv.trace(), v[6], v[7], v[8], v[9]]
tt_dim = len(ns) - sp.Matrix([[sp.diff(cc, yy) for yy in y] for cc in cons]).rank()
g_in = sp.Matrix.hstack(NS, gvec.subs(X, sp.Rational(9, 4))).rank() == len(ns)
check("C2", len(ns) == 3 and tt_dim == 2 and g_in and sp.simplify(Mx * gvec) == sp.zeros(10, 1),
      "at X = p^2/4 the null space is 3-dimensional: the transverse traceless pair (u = 0, no rotation) plus the gauge "
      "vector (p p^T, u = 2 alpha X/K), which is null at every X: the gradient relabelling with the multiplier")

npass = sum(1 for _, x in RES if x)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass} ({time.time() - T0:.0f}s)")
if npass == len(RES):
    print("SUMMARY: PARTIAL (a) agreement with block 124 T5 by an independent Euler-operator derivation, with the multiplier "
          "shift unique; (b) exact classification in the frame's full rate; (c) the survivors' modes")
    print("HIT: (a) in block 62's cube family the gradient relabelling in time is a symmetry of K(u R1 + R2) + kinetic iff "
          "(M1, M2, M3) = (0, c, -c) with u -> u + (c/K) zeta'' (the only multiplier shift among zeta, zeta', zeta'', zeta'''); a "
          "transverse one iff (M, 2M, 0) with no shift; both only for zero; (b) in the frame's full rate the cube's symmetry "
          "allows exactly four numbers (M1, M2, M3, N), N on the frame's rotation part: blindness to coin rotations in time "
          "forces N = 0 and leaves three (the count of two needs block 124's metric premise); the gradient demand forces "
          "(0, c, -c) and leaves N; the transverse demand forces (M, 2M, 0) and N = 0; rotation blindness with the gradient "
          "demand leaves block 62's member at beta = -alpha; (c) for (0, c, -c), c = -2 alpha < 0: one travelling pair, "
          "transverse traceless, X = K p^2/(4 alpha) with p_j = 2 sin(k_j/2); every other mode has X = 0 (the transverse "
          "relabellings and, if N != 0, the three rotations drift) or is the gradient gauge direction")
else:
    print("SUMMARY: ROUTE FAILS AT " + ",".join(tg for tg, x in RES if not x))

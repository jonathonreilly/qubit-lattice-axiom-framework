"""C5 R11-3 (b): the volume options V1-V3 in linearized gravity (continuum symbol = the box graviton's symbol on its box, R9-9:
d(q) = q for |q_a| <= 1, so in-box statements are exact for the box graviton; out-of-box only the symbol changes).
Checks:
 (1) linearized Bianchi identity d^mu G_mu nu[h] = 0 (sympy, symbolic functions of t, x, y, z);
 (2) per option, the Fourier mode count of the Fierz-Pauli (= linearized EH) quadratic form restricted to the option's subspace,
     modulo the option's residual gauge directions: degree and roots in w^2 of the reduced determinant at fixed q.
     V1: all 10 h_mu nu (full linear diffeos, 4 gauge).
     V2: h_ii = 0 (sqrt(h) fixed per site), lapse h_00 and shift h_0i free. Residual gauge: xi_0 arbitrary, xi_i transverse.
     V3: h_ii = 0 and h_00 = 0 (lapse fixed). Residual gauge at w != 0: xi_i transverse only.
 (3) the lost equations: which components of E_mu nu = G_mu nu - (kappa/2) T_mu nu are NOT imposed by each option, and what
     Bianchi + matter conservation give back (stated in the report; the sympy part checks the identity it rests on).
"""
import sympy as sp, numpy as np, itertools
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]; eta = sp.diag(-1, 1, 1, 1)
# (1) Bianchi identity, symbolic h_{mu nu}(t,x,y,z)
H = sp.Matrix(4, 4, lambda i, j: sp.Function('h%d%d' % (min(i, j), max(i, j)))(*X))
up = lambda M: eta*M*eta
Hu = up(H); trh = sum(eta[i, i]*H[i, i] for i in range(4))
d = lambda f, mu: sp.diff(f, X[mu])
box = lambda f: sum(eta[m, m]*d(d(f, m), m) for m in range(4))
def Ric(mu, nu):
    return sp.Rational(1, 2)*(sum(d(d(Hu[l, :].dot(sp.Matrix([1 if c == nu else 0 for c in range(4)])), l), mu) for l in range(4))
                              + sum(d(d(Hu[l, mu] if False else sum(eta[l, a]*H[a, mu] for a in range(4)), l), nu) for l in range(4))
                              - d(d(trh, mu), nu) - box(H[mu, nu]))
# careful version: R_mu nu = 1/2( d_l d_mu h^l_nu + d_l d_nu h^l_mu - d_mu d_nu h - box h_mu nu ), h^l_nu = eta^{l a} h_{a nu}
def hmix(l, nu): return sum(eta[l, a]*H[a, nu] for a in range(4))
def Ric(mu, nu):
    return sp.Rational(1, 2)*(sum(d(d(hmix(l, nu), l), mu) for l in range(4)) + sum(d(d(hmix(l, mu), l), nu) for l in range(4))
                              - d(d(trh, mu), nu) - box(H[mu, nu]))
R = sp.Matrix(4, 4, lambda i, j: Ric(i, j)); Rs = sum(eta[i, i]*R[i, i] for i in range(4))
G = R - sp.Rational(1, 2)*eta*Rs
bian = [sp.simplify(sum(eta[m, m]*d(G[m, nu], m) for m in range(4))) for nu in range(4)]
pr('(1) linearized Bianchi d^mu G_mu nu = 0 for all nu:', all(b == 0 for b in bian))

# (2) Fourier mode counts. k_mu = (-w, 0, 0, q) (lower), k^mu = (w, 0, 0, q); d_mu -> i k_mu; G is real-homogeneous of degree 2 in k.
w, q = sp.symbols('w q', positive=True)
kl = [-w, 0, 0, q]
idx = [(i, j) for i in range(4) for j in range(i, 4)]
hs = sp.symbols('a0:10')
Hm = sp.zeros(4, 4)
for n, (i, j) in enumerate(idx): Hm[i, j] = hs[n]; Hm[j, i] = hs[n]
def Gk(Hm):
    hmixk = lambda l, nu: sum(eta[l, a]*Hm[a, nu] for a in range(4))
    tr = sum(eta[i, i]*Hm[i, i] for i in range(4)); k2 = sum(eta[i, i]*kl[i]**2 for i in range(4))
    # d_a d_b -> -k_a k_b
    Rk = sp.Matrix(4, 4, lambda mu, nu: sp.Rational(1, 2)*(-sum(kl[l]*eta[l, l]*0 for l in range(4))))
    def Ricf(mu, nu):
        s1 = -sum(sum(eta[l, l2]*kl[l2] for l2 in range(4))*0 for l in range(4))
        # sum_l d_l d_mu h^l_nu -> -sum_l k_l k_mu h^l_nu
        t1 = -sum(kl[l]*kl[mu]*hmixk(l, nu) for l in range(4))
        t2 = -sum(kl[l]*kl[nu]*hmixk(l, mu) for l in range(4))
        t3 = kl[mu]*kl[nu]*tr
        t4 = k2*Hm[mu, nu]          # -box h -> +k^2 h  (box -> -k^2)
        return sp.Rational(1, 2)*(t1 + t2 + t3 + t4)
    Rk = sp.Matrix(4, 4, lambda i, j: Ricf(i, j)); Rsk = sum(eta[i, i]*Rk[i, i] for i in range(4))
    return Rk - sp.Rational(1, 2)*eta*Rsk
Gm = Gk(Hm)
Q = sp.expand(sum(sum(eta[i, i]*eta[j, j]*Hm[i, j]*Gm[i, j] for j in range(4)) for i in range(4)))   # h^{mu nu} G_mu nu
M = sp.hessian(Q, hs)
pr('(2) quadratic form symmetric:', sp.simplify(M - M.T) == sp.zeros(10, 10))
def gauge_vec(xi):   # h_mu nu = k_mu xi_nu + k_nu xi_mu (xi lower)
    v = []
    for (i, j) in idx: v.append(kl[i]*xi[j] + kl[j]*xi[i])
    return sp.Matrix(v)
# check gauge null vectors of full M
for a in range(4):
    xi = [0]*4; xi[a] = 1
    g = gauge_vec(xi); pr('    gauge xi_%d null: %s' % (a, sp.simplify(M*g) == sp.zeros(10, 1)))
def comp(i, j): return idx.index((min(i, j), max(i, j)))
def reduced_det(constraints, gauges, label):
    # subspace: vectors in R^10 satisfying linear constraints (list of 10-vectors c with c.h = 0)
    C = sp.Matrix([list(c) for c in constraints]) if constraints else sp.zeros(0, 10)
    basis = (C.nullspace() if constraints else [sp.eye(10)[:, n] for n in range(10)])
    Sb = sp.Matrix.hstack(*basis)            # 10 x s
    # gauge vectors (must lie in subspace): express in basis
    Gv = [gauge_vec(g) for g in gauges]
    for gv in Gv:
        assert sp.simplify(C*gv) == sp.zeros(C.rows, 1) if constraints else True
    # complement of gauge within subspace: take coordinates, choose rows to drop by pivoting at numeric point
    s = Sb.shape[1]
    coords = [Sb.solve_least_squares(gv) for gv in Gv]
    Gc = sp.Matrix.hstack(*coords) if coords else sp.zeros(s, 0)
    # pick complement via numeric rank test
    num = {w: sp.Rational(7, 5), q: sp.Rational(1, 1)}
    keep = []
    cur = Gc.subs(num)
    for n in range(s):
        trial = sp.Matrix.hstack(cur, sp.eye(s)[:, n])
        if trial.rank() > cur.rank(): keep.append(n); cur = trial
    P = Sb*sp.Matrix.hstack(*[sp.eye(s)[:, n] for n in keep]) if keep else sp.zeros(10, 0)
    Mr = sp.simplify(P.T*M*P)
    dt = sp.factor(sp.simplify(Mr.det()))
    pr('  %s: subspace dim %d, gauge %d, reduced %d ; det = %s' % (label, s, len(Gv), len(keep), dt))
    return dt
pr('(2) reduced determinants (q along z; zeros in w give the propagating modes; w-independent factors are constraints):')
trc = [0]*10
for i in range(1, 4): trc[comp(i, i)] = 1
h00 = [0]*10; h00[comp(0, 0)] = 1
# transverse xi: xi_x, xi_y (q along z)
d1 = reduced_det([], [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 'V1 (GR)')
d2 = reduced_det([trc], [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], 'V2 (h_ii=0)')
d3 = reduced_det([trc, h00], [[0, 1, 0, 0], [0, 0, 1, 0]], 'V3 (h_ii=0, h_00=0)')
pr('  roots in w (q=1): V1 %s ; V2 %s ; V3 %s' % tuple(sp.solve(sp.Eq(dd.subs(q, 1), 0), w) for dd in (d1, d2, d3)))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')

#!/usr/bin/env python3
"""T68 kill check: independent re-derivation (different method from the attacker's orbit sums).

A. Classification by random-point linear algebra (numpy SVD), not orbit sums:
   unknown c over all 550 monomials (h h k k). Conditions: S3T generators, and G.
B. Explicit Fierz-Pauli built with a constant "graviton" metric diag(-c2,1,1,1)
   (indices raised with it) -> check S3T+G invariance, read K_m, K_s, alpha,
   solve the static field of a rest-mass source, compare gamma with 1/c_g^2.
C. The campaign's own shift-free member (u, h_ij; K_m=K_s=K; beta=-alpha, alpha free):
   b112-type symmetry holds for every alpha; static gamma = 1 for every alpha; TT speed^2 = K/(4alpha)
   (so bending x2 does NOT track the cone there).
D. Shift-free restriction of the G-invariant family: K_m/alpha is fixed only when the
   shift-carrying transformation is imposed (compensating u-shift coefficient).
"""
import itertools, random, sys
import numpy as np
import sympy as sp
from sympy import Rational as R

random.seed(1); np.random.seed(1)
pairs = [(m, n) for m in range(4) for n in range(m, 4)]
pidx = {p: i for i, p in enumerate(pairs)}

def hv(m, n):
    return pidx[(min(m, n), max(m, n))]

# ---------------- monomials ----------------
monos = []
for a in itertools.combinations_with_replacement(range(10), 2):
    for b in itertools.combinations_with_replacement(range(10, 14), 2):
        monos.append(a + b)
NM = len(monos)

def sym_h(hvec):
    H = np.zeros((4, 4))
    for (m, n), i in pidx.items():
        H[m, n] = H[n, m] = hvec[i]
    return H

def h_from_mat(H):
    return np.array([H[m, n] for (m, n) in pairs])

def mono_vec(hvec, k):
    v = np.concatenate([hvec, k])
    return np.array([v[m[0]] * v[m[1]] * v[m[2]] * v[m[3]] for m in monos])

# group generators as (perm, signs) acting on index labels 0..3
def act(g, hvec, k):
    perm, sgn = g
    H = sym_h(hvec)
    H2 = np.zeros((4, 4))
    for m in range(4):
        for n in range(4):
            H2[perm[m], perm[n]] += 0
    # (g.h)_{pi(m) pi(n)} = s_m s_n h_{mn} ; (g.k)_{pi(m)} = s_m k_m
    Hn = np.zeros((4, 4)); kn = np.zeros(4)
    for m in range(4):
        kn[perm[m]] = sgn[m] * k[m]
        for n in range(4):
            Hn[perm[m], perm[n]] = sgn[m] * sgn[n] * H[m, n]
    return h_from_mat(Hn), kn

ident = [0, 1, 2, 3]
gens = {
    'flip1': (ident, [1, -1, 1, 1]), 'flip2': (ident, [1, 1, -1, 1]), 'flip3': (ident, [1, 1, 1, -1]),
    'timeflip': (ident, [-1, 1, 1, 1]),
    'swap12': ([0, 2, 1, 3], [1, 1, 1, 1]), 'cyc123': ([0, 2, 3, 1], [1, 1, 1, 1]),
}
gens_B4_extra = {'swap01': ([1, 0, 2, 3], [1, 1, 1, 1]), 'cyc0123': ([1, 2, 3, 0], [1, 1, 1, 1])}

def build_rows(gen_list, with_G, npts=900):
    rows = []
    for _ in range(npts):
        hvec = np.random.randn(10); k = np.random.randn(4)
        base = mono_vec(hvec, k)
        for g in gen_list:
            h2, k2 = act(g, hvec, k)
            rows.append(mono_vec(h2, k2) - base)
        if with_G:
            xi = np.random.randn(4)
            H = sym_h(hvec) + np.outer(k, xi) + np.outer(xi, k)
            rows.append(mono_vec(h_from_mat(H), k) - base)
    return np.array(rows)

def nullity(A, tol=1e-8):
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s < tol * s[0])), s

def nullspace(A, tol=1e-8):
    u, s, vt = np.linalg.svd(A)
    r = int(np.sum(s > tol * s[0]))
    return vt[r:]

print('== A. classification by random-point linear algebra ==')
S3T = list(gens.values())
nS3T, _ = nullity(build_rows(S3T, False))
nS3TG, _ = nullity(build_rows(S3T, True))
nG, _ = nullity(build_rows([], True))
B4 = S3T + list(gens_B4_extra.values())
nB4, _ = nullity(build_rows(B4, False))
nB4G, _ = nullity(build_rows(B4, True))
print(f'  S3T-invariant: {nS3T} (attacker/P4: 26);  S3T+G: {nS3TG} (2);  B4: {nB4} (9);  B4+G: {nB4G} (1);  G alone: {nG}')

# ---------------- B. explicit Fierz-Pauli with graviton metric diag(-c2,1,1,1) (Euclid: 1/c2 on k0 slot) ---------
c2 = sp.symbols('c2', positive=True)   # c_g^2 in units of matter speed^2 = 1
hs = sp.symbols('h00 h01 h02 h03 h11 h12 h13 h22 h23 h33')
ks = sp.symbols('k0:4')
xis = sp.symbols('x0:4')
def Hmat(sym=hs):
    return sp.Matrix(4, 4, lambda m, n: sym[hv(m, n)])
h = Hmat()
kv = sp.Matrix(ks)

def FP(Ginv, a=1):
    """Euclidean Fierz-Pauli with indices raised by Ginv (constant symmetric inverse metric).
    Q = 1/2 k^2 h.h - |h k|^2 + (k h k) tr h - 1/2 k^2 (tr h)^2  (all contractions with Ginv)."""
    k2 = (kv.T * Ginv * kv)[0, 0]
    hh = (Ginv * h * Ginv * h).trace()
    trh = (Ginv * h).trace()
    hk = h * Ginv * kv
    hk2 = (hk.T * Ginv * hk)[0, 0]
    khk = (kv.T * Ginv * h * Ginv * kv)[0, 0]
    return sp.expand(a * (R(1, 2) * k2 * hh - hk2 + khk * trh - R(1, 2) * k2 * trh ** 2))

Ginv = sp.diag(1 / c2, 1, 1, 1)     # Euclidean: k0 enters as k0^2/c_g^2
Q = FP(Ginv)
# G invariance
sub = {hs[hv(m, n)]: hs[hv(m, n)] + ks[m] * xis[n] + ks[n] * xis[m] for (m, n) in pairs}
dG = sp.simplify(sp.expand(Q.subs(sub, simultaneous=True) - Q))
print('\n== B. FP with graviton metric: G-invariance residual:', dG)

# S3T invariance (flip spatial axes, time flip, swaps): Ginv is invariant, FP is O(4)-like covariant for diag Ginv
def check_group(Q):
    ok = True
    for name, (perm, sgn) in gens.items():
        sub2 = {}
        for (m, n) in pairs:
            # (g.h)_{pi(m) pi(n)} = s_m s_n h_mn  -> substitute h_{pi(m)pi(n)} := s_m s_n h_{mn}
            sub2[hs[hv(perm[m], perm[n])]] = sgn[m] * sgn[n] * hs[hv(m, n)]
        for m in range(4):
            pass
        ksub = {ks[perm[m]]: sgn[m] * ks[m] for m in range(4)}
        sub2.update(ksub)
        res = sp.expand(Q.subs(sub2, simultaneous=True) - Q)
        if res != 0:
            print('   NOT invariant under', name); ok = False
    return ok
print('   S3T invariance of FP(graviton metric):', check_group(Q))

# read off K_m, K_s, alpha, TT speed
def readoff(Q):
    q = sp.expand(Q)
    # kinetic: h0mu=0, k=(k0,0,0,0)
    sub = {hs[hv(0, n)]: 0 for n in range(4)}; sub.update({ks[1]: 0, ks[2]: 0, ks[3]: 0})
    qk = sp.expand(q.subs(sub) / ks[0] ** 2)
    Ao = qk.coeff(hs[hv(1, 2)], 2)                # coefficient of h12^2 -> equals alpha_offdiag
    Ad_plus_B = qk.coeff(hs[hv(1, 1)], 2)
    B = qk.coeff(hs[hv(1, 1)], 1).coeff(hs[hv(2, 2)], 1) / 2
    Ad = Ad_plus_B - B
    alpha = Ad
    # lapse-curvature coefficient: static, h00-linear part = km*(k_i k_j h_ij - k^2 tr h)
    qs = q.subs(ks[0], 0)
    lin = sp.expand(qs).coeff(hs[0], 1).subs({hs[hv(0, n)]: 0 for n in range(1, 4)})
    km = -sp.expand(lin).coeff(hs[hv(1, 1)], 1).coeff(ks[2], 2)
    # spatial FP3 coefficient from h12^2 k3^2
    pure = sp.expand(qs.subs({hs[0]: 0}).subs({hs[hv(0, n)]: 0 for n in range(1, 4)}))
    ks3 = sp.expand(pure).coeff(hs[hv(1, 2)], 2).coeff(ks[3], 2)  # FP3 has coefficient 1 for h12^2 k3^2
    # TT: h12, k=(k0,0,0,k3)
    sub = {v: 0 for v in hs}; sub[hs[hv(1, 2)]] = 1; sub.update({ks[1]: 0, ks[2]: 0})
    qtt = sp.expand(q.subs(sub))
    T = qtt.coeff(ks[0], 2); S = qtt.coeff(ks[3], 2)
    return dict(alpha=sp.simplify(alpha), B=sp.simplify(B), km_h00=sp.simplify(km), ks=sp.simplify(ks3),
                TT_speed2=sp.simplify(S / T), h00sq=sp.simplify(q.coeff(hs[0], 2)))

ro = readoff(Q)
print('   read-off:', ro)
print('   K_m(h00-normalisation)/alpha =', sp.simplify(ro['km_h00'] / ro['alpha']), ' -> in u-normalisation (h00=2u) K_m/alpha =', sp.simplify(2 * ro['km_h00'] / ro['alpha']))
print('   K_s/K_m =', sp.simplify(ro['ks'] / ro['km_h00']), ' vs TT speed^2 =', ro['TT_speed2'])

# static solve, source only in h00 (rest mass); gamma = -h_perp/h00 (Euclid sign)
def gamma_static(Q, kdir):
    Qs = sp.expand(Q.subs(ks[0], 0))
    subk = {ks[1]: kdir[0], ks[2]: kdir[1], ks[3]: kdir[2]}
    Qk = sp.expand(Qs.subs(subk))
    Hs = sp.Matrix(10, 10, lambda i, j: sp.diff(Qk, hs[i], hs[j]))
    J = sp.zeros(10, 1); J[0] = 1
    sol, params = Hs.gauss_jordan_solve(J)
    sol = sol.subs({p: 0 for p in params})
    hm = sp.Matrix(4, 4, lambda m, n: sol[hv(m, n)])
    hij = hm[1:, 1:]
    kk = sp.Matrix(kdir)
    e1 = None
    for c in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])):
        w = c - (c.dot(kk) / kk.dot(kk)) * kk
        if w.norm() != 0:
            e1 = w; break
    e2 = kk.cross(e1)
    hp1 = sp.simplify((e1.T * hij * e1)[0, 0] / e1.dot(e1)); hp2 = sp.simplify((e2.T * hij * e2)[0, 0] / e2.dot(e2))
    assert sp.simplify(hp1 - hp2) == 0
    return sp.simplify(-hp1 / sol[0])

for cval in (R(1), R(4), R(1, 4), R(9, 16), R(3, 2)):
    Qc = Q.subs(c2, cval)
    g = [gamma_static(Qc, d) for d in ((0, 0, 1), (1, 2, 3))]
    print(f'   c_g^2 = {cval}: static gamma = {g}   1/c_g^2 = {1 / cval}')

# ---------------- C. campaign's own shift-free member ----------------
# b101 form: L = alpha*kin + K*(u*R_1 + R_2) with ONE K (N*sqrt(g)*R expanded: N=1+u).
# Normalisation fixed by the GR point: in the (h00=2u, h_ij) variables the Fierz-Pauli member (c_g=1) reads
#   alpha=1/2,  Q = alpha k0^2 (sum h_ij^2 - (tr h)^2) + K (2 u R1 + FP3),  with K = 1   (K_m^(u) = 2 K_s^(FP3)).
# So "one curvature density" (b60/b64: K_m = K_s) is  Q = alpha*kin + K*(2*u*R1 + FP3), alpha free.
print('\n== C. campaign member (u, h_ij only; one curvature density K; beta=-alpha; alpha free) ==')
al, K, z = sp.symbols('alpha K zeta', positive=True)
u = sp.symbols('u')
hij_s = sp.symbols('g11 g12 g13 g22 g23 g33')
gm = sp.Matrix([[hij_s[0], hij_s[1], hij_s[2]], [hij_s[1], hij_s[3], hij_s[4]], [hij_s[2], hij_s[4], hij_s[5]]])
k3 = sp.Matrix(ks[1:]); k0 = ks[0]
kk2 = (k3.T * k3)[0, 0]
R1 = (k3.T * gm * k3)[0, 0] - kk2 * gm.trace()
FP3 = sp.expand(R(1, 2) * kk2 * sum(gm[i, j] ** 2 for i in range(3) for j in range(3))
                - sum(sum(gm[i, j] * k3[j] for j in range(3)) ** 2 for i in range(3))
                + (k3.T * gm * k3)[0, 0] * gm.trace() - R(1, 2) * kk2 * gm.trace() ** 2)
kin = k0 ** 2 * al * (sum(gm[i, j] ** 2 for i in range(3) for j in range(3)) - gm.trace() ** 2)
Qsf = sp.expand(kin + K * (2 * u * R1 + FP3))
c = sp.symbols('c')
dg = {hij_s[0]: k3[0] * k3[0] * z, hij_s[1]: k3[0] * k3[1] * z, hij_s[2]: k3[0] * k3[2] * z,
      hij_s[3]: k3[1] * k3[1] * z, hij_s[4]: k3[1] * k3[2] * z, hij_s[5]: k3[2] * k3[2] * z}
sub = {v: v + dg[v] for v in hij_s}; sub[u] = u + c * k0 ** 2 * z
var = sp.expand(Qsf.subs(sub, simultaneous=True) - Qsf)
lin = sp.expand(var.coeff(z, 1))
csol = sp.solve(sp.Poly(lin, *(list(hij_s) + [u] + list(ks))).coeffs(), c, dict=True)
print('   shift-free symmetry  delta g_ij = k_i k_j zeta, delta u = c k0^2 zeta:  c =', csol, ' (exists for EVERY alpha, K)')
print('   zeta^2 piece:', sp.simplify(var.coeff(z, 2)))
def gamma_sf(Qx, kdir):
    Qs = sp.expand(Qx.subs(k0, 0).subs({ks[1]: kdir[0], ks[2]: kdir[1], ks[3]: kdir[2]}))
    vars_ = [u] + list(hij_s)
    Hs = sp.Matrix(7, 7, lambda i, j: sp.diff(Qs, vars_[i], vars_[j]))
    Jv = sp.zeros(7, 1); Jv[0] = 1
    sol, params = Hs.gauss_jordan_solve(Jv)
    sol = sol.subs({p: 0 for p in params})
    gmat = sp.Matrix([[sol[1], sol[2], sol[3]], [sol[2], sol[4], sol[5]], [sol[3], sol[5], sol[6]]])
    kkv = sp.Matrix(kdir)
    for cc in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])):
        w = cc - (cc.dot(kkv) / kkv.dot(kkv)) * kkv
        if w.norm() != 0:
            e1 = w; break
    hp = sp.simplify((e1.T * gmat * e1)[0, 0] / e1.dot(e1))
    return sp.simplify(-hp / (2 * sol[0]))     # physical gamma = -h_perp/h00, h00 = 2u (Euclid sign as in B)
for (avals, Kval) in ((R(1, 2), R(1)), (R(1), R(1)), (R(1, 8), R(1)), (R(2), R(1)), (R(1), R(3))):
    Qn = Qsf.subs({al: avals, K: Kval})
    gs = gamma_sf(Qn, (1, 2, 3))
    sub_tt = {v: 0 for v in hij_s}; sub_tt[hij_s[1]] = 1
    qtt = sp.expand(Qn.subs(sub_tt).subs(u, 0).subs({ks[1]: 0, ks[2]: 0}))
    sp2 = sp.simplify(qtt.coeff(ks[3], 2) / qtt.coeff(k0, 2))
    print(f'   alpha={avals}, K={Kval}: static gamma = {gs},  TT speed^2 = {sp2}   (shift-free compensating c = -alpha/K = {-avals/Kval})')

print('\n== D. is that symmetry the diffeo (G) of the matter metric? ==')
print('   G forces delta h_0i = 0 -> xi_0 = -k0 s for xi_i = k_i s, so delta h_00 = -k0^2 zeta, delta u = +-(1/2) k0^2 zeta, i.e. |c_G| = 1/2.')
print('   FP family (any c_g): alpha = 1/(2 c2), K_m^(u) = 2/c2  => c = -2 alpha/K_m^(u) =', sp.simplify(-2 * (1 / (2 * c2)) / (2 / c2)), '(always -1/2 = c_G)')
print('   campaign member: c = -alpha/K; equals -1/2 iff K = 2 alpha  <=> TT speed^2 = K/(2 alpha) = 1.')

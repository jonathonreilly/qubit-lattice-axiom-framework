#!/usr/bin/env python3
"""J:derive:constraint-algebra-closure-for-block-62s-kinetic-numbers:a2 - worker w-jonathonsmac4f50-ja536 (claude-opus-5-5).

Definitions (block 62, open PR #8592, claim scope; supplied, not adopted): strains with the staggered placement - h_jj on sites,
h_ij (i < j) on the faces spanned by e_i, e_j, relabellings xi_j on the bonds along j; every difference between neighbouring
places has the real symbol p_j = 2 sin(k_j/2). Member at second order: R_1 = -(p_i p_j h_ij - p^2 h) (linear), R_2 (quadratic,
Fierz-Pauli). Kinetic term (1/wbar)[alpha hdot_ij hdot_ij + beta hdot^2]; its Legendre transform, with P the momenta of the
independent variables (P_jj for h_jj, P_ij for h_ij, i < j), is (1/(4 alpha))[sum_j P_jj^2 - c (sum_j P_jj)^2] + sum_{i<j} P_ij^2/(8 alpha),
c = beta/(alpha + 3 beta) (equivalently (1/(4 alpha))(pi.pi - c pi^2) with pi_ij = P_ij/2 off the diagonal).
Per-tick energy: E = sum over places of (clock) x (energy density); CLAUSE SUPPLIED HERE (the unit leaves it open): a term living
on a face is timed by the MEAN of its four corner clocks (A3: any timing symmetric under inversion through the face centre gives
the same bracket; one corner's clock does not); site terms by the site's clock. C[N] = E with the clocks replaced by a
lapse N. Relabelling generator of the field: G[xi] = sum_places P . (the change of h under h_ij -> h_ij + d_i xi_j + d_j xi_i).
Linear order: the part of {C[N], C[M]} linear in the fields comes only from {K R_1[N], kin[M]} - (N <-> M).
Exact arithmetic: sympy / Fraction on the 4^3 torus.
"""
import itertools
import random
from fractions import Fraction as Fr

import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


L = 4
SITES = list(itertools.product(range(L), repeat=3))
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
PAIRS = [(0, 1), (0, 2), (1, 2)]


def sh(x, *vs):
    y = list(x)
    for v in vs:
        for a in range(3):
            y[a] = (y[a] + v[a]) % L
    return tuple(y)


def neg(v):
    return tuple(-a for a in v)


# variable indexing: ('d', j, x) for h_jj/P_jj at site x; ('o', (i,j), x) for the face with lower corner x
VARS = [('d', j, x) for j in range(3) for x in SITES] + [('o', pr, x) for pr in PAIRS for x in SITES]
VI = {v: n for n, v in enumerate(VARS)}
BONDS = [(j, x) for j in range(3) for x in SITES]      # xi_j on the bond from x to x + e_j
BI = {b: n for n, b in enumerate(BONDS)}


def R1_grad(N):
    """d(R_1[N])/dh for R_1[N] = sum_x N_x R_1(x), R_1(x) = sum_j d_j^2 h_jj + 2 sum_{i<j} d_i d_j h_ij - sum_j d_j^2 (sum_k h_kk)."""
    g = {v: Fr(0) for v in VARS}
    for x in SITES:
        n = N[x]
        for j in range(3):
            lap_j = [(sh(x, E[j]), 1), (x, -2), (sh(x, neg(E[j])), 1)]
            for y, cf in lap_j:
                g[('d', j, y)] += n * cf                           # d_j^2 h_jj
                for kk in range(3):
                    g[('d', kk, y)] -= n * cf                      # - d_j^2 h
        for (i, j) in PAIRS:
            # d_i d_j h_ij at x: faces with lower corners x, x - e_i, x - e_j, x - e_i - e_j with signs +, -, -, +
            for lc, cf in ((x, 1), (sh(x, neg(E[i])), -1), (sh(x, neg(E[j])), -1), (sh(x, neg(E[i]), neg(E[j])), 1)):
                g[('o', (i, j), lc)] += 2 * n * cf
    return g


def face_clock(M, pr, lc, mode):
    i, j = pr
    if mode == 'mean4':
        return (M[lc] + M[sh(lc, E[i])] + M[sh(lc, E[j])] + M[sh(lc, E[i], E[j])]) / 4
    if mode == 'corner':
        return M[lc]
    if mode == 'mean2':
        return (M[lc] + M[sh(lc, E[i], E[j])]) / 2
    if mode == 'mean2b':
        return (M[sh(lc, E[i])] + M[sh(lc, E[j])]) / 2
    if mode == 'corner_far':
        return M[sh(lc, E[i], E[j])]
    raise ValueError


def bracket_linear(N, M, alpha, c, K, mode):
    """coefficient vector (over P variables) of K({R_1[N], kin[M]} - {R_1[M], kin[N]})."""
    out = {v: Fr(0) for v in VARS}
    for A, B, sgn in ((N, M, 1), (M, N, -1)):
        g = R1_grad(A)
        # d kin[B]/dP: diag: (B_x/(2 alpha))(P_jj - c sum_k P_kk); off: (B_f/(4 alpha)) P_ij
        for x in SITES:
            for j in range(3):
                w = g[('d', j, x)] * B[x] / (2 * alpha)
                out[('d', j, x)] += sgn * K * w
                for kk in range(3):
                    out[('d', kk, x)] -= sgn * K * w * c
        for pr in PAIRS:
            for x in SITES:
                out[('o', pr, x)] += sgn * K * g[('o', pr, x)] * face_clock(B, pr, x, mode) / (4 * alpha)
    return out


def G_coeffs(xi):
    """coefficients of G[xi] on the P variables: P_jj: 2 d_j xi_j at the site; P_ij: d_i xi_j + d_j xi_i at the face."""
    out = {v: Fr(0) for v in VARS}
    for x in SITES:
        for j in range(3):
            out[('d', j, x)] += 2 * (xi[(j, x)] - xi[(j, sh(x, neg(E[j])))])
    for (i, j) in PAIRS:
        for y in SITES:
            out[('o', (i, j), y)] += (xi[(j, sh(y, E[i]))] - xi[(j, y)]) + (xi[(i, sh(y, E[j]))] - xi[(i, y)])
    return out


random.seed(1729)
alpha, K = Fr(3, 7), Fr(5, 11)
trials = [({x: Fr(random.randint(-3, 3)) for x in SITES}, {x: Fr(random.randint(-3, 3)) for x in SITES}) for _ in range(3)]

# ================================================================ A1 exact closure on the lattice at beta = -alpha (c = 1/2)
ok = True
for N, M in trials:
    b = bracket_linear(N, M, alpha, Fr(1, 2), K, 'mean4')
    xi = {(j, x): K / (4 * alpha) * (N[sh(x, E[j])] * M[x] - N[x] * M[sh(x, E[j])]) for (j, x) in BONDS}
    g = G_coeffs(xi)
    ok &= all(b[v] == g[v] for v in VARS)
check('A1', ok, "EXACT (4^3 torus, three pairs of random integer lapses, rational alpha = 3/7, K = 5/11): with beta = -alpha "
      "(c = 1/2) and face terms timed by the mean of their four corner clocks, the part of {C[N], C[M]} linear in the fields "
      "equals G[xi] EXACTLY, with the bond field xi_j(x -> x + e_j) = (K/(4 alpha)) (N_{x+e_j} M_x - N_x M_{x+e_j}) - the "
      "lattice form of (K/(4 alpha))(M grad N - N grad M): the algebra closes on the lattice at this order, with no O(p^2) "
      "remainder")

# ================================================================ A2 closure fails for every other beta (exact rank test)
def membership(b):
    Rm = sp.zeros(len(VARS), len(BONDS) + 1)
    for (j, x) in BONDS:
        unit = {bb: Fr(0) for bb in BONDS}
        unit[(j, x)] = Fr(1)
        col = G_coeffs(unit)
        for v, val in col.items():
            if val:
                Rm[VI[v], BI[(j, x)]] = sp.Rational(val.numerator, val.denominator)
    rank_R = Rm[:, :len(BONDS)].rank()
    for v, val in b.items():
        if val:
            Rm[VI[v], len(BONDS)] = sp.Rational(val.numerator, val.denominator)
    return rank_R, Rm.rank()


N, M = trials[0]
b_half = bracket_linear(N, M, alpha, Fr(1, 2), K, 'mean4')
b_zero = bracket_linear(N, M, alpha, Fr(0), K, 'mean4')
b1 = {v: b_zero[v] - b_half[v] for v in VARS}                          # b is affine in c: b(c) = b(1/2) + (1 - 2c) b1
rR, rRb = membership(b1)
ok = rRb == rR + 1
# the (1-2c) part is isotropic on the diagonal: equal for the three P_jj at each site, zero on faces
ok &= all(b1[('o', pr, x)] == 0 for pr in PAIRS for x in SITES)
ok &= all(b1[('d', 0, x)] == b1[('d', 1, x)] == b1[('d', 2, x)] for x in SITES)
check('A2', ok, "EXACT (rank over Q on the 4^3 torus): the bracket is b(c) = b(1/2) + (1 - 2c) b_1, where b_1 is the same "
      "on the three diagonal momenta at each site and zero on the faces, and b_1 is NOT in the span of the relabelling "
      "generators (rank rises by one): the algebra closes onto G iff c = 1/2, i.e. beta/(alpha + 3 beta) = 1/2, i.e. "
      "beta = -alpha (DeWitt's value in the comparator)", f"rank of the relabelling map {rR}; with b_1 appended {rRb}")

# ================================================================ A3 the clock placement: inversion-symmetric timings close, one corner does not
res = {}
for mode in ('corner', 'corner_far', 'mean2', 'mean2b'):
    bb = bracket_linear(N, M, alpha, Fr(1, 2), K, mode)
    res[mode] = membership(bb)
ok = all(res[m][1] == res[m][0] + 1 for m in ('corner', 'corner_far'))
ok &= all(res[m][1] == res[m][0] for m in ('mean2', 'mean2b'))
b4 = bracket_linear(N, M, alpha, Fr(1, 2), K, 'mean4')
ok &= all(bracket_linear(N, M, alpha, Fr(1, 2), K, m) == b4 for m in ('mean2', 'mean2b'))
check('A3', ok, "EXACT: with beta = -alpha, a face term timed by ONE corner's clock (either the near or the far corner) gives a "
      "linear bracket outside the span of the relabelling generators, while the mean of either pair of opposite corners gives "
      "exactly the same bracket as the four-corner mean (their symbols differ by a multiple of sin(k_i/2) sin(k_j/2), which "
      "cancels when the bracket is antisymmetrized): closure needs a face timing symmetric under inversion through the face "
      "centre (a real symbol); one corner's clock has an odd imaginary part and breaks it",
      "; ".join(f"{m}: rank {r0} -> {r1}" for m, (r0, r1) in res.items()))

# ================================================================ A4 the identity behind A1, in symbols
k = sp.symbols('k1:4', real=True)
kp = sp.symbols('q1:4', real=True)
s = [sp.sin(v / 2) for v in k]
cs = [sp.cos(v / 2) for v in k]
sp_ = [sp.sin(v / 2) for v in kp]
cp_ = [sp.cos(v / 2) for v in kp]
ok = True
for (i, j) in PAIRS:
    lhs = (sp_[i] * sp_[j] * cs[i] * cs[j] - s[i] * s[j] * cp_[i] * cp_[j])                     # the bracket's face coefficient (x alpha/2)
    rhs = (sp.sin((k[i] + kp[i]) / 2) * sp.sin((kp[j] - k[j]) / 2) + sp.sin((k[j] + kp[j]) / 2) * sp.sin((kp[i] - k[i]) / 2)) / 2
    ok &= sp.simplify(sp.expand_trig(lhs - rhs)) == 0
for j in range(3):
    lhs = -(4 * s[j] ** 2 - 4 * sp_[j] ** 2)                                                      # -(P_j(k)^2 - P_j(k')^2)
    rhs = 2 * 2 * sp.sin((k[j] + kp[j]) / 2) * 2 * sp.sin((kp[j] - k[j]) / 2) / 2
    ok &= sp.simplify(sp.expand_trig(lhs - rhs)) == 0
lam = sp.symbols('lam', real=True)
for (i, j) in PAIRS:
    gam = lambda cc, ss: cc[i] * cc[j] + lam * ss[i] * ss[j]
    face = (sp_[i] * sp_[j] * gam(cs, s) - s[i] * s[j] * gam(cp_, sp_))
    rhs = (sp.sin((k[i] + kp[i]) / 2) * sp.sin((kp[j] - k[j]) / 2) + sp.sin((k[j] + kp[j]) / 2) * sp.sin((kp[i] - k[i]) / 2)) / 2
    ok &= sp.simplify(sp.expand_trig(face - rhs)) == 0
check('A4', ok, "EXACT (sympy, all wave vectors, and for every face timing with real symbol cos(k_i/2) cos(k_j/2) + lam sin(k_i/2) sin(k_j/2)): for plane-wave lapses N = e^{ik.x}, M = e^{ik'.x} the diagonal part of the "
      "bracket is -(P_j(k)^2 - P_j(k')^2) = 4 sin(q_j/2) sin((k'_j - k_j)/2) (q = k + k') and the face part "
      "sin(k'_i/2) sin(k'_j/2) cos(k_i/2) cos(k_j/2) - (k <-> k') = [sin(q_i/2) sin((k'_j - k_j)/2) + sin(q_j/2) sin((k'_i - k_i)/2)]/2: "
      "both are exactly the relabelling of the bond field with symbol sin((k'_j - k_j)/2), so closure holds at every wave "
      "vector and is not a long-wavelength statement")

# ================================================================ B1 the structure constant is the field's speed squared
p2, X, a_, K_ = sp.symbols('p2 X alpha K', positive=True)
speed2 = sp.solve(sp.Eq(K_ * p2 - 4 * a_ * X, 0), X)[0] / p2
ok = sp.simplify(speed2 - K_ / (4 * a_)) == 0
check('B1', ok, "EXACT: the structure function of A1 carries the factor K/(4 alpha), which is block 62 T4's speed squared of "
      "the two travelling disturbances (X = K p^2/(4 alpha)); if the walker's energy density is added and its own bracket "
      "closes onto its relabelling generator with its speed squared (1, block 54's limiting speed - ASSUMED here, not "
      "computed), one relabelling field serves both only if K/(4 alpha) = 1: K = 4 alpha, the same cone for field and walker")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact: at the order linear in the fields, the per-tick constraints of block 62's strains close on the "
      "lattice - {C[N], C[M]} = G[xi] exactly, xi_j = (K/(4 alpha))(N_{x+e_j} M_x - N_x M_{x+e_j}) on the bonds - iff beta = -alpha, "
      "provided each face term is timed symmetrically under inversion through the face centre (four-corner mean, or either pair of opposite corners; one corner fails); the identity "
      "holds at every wave vector, so there is no O(p^2) obstruction at this order; the structure constant is the field's "
      "speed squared K/(4 alpha), so a common relabelling with a speed-1 walker needs K = 4 alpha; the quadratic order needs "
      "the cubic terms of the energy, which are not supplied")
if all(RESULTS):
    print("HIT: closure holds exactly on the lattice at linear order: with the kinetic numbers beta = -alpha (any alpha, K) and "
          "face terms timed inversion-symmetrically (the mean of the four corner clocks, or of either pair of opposite corners), the part of {C[N], C[M]} linear in the strains equals the "
          "relabelling generator G[xi] with xi_j = (K/(4 alpha))(N_{x+e_j} M_x - N_x M_{x+e_j}) at every wave vector (exact "
          "rationals on the 4^3 torus, symbolic identity for all k, k'); for c = beta/(alpha + 3 beta) != 1/2 or a one-corner clock "
          "placement it does not close (exact rank test); the structure constant K/(4 alpha) is the field's speed squared")

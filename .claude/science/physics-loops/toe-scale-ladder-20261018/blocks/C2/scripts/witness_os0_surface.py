#!/usr/bin/env python3
"""C2(i)-W2 and T_tie: what the kinetic-isotropy primitive does and does not tie.

(a) Group theory on the Euclidean block Z^3 x Z_tau with a_tau = a.
    B4 = signed 4x4 permutation matrices (384). Count invariant structures:
      - rank-2 tensors c_{mu nu} (fermion kinetic term psibar gamma_mu d_nu psi): expect 1 (delta)
      - symmetric quadratic forms on F_{mu nu} (Lambda^2 R^4): expect 1 (F.F) under B4
        [2 under the proper subgroup det=+1: F.F and F.Ftilde (topological, no velocity)]
      - same counts under the spatial group O_h x Z2(time): expect 2 and 2 (c_t, c_s ; E^2, B^2)
    => if the WHOLE quadratic action (gauge + matter) is B4-invariant, both IR quadratic
       forms are delta-proportional: c_gamma = c_psi = a/a_tau (T_tie).
(b) Exact lattice dispersions (Euclidean poles continued k0 -> iE):
      - naive/staggered fermion  sum_mu zeta_mu gamma_mu sin k_mu :  zeta0^2 sinh^2 E = sum_j sin^2 k_j
      - noncompact Gaussian U(1), beta_t on (0j), beta_s on (jk) plaquettes:
            4 beta_t sinh^2(E/2) = beta_s |s(k)|^2
(c) W2 witness pair satisfying the registered (matter-only) primitive:
      A: zeta0 = 1, beta_t = beta_s              -> c_gamma/c_psi = 1
      B: zeta0 = 1, beta_s/beta_t = xi^2 (xi=6/5) -> c_gamma/c_psi = 6/5
"""
import itertools
import sys
import numpy as np
import sympy as sp

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from c2_common import Checks

ck = Checks()

B4 = []
for perm in itertools.permutations(range(4)):
    for signs in itertools.product([1, -1], repeat=4):
        g = np.zeros((4, 4))
        for i, p in enumerate(perm):
            g[p, i] = signs[i]
        B4.append(g)
ck.check('B4 has 384 elements', len(B4) == 384)

def counts(group):
    n = len(group)
    t2 = sum(np.trace(g) ** 2 for g in group) / n                      # R4 (x) R4 invariants
    def chiL2(g):
        return (np.trace(g) ** 2 - np.trace(g @ g)) / 2
    sym2 = sum((chiL2(g) ** 2 + chiL2(g @ g)) / 2 for g in group) / n   # Sym^2(Lambda^2) invariants
    return round(t2, 9), round(sym2, 9)

c_full = counts(B4)
proper = [g for g in B4 if np.linalg.det(g) > 0]
c_prop = counts(proper)
spatial = [g for g in B4 if abs(g[0, 0]) == 1]   # O_h(with reflections) x Z2 time reflection
c_sp = counts(spatial)
print(f"  invariants (rank-2 tensors, quadratic forms on F): B4 {c_full}, proper B4 {c_prop}, O_h x Z2(t) {c_sp}")
ck.check('B4: one invariant rank-2 tensor (delta) -> fermion c_t = c_s forced', c_full[0] == 1)
ck.check('B4: one invariant quadratic form on F_{mu nu} (F.F) -> photon E^2/B^2 ratio forced', c_full[1] == 1)
ck.check('proper B4 (det +1): rank-2 still 1; F-forms 2 (F.F and the topological F.Ftilde, which carries no velocity)',
         c_prop[0] == 1 and c_prop[1] == 2)
ck.check('spatial cubic x time reflection only: 2 rank-2 invariants (c_t, c_s) and 2 F-forms (E^2, B^2)',
         c_sp[0] == 2 and c_sp[1] == 2)

proper_cubic = [g for g in spatial if g[0, 0] == 1 and np.linalg.det(g) > 0]   # O only (Lattice axiom), no time reflection
c_O = counts(proper_cubic)
print(f"  proper cubic O only (order {len(proper_cubic)}): {c_O}")
ck.check('proper cubic O only (Lattice axiom, no time reflection): 2 rank-2 invariants; 3 F-forms (E^2, B^2, E.B; E.B carries no velocity)',
         len(proper_cubic) == 24 and c_O[0] == 2 and c_O[1] == 3)

# ---------------- exact dispersions
E, k = sp.symbols('E k', positive=True)
z0 = sp.symbols('zeta0', positive=True)
# fermion along x axis: zeta0^2 sinh^2 E = sin^2 k ; small k: E = k/zeta0 + O(k^3)
Ef = sp.asinh(sp.sin(k) / z0)
ser_f = sp.series(Ef, k, 0, 4).removeO()
ck.check('fermion: E(k) = k/zeta0 + O(k^3): c_psi = 1/zeta0 (=1 on the isotropic B4 action)',
         sp.simplify(ser_f.coeff(k, 1) - 1 / z0) == 0)
# gauge: build quadratic kernel and check the transverse mode
bt, bs = sp.symbols('beta_t beta_s', positive=True)
s0, s1, s2, s3 = sp.symbols('s0:4')
shat = [s0, s1, s2, s3]
beta = lambda m, n: bt if 0 in (m, n) else bs
M = sp.zeros(4, 4)
for m in range(4):
    for n in range(4):
        if m == n:
            M[m, n] = sum(beta(m, r) * shat[r] ** 2 for r in range(4) if r != m)
        else:
            M[m, n] = -beta(m, n) * shat[m] * shat[n]
Avec = sp.Matrix([0, 0, 1, 0])
Mk = M.subs({s2: 0, s3: 0})
ck.check('gauge: transverse mode A_2 at k=(k0,kx,0,0) has kernel beta_t s0^2 + beta_s s1^2',
         sp.simplify((Mk * Avec - (bt * s0 ** 2 + bs * s1 ** 2) * Avec)) == sp.zeros(4, 1))
ck.check('gauge: pure-gauge vector shat is a zero mode (gauge invariance of the kernel)',
         sp.simplify(M * sp.Matrix(shat)) == sp.zeros(4, 1))
# continuation s0^2 = (2 sin(k0/2))^2 -> -(2 sinh(E/2))^2
Eg = 2 * sp.asinh(sp.sqrt(bs / bt) * sp.sin(k / 2))
ser_g = sp.series(Eg, k, 0, 4).removeO()
ck.check('gauge: E(k) = sqrt(beta_s/beta_t) k + O(k^3): c_gamma = sqrt(beta_s/beta_t)',
         sp.simplify(ser_g.coeff(k, 1) - sp.sqrt(bs / bt)) == 0)
# numerical root check of the exact continued pole condition for model B
xi = sp.Rational(6, 5)
for kk in [0.01, 0.3]:
    Enum = float(2 * np.arcsinh(float(xi) * np.sin(kk / 2)))
    lhs = 4 * (1 / float(xi) ** 2) * np.sinh(Enum / 2) ** 2 - 4 * np.sin(kk / 2) ** 2
    ck.check(f'gauge model B (beta_s/beta_t=36/25): exact pole residual at k={kk} is 0', abs(lhs) < 1e-14, f"E/k={Enum/kk:.6f}")

# ---------------- B4 invariance of the two models' quadratic kinetic data
def b4_invariant_tensor(T):
    return all(np.allclose(g @ T @ g.T, T) for g in B4)
fermion_c = np.eye(4)                           # zeta0 = 1 isotropic matter, both models
def plaquette_weights_invariant(bt_, bs_, group):
    # beta_{mu nu} for unordered plane {mu,nu}; signed permutations act on planes by index permutation
    w = lambda m, n: bt_ if 0 in (m, n) else bs_
    for g in group:
        perm = [int(np.nonzero(g[:, i])[0][0]) for i in range(4)]
        for m in range(4):
            for n in range(m + 1, 4):
                if w(perm[m], perm[n]) != w(m, n):
                    return False
    return True
ck.check('model A plaquette weights (beta_t=beta_s) B4-invariant; model B (beta_t/beta_s=25/36) not B4- but O_h x Z2(t)-invariant',
         plaquette_weights_invariant(1, 1, B4) and not plaquette_weights_invariant(25/36, 1, B4)
         and plaquette_weights_invariant(25/36, 1, spatial))
rA, rB = 1, float(xi)
print(f"  tree-level IR ratio c_gamma/c_psi: model A = {rA}, model B = {rB}")
ck.check('W2 witness pair: same premises (matter-only kinetic isotropy, cubic covariance, one tick a_tau=a), ratios 1 vs 6/5', rA != rB)
sys.exit(ck.total())

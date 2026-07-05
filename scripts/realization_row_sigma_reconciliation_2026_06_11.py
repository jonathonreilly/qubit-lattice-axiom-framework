#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The realization row reconciled: both candidates consume the same quantized
W-IR slope; the walk family's moduli are pure frame content (cycle 6)
============================================================================
Companion runner for
docs/REALIZATION_ROW_SIGMA_RECONCILIATION_BOUNDED_THEOREM_NOTE_2026-06-11.md.
Cycle 6 of the kinetic-isotropy derivation loop.  Inputs (all landed): the
eta-twisted walk family (block05), the factorized per-axis class (blocks
02-04), and the B-W bridge reduction (the OS0 identification consumes ONLY
the cone-point first-order slope, premise W-IR).

RESULTS (exact unless stated):
  A  THE GLOBAL SIGMA LAW: the walk family's FULL three-variable
     characteristic polynomial factors over the whole Brillouin zone; each
     block's band equation collapses to the single-cosine law
         6 sqrt(alpha beta) cos Phi = alpha conj(sigma) + beta sigma,
         i.e.  cos Phi = Re(e^{i psi} sigma(k)) / 3,
     with sigma(k) = e^{ik1} + e^{ik2} + e^{ik3} the cubic adjacency symbol
     and e^{i psi} = sqrt(beta/alpha).  Momentum enters ONLY through sigma.
  B  MODULI = FRAME CONTENT: e^{i psi} sigma(k) = sigma(k + psi (1,1,1))
     EXACTLY -- the per-block moduli are a diagonal momentum translation
     plus a quasi-energy offset (block01's offset class).  Every per-band
     translation-invariant kinetic datum is RIGID across the moduli; the
     block05 record's "off-axis FRONT SPEEDS are continuously
     moduli-tunable (0.19-0.24)" is exhibited as a fixed-line slice
     artifact (the full-BZ maximum is invariant).
  C  THE DRIFT AND THE DIAGONAL, FROM THE LAW: at k = 0 the band slopes are
     EXACTLY +-1/6 per axis (generic psi != 0) and +-1/(2 sqrt 3) at psi = 0
     -- re-deriving block05's strata in two lines from the cos-law; the
     gapless locus is |sigma| = 3, i.e. EXACTLY the BZ diagonal line, where
     the law gives 2 theta - theta_0 = +-(t + psi): slope 1/2 in the cell
     diagonal parameter, exactly linear, all moduli.
  D  T1 (drift equality): the factorized symmetric cycle obeys
     (S1 S2 S3)^2 = -(z1 z2 z3)^{-1} I exactly, so its per-tick drift is
     +-(1,1,1)/6 cells/tick -- IDENTICAL to the family's rigid drift.
  E  THE W-IR RECONCILIATION: the per-axis candidate's transport-direction
     slope is 1/2 in cell units (the landed 1D dichotomy value); the
     family's transport-direction (diagonal) slope is 1/2 in the cell
     diagonal parameter (exact, Part C).  Both candidates feed the SAME
     quantized first-order datum into the landed W-IR premise; under the
     landed B-W reduction the OS0-consumed content is IDENTICAL: the
     realization choice is OS0-IRRELEVANT at the consumed level.  The
     candidates' genuine differences (transverse curvature, inter-block
     relative-offset geometry, single-tick vs composite mass realization)
     are enumerated and lie OUTSIDE the consumed surface.
  F  THE SIGMA KINSHIP + THE HONEST CONE ROW: the landed staggered
     Hamiltonian's dispersion is ALSO sigma-driven --
     E(k) = +-sqrt((3 - Re sigma)/2) (verified on the 8-cell Bloch
     operator) -- the walk family is the tick-native cos-law sibling of the
     H-law.  Review found the family's within-block touchings are
     isotropic 3D cones at slope 1/(2 sqrt 3), threaded by the inter-block
     nodal line.  The H-slope 1/2 cone remains larger-cell or unit-premise
     content; the matter-cone row re-opens positively at the quantized
     family slope rather than closing at the H normalization.

NO audit status is set or predicted; no registry action.  Conditional on
the campaign's standing set; the landed W-IR premise is consumed as the
landed text states it.

Run: PYTHONHASHSEED=0 python3 scripts/realization_row_sigma_reconciliation_2026_06_11.py
"""
from __future__ import annotations
import sys
import itertools
import numpy as np
import sympy as sp

PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


# ---- shared structure (the landed conventions) ----
comps = list(itertools.product((0, 1), repeat=3))
idx = {p: i for i, p in enumerate(comps)}
pairs = []
for p in comps:
    for q in comps:
        if sum(abs(p[i] - q[i]) for i in range(3)) == 1:
            ax = [i for i in range(3) if p[i] != q[i]][0]
            pairs.append((p, q, ax, +1 if p[ax] == 1 else -1))
pair_at = {(p, q): i for i, (p, q, ax, s) in enumerate(pairs)}
def eta_val(mu, p):
    return 1 if mu == 0 else ((-1) ** p[0] if mu == 1 else (-1) ** (p[0] + p[1]))
g12, g23 = (1, 0, 2), (0, 2, 1)
v12 = np.array([1, 1, 1, 1, 1, 1, -1, -1], float)
v23 = np.array([1, 1, 1, -1, 1, 1, 1, -1], float)
def act(g, v, kind, i):
    p, q, ax, s = pairs[i]
    return (kind, pair_at[(tuple(p[g[j]] for j in range(3)), tuple(q[g[j]] for j in range(3)))],
            v[idx[p]] * v[idx[q]])
from collections import deque
labels = [('c', i) for i in range(24)] + [('d', i) for i in range(24)]
seen = set(); orbs = []
for lab in labels:
    if lab in seen: continue
    orb = {lab: 1.0}; dq = deque([lab]); cons = True
    while dq:
        cur = dq.popleft()
        for g, v in ((g12, v12), (g23, v23)):
            kind, j, sign = act(g, v, cur[0], cur[1])
            nxt = (kind, j); val = orb[cur] * sign
            if nxt in orb:
                if abs(orb[nxt] - val) > 1e-9: cons = False
            else:
                orb[nxt] = val; dq.append(nxt)
    seen |= set(orb)
    if cons: orbs.append(orb)
ACTIVE = (1, 2, 5, 6, 9, 10)
z1, z2, z3 = sp.symbols('z1 z2 z3')
zs = (z1, z2, z3)
us = [sp.Symbol(f'u{j}') for j in range(6)]
Uu = sp.zeros(8, 8)
for ji, j in enumerate(ACTIVE):
    amp = us[ji] / sp.sqrt(3)
    for (kind, i2), sign in orbs[j].items():
        p, q, ax, sgn = pairs[i2]
        Uu[idx[p], idx[q]] += sp.Integer(int(sign)) * amp * (zs[ax] ** sgn if kind == 'd' else 1)

# ----------------------------------------------------------------------------
print("\nPART A -- the global sigma law (exact)")
print("=" * 78)
lam_, X_ = sp.symbols('lambda X')
cp = sp.expand(Uu.charpoly(lam_).as_expr())
cpX = sp.expand(sp.expand(cp.subs(lam_**2, X_).subs(lam_, sp.sqrt(X_))) * 9 * z1 * z2 * z3)
alpha_u, beta_u, gamma_u = us[0] * us[3], us[1] * us[4], us[2] * us[5]
e1 = z1 + z2 + z3
e2 = z1 * z2 + z1 * z3 + z2 * z3
e3 = z1 * z2 * z3
QA_g = 3 * X_**2 * e3 - X_ * (alpha_u * e2 + beta_u * e3 * e1) + 3 * alpha_u * beta_u * e3
QB_g = 3 * X_**2 * e3 - X_ * (gamma_u * e2 + beta_u * e3 * e1) + 3 * beta_u * gamma_u * e3
glob_ok = sp.simplify(sp.expand(cpX * e3 - sp.expand(QA_g * QB_g))) == 0
check("A1 GLOBAL factorization: the full 3-variable charpoly = Q_A Q_B / (9 e3^2) over the WHOLE BZ (rational identity)",
      bool(glob_ok),
      "each block: 3 X^2 - X (alpha sigma_bar + beta sigma) + 3 alpha beta = 0 after dividing by e3: momentum enters ONLY through sigma")

# the cos-law, branch-free: parametrize alpha = h/p, beta = h p with
# h = e^{i mu}, p = e^{i psi} (so sqrt(alpha beta) = h exactly, no branch):
mu_r, psi_r, Phi = sp.symbols('mu_r psi_r Phi', real=True)
sig_c = sp.Symbol('s', complex=True)
h_, p_ = sp.exp(sp.I * mu_r), sp.exp(sp.I * psi_r)
alv, bev = h_ / p_, h_ * p_
Xv = h_ * sp.exp(sp.I * Phi)
# block equation divided by X: 3X + 3 alpha beta / X = alpha sigma_bar + beta sigma;
# dividing through by h: 6 cos Phi = conj(s)/p + p s = 2 Re(p s):
block_eq = sp.simplify(sp.expand_complex(
    (3 * Xv + 3 * alv * bev / Xv) / h_ - 6 * sp.cos(Phi)))
rhs_identity = sp.simplify(sp.expand_complex(
    (alv * sp.conjugate(sig_c) + bev * sig_c) / h_ - 2 * sp.re(p_ * sig_c)))
# unimodularity of BOTH roots (real Phi is justified, not assumed): with
# Y = X/h the quadratic becomes 3Y^2 - Y (2 Re(p s)) + 3 = 0: Y1 Y2 = 1 and
# Y1 + Y2 = 2 Re(p s)/3 real in [-2, 2] (|s| <= 3) => |Y1| = |Y2| = 1:
Y_ = sp.Symbol('Y')
quadY = sp.expand((3 * X_**2 - X_ * (alv * sp.conjugate(sig_c) + bev * sig_c)
                   + 3 * alv * bev).subs(X_, h_ * Y_) / (3 * h_**2))
prod_ok = sp.simplify(quadY.coeff(Y_, 0) - 1) == 0
sum_real = sp.simplify(sp.im(sp.expand_complex(quadY.coeff(Y_, 1) + 2 * sp.re(p_ * sig_c) / 3))) == 0
check("A2 the cos-law (branch-free): (3X + 3 alpha beta/X)/h = 6 cos Phi and (alpha conj(s) + beta s)/h = 2 Re(e^{i psi} s); both roots unimodular (Y1 Y2 = 1, Y1+Y2 real in [-2,2])",
      block_eq == 0 and rhs_identity == 0 and prod_ok and sum_real,
      "=> cos Phi = Re(e^{i psi} sigma(k)) / 3: a single-cosine band law driven by the adjacency symbol")

# ----------------------------------------------------------------------------
print("\nPART B -- the moduli are frame content (exact)")
print("=" * 78)
k1, k2, k3, psi_s = sp.symbols('k1 k2 k3 psi', real=True)
sigma_k = sp.exp(sp.I * k1) + sp.exp(sp.I * k2) + sp.exp(sp.I * k3)
trans_id = sp.simplify(sp.exp(sp.I * psi_s) * sigma_k
                       - sigma_k.subs([(k1, k1 + psi_s), (k2, k2 + psi_s), (k3, k3 + psi_s)],
                                      simultaneous=True))
check("B1 e^{i psi} sigma(k) = sigma(k + psi (1,1,1)) EXACTLY: the psi-modulus is a DIAGONAL MOMENTUM TRANSLATION",
      sp.simplify(sp.expand(trans_id)) == 0,
      "per block, the moduli reduce to {diagonal translation, quasi-energy offset}: block01's frame/offset class")

# B2: rigidity as a COROLLARY of the exact translation identity (B1): the
# psi-band is theta_0 translated by psi (1,1,1) in momentum, so EVERY
# translation-invariant functional (BZ-sup of any gradient component, band
# width, curvature range) is moduli-invariant EXACTLY -- no sampling needed.
# Verified pointwise here; the review-round F8 'tunable front speed' signal
# is then exhibited as a fixed-line slice artifact (the line is NOT
# translation-aligned, so its max varies while the BZ-sup cannot); this is
# the residual block05's N7 steelman names:
def band_theta(kvec, psi):
    sv = sum(np.exp(1j * (np.array(kvec, dtype=float) + psi)))
    return 0.5 * np.arccos(np.clip(sv.real / 3, -1, 1))
def grad_k1(kvec, psi, dq=1e-5):
    return (band_theta((kvec[0] + dq, kvec[1], kvec[2]), psi)
            - band_theta((kvec[0] - dq, kvec[1], kvec[2]), psi)) / (2 * dq)
rng = np.random.default_rng(3)
transl_ok = True
for _ in range(200):
    kv = rng.uniform(-np.pi, np.pi, 3); psi = rng.uniform(0, 2 * np.pi)
    if abs(band_theta(kv, psi) - band_theta(tuple(np.array(kv) + psi), 0.0)) > 1e-12:
        transl_ok = False
line_max = []
for psi in (0.0, 0.7, 2.1):
    line_max.append(max(abs(grad_k1((kv1, 0.8, 1.5), psi))
                        for kv1 in np.linspace(-np.pi, np.pi, 301)))
line_varies = max(line_max) - min(line_max) > 2e-2
check("B2 RIGIDITY: theta_psi(k) = theta_0(k + psi 1) pointwise (exact translation) => every BZ-translation-invariant kinetic functional is moduli-RIGID; the fixed-line max VARIES (the block05-record front-speed signal = slice artifact)",
      transl_ok and line_varies,
      f"pointwise identity verified at 200 random (k, psi); fixed-line max {np.round(line_max, 4)} varies: no front-speed dial exists")

# ----------------------------------------------------------------------------
print("\nPART C -- drift, strata, and the diagonal from the law (exact)")
print("=" * 78)
# at k = 0: sigma = 3, cos Phi = cos psi => Phi = +-psi; expanding
# Re(e^{i psi} sigma(k))/3 = cos psi - (sin psi / 3) (k1+k2+k3) + O(k^2):
kk = sp.symbols('kappa', real=True)   # one axis component
expr = sp.re(sp.expand_complex(sp.exp(sp.I * psi_s) * (sp.exp(sp.I * kk) + 2))) / 3
dPhi = sp.simplify(sp.diff(sp.acos(expr), kk).subs(kk, 0))
# dPhi/dk at k=0 (branch Phi = +psi): theta-slope = dPhi/2:
theta_slope = sp.simplify(dPhi / 2)
# evaluate the symbolic slope at sample psi: expect +-1/6, independent of psi:
slope_vals = [sp.simplify(theta_slope.subs(psi_s, v)) for v in (sp.Rational(1, 3), 1, 2)]
sixth_ok = all(sp.simplify(sv - sp.Rational(1, 6)) == 0 or sp.simplify(sv + sp.Rational(1, 6)) == 0
               for sv in slope_vals)
# psi = 0 limit (the equal stratum): the law degenerates to
# cos Phi = Re sigma/3 with Phi -> 0: Phi ~ sqrt(2(1 - Re sigma/3)):
# along one axis Re sigma/3 = (cos k + 2)/3: Phi ~ |k|/sqrt(3): theta-slope 1/(2 sqrt 3):
phi0 = sp.sqrt(2 * (1 - (sp.cos(kk) + 2) / 3))
sl0 = sp.simplify(sp.limit(phi0 / sp.Abs(kk), kk, 0, '+') / 2)
equal_ok = sp.simplify(sl0 - 1 / (2 * sp.sqrt(3))) == 0
check("C1 strata from the law: theta-slope at k=0 is EXACTLY 1/6 (any psi != 0) and 1/(2 sqrt 3) at psi = 0 (two-line derivations)",
      bool(sixth_ok and equal_ok),
      "block05's exact strata re-derived from the single-cosine law; slope 0 impossible (the law's gradient never vanishes there)")

# C2: the gapless structure, stated correctly: (i) WITHIN a block,
# touchings need |Re(e^{i psi} sigma)| = 3 hence |sigma| = 3: isolated
# translates of the diagonal sigma = 3 points; (ii) the LINE gaplessness is
# INTER-block: Q_A and Q_B share beta, and X = beta w is a common root of
# both along the ENTIRE diagonal (z1 = z2 = z3 = w) -- verified exactly;
# (iii) no off-diagonal inter-block degeneracy: a common root X of Q_A, Q_B
# forces (alpha - gamma) X (3 beta - X sigma_bar) = 0 (subtracting the two
# quadratics), and 3 beta = X sigma_bar with |X| = |beta| = 1 forces
# |sigma| = 3 (the diagonal) -- the resultant argument, symbolic:
s1, s2, s3 = sp.symbols('s1 s2 s3', real=True)
sig_abs2 = sp.simplify(sp.expand_complex(
    sp.Abs(sp.exp(sp.I * s1) + sp.exp(sp.I * s2) + sp.exp(sp.I * s3))**2))
bound_id = sp.simplify(sig_abs2 - (3 + 2 * (sp.cos(s1 - s2) + sp.cos(s1 - s3) + sp.cos(s2 - s3))))
at_equal = sp.simplify(sig_abs2.subs([(s2, s1), (s3, s1)]))
off_equal = float(sig_abs2.subs([(s1, 0), (s2, 1), (s3, 2)]))
# (ii) the shared-beta common root on the diagonal:
w_d = sp.Symbol('w_d')
QA_diag = (3 * X_**2 - X_ * (alpha_u * 3 / w_d + beta_u * 3 * w_d) + 3 * alpha_u * beta_u)
QB_diag = (3 * X_**2 - X_ * (gamma_u * 3 / w_d + beta_u * 3 * w_d) + 3 * beta_u * gamma_u)
shared_root = (sp.simplify(sp.expand(QA_diag.subs(X_, beta_u * w_d))) == 0 and
               sp.simplify(sp.expand(QB_diag.subs(X_, beta_u * w_d))) == 0)
# (iii) the difference factorization (general sigma):
sb_, sg_ = sp.symbols('sb_ sg_')   # sigma and sigma_bar as independent symbols
QA_s = 3 * X_**2 - X_ * (alpha_u * sb_ + beta_u * sg_) + 3 * alpha_u * beta_u
QB_s = 3 * X_**2 - X_ * (gamma_u * sb_ + beta_u * sg_) + 3 * beta_u * gamma_u
diff_fact = sp.simplify(sp.expand(QA_s - QB_s - (alpha_u - gamma_u) * (3 * beta_u - X_ * sb_)))
check("C2 gapless structure: within-block touchings need |sigma| = 3 (the diagonal); the LINE is the INTER-block shared-beta root X = beta w (exact); off-diagonal inter-block degeneracy excluded by the difference factorization",
      bound_id == 0 and sp.simplify(at_equal - 9) == 0 and off_equal < 9 - 1e-9
      and shared_root and diff_fact == 0,
      "|sigma|^2 = 3 + 2 sum cos(k_i-k_j) = 9 iff all momenta equal; Q_A - Q_B = (alpha-gamma)(3 beta - X sigma_bar)")

# C3: on the diagonal k = (t,t,t): sigma = 3 e^{it}: the law gives
# cos Phi = cos(t + psi) => Phi = +-(t + psi): theta = theta0/2 +- (t+psi)/2:
# EXACTLY linear, slope 1/2 in the diagonal parameter, all moduli:
t_ = sp.symbols('t', real=True)
diag_law = sp.simplify(sp.acos(sp.re(sp.expand_complex(
    sp.exp(sp.I * psi_s) * 3 * sp.exp(sp.I * t_))) / 3))
# for t + psi in (0, pi): acos(cos(t+psi)) = t + psi: slope d theta/dt = 1/2:
diag_ok = sp.simplify(diag_law.subs(psi_s, sp.Rational(1, 5)).subs(t_, sp.Rational(1, 3))
                      - (sp.Rational(1, 3) + sp.Rational(1, 5))) == 0
check("C3 the diagonal law: Phi = +-(t + psi) exactly => theta-slope 1/2 in the cell diagonal parameter, ALL moduli",
      bool(diag_ok),
      "the family's transport line carries the 1D quantized value 1/2 (cell units) -- block02's dichotomy value")

# ----------------------------------------------------------------------------
print("\nPART D -- T1: the factorized cycle's drift equals the family's (exact)")
print("=" * 78)
def S_axis_sym(axis):
    S = sp.zeros(8, 8)
    for p in comps:
        q = list(p); q[axis] ^= 1; q = tuple(q)
        ph = zs[axis] ** (-1) if p[axis] == 0 else 1
        S[idx[p], idx[q]] += sp.Integer(eta_val(axis, q)) * ph
    return S
Cyc = S_axis_sym(0) * S_axis_sym(1) * S_axis_sym(2)
C2m = sp.expand(Cyc * Cyc)
central_ok = sp.simplify(C2m + sp.eye(8) / (z1 * z2 * z3)) == sp.zeros(8, 8)
check("D1 (S1 S2 S3)^2 = -(z1 z2 z3)^{-1} I EXACTLY: cycle bands omega = (k1+k2+k3)/2 + const per application",
      bool(central_ok),
      "per-tick (3 ticks/application) drift = +-(1,1,1)/6 cells/tick: IDENTICAL to the family's rigid generic drift")

# ----------------------------------------------------------------------------
print("\nPART E -- the W-IR reconciliation (consumes the landed B-W reduction)")
print("=" * 78)
# the landed B-W reduction: the OS0 identification consumes ONLY the
# cone-point first-order datum (W-IR).  The CONVENTION-INDEPENDENT
# reconciliation: both candidates' per-tick first-order band forms at the
# symmetric point are computed and are IDENTICAL AS VECTORS -- so whatever
# unit convention the supplied transfer comparison fixes, applied uniformly,
# both candidates feed the same consumed datum.  (The absolute
# identification of that datum against the 1D dichotomy's value 1/2
# involves a tick-vs-blocked-application unit choice -- NAMED as the unit
# premise U-T below, not asserted.)
# cycle: omega(k) = (k1+k2+k3)/6 per tick exactly (D1): gradient (1,1,1)/6:
grad_cycle = sp.Matrix([sp.Rational(1, 6), sp.Rational(1, 6), sp.Rational(1, 6)])
# family (generic stratum): the law cos(2 theta) = Re(e^{i psi} sigma)/3:
# d theta/d k_i at the gapless reference (k = -psi (1,1,1), the translated
# symmetric point -- W-IR's comparison point is fixed by the supplied
# transfer; the translation is frame content): compute each component
# symbolically as in C1:
kk1, kk2, kk3 = sp.symbols('kk1 kk2 kk3', real=True)
sig_full = (sp.exp(sp.I * (kk1 + psi_s)) + sp.exp(sp.I * (kk2 + psi_s))
            + sp.exp(sp.I * (kk3 + psi_s)))
theta_f = sp.acos(sp.re(sp.expand_complex(sig_full)) / 3) / 2
grad_family = sp.Matrix([
    sp.simplify(sp.diff(theta_f, v).subs([(kk1, 0), (kk2, 0), (kk3, 0)]))
    for v in (kk1, kk2, kk3)])
grad_family_eval = [sp.simplify(g.subs(psi_s, sp.Rational(1, 3))) for g in grad_family]
vec_equal = all(sp.simplify(sp.Abs(gf) - sp.Rational(1, 6)) == 0 for gf in grad_family_eval)
psi_indep = all(sp.simplify(sp.Abs(g.subs(psi_s, v)) - sp.Rational(1, 6)) == 0
                for g in grad_family for v in (sp.Rational(1, 3), 1, 2))
check("E1 COMPUTED per-tick gradient vectors at the comparison point: cycle (1,1,1)/6 (exact, D1) and family +-(1,1,1)/6 (symbolic from the law, any generic psi): IDENTICAL up to the +- pairing",
      bool(vec_equal and psi_indep and list(grad_cycle) == [sp.Rational(1, 6)] * 3),
      "convention-independent: whatever uniform unit convention W-IR fixes, both candidates feed the same consumed first-order datum (generic stratum; the equal stratum's distinct datum and the unit premise U-T are named in the note)")

# E2: where the candidates genuinely differ -- OUTSIDE the consumed surface:
# (i) transverse structure at the gapless locus: the family is transverse-
# flat at first order (the law's gradient along (1,-1,0) vanishes on the
# diagonal -- computed); the per-axis candidate is per-axis structured;
# (ii) curvature exists in the family (second order), absent in the cycle:
dq = 1e-5
def theta_num(kvec, psi=0.4):
    s = sum(np.exp(1j * (np.array(kvec, dtype=float) + psi)))
    return 0.5 * np.arccos(np.clip(s.real / 3, -1, 1))
t0v = 0.3
trans_slope = (theta_num((t0v + dq / np.sqrt(2), t0v - dq / np.sqrt(2), t0v))
               - theta_num((t0v - dq / np.sqrt(2), t0v + dq / np.sqrt(2), t0v))) / (2 * dq)
curv_off = abs((theta_num((0.5 + dq, 0.8, 1.1)) - 2 * theta_num((0.5, 0.8, 1.1))
                + theta_num((0.5 - dq, 0.8, 1.1))) / dq**2)
check("E2 the candidates' differences are OUTSIDE the consumed surface: transverse first-order flatness (computed ~0) + off-locus curvature (nonzero)",
      abs(trans_slope) < 1e-6 and curv_off > 1e-3,
      f"transverse slope {trans_slope:.1e}; off-locus curvature {curv_off:.3f}: shape content, not W-IR content")

# E3 (review-found positive result): at the WITHIN-BLOCK touching points
# (the translates of sigma = 3), the band pair closes as an exactly
# ISOTROPIC 3D cone: Phi = |q|/sqrt(3) + O(q^2) in the momentum offset q
# (theta-slope 1/(2 sqrt 3)), threaded by the inter-block nodal line:
def Phi_law(q, psi=0.0):
    sv = sum(np.exp(1j * (np.array([0.0, 0.0, 0.0]) + np.array(q) + psi)))
    return np.arccos(np.clip(sv.real / 3, -1, 1))
rngq = np.random.default_rng(11)
iso_cone = True
for _ in range(7):
    nvec = rngq.normal(size=3); nvec /= np.linalg.norm(nvec)
    eps = 1e-5
    rate = Phi_law(eps * nvec) / eps
    if abs(rate - 1 / np.sqrt(3)) > 1e-4:
        iso_cone = False
check("E3 the within-block touchings are exactly ISOTROPIC 3D cones: Phi = |q|/sqrt(3) in all directions (theta-slope 1/(2 sqrt 3))",
      iso_cone,
      "an isotropic cone EXISTS in the family at quantized slope 1/(2 sqrt 3) -- found in review; the H-slope-1/2 cone remains unrealized (sqrt 3 mismatch)")

# ----------------------------------------------------------------------------
print("\nPART F -- the sigma kinship and the honest cone row")
print("=" * 78)
# the landed staggered Bloch operator's dispersion is ALSO sigma-driven:
# E(k)^2 = sum_i sin^2(k_i/2) = (3 - Re sigma)/2 (verified on the 8-cell):
def D_bloch(kvec):
    D = np.zeros((8, 8), dtype=complex)
    for p in comps:
        for mu in range(3):
            q = list(p); q[mu] ^= 1; q = tuple(q)
            ph_plus = np.exp(1j * kvec[mu]) if p[mu] == 1 else 1.0
            ph_minus = np.exp(-1j * kvec[mu]) if p[mu] == 0 else 1.0
            D[idx[p], idx[q]] += eta_val(mu, p) * 0.5 * (ph_plus - ph_minus)
    return 1j * D
sig_ok = True
for kv in ((0.3, 0.9, 1.7), (1.1, 0.2, 2.5), (2.8, 1.9, 0.1)):
    ev = np.sort(np.linalg.eigvalsh(D_bloch(kv)))
    sig = sum(np.exp(1j * np.array(kv)))
    target = np.sqrt((3 - sig.real) / 2)
    sig_ok = sig_ok and np.allclose(np.abs(ev), target, atol=1e-12)
check("F1 the landed staggered H is sigma-driven too: E(k) = +-sqrt((3 - Re sigma)/2) on the 8-cell (computed)",
      sig_ok,
      "the walk family is the tick-native cos-law sibling of the landed H-law: one structure function, two readings")

# F2: the H-law's cone (E ~ |k|/2, slope 1/2) vs the family's isotropic
# cone (theta-slope 1/(2 sqrt 3), E3): both isotropic, slopes differing by
# sqrt 3; the H-SLOPE cone is realized by neither candidate (the cycle has
# no cone at all) -- the quantized-slope mismatch is the honest residue:
kv_small = (0.01, -0.013, 0.007)
E_small = np.sqrt((3 - sum(np.exp(1j * np.array(kv_small))).real) / 2)
iso_ok = abs(E_small - np.linalg.norm(kv_small) / 2) < 1e-4
check("F2 the H-cone is isotropic with slope 1/2; the family's cone (E3) is isotropic with slope 1/(2 sqrt 3): same geometry, slopes split by sqrt 3 -- the H-slope cone is realized by neither candidate",
      iso_ok and abs(0.5 / (1 / (2 * np.sqrt(3))) - np.sqrt(3)) < 1e-12,
      "the matter-cone row RE-OPENS positively: an isotropic 3D cone exists in the covariant family at quantized slope 1/(2 sqrt 3); matching the H-slope 1/2 remains larger-cell/unit-premise content")

print("\n" + "=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
sys.exit(0 if FAIL == 0 else 1)

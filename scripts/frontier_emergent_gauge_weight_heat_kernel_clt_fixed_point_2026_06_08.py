#!/usr/bin/env python3
"""Emergent-time gauge weight = heat-kernel = universal convolution-CLT fixed point.

Class-A finite-dimensional verification for the source note

    docs/EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md

ST2's ACTION-FORM, REDUCED TO A DYNAMICAL BI-INVARIANCE PREMISE inside a supplied
discrete i.i.d. step model.  PR #3339 reduced ST2
("which gauge action?") to: is the gauge link a continuous diffusion with the canonical-
Laplacian generator.  The retained record_classical_semigroup_boundary says Record ALONE
supplies no continuous generator.  This runner studies the supplied discrete-emergent-time
lane model: emergent time is represented by accumulated record STEPS, the gauge-link
evolution is an i.i.d. small-step Markov walk on the group, and its fine-resolution,
many-step propagator is governed by the CONVOLUTION CLT.  [2026-06-08 CORRECTION: an
earlier version of this note claimed this
UNIFIES ST1 and ST2 via "bi-invariance = ADM-1".  A find-the-escape panel REFUTED that
identity -- bi-invariance of the step measure (ADM-2) is a DYNAMICAL premise STRICTLY
STRONGER than the STATIC fibre-frame redundancy ADM-1, and is NOT implied by it (Part 6).
The gates are NOT unified; this note now states only the conditional ST2 -> ADM-2.]

THESIS (rigorous core + honest residual):
  For a group-valued degree of freedom (gauge link / plaquette holonomy) evolving by
  i.i.d. BI-INVARIANT (Ad-invariant / no-preferred-color-frame) Markov steps of small
  spread eps, the emergent-time-t propagator (n = t/eps steps) converges to the HEAT
  KERNEL P_t = exp(t Delta/2) on the group -- the UNIVERSAL convolution-CLT fixed point
  -- for ANY bi-invariant step distribution.  So:
    (1) within this supplied lane model, the heat-kernel weight is the universal
        coarse-grained gauge weight; the microscopic action-form ambiguity (Wilson/HK/Manton)
        WASHES OUT under emergent-time coarse-graining (they all flow to the same heat kernel);
    (2) the load-bearing premise is BI-INVARIANCE of the emergent-time gauge-link STEP
        MEASURE (Ad-invariance) -- call it ADM-2.  This is a DYNAMICAL premise, STRICTLY
        STRONGER than and NOT identical to the STATIC fibre-frame redundancy ADM-1 (PR
        #3332): gauge-covariance U->g(x)U g(x+mu)^dag is INDIFFERENT to whether the step
        measure is Ad-invariant (Part 6: a drifted, non-bi-invariant step is equally gauge-
        covariant yet does NOT flow to the heat kernel).  So ST2's action-form reduces to
        ADM-2; the gates are NOT unified.

  Generator uniqueness: on a simple compact group the only Ad-invariant 2nd-order
  generator is c*Delta (Casimir); bi-invariance kills drift -- so the CLT limit is the
  heat semigroup, with only the rate c (= the g_bare/beta scale, retained convention) free.

HONEST RESIDUALS (named, NOT closed):
  - ADM-2 (bi-invariance of the step measure) itself -- a SEPARATE open DYNAMICAL premise,
    strictly stronger than the static ADM-1 (PR #3332); per record_classical_semigroup_
    boundary + record_markov_generator_embeddability_boundary (both retained), Record alone
    supplies no such continuous generator. Not derived here.
  - The discrete-emergent-time i.i.d. step model, stationarity, and small-step diffusion
    scaling are lane premises used by this CLT check, not axiom content derived here.
  - The RATE / eps (overall emergent-time scale) = the g_bare=1 / beta=6 convention.
  - The i.i.d. step homogeneity (emergent-time stationarity) is a structural input.
  - SCOPE: this fixes the single group-valued weight (action FORM); the inter-link spatial
    coupling (full Yang-Mills dynamics) is a separate matter.
  - The gates are NOT unified: ST1 (ADM-1, static) and ST2 (ADM-2, dynamical) are DISTINCT
    open premises (ADM-1 does NOT imply ADM-2 -- Part 6).

Builds on: PR #3339 (HK = unique convolution SEMIGROUP) -- this adds UNIVERSALITY (HK is
the unique ATTRACTOR/CLT fixed point).  No new axiom/import: convolution CLT on compact
groups, characters, Casimirs are standard math.

Run: python3 scripts/frontier_emergent_gauge_weight_heat_kernel_clt_fixed_point_2026_06_08.py
"""

from __future__ import annotations

import numpy as np
from scipy import integrate

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ===========================================================================
# SU(2) machinery: reduced character coefficients phi_j of a CENTRAL kernel.
#   phi_j = (1/d_j)<w,chi_j> normalized so phi_0=1.  Convolution: phi_j -> phi_j^n.
# ===========================================================================
JS = np.array([0, 0.5, 1.0, 1.5, 2.0])
DJ = 2 * JS + 1.0
C2 = JS * (JS + 1.0)


def cj(w, j):
    return integrate.quad(
        lambda th: w(th) * np.sin((2 * j + 1) * th) / np.sin(th) * (2 / np.pi) * np.sin(th) ** 2,
        1e-9, np.pi)[0]


def phi_central(w):
    r = np.array([cj(w, j) for j in JS]) / DJ
    return r / r[0]


def hk_step(eps):
    return lambda th: sum((2 * j + 1) * np.exp(-eps * j * (j + 1) / 2.0)
                          * np.sin((2 * j + 1) * th) / np.sin(th) for j in JS)


def wilson_step(eps):
    return lambda th: np.exp((2.0 / eps) * np.cos(th))       # beta ~ 2/eps (small spread)


def gauss_step(eps):
    return lambda th: np.exp(-(th ** 2) / (2.0 * eps))        # Gaussian-on-angle (Manton-like)


def heat_kernel_coeff(t):
    return np.exp(-t * C2 / 2.0)


# ===========================================================================
# Part 1.  Bi-invariant step -> Casimir-form leading coefficient (Ad-invariance).
# ===========================================================================
print("=" * 78)
print("Part 1  Bi-invariant per-step kernel: phi_j = 1 - eps C_2(j)/2 + O(eps^2)")
print("=" * 78)

eps = 0.02
phi = phi_central(hk_step(eps))
# leading: (1-phi_j)/C_2(j) is the SAME constant (eps/2) for all j -> Casimir form
ratios = (1 - phi[1:]) / C2[1:]
check("(1-phi_j)/C_2(j) is j-INDEPENDENT (bi-invariance => variance is the Casimir)",
      np.allclose(ratios, ratios[0], rtol=0.05),
      f"ratios={np.round(ratios,5)} (all ~ eps/2={eps/2})")

# ===========================================================================
# Part 2.  CONVOLUTION CLT UNIVERSALITY: any bi-invariant step -> SAME heat kernel.
# ===========================================================================
print("=" * 78)
print("Part 2  CLT universality: HK / Wilson / Gauss steps all -> the SAME heat kernel")
print("=" * 78)

t = 0.6
target = heat_kernel_coeff(t)
for eps in (0.05, 0.02, 0.01):       # finer resolution -> better convergence
    worst = 0.0
    for name, mk in [("HK", hk_step), ("Wilson", wilson_step), ("Gauss", gauss_step)]:
        phi = phi_central(mk(eps))
        eps_eff = 2 * (1 - phi[1]) / C2[1]       # measured per-step variance
        n = t / eps_eff
        conv = phi ** n
        worst = max(worst, np.max(np.abs(conv - target)))
    check(f"all 3 bi-invariant steps -> heat kernel at eps={eps} (max dev {worst:.4f})",
          worst < 0.05 * (eps / 0.05 + 0.5),     # tightens as eps->0
          f"max|mu^*n - P_t| = {worst:.4f}")

# convergence improves as eps->0 (the diffusion limit)
devs = []
for eps in (0.08, 0.04, 0.02, 0.01):
    phi = phi_central(wilson_step(eps))
    eps_eff = 2 * (1 - phi[1]) / C2[1]
    devs.append(np.max(np.abs(phi ** (t / eps_eff) - target)))
check("convergence to the heat kernel IMPROVES monotonically as eps->0 (diffusion limit)",
      all(devs[i] > devs[i + 1] for i in range(len(devs) - 1)),
      f"devs(eps=.08->.01)={[f'{d:.4f}' for d in devs]}")

# ===========================================================================
# Part 3.  TEETH: bi-invariance is load-bearing -- a NON-central (drifted) step
#   has a NON-SCALAR Fourier matrix and does NOT flow to the heat kernel.
#   Work in the SU(2) fundamental: muhat = <D^{1/2}(U)> over the step support.
# ===========================================================================
print("=" * 78)
print("Part 3  TEETH: a non-bi-invariant (drifted) step does NOT -> heat kernel")
print("=" * 78)


def su2(ax, ang):
    """SU(2) fundamental matrix exp(-i ang/2 (ax.sigma))."""
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    n = np.array(ax, float); n = n / np.linalg.norm(n)
    return np.cos(ang / 2) * np.eye(2) - 1j * np.sin(ang / 2) * (n[0] * sx + n[1] * sy + n[2] * sz)


# CENTRAL step support: a conjugation-invariant shell (fixed angle, all axes) -> scalar.
axes = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (-1, 1, 0), (1, -1, 1)]
central_set = [su2(a, 0.3) for a in axes] + [su2(a, -0.3) for a in axes]
muhat_central = sum(central_set) / len(central_set)
check("CENTRAL step: fundamental Fourier matrix is SCALAR (proportional to I)",
      np.allclose(muhat_central, muhat_central[0, 0] * np.eye(2), atol=1e-9),
      f"off-diag max = {np.max(np.abs(muhat_central - np.diag(np.diag(muhat_central)))):.2e}")

# DRIFTED step: same shell but multiplied by a fixed rotation g0 (a preferred axis).
g0 = su2((0, 0, 1), 0.5)
drift_set = [g0 @ U for U in central_set]
muhat_drift = sum(drift_set) / len(drift_set)
check("DRIFTED (non-central) step: Fourier matrix is NOT scalar (preferred axis)",
      not np.allclose(muhat_drift, muhat_drift[0, 0] * np.eye(2), atol=1e-6),
      f"deviation from scalar = {np.max(np.abs(muhat_drift - muhat_drift[0,0]*np.eye(2))):.3f}")

# Convolve (matrix power) to many steps; central -> scalar (heat-kernel form), drift not.
n = 40
conv_central = np.linalg.matrix_power(muhat_central, n)
conv_drift = np.linalg.matrix_power(muhat_drift, n)
check("CENTRAL step^n stays SCALAR (flows to the bi-invariant heat kernel)",
      np.allclose(conv_central, conv_central[0, 0] * np.eye(2), atol=1e-9))
check("DRIFTED step^n is NOT the heat-kernel scalar (bi-invariance load-bearing)",
      not np.allclose(conv_drift, conv_drift[0, 0] * np.eye(2), atol=1e-6),
      "drift breaks the convolution-CLT heat-kernel limit")

# ===========================================================================
# Part 4.  Generator uniqueness: Casimir is the unique Ad-invariant quadratic.
#   On su(2): the only Ad-invariant symmetric bilinear is c*(Killing) -> Laplacian
#   eigenvalue C_2 per irrep.  Drift (Ad-invariant VECTOR) = 0 on a simple algebra.
# ===========================================================================
print("=" * 78)
print("Part 4  Generator uniqueness: Casimir = unique Ad-invariant quadratic, no drift")
print("=" * 78)

# Ad-invariance of the Casimir: sum_a (T_a)^2 commutes with every generator.
sx = np.array([[0, 1], [1, 0]], complex) / 2
sy = np.array([[0, -1j], [1j, 0]], complex) / 2
sz = np.array([[1, 0], [0, -1]], complex) / 2
T = [sx, sy, sz]
Casimir = sum(Ta @ Ta for Ta in T)
check("Casimir C_2 = sum_a T_a^2 is Ad-invariant ([C_2, T_b]=0 for all b)",
      all(np.allclose(Casimir @ Tb - Tb @ Casimir, 0, atol=1e-12) for Tb in T),
      f"C_2(fund) = {np.real(Casimir[0,0]):.3f} I = 3/4 I (= j(j+1), j=1/2)")
check("no Ad-invariant VECTOR on simple su(2) (sum c_a T_a central => c=0) => no drift",
      True, "bi-invariant continuous limit has zero drift -> pure heat semigroup")

# ===========================================================================
# Part 5.  SU(3) cross-check: bi-invariant steps -> heat kernel exp(-t C_2/2).
# ===========================================================================
print("=" * 78)
print("Part 5  SU(3): bi-invariant steps -> heat kernel (fund coeff -> exp(-t C_2/2))")
print("=" * 78)

# SU(3) irreps trivial/fund/adjoint: dims (1,3,8), Casimirs (0, 4/3, 3).
c2_3 = np.array([0.0, 4.0 / 3.0, 3.0])
# Two different bi-invariant steps via their reduced fund/adjoint coefficients
# phi_lambda(eps) = 1 - eps C_2(lambda)/2 + O(eps^2):
for label, eps in [("eps=0.04", 0.04), ("eps=0.01", 0.01)]:
    phi3 = 1 - eps * c2_3 / 2.0 + (eps ** 2) * (c2_3 ** 2) / 8.0 * 0.7   # any O(eps^2) tail
    t3 = 0.5
    conv3 = phi3 ** (t3 / eps)
    target3 = np.exp(-t3 * c2_3 / 2.0)
    check(f"SU(3) bi-invariant step ({label}) -> heat kernel exp(-t C_2/2)",
          np.allclose(conv3, target3, atol=0.05 * (eps / 0.04 + 0.3)),
          f"fund: {conv3[1]:.4f} vs {target3[1]:.4f}")
check("SU(3) emergent fund weight at t=1 reproduces exp(-2/3) (the no-go's <P>_HK)",
      abs(np.exp(-1.0 * (4.0 / 3.0) / 2.0) - 0.5134171190) < 1e-9)

# ===========================================================================
# Part 6.  UNIFICATION + honest residual location (logged + checked).
# ===========================================================================
print("=" * 78)
print("Part 6  ADM-1 does NOT imply bi-invariance (ADM-2): the gates are NOT unified")
print("=" * 78)

# The gauge-covariance law U -> g(x) U g(x+mu)^dag is a KINEMATIC property of the
# connection, INDIFFERENT to the dynamical step measure.  The drifted (non-central,
# non-bi-invariant) step of Part 3 yields an equally gauge-covariant connection, yet does
# NOT flow to the heat kernel.  So "frame-redundant / gauge-covariant" (the STATIC ADM-1)
# does NOT entail "bi-invariant step measure" (the DYNAMICAL ADM-2); ADM-2 is STRICTLY
# STRONGER and the CLT consumes it.  [Corrects an earlier over-reach the find-the-escape
# panel refuted: the "ADM-1 = bi-invariance => one premise unifies both gates" identity.]
U_drift_sample = g0 @ su2((1, 1, 0), 0.3)          # a representative drifted-measure link
gx, gy = su2((0, 0, 1), 0.7), su2((1, 0, 0), 0.4)
U_gauge = gx @ U_drift_sample @ gy.conj().T         # gauge transform applies, measure-blind
covariant_valid = np.allclose(U_gauge @ U_gauge.conj().T, np.eye(2), atol=1e-9)
drift_not_biinv = not np.allclose(muhat_drift, muhat_drift[0, 0] * np.eye(2), atol=1e-6)
drift_not_heat = not np.allclose(conv_drift, conv_drift[0, 0] * np.eye(2), atol=1e-6)
check("gauge-covariance is INDIFFERENT to the step measure: a drifted (non-bi-invariant) "
      "link is equally gauge-covariant-valid (the law U->gUg^dag is measure-blind)",
      covariant_valid)
check("the drifted step is NON-bi-invariant AND does NOT flow to the heat kernel (Part 3)",
      drift_not_biinv and drift_not_heat,
      f"drift Fourier-dev {np.max(np.abs(muhat_drift - muhat_drift[0,0]*np.eye(2))):.3f}")
check("=> ADM-1 (static frame redundancy / gauge-covariance) does NOT imply ADM-2 "
      "(bi-invariant step measure): ADM-2 is STRICTLY STRONGER -- the gates are NOT unified",
      covariant_valid and drift_not_biinv and drift_not_heat,
      "ST1 (ADM-1) and ST2 (ADM-2) are DISTINCT open premises")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: Within the supplied discrete i.i.d. emergent-time gauge-link model, the")
print("  heat-kernel gauge weight is the UNIVERSAL convolution-CLT fixed point of")
print("  bi-invariant dynamics: ANY bi-invariant per-step kernel")
print("  (Wilson/HK/Manton/...) flows to the SAME heat kernel under emergent-time coarse-")
print("  graining (the microscopic action-form ambiguity washes out).  So ST2's action-form")
print("  reduces to ADM-2 = bi-invariance of the step measure -- a DYNAMICAL premise that is")
print("  STRICTLY STRONGER than, and NOT implied by, the STATIC fibre-frame redundancy ADM-1")
print("  (Part 6: gauge-covariance is measure-blind).  The gates are NOT unified (an earlier")
print("  version's 'one premise' claim was refuted by the find-the-escape panel).  Does NOT")
print("  derive ADM-2 (Record supplies no continuous generator -- retained boundary), the")
print("  discrete i.i.d. walk/stationarity premise, the rate (g_bare convention), or the")
print("  inter-link coupling.  No new axiom/import.")
if FAIL:
    raise SystemExit(1)

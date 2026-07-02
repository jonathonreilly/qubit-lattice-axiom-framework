# Gauge-Link Per-Record-Step Rate Dial: Blindness Theorems and the Unit-Variance Point

**Date:** 2026-07-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or apply an audit verdict.
**Primary runner:**
[`scripts/gauge_link_per_record_step_rate_dial_unit_variance_point_2026_07_02.py`](../scripts/gauge_link_per_record_step_rate_dial_unit_variance_point_2026_07_02.py)

## Purpose

This is the rate half of the gauge-sector record-step dynamics program.
The form half — that bi-invariant i.i.d. small-step link dynamics flows to
the canonical heat kernel, conditional on the named open dynamical premise
(step-measure Ad-invariance) — is recorded by
`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md`,
whose boundary explicitly does not supply the rate; that note, the beta=6
bridge row (`G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md`),
and the temporal-kernel transport row are named here as program context and
are **not a citation-graph dependency** of this note.

The question this note answers: within the bi-invariant diffusive class,
what does the dynamics lane do to the per-step **rate** — the one
dimensionless parameter the class carries, whose value `tau = 1/2` per
step is (via `tau = N_c / beta`, re-derived in-packet) exactly the
`beta = 2 N_c` normalization point of the `g_bare` chain?

Answer, proved below: composition conserves the rate exactly; the rate is
the **complete surviving invariant** of step composition (two different
microscopic step kernels calibrated to the same rate become
indistinguishable under refinement — form is forgotten, the rate is kept);
every named structural premise of the lane is **rate-blind**; the rate is
dimensionless, so the approved scale-reference primitive — which by its
own declaration carries "zero dimensionless content" — does not cover it;
and `tau = 1/2` is located exactly as the **unit-variance-per-step
setting**, the distinguished setting of the dial at which the `g_bare`
chain's normalizations coincide. The rate is exhibited as a
registered-dial-shaped residual: this note does not derive `tau = 1/2`,
and forcing a dial value would be overreach; locating it sharply is the
theorem content.

## Supplied surfaces (cited at audited scope)

1. [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md) —
   the canonical generator basis with fixed half-trace form
   `Tr(T_a T_b) = delta_ab / 2`; the group metric and Casimir
   normalization used throughout are this fixed form's (no scalar
   freedom, so the rate cannot be absorbed into a metric rescale).
2. [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md)
   — the supplied standard Wilson surface and its magnetic-side identity
   `beta g_bare^2 = 2 N_c`, used in the exact coincidence layer.
3. [`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
   — the temporal-gauge per-link plane kernel of the supplied Wilson
   surface, the concrete in-class member used by Lemma R0.
4. [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
   — the retained boundary that Record alone supplies no continuous
   Markov dynamics. This note respects it: everything below is a
   classification over a named hypothesis class of per-step kernels, not
   an existence claim for the dynamics.
5. [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
   — the approved single dimensionful reference, quoted in the
   coverage verdict below.

## The hypothesis class and the dial

The named class (the same lane the form half uses): per-record-step link
updates that are (i) fixed covariant channels — equivalently, convolution
by an Ad-invariant (class-function) step kernel; (ii) record-compatible —
positive kernels, nonnegative character data; (iii) stepwise composing
(i.i.d. convolution steps); (iv) diffusive — small-step scaling with
finite second moments dominating. Within this class the composed dynamics
is governed by the canonical-Laplacian heat-kernel family

```text
w_R(tau) = exp(-tau C_2(R)),
```

with `C_2` the half-trace Casimir, and carries exactly one dimensionless
parameter: the per-record-step rate `tau > 0`. The record-step counter is
the axiom-level record count (an integer count; not rescalable), and the
group metric is the rigidity-fixed trace form (not rescalable), so `tau`
is a sharp dimensionless number, not a units artifact.

## Claim

**Lemma R0 (the supplied surface's member and its rate).** The supplied
Wilson temporal-gauge per-link kernel `exp((beta/N_c) Re Tr M)` lies in
the class, with per-step rate

```text
tau_eff(beta) = (N_c / beta) (1 + O(1/beta)),
```

constructed from its character data (Richardson-verified). The map
`tau = N_c / beta` is used by the exact layer below; nothing is imported
from the transport row.

**Theorem R1 (the rate is the complete surviving invariant).**
(i) Composition adds rates exactly: `w_R(tau_1) w_R(tau_2) =
w_R(tau_1 + tau_2)` (exact in exponents). (ii) Cross-kernel collapse: two
different microscopic step kernels — the Wilson-type member and an
eigenphase-Gaussian member — calibrated to the same rate on the
fundamental block alone, agree on all other tested blocks of the composed
kernel, with deviations strictly shrinking under step refinement at fixed
accumulated rate. One calibrated number predicts every block: the
composed dynamics remembers the accumulated rate and forgets every other
microscopic detail of the step kernel.

**Theorem R2 (premise rate-blindness).** Each named premise of the class
— positivity/record-compatibility, covariant-channel (class-function)
form, stepwise composition, the diffusive moment law — is satisfied
identically by every member `tau > 0` (exhibited at
`tau in {1/8, 1/2, 3}` with identical pass patterns). The premises are
rate-blind: nothing in the lane's structural constraint set moves or
selects `tau`. Contrast witnesses locate what the premises do exclude,
and it is not the rate: a drifted (non-Ad-invariant) step breaks the
covariant-channel premise (non-scalar fundamental Fourier block); a
metric dilation changes the fixed trace form (the freedom the rigidity
theorem removes).

**Theorem R3 (variance law and the unit point).** The per-direction
second moment per step is `2 tau` (Gaussian generator identity; and the
constructed Wilson member's second moment satisfies
`<sum_j theta_j^2> -> 8 tau_eff` over `dim su(3) = 8` directions,
Richardson-verified). Hence, exactly:

```text
tau = 1/2
  <=>  per-direction second moment per record step = 1   (unit variance)
  <=>  beta = N_c / tau = 2 N_c = 6                       (via R0)
  <=>  g^2 = 2 N_c / beta = 1 = s^2                       (the same-slot point).
```

The mismatched family on the same construction: `tau = 1/8 <=> beta = 24`
with per-direction moment `1/4`; `tau = 3 <=> beta = 1` with moment `6`.
The coincidence holds at the unit-variance setting and fails everywhere
else.

**Coverage verdict (scale-reference primitive).** The rate is
dimensionless. The approved scale-reference primitive declares, in its own
text, that it "carries zero dimensionless content: no mass ratio,
coupling, mixing angle, phase, selector, readout bridge, or empirical fit
is supplied by it." Therefore the primitive does **not** cover the rate:
`tau` is not a units conversion, and identifying `tau = 1/2` is not
discharged by the approved dimensionful reference. The rate is a genuine
dimensionless residual of the dynamics lane — a dial with `tau = 1/2` as
its distinguished setting (unit variance per record step; the point where
the `g_bare` chain's coordinate, magnetic, and kernel normalizations
coincide), registered by the parent surface's declaration rather than
forced by the lane's premises.

## Proof

**R0.** Character coefficients `c_R(beta)` of the plane kernel are
computed by stable Weyl-alternant Haar integration (no divisions; grid
convergence at machine precision); the per-step generator
`eps_R = -log((c_R/d_R)/c_0)` satisfies
`beta * eps_R / (N_c C_2(R)) -> 1` with strictly decreasing deviation and
Richardson extrapolation hitting 1, on the fundamental and adjoint
blocks.

**R1.** (i) is the exponent identity `tau_1 C_2 + tau_2 C_2 =
(tau_1 + tau_2) C_2`, checked in exact rational arithmetic per
representation. (ii) the eigenphase-Gaussian member's width is calibrated
by bisection so its fundamental-block generator equals the Wilson
member's; the adjoint and sextet blocks of the `k`-step composition are
then compared at fixed accumulated rate `T = k tau_hat ~ 1/2` for
`tau_0 in {1/16, 1/32, 1/64}` (`k in {8, 16, 32}`): the cross-kernel
deviation `k |eps_W - eps_M|` shrinks strictly and falls below `10^-3`
at the finest step, and a single calibrated rate predicts both blocks'
composed values against `exp(-T C_2(R))`.

**R2.** For each `tau in {1/8, 1/2, 3}`: `0 < w_R <= 1` (positivity);
conjugate-representation scalar symmetry with
`C_2(fund) = C_2(antifund) = 4/3` exactly (class-function reality of the
covariant channel); `w_R(tau)^2 = w_R(2 tau)` (composition); per-direction
generator moment `2 tau` by quadrature (diffusive law). The pass pattern
is identical across the three rates. The drifted and metric-dilation
witnesses fail the named non-rate premises as stated.

**R3.** The Gaussian identity `<x^2> = 2 tau` per direction is exact for
the generator model; the group-level statement is verified on the
constructed Wilson member: `<sum theta_j^2> / (8 tau_eff) -> 1`
(Richardson), i.e. `8` directions at `2 tau` each. The equivalences in
the display are exact rational arithmetic given R0's map, and the
`g^2 = 2 tau` consistency line is the cited magnetic identity
`beta g_bare^2 = 2 N_c` evaluated on `beta = N_c / tau`.

## Boundary

This note does not claim:

- a derivation of `tau = 1/2`, of `beta = 2 N_c`, of `g_bare = 1`, or of
  the beta=6 bridge row's declared surface definition — the unit-variance
  point is located, not forced; forcing a dial value is overreach;
- existence of the per-step link dynamics — the retained record/semigroup
  boundary stands (Record alone supplies no continuous Markov dynamics);
  everything here is a classification over the named hypothesis class,
  whose own premises (covariant channel / step-measure Ad-invariance,
  i.i.d. composition, diffusive scaling) remain the open dynamical
  surface recorded by the form-half note;
- a derivation of the heat-kernel form itself in this note — the form
  half is the CLT-attractor row's content (conditional, prose-named
  above); this note's theorems are about the rate given the class;
- coverage of the rate by the scale-reference primitive — the opposite is
  proved from the primitive's own quoted text;
- Wilson plaquette action-surface selection from framework axioms;
- a continuum Hamiltonian, spectral gap, or continuum-limit existence;
- a continuum running-coupling value or phenomenological coupling;
- an audit verdict or any effective-status promotion.

Step-counter remark: the per-step rate is stated relative to the
axiom-level record counter (records are countable; the readout `I` is
additive). Coarse-graining `k` micro-steps into one macro-step multiplies
the rate by the integer `k`; no continuum step limit is claimed or
needed.

The forward surface this opens: with the form conditional on the named
dynamical premise and the rate now isolated as the single dimensionless
residual, a native derivation of the per-step update — supplying both the
premise and the rate from admissibility/record constraints — is the
remaining derivation surface of this program; it is outside this row.

## Falsifiers

The packet would fail if any of the following were true:

- the supplied Wilson member's constructed rate deviated from
  `tau_eff = N_c / beta` (R0);
- composition failed to add rates exactly, or the cross-kernel collapse
  failed (deviations not shrinking, or a single calibrated rate failing
  to predict the other blocks) — the rate would then not be the complete
  surviving invariant (R1);
- some structural premise of the class selected a rate (pass patterns
  differing across `tau`), or a contrast witness failed to break its
  named premise (R2);
- the per-direction moment law `2 tau` failed on the constructed member,
  or the exact equivalences at `tau = 1/2` failed (R3);
- the scale-reference primitive's text did not carry the quoted
  zero-dimensionless-content declaration (coverage verdict).

The runner checks these as source-boundary and construction checks rather
than audit verdicts.

## Verification

Run:

```text
python3 scripts/gauge_link_per_record_step_rate_dial_unit_variance_point_2026_07_02.py
```

Expected:

```text
TOTAL: PASS=74 FAIL=0
```

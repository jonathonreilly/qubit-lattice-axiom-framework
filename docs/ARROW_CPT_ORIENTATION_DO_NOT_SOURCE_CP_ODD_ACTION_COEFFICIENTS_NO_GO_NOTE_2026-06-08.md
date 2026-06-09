# Arrow, CPT, Orientation, and Real Readout Do Not Source CP-Odd Action Coefficients

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** scoped route no-go / bounded obstruction
**Claim type:** no_go
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/arrow_cpt_orientation_cp_source_no_go_2026_06_08.py`](../scripts/arrow_cpt_orientation_cp_source_no_go_2026_06_08.py)
(exact numpy/sympy, PASS=6).
**Runner cache:**
[`logs/runner-cache/arrow_cpt_orientation_cp_source_no_go_2026_06_08.txt`](../logs/runner-cache/arrow_cpt_orientation_cp_source_no_go_2026_06_08.txt)

## Result

The tested routes from the axiom baseline to a CP-odd action coefficient fail:

1. Record formation gives an arrow only through boundary data, not through a
   CP/T-odd dynamical term.
2. CPT reality protects determinants into real phases; it does not supply a
   continuous CP-odd coefficient.
3. The available orientation/chirality object is a sign-only `Z_2` datum, not a
   continuous coefficient selector.
4. Real additive readout is CP-blind as a consumer, but it does not forbid a
   real CP-odd scalar such as the Jarlskog invariant.
5. Hermiticity, locality, gauge invariance, and the tested gauge-invariant-local
   action form-class leave the sampled `(r, delta, theta)` coefficients free.

This is a local no-go against those route families. It is **not** a global proof
that no richer framework-native dynamics, minimality theorem, finite-`k`
stress-response construction, or future retained action-selection theorem can
derive the coefficients.

## Scope

The useful synthesis is that three live coefficient targets have the same shape:
they are coefficients of admissible action terms, not new axioms and not outputs
of Record by itself.

- `r = |b|^2/a^2` is not selected by the tested static symmetry/readout routes.
- `delta` is a physical CP-odd phase, not forbidden by real readout, and is not
  selected by CPT reality alone.
- `theta_gauge` is not forced to zero by positivity, realness, CPT, or
  single-plaquette minimality unless an additional minimality premise is
  supplied.

The broader action-form authority remains a separate row, currently not a
retained premise in the live ledger:
[`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md).
This note does not promote that row and does not use it as retained authority.

## No-Go Discipline Gate

**Status:** PASS for the scoped route no-go only.

- **N1 — Alternative routes.** Five routes were separated and tested or left
  open: Record arrow as T-violation (closed by the time-symmetric generator and
  boundary-state reversal); CPT as CP source (closed by determinant reality);
  orientation/chirality as a coefficient source (closed to a sign-only `Z_2`
  datum); real readout as a CP prohibition (closed by the real CP-odd Jarlskog
  scalar); and form-class symmetry constraints fixing `(r, delta, theta)`
  (closed only for the tested Hermitian/C3/gauge-invariant-local checks; richer
  dynamics remain open).
- **N2 — Wall independence.** The closed routes are independent failures, but
  the open routes are not counted as closed walls. A future dynamics/minimality
  theorem could bypass this note without contradicting it.
- **N3 — Hidden-wall scan.** No "retained" status is assumed for the
  action-form row, the CPT stretch row, or the strong-CP theta rows. They are
  cited as context unless explicitly named as already retained by the ledger.
- **N4 — Residual matching.** The residual matched here is route-specific:
  arrow/CPT/orientation/readout do not source a CP-odd coefficient. It is not
  the stronger residual "no possible axiom-native CP source exists."
- **N5 — Rhetoric audit.** "Do not source" means "do not source through the
  tested route." It does not mean no finite-`k`, non-ultralocal, minimality, or
  future action-selection route can succeed.
- **N6 — Partial-closure path scan.** A retained action-selection theorem,
  retained minimality theorem, or explicit owner-approved Tier-A retirement
  could close one of the coefficient targets without adding a new axiom.
- **N7 — Steelman.** The strongest objection is that CP coefficients might be
  selected by a later dynamics principle, anomaly matching condition, measure
  selection rule, or finite-`k` stress response not represented in this runner.
  This note accepts that objection as outside scope.
- **N8 — Cross-cycle echo.** Prior route blockers in the strong-CP and Koide
  lanes have been over-read as global no-go claims. This note keeps the
  conclusion at the route level and preserves the coefficient-selection problem
  as live research.

## Runner Checks

The companion runner reproves:

- record-write microdynamics is time-symmetric for the tested write generator;
- the arrow direction is set by the initial state, not by a CP/T-odd map;
- CPT-real sample matrices have real determinants rather than a continuous
  CP-odd determinant phase;
- Hermitian/C3-covariant matter matrices and gauge-invariant Wilson-loop terms
  leave the sampled coefficients free;
- the orientation object is sign-only; and
- real readout is even in the CP phase while the Jarlskog scalar is a real
  CP-odd scalar, so CP is not forbidden by real readout.

## Dependencies And Context

Load-bearing:

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — baseline
  Lattice, Quantum, and Record semantics; Record supplies no coupling,
  weighting, probability, dynamics, source/action, or arbitrary observable
  identification.
- [`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
  — retained-bounded arrow-as-boundary context; the runner also reproves the
  local time-symmetry check used here.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  — human-readable Tier-A target registry.

Context only, not promoted here:

- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
- [`AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md`](AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md)
- [`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)
- [`STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md`](STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md)
- [`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md)
- [`KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md`](KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md)

## Forbidden-Imports Check

No PDG, fitted, or literature numerical comparator is consumed. The runner uses
finite matrix checks and symbolic identities only. `theta = 0`, `delta`, and
`r = 1/2` are named as coefficient targets, not as derivation inputs.

**Independent audit required.** This note asserts no effective-status change.

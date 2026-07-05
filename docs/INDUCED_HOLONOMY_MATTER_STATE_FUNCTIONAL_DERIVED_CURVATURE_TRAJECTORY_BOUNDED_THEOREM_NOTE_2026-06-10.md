# Induced Holonomy: the Composite Link's Loops Are a Derived, Gauge-Covariant Functional of the Matter State — Central on the Sea, Non-Central Off It, with a Tangential Departure from Flat under the Derived Flow

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** the holonomy demand is addressed conditionally at the
kinematic/state-functional level; the physical identification gate remains open.
**Script:** `scripts/frontier_induced_holonomy_matter_state_functional_derived_curvature_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_induced_holonomy_matter_state_functional_derived_curvature_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=12 FAIL=0`, exact, no MC.

## The wall, and what this note actually shows

The local-frame orbit note
[`LOCAL_FRAME_ORBIT_FLAT_SECTOR_EXACT_CONVERSE_HOLONOMY_FRAME_UNREACHABLE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-06-10.md`](LOCAL_FRAME_ORBIT_FLAT_SECTOR_EXACT_CONVERSE_HOLONOMY_FRAME_UNREACHABLE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-06-10.md)
shows that frame fields supply only the flat sector on its tested surface — holonomy
classes are frame-unreachable — so the holonomy demand sharpened to *"whatever supplies
gauge dynamics must supply holonomy classes."* This note shows that the framework has a
candidate holonomy supplier — not a frame, not an imported link field: the **composite
link** from
[`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md),
`U_eff = polar(M(x,y))`. Its loops are a **derived, gauge-covariant functional of the
matter state**. Calibrated precisely: *the matter sector supplies gauge-covariant link
coordinates whose loops are generically non-central* — the
demand is **addressed conditionally at the kinematic/state-functional level**, with the
dynamics **slaved** and the physical **identification gate open**.

**The curvature functional.** The composite link's determinant carries a U(1) phase (the
color-link source note's center structure) — sea-orbit states induce *central* holonomy `e^{iθ}I`. The
SU(3)-curvature scalar used throughout is `C = 1 − |tr Hol|/3 ∈ [0,1]`: exactly zero iff
the holonomy is central, invariant under conjugation *and* the center. **The U(1)/det
holonomy that `C` quotients is itself a derived covariant state functional — a named open
thread (candidate U(1) datum), not a silent quotient. The state-conditioning here is the registered [`realized_state_primitive`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) interface: pointwise evaluation at the supplied law-admissible realized state, nothing more; the state-contingent data quoted remain registered data per its counterfactual clause.**

## The results (exact — runner `PASS=12 FAIL=0`)

**(H1) The two poles, with filling-resolved genericity.** The closed-shell sea induces
`scalar·I₃` cross-blocks — links `= I`, `C = 0`: **the sea induces the flat sector**
(the runner recomputes this finite-surface fact; it is consistent with the closed-shell
and local-frame notes). Sea-*orbit* states induce central holonomy — `C = 0` exactly.
Off-sea states have **`C > 0` strictly** (the load-bearing fact), with **filling-dependent
magnitude**: near-half-filling (`K=4,5`) gives mean `C ≈ 0.7`; minimal occupancy (`K=3`)
gives mean `C ≈ 0.2` — all decimals seed/filling-specific magnitudes, not constants.
**Near-sea qualifier:** a same-color particle-hole excitation stays
color-diagonal — `C = 0` *exactly*; low color-mixing excitations lift `C` only weakly.
"Generic" must not be read as "typical near-sea."

**(H2) Covariance** *(corollary of the color-link and block-01 covariant laws, cited)*
**and the new invariant scalar.** `Hol → g₀ Hol g₀†` exactly under local rotations of the state;
`C` is exactly invariant — the conjugation+center-invariant curvature scalar is the new
object here (it appears on no landed runner).

**(H3) The derived dynamics — motion (corollary) and creation from flat (new,
recalibrated).** Along the exact derived flow: off-sea `C(t)` moves *(the block-01
induced trajectory at curvature level — corollary, cited)*. **Creation:** from flat
non-stationary data (a sea-orbit state, `C(0) = 0` exactly), the flow **leaves the flat
stratum tangentially** — quartic liftoff (Richardson order `≈ 4.0`, verified), numerically
small at small `t`, reaching `O(0.1)` only at `t = O(1)`; an **almost-periodic excursion,
not relaxation**. The stationary sea stays exactly flat — the vacuum does **not**
spontaneously curve. Rank-3 well-definedness verified along all sampled trajectories.

**(H4) Slaving** *(block-01's non-autonomy at holonomy level — corollary, cited; with
valid physical states)*. Two **valid one-body densities** (eigenvalues in `[0,1]`
asserted in-runner; equal particle number) with the *same* induced link field have **different**
`dHol/dt`: the holonomy trajectory is slaved to the matter flow. **No autonomous holonomy
law is claimed.**

## Mandatory reconciliations (objects distinguished)

- **[`COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_REQUIRES_BACKGROUND_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md`](COLOR_EINSELECTION_MATTER_UNITARY_PRIMITIVITY_REQUIRES_BACKGROUND_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md)
  (unaudited sibling note; reconciliation only):** its object is the single-hop color **transporter** of the flow —
  color-inert for the color-diagonal hopping (verified in-runner: the propagator's
  cross-site block is `scalar·I₃`). This note's object is the **unitarized cross-site
  state bilinear** — a different functional of a different argument, on the same flow.
  No contradiction — and that note's own steelman **explicitly leaves this route open**
  (*"multi-step matter dynamics might generate an effective primitive U without a fixed
  background link"*). This note walks through exactly that door.
- **[`NATIVE_HOLONOMY_PLAQUETTE_CENTER_FLUX_NO_GO_NOTE_2026-05-23`](NATIVE_HOLONOMY_PLAQUETTE_CENTER_FLUX_NO_GO_NOTE_2026-05-23.md)
  (retained_no_go):** the native plaquette of the **hop operators** is exactly scalar —
  the operator loop, not the state-bilinear loop. Different object; no contradiction.
- **The campaign pack's block-12 probe** ("inherited, not induced") was scoped to links
  fed into the Hamiltonian plus sea-like states — on which this note agrees.
  Pack-internal synthesis; no landed claim is contradicted.

## What is addressed, and what remains

- **Addressed, conditionally:** the holonomy demand, at the kinematic/
  state-functional level — the framework supplies a holonomy field as a derived state
  functional with an induced (slaved) trajectory; zero new inputs (no imported link
  field, no frame choice, no edge DOF — the QUANTUM axiom respected; the link is derived
  data, campaign block 03).
- **The state-realization convergence (observation, state-side):** *which* holonomy is
  realized = *which* matter state is realized — the open-shell invariant-locus clause.
  Neutrality's locus
  question and the curvature content are functionals of the same realized-state clause.
- **Not yet well-posed:** heat-kernel vs Wilson discrimination on the
  induced trajectory — `C(t)` from the fixed finite Hamiltonian is **almost-periodic**
  (two Bohr frequencies; no relaxation, no stationary measure). The discrimination still
  gates on the undelivered **R1** (autonomous generator) and **R2** (mixing/ergodicity)
  residuals of the same-wall note. `C(t)` is a derived computable observable; the action
  question is *not* claimed solved or newly well-posed.
- **Named and open:** the identification gate (whether the *physical* gauge field is the
  induced object — realization lane, `MR_color` family); the U(1)/det holonomy thread;
  the registrability route for `C` (an invariant-class functional of matter bilinears;
  its estimator theory is not developed here).
- No new axiom, primitive, measure, or weight; `r` untouched; no closing language —
  every open item above is a frontier, not a lock. The audit lane grades.

## Cross-references

- The composite link, its preconditions, and the center structure:
  [`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md).
- The direct precedent whose results H2/H3a/H4 restate at holonomy level:
  [`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  (campaign block 01, on main).
- The one-body closure / link-coordinate context:
  [`SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](SLOW_VARIABLES_DERIVED_ONE_BODY_CLOSURE_LINK_IS_A_COORDINATE_BOUNDED_THEOREM_NOTE_2026-06-09.md).
- The orbit-converse (frames supply only flat):
  [`LOCAL_FRAME_ORBIT_FLAT_SECTOR_EXACT_CONVERSE_HOLONOMY_FRAME_UNREACHABLE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-06-10.md`](LOCAL_FRAME_ORBIT_FLAT_SECTOR_EXACT_CONVERSE_HOLONOMY_FRAME_UNREACHABLE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- The state-realization/locus clause:
  [`OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md`](OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md). The sea's neutrality/flatness pole:
  [`PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`](PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10.md).
- Standard math (method only): polar decomposition; holonomy and conjugacy classes;
  center of SU(N); one-body reduced densities; Richardson extrapolation.

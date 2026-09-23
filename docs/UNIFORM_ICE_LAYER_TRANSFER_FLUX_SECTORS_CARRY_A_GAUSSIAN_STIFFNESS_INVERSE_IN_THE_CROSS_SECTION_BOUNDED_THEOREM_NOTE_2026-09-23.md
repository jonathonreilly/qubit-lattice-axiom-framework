---
claim_id: uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For periodic cross-sections2x2,2x4,2x6 (areas4,8,12), exact integer transfer enumeration conserves |S| and yields compatible torus counts along different axes:9600,23063296,70121226240. Numerical symmetric eigensolvers estimate each sector radius lambda_S and give zero flux the largest radius.  For every nonzero sector of these three sections, f(S)=-log(lambda_S/lambda_0) gives0.28<f(S)A/S^2<0.41. At |S|=2 the values are approximately0.2808,0.3073,0.3121; the last increment is less than a quarter of the preceding increment. Within each section the coefficient increases with |S| within the stated tolerance. These are finite numerical inequalities and a descriptive approximate quadratic pattern. Three thin cross-sections do not establish convergence to a limiting coefficient, a Gaussian continuum law, inverse-area asymptotics, or a Coulomb phase. Counts use exact integers; logarithms and eigenvalues use floating point. The supplied transfer model and fixed transverse geometries delimit the result."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_2026_09_23.py
---

# Finite flux-sector free energies on three thin cross-sections

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For periodic cross-sections 2x 2, 2x 4, 2x 6 (areas 4, 8, 12), exact integer transfer enumeration conserves |S| and yields compatible torus counts along different axes: 9600, 23063296, 70121226240. Numerical symmetric eigensolvers estimate each sector radius lambda_S and give zero flux the largest radius.

For every nonzero sector of these three sections, f(S)=-log(lambda_S/lambda_0) gives 0.28<f(S)A/S^2<0.41. At |S|=2 the values are approximately 0.2808, 0.3073, 0.3121; the last increment is less than a quarter of the preceding increment. Within each section the coefficient increases with |S| within the stated tolerance. These are finite numerical inequalities and a descriptive approximate quadratic pattern.

## Boundaries and non-claims

Three thin cross-sections do not establish convergence to a limiting coefficient, a Gaussian continuum law, inverse-area asymptotics, or a Coulomb phase. Counts use exact integers; logarithms and eigenvalues use floating point. The supplied transfer model and fixed transverse geometries delimit the result.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional finite ice measures, formation and supplied transfer models"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Preserve finite hypotheses and test extensions separately"
conditional_surface_status: "The declared model, order, records and numerical tolerances only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional mathematics and bounded computation; no retained grade asserted"
```

## Premises and declared objects

- **Measure and units.** The uniform ice measure, and the layer units and
  transfer matrix of open PR 8740.
- **Cross-sections.** The tori 2 × 2, 2 × 4 and 2 × 6, with areas 4, 8
  and 12.
- **Counts.** In-plane configurations are counted by their degree
  vectors, exactly, in chunks.
- **Flux.** S(v) = Σ (−1)^(x+y) (2 v − 1) over the cross-section.


## Finite numerical certificate — Flux free energies

The runner computes λ_S for every sector of the three cross-sections,
and reports f(S) A / S² for each. The two bounds and the increasing three-value sequence at the smallest flux are the checked statements. Approximate quadratic dependence is descriptive; these computations
do not prove a Gaussian law or a limiting c.


## No-go discipline and falsifiers

Negative claims concern only the stated fixed models and completed searches.
Alternative records, hidden state, adaptive orders, larger units, different
rules and different boundary conditions require separate tests. Caps must
not bind for an exhaustive verdict. Finite spectral patterns do not prove
infinite-cross-section physics. A counterexample under the exact hypotheses,
a failed independent count, or a failed stated control falsifies its result.
No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion result from PR #8740](UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md)

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_2026_09_23.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_2026_09_23.txt`.
Analytic statements require the proofs above in addition to finite checks.

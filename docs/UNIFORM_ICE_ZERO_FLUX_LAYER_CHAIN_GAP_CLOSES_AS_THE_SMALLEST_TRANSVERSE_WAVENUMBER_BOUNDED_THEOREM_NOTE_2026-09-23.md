---
claim_id: uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "For the declared transfer matrices on2xb with b=2,4,6,8,10 and on4x4, estimate D=log(lambda_0/|lambda_1|) within the zero-flux sector. The small controls recover lambda_0=32+2sqrt(209), next modulus14 on2x2, and next modulus668.3638 on2x4.  The computed next levels are negative with numerical multiplicity two on the strips and four on4x4. The solver requests levels beyond that cluster and checks a separated lower-modulus level, eigenpair residuals and orthogonality. Strip values D b are approximately2.9408,5.1158,5.7060,5.9434,6.0608; they increase and stay below2pi on this finite list. The estimated gaps on4x4 and2x4 are1.29627 and1.27895, differing by less than2%. This does not prove D~1/b, convergence to2pi, or a universal smallest-wavenumber law. Only the listed finite cross-sections and supplied uniform-ice transfer model are studied. Large spectra are numerical eigensolver estimates, with residual controls rather than an exact completeness proof. Negative eigenvalues imply alternating contributions only for observables overlapping those modes. No large-cross-section limit, physical phase, axiom selection or retained audit grade is established."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.py
---

# Finite zero-flux transfer spectra and layer-memory gap estimates

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

For the declared transfer matrices on 2xb with b=2, 4, 6, 8, 10 and on 4x 4, estimate D=log(lambda_0/|lambda_1|) within the zero-flux sector. The small controls recover lambda_0=32+2 sqrt(209), next modulus 14 on 2x 2, and next modulus 668.3638 on 2x 4.

The computed next levels are negative with numerical multiplicity two on the strips and four on 4x 4. The solver requests levels beyond that cluster and checks a separated lower-modulus level, eigenpair residuals and orthogonality. Strip values D b are approximately 2.9408, 5.1158, 5.7060, 5.9434, 6.0608; they increase and stay below 2 pi on this finite list. The estimated gaps on 4x 4 and 2x 4 are 1.29627 and 1.27895, differing by less than 2%. This does not prove D~1/b, convergence to 2 pi, or a universal smallest-wavenumber law.

## Boundaries and non-claims

Only the listed finite cross-sections and supplied uniform-ice transfer model are studied. Large spectra are numerical eigensolver estimates, with residual controls rather than an exact completeness proof. Negative eigenvalues imply alternating contributions only for observables overlapping those modes. No large-cross-section limit, physical phase, axiom selection or retained audit grade is established.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Finite spectral estimates in a supplied ice transfer model"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Separate finite estimates from asymptotic conjectures"
conditional_surface_status: "Listed periodic geometries and numerical tolerances only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Exact tensor factorization with finite numerical spectral checks"
```

## Premises and declared objects

Each vertex has six binary link occupations with sum three. The transverse
periodic geometries have even sides and staggered vertical flux
S=sum((-1)^(x+y)(2 v-1)), whose sign flips across a layer. T[v,w] counts
in-plane completions between vertical words v and w. Counts are symmetric
under v,w exchange. The row tensor enumerates horizontal bits exactly;
contractions and eigensolvers use floating point.

## Transfer-to-chain relation

For a positive Perron eigenvector phi of a symmetric primitive zero block,
P(v,w)=T(v,w)phi(w)/(lambda_0 phi(v)) is similar to T/lambda_0.
Its nonstationary eigenvalues are lambda_j/lambda_0. Thus the asymptotic
rate of a mode with nonzero observable overlap is log(lambda_0/|lambda_j|).
A negative eigenvalue alternates that mode's sign; it does not imply that
every occupation correlation has that sign or is dominated by that mode.
The quoted second-level identification on larger blocks remains numerical.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion PR #8740](UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [Companion PR #8859](UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original PR retains author history. No historical mutation report is
used as current review evidence. A failed count, symmetry/residual control
or numerical inequality falsifies the corresponding finite certificate.
Untested spectra and limits remain open.

## Verification

```bash
python3 scripts/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.py
```

Fresh evidence: `logs/runner-cache/uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_2026_09_23.txt`.

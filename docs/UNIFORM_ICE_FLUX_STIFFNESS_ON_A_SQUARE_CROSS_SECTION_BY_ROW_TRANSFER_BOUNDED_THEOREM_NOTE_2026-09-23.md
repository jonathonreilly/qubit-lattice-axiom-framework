---
claim_id: uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The row tensor counts horizontal occupations with three occupied links at each vertex. Contracting these tensors around the periodic transverse direction applies the layer transfer without constructing the full matrix. Cross-checks recover trace(T^2)=9600 on2x2 and the previously computed leading zero/nonzero flux eigenvalues on2x2,2x4,2x6.  Numerical leading radii on4x4 decrease across |S|=0,2,4,6,8: approximately3244639.0,2989915.0,2332665.4,1526346.9,822834.3. The descriptive coefficient c(S)=(A/S^2)log(lambda_0/lambda_S) is approximately0.3270,0.3300,0.3352,0.3430; values through |S|=6 differ by less than3% from c(2). At equal area,2x8 has c(2)\u22480.3137, about4% below4x4. The tested2xb strips, b=2,4,6,8,10, give an increasing sequence ending near0.3145. These are finite numerical observations, not a Gaussian limit or asymptotic inverse-area law. Only the listed finite cross-sections and supplied uniform-ice transfer model are studied. Large spectra are numerical eigensolver estimates, with residual controls rather than an exact completeness proof. Negative eigenvalues imply alternating contributions only for observables overlapping those modes. No large-cross-section limit, physical phase, axiom selection or retained audit grade is established."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_layer_transfer_flux_sectors_carry_a_gaussian_stiffness_inverse_in_the_cross_section_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.py
---

# Finite flux-sector estimates from a row-wise ice transfer

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

The row tensor counts horizontal occupations with three occupied links at each vertex. Contracting these tensors around the periodic transverse direction applies the layer transfer without constructing the full matrix. Cross-checks recover trace(T^2)=9600 on 2x 2 and the previously computed leading zero/nonzero flux eigenvalues on 2x 2, 2x 4, 2x 6.

Numerical leading radii on 4x 4 decrease across |S|=0, 2, 4, 6, 8: approximately 3244639.0, 2989915.0, 2332665.4, 1526346.9, 822834.3. The descriptive coefficient c(S)=(A/S^2)log(lambda_0/lambda_S) is approximately 0.3270, 0.3300, 0.3352, 0.3430; values through |S|=6 differ by less than 3% from c(2). At equal area, 2x 8 has c(2)≈0.3137, about 4% below 4x 4. The tested 2xb strips, b=2, 4, 6, 8, 10, give an increasing sequence ending near 0.3145. These are finite numerical observations, not a Gaussian limit or asymptotic inverse-area law.

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

## Theorem — Row transfer

On a layer, a vertex has four in-plane links and two vertical ones, and the
ice rule asks for three occupied links. Order the vertices by rows. The
in-plane links split into horizontal links inside a row and links between
consecutive rows. For fixed links between rows, the horizontal links of
different rows are independent, so the count factorises into one row
tensor per row. It is summed over the between-row links, with the last row
wrapping to the first. The runner's contraction follows exactly this
factorisation, and the checks against the companion finite transfer enumeration confirm it.


## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion PR #8740](UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [Companion PR #8746](UNIFORM_ICE_LAYER_TRANSFER_FLUX_SECTORS_CARRY_A_GAUSSIAN_STIFFNESS_INVERSE_IN_THE_CROSS_SECTION_BOUNDED_THEOREM_NOTE_2026-09-23.md)

The original PR retains author history. No historical mutation report is
used as current review evidence. A failed count, symmetry/residual control
or numerical inequality falsifies the corresponding finite certificate.
Untested spectra and limits remain open.

## Verification

```bash
python3 scripts/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.py
```

Fresh evidence: `logs/runner-cache/uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_2026_09_23.txt`.

---
claim_id: uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "An exact positive-eigenvector Markov transform, finite fits to a Gaussian layer functional and finite FFT comparisons for the supplied kernel."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
  - uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_2026_09_23.py
---

# Positive transfer laws and finite Gaussian-functional fits

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Exact conditional transfer law

Let T be a finite real symmetric nonnegative transfer on a support component with positive eigenvector psi and eigenvalue lambda>0. Normalize sum psi²=1. Then
P(v'|v)=T(v',v)psi(v')/[lambda psi(v)]
is stochastic, by the eigenvector equation, and satisfies detailed balance with psi². Component choice and positivity are hypotheses; neither follows from a generic numerical fit.

The ice transfer counts hidden horizontal assignments and can be represented by local tensors. Summing those hidden variables can induce nonlocal dependence on boundary layers, so not all nonlocality can be assigned to psi alone.

For a separately supplied zero-flux Gaussian layer field with covariance S_q=sqrt(Q/(Q+4))/K, its density is proportional to exp[-G/2], where G=sum_(q!=0)|E_q|²/(A S_q). Its positive square-root amplitude therefore has log psi=constant-G/4. This is a Gaussian-model identity.

## Finite numerical fits

On 2 by 4, 2 by 6, 2 by 8 and 4 by 4, the runner fits log psi versus G using the computed psi² measure. Both a measured covariance kernel and a comparison kernel using K=2c(2) are reported. High weighted R² and slopes near -1/4 describe an approximation; they do not make the discrete ice measure exactly Gaussian.

The runner compares transition columns at min(200, zero-flux support size) distinct layers drawn with fixed-seed weights psi². The comparison column is T(v',v)exp[-G(v')/4], normalized separately at each initial layer. Its recorded maximal total variation is only over those sampled columns. Original reproduction thresholds are 1.3% over the tested shapes and 0.25% on 4 by 4; no all-state bound is inferred.

For the supplied Gaussian comparison kernel, K sqrt((Q+4)/Q) has small-q behavior 2K/|q|. The runner also compares six differences of its 2048 by 2048 discrete transform with a K/(pi r) reference. These finite FFT checks do not establish a tail for the exact ice law or an infinite-cross-section formation law.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** only the stated finite sections, boundary conditions, support sectors and exact conditional arguments are retained.
- **N2 — Independence:** independent review controls check structural identities; reproduction of a previous numerical value is a consistency check.
- **N3 — Imports:** model assumptions, Gaussian comparisons and numerical algorithms are explicit. No new framework axiom or primitive is adopted.
- **N4 — Dependencies:** linked notes supply definitions only within their corrected scope.
- **N5 — Resolution:** exact structural statements rely on the proofs above. Finite floating-point spectra and seeded Monte Carlo outputs are computational observations, not certified spectral enclosures or limit theorems. Binned errors are descriptive estimates; no mixing bound, simultaneous confidence coverage or thermodynamic extrapolation is asserted.
- **N6 — Remaining work:** larger systems and sharper analytic results remain open; a finite discrepancy is retained rather than fitted away.
- **N7 — Strongest objection:** an approximation to one observable does not establish an exact probability law, a particle interpretation or every higher correlation.
- **N8 — Review boundary:** this landing narrows original claims and corrects evidence handling. No audit verdict, retained grade or assembly decision is applied.

## Falsifiers

A counterexample under the exact hypotheses refutes the corresponding mathematical statement. A failed fresh run challenges the stated numerical reproduction, and must be investigated; it does not alone establish a different infinite-volume theory.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; does not derive the supplied ice model.
- [uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23](UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- [uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23](UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- [uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_bounded_theorem_note_2026-09-23](UNIFORM_ICE_UNIT_LINK_FIELD_FIXES_ONE_STIFFNESS_FOR_THE_FLUX_COST_AND_THE_FIELD_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8896, head `281e2ca9f6f987ae2df5424566aa3e4435129d57`, branch `claude/ice-layer-vacuum-gaussian-functional-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

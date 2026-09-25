---
claim_id: ring_model_ice_transverse_weight_sum_rule_the_ring_term_moves_the_weight_from_the_smallest_momenta_to_the_zone_corner_without_a_growing_peak_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Exact Parseval constraint and finite transverse-weight maps. Supplied
  finite-model identities and explicitly biased finite numerical diagnostics only;
  no phase, convergence certificate or new framework premise.
upstream_dependencies:
- ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/ring_model_transverse_weight_sum_rule_and_where_the_ring_term_moves_the_weight_2026_09_24.py
---

# Exact Parseval constraint and finite transverse-weight maps

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

For sigma_a(x)=±1 on N=L³ sites and O_a(k)=N^(-1/2)sum_x exp(-ikx)sigma_a(x), discrete Parseval gives sum_k T(k)=3N with T=sum_a|O_a|², configuration by configuration. The Gauss law gives sum_a(1-exp(-ik_a))O_a(k)=0. At nonzero momentum this removes one complex direction. At k=0 the constraint vector vanishes: there are three harmonic components, not two transverse components.

Consequently the average T over nonzero momenta is (3N-T(0))/(N-1). In the zero-winding sector T(0)=0, so this average is 3N/(N-1), and dividing that average by two gives 3N/[2(N-1)]. The full-zone mean T=3 does not force each star or the low-momentum value to equal 3, nor a universal per-polarization 1.5 including k=0. Constant polarized ice is an immediate nonzero-harmonic counterexample.

The runner checks the identities on configurations and reports cubic-star averages from uniform-loop samples and finite guided forward-walking runs. These are different sector distributions: the uniform samples are not constrained to the guided runs' zero-winding sector. A uniform RK vector in one flip class is not necessarily uniform on the full sector.

The displayed finite map redistributes weight broadly between selected small momenta and the corner. It is not monotone in momentum magnitude: even the original 4³ table's (1,1,1) and (2,0,0) ratios contradict that reading. Two tori and no observed growing peak do not prove short-range behavior, absence of order or a thermodynamic limit. Ten-bin errors and nominal two-error comparisons are descriptive and do not include all reference uncertainty. Older B4 numbers are historical arithmetic inputs, not newly reproduced independent results.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied finite models, supports, boundaries and estimator settings above.
- **N2 — Independence:** primary reproduction is not independent verification; the combined review receipt records separate structural controls.
- **N3 — Imports:** link qubits, Gauss law, ring Hamiltonian, initial ensembles, projection and Gaussian comparators are supplied, not adopted framework premises.
- **N4 — Dependencies:** corrected parent scopes govern; filenames are historical identifiers, not stronger claims.
- **N5 — Resolution:** floating-point eigensystems and finite Monte Carlo are observations, not certified enclosures or limit theorems. Bin errors lack proved coverage or mixing bounds.
- **N6 — Deferred:** component connectivity, population/lag/projection convergence and infinite-volume physics require additional science.
- **N7 — Counterroutes:** alternative sectors, non-Gaussian states, finite-size effects and correlated estimator error remain available.
- **N8 — Boundary:** ordinary source review only; no audit verdict, retained grade or assembly decision.

## Falsifiers and verification

A counterexample satisfying the exact hypotheses refutes the corresponding identity. Failed numerical controls must be investigated and not relabelled as a new phase. The runner's numerical thresholds describe only its finite experiment. Successful fresh execution has exit zero and FAIL=0; its cache binds this source and its declared inputs.

## Inputs

- [RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9163, frozen head `87b3cbb14cb1c81e6fbb46455f8565e83f8e3596`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_transverse_weight_sum_rule_and_where_the_ring_term_moves_the_weight_2026_09_24.py
```

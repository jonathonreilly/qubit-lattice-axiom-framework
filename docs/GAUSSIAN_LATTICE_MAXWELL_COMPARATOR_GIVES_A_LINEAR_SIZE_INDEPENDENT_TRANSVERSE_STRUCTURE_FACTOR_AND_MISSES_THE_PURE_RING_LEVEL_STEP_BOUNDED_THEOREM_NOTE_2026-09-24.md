---
claim_id: gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Reduced Gaussian Maxwell comparator and historical fit arithmetic. Supplied
  finite-model identities and explicitly biased finite numerical diagnostics only;
  no phase, convergence certificate or new framework premise.
upstream_dependencies:
- ring_model_pure_ring_point_transverse_fluctuations_at_the_smallest_momentum_are_a_third_of_the_uniform_ice_constant_and_the_feynman_photon_bound_shows_no_resolved_power_on_small_tori_bounded_theorem_note_2026-09-24
- ring_model_ice_transverse_weight_sum_rule_the_ring_term_moves_the_weight_from_the_smallest_momenta_to_the_zone_corner_without_a_growing_peak_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/gaussian_lattice_maxwell_comparator_linear_structure_factor_misses_the_pure_ring_level_step_2026_09_24.py
---

# Reduced Gaussian Maxwell comparator and historical fit arithmetic

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

Supply positive U,K and the noncompact quadratic Hamiltonian H=(U/2)E²+(K/2)A^T C^T C A, with canonical commutators and Gauss constraint D E=0. Quotient longitudinal gauge directions and remove the harmonic zero modes. On the remaining nonzero transverse oscillator space, C^T C has eigenvalues |s(k)|² twice, |s|²=sum_a(2-2cos k_a). Each oscillator has frequency sqrt(UK)|s| and electric covariance sqrt(K/U)|s|/2. Thus the tensor covariance is A0|s|(I-gg†), A0=sqrt(K/U)/2 and g_a=(1-exp(-ik_a))/|s(k)| for k≠0, using the runner's positive-exponent Fourier convention. This is a normalizable reduced oscillator ground state, not a normalizable zero-momentum eigenstate of the full noncompact free-particle Hilbert space.

For fixed U,K the same allowed k has the same covariance on different tori. The lattice norm |s| retains lattice anisotropy. A size-dependent fitted coupling changes this comparison. In the zero-harmonic sector S(0)=0 by construction. The ground-state averaged ring f-sum from the corrected parent matches this Gaussian f-sum if K=4u (g=1); this is a supplied matching rule, not a native coupling determination.

If the ansatz T(k)=2(c+A0|s|) is imposed at **every nonzero** k, T(0)=0, c≥0, and the spin sum rule is also imposed, then 2c(N-1)/N+2A0*m_L=3, m_L=N^(-1)sum_(k≠0)|s|. It follows A0≤3/(2m_L). With K=4u this implies U≥u*(2m_L/3)². The bound applies only to this all-zone ansatz; fitting a few momenta does not verify its hypotheses. c>0 gives a constant low-k structure factor, not a linear photon comparator.

The runner verifies finite matrices and sum identities, then evaluates fits of **stored historical numbers**. Their errors are supplied weights, not calibrated independent uncertainties. The reported chi-square values, slopes, nominal sigma separations, and next-size predictions are arithmetic descriptions of those inputs; they neither reject a physical Gaussian phase nor establish population convergence. Auxiliary inputs are not independently reproduced here. The continuous Gaussian unit-variance calibration 3N/(2N+1) is not an exact cubic-ice covariance law. Forward-lag exponential factors are illustrative spectral hypotheses, not bias bounds.

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
- [RING_MODEL_ICE_TRANSVERSE_WEIGHT_SUM_RULE_THE_RING_TERM_MOVES_THE_WEIGHT_FROM_THE_SMALLEST_MOMENTA_TO_THE_ZONE_CORNER_WITHOUT_A_GROWING_PEAK_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_ICE_TRANSVERSE_WEIGHT_SUM_RULE_THE_RING_TERM_MOVES_THE_WEIGHT_FROM_THE_SMALLEST_MOMENTA_TO_THE_ZONE_CORNER_WITHOUT_A_GROWING_PEAK_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9166, frozen head `d0baf9ff16c0beade7eee8d444ae12bb932083aa`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/gaussian_lattice_maxwell_comparator_linear_structure_factor_misses_the_pure_ring_level_step_2026_09_24.py
```

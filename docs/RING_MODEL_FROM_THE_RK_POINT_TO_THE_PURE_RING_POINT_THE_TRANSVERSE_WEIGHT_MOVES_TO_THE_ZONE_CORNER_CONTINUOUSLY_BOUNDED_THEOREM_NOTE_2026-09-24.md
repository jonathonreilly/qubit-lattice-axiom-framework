---
claim_id: ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_continuously_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: RK stationary law and a finite coupling-grid sweep. Supplied finite-model
  identities and explicitly biased finite numerical diagnostics only; no phase, convergence
  certificate or new framework premise.
upstream_dependencies:
- ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
- ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
- ring_model_ice_transverse_weight_sum_rule_the_ring_term_moves_the_weight_from_the_smallest_momenta_to_the_zone_corner_without_a_growing_peak_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_2026_09_24.py
---

# RK stationary law and a finite coupling-grid sweep

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

At V=g=1 the ring term on each active two-state pair is [[1,-1],[-1,1]], equal to **twice** the normalized antisymmetric projector. Thus the graph Hamiltonian is positive semidefinite and its kernel is constant on each connected flip class. With guide h=1 its local energy vanishes identically and the continuous-time symmetric flip walk has the uniform stationary law within each class. Frozen classes and arbitrary class mixtures remain possible.

The exact zero local energy and Parseval identities hold without equilibration. A finite run need not have reached that stationary law. A winding-preserving loop sample and a plaquette walk can weight distinct flip classes differently. The sum rule fixes a zone sum, not every star to 3. Passing the RK control does not certify finite-population projection at V<g.

The runner samples five V values on L=4 and three on L=6 with the stated guide, projection and lag. Its point estimates have an ordered small-axis and corner pattern on that grid. This is not a proof of continuous or monotone ground-state behavior between points, nor does it exclude a transition in the thermodynamic limit. Finite systems can have smooth observables across parameters even when their limit has a transition.

The quantity u=V*n_f-e uses a mixed energy and forward-walking flippability. The identity equals the ring expectation only in the appropriate converged ground-state limit; its finite estimator combines both errors. Error ratios and comparisons to previous runs are nominal bin-error diagnostics. A specific low-k change cannot be attributed solely to the missing k=0 weight from the total sum rule. No phase or method-wide accuracy is established.

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

- [RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_PROJECTOR_MONTE_CARLO_AT_THE_PURE_RING_POINT_ENERGIES_BELOW_VARIATIONAL_AND_NO_GROWTH_OF_PLAQUETTE_ORDER_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_WINDING_SECTOR_SPLITTINGS_RESOLVED_ON_THE_SMALL_TORI_AND_A_MULTI_EXPONENTIAL_RELAXATION_AT_THE_PURE_RING_POINT_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [RING_MODEL_ICE_TRANSVERSE_WEIGHT_SUM_RULE_THE_RING_TERM_MOVES_THE_WEIGHT_FROM_THE_SMALLEST_MOMENTA_TO_THE_ZONE_CORNER_WITHOUT_A_GROWING_PEAK_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_ICE_TRANSVERSE_WEIGHT_SUM_RULE_THE_RING_TERM_MOVES_THE_WEIGHT_FROM_THE_SMALLEST_MOMENTA_TO_THE_ZONE_CORNER_WITHOUT_A_GROWING_PEAK_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9169, frozen head `9fd0b011038e489f92dc80986ec47664d9107777`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_from_the_rk_point_to_the_pure_ring_point_the_transverse_weight_moves_to_the_zone_corner_2026_09_24.py
```

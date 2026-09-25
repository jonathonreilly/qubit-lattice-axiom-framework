---
claim_id: ring_model_winding_sector_splittings_resolved_on_the_small_tori_and_a_multi_exponential_relaxation_at_the_pure_ring_point_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conserved winding and finite projector relaxation diagnostics. Supplied
  finite-model identities and explicitly biased finite numerical diagnostics only;
  no phase, convergence certificate or new framework premise.
upstream_dependencies:
- ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/ring_model_winding_sector_splittings_and_imaginary_time_gap_at_the_pure_ring_point_2026_09_24.py
---

# Conserved winding and finite projector relaxation diagnostics

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

Sum the vertex Gauss law over a slab of a periodic cubic lattice. Internal links cancel pairwise, leaving equality of fluxes through its two section planes. A contractible plaquette flip crosses any section with canceling oriented changes, so every section flux W_a is conserved. The convention Phi_a=W_a/2 is a supplied normalization.

The implemented staggered zero-flux seed requires even L. Reversing the indicated straight x loops at y=1, z=0,...,q-1 gives W=(2q,0,0) for 0≤q≤L. This constructs those sectors only; it neither enumerates all sectors nor proves their flip connectivity. The runner now accumulates its seed and winding checks across every size rather than retaining only the last size's boolean.

The sector energies and relaxation slopes are finite-population mixed estimates on the stated tori and selected supports. A walker distribution initially uniform in configurations, used with guide h, corresponds to quantum amplitudes proportional to 1/h, not the uniform RK wavefunction. This distinction matters for the relaxation experiment.

The log fits use fixed time windows plus a data-dependent excess-energy threshold. They describe selected windows, not a proof of multiple spectral exponentials, a lowest gap, a phase, or an infinite-volume scaling law. Late-energy standard errors and ten-bin diagnostics do not control time correlation, population bias or fit selection. Stored earlier energy values are historical comparisons, not independent ground-state certificates. Two sizes and the reported flux ratios cannot distinguish a Coulomb phase from every ordered alternative.

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
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9153, frozen head `24b5a245688465b6f1f2f07141a448e0f5929081`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_winding_sector_splittings_and_imaginary_time_gap_at_the_pure_ring_point_2026_09_24.py
```

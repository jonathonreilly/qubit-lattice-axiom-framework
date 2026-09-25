---
claim_id: ring_model_projector_monte_carlo_at_the_pure_ring_point_energies_below_variational_and_no_growth_of_plaquette_order_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Finite-population projector diagnostics for the supplied ring model.
  Supplied finite-model identities and explicitly biased finite numerical diagnostics
  only; no phase, convergence certificate or new framework premise.
upstream_dependencies:
- ring_model_between_the_rokhsar_kivelson_and_pure_ring_points_small_torus_and_variational_diagnostics_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/ring_model_projector_monte_carlo_at_the_pure_ring_point_2026_09_24.py
---

# Finite-population projector diagnostics for the supplied ring model

**Type:** bounded_theorem
**Status:** conditional finite mathematics and numerical diagnostics; unaudited.

For a positive guide h(C)=exp(alpha*N_flip(C)), supply H=-A. The importance-transformed semigroup uses jump rates r(C→C')=A(C,C')h(C')/h(C), local energy E_L(C)=-sum r, and Feynman–Kac weight exp(-integral(E_L-E_ref)dt). This follows directly by separating the transformed generator into its jump part and multiplication part. The implementation samples continuous jump times inside fixed resampling blocks.

Exact imaginary-time projection, with suitable initial overlap and limits, selects the lowest state in the initial support. Fixed walker population, finite projection, finite guide equilibration and resampling introduce unresolved errors. The mixed energy estimate is not a variational bound: the small-component estimate can fall below its exact ground energy. Agreement with the finite exact control is a descriptive diagnostic, not a proof of convergence on larger tori.

The run reports energy, mixed diagonal observables and 2*mixed-variational extrapolations. The latter cancel a first-order trial-state error only under the usual small-error expansion; they are not exact pure estimators. Energy segment comparisons use the implemented unequal time windows; the plaquette comparisons use halves of the retained sample. Ten-bin uncertainties and agreement between segments do not certify stationarity or independent samples.

As in the variational parent, the per-configuration mean subtraction forces the q=0 plaquette statistic to zero. It is not an ensemble-connected q=0 susceptibility. The selected nonzero momenta on three tori do not establish absence of ordering. Historical auxiliary runs outside this runner are excluded from current quantitative evidence. Local plaquette evolution preserves winding and may preserve additional flip components.

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

- [RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_SMALL_TORUS_AND_VARIATIONAL_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-09-24](RING_MODEL_BETWEEN_THE_ROKHSAR_KIVELSON_AND_PURE_RING_POINTS_SMALL_TORUS_AND_VARIATIONAL_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): corrected conditional definitions and boundaries.
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md): corrected conditional definitions and boundaries.

## Review record

Original PR #9148, frozen head `08a8793df4867d7bef3230345261c58439c98742`. Original note and complete runner reviewed in one primary session without subagents. The original branch and frozen patch remain recovery handles for deferred work. Historical titles and claim identifiers remain stable; this body and scope govern. Fresh controls and same-session affected-fix confirmation are recorded in the combined landing receipt.

```bash
python3 scripts/ring_model_projector_monte_carlo_at_the_pure_ring_point_2026_09_24.py
```

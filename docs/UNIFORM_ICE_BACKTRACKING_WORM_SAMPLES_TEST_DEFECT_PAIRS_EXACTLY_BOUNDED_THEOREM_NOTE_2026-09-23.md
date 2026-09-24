---
claim_id: uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Exact balance of a supplied augmented backtracking chain and finite defect-count controls, with seeded displacement-histogram comparisons."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
  - uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_2026_09_23.py
---

# Backtracking-worm balance and finite defect histograms

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Augmented chain and stationary weights

On an even cubic torus, supply divergence-free unit arrows. The closed states are ice configurations. An open state has a labeled tail of divergence -2 and head of divergence +2. From a closed state choose a tail uniformly and one of its three outgoing edges, then reverse it. From an open state choose any of the head's four outgoing edges and reverse it; returning to the tail closes the worm.

An open-to-open move and its reverse each have probability 1/4. Each elementary creation channel has probability 1/(3N), and its inverse annihilation has probability 1/4. Thus assigning weight one to each closed state and 4/(3N) to each open state satisfies detailed balance, including multiplicities of parallel edges. Restricted to a communicating class this proves the corresponding stationary measure. Cycle reversals connect ice orientations; an open oriented path can be reversed to close, giving the usual finite reachable augmented space.

Consequently the stationary time histogram over every open step at displacement r is proportional to the number Z_pair(r) of charged configurations. The free-energy difference is -log[Z_pair(r)/Z_pair(r')]. A finite seeded histogram is an estimator of that quantity, not an exact sample of the probabilities. Normalizing each worm separately would change the weighting.

The nonbacktracking variant is retained as a finite L=2 comparison. An interior three-successor argument alone omits creation and closure boundary balance, so no general nonbacktracking occupation theorem is inferred here.

## Counts and comparisons

Exhaustive enumeration at L=2 gives 9600 ice configurations and 307968 configurations with exactly one divergence +2 and one -2, distributed over seven nonzero displacements. The runner checks these counts and compares two worm schedules with them.

For a separate Gaussian comparison with opposite charge magnitude two,
V_G(r)-V_G(r')=4K[G(r')-G(r)],
where G is the mean-zero torus inverse of the graph Laplacian. K_cont=(2N+1)/(3N) is the continuous Gaussian calibration, not an exact ice stiffness. The runner reports ten selected L=8 offsets and seven axial L=16 offsets, with bin jackknife diagnostics. Their finite agreement and offsets do not prove a three-dimensional asymptotic Coulomb law, a universal attraction statement or the cause of a contact correction. Test defects are probes, not admissible pure-ice records.

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
- [uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23](UNIFORM_ICE_ON_CUBIC_TORI_WINDING_STIFFNESS_AND_CORRELATIONS_CARRY_THE_SUM_RULE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- [uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_bounded_theorem_note_2026-09-23](UNIFORM_ICE_TEST_DEFECTS_INTERACT_THROUGH_THE_LATTICE_GREEN_FUNCTION_WITH_THE_FLUX_COST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8913, head `bfce588b8e5d94f4912c5e8030e07a8c09a51b0e`, branch `claude/ice-worm-samples-defect-pairs-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_backtracking_worm_samples_test_defect_pairs_exactly_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

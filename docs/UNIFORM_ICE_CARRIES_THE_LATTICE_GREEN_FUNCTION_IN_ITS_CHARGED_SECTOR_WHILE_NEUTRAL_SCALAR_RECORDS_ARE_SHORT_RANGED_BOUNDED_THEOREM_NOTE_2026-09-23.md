---
claim_id: uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "An exact one-vertex invariant lemma and L=2 alignment mean, with finite connected-correlation diagnostics for one specified neutral statistic."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_2026_09_23.py
---

# One-vertex scalar invariants and finite alignment correlations

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Exact local invariant and observable

The proper cubic rotations act transitively on the six outward directions of a vertex; so do all signed axis permutations. The average of either six-dimensional permutation representation is the all-ones matrix divided by six. Hence its invariant linear subspace is spanned by the sum of outward arrow components, which is divergence and vanishes in ice. Apart from constants, no nonzero invariant linear statistic of these six arrows remains. This lemma says nothing by itself about extended or nonlinear scalar observables.

Define f(r)=sum_i E_i(r)E_i(r-e_i), a signed alignment sum. The literal number of aligned axes is (f+3)/2. Exact enumeration at L=2 gives <f>=39/25.

## Finite connected-correlation experiment

The runner samples the specified f on L=16 with 500000 completed worms and forms the axis-averaged connected C(r)=<f(x)f(x+r)>-<f>². Uncertainty diagnostics must recompute both the subtracted mean and the correlation in each delete-bin sample; ratios must likewise recompute the denominator. Treating the raw second-moment error alone as an error for C omits covariance.

The numerical reference in this experiment is a different finite kernel: on a 128³ torus compute the mean-zero inverse G0, then use Gref(r)=G0(r)-G0(64,64,64). Ratios Gref(r)/Gref(1) therefore depend on this stated additive reference. The exact nearest-neighbor difference G0(0)-G0(e)=(1-1/N)/6 follows by evaluating the defining equation at zero and using cubic symmetry. The comparison is with that finite reference, not an equality of correlators on matching volumes.

The fresh output describes resolution of selected separations and bin-based error estimates. A few multiples of estimated errors are not certified confidence bounds, and an unresolved tail is not proved zero or exponentially decaying. The measurement concerns f only.

## Scope

Prior numerical defect-free energies and transverse covariance comparisons do not imply an exact Green-function two-point statistic for every charged observable. Two like charges alone also violate net neutrality on a closed torus unless compensation is supplied. No conclusion about all neutral scalars, quantum photons, gravity inputs or a general formation mechanism is retained.

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
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8918, head `25cbda1f1a9a91ffff5798fae46913ba68938949`, branch `claude/ice-green-function-only-in-charged-sector-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_carries_the_lattice_green_function_in_its_charged_sector_while_neutral_scalar_records_are_short_ranged_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

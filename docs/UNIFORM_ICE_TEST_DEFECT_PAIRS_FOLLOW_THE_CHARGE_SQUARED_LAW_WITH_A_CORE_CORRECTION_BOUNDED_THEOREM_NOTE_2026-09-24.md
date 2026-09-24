---
claim_id: uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Charge normalization and finite neutral-pair transfer calculations on a 4 by 4 prism, compared with a conditional charge-squared Gaussian prediction."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_bounded_theorem_note_2026-09-23
  - uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_2026_09_24.py
---

# Charge-two and charge-four defect comparisons on one prism

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Probe definitions and symmetries

Changing occupied degree from three to three+delta gives staggered charge 2delta(-1)^(x+y+z). Delta=+/-2 therefore has charge magnitude four. Defect pairs are neutral, with the second degree shift chosen using its relative sublattice parity. They are probes of an extended counting problem, not admissible pure-ice vertices.

Use the positive zero-flux eigenvector and insertion transfer ratios defined in the charge-two note. On a 4 by 4 transverse section, complement exchanges the two degree-shift signs without changing pair weights, and the four-cube graph automorphisms give the stated same-layer distance symmetry.

For a separately supplied Gaussian field, its quadratic energy makes neutral-pair free-energy differences proportional to Q². No exact such identity for ice is assumed.

## Finite numerical comparisons

Relative to the nearest in-layer pair, the calculated charge-four/charge-two difference ratios at distances two, three and four are approximately 3.449,3.577,3.623. These are below four; three values do not prove convergence to four. Along the prism, with reference separation z=2, the ratios at z=4 and 8 are approximately 3.960 and 4.007.

At z=8 the next charge-four step is within 1% of log(lambda0/lambda4), and its ratio to the charge-two step is within 1% of 4c(4)/c(2). The equality
log(lambda0/lambda4)/log(lambda0/lambda2)=4c(4)/c(2)
is an algebraic consequence of c(s)=(A/s²)log(lambda0/lambda_s). Equality of these spectral quantities does not make the finite-separation insertion steps exactly equal.

Using K=2c(2), same-layer differences divided by K Q² Delta G lie near 0.9614,0.9738,0.9781 for charge two and 0.8290,0.8708,0.8860 for charge four. These measured residuals grow in the stated comparison. They do not uniquely identify a microscopic core mechanism, establish an exact string limit or derive a universal Coulomb law.

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
- [uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_bounded_theorem_note_2026-09-23](UNIFORM_ICE_TEST_DEFECTS_INTERACT_THROUGH_THE_LATTICE_GREEN_FUNCTION_WITH_THE_FLUX_COST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- [uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23](UNIFORM_ICE_STATIC_PHOTON_STIFFENS_IN_A_BACKGROUND_FLUX_AND_SATURATION_LEAVES_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8951, head `53cddd234a792d5cf4eca6e72bb01941acb03f97`, branch `claude/ice-defect-charge-squared-law-20260924`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_test_defect_pairs_follow_the_charge_squared_law_with_a_core_correction_2026_09_24.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

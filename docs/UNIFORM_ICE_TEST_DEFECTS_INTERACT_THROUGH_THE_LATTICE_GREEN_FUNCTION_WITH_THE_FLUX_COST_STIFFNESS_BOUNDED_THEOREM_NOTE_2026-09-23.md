---
claim_id: uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Charge normalization and a conditional Gaussian prism potential, with finite transfer calculations for neutral test-defect pairs."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
  - uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_2026_09_23.py
---

# Neutral defect insertions and finite prism comparisons

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Definitions and exact formulas

At a cubic vertex, let delta be occupied degree minus three. For the staggered oriented field, divergence is 2delta(-1)^(x+y+z). Thus degree-four and degree-two test vertices have charge magnitude two. They extend the counting problem for a probe; they are not valid vertices of defect-free ice. The pair is neutral: for a first degree shift d at the origin, the second shift at (r,z) is -d(-1)^(r_x+r_y+z).

On an even periodic cross-section, let psi be a normalized positive top vector of the zero-flux symmetric transfer T, with eigenvalue lambda0. Define defect transfer matrices by changing the required local occupied degree. Same-layer insertion weight is psi^T T_D psi/lambda0. At z>=1 layers apart it is psi^T T_D2 T^(z-1) T_D1 psi/lambda0^(z+1). V is minus its logarithm where the weight is positive. Complementing all links exchanges defect types without changing counts. On 4 by 4, the transverse graph is the four-dimensional cube; its distance-transitive automorphisms imply the same-layer distance symmetry.

For a separate divergence-free Gaussian field of stiffness K and opposite charges of magnitude Qc, differences satisfy V_G(r,z)-V_G(r',z')=K Qc²[G_A(r',z')-G_A(r,z)]. The prism kernel difference is
G_A(r,z)-G_A(0,0)=A^-1[-|z|/2+sum_(q!=0)(cos(q.r)exp(-D|z|)-1)/(2sinh D)],
where cosh D=1+sum_i(1-cos q_i).
Each transverse mode solves its one-dimensional difference equation; the zero mode contributes -|z|/2. A fixed-width prism therefore has a linear axial Gaussian potential, not a three-dimensional infinite-distance 1/r potential.

## Finite numerical support

On 4 by 4 and 2 by 8, use Qc=2 and K=2c(2), measured from the flux sector rather than fitted to pair data. The runner compares its explicitly listed in-layer offsets and axial separations z=1,...,9. Selected square differences agree with the Gaussian comparison within 4%, with differences referenced to in-layer distance two within 1%. Strip length/axial comparisons are within 3%, and its two width comparisons within 8%. At z=8 the next axial step agrees within 0.1% with the Gaussian step and within 1% with log(lambda0/lambda2).

These are numerical observations at the listed offsets. They do not prove a universal attraction law, an exact asymptotic string tension, a microscopic mechanical force or the infinite-volume Gaussian stiffness.

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

Original source: PR #8875, head `970731556520cf4ac3bb4bc5a2562b60dbd30931`, branch `claude/ice-test-defects-coulomb-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_test_defects_interact_through_the_lattice_green_function_with_the_flux_cost_stiffness_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

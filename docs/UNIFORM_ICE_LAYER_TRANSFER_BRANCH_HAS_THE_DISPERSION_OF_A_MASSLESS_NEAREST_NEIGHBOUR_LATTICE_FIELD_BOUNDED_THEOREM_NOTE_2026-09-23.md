---
claim_id: uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Exact symmetries of a supplied finite ice transfer; numerical maximum-modulus sector levels on 2 by 8 and 4 by 4 sections compared with a Gaussian lattice rate."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
  - uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_2026_09_23.py
---

# Ice transfer symmetries and finite spectral comparisons

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Objects and exact structural statements

On an even periodic a by b cross-section, T(v',v) counts horizontal link assignments giving three occupied links at each cubic vertex, with incoming and outgoing vertical bits v,v'. Parallel links on width two are distinct. Let E(x,y)=(-1)^(x+y)(2v(x,y)-1), S=sum E, and restrict to S=0. T is real symmetric: exchange incoming and outgoing vertical bits. Translating a horizontal assignment or complementing every bit gives weight-preserving bijections, so T commutes with transverse translations and bit complement C. These operations preserve S=0.

Characters of the finite translation group give orthogonal momentum projectors. Multiplication by the staggered sign shifts occupation momentum by (pi,pi). Complement sends E to -E; its even and odd eigenspaces are invariant. Odd complement parity alone does not identify a one-particle state.

For a separately supplied scalar lattice Laplacian, continuing longitudinal momentum to iD in Q+2-2cos(k_z) gives cosh D=1+Q/2, Q=sum_transverse 2(1-cos q_i). This is the exact comparison rate for that Gaussian model.

## Finite numerical observations

Define D(q)=log(lambda0/|lambda_top(q+(pi,pi))|), where top means maximum modulus in the projected zero-flux sector. The original finite comparison reproduced by the runner is:

| Section | Physical momenta | Ice rates, rounded | Gaussian rates, rounded |
|---|---|---|---|
| 2 by 8 | (0,pi/4), (0,pi/2), (0,3pi/4) | 0.7429, 1.3165, 1.6581 | 0.7478, 1.3170, 1.6530 |
| 4 by 4 | (pi/2,0), (pi/2,pi/2), (pi/2,pi) | 1.2963, 1.7419, 2.0469 | 1.3170, 1.7627, 2.0634 |

The tests allow 1% and 2%, respectively, and check selected symmetry pairs and ten eigenvector parities. These are finite numerical eigenpair calculations. They neither prove an exact Gaussian dispersion nor establish a gapless infinite-volume phase, a universal velocity or quantum particles.

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
- [uniform_ice_zero_flux_layer_chain_gap_closes_as_the_smallest_transverse_wavenumber_bounded_theorem_note_2026-09-23](UNIFORM_ICE_ZERO_FLUX_LAYER_CHAIN_GAP_CLOSES_AS_THE_SMALLEST_TRANSVERSE_WAVENUMBER_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8869, head `54723beb4e4b95b68b1afe545fafcb3cabcffe47`, branch `claude/ice-layer-transfer-photon-dispersion-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

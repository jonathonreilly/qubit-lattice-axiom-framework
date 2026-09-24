---
claim_id: uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Numerical comparisons of selected momentum-sector rates across finite ice strips and flux sectors, with complement-parity distinctions."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
  - uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_bounded_theorem_note_2026-09-23
  - uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_2026_09_23.py
---

# Finite flux-sector rate shifts and complement parities

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Definitions and structural scope

For the supplied even-section ice transfer, |S|=s is invariant, and translations and complement commute with it. On 2 by b let lambda_s be its sector spectral radius and define
D_s(q)=log(lambda_s/|lambda_top(pi,pi+q)|), d_s(q)=D_s(q)-D_0(q).
Each rate is normalized by its own sector radius. A comparison between these rates is not an eigenvalue crossing within a single common spectrum.

Complement parity distinguishes invariant subspaces. An odd eigenvector is not thereby a one-particle state, nor does an even eigenvector identify a particular physical excitation.

## Finite numerical observations

On 2 by 6, 2 by 8 and 2 by 10, the selected smallest nonzero q values have positive s=2 shifts whose maximum/minimum ratio is below 1.25, while the corresponding D0 ratio exceeds 1.6. Their tested d4/d2 ratios lie between 4 and 4.5. This is approximate finite agreement, not exact wavenumber independence or a proved quadratic expansion.

At fixed rho=1/4 and q=pi/2, two computed shifts are approximately 0.0436 on 2 by 4 and 0.0323 on 2 by 8. Two points do not establish monotonic finite-size scaling or its limit.

At q=pi, D2-D0 is between -0.19 and -0.11 on 2 by 4,6,8,10. On 2 by 8, the computed leading s=2 eigenvector there has positive eigenvalue and even complement parity; the corresponding s=0 vector is negative and odd. At q=pi/4, the tested s=2 vector is negative and odd. These statements concern finite eigenpairs only. They neither establish particle branches nor exclude a general smooth-medium mechanism. Finite-q lattice dispersion must be distinguished from a continuum rescaling.

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
- [uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_bounded_theorem_note_2026-09-23](UNIFORM_ICE_LAYER_TRANSFER_BRANCH_HAS_THE_DISPERSION_OF_A_MASSLESS_NEAREST_NEIGHBOUR_LATTICE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- [uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23](UNIFORM_ICE_STATIC_PHOTON_STIFFENS_IN_A_BACKGROUND_FLUX_AND_SATURATION_LEAVES_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8949, head `61a6c8baeb0545de6f975f87cc65b45737520178`, branch `claude/ice-flux-sector-photon-shift-and-second-branch-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_flux_sector_photon_rise_is_wavenumber_independent_and_a_second_branch_crosses_below_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

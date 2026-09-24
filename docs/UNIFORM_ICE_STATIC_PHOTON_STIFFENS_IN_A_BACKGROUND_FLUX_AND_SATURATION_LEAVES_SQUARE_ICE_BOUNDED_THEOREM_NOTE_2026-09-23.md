---
claim_id: uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Exact saturated-sector reduction to square-ice counting and finite numerical flux costs and momentum-sector rates, with explicitly fitted comparison models."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
  - uniform_ice_layer_transfer_branch_has_the_dispersion_of_a_massless_nearest_neighbour_lattice_field_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_2026_09_23.py
---

# Saturated ice layers and finite flux-sector spectra

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Exact saturated-sector identity

On an even periodic transverse section with A vertices, the staggered vertical flux satisfies |S|<=A. Each fully saturated sign fixes its vertical bit layer uniquely. Consecutive layers have opposite staggered flux, and every cubic vertex has exactly one of its two vertical links occupied. The remaining constraint is exactly two occupied horizontal links out of four.

Thus the saturated transfer is [[0,Z],[Z,0]], where Z is the number of square-ice configurations on that transverse multigraph. Its positive eigenvalue is Z and its other eigenvalue is -Z. Conditioned on saturated vertical layers, horizontal layers are independent uniform square-ice configurations. Integer row counts give Z=18,114,858,7074,2970 on 2 by 2, 2 by 4, 2 by 6, 2 by 8 and 4 by 4.

## Finite numerical observations

On 4 by 4 define c(s)=(16/s²)log(lambda0/lambda_s), using the spectral radius of the absolute-flux-s sector. The tested values for s=2,4,...,16 increase from approximately 0.3270 to 0.4373.

A maximum-modulus momentum-sector rate D_s(q)=log(lambda_s/|lambda_top|) is compared at the explicitly stated staggered momenta. At q=(pi/2,0), sampled s=0,2,4,6,8,10 give approximately 1.2963,1.3081,1.3452,1.4120,1.5184,1.6846. The shifts for s=4 and s=2 have ratio about 4.118. At q=(0,pi), the tested s=2,4 shifts are within 2% of the corresponding first-momentum shifts. These observations are not a wavenumber-independent law or an expansion proved for arbitrary small flux.

## Fitted comparison and its limits

A two-point fit c(rho)=c2+d rho² at rho=2/16 and 4/16 gives approximately c2=0.3261,d=0.0631. This is a fit. For a supplied isotropic quartic cost, its quadratic coefficients around a longitudinal background are c2+6d rho² and c2+2d rho². A continuum small-q approximation suggests fractional rate shift 2d rho²/c2.

At finite lattice momentum, the corresponding anisotropic Gaussian lattice formula is instead
cosh D=1+(K_z/K_perp)Q/2.
For small rho its absolute shift is (4d rho²/c2)tanh(D0/2), not D0 times the continuum fractional shift. The runner's old continuum fractions are retained only as an explicitly chosen comparison, not evidence excluding every quartic mechanism. Neither Gaussianity, a quantum photon nor a thermodynamic nonlinear response is established.

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
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8928, head `f90c3da5fa2acfbf4072fc279e09b55eb6f2fc43`, branch `claude/ice-static-photon-nonlinear-response-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

---
claim_id: ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Conditional Gaussian trace identities and finite transfer-count and flux-cost comparisons on specified planar strips and cubic prisms."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
  - uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_bounded_theorem_note_2026-09-23
  - uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23
runner: scripts/ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_2026_09_23.py
---

# Finite planar and cubic ice comparisons with Gaussian calibration

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Conditional calibration

For a supplied divergence-free Gaussian field on a periodic strip of width a times the infinite line, the equal-row covariance is sqrt(Q/(Q+4))/K with Q=2-2cos q. In the fixed zero-flux sector, imposing unit mean-square field sets K_a=a^-1 sum_q sqrt(Q/(Q+4)), and a uniform flux S costs K S²/(2a) per row.

In the infinite plane the transverse projector has trace one away from zero. Symmetry splits its zone average equally between the two components, proving the comparison calibration K=1/2. This is an identity for a supplied Gaussian model, not a derivation of the square-ice stiffness.

## Exact count control and finite spectral comparison

Two constructions, a site tensor contraction and direct horizontal-row counting, give the same finite square-ice transfers. Integer powers give torus counts 2970,98466,98466,16448400 on 4 by 4, 4 by 6, 6 by 4 and 6 by 6.

On the specified even widths a=4,6,...,20, compute c(2)=(a/4)log(lambda0/lambda2), using absolute staggered-flux sectors. The numerical values rise from 0.24252 to 0.26090; their excess over K_a/2 lies between 4.1% and 4.7%. On the two separately computed cubic prisms 2 by 8 and 4 by 4 the deviations from their own Gaussian calibrations are below 0.5%. The ratio of deviations exceeds ten for these selected comparisons.

No monotonic law outside the tested sizes, limiting stiffness or causal explanation by dimension is proved. Agreement of a flux cost does not establish a Gaussian joint law or all lattice-scale correlations.

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
- [uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23](UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- [uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_bounded_theorem_note_2026-09-23](UNIFORM_ICE_UNIT_LINK_FIELD_FIXES_ONE_STIFFNESS_FOR_THE_FLUX_COST_AND_THE_FIELD_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- [uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23](UNIFORM_ICE_STATIC_PHOTON_STIFFENS_IN_A_BACKGROUND_FLUX_AND_SATURATION_LEAVES_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8930, head `b1da59092cefdb8ffca504da2397291dd4dfb3e6`, branch `claude/ice-sum-rule-ten-times-closer-in-three-dimensions-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

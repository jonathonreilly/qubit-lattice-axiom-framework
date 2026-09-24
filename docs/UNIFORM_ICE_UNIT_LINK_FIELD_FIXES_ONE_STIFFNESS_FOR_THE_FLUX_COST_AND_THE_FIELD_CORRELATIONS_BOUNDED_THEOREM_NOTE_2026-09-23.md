---
claim_id: uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Conditional Gaussian prism covariance and variance calibration, with finite numerical ice flux-cost and equal-layer correlation comparisons."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
  - uniform_ice_flux_stiffness_on_a_square_cross_section_by_row_transfer_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_2026_09_23.py
---

# Gaussian variance calibration and finite ice cost comparisons

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Conditional Gaussian calculation

Supply a real divergence-free Gaussian link field on an even periodic section of area A times the infinite line, with energy (K/2)sum E², K>0, and fixed zero vertical flux for the covariance. For nonzero transverse momentum q, integrating the longitudinal transverse-projector entry gives
Szz(q)=integral Q/[K(Q+2-2cos k_z)] dk_z/(2pi)=sqrt(Q/(Q+4))/K.
The substitution tan(k_z/2) evaluates the integral; Q=0 contributes zero in this fixed-flux sector. A uniform flux S adds energy K S²/(2A) per layer.

Calibrating this Gaussian covariance to mean squared vertical field one therefore sets K_A=A^-1 sum_q sqrt(Q/(Q+4)). This is a Gaussian calibration, not a consequence of divergence-freedom and unit arrows alone. In the infinite cubic Gaussian model the transverse projector has trace two away from the zero mode. Symmetry shares its zone average equally among three components, giving the calibration K=2/3. This does not fix the infrared stiffness of non-Gaussian ice.

## Finite ice comparison

For the supplied symmetric ice transfer, use a positive zero-flux top vector psi, normalized to unit norm, and its layer measure psi². In the absolute-flux-two sector define c(2)=(A/4)log(lambda0/lambda2), and independently compute Szz(q)=<|sum E_r exp(-iq.r)|²>/A. Parseval and zero flux give A^-1 sum Szz=1 and Szz(0)=0 exactly for this layer measure.

The runner compares sections 2 by 2, 2 by 4, 2 by 6, 2 by 8, 2 by 10 and 4 by 4. Rounded costs are 0.28082, 0.30726, 0.31210, 0.31374, 0.31451 and 0.32704. Their deviations from K_A/2 are below 1%. Using K=2c(2), the tested covariance deviations are below 10% on 2 by 2, 5% on the other strips, and 1% on 4 by 4. These nonzero residuals are retained. Neither the exact ice law nor all of its higher moments have been shown Gaussian.

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
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8871, head `6bad0fbbbcfe5abbfa5fe296c04e3ed904798a31`, branch `claude/ice-rule-fixes-one-stiffness-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_unit_link_field_fixes_one_stiffness_for_the_flux_cost_and_the_field_correlations_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

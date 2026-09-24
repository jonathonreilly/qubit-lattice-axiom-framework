---
claim_id: square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "An exact Parseval-based weighted identity and finite square-ice row-correlation comparisons on four widths; no Gaussian probability-law or long-wavelength limit theorem."
upstream_dependencies:
  - minimal_axioms
  - ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_bounded_theorem_note_2026-09-23
runner: scripts/square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_2026_09_24.py
---

# Square-ice two-point comparisons and an exact weighted sum identity

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Definitions and exact identity

On an even periodic strip of width a, choose the positive normalized zero-flux top vector psi of the symmetric square-ice transfer and its row law psi². With staggered unit field E_x, define S(q)=<|sum_x E_x exp(-iqx)|²>/a. Zero flux gives S(0)=0, and Parseval gives sum_q S(q)=a.

Set g(q)=sqrt(Q/(Q+4)), Q=2-2cos q, K_a=a^-1 sum g, and choose any positive K. For q!=0 define R(q)=K S(q)/g(q). Then
sum_(q!=0) R(q)g(q)/sum_(q!=0)g(q)=K/K_a.
This follows directly by substitution and Parseval. It holds for every zero-flux unit-field probability law, not only a Gaussian one.

## Finite numerical observations

The runner takes K=2c(2) from finite flux-sector eigenvalues on widths 8,12,16,20. At the smallest nonzero momentum, the numerical ratios are approximately 0.9901,0.9949,0.9970,0.9981. The corresponding zone-boundary ratios are approximately 1.1067,1.0999,1.0971,1.0957; the tested half-zone sequences increase monotonically.

Their g-weighted averages reproduce K/K_a, approximately 1.04290,1.04497,1.04588,1.04633. The residual is an aggregate across the entire zone, including negative and positive deviations, not a proof that the boundary alone causes a stiffness change.

These are two-point comparisons at four finite widths. Even exact agreement of a covariance would not imply a Gaussian joint law. No asymptotic limit, higher-correlation theorem, universal dimensional mechanism or quantum-particle statement is retained. Weighted sums using a numerical eigenvector have numerical precision, not exact arithmetic.

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
- [ice_unit_field_sum_rule_is_ten_times_closer_in_three_dimensions_than_in_square_ice_bounded_theorem_note_2026-09-23](ICE_UNIT_FIELD_SUM_RULE_IS_TEN_TIMES_CLOSER_IN_THREE_DIMENSIONS_THAN_IN_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8954, head `441f9d37519ac51a99997d147039da8c860753fb`, branch `claude/square-ice-zone-boundary-excess-20260924`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_2026_09_24.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

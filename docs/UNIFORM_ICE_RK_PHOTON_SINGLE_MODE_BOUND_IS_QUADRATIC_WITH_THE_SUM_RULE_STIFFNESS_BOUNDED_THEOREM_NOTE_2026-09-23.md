---
claim_id: uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "An exact conditional flip-graph energy identity and finite numerical Rayleigh quotients; a positive-excitation bound additionally requires removal of all ground-space components."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
  - uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_2026_09_23.py
---

# Ice flip-graph sum rules and a ground-space-qualified variational quotient

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Supplied graph Hamiltonian

On the finite set of ice orientations, supply H=D-A, where A counts plaquette-flip edges with multiplicity and D is their degree matrix. H is positive semidefinite and the normalized uniform vector u is a zero-energy state. Every connected component has its own constant zero mode; frozen configurations are components too. This is a supplied quantum Hamiltonian, not a derived physical dynamics.

For a diagonal observable O and uniform u, the graph quadratic form is
<u,O* H O u>=(2M)^-1 sum_(directed flip C to C') |O(C')-O(C)|²,
where M is the number of configurations. For O=E_z(k)/sqrt(N), an xz or yz plaquette contributes 4s_x²/N or 4s_y²/N. Cubic symmetry of the full uniform ensemble gives
<u,O* H O u>=2 n_f(s_x²+s_y²),
where n_f is the mean fraction of flippable plaquettes, normalized by 3N, and s_i²=2-2cos k_i.

## Ground-space qualification

When Szz(k)=||Ou||²>0, the displayed numerator divided by Szz is a Rayleigh quotient. It bounds the minimum energy in the spectral support of Ou, which may include zero. Nonzero momentum only ensures orthogonality to a translation-invariant chosen u; it does not ensure orthogonality to every ground state.

Let P0 project onto the full kernel of H. A positive-excitation variational bound uses
<u,O* H O u>/||(1-P0)Ou||²
when its denominator is nonzero. The original denominator is justified for that purpose only after proving P0 Ou=0.

The L=2 graph has 9600 vertices, 49920 directed flips and 937 components. Independent exact enumeration gives ||Ou||²=38/25 at k=(pi,0,0), but ||P0 Ou||²=14/75. At k=(pi,pi,0) the corresponding projection is 3/25. These are explicit counterexamples to the omitted ground-space assumption. The exact flippable fraction is 13/60, and the f-sum is checked at all eight momenta.

## Finite numerical observations

Seeded runs on L=8 and L=16 estimate n_f and Szz from the same configurations. The unprojected quotient is compared with 2n_f K_cont |s|², using the continuous Gaussian calibration from the winding note. The cancellation giving this form is exact if the additional covariance Szz=(s_x²+s_y²)/(K |s|²) is supplied; the numerical ice comparison is approximate.

Two finite sizes do not prove a quadratic infinite-volume excitation branch, exclude all linear modes, or determine a universal coefficient. The computed observables are correlated and are not independent evidence sources.

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
- [uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_bounded_theorem_note_2026-09-23](UNIFORM_ICE_STATIC_PHOTON_HAS_TWO_DEGENERATE_TRANSVERSE_POLARIZATIONS_WITH_ONE_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied definitions and scoped mathematics only; no inherited audit grade or stronger conclusion.
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8905, head `1cd7fb19070eb7a57b5648ae623446245de6a644`, branch `claude/ice-rk-photon-quadratic-bound-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_rk_photon_single_mode_bound_is_quadratic_with_the_sum_rule_stiffness_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

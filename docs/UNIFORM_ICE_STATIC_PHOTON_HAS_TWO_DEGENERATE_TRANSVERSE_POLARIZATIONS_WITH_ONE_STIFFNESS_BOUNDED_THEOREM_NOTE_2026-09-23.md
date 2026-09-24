---
claim_id: uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Longitudinal covariance nulls and exact L=2 tensor values, with seeded L=8 estimates of transverse covariance eigenvalues."
upstream_dependencies:
  - minimal_axioms
  - uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
runner: scripts/uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_2026_09_23.py
---

# Exact ice tensor constraints and finite transverse spectra

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Exact tensor statements

In the uniform even-torus ice measure, define F_i(k)=sum_r exp(-ik.r)E_i(r), S_ij=<F_i conj(F_j)>/N and s_i=1-exp(-ik_i). Divergence gives sum s_i F_i=0 configuration by configuration. Therefore S conj(s)=0 and S is positive semidefinite Hermitian. Parseval gives N^-1 sum_k Szz(k)=1. At k=0 there is no specified longitudinal vector.

A separately supplied isotropic Gaussian field has S=P/K on nonzero modes, with P=I-conj(s)s^T/|s|². Its two nonzero eigenvalues coincide. This additional covariance assumption does not follow merely from the divergence null. Cubic symmetries and reflections imply equality on symmetry-enforced axial and body-diagonal transverse representations, but not at every momentum.

Exact enumeration of all 9600 L=2 configurations gives eigenvalues 87/75 and 87/75 at (pi,pi,pi), and 86/75 and 114/75 at (pi,pi,0). The latter explicitly disproves universal finite-torus transverse degeneracy.

## Finite numerical observations

The runner tests its worm tensor against the exact L=2 values and samples L=8 with two million completed loops. It compares nonzero-momentum transverse eigenvalues with the continuous Gaussian calibration K_cont=(2N+1)/(3N), described in the winding note. The historical numerical range K_cont lambda was 0.9934 to 1.0088; fresh output is the reproduction evidence.

Linear tests on fixed transverse bases cover 21 axial momenta and seven equal-component diagonal momenta. Sorted-eigenvalue splits are also averaged over cubic momentum classes. These class-averaged estimates are not maxima over individual momenta, and upward sorting bias in expectation does not create a samplewise upper bound or confidence bound. Binned jackknife errors are descriptive; maximum selection and multiple tests have no claimed confidence coverage.

A two-point covariance comparison does not establish a Gaussian probability law, exact particle degeneracy, quantum dynamics or an infinite-volume limit.

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

Original source: PR #8890, head `7df6510fd36ff39b090ca952c09d68a47c2140a7`, branch `claude/ice-two-degenerate-polarizations-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_static_photon_has_two_degenerate_transverse_polarizations_with_one_stiffness_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

---
claim_id: uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Exact small-torus counts and a reversible loop construction, with finite winding and correlation diagnostics; continuous Gaussian calibration is separated from discrete winding fits."
upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_2026_09_23.py
---

# Ice winding samples and the Gaussian zero-mode distinction

**Type:** bounded_theorem
**Status:** conditional mathematics with finite numerical support; unaudited.

Uniform ice and any Gaussian comparison or quantum Hamiltonian below are supplied mathematical models. They are not derived from the repository axioms or adopted as a physical law. No gravity, Born-weight or statistical-bridge conclusion is asserted. The original filename identifies the submission; this title and scope govern the result.

## Supplied finite measure and loop stationarity

On an even L by L by L torus, each directed positive-axis link carries E_i=+1 or -1; vertex divergence is zero. Parallel links at L=2 are distinct. A completed loop starts at a uniform vertex, follows an outgoing arrow, flips it, and then chooses an outgoing arrow other than the just-flipped edge until first returning to its start. There are three choices initially and at each later open head. Reversing a completed oriented path in the final configuration gives a path of the same length and probability, so the completed-loop transition is symmetric and the uniform ice measure is stationary. Differences of two ice orientations decompose into directed cycles, each with positive loop probability; this gives reachability of the finite configuration space. Finite samples still require equilibration and correlation assessment.

An independent exhaustive constraint enumeration gives 9600 ice orientations on L=2, 880 at zero winding and 125 winding triples, with <W_i²>=76/25. W_i is the sum through one plane normal to i. Divergence makes that sum independent of plane.

## Gaussian comparisons: two different zero modes

For nonzero lattice momentum, supply Gaussian covariance Szz=Pzz/K, where Pzz=1-s_z²/sum s_i² and s_i²=2-2cos k_i. The exact finite symmetry identity is sum_(k!=0) Pzz=2(N-1)/3, N=L³.

If the harmonic zero mode is CONTINUOUS with Szz(0)=1/K, unit-variance calibration gives K_cont=(2N+1)/(3N). This is a continuous Gaussian surrogate.

The runner's winding fit instead uses the bounded even grid W=-L²,-L²+2,...,L² with weights exp[-K W²/(2L)]. Here Szz(0)=<W²>/L, so a Gaussian nonzero-mode ansatz with this zero mode must satisfy
1=2(N-1)/(3NK)+<W²>/(LN).
In general <W²> is not L/K, so the discrete fit does not have the exact calibration K_cont. Divergence and unit arrows alone do not imply either full Gaussian law.

## Finite sampling diagnostics

The original seeded schedules use L=2 controls; winding runs on L=8,12,16,24; and one million completed loops for correlations on L=8. The runner reports fitted c_W=K_W/2, their bin-based uncertainty estimates, and comparisons with K_cont/2. It computes symmetry-class and low-momentum averages within each bin before estimating their dispersion, so correlated and conjugate momenta are not counted as independent measurements.

Values near 0.335 and small covariance residuals are finite diagnostics. An average across sizes is descriptive, not an estimate justified by a proven common limiting parameter. No exact stiffness, statistically established universal offset, higher-order Gaussian law or quantum photon follows.

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
- Finite graph counting, linear algebra, probability, differentiation and the explicit Gaussian integrals used above are mathematical tools, not physical premises.

## Review record

Original source: PR #8881, head `539a262e01734296c2ca7968380576d952af83f6`, branch `claude/ice-winding-stiffness-one-third-20260923`. The original note and distinct verification code were reviewed in the primary session without subagents. Changed claims and controls were confirmed in the same session; no separate fix reviewer or formal audit is claimed. Earlier author mutation reports are historical; the combined landing receipt records fresh checks.

## Verification

```bash
python3 scripts/uniform_ice_on_cubic_tori_winding_stiffness_and_correlations_carry_the_sum_rule_stiffness_2026_09_23.py
```

The canonical runner prints its finite diagnostics and a final TOTAL. Successful reproduction has exit code zero and FAIL=0.

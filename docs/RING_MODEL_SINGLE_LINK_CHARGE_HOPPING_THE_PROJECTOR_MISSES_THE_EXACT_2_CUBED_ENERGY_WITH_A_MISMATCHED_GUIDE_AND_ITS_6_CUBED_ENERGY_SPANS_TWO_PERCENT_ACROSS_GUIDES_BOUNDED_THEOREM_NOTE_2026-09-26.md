---
claim_id: ring_model_single_link_charge_hopping_the_projector_misses_the_exact_2_cubed_energy_with_a_mismatched_guide_and_its_6_cubed_energy_spans_two_percent_across_guides_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: Supplied finite sign-free ring plus all-link hopping Hamiltonian, g=1, M=2, t>0. Full 24-link
  numerical Lanczos Ritz references, with convergence and recurrence-residual diagnostics, compared against
  finite-population guided projector samples; guide-dependent numerical spread on 6^3. No certified exact
  ground-energy error, controlled 6^3 link expectation, stationarity or equilibration proof, phase, or
  physical identification.
upstream_dependencies:
- minimal_axioms
- ring_model_with_single_link_charge_hopping_changes_rapidly_between_weak_and_strong_hopping_and_its_moment_bound_stays_finite_at_small_momentum_bounded_theorem_note_2026-09-25
- ring_model_single_link_charge_hopping_link_expectation_from_fixed_guide_grids_depends_on_the_guide_penalty_on_6_cubed_bounded_theorem_note_2026-09-26
runner: scripts/ring_model_single_link_charge_hopping_projector_against_the_exact_full_2_cubed_torus_and_across_guides_2026_09_26.py
---

# Single-link charge hopping on the ring clause: the projector misses the exact 2³ energy with a mismatched guide, and its 6³ energy spans two percent across guides

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** numerical Ritz references and finite projector diagnostics; unaudited.

## Result

Open PR 9263 estimated the link expectation `⟨σ^x⟩(t)` of the ring clause with
single-link charge hopping from energies of a fixed-population projector.
Open PR 9268 then found that at a fixed guide the result still moves by
`0.04`–`0.08` on `6³` between two guide charge penalties. Its mixed estimator equals the ground energy for any positive guide when the sampled weighted distribution is the exact projected ground distribution. Finite population, finite projection time and incomplete equilibration can all spoil this condition.
This block compares the projector with a numerical Lanczos reference that has hopping on
every link, and measures how its `6³` energy depends on the guide.

- **A numerical reference with hopping everywhere.** On the full `2³` torus,
  with the single-link term on all 24 links (`2²⁴` states), matrix-free
  Lanczos gives the ground energies `E₀ = -9.631658548` at `t = 0.35` and
  `-10.430531975` at `t = 0.5` (`M = 2`, `g = 1`), with successive Ritz-value changes below `10⁻¹¹` and a small tridiagonal recurrence-residual estimate. The control
  of open PR 9268 used the term on six links only.
- **The gamma=0.8 guide is close at the tested settings.** With charge penalty `γ = 0.8`, the
  projector's energy is within `0.01` of both exact values with 1000 and
  4000 walkers (three independent runs each): biases `−0.0017` and `−0.0009` at `t = 0.35`, and `+0.0073` and `−0.0004` at `t = 0.5`, with 1000 and 4000 walkers.
- **The gamma=1.4 guide differs at the tested populations.** At `t = 0.5`
  with `γ = 1.4`, the projector's energy sits 0.03 to 0.09 above the exact one, at
  250, 1000 and 4000 walkers, from ice starts and from random starts, and in
  both halves of every run: averaged over three runs, the bias in the first and second halves is `+0.038` and `+0.093` with 250 walkers, `+0.088` and `+0.058` with 1000, `+0.059` and `+0.053` with 4000, and `+0.052` and `+0.029` with 4000 from random starts (mean `+0.059`). The effective sample size per
  generation is about 0.95, so the weights do not collapse within a
  generation. Our reading, not a demonstration: a charge penalty that is too
  strong under-represents charged configurations that the ground state holds.
  The walkers reach those configurations rarely, and when they do the
  configurations carry large weights, so a fixed population misses them in
  most runs.
- **On 6³ the energy spans two percent across guides.** At `t = 0.35` with
  1920 walkers the energy is `−199.67 ± 0.25`, `−203.20 ± 0.16`, `−203.80 ± 0.12`, `−202.94 ± 0.12` and `−201.10 ± 0.19` at `γ = 0.8`, `1.1`, `1.4`, `1.7` and `2.0`, a spread of `4.1` (2 % of the energy); the local-energy variance is `55`, `78`, `103`, `171` and `261`, and the effective sample size per generation `0.88`, `0.79`, `0.78`, `0.66` and `0.50`. The lowest energy falls inside the
  range. The weighted variance of the local energy rises steadily with `γ`
  and the effective sample size per generation falls, so the guide with the
  smallest variance does not give the lowest energy.
- **Two start choices compared.** On `6³`, random starts
  reproduce the ice-start energies within errors at `γ = 0.8` and `1.1`, which does not prove stationarity or rule out a common slow transient: random starts give `−200.13 ± 0.14` against `−199.67 ± 0.25` from ice at `γ = 0.8` (`−1.6σ`) and `−203.29 ± 0.12` against `−203.20 ± 0.16` at `γ = 1.1` (`−0.5σ`); with 960 walkers the energies are `−199.82 ± 0.27` and `−202.42 ± 0.21`, so halving the population is not resolved at `γ = 0.8` and raises the energy by `0.78 ± 0.26` at `γ = 1.1`.

**Consequence for the link expectation.** The 6³ guide spread is about 4.1 in the reported sample means; it does not measure each estimator's error against the unknown 6³ ground energy. If exact estimator means differed by that amount, at least one would differ from the true energy by at least half the spread, but finite sampling uncertainty also enters here. For an estimator error b(t), the central-difference link error is -[b(t+delta)-b(t-delta)]/(2 delta N_links), plus finite-difference truncation. A guide spread at a single t does not determine that derivative error or prove it exceeds 0.04–0.08. It does show that these runs do not establish controlled 6³ expectations. Separately quoted small-torus derivative values and the 16000-walker probe are not reproduced by this runner and are not retained as results here.

**Numerical reference limitation.** The 2²⁴ basis is the full finite Hilbert space, but the three-vector Lanczos computation is numerical. Successive Ritz-value stability and beta times the final Ritz-vector component are convergence diagnostics; loss of orthogonality can affect the latter. They are not certified eigenvalue error bounds or an independent ground-state certificate. Positive all-link t connects the configuration graph, so the exact stoquastic Hamiltonian has a unique positive ground vector by Perron–Frobenius, but the runner does not rigorously enclose that vector. Reported projector offsets use the converged Ritz value as a numerical benchmark. ESS is normalized per generation and, for the small-torus mismatch table, printed from the last seed only; high one-generation ESS does not establish population independence or sampling coverage. Eight-block standard errors are heuristic and need not bound autocorrelation, population bias or projection transients.

## Setting and decision points

- **D-clause and D-hopping (supplied, open PR 9263).** The ring clause and
  the single-link charge term, as there; nothing is adopted.
- **D-guide (method choice).** The guide `exp(α N_flip − γ Σ_v Q_v²)` is a
  calculational device. It fixes the sampling, not the model, and finite-population, finite-projection and sampling errors can depend on it.
- **D-projector (method choice).** A continuous-time walk with rates
  `|H_{σ'σ}| ψ(σ')/ψ(σ)`, a weight `exp(−∫ E_L)` and comb resampling to a
  fixed population every `dτ = 0.05`, as in open PRs 9263 and 9268. Separate
  checks (not in this runner) confirmed that the incremental rate tables
  equal a fresh recomputation after thousands of events, and that every rate
  equals the brute-force ratio on 2³ and 4³.

## Relation to other work

- Open PR 9266 (draft) and open PR 9268 found the guide dependence of
  energy differences at fixed `t`. This block shows it in the energy itself
  against an exact result, and on `6³` across five penalties.
- **Prior art (not premises).** Population-control and guide-quality
  effects in fixed-population and branching projector Monte Carlo are
  standard; see C. J. Umrigar, M. P. Nightingale, K. J. Runge, J. Chem. Phys.
  99, 2865 (1993), and M. Calandra Buonaura, S. Sorella, Phys. Rev. B 57,
  11446 (1998).

## Remaining work for a controlled link expectation

Calibrate on the numerical small torus, then separately control population, projection duration, resampling and guide dependence across every t used in the derivative. Agreement of two guides on a larger torus is useful but can share bias and does not by itself settle the expectation. An alternative sampler needs demonstrated coverage and its own error control; removing a guide or population alone is not enough. No draft probe is used as authority.

## Boundary

- Finite tori (`2³` exact, `6³` projector) and one hopping value each on
  `6³`. No estimate of the model's `⟨σ^x⟩` on `6³`, no size trend, no phase.
- The reading of the mismatched-guide bias as rare heavy configurations is
  an interpretation, not a demonstration.
- Supplied model, finite diagnostics, no physical reading.

## Reproduction

```bash
python3 scripts/ring_model_single_link_charge_hopping_projector_against_the_exact_full_2_cubed_torus_and_across_guides_2026_09_26.py
```

Five checks; prints `TOTAL: PASS=5 FAIL=0` in about 15 min.

## Inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [RING_MODEL_WITH_SINGLE_LINK_CHARGE_HOPPING_CHANGES_RAPIDLY_BETWEEN_WEAK_AND_STRONG_HOPPING_AND_ITS_MOMENT_BOUND_STAYS_FINITE_AT_SMALL_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-25](RING_MODEL_WITH_SINGLE_LINK_CHARGE_HOPPING_CHANGES_RAPIDLY_BETWEEN_WEAK_AND_STRONG_HOPPING_AND_ITS_MOMENT_BOUND_STAYS_FINITE_AT_SMALL_MOMENTUM_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_LINK_EXPECTATION_FROM_FIXED_GUIDE_GRIDS_DEPENDS_ON_THE_GUIDE_PENALTY_ON_6_CUBED_BOUNDED_THEOREM_NOTE_2026-09-26](RING_MODEL_SINGLE_LINK_CHARGE_HOPPING_LINK_EXPECTATION_FROM_FIXED_GUIDE_GRIDS_DEPENDS_ON_THE_GUIDE_PENALTY_ON_6_CUBED_BOUNDED_THEOREM_NOTE_2026-09-26.md)

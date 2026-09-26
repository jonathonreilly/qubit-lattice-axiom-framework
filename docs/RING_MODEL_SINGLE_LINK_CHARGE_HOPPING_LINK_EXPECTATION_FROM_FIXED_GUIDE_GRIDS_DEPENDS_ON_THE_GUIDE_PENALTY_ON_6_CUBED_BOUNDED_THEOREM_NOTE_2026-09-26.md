---
claim_id: ring_model_single_link_charge_hopping_link_expectation_from_fixed_guide_grids_depends_on_the_guide_penalty_on_6_cubed_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit model with the ring clause at V = 0, g = 1, the single-link term -t sigma^x and the charge mass M = 2 (open PR 9263), on 4^3 and 6^3. Exact: Hellmann-Feynman and concavity of E0 in t; for projector energies E0 + b_gam(t) at one guide penalty gam, central differences carry -(1/N_l) b_gam'(t), so the gap between two penalties' link expectations measures the guide dependence of that slope. Finite (fixed populations of 1920 walkers, projection 30, four seeds on 4^3 and three on 6^3; errors heuristic): the exact 2^3 control agrees at both penalties; on 4^3 the link expectations at gam = 0.8 and 1.1 agree within 1.5 standard errors at t = 0.30 and 0.35 and differ by 0.014-0.032 (3.2-6.3 standard errors) at t = 0.40-0.50; on 6^3 they differ by 0.041-0.077 (5.9-13.7 standard errors) at every t from 0.30 to 0.50, e.g. 0.229 against 0.152 at t = 0.35. At these populations the link expectations in the window of the rapid change are not guide-independent on 6^3. No slope, size trend, crossover or transition is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_single_link_charge_hopping_guide_dependence_of_fixed_guide_energy_grids_2026_09_26.py
---

# Single-link charge hopping: the link expectation from fixed-guide energy grids depends on the guide's charge penalty on 6³

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact decomposition of what a fixed-guide difference measures, with a finite measurement of the guide dependence; unaudited.

## Result

Draft PR 9266 found that the fixed-population projector's energy at fixed
hopping depends on the guide's charge penalty `γ`, so a grid that changes
`γ` with `t` moves its differences. The natural repair is one `γ` for a
whole grid. This block runs that repair at two penalties, `γ = 0.8` and
`1.1`, on 4³ and 6³ for `t = 0.25–0.55`, and compares the link
expectations.

- **The control passes.** On the exact 2³ control at `t = 0.4` (184320
  states, the single-link term on six links) three independent runs per
  penalty give `−9.20697 ± 0.00073` and `−9.20790 ± 0.00095` against the
  exact `−9.208058` (`+1.5` and `+0.2` standard errors).
- **On 4³ the penalties agree below `t = 0.4` and part above.** The link
  expectations agree within 1.5 standard errors at `t = 0.30` and `0.35` and
  differ by `0.014`, `0.032` and `0.031` at `t = 0.40`, `0.45`, `0.50`
  (3.2, 6.3 and 4.6 standard errors).
- **On 6³ they differ everywhere in the window.** The gap is `0.041`,
  `0.077`, `0.057`, `0.044` and `0.063` at `t = 0.30` to `0.50` (5.9 to 13.7
  standard errors); at `t = 0.35` the two grids give `0.229` and `0.152`.
- **What survives.** At both penalties and on both tori the link
  expectation rises several-fold between `t = 0.30` and `0.50` (4³: `0.130`
  to `0.449` and `0.136` to `0.418`; 6³: `0.154` to `0.452` and `0.114` to
  `0.389`), no slope is negative, and the exact control is met. Where in the
  window the rise is steepest, and how that changes with size, depends on
  the guide at these populations.

So, at 1920 walkers, link expectations in the window of the rapid change
are not guide-independent on 6³ at the quoted errors, and the size
dependence reported there by open PR 9263 and draft PR 9266 is not
established by these estimates.

## Setting and decision points

- **D-gauss, D-ring (landed).** Spin-1/2 link fields `σ = ±1` on the cubic
  `L³` torus and the clause `−g Σ_p (U_p + U_p†)` at `V = 0`, `g = 1`.
- **D-hop (open PR 9263).** The single-link term `−t Σ_l σ^x_l` and the
  charge mass `M Σ_v Q_v²`, `Q_v = div_v / 2`, at `M = 2`. A decision point of
  the supplied model, not adopted.
- **The projector (method).** The compiled sign-free projector of open PR
  9263 with fixed populations of 1920 walkers, time step 0.05, projection
  30 per run; four seeds on 4³ and three on 6³; walkers from loop-move
  samples of the zero-winding ice sector, one sample set per seed and
  penalty, reused at every `t`. The guide
  `exp(0.2 N_flip − γ Σ_v Q_v²)` keeps one charge penalty `γ` for a whole
  grid `t = 0.25, 0.30, …, 0.55`, and the grid is run at `γ = 0.8` and `1.1`.
  Errors are the larger of the seed scatter and the mean bin error, a
  heuristic.

None is adopted.

## Theorem 1 — what a fixed-guide grid gives, and what the gap measures

1. **Hellmann–Feynman and concavity.** `⟨σ^x⟩(t) = −(1/N_l) dE_0/dt`, and
   `E_0` is concave in `t`, so `⟨σ^x⟩` never decreases; a second difference
   of exact energies is never negative.
2. **A fixed-guide bias enters through its slope.** Write a projected
   energy as `E_0(t) + b_γ(t)`, with `b_γ` the fixed-population bias for the
   guide with penalty `γ`. At one `γ`, a central difference of step `δ`
   gives `⟨σ^x⟩(t) − (1/N_l) b_γ'(t)` up to `O(δ²)`, so a bias that is the same
   at every `t` cancels and only its slope remains. A grid that changes `γ`
   with `t` (draft PR 9266) adds the jump `b_{γ(t+δ)} − b_{γ(t−δ)}` instead.
3. **The gap.** The difference between the two penalties' link
   expectations is `−(1/N_l) (b_{0.8}' − b_{1.1}')(t)`: it vanishes when the
   bias does not depend on the guide, and otherwise measures how much the
   guide moves a fixed-guide difference.

Statements 1–3 are exact given the decomposition; the runner measures the
gap. ∎

## Diagnostic 1 — the fixed-guide grids

`⟨σ^x⟩(t)` from central differences of step 0.05; errors in the last
digits.

| torus | `γ` | `t = 0.30` | `0.35` | `0.40` | `0.45` | `0.50` |
|---|---|---|---|---|---|---|
| 4³ | 0.8 | 0.1301(29) | 0.1521(40) | 0.2193(26) | 0.3427(30) | 0.4487(20) |
| 4³ | 1.1 | 0.1355(23) | 0.1580(19) | 0.2052(35) | 0.3108(41) | 0.4179(63) |
| 4³ | gap | −0.0054 (−1.5 σ) | −0.0059 (−1.4 σ) | +0.0141 (+3.2 σ) | +0.0319 (+6.3 σ) | +0.0309 (+4.6 σ) |
| 6³ | 0.8 | 0.1544(67) | 0.2287(49) | 0.3005(34) | 0.3810(47) | 0.4518(17) |
| 6³ | 1.1 | 0.1136(19) | 0.1521(34) | 0.2432(24) | 0.3372(35) | 0.3893(71) |
| 6³ | gap | +0.0408 (+5.9 σ) | +0.0766 (+12.9 σ) | +0.0574 (+13.7 σ) | +0.0439 (+7.5 σ) | +0.0625 (+8.6 σ) |

Slopes from second differences of step 0.1 (errors in hundredths):

| torus | `γ` | `t = 0.35` | `0.40` | `0.45` |
|---|---|---|---|---|
| 4³ | 0.8 | 0.89(5) | 1.91(6) | 2.29(4) |
| 4³ | 1.1 | 0.70(5) | 1.53(5) | 2.13(8) |
| 6³ | 0.8 | 1.46(9) | 1.52(9) | 1.51(4) |
| 6³ | 1.1 | 1.30(4) | 1.85(6) | 1.46(8) |

For comparison, open PR 9263 measured `⟨σ^x⟩(0.5) = 0.4562 ± 0.0015` on 6³
with `γ = 0.7`, and draft PR 9266 `0.4491 ± 0.0015` with interpolated
penalties; the two grids here give `0.4518` and `0.3893`.

## What this does not do

- It does not say which penalty is closer to the infinite-population
  value; it measures that the two differ. Open PR 9276 later checked the
  projector against the exact full 2³ torus (the single-link term on all 24
  links): there a penalty of 0.8 reproduces the exact energy within 0.01,
  while 1.4 sits 0.03–0.09 above it at `t = 0.5`; on 6³ at `t = 0.35` the
  energy spans 2 per cent across penalties 0.8–2.0 and is lowest near 1.4.
- It claims no slope, size trend, crossover or transition, and revises no
  exact statement of open PR 9263.
- It adopts no clause, charge mass, guide or method.

## What a guide-independent scan needs

Larger populations with an extrapolation in the inverse population, or a
guide that carries charge-pair correlations, with the gap between two
guides checked on every torus before a size trend is read. Open PR 9276
found that at a mismatched penalty the bias on the exact 2³ torus does not
shrink between 250 and 4000 walkers, so an extrapolation in the inverse
population is not reliable at these sizes; a guide with the ground state's
charge statistics, validated on the exact 2³ torus, or a sampler with no
guide and no population, is what the scan needs.

## Prior art (not premises)

Trivedi and Ceperley 1990, Calandra Buonaura and Sorella 1998 (population
control bias in fixed-population projectors). Cited as prior art, not as
premises.

## Checks

The runner has two checks: the exact 2³ control at both penalties with
independent runs; the fixed-guide grids with the concavity test and the
gap (reported). The fresh run takes about 28 minutes.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the supplied model on 4³ and 6³ with the stated projector settings.
- **N2 — Independence:** self-checked; the 2³ control is internal to this runner.
- **N3 — Imports:** the clauses, charge mass and guide are supplied, not framework admissions.
- **N4 — Dependencies:** open and draft PRs are cited, not relied on.
- **N5 — Resolution:** finite Monte Carlo with heuristic errors and a guide-dependent bias that this block measures.
- **N6 — Residuals:** the guide-independent scan above; 8³ and larger.
- **N7 — Counterroutes:** other guides, populations and estimators remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

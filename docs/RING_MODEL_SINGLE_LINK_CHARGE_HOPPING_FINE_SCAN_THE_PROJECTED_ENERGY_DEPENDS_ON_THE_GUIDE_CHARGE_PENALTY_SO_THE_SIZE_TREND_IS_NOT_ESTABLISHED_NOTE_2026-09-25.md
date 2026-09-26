---
claim_id: ring_model_single_link_charge_hopping_fine_scan_the_projected_energy_depends_on_the_guide_charge_penalty_so_the_size_trend_is_not_established_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Draft, not for landing: the runner's consistency check fails and this note preserves the evidence. Supplied link-qubit model with the ring clause at V = 0, g = 1, the single-link term -t sigma^x and the charge mass M = 2 (open PR 9263), on 4^3-10^3 tori. Exact: E0 is concave in t, so <sigma^x> never decreases and second differences of exact energies are never negative; central and second differences check against exact diagonalization on 2^3. Finite: a 0.05 grid in t with the guide's charge penalty interpolated between values tuned on 4^3 gives link expectations that miss open PR 9263's at t = 0.25 and 0.5 on 6^3 by 3.7 and 3.4 standard errors; outside the runner, the projected energy at fixed t = 0.35 on 6^3 differs by 1.22 +- 0.16 between penalties 1.0 and 1.2, so the fixed-population bias depends on the guide and the grid's differences mix two guides. The slopes and their size dependence printed by the runner are therefore not established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ring_model_single_link_charge_hopping_fine_scan_of_the_link_expectation_across_the_rapid_change_2026_09_25.py
---

# Fine scan of single-link charge hopping: the projected energy depends on the guide's charge penalty, so the size trend is not established

**Date:** 2026-09-25
**Type:** bounded_theorem (draft, not for landing)
**Status:** one of the runner's three checks fails; preserved as evidence of a guide-dependent population bias and as the plan for a corrected scan; unaudited.

## Result

Open PR 9263 found that, at charge mass `M = 2`, the link expectation
`⟨σ^x⟩` rises fastest between `t = 0.25` and `0.5`. This block measured the
ground energy on a grid of step 0.05 in `t` on 4³, 6³, 8³ and 10³, to see
whether that rise sharpens with size. The guide's charge penalty `γ(t)`
was interpolated between the values tuned on 4³ in open PR 9263.

- **The consistency check fails.** Central differences of step 0.1 on the
  grid reproduce open PR 9263's link expectations on 4³ within 2.5
  standard errors, but on 6³ they lie `3.7` and `3.4` standard errors below
  at `t = 0.25` and `0.5` (`0.0913 ± 0.0019` against `0.1016 ± 0.0020`,
  `0.4491 ± 0.0015` against `0.4562 ± 0.0015`).
- **The cause: the fixed-population bias depends on the guide.** Outside
  the runner, two seeds on 6³ at fixed `t = 0.35` give projected energies
  `−202.479 ± 0.139` with penalty `γ = 1.0` (the grid's interpolated value)
  and `−203.697 ± 0.086` with `γ = 1.2`, 7.5 standard errors apart; at
  `t = 0.15`, `−190.303 ± 0.052` with `γ = 1.2` and `−190.442 ± 0.040` with
  `γ = 1.5`. The mixed energy estimator is exact for any guide only for an
  infinite population; with 1920 walkers its bias depends on the guide and
  grows with the torus. The grid changes `γ` between the two energies of
  each difference, and the change enters the differences. With one penalty
  for both energies, the same probe gives `⟨σ^x⟩(0.25) = 0.1033` on 6³,
  consistent with open PR 9263.
- **What the grid still shows.** The exact 2³ control passes, and no
  second difference on any torus falls below zero by more than four
  standard errors, as concavity requires. On every torus the largest
  printed slope lies between `t = 0.35` and `0.45` (on 8³ and 10³ at the
  lower edge of the scanned window). The printed slopes, and
  their apparent fall with size (`2.30`, `2.18`, `2.08`, `1.81` on 4³ to
  10³), mix guides and are not established.

## Setting and decision points

- **D-gauss, D-ring (landed).** Spin-1/2 link fields `σ = ±1` on the cubic
  `L³` torus and the clause `−g Σ_p (U_p + U_p†)` at `V = 0`, `g = 1`.
- **D-hop (open PR 9263).** The single-link term `−t Σ_l σ^x_l` and the
  charge mass `M Σ_v Q_v²`, `Q_v = div_v / 2`, at `M = 2`. A decision point of
  the supplied model, not adopted.
- **The projector (method).** The compiled sign-free projector of open PR
  9263 with fixed populations of 1920 walkers, time step 0.05, projection
  30 per run; four seeds on 4³, three on 6³, 8³ and 10³; walkers from
  loop-move samples of the zero-winding ice sector. The guide's charge
  penalty `γ(t)` interpolates linearly between `1.2, 0.7, 0.5, 0.3` at
  `t = 0.25, 0.5, 0.75, 1` and is held at `1.2` below `t = 0.25`.

None is adopted.

## Theorem 1 — what an energy grid gives exactly

1. **Hellmann–Feynman.** `⟨σ^x⟩(t) = −(1/N_l) dE_0/dt`.
2. **Monotone link expectation.** `E_0(t)` is the minimum over states of
   functions linear in `t`, so it is concave and `⟨σ^x⟩(t)` never decreases;
   its slope is the static link susceptibility
   `(2/N_l) Σ_{n>0} |⟨n|Σ_l σ^x_l|0⟩|² / (E_n − E_0) ≥ 0`.
3. **Differences.** The central difference of step `δ` equals `⟨σ^x⟩(t)` up
   to `(δ²/6) d²⟨σ^x⟩/dt²`, and the second difference equals the slope at a
   point of `(t − δ, t + δ)`, so for exact energies it is never negative.

These hold for exact energies. For projector energies they hold only when
the bias of the energies is the same function of `t` on both sides of a
difference, which a changing guide breaks. ∎

## Diagnostic 1 — exact 2³ control

With the single-link term on the six links at one vertex (184320 states),
single long runs (4000 walkers, 12000 generations) give `−9.12715`,
`−9.20903` and `−9.31223` at `t = 0.3, 0.4, 0.5` against the exact
`−9.128109`, `−9.208058` and `−9.312178` (`+1.3`, `−1.5`, `−0.1` standard
errors); the central difference gives `Σ ⟨σ^x⟩ = 0.9254 ± 0.0061` against the
exact `0.9203`, and the second difference `2.132 ± 0.178` against `2.417`.

## Diagnostic 2 — the failed consistency check

| torus | `t` | grid (step 0.1) | open PR 9263 | deviation |
|---|---|---|---|---|
| 4³ | 0.25 | 0.1063 ± 0.0007 | 0.1065 ± 0.0010 | −0.1 σ |
| 4³ | 0.5 | 0.4304 ± 0.0008 | 0.4378 ± 0.0028 | −2.5 σ |
| 4³ | 0.75 | 0.6693 ± 0.0004 | 0.6681 ± 0.0006 | +1.6 σ |
| 6³ | 0.25 | 0.0913 ± 0.0019 | 0.1016 ± 0.0020 | −3.7 σ |
| 6³ | 0.5 | 0.4491 ± 0.0015 | 0.4562 ± 0.0015 | −3.4 σ |
| 6³ | 0.75 | 0.6695 ± 0.0005 | 0.6668 ± 0.0011 | +2.3 σ |

Open PR 9263 used one penalty for the three energies of each difference;
this grid used the interpolated penalty at each energy.

## Diagnostic 3 — the grid as printed (not established)

The runner prints `⟨σ^x⟩(t)` from central differences of step 0.05 and
slopes from second differences of step 0.1 on every torus. On 4³ the curve
rises from `0.08` at `t = 0.2` to `0.69` at `0.8` with its largest slope
`2.30 ± 0.04` at `t = 0.45`; the largest slopes on 6³, 8³ and 10³ are
`2.18 ± 0.06` (`t = 0.40`), `2.08 ± 0.07` (`0.35`) and `1.81 ± 0.06` (`0.40`).
At small `t` the larger tori print link expectations below the 4³ values
(at `t = 0.30`: `0.131`, `0.099` and `0.088` on 4³, 6³ and 8³), the pattern
the guide dependence produces. None of these numbers is claimed.

## What a corrected scan needs

- Evaluate both energies of each difference at one charge penalty, or
  obtain `⟨σ^x⟩` from the same-penalty pair `E(t ± δ)` at every grid point.
- Tune the penalty on each torus, not only on 4³, or check the energy's
  dependence on it at each size.
- Raise the population where the dependence persists, and keep the exact
  2³ control with independent runs.

## What this does not do

- It claims no slope, size trend, crossover or transition.
- It does not revise open PR 9263's numbers, which used one penalty per
  difference; the same-penalty probe here agrees with its `t = 0.25` value
  on 6³.
- It adopts no clause, charge mass, guide or method.

## Prior art (not premises)

Trivedi and Ceperley 1990, Calandra Buonaura and Sorella 1998 (population
control bias in fixed-population projectors); Fradkin and Shenker 1979.
All cited as prior art, not as premises.

## Checks

The runner has three checks: the exact 2³ control (passes); the
consistency with open PR 9263 (fails, as above); the scan with the
concavity test (passes). The fresh run takes about two hours and ten
minutes.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the supplied model on the stated tori and projector settings.
- **N2 — Independence:** self-checked; the guide-dependence probe ran outside the runner.
- **N3 — Imports:** the clauses, charge mass and guide are supplied, not framework admissions.
- **N4 — Dependencies:** open PRs are cited, not relied on.
- **N5 — Resolution:** finite Monte Carlo with a guide-dependent bias that this block exposes.
- **N6 — Residuals:** the corrected scan above.
- **N7 — Counterroutes:** other guides, populations and estimators remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

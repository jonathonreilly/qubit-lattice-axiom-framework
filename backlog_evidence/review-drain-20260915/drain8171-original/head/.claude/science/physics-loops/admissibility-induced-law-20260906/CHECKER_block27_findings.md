# Refuting pass — block 27 (supervisor-run, disjoint machinery; 2026-09-16)

Routes compared (control `specs/supervisor_control_block27.py`, refuting pass `specs/supervisor_control_block27_refuter.py`, outputs in `.out.txt`):

| item | runner's / control's route | refuting route | result |
|---|---|---|---|
| the sensitivity constant (T1d) | the proof's chain: `∫|∂f| ≤ (A/κ)^{1/2}|δ| ≤ |δ|/√3`; quadrature on a `300 × 300` grid at `300` random pairs (`0.2499` per unit) | Monte Carlo `E[(1 − f'/f)^+]` at `40` random pairs with `10⁵` samples each | `0.2509` per unit, inside `0.2887`; the small-`|V|` value `1/4` is the maximum seen on both routes |
| the contraction (T2) | `D_{t+1} ≤ √3β D_t` from the sensitivity | two runs from antipodal planes on a `64 × 64` plane coupled site by site by the maximal (overlap) coupling of the two kernels, built by rejection from the densities; `20` levels | ratios `D_{t+1}/D_t` of `0.33–0.38` (`β = 0.3`), `0.51–0.57` (`0.5`), `0.58–0.65` (`0.577`): about `1.1β`, inside `√3β = 0.52, 0.87, 1.00` |
| the one-site rate (T3) | `E[s_{t+1}·e | s_t] = A(3β)(s_t·e)` symbolically | `2·10⁴` independent one-site chains at `β = 0.5` for `6` levels | `0.438, 0.198, 0.087, 0.038, 0.015, 0.009` against `A(1.5)^t = 0.438, 0.192, 0.084, 0.037, 0.016, 0.007` |
| the reach (T4) | `A(δ)/δ ≥ 1/3 − δ²/45` by series and exact enclosure | the mean difference and `2·TV` per unit at `V = 0`, `|V'| = 0.05, 0.2, 0.5` by Monte Carlo | mean difference `0.3333, 0.3324, 0.3279` (the lower bound to four digits); `2·TV` per unit `0.4999, 0.4990, 0.4939` |

Findings: none against the theorems. One tooling slip folded before the outputs were recorded: the refuter's sampler degenerated at exactly zero concentration (the frame built from `V/|V|` vanishes), which the `V = 0` check exposed (`2·TV` per unit came out `0.017` instead of `0.5`); a direct uniform draw at zero concentration fixed it, and the control's simulations never hit exactly zero.

Attempts to refute (nothing refuted): the sign of `1 − 3A/κ − A²` near `κ = 0` (`−2κ²/45`, the first non-cancelling term); whether the `κ²` terms of the series comparison cancel exactly (they do, so the lemma is not strict at second order); whether the per-site coupling may use only predecessor distances (the automaton draws the sites of a level independently given the previous level, as the coupling does); whether `1/√3` could be a threshold (block 26's runs at `β = 3, 6, 12, 24` lose the memory; T4 caps the route at `β = 1`). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.

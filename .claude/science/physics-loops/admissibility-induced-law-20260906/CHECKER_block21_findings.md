# Refuting pass — block 21 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (controls `specs/supervisor_control_block21_weak_coupling.py`, refuting pass `specs/supervisor_control_block21_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the total-variation response (W1) | the covariance identities, the series ratios, the derivative identity on a finite weighted space, symbolically | direct quadrature of `TV(P_h, P_{h+Δ})` on the sphere at 600 random `(β, h, Δ)` with `|h| ≤ 6`, `|Δ| ≤ 2`, `β ∈ {1/10, 28/100, 1, 3}` | the bound `β|Δ|/(2√3)` holds at every sample; worst ratio `0.866 = √3/2`, the slack predicted by the antipodal value `tanh(β/2)` |
| the eigenvalue bounds (W1 ii) | closed-form coefficient ratios `6/(n(2n−1))`, `3/(2n+1)` and the series to `n = 12` | `L'(x)` and `L(x)/x` on a grid of `60000` points in `(0, 60]` | both at most `1/3`, with `1/3` the limit at `0` |
| the decay bound's direction (W5) | the walk bounds on the `7³` box | the exactly solvable open chain: `⟨s_0·s_2⟩ = L(β)²` by a one-dimensional quadrature (the middle site integrates to `Z(|s_0 + s_2|)`), and `L(β) ≤ 2β/√3` (the line's `α`) for `β < √3/4` | consistent; the true decay `L(β)^r ≈ (β/3)^r` is faster than the bound |
| the fixed point (W3) | `D = (I − C)^{−1}`, `u* = Db`, the decreasing iterates on the `2³` window, exact | the `3×3×3` box by floating-point linear algebra; the centre's value against `α²/(2(1−α))` | `D ≥ 0`; the bound holds with room |
| the torus sum (W5 c) | the `6³` torus at `α = 9/10`, exact | `L = 1..10` in floating point | at most `((1+α)/(1−α))³` throughout |

Findings: none in the primary. The controls corrected the contract before the primary: a first route (`TV ≤ tanh(osc/4)`, threshold `artanh(1/6) = (1/2)log(7/5) ≈ 0.168`) was replaced by the variance route (`√3/6 ≈ 0.289`) after the sphere sweep showed the one-site response is about half the crude bound; the mean-absolute-deviation route, which would give `β/2` per unit change, was found maximal at zero field but not proved, and is recorded as not claimed.

Attempts to refute (nothing refuted): W1's use of the segment `h_t` when `h = 0` (the covariance is `I/3` there; the derivative identity holds for every `t`); the step from `Var_h(s·Δ) ≤ |Δ|²/3` to `σ ≤ |Δ|/√3` for `Δ` not aligned with `h` (the covariance is diagonal in the frame `(ĥ, e, e')` with all eigenvalues at most `1/3`); W3's Step 5 without a limit coupling (the bound at each time `t` uses only stationarity and the telescoping); W4(b)'s consistency identity for windows with exterior records read off the product density; W5(b)'s torus graph minus a site (row sums at most `α`; the torus distance in the walk count); the sum over three components in W5(a) (each covariance separately bounded, then summed). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.

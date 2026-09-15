# Refuting pass — block 23 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block23_complex_rotations.py`, refuting pass `specs/supervisor_control_block23_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the shift bound (P1) | the identities symbolically; the shift lemma on monomials; the solvable two-site instance | a heat-bath Monte Carlo estimate of `⟨s_0^1s_x^1 + s_0^2s_x^2⟩` on a `4×4` window with free boundary at `β = 1/2, 2` against the bound with the shift function at two values of `γ` | the bound dominates the estimate (`0.50` and `0.94` against `−0.009` at `β = 1/2`; `0.73` and `0.98` against `0.17` at `β = 2`) |
| the shift function's Lipschitz bound (P2) | the mean value bound symbolically; shell counts | every bond of the `24×24` torus with the torus distance, for `R = 3, 8, 12, 16` (wrapping past the half-side) | holds on every bond |
| the bond sum (P2 c) | `Σ_{j≤R} 8j/(1+j)² ≤ 8H_R` exactly; the series ratios | the exact sum over bonds of `cosh(a_y − a_z) − 1` on `Z²` for `R ≤ 40` at `γ = 7/10` against `2γ²cosh γ(1 + 8H_R)` | below the bound throughout; largest ratio `0.10` (the shell bound has a factor ten of room — not claimed) |
| the harmonic bound (P3) | `log(1+u) ≥ u/(1+u)` symbolically | `H_R ≤ 1 + log R` at `R = 10^k`, `k ≤ 6` | consistent |
| the optimization (P3) | the maximizer and maximum symbolically; the two branches | a grid of `10⁵` points on `(0, 1]` at `β = 1/10, 1, 10` | agrees to six digits with `5/(512β)` (and with `1 − 128β/5` below `5/256`) |
| the torus consequence (P4) | the shell sum at `κ' = 1/2, 1` for `L ≤ 40` (termwise) | direct shell sums for `L ≤ 200` | consistent |

Findings: none in the primary. Observations recorded: the bond-sum bound is loose by about a factor ten (the sup-norm shell count and the crude `cosh t − 1 ≤ (t²/2)cosh γ` both lose), so the exponent `κ(β)` could be improved by that factor by a finer count; not claimed. The Monte Carlo estimate on the `4×4` window at `β = 2` (`0.17` for the two-component correlator at distance `√18`) is far below the bound, as expected of a bound uniform in the volume.

Attempts to refute (nothing refuted): the shift lemma's hypothesis for the bond weights with an exterior endpoint (entire and periodic in the interior angle; the exterior angle is a constant); the modulus step when `ρ_yρ_z cos(φ_y − φ_z) < 0` (the inequality `cos θ cosh τ ≤ cos θ + (cosh τ − 1)` needs no sign of `cos θ`; and `ρρ' ≤ 1` is applied to the nonnegative correction only); the torus shells at `j = L` (`4L − 1 ≤ 8L`); the requirement `Λ ⊇ {d < R}` for windows (so the formula vanishes at exterior sites); the sum over the three component pairs (`2s·s'` is their sum, no isotropy used). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.

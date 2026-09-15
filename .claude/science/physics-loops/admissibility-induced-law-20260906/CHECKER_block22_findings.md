# Refuting pass — block 22 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block22_return_sum.py`, refuting pass `specs/supervisor_control_block22_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| the closed-walk counts (V1) | enumeration of all `6^{2n}` walks for `n ≤ 3`; the Vandermonde form against the multinomial sum for `n ≤ 12` | direct enumeration of `(a, b, c)` for `n ≤ 300` (the `T_300` term has `284` digits) | equal throughout |
| the cube integrals (V1) | exact cosine moments, `n ≤ 6`, odd integrals zero | — (the walk-count identity is the second route) | consistent |
| the tail bound (V2) | derivative identities and sample points; the Gaussian integral | the bound against the exact `P_{2n}` (as floats) for every `n ≤ 1000`; the symbol's lower bound on a `41³` grid of the cube | dominates throughout; slack `1.14` at `n = 1000` |
| the size of the true tail (V3) | the majorant `T_1 < 181/10⁴` at `N = 1000` | a fit `P_{2n} ≈ c n^{−3/2}` from `n = 800..1000` (`c = 0.2332`, spread `2·10^{−5}`), tail `2c/√N = 0.01475`; `S_N + 2c/√N = 1.5163854` against the classical value `1.5163861` (reference only, never in the certificate) | the majorant exceeds the true tail by about `20%`; the certificate's margin (`2·76/100 − S_N − T_1 ≈ 3.5·10^{−4}`) is small but exact |
| the exponential majorant (V3) | `e^{−x} ≤ 1 − x + x²/2` symbolically; `197/225` exact | `log((197/225)^{N+1}) = −133.0 ≥ −2(N+1)/15 = −133.5 ≥ −4(N+1)/(3π²) = −135.2`; `225/14 = 2/(1 − 197/225)` | consistent |

Findings: none in the primary. Three first-run failures of the runner were fixed before the census: the expected integer decimal of `T_1²` had been taken from the control's `N = 2000` run (the runner uses `N = 1000`); a decimal inside a runner string tripped the floating-point self-scan; and the note's proof of V1 used the phrase "monotone convergence", whose substring is on the lane's forbidden list (reworded to the monotone limit theorem, named under Imports).

Attempts to refute (nothing refuted): the paired-series step for negative `φ` (the terms `(1 + φ)φ^{2m}` are nonnegative, so termwise integration is legitimate; the odd integrals vanish); the two-region step (the shift by `(π, π, π)` maps the cube to itself modulo `2π` and negates `φ`); the use of `π ≥ 3` in `T_1` (it only enlarges the majorant); whether `N = 1000` suffices (`2·76/100 − S_N − T_2 = 0.018363 > T_1 = 0.018016`: it does, with little room; `N = 2000` would give `77/100` with room but costs two and a half minutes per run); the lower bound (`S_N/2 = 0.7508 > 0.75`). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.

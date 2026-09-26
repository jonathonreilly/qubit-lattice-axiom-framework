# Referee: nonlinear record motion and lasting waves, attempt 1

Attempt `w-macbookpro9927a-j0bdc`. The ring rule and the site-factorized mean field are recomputed here. The attempt's script is not imported.

The rule is the one named in the task. A record of speed `v` and gap `g` takes `u = min(v+1, V, g)`, then slows by one with probability `r`, and advances by the final move. Its new speed is that move.

## Verdicts

**Deterministic rule, r = 0.** Steps 1–4 hold. After one step the gap is at least the leader's speed. A record saturated at that time stays saturated and copies its leader's move one step later. Saturation at step 0 need not persist: gaps `(0, 2)`, speeds `(0, 2)`, `V = 2`, both start saturated and record 0 is not saturated at the next step.

Step 5 is the pair of implications actually used. If some record never saturates, then eventually every record moves `V`, so `N(V+1) ≤ L`. If every record saturates, then `N(V+1) ≥ L`. Below density `1/(V+1)` every orbit therefore reaches the free set and translates by `+V`. Above it, every orbit reaches the jam set and the occupied set translates by `-1`. On the equal line the two sets are the same state, every gap equal to `V`, and the two translations agree. The free set is empty on the jam side and the jam set is empty on the free side, because the gaps cannot all lie on the wrong side of `V`.

On every state of the rings `V = 1, 2, 3` with `L ≤ 9, 8, 7` (130592 states) the orbit enters that rigid motion. The longest entry observed there is 3 steps. That length is not claimed for every ring. The same motion holds on 54 random states of `L = 40, 60, 80`, seed `20260926`.

**Random rule, 0 < r < 1.** The support of one step is every subset of the records whose move before slowing is at least 1, and all-slowdown never raises a speed. On 64 rings and 41944 states (`V = 1` with `L ≤ 8`, `V = 2` with `L ≤ 7`, `V = 3` with `L ≤ 6`) every state reaches one reference state, and the forward closure of that state has period 1. The reference is the stopped jam, except for one record with `min(V, L-1) ≥ 2`, which cruises in speeds `{m-1, m}` and returns to a marked state in both `L` and `L+1` steps. One common-speed configuration, gaps `(3, 3, 3)` and speeds `(2, 2, 2)`, drops its common speed when a single record withholds the slowdown, as in the lowering step.

The convergence theorem for a finite chain with one aperiodic closed class is imported, not re-proved. Given that import, rotation invariance makes every nonzero density mode decay on each fixed finite ring. The author's graph of 1184754 states was not rebuilt.

**Mean field.** The uniform fixed point and the symbol match unit differences of the ring map at `(V, r, ρ, L) = (1, 1/4, 1/3, 5)`, `(2, 1/4, 1/4, 7)`, `(2, 0, 3/20, 7)` and `(3, 1/2, 1/10, 9)`. For `V = 1` the density closes on nonnegative weights `r`, `(1-r)(1-ρ)`, `(1-r)ρ`. With `p = 1-r`,
`1 - |λ|² = 2p(1-p)(1-cos k) + 4p²ρ(1-ρ) sin² k`,
so every `k ≢ 0` is strictly damped when `0 < r < 1` and `0 < ρ < 1`. At `r = 0` the identity vanishes only at `k ∈ {0, π}`.

For `V ≥ 2` the speed weights include negative values. At `r = ρ = 1/4` there are 3, 6 and 15 of them for `V = 2, 3, 5`, and the least for `V = 2` is `-111/880`. All roots lie strictly inside the unit circle at the 144 stated rational points. At the three stated points, Schur–Cohn fails and the resultant with the reciprocal polynomial is nonzero, so a root lies outside. The floating moduli are about 1.0456, 1.0199 and 1.0064.

**What lasts.** The hypothesis of block 122 that fails is linearity: the move is a minimum with the gap. At `r = 0` the lasting disturbance is still rigid transport of the occupied set. Below density `1/(V+1)` the pattern travels at `+V`. Above it, the pattern travels at `-1`, against the records. That jam wave is not a velocity any record carries. It is not an oscillation. For `0 < r < 1` the finite-ring chain has no second closed class.

## What stays open

The autocorrelation runs at fixed wave number, and the floating-point scan of the mean-field modulus over the `(V, r, ρ)` grid, were not rebuilt. Decay as `L → ∞` at fixed `k` is not proved. The block 122 and block 123 source hashes were not re-checked. The transient length is not bounded for every ring.

## Result

HIT: confirmed. At `r = 0` the occupied set eventually translates by `+V` or by the jam wave `-1`. For `0 < r < 1` every executed finite ring has one aperiodic closed class. The mean-field linearization is not always damped.

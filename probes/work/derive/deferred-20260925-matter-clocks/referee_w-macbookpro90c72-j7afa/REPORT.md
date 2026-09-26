# Referee: formation-clock dephasing, attempt 1

Attempt `w-jonathonsmac4f50-j324c`. The characteristic function and the resonant clocks are recomputed here. The attempt's script is not imported. No formation law is derived from the axioms.

A qubit precesses at frequency `ω > 0`. A supplied nonnegative hazard forms the record at a random time. The formation-weighted Bloch average keeps a perpendicular part equal to the characteristic function `z = E[e^{iωτ} | τ < T]`.

## Verdicts

**Constant clock.** Conditioning the hazard `f` on formation before `T` gives
`z = f [1 − e^{−(f−iω)T}] / [(f − iω)(1 − e^{−fT})]`.
Its real and imaginary parts are the cosine and sine averages, so the Bloch average is `r_∥ + (Re z) r_⊥ + (Im z) ĥ × r_⊥`.

**Joint bound.** With `x = f/ω` and `κ = fT`,
`|z|² = x² (1 − 2e^{−κ} cos τ + e^{−2κ}) / ((1+x²)(1−e^{−κ})²)`.
The comparison with `(1+e^{−κ})²` differs by `2x² e^{−κ}(1+cos τ)` over a positive denominator. Also `|x−i| ≥ 1` and `1+e^{−κ} ≤ 2`, so `|z| ≤ 2x/(1−e^{−κ})`. The function `(y+1)(1−e^{−y})−y` vanishes at 0 and has derivative `y e^{−y} ≥ 0`, hence `1/(1−e^{−y}) ≤ 1+1/y`. Therefore
`|z| ≤ 2(f/ω + 1/(ωT))`
for every `f, T > 0`. Along every path with `(f, 1/T) → (0, 0)`, `z → 0`.

**Sharpness.** At fixed `T` and `f → 0`, `z → (e^{iωT}−1)/(iωT)`. At `ωT = π` the modulus is `2/π`, equal to the `1/(ωT)` term. At fixed `f` and `T → ∞`, `z → f/(f−iω)`, with modulus `f/√(f²+ω²)`, at most the `f/ω` term and at least half of it for every `f`.

**Bounded variation.** Integration by parts gives `ω|z| ≤ w(0⁺) + w(T⁻) + TV(w)`. A monotone density contributes `2 max w`. A unimodal density does the same: the rise to the peak and the fall off it sum to `2 max w − w(0⁺) − w(T⁻)`, and the endpoint terms cancel that deficit. The linear hazard `βt e^{−β t²/2}` has derivative proportional to `1−β t²`, so it peaks at `t = 1/√β` with height `√β e^{−1/2}`.

**Resonance.** On a whole number of precession periods, `w = (1+cos ωt)/T` is a probability density and `z = 1/2`. The hazard `f = m w/(1−m W)` has survival `1−m W`, so its conditioned formation density is `w`. Since `1+cos ≤ 2` and `W ≤ 1`, `sup f ≤ 2m/(T(1−m))`, which tends to 0 as `T → ∞` while `|z|` stays `1/2`. A hazard that is on only while `cos ωt > 0` tends, as its height tends to 0, to the uniform law on those half-periods, and `z → 2/π`. One exact period was integrated and has the same limit.

## What stays open

Whether any supplied hazard meets the rest of the axioms was not taken up. Many-site clocks and record-determined neighbour events were not built. The sixty-four numerical spot checks were not rebuilt; the constant-clock inequality is proved for every positive `f` and `T`.

## Result

HIT: confirmed. Dephasing is the decay of the formation-time characteristic function. The constant clock dephases in the joint slow and long limit. Resonant hazards do not.

# Referee: delay-of-the-rate-field-with-the-curvature-member a1

Worker `w-macbookpro90c72-jf4c8` (`grok-4.6`). Author `w-jonathonsmac4f50-j03c0` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed partial, at second order around the uniform state. The rate is a constraint. A change in a body's energy moves the clocks, and therefore a slow packet's fall, at the same label time. The only travelling modes are the two transverse traceless strains, and a body at rest does not source them.

## What was checked

- **The member.** `R₁` and `R₂` are unchanged by `h → h + pξ + ξp`. On the scalar `h = (1 − p̂p̂)φ`, `R₁ = 2p²φ` and `R₂ = ½ p² φ²`. On `h = 2λ I` the constraint is `p² λ = e/(4 K w̄)`.
- **The equations, with `p` along one axis.** The rate equation is `2 K w̄ p² φ = e`, with no time derivative. The traceless strains satisfy `(4α/w̄) ä = −K w̄ p² a`, so `speed² = K w̄²/(4α)`. The longitudinal relabelling has no potential. Eliminating it gives
  `u = −e/(4 K w̄ p²) + α(α+3β) ë / (K² w̄³ (α+β) p⁴)`.
- **The two ratios.** At `α + 3β = 0` the second-derivative term drops. At `α + β = 0` the relabelling equation forces `ė` to be constant, so a jump has no solution.
- **A smooth switch-on.** At label time `0⁺`, `δu = 6α(α+3β) Δe / (K² w̄³ (α+β) p⁴ τ²)`. After the step, the jump of `u` is the Poisson field `−Δe/(4 K w̄ p²)`.

The `48×48` slice was not rebuilt. The fall `−E∇u` is the supplied slow-packet law; what was checked is that `u` itself is fixed by `e` and `ë` at the same label time.

# Referee report: J:derive:wind-force-on-an-absorbing-sphere:a4

- **Author:** `w-macbookpro90c72-j9625` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-je812` (`grok-4.6`). Different model family.
- **Checks:** the circle identity and the Legendre integrals, recomputed. The author's script is not called. The flow past the sphere is not re-opened: the attempt does not solve it.

## The statement

Clause (C) re-draws the two contents uniformly on the pairs with a fixed sum. Linearised about the uniform law, a degree-`l` harmonic is multiplied by `μ_l = 4 ∫₀¹ u P_l(u)² du`. Momentum is conserved and the stress is halved, so in the product closure the stress relaxes at `3γρ`.

## Steps

**K1.** `|s₁| = |s₂| = 1` and `P = s₁ + s₂` give `|P|² = 2 + 2t` and `|P|/2 = √((1+t)/2)`. The same quantity is `P̂·s₁`. So both outgoing contents lie on one circle, and they are opposite each other.

**K2.** With `t` uniform on `[-1, 1]` and `u = √((1+t)/2)`, `2 E_t[P_l(u)²] = 4 ∫₀¹ u P_l(u)² du`. That integral equals `2 c_{⌊l/2⌋} c_{⌈l/2⌉}`, `c_k = (2k−1)!!/(2k)!!`, for every `l ≤ 12`. The first eight values are `1, 1/2, 3/8, 9/32, 15/64, 25/128, 175/1024, 1225/8192`.

**K3.** `μ₁ = 1` and `μ₂ = 1/2`. A record meets a re-draw at rate `6γρ`, so the degree-`l` rate is `6γρ(1−μ_l)`: `3γρ`, `15γρ/4`, `69γρ/16` for `l = 2, 3, 4`.

**K4.** The sphere's fourth moment is `(δ_{ij}δ_{kl} + δ_{ik}δ_{jl} + δ_{il}δ_{jk})/15`. A traceless quadrupole therefore puts `4εQ/15` into the pair's second moment. The two contractions of the outgoing tensor give `a = 1/5`, `b = 1/30`, and `E_t[s₁ᵀ g s₁] = 1`. The outgoing traceless piece is `4b εQ = 2εQ/15`, half the incoming piece.

**K5.** `l μ_l` is `1.257, 1.265, 1.269` at `l = 40, 80, 160`, against `4/π ≈ 1.273`.

## Verdict

The spectrum survives. It does not explain `K/K₀`: the attempt stops before the streaming operator and the absorbing-sphere problem, and nothing here fills that gap.

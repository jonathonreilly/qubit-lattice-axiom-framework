# Referee: odds field on the massless surface, a1

Author `w-macbookpro90c72-jcd49` (claude-opus-5-5). Referee `w-macbookpro90c72-jf3a8` (grok-4.6).

The cubic coefficient is exact:

`u = 90 l1² (1 − 36 l2) / (1 − 6 l2)`.

On `5p = 7q + 4r` this is `(5/2)(4r − 7q)/(r − q)`, and at `(3,1,2)` it is `5/2`.

## What was recomputed

1. **Channels.** `(Wπ)(+e₁) = (T/6)(1 + 3 l1 v + 2 l2 D)` and `(Wπ)(e₂) = (T/6)(1 − l2 D)`, with `T = p+q+4r`.

2. **The map.** The normalized product over six neighbours, expanded with `v ~ t` and `D ~ t²`, matches
   `v′ = l1 S₁ + 3 l1³(Σv³ − S₁ Σv²) − 2 l1 l2(ΣvD − S₁ ΣD)` through order `t⁴`, and the quadrupole formula through order `t³`, on three neighbourhoods.

3. **Slaving.** The local sums turn the cubic into `−90 l1³ v³ + 60 l1 l2 v D`. With `D = 45 l1² v²/(1−6 l2)` this is `u v³` for the `u` above. On the surface, `l1 = 1/6`. At `(3,1,2)`, `l2 = 0` and `u/9 = 5/18`.

4. **Sign.** `u` has the sign of `(4r−7q)/(r−q)`. At `q = 2`, `r = 1` one has `4r < 7q` and `u = 25`. The sentence "positive iff `4r > 7q`" misses the region `r < q`.

5. **Far field.** `Lap(A/r) = A″/r`, so `A_ττ − A_τ = u A³` in `τ = log r`. The centre manifold through order 7 is `−u A³ + 3u² A⁵ − 24u³ A⁷`, and `(A⁻²)_τ = 2u − 6u² A² + …`.

The torus iteration and the shooting solution were not rebuilt.

`SUMMARY: confirmed - u is the displayed rational function of the weights.`

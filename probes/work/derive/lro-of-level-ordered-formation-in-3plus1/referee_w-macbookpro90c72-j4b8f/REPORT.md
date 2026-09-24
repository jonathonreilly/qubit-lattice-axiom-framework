# Referee: level-ordered formation in 3+1, a1

Author `w-macbookpro90c72-j9436` (claude-opus-5-5). Referee `w-macbookpro90c72-j4b8f` (grok-4.6).

## Steps

1. **S5 follows.** For `L = 3..8`, the test configuration has backward `|S|²` equal to 4 on 10 sites and 16 elsewhere, and forward `|S|²` equal to 0 on 3 sites, 4 on 6, and 16 elsewhere. The ratio of the two layer weights is `Z(4β)/Z(2β)⁴ = u³ cosh u / sinh³ u` with `u = 2β`. The odd Taylor coefficients of `sinh³ u − u³ cosh u` vanish at orders 3 and 5 and stay positive from order 7, so the ratio is below 1 for every `β > 0`. `Σ|S|⁴` differs by 192, which is the `−16β⁴/15` quartic.

2. **S7 follows.** The 3-cycle (all `e_z`; `e_x` at the origin; `e_y` at `e₁`) has exponent sum 1 for `L = 3..6`, so the kernel ratio is `e^β`. It is 0 for `L = 2`.

3. **S9 follows.** `Aff(N4) = 24` and `Aff(N7) = 48`. Of the fixed-point-free affine involutions, 0 of 191 (`L = 4`) and 0 of 475 (`L = 6`) pass the necessary condition for a positive-semidefinite crossing matrix. The light-cone graph has 7 of 621 at `L = 4`. Fixed-vertex involutions: 73 and 145.

4. **S11 follows.** `1 − |φ|² = (3/4)(1 − λ_FCC)`, so the linear covariance is even in `k`.

The four route obstructions are these facts: the layer marginal is not stationary, no diamond reflection gives Gaussian domination, tilted islands are not eroded, and the infrared bound is not supplied. No long-range order is proved, as the attempt says.

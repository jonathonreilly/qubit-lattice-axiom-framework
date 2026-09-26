# Referee: collisionless force between extended bodies, a3

Author `w-macbookpro90c72-j0662` (claude-opus-5-5). Referee `w-macbookpro90c72-j09b1` (grok-4.6).

The author's script was not imported. The 20-site body averages and the Gauss–Jacobi quadrature of `Φ` were not rebuilt. The single-site law is the stated input.

## What holds

Dirichlet moments are the rising-factorial ratios. The delta-method remainder of `E[Φ(W)]/((n+1)(n+2))` is `c/|x|₁ + O(|x|₁⁻²)`, with

`c = −3 + (direction of Φ) · (mean shift + covariance Hessian) / |Φ|`

at `ŷ = x/|x|₁`. The values are `−8` on `(1,1,1)`, `−481/81` toward `(1,2,2)`, and `167603/34322` toward `(28,1,1)`. On the diagonal the mean equals `ŷ`, the covariance piece is `−5`, and `−3 + −5 = −8`. These are not the quoted `−24`, `−16` and `+5.6`.

The leading magnitude is `m |x|₁²/|x|⁴`, with `m = 1, 2, 4` off a coordinate plane, on a plane, and on an axis. Times `r²`, the point-pair factors are 4, 4 and 3. A ball of radius 6 contains 925 lattice sites, and the pair-offset counts sum to `925²`.

`SUMMARY: confirmed — the 1/n remainder coefficients are −8, −481/81 and 167603/34322, not −24, −16 and +5.6.`

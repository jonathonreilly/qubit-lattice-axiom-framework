# Referee: nondegenerate stationary points of the pair bands, attempt 1

Attempt `w-macbookpro9927a-j546d`. The band derivatives and the degenerate-stationary ideal are rebuilt here. The attempt's script is not imported.

A band is `E = s1 eps(K0/2 + q) + s2 eps(K0/2 - q)`, with `eps(k) = (sum_a sin^2 k_a)^(1/2)` and each sign `±1`. The tested wave vectors are `tan K0 = (5/6, 18/5)` and `(5/6, 18/5, 1/2)`.

## Verdicts

**Derivatives.** In circle coordinates `C_a = cos 2k1_a` and `S_a = sin 2k1_a`, the gradient is `S_a/(2 e1) - S2_a/(2 e2)`, where `e_i` is the signed energy. The Hessian is the sum of the two single-record Hessians; the two minus signs from `k2 = K0/2 - q` cancel. Both formulas match direct differentiation to 40 digits, at `q = (1/4, -1/5)` for all four plane bands and at `q = (1/4, -1/5, 1/7)` for the positive space band.

**Certificate.** Off the cones, a degenerate stationary point would be a common zero of the circles, the two energy squares, the cleared stationarity equations, `z e1 e2 - 1`, and the numerator of `det Hess`. That denominator is a monomial in `e1, e2`, so it does not vanish on this set. The reduced Gröbner basis is `[1]` in the plane (2.1 s) and in space (46 s). The space numerator has total degree 10. A Gröbner basis `[1]` means the ideal is the unit ideal, so there is no common zero over `C`. That fact is the weak Nullstellensatz, imported and not re-proved.

Without the Hessian numerator the plane basis is not `[1]`, so the stationarity system itself is consistent over `C`. At `K0 = 0` the band `eps(q) - eps(-q)` is identically zero, and the same full system is not the unit ideal.

**Cones.** At the opposite cone the smooth record has squared gradient `139761000/606502321` in the plane and `2653455542/8714332815` in space, both below 1. The same square arises at the other record's cone. Near a cone, `eps = |y| + O(|y|^3)`, so `E = τ + s1|y| + t·y + O(|y|^2)` with `|t| < 1`. The gradient of that model does not vanish off the tip.

## What stays open

Real stationary points were not counted. The resultant degrees and the candidate-box counts inside T6 were not rebuilt. Persistence of the nondegeneracy to a neighbourhood of `K0` is the inverse-function step stated in block 143; that step was not re-proved.

## Result

HIT: confirmed. Every stationary point of every band pair off the cones is nondegenerate at both tested wave vectors, and both cone tilts are strictly below 1.

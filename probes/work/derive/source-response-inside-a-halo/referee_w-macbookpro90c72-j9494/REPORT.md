# Referee: source response inside a halo a5

Author `w-macbookpro90c72-j716e` (claude-opus-5-5). Referee `w-macbookpro90c72-j9494` (grok-4.6).

The gas is an imposed product state. Block 41's halo profile is assumed. Whether a formed record stays on the lump was not derived.

## Steps

1. **First order.** At `c₀ = 6/(p+q+4r)`, heat bath gives `-52/45`, `-21002/9207`, `-13866/12455`, `-79/72`. Metropolis gives `-26/9`, `-3337/504`, `-974/345`, `-284/105`. All eight are negative.

2. **Reversal.** Each heat-bath expression changes sign in a window of width `4·10⁻⁶` around the published root, and those roots are `1.38` to `2.09` times `c₀`. Metropolis stays negative at `c = 1/1000, 1, 10, 1000`. Its formula is `12 E min(1, W) − 2 E min(1, 1/W) − 12`, and `E min(1, W) ≤ 1`, so the coefficient is at most `-2 E min(1, 1/W)`.

3. **Density.** The exact first-order-in-`g` polynomial in `ρ₀`, rebuilt from the class distributions, starts at those constants. On `(3,1,2)` the heat-bath linear term is `317/1755`. None of the eight polynomials has a root in `(0,1)`.

4. **Formation.** At `c₀` a row of pair weights sums to 6. The outer shell of a cube of side `m` has one cube neighbour per site, and the first moment of the formation rate is `-z g m²(m+1)(5m+1)`. Shells of side 1 through 4 match that formula.

## Verdict

At the neutral scale the free record drifts down the gradient for both admitted acceptances, and only heat bath turns around above `c₀`. Formation on a held cube also moves the centre down the gradient.

`HIT: confirmed`.

# Referee: record-gas chessboard threshold a2

Author `w-macbookpro9927a-jfc7a` (claude-opus-5-5). Referee `w-macbookpro90c72-jdb5b` (grok-4.6).

Mayer–Vietoris for walls larger than six cells is the attempt's import. The random content-weight graphs were not rebuilt. The `g*` inequalities use the worst-case factors `m` and `Λ`.

## Steps

1. **Geometry.** Fixed polycubes of 1 through 7 cells are `1, 3, 15, 86, 534, 3481, 23502`. Around a site, the walls of at most six cells have sizes `{6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538}`. Every such wall is vertex-connected and edge-connected, and the `e₁` ray leaves within a quarter of the wall. Seven cells need at least 24 faces, so the count through 22 is complete. A plaquette meets 32 others at a vertex and 12 along an edge.

2. **Certificate.** At `x = 3/250`, below `30³⁰/31³¹`, the tree tail plus those counts sums to `0.0896`, under `1/2`. With no contents, `x = g^{1/2}`, so `g ≤ (3/250)² = 9/62500`. At `(3,1,2)`, `(5,2,4)`, `(12,1,2)`, and `(9,8,8)`, the published content bounds satisfy `g³ Λ⁶ (Λ/m)⁵ ≤ (3/250)⁶`, with `Λ` and `m` the largest and smallest of `6p, 6q, 6r` over `p+q+4r`.

3. **Half filling.** At the published half-filling values, including `5·10⁻⁶` with no contents, a framed box is above half filling at `H₊` and below it at `H₋`, and the fugacity window stays inside the Peierls bound.

4. **Translation.** On a framed `4³` box the bond identity holds for 20 configurations. Twenty-four explicit shifts of small B-regions drop the unlike-bond count by exactly the wall size.

## Verdict

The content-less gas is ordered for `g ≤ 9/62500` at `ζ = g⁻³`, and the published content and half-filling bounds sit in the same window.

`HIT: confirmed`.

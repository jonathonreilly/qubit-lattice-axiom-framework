# Referee report: J:derive:moving-jammed-clusters:a2

- **Author:** `w-jonathonsmac4f50-j7b51` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-jb732` (`grok-4.6`). Different model family.
- **Material:** the attempt's `ATTEMPT.md`. The checks below re-enumerate bonds, facets and shapes. They do not call the author's script.

## The statement

Under block 39's rule that every occupied-empty bond is visited at one rate, the attempt corrects the box's evaporation count, moves the switch between a largest stable size and a nucleation size from attempt a1's `x* ≈ 2.056` to `cp = 1`, and shows that a one-move balance cannot be a growth law on tied facets.

That is the statement. The dodecahedron census past the enumerated sizes is marked ASSUMED by the attempt, and is not used below as a theorem for every `R`.

## Step by step

**M1 (the box): holds.** For `L = 2..7`, every occupied-empty bond of the cube ends at an isolated site, there are `6L²` of them, and the rate is `E(L) = 24/(1+x³) + 24(L−2)/(1+x⁴) + 6(L−2)²/(1+x⁵)`. Corners contribute three bonds, edges two, faces one.

**M2 (a1's count): holds.** A corner of the 2-box has `k_s = 3` and three empty neighbours; the destination is isolated and has six empty neighbours. Visiting every bond at rate 1 gives forward/backward flux 1 against the static weight. Splitting one attempt per record over its empty bonds gives flux 2. That realization is not in detailed balance, and no bond-only rate can charge a corner bond at one third of a face bond.

**M3–M4 (the threshold): hold.** `E(L) = 6L²/(1+x⁵) + βL + γ` with `β` and `γ` carrying the sign of `x − 1`. At `x = 1`, `E = 3L²`. So `cp = 1` is the switch, and at the neutral scale that is `5p = q + 4r`. a1's linear coefficient vanishes on `x⁵ − 2x⁴ − 1 = 0`, which is a different root. Exact `G − E` on `L = 2..200`: at `(3,1,2)`, `x = 3/2`, `z_c = 16/825`; `(9/10)z_c` and `z_c` shrink at every size under the definition while a1's count grows (up to `L = 10`, or at every size); `(11/10)z_c` is repelling between 17 and 18. `(20,1,1)` at `(3/2)z_c` flips at 33 (definition) and 13 (a1). `(1,1,2)` at `(99/100)z_c` is attracting between 18 and 19.

**M5 (facets): holds.** On 19 normals, including signed ones, inside `|coordinates| ≤ 4`: layer `m` has `3 + #{i: |n_i| ≤ m}` recorded neighbours, and it has exactly one isolated destination, along the largest normal component, if and only if `m < h − k`. Tied facets have no such layer.

**M6 (shapes): holds on the enumerated range, and the octahedron holds in general.** For the octahedron the only one-move departures are the six tips, checked for `R = 1..8` and read off the same neighbour test the attempt gives: a non-tip keeps a side neighbour of the destination inside. Growth sites are `6 + 12R + (4R² − 4R)`. The dodecahedron's isolated-departure count is `6 + 12R` (`R` even) or `6 + 12(R−1)` (`R` odd) for `R = 2..8`, and its growth class of `j = 2` is quadratic. One-move evaporation is therefore `O(R)` against formation `Θ(R²)` on this range, so those shapes have no critical rate in the one-move accounting. The attempt already does not claim the dodecahedron formula past the sizes it enumerated.

**M7 (two moves): holds.** A top-layer record of `(111)`, `(110)`, `(100)`, `(221)` and `(331)` reaches an isolated site in two moves along the large normal component. The hop probability is `1/(1+x)` on `(111)` (`k_s = 3`, `k_t = 2`) and `1/(1+x³)` on `(110)` (`k_s = 4`, `k_t = 1`). Each move multiplies the static weight by `w_new/w_old`, so the path multiplies by `x^{−k_s}`: `x^{−3}`, `x^{−4}`, `x^{−5}` on `(111)`, `(110)`, `(100)`. The one-move zero on tied facets is not a zero of evaporation.

**M8 (what one move reaches, and what it reads): holds.** On the box, octahedron and dodecahedron at sizes 2..5, the arrangements reached in one move are exactly the occupied-empty bonds, and that number is twice the sum of the three projection areas. At `(3,1,2)`, `c = 1/2`, changing one record among aligned, opposite and orthogonal changes the surface law when the record is at depth 1 (3-box centre, 4-box core, 5-box site `(1,2,2)`) and does not change it at the 5-box centre.

## Verdict

The partial result survives. Per-bond evaporation switches at `cp = 1`, and a one-move balance is not a growth law for tied facets.

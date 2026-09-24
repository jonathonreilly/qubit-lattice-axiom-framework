# Referee report: J:derive:causal-clauses:a3

- **Author:** `w-jonathonsmac4f50-j2fc2` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-jec16` (`grok-4.6`). Different model family.
- **Checks:** every three-parent kernel on the six axis values, recomputed in exact rationals. The author's script is not called. Blocks 25 and 30 are not re-proved.

## The statement

On the line `(p, 1, 2)`, the single-parent total variation `α₃` that attempt a1 uses in its Dobrushin bound has the closed form `p²(p−1)(p+33)/((p³+33)(p²+p+32))` through the threshold, crosses `1/3` at `p* ≈ 3.75636`, and tends to `1` at strong coupling, so that bound cannot prove uniqueness there.

## Steps

**M1.** With weight `Π φ(a, u_j)` and `φ = p, q, r` for equal, antipodal and other, the largest total variation after changing one parent is `27/110`, `10650/63407`, `1/9`, `130/137` at `(3,1,2)`, `(5,2,4)`, `(2,1,2)`, `(40,1,1)`. So `3α₃` is `81/110`, `31950/63407`, `1/3`, `390/137`.

**M2.** On `p ∈ {5/2, 3, 7/2, 15/4, 4, 5}` the maximum is the configuration of three equal parents with one flipped to its antipode, and it equals the closed form. At `p = 8` and `p = 20` a different pair is strictly larger. The formula is not the maximum for every `p`.

**M3.** Brute force gives `3α₃ = 1455300/1457713 < 1` at `p = 15/4` and `21011234850/20991436937 > 1` at `p = 94/25`. On that interval the closed form is the maximum, and `3α₃ = 1` is the quintic `x⁵ − 2x⁴ − 64x³ + 132x² + 33x + 1056 = 0`. Its smallest positive root is `p* = 3.756359818320370`.

**M4.** The antipodal-flip formula itself tends to `0`. The true maximum is `0.97710`, `0.99952`, `0.99980` at `p = 100, 4165, 10⁴`. One parent can move a nearly deterministic child, so `3α₃ → 3`. No sharpening that still sums three single-parent influences stays below `1` at strong coupling.

**S5.** The ordered-phase counterexample is a citation of blocks 25 and 30 (`p ≥ 4165` gives two invariant laws). That theorem is not re-proved here. The attempt already marks the identification of those laws with two infinite-past limits as a soft joint. The arithmetic that `3α₃ > 1` at `p = 4165` is checked.

## Verdict

The boundary of the Dobrushin argument survives. Uniqueness by that bound stops at `p*`, and the bound cannot be repaired by a smaller constant.

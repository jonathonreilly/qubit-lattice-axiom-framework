# Referee report: corrigendum PR 8152, attempt 2

- **Author:** `w-jonathonsmac4f50-j90ec` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-jeb50` (`grok-4.6`). Different model family.
- **Checks:** own cross products and own Cayley rotations. The author's script is not called.

## The statement that survives

For unit vectors at angle `t ∈ (0, π)`, the note's frame `(q₁, u₂, q₁ × q₂)` has Gram `diag(1, 1, sin² t)` and determinant `sin t`. It is a rotation only when the vectors are orthogonal. The corrected frame `(q₁, u₂, q₁ × u₂)` is a rotation for every non-collinear pair, and the note's frame is that rotation times `diag(1, 1, sin t)`. Both frames are `SO(3)`-equivariant. The runner already normalises the second axis and then crosses, so it builds the corrected frame.

## Steps

**1.** The Lagrange identity gives `|q₁ × q₂|² = sin² t`. On the standard pair `q₁ = e₁`, `q₂ = (cos t, sin t, 0)` the written Gram and determinant match, and the corrected frame has `FᵀF = I` and `det F = 1`.

**2.** At `(1,0,0)` and `(3/5, 4/5, 0)` the cross square is `16/25` and the note determinant is `4/5`. At `(2/3, 2/3, 1/3)` and `(2/7, 3/7, 6/7)` the cross square is `185/441`. Both corrected frames are rotations.

**3.** Two rational Cayley rotations are in `SO(3)`. Each carries both frames: `F(gq₁, gq₂) = g F(q₁, q₂)`.

**4.** Line 91 of the note at `70f28178` writes `q₁ × q₂` and calls the result a rotation. Lines 131–135 of the runner divide the second axis by its length and then take `e₁ × e₂`.

## Verdict

The corrigendum survives. The repair is the normalisation of the third column. The runner does not need a change.

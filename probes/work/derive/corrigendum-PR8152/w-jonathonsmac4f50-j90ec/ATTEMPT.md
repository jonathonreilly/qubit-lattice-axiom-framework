# Corrigendum packet for PR #8152 (block 18): derivation attempt 2 of 2

Worker `w-jonathonsmac4f50-j90ec` (claude-opus-5), unit `J-derive-corrigendum-PR8152-a2`.

**Sources.**
- Block 18's note, runner and pack files at the PR #8152 head `70f28178`. The note is `docs/ADMISSIBILITY_RULE_MENUS_NEIGHBOUR_GENERATED_SUPPORTS_UNSOLDERED_AND_CUBE_ORBIT_MENUS_SOLDERED_BOUNDED_THEOREM_NOTE_2026-09-15.md`.
- The docs notes of PRs #8146–#8180 at their heads, for the use search.

**Provenance.**
- The defect was found by a grok worker (`J:attack-f:PR8152`, `w-macbookpro90c72-j427d`).
- It was confirmed by a claude-opus-5 worker (`J:confirm:J-attack-f-PR8152`, `w-jonathonsmac4f50-j741f`), which is my model family.
- No attempt a1 was on `origin/ai/probes` when I wrote this.

## 1. The statement attempted

**What the note says** (L90–92): "For non-collinear unit vectors `q_1, q_2`, the frame `F(q_1, q_2) = (q_1, (q_2 − (q_1·q_2) q_1)/|·|, q_1 × q_2)` is a rotation matrix with `F(g q_1, g q_2) = g F(q_1, q_2)` for `g ∈ SO(3)`."

**(a) What actually holds.**
- For unit `q_1, q_2` at angle `t ∈ (0, π)`, the written frame satisfies `F_noteᵀ F_note = diag(1, 1, sin² t)` and `det F_note = sin t`. So it is a rotation exactly when `q_1 · q_2 = 0`; that is the largest domain of the original.
- It is SO(3)-equivariant for every pair.
- **Minimal correction:** replace the third column by `q_1 × u_2`, where `u_2 = (q_2 − (q_1·q_2) q_1)/|·|`; equivalently, divide `q_1 × q_2` by `|q_1 × q_2| = sin t`.
- The corrected `F` is a rotation (`FᵀF = I`, `det F = 1`) for every non-collinear pair, is equivariant, and `F_note = F · diag(1, 1, sin t)`.

## 2. Steps

**S1 (PROVED; CHECKED `F1`).** The first two columns are orthonormal. The third, `q_1 × q_2`, is orthogonal to `span(q_1, q_2)`, which contains both of them. Its squared length is `|q_1|²|q_2|² − (q_1·q_2)² = 1 − cos² t` by the Lagrange identity. Hence `F_noteᵀ F_note = diag(1, 1, sin² t)` and `det F_note = sin t > 0`.

**S2 (CHECKED `F2`). Witnesses.**
- At the runner's executed pair `q_1 = (1, 0, 0)`, `q_2 = (3/5, 4/5, 0)`: `det F_note = 4/5`, and `F_note e_3 = (0, 0, 4/5)` has squared length `16/25`, so `F_note · S_0` leaves `S²`.
- At the pair `(2/3, 2/3, 1/3)`, `(2/7, 3/7, 6/7)`: `|q_1 × q_2|² = 185/441`.

**S3 (PROVED; CHECKED `F3`). The corrected frame.**
- `u_2` is a unit vector orthogonal to `q_1`, so `(q_1, u_2, q_1 × u_2)` is a right-handed orthonormal frame.
- `q_1 × q_2 = |q_2 − (q_1·q_2) q_1| (q_1 × u_2) = sin t (q_1 × u_2)`.
- Equivariance holds for both frames: for `g ∈ SO(3)`, `g(a × b) = ga × gb`, and the Gram–Schmidt step commutes with `g`. This is checked with two rational Cayley rotations at both pairs.

**S4 (CHECKED `F4`). The runner already builds the corrected frame.** Block 18's runner (L131–135) normalises `e2` and uses `e1.cross(e2)`. At the executed pair it equals the corrected `F` and differs from the note's formula. So the runner's B2, "a rotation matrix", verified the corrected frame. The defect is in the note's text only.

## 3. (b) Every use, with a verdict

### Block 18 note (#8152 @ `70f28178`)

| Lines | Statement | Verdict |
|---|---|---|
| L90–92 | the frame's definition and "is a rotation matrix" | needs its own repair: `q_1 × q_2` → `q_1 × u_2` |
| L4 (claim_scope, M2) | "`S(q_1, q_2) = F(q_1, q_2) S_0(q_1 . q_2)` with `F` the equivariant frame" | holds with the corrected `F`. With the written `F` the image `F S_0` leaves `S²` unless `q_1 ⊥ q_2` |
| L141–157 (M2 statement and proof) | frame-attached supports `S = F · S_0`; "every frame-attached assignment is covariant since `F` is equivariant" | holds with the corrected `F`. The proof uses equivariance, which holds for both, and the frame acting on `S²`, which needs orthogonality |
| L114–115 (table M2) | "the frame's equivariance executed (B2)" | unaffected: B2 executed the corrected frame (S4) |
| L185–196 (M4) | "the alphabet … is contained in the orbit of the seeds under compositions of the frame maps" | holds with the corrected `F` |
| L26–28 (result up front) | "can sit anywhere in a frame built from them" | unaffected (qualitative) |
| M1, M3, M5 (L121–137, L159–183, L199–) | the antipodal reduction, the cube orbits, Born on the antipodal pair | unaffected (no frame) |

**Block 18 runner (`70f28178`).** L131–140 already implement the corrected frame; no change is required. Optionally, add the note's formula as a negative control: `det = 4/5` at the executed pair.

**Block 18 pack files.** No occurrence of the frame formula (searched all pack files on the branch).

### Other notes of the campaign

| Note | Use | Verdict |
|---|---|---|
| Block 20 (#8154) L137, L166 | block 18's *classification* of the menus (continuous unsoldered, cube orbits soldered) | unaffected |
| #8169 (frame-attached four-point menu) L65, L127–129, L267 | block 18's classification of one- and two-neighbour supports; defines no frame by a cross product | unaffected |
| Block 26 (#8170) L82 | "block 18's menu" (unit vectors, unsoldered reading) | unaffected |
| Blocks 27–29 (#8171–#8173) | evidence addresses only | unaffected |

No other note of #8146–#8180 writes the frame formula. The search covered "frame", "`×`", "cross" and "Gram" over the fetched notes.

## 4. (c) The exact lines to change

- **Note L91:** "`F(q_1, q_2) = (q_1, (q_2 − (q_1·q_2) q_1)/|·|, q_1 × q_2)`" → "`F(q_1, q_2) = (q_1, u_2, q_1 × u_2)` with `u_2 = (q_2 − (q_1·q_2) q_1)/|·|`". Equivalently, the third column is `q_1 × q_2/|q_1 × q_2|`.
- **Note L92:** unchanged. The corrected frame is a rotation and is equivariant.
- **Runner:** no change required (L131–135 already implement the corrected frame). Optional negative control as above.

## 5. What would finish it

Nothing in (a)–(c) is open. The edit is the note owner's; no PR is touched here.

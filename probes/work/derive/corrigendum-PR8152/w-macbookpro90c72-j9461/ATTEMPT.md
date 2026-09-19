# Corrigendum for PR #8152 (block 18, menus note) — attempt a1

Worker `w-macbookpro90c72-j9461`, task `J:derive:corrigendum-PR8152:a1`.
Every finite claim below marked CHECKED is verified exactly (sympy, rationals, symbolic
angle) by `check.py` in this directory.

## 0. The defective sentence

`docs/ADMISSIBILITY_RULE_MENUS_NEIGHBOUR_GENERATED_SUPPORTS_UNSOLDERED_AND_CUBE_ORBIT_MENUS_SOLDERED_BOUNDED_THEOREM_NOTE_2026-09-15.md`,
lines 90–92 on the PR branch (the formula is line 91):

> **Frames.** For non-collinear unit vectors `q_1, q_2`, the frame
> `F(q_1, q_2) = (q_1, (q_2 − (q_1·q_2) q_1)/|·|, q_1 × q_2)` is a rotation matrix
> with `F(g q_1, g q_2) = g F(q_1, q_2)` for `g ∈ SO(3)`.

Write `t = q_1·q_2 ∈ (−1,1)`, `s = √(1−t²) > 0`, `ê_2 = (q_2 − t q_1)/s`, and

* `W(q_1,q_2) = [ q_1 | ê_2 | q_1 × q_2 ]` — the map as written at line 91;
* `F(q_1,q_2) = [ q_1 | ê_2 | q_1 × ê_2 ]` — the corrected map.

The third column is the only difference: `q_1 × q_2 = s·(q_1 × ê_2)`.

## 1. The exact statement attempted

(a) The minimal corrected statement, with the largest domain on which the sentence as
written is true, proved. (b) A verdict — unaffected / holds on the corrected domain /
needs its own repair — for every later statement of that note and of every other note of
the campaign (PRs #8146–#8180) that uses the frame. (c) The exact lines of the note and
of the runner that must change.

## 2. (a) The corrected statement and the exact domain

**Step 1 (PROVED, CHECKED A1/A3).** For every 3×3 matrix `M` and all vectors `a,b`,
`(Ma)×(Mb) = cof(M)(a×b)` where `cof(M) = adj(M)ᵀ`. This is a polynomial identity in the
15 entries; `check.py` expands both sides symbolically. For `g ∈ SO(3)`,
`adj(g) = det(g) g⁻¹ = gᵀ`, so `cof(g) = g` and `(g a)×(g b) = g(a×b)`.

**Step 2 (PROVED).** For `g ∈ SO(3)`: `(g q_1)·(g q_2) = t` and `|g v| = |v|`, so
Gram–Schmidt is equivariant, `ê_2(g q_1, g q_2) = g ê_2(q_1,q_2)`. With Step 1 this gives
`W(g q_1, g q_2) = g W(q_1,q_2)` **and** `F(g q_1, g q_2) = g F(q_1,q_2)`: *both* maps are
SO(3)-equivariant. Equivariance is therefore not the property at issue.

**Step 3 (PROVED, CHECKED B1–B5).** Let `r(t) = (e_x, t e_x + s e_y)` be the reference
pair. Then `F(r(t)) = I` and `W(r(t)) = diag(1, 1, s)`, symbolically in `t`. Hence, by
Step 2, for every non-collinear pair `(q_1,q_2) = g·r(t)`,

  `F(q_1,q_2) = g ∈ SO(3)` and `W(q_1,q_2) = g·diag(1,1,s) = F(q_1,q_2)·diag(1,1,√(1−t²))`.

Consequently `Wᵀ W = diag(1, 1, 1−t²)` and `det W = √(1−t²)`, both verified symbolically.

**Step 4 (PROVED, CHECKED B6).** `W(q_1,q_2)` is orthogonal ⟺ `1−t² = 1` ⟺ `t = 0`.
So the sentence at line 91 is true **exactly on the orthogonal locus** `q_1·q_2 = 0`, and
false at every other non-collinear pair. That locus is the largest domain on which the
original statement holds; it is a measure-zero subset of the configurations the note's M2
quantifies over ("two non-collinear recorded values"), so the statement is not repairable
by restriction — the formula must be corrected.

**Corrected statement (minimal change).** For non-collinear unit vectors `q_1,q_2`,

  `F(q_1,q_2) = ( q_1, (q_2 − (q_1·q_2) q_1)/|·|, (q_1 × q_2)/|q_1 × q_2| )`

is a rotation matrix with `F(g q_1, g q_2) = g F(q_1,q_2)` for `g ∈ SO(3)`.
Equivalent formula-free statement, which is what M2 actually uses (PROVED, CHECKED
B7/D4/E2): `F(q_1,q_2)` is the unique rotation carrying `r(q_1·q_2)` to `(q_1,q_2)`; it
exists because the two pairs have the same Gram matrix, and it is unique because a
rotation fixing two non-collinear vectors is the identity.

**Step 5 (PROVED, CHECKED F1/F2) — why every executed check missed it.** A map
`A(q_1,q_2)` is SO(3)-equivariant iff `A = F·M` for some matrix function `M` of the
invariant `t` alone: given equivariance, `M(t) := A(r(t))` and `A(g·r(t)) = g M(t) =
F(g·r(t)) M(t)`; conversely every `F·M(t)` is equivariant. The written map is the member
`M(t) = diag(1,1,√(1−t²))`. **No equivariance test can distinguish the two maps**, for any
pair and any rotation. The properties that separate them are orthogonality and the
determinant.

**Step 6 (CHECKED D1–D3) — the defect at the packet's own executed configurations.**
At the runner's pair `q_1 = (1,0,0)`, `q_2 = (3/5,4/5,0)` (`t = 3/5`):
`det W = 4/5`, `Wᵀ W = diag(1,1,16/25)`, and `W e_z = (0,0,4/5)`, which is **not on the
unit sphere** — so M2's "supports `S(q_1,q_2) = F(q_1,q_2)·S_0(q_1·q_2)`" would not be
sets of recorded values at all if read with line 91's formula. At the refuter's pair
`q_1 = (3/5,4/5,0)`, `q_2 = (0,5/13,12/13)` (`t = 4/13`): `det W = √153/13 = 3√17/13 ≈ 0.9518`.
At both, `W` passes the equivariance conjunct exactly and fails `Wᵀ W = I`.

## 3. (b) Every later statement that uses the frame

Branches fetched as `refs/probeaudit/<n>` for the 35 campaign PRs:

```
for n in $(gh pr list -R jonathonreilly/qubit-lattice-axiom-framework --state all --limit 100 \
  --json number,headRefName -q '.[]|select(.number>=8146 and .number<=8180)|"\(.number) \(.headRefName)"'); do :; done
git fetch origin "+refs/heads/<branch>:refs/probeaudit/<n>"   # one refspec per PR
git diff --name-only origin/main...refs/probeaudit/<n>        # that PR's own files
git grep -n -i frame refs/probeaudit/<n> -- <those files> | grep -vi framework
```

Note: on macOS `git grep -E '\bframes?\b'` matches nothing (the word-boundary escape is
not supported there) — it silently returns an empty sweep. Use plain `-i frame` and filter
`framework` afterwards, as above.

| statement | verdict |
|---|---|
| block 18 note line 4 `claim_scope` ("`F` the equivariant frame", no formula) | unaffected — formula-free, and `F` *is* equivariant |
| block 18 M2, lines 139–170 (stabilizer trivial; supports frame-attached) | holds on the corrected formula; the proof uses only "`F(q_1,q_2)` is the rotation taking the reference pair to `(q_1,q_2)`", which is Step 4's formula-free statement. With line 91 as written the statement is false (Step 6: the images leave the sphere) |
| block 18 M4, "the alphabet is generated by the formation" (lines ~194–208, "compositions of the frame maps") | holds on the corrected formula; repaired by the same one-character fix, no independent repair |
| block 18 M1 (antipodal), M3 (cube orbits 6/8/12/24), M5 (Born on the antipodal menu) | unaffected — no frame |
| block 18 runner `scripts/…_cube_orbit_menus_2026_09_15.py`, B2 lines 131–140 | unaffected — the runner **codes the corrected frame** (`e1.cross(e2)`, line 135) and checks `FᵀF = I`. No executed number changes |
| block 18 `GOAL_block18.md` line 11, RESULTS, STATE.yaml, TRACE_GATE, NO_GO_LEDGER | unaffected — formula-free |
| PR #8169 (block 19, frame-attached four-point menus) — the only other note whose subject is the pair frame | unaffected — block 18 is absent from its `upstream_dependencies` (minimal_axioms + the possibility-covariance note only), its citation manifest has no edge to block 18's claim, it states block 18 "is not a premise of the proofs below", and its Theorem 1 proves `S(g q, g q') = g S(q,q')` for `S(q,q') = {q, q', −q, −q'}` directly, without a frame map |
| #8170 block 26, #8171 block 27, #8178 block 34 ("frame") | unaffected — tangent frame on the sphere, a different object |
| #8173 block 29, #8180 block 35 ("frame") | unaffected — instantaneous / rotating measurement frame |
| #8159 ("frame", "reframe"), approach-registry and review prose across the campaign | unaffected — ordinary English |
| #8147 block 13 line 239, the only other file using `q_1, q_2` notation | unaffected — `(q_1² + q_1 q_2 + q_2²)²/9` for `k = (q_1,q_2,−q_1−q_2)`: momentum components, not a frame |

**No statement anywhere in the campaign needs its own repair.** The defect is confined to
one line of prose in one note, and no executed number moves.

## 4. (c) The exact lines that must change

1. **Required — block 18 note, line 91 only.** Replace the third column
   `q_1 × q_2` by `(q_1 × q_2)/|q_1 × q_2|` (equivalently `q_1 × ê_2`). This is the whole
   corrigendum.
2. **Runner: no change.** `scripts/admissibility_rule_menus_neighbour_generated_supports_and_cube_orbit_menus_2026_09_15.py`
   lines 131–140 already implement the corrected frame and already check `FᵀF = I`; the
   note's line 91 disagreed with the runner it cites, not the other way round.
3. **Recommended (not required for correctness).**
   - Note line 115: the table row reads "the frame's equivariance executed (B2)" while B2
     executes equivariance **and** orthonormality; by Step 5 only the second conjunct has
     purchase, so the row understates its own evidence.
   - `.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block18_menus.py`
     lines 38–44 and `…/specs/supervisor_control_block18_refuter.py` lines 57–62 code the
     corrected frame but **print only the equivariance conjunct** (control print (3),
     refuter R3). By Step 5 those two prints return `True` on the defective map as well
     (CHECKED D1/D2), so as written neither the control nor the refuting pass could have
     caught line 91. Printing `FᵀF = I` and `det F = 1` closes that blind spot.

## 5. What would finish it

Nothing is open in (a)–(c). The one judgment left to the note's owner is editorial: line
91 can be replaced either by the corrected formula or by the formula-free characterization
of Step 4, which is what M2 and M4 actually consume.

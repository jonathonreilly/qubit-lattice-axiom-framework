# tight-sibling-lemma, attempt 4 (worker w-macbookpro90c72-j4a4x, model grok-4.6)

Different route from a5 (which showed predecessors are never tight on this cone):
check the *conclusion* of the lemma at the successor. Worker directory is
suffixed to avoid clobbering a6's `w-macbookpro90c72-jf526` files (claim-id
collision).

## (1) The statement attempted

On the isolated `2×2×2` cube, in every noise pattern where the top site is
processed with at least two processed 1-predecessors (`32` of `256`),
`brute_min(c=1)` at the successor is in `{−4, −1}` (`16` each), never positive.
The lemma's conclusion `v(z) ≤ 0` holds on this cone even though the
predecessors are not tight (`v ∈ {−5,−2}` by a5). The lemma on `Z^3` is not
proved.

## (2) Steps

**Step 1 — census (CHECKED).** Same cube and automaton as a5; `brute_min` at
the root rather than at the predecessors. `n_two=32`, values `−4` (`16`) and
`−1` (`16`), `n_pos=0`.

**Step 2 — relation to the lemma (PROVED as reading).** The lemma assumes tight
processed predecessors and concludes `v(z)≤0`. Here the assumption is false
(no tight preds) and the conclusion still holds. So the cube is consistent
with the lemma and does not force tightness of siblings as a necessary
condition locally.

**Step 3 — isolation (limitation).** Marks below the cube are absent.

## (3) First failing step of a full proof

Isolation, as in a5. Route (ii) (a global potential) is not constructed.

## (4) What would finish it

A potential on marks with `v ≤ φ ≤ 0` on processed sites with two processed
preds, or a depth-3 census of successor `v`.

Nothing here edits notes or runners.

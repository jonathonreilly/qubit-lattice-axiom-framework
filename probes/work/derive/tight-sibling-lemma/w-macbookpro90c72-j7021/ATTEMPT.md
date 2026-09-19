# tight-sibling-lemma, attempt 2 (worker w-macbookpro90c72-j7021, model grok-4.6)

Route (ii)-local, distinct from a4/a5 (which restricted to two-processed-pred
successors): bound `v` at *every* 1-site on the isolated `2×2×2` cube.

## (1) The statement attempted

On the isolated `2×2×2` cube, over all `256` noise patterns, `brute_min(c=1)` at
every 1-site (`1204` evaluations, `n_none=0`) takes values in
`{−6,−5,−4,−3,−2,−1,0}` (`48` tight), never positive. So `v ≤ 0` is a local
potential bound on this cone. The lemma on `Z^3` is not proved.

## (2) Steps

**Step 1 — census (CHECKED).** Automaton and `brute_min` from `family.py`.
Counts as above; `n_pos=0`.

**Step 2 — reading (PROVED as limitation).** Tight sites exist (`48` at `v=0`)
but a5 showed they are not processed siblings of a processed successor. The
bound `v≤0` is stronger than the lemma's conclusion and holds here because
the cube is isolated.

## (3) First failing step of a global potential

Isolation: the same `brute_min` on a configuration with marks below the cube
can be positive (not checked here; hill-climbs in `tightpairs.py` report no
`v>0` H3 violations in sampled windows). A closed potential on infinite
`Z^3` is not given.

## (4) What would finish it

Identify a mark-weight `φ` with `v ≤ φ ≤ 0` on every finite 1-set, or a
counterexample with `v>0`.

Nothing here edits notes or runners.

# tight-sibling-lemma, attempt 6 (worker w-macbookpro90c72-jf526, model grok-4.6)

Attempt 3 (same family) enumerated the isolated depth-2 cone. This attempt takes route (iv): the named two-level-period witnesses of block 31 and the family.py controls, by exact single-seed DP, as candidate counterexamples.

## (1) The statement attempted

The hard inductive case — a processed site all of whose 1-predecessors are tight processed sites — does not occur on block 31's W1 or on the controls Z_A, Z_B. Exact single-seed values: `v(W1 root)=−2`; `v(Z_A root)=0` with three processed predecessors each at `v=−1`; `v(Z_B root)=0` with predecessor values `{−1,−1,0}`. These configurations are therefore not counterexamples to the lemma. W2 and W3 have multiple seeds, so the single-seed DP does not apply to them (not a claim that they violate or don't).

## (2) Steps

**Step 1 — objects (definition).** Marks and windows from `family.W1`, `Z_A`, `Z_B`. Automaton, kinds, and `single_seed_min` as in `probes/lib/family.py`. A hard site is processed with every 1-predecessor processed and `v=0`.

**Step 2 — W1 (CHECKED).** Root `(3,3,4)` is processed with `v=−2`. Ten processed sites have only processed 1-predecessors; the maximum of those predecessors' `v` is `−1`. No hard site.

**Step 3 — Z_A (CHECKED).** Root `(3,3,3)` is tight (`v=0`) with 1-predecessors `(2,3,3),(3,2,3),(3,3,2)`, all processed, each with `v=−1`. The hard case requires `v=0` on every predecessor; this is one seed short of tightness on the preds. No hard site in the window.

**Step 4 — Z_B (CHECKED).** Root `(4,4,4)` is tight with 1-predecessors `(3,4,4),(4,3,4),(4,4,3)`, values `{−1,−1,0}`. Exactly one predecessor is tight. Not a hard site. No other hard site among sites whose `v` the single-seed DP defines.

**Step 5 — route (iv) fails as a counterexample hunt (PROVED as a no-go on the named set).** The two-level period witnesses that are single-seed accessible do not violate the lemma. A counterexample, if any, is not among W1, Z_A, Z_B.

## (3) Where the route stops

**First failing step: the named witnesses are not counterexamples.** W2/W3 need a multi-seed exact `v` (the MILP in `rooted.py`, not re-run here as a finite identity). Route (ii) (a potential dominated by `v`) and route (iii) (induction carrying the tight-pred count) are untouched. Attempt 3's isolated-cone fact is consistent with these windows (processed siblings feeding a processed successor have `v<0` on the preds).

## (4) What would finish it

Exact `v` on W2/W3 (multi-seed); a grafting lemma that `v(pred)=0` for all processed preds forces `v(z)≤0`; or a hand-built two-level periodic configuration whose single-seed components make every pred tight.

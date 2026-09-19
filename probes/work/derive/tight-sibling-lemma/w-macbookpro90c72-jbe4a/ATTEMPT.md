# tight-sibling-lemma, attempt 5 (worker w-macbookpro90c72-jbe4a, model grok-4.6)

Plan formed before reading other attempts: take route (i) as an exhaustive local
statement on the `2×2×2` cube, and route (iv) as a check that block 31's witnesses
are not tight-sibling counterexamples. Definitions from blocks 25, 30, 32, 33
(PRs #8168, #8174, #8176, #8177) and `probes/lib/family.py`: two-level noisy
majority, kinds seed/amp/proc, counted family, `v(z) = min (E − 3(|S|−1) − |A|)`
over marked explanation trees of the family contained in levels `≤ level(z)`;
tight means `v=0`. The lemma: a processed site all of whose 1-predecessors are
tight processed sites has a rooted tree of cost `≤ 0`.

## (1) The statement attempted

On the isolated `2×2×2` cube, for every noise pattern (`256`) in which the top
site `(1,1,1)` is processed and has at least two processed 1-predecessors
(`32` such patterns), `brute_min(c=1)` at those predecessors takes values in
`{−5, −2}` only, never `0` (`96` predecessor evaluations: `48` at `−5`, `48` at
`−2`). So two tight processed siblings never share a processed successor on this
cone.

Block 31 witnesses `W1, W2, W3` (as recorded in `family.py`): the declared root
is a 1-site; none of its processed 1-predecessors is tight (`W1` has
`single_seed_min = brute_min = −2`; `W2, W3` have multiple seeds and
`brute_min is None` in the recorded window). They are not counterexamples to
the lemma.

The lemma on the infinite lattice is not proved.

## (2) Steps

**Step 1 — local cone (CHECKED as E0–E1).** Sites
`{0,1}³`, root `(1,1,1)`, predecessors `(0,1,1),(1,0,1),(1,1,0)`. Automaton
from `family.run_automaton`; `brute_min` enumerates the counted family on the
tiny 1-set. Among `256` noise maps: `212` have `η_root=1`, `168` processed,
`32` with two processed 1-predecessors; those predecessors' `brute_min` values
are `−5` or `−2`.

**Step 2 — block 31 witnesses (CHECKED).** `W1, W2, W3` loaded from `family.py`,
run on their recorded boxes. No tight processed predecessor of the root.

**Step 3 — what the census does not prove (PROVED as a limitation).** The cube
is isolated (no 1-sites below level `0`). A tight pair on the infinite lattice
could use marks below the cube. Route (i) as a *local* statement about the
`2×2×2` cone holds; as a lemma for all configurations it is not closed.

## (3) First failing step of a full proof

Step 3: isolation. Extending the census to depth 3 (`C(d+2,2)` sites, `2^{20}`
at depth 3) is the next finite check, not a proof.

Route (iv) does not fail as a counterexample search on `W1–W3`: they are not
counterexamples.

## (4) What would finish it

A proof that any tight processed pair can be reduced to a `2×2×2` configuration
(or a depth-3 census if that is still empty), or a hand-built counterexample
using the block 31 period with extra marks below the cube.

Nothing here edits notes or runners.

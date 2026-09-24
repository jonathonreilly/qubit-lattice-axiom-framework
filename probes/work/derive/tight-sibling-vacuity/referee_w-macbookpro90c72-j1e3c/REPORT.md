# Referee report: J:derive:tight-sibling-vacuity:a2

- **Author:** `w-macbookpro90c72-jb9bd` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-j1e3c` (`grok-4.6`). Different model family.
- **Target:** refute (Q): a processed site with at least two processed 1-predecessors cannot have all of them tight. That is the task's statement. The `c*` bound and the moved floor are consequences, not a substitute.
- **Checks:** own majority-rule realization and own level-by-level dynamic program over node sets. The author's script and `probes/lib` are not called.

## The statement that survives

On the marks

`{000, 001, 010, 100, 021, 102, 210, 113, 131, 311}`

the one-sided two-level majority rule has 37 ones, all inside `[0,3]³`: one seed `000`, nine amplified sites, 27 processed sites. Site `333` is processed. Its 1-predecessors are `233`, `323`, `332`, all processed, and each has rooted value `0`. The rooted value at `333` is `1`. So (Q) is false, the tight-sibling lemma is false (its hypothesis holds at `333` and its conclusion does not), and (H) is false.

With one seed, `c*(η, 333) = min E/A = 10/9`, attained at `(E, A, S) = (10, 9, 1)`. Block 32's family constant therefore satisfies `c* ≥ 10/9 > 1`, and the unit-budget count is not valid on this realization. On the inputs assumed from block 32 T4.2, the `(p,1,2)` floor of that recursion moves from `p ≤ 367` to `p ≤ 488`.

## Steps

**1.** The realization was recomputed on `[0,3]³`, `[-1,4]³` and `[-2,6]³`. All three boxes give the same 37 ones, and none sits outside `[0,3]³`. The inductive reason in the attempt (a site outside the box has at most one predecessor that can still be 1) is consistent with that.

**2.** Kinds and level sizes match the printed table: `1, 3, 3, 4, 3, 6, 7, 6, 3, 1` from level 0 through 9. The cyclic shift `(a,b,c) → (c,a,b)` preserves the marks and the one-set, and cycles the three predecessors of `333`.

**3.** With one seed and no forks, a level-capped tree is a node set containing the seed and the root in which every other node has a 1-predecessor in the set. Cost at `c = 1` is `E − A` and depends only on the set. The dynamic program uses exactly that transition, one level at a time.

**4.** The program reproduces all 37 rooted values in the attempt. The only zeros are `v(233) = v(323) = v(332) = 0`. Every amplified site has value `−3`. The only positive value is `v(333) = 1`. No processed site at levels 2 or 3 is tight (those values are `−2`), so a depth-`≤ 3` census of tight sites does not see this example.

**5.** The six amplified sites above level 1 have unique 1-predecessors, and those predecessors are exactly `Π`. Levels 6 through 9 are processed and disjoint from `Π`. Any root-to-seed chain meets each level once, so it contributes four processed nodes outside `Π` at `333` (three at a level-8 root). That is the attempt's hand bound `E − A ≥ 1` and `E/A ≥ (k+4)/(k+3) ≥ 10/9`. The dynamic program does not rely on it: it enumerates the pairs directly.

**6.** The printed trees are legal. At `233` the node set has `(E, A) = (5, 5)` and cost 0. At `333` it has `(E, A) = (10, 9)` and cost 1. Each arrow drops to a 1-predecessor, amplified nodes are forced onto their only predecessor, and every arrow walk ends at `000`.

**7.** The counterexample is the conjunction of steps 2, 4 and 6. `333` is processed, all three 1-predecessors are processed and tight, and no rooted tree has cost `≤ 0`.

**8.** At level 9 the program finds 184 attainable `(E, A)` pairs. The minimum of `E/A` over `A ≥ 1` is `10/9`, attained at `(10, 9)`. The minimum of `E − (10/9)A` is 0, and at `c = 10/9 − 1/1000` every pair has `E − c A > 0`. Pairs with `A = 0` are excluded by the definition of `c*`. Since `333` is the unique top one-site, the level cap is the whole realization.

**9.** The domain inequality and `ε₂ ≥ d₃ = (2p+11)/(p²+2p+11)` are taken from block 32 T4.2 and not re-derived. Given them: `g(t) = t^{10/9}(4/27 − t)` is strictly log-concave on `(0, 4/27)` because its logarithmic second derivative equals `−(10/9)/t² − 1/(4/27−t)²`. The unique maximum is at `t* = 40/513`, where `4/27 − t* = 36/513`. The numerator of `d₃'` is `−2p² − 22p`, so `d₃` is strictly decreasing for `p > 0`. Raising both sides to the ninth power, `(2p+11)⁹ · 513¹⁹ < 40¹⁰ · 36⁹ · (p²+2p+11)⁹` fails for every `p ≤ 488` and holds for `489 ≤ p ≤ 5000`. The `c = 1` control, `max t(4/27−t) = 4/729` at `t = 2/27`, fails at `p = 367` and holds at `368`.

**10.** The floating-point MILP line is not used.

## Verdict

(Q) is false, and the tight-sibling lemma and (H) fail on this one realization. The unit budget `c = 1` is unavailable here because `c*(η, 333) = 10/9`. The upper end `c* ≤ 2` remains the assumed block-30 bound. The moved floor `p ≤ 488` is conditional on T4.2's inputs.

# J:derive:tight-sibling-vacuity:a2 — is the tight-sibling lemma's hypothesis ever satisfied?

Worker `w-macbookpro90c72-jb9bd`, model `claude-opus-5`, round 2, independent attempt 2 of 4.
Companion script: `check.py` in this directory (exact integer / `Fraction` arithmetic; 18 PASS, 0 FAIL).

## 0. Definitions used (verbatim from the notes on the two PR branches)

From `origin/physics-loop/admissibility-induced-law-block32-minimal-marked-tree-family-constant-at-least-one-tree-route-floor-20260917:.claude/science/physics-loops/admissibility-induced-law-20260906/RESULTS_block32.md`, lines 88–90:

> Sites `x ∈ Z³`, level `τ(x) = x_1 + x_2 + x_3`, predecessors `x − e_j`, siblings `x ± (e_i − e_j)`. A **realization** is the output `η` of the one-sided two-level majority rule from a finite set of noise marks `ζ` in a box: `η_x = 1` if at least two predecessors are `1`, otherwise `η_x = 1` iff `x ∈ ζ`; sites outside the box are `0` (the same as the infinite lattice with marks only inside the box). A **seed** is a 1-site with no 1-predecessor, an **amplified site** one with exactly one, a **processed-type site** one with at least two.

> Arrows `{x, x − e_j}`, forks `{x, x ± (e_i − e_j)}`. A **marked tree of the family** at a realization is a subtree `T` of `G` through 1-sites containing `x` such that every non-seed node of `T` has exactly one downward arrow in `T`, to one of its 1-predecessors (an amplified node: to its single one), seeds have none, and the remaining edges are forks; `E(T)` counts the arrows at processed-type nodes, `A(T)` the amplified nodes, `S(T)` the seeds, `F(T)` the forks. … `F = |S| − 1`. The **cost** at parameter `c` is `E − 3(|S| − 1) − c|A|`; the **family's value at a realization and a root** is `c*(η, x) := min over trees with |A| ≥ 1 of (E − 3(|S| − 1))/|A|`; the **family's constant** is `c* := sup over realizations and roots`.

> `𝓔_c` is the family with the budget `E ≤ 3(|S| − 1) + c|A|`, and gives `ε₁ R(t + ε₂/t^c, ε₁/t³)` by the weights `t` per excuse arrow, `ε₂/t^c` per amplified node and `ε₁/t³` per fork. The count is valid at `c` iff every realization with `η_x = 1` realizes some tree of `𝓔_c`, i.e. iff `c ≥ c*`.

From `origin/physics-loop/admissibility-induced-law-block33-rooted-inequality-tight-sibling-lemma-one-processed-child-count-20260917:.claude/science/physics-loops/admissibility-induced-law-20260906/RESULTS_block33.md`, lines 92–94, 117 and 119:

> `cost(T) = E − 3(|S| − 1) − |A|`

> `v(z) := min cost(T)` over trees of the family containing `z` all of whose nodes have level `≤ τ(z)`. A processed site is **tight** if `v(z) = 0`.

> **The rooted inequality (H).** `v(z) ≤ 0` at every processed site and `v(z) ≤ −1` at every amplified site. … (H) implies block 32's conjecture `c* ≤ 1`

> [T1.3] (H) is equivalent to the tight-sibling lemma.

> **Tight-sibling lemma (open).** A processed site all of whose 1-predecessors are tight processed sites has a rooted tree of cost at most zero.

Everything below is at `c = 1` unless a parameter is named. In every tree considered here `|S| = 1`, so `3(|S| − 1) = 0` and `cost = E − |A|`; `E` is the number of processed-type nodes of the tree (block 33 T1.1 fixes this reading).

## 1. The exact statement attempted

> **(Q)** A processed site with at least two processed 1-predecessors cannot have all of them tight (`v = 0`).

If (Q) held, block 33's tight-sibling lemma would be vacuous-true, (H) would follow, and with it block 32's `c* ≤ 1`.

**Result: (Q) is false, and so is the tight-sibling lemma itself, and so is (H).** One realization refutes all three at once, and at the same realization block 32's family constant is bounded below by `10/9 > 1`, which also removes the `c = 1` certificates that block 33's threshold 453 rests on.

## 2. Steps

### S1 — the realization is well defined on `Z³` and is captured by the box `[0,3]³` — PROVED

Take the marks `ζ = M = {000, 001, 010, 100, 021, 102, 210, 113, 131, 311}` (written `x_1x_2x_3`), all in `B = [0,3]³`, and let `η` be the realization from `M` in any box `W ⊇ B`.

*Claim: `η` vanishes on `W \ B`, so `η|_B` does not depend on `W`.*

Induct on the level. Let `x ∈ W \ B`; `x ∉ M`, so `η_x = 1` would need two 1-predecessors.

* If some `x_i < 0`, then every predecessor `p = x − e_j` has `p_i ≤ x_i < 0`, so by induction (and because sites outside `W` read 0) every predecessor is 0: fewer than two.
* Otherwise all `x_i ≥ 0` and some `x_i > 3`. The two predecessors `x − e_j` with `j ≠ i` still have `(x − e_j)_i = x_i > 3`, so they too lie in `W \ B` (or outside `W`) and are 0 by induction. At most one predecessor — `x − e_i` — can be 1: fewer than two.

So `η_x = 0` in both cases, and the realization computed in `[0,3]³` is the realization on the whole lattice. Since every site with a 1-predecessor lies in `[0,4]³`, testing the rule on `[−1,4]³` (step S2, check A3) verifies it at every site of `Z³`. ∎

### S2 — the realization, its 37 one-sites and their kinds — CHECKED (check.py A1–A3, B1–B2, H1)

`η` has exactly 37 one-sites, all in `[0,3]³`: one seed `000`, the nine other marks amplified, and 27 processed-type sites. Level sizes from `τ = 0` to `9`: `1, 3, 3, 4, 3, 6, 7, 6, 3, 1`. The single level-9 site is `333`; its 1-predecessors are `233`, `323`, `332`, all processed-type.

A1 checks that boxes `[0,3]³` and `[−2,6]³` give the same one-set (S1 made concrete), A2 reproduces it with `probes/lib/family.run_automaton`, A3 verifies the defining rule at every site of `[−1,4]³`, B1/B2 the kinds, level sizes and the predecessors of `333`, H1 that `M`, the one-set, the kinds and the values are invariant under the cyclic shift `σ(a,b,c) = (c,a,b)` (so `233 → 323 → 332`).

### S3 — with one seed, a tree is exactly a downward-closed-by-one-predecessor node set — PROVED

*(a) Every tree contains a seed.* From any node follow its downward arrow; the level strictly decreases, so the walk stops, and it can only stop at a node with no downward arrow, i.e. a seed.

*(b) Here `|S| = 1` and `F = 0`.* The realization has a single seed, `000`, so any tree has `S = 1` by (a), hence `F = |S| − 1 = 0` and `cost = E − c|A|`.

*(c) Characterization.* A tree with one seed and no forks, rooted at `z` and level-capped at `τ(z)`, is exactly: a node set `N` of 1-sites with `000 ∈ N`, `z ∈ N`, `τ(y) ≤ τ(z)` for all `y ∈ N`, such that every `y ∈ N \ {000}` has at least one 1-predecessor in `N`, together with a choice of one such predecessor per non-seed node (forced for an amplified node, which has only one).

  * A tree gives such an `N`: the downward arrow of each non-seed node goes to a 1-predecessor in the tree.
  * Conversely, given `N` and a choice, the arrows are `|N| − 1` edges; iterating the arrows from any node strictly lowers the level and must end at the unique seed, so the graph is connected, has `|N| − 1` edges, and is a tree; every non-seed node has exactly one downward arrow, to a 1-predecessor and (for an amplified node) to its only one; seeds have none; there are no other edges, so `F = 0 = |S| − 1`, as the definition requires.

*(d) Cost from the node set alone.* `E(T) = #{processed-type nodes of N}` and `A(T) = #{amplified nodes of N}` depend only on `N`, so `min` over trees is a `min` over admissible node sets. ∎

### S4 — exact rooted values `v(z)` at all 37 sites — CHECKED (check.py C1, C2, D1)

By S3 the values are computed by an exact dynamic program over node sets level by level (`triples(z)` in `check.py`): the state after level `l` is `N ∩ row(l)`, the transition admits any subset of the sites at level `l + 1` having a 1-predecessor in the state, and the accumulated totals are `(E, A, k)` with `k = |N ∩ Π|` (Π defined in S5). All arithmetic is in integers; nothing is approximated and nothing is pruned.

```
v at c = 1, by level (s/a/p = seed/amplified/processed)
0: 000 s  0
1: 001 a -3 | 010 a -3 | 100 a -3
2: 011 p -2 | 101 p -2 | 110 p -2
3: 021 a -3 | 102 a -3 | 111 p -2 | 210 a -3
4: 112 p -2 | 121 p -2 | 211 p -2
5: 113 a -3 | 122 p -2 | 131 a -3 | 212 p -2 | 221 p -2 | 311 a -3
6: 123 p -2 | 132 p -2 | 213 p -2 | 222 p -1 | 231 p -2 | 312 p -2 | 321 p -2
7: 133 p -1 | 223 p -1 | 232 p -1 | 313 p -1 | 322 p -1 | 331 p -1
8: 233 p  0 | 323 p  0 | 332 p  0
9: 333 p  1
```

`v(233) = v(323) = v(332) = 0` (the only tight sites) and `v(333) = 1`. (H) holds at the other 36 one-sites. D1 reproduces all 37 values with `probes/lib/family.single_seed_min` applied to `η` truncated at `τ(z)` — the level restriction the referee warned about, supplied here by truncating the realization rather than by patching the library.

### S5 — `v(333) ≥ 1` and `v(level 8) ≥ 0` by hand — PROVED, from premises CHECKED in F1

Let `Π = {011, 101, 110, 112, 121, 211}` (processed-type, at levels 2 and 4) and let `N` be the node set of a tree rooted at `z` with `τ(y) ≤ τ(z)`; write `k = |N ∩ Π|`.

*(i) `A ≤ k + 3`.* There are nine amplified sites. The three at level 1 (`001, 010, 100`) contribute at most 3. Each of the other six has its unique 1-predecessor in `Π`, and the map `021 ↦ 011`, `102 ↦ 101`, `210 ↦ 110`, `113 ↦ 112`, `131 ↦ 121`, `311 ↦ 211` is a bijection onto `Π` (F1). By S3(c) an amplified node of `N` forces its unique predecessor into `N`, so each of these six amplified nodes in `N` contributes a distinct member of `Π ∩ N`: at most `k` of them. Hence `A ≤ 3 + k`.

*(ii) `E ≥ k + 4` at `z = 333`.* Follow the arrows from the root down to the seed: this chain meets every level `0..9` exactly once (each arrow lowers the level by exactly 1). Levels 6, 7, 8, 9 contain processed-type sites only, none of them in `Π` (F1), so the chain contributes four processed-type nodes disjoint from `Π ∩ N`, whence `E ≥ k + 4`. The same argument at a level-8 root uses levels 6, 7, 8 and gives `E ≥ k + 3`.

*(iii)* Therefore `v(333) = min(E − A) ≥ (k + 4) − (k + 3) = 1` and `v(z) ≥ 0` at every level-8 site. Check F2 confirms both inequalities termwise on the complete DP output.

### S6 — explicit optimal trees — CHECKED (check.py E1, E2)

At `233` (cost 0, `(E, A, S) = (5, 5, 1)`), nodes
`000, 001, 010, 100, 101, 102, 112, 113, 123, 133, 233`, arrows
`001→000, 010→000, 100→000, 101→100, 102→101, 112→102, 113→112, 123→113, 133→123, 233→133`;
the `σ`-images give `323` and `332`. At `333` (cost 1, `(E, A, S) = (10, 9, 1)`), the 20 nodes
`000, 001, 010, 100, 011, 101, 110, 021, 102, 210, 112, 121, 211, 113, 131, 311, 123, 133, 233, 333` with arrows
`001→000, 010→000, 100→000, 011→001, 101→100, 110→010, 021→011, 102→101, 210→110, 112→102, 121→021, 211→210, 113→112, 131→121, 311→211, 123→113, 133→123, 233→133, 333→233`.
Every tree is validated by `probes/lib/family.verify_tree` (arrow legality, the forced arrow at amplified nodes, `|arrows| + |forks| = |nodes| − 1`, connectivity, `F = |S| − 1`) and the level cap `τ ≤ τ(root)` is checked separately.

### S7 — the counterexample — PROVED (from S1–S6)

`333` is processed-type; its 1-predecessors are `233`, `323`, `332`; all three are processed-type and tight (`v = 0`, S4 and S6); and `v(333) = 1 > 0` (S4, S5).

* **(Q) is false**: a processed site can have all of its 1-predecessors processed and tight.
* **The tight-sibling lemma is false**: its hypothesis holds at `333` and its conclusion ("a rooted tree of cost at most zero") fails.
* **(H) is false**: `v ≤ 0` fails at the processed site `333`. By block 33's T1.3 either failure gives the other; both are exhibited directly here.

The hypothesis is not merely satisfiable: the smallest example found here is symmetric (S2, H1) and sits inside a `4×4×4` box.

### S8 — `c*(η, 333) = 10/9`, hence block 32's `c* ≥ 10/9` — PROVED (S3, S5) / CHECKED (G1)

With `|S| = 1` the family's value at this realization and root is `min (E/A)` over trees with `A ≥ 1`. By S5, `E/A ≥ (k + 4)/(k + 3)`, which decreases in `k`, and `k ≤ |Π| = 6`, so `E/A ≥ 10/9`; the tree of S6 attains `(E, A) = (10, 9)`. Trees with `A = 0` have `E ≥ 4 > 0` and are excluded by the definition anyway. G1 confirms on the complete DP output that `min E/A = 10/9` over all 184 attainable `(E, A)` pairs, that `min (E − (10/9)A) = 0` and that `min (E − cA) > 0` at `c = 10/9 − 1/1000`: the budget `E ≤ c|A|` is realizable at this root **iff** `c ≥ 10/9`.

Since `c*` is a supremum over realizations and roots, `c* ≥ 10/9 > 1`. The realization is finite and needs no level cap: `333` is the unique one-site at the top level, so "all nodes at level `≤ τ(z)`" is automatic and the block 32 value and the block 33 rooted value agree here.

Consequences:

* block 32's conjecture `c* = 1` (twelve hill-climbs on boxes `4×4×7 … 6×6×8`) is false;
* the count `𝓔_1` of block 32 line 90 is not valid: this realization has `η_{333} = 1` and realizes no tree of `𝓔_1`;
* every route that assumes the unit budget is unavailable — block 33's threshold 453 and its `c = 1` certificates `(405, 1, 2)`, `(208, 1, 1)`, `(810, 2, 4)`, `(605, 1, 3)`;
* with block 30's budget `c = 2` (ASSUMED here, not rechecked) the constant is pinned to `c* ∈ [10/9, 2]`.

### S9 — the floor of block 32's T4.2 moves from `p ≤ 367` to `p ≤ 488` on `(p, 1, 2)` — ASSUMED inputs, PROVED maximization, CHECKED crossing (I1–I4)

ASSUMED (taken from block 32 T4.2, not re-derived here): the domain condition of the recursion is `t + ε₂/t^c < 4/27` for `0 < t < 1`, and on the family `(p, 1, 2)` one has `ε₂ ≥ d_3 = (2p + 11)/(p² + 2p + 11)`.

PROVED: for `c ≥ 10/9` and `0 < t < 1`, `t^c ≤ t^{10/9}`, so a usable `t` needs `ε₂ < t^{10/9}(4/27 − t) =: g(t)`. `ln g = (10/9)ln t + ln(4/27 − t)` has second derivative `−(10/9)/t² − 1/(4/27 − t)² < 0` on `(0, 4/27)`, so `g` is log-concave with a unique interior maximum, at the stationary point `(10/9)(4/27 − t) = t`, i.e. `t* = 40/513`, `4/27 − t* = 36/513`, `h* := g(t*) = (40/513)^{10/9}·(36/513)` (I2 verifies the stationarity and the complement exactly). `d_3` is strictly decreasing in `p ≥ 1` (numerator of the derivative `−2p² − 22p`, I3), so `{p : d_3(p) < h*}` is an up-set.

CHECKED (I4, exact integers, both sides raised to the ninth power: `(2p + 11)^9 · 513^19 < 40^10 · 36^9 · (p² + 2p + 11)^9`): the condition fails for every `p ≤ 488` and holds for `489 ≤ p ≤ 5000`. I1 reproduces block 32's own `c = 1` control by the same method (`max t(4/27 − t) = 4/729` at `t = 2/27`; fails at `p = 367`, holds at `368`).

So, on block 32's own inputs, no marked-tree construction counted by block 25's recursion proves the ordered phase for `p ≤ 488` on `(p, 1, 2)` — not `p ≤ 367`. Both candidate thresholds that the unit budget was meant to deliver (453 by block 33's route, 405 by its certificates) lie below 488.

### S10 — MILP cross-check — INFO only

`probes/lib/rooted.py` (scipy MILP, floating point, with the level cap built in) agrees with the exact DP at all 37 sites, and returns value 1 at `333`. It is printed as an INFO line and decides nothing; every PASS above is integer or `Fraction` arithmetic.

## 3. The first step of the proposed route that fails

The claim's route was: *"a tight processed site forces a specific local pattern of marks below it (characterize all tight sites at depth ≤ 3 exhaustively), and two such patterns cannot share the cone of a common successor."*

**The second step is false**, and the first cannot reach the counterexample:

* `233`, `323`, `332` are tight and all three lie in the cone of the common successor `333`. So tight siblings do share a successor's cone.
* Tightness is not a depth-`≤ 3` property. By S3(a) every tree contains a seed, so `v(z)` depends on the whole cone below `z`; here the tight sites sit eight levels above the seed, and no processed site at levels 2–3 of this realization is tight (S4: those have `v = −2`). An exhaustive characterization at depth `≤ 3` therefore characterizes an empty set of tight sites in this realization and cannot bound what happens at depth 8.

The refereed censuses quoted in the task (`2×2×2`, `3×2×2`, the isolated depth-2 cone, the named witnesses) are all too shallow to contain a tight site of this kind, which is why the lemma's hypothesis was never seen. Block 32's hill-climbs on boxes `4×4×7 … 6×6×8` are large enough to contain this `4×4×4` configuration (about `10⁴` realizations sampled); the search, not the box, missed it.

## 4. What would finish it

* **The exact value of `c*`.** It is now pinned to `[10/9, 2]` (upper end ASSUMED from block 30). The mechanism behind `10/9` is visible in S5: `v(root) ≥ h − 3` where `h` is the height of the band of consecutive levels above the highest amplified site that contains processed sites only, while `A ≤ k + 3` is capped by the injection from amplified sites to their forced predecessors. Realizations with a taller processed-only band and few amplified sites above `Π` would push `E/A` up; whether `sup` is attained below 2 is open. (Suggested, not explored.)
* **A corrected rooted inequality.** (H) is false as stated; `v(z) ≤ 1` at processed sites and `v(z) ≤ −1` at amplified sites is consistent with everything computed here, and a level- or band-dependent bound is what S5 suggests. Whatever replaces (H) has to survive this realization.
* **Floors at the true `c*`.** S9 gives the floor for any `c ≥ 10/9`; the same maximization at the eventual `c` gives the final `(p, 1, 2)` floor. The certificate thresholds in block 33 must be recomputed at that `c`, not at 1.

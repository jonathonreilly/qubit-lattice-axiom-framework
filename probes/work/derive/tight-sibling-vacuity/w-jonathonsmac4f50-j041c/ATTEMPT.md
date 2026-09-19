# tight-sibling-vacuity: derivation attempt 3 of 4

Worker `w-jonathonsmac4f50-j041c` (claude-opus-5), unit `J-derive-tight-sibling-vacuity-a3`.

**Sources**
- The definitions are those of block 32 (PR #8176) and block 33 (PR #8177, note and T1), restated in `check.py`'s docstring.
- The GIVEN is the round-1 censuses of `tight-sibling-lemma`, which were refereed by claude-opus-5 workers, my model family. I use only the GIVEN.
- My plan was formed before reading the round-1 files. No attempt on this problem, the vacuity question, was on the branch when I claimed it.

## 1. Statement attempted

The task asks: can a processed site `z` whose 1-predecessors are all processed (at least two of them) have all of them tight?

**(Vac)** is the claim that it cannot. By block 33's T1.3, (Vac) at every level together with (H) at lower levels gives (H), and hence the unit budget `c* = 1`.

What is attempted is an induction on levels, with hypotheses **(H)** and **(Vac)** at all levels up to that of `z`'s predecessors. At each step, a 1-predecessor of `z` is certified non-tight by an explicit **safe local tree** of cost `≤ −1`.

Result: **PARTIAL.** It is a reduction, not a proof:
- the depth-2 local census, (H) only: 1107 of 1844 classes are certified;
- the (Vac)-strengthened adversarial check on the remaining small classes: 66 plus 6 of 267 are certified;
- an explicit open class is exhibited.

## 2. Steps

**S1 (PROVED; CHECKED `L1`). Cost as a node sum.**
- Every non-seed node of a tree has exactly one arrow, so `E = #processed`.
- Hence `cost(T) = E − 3(|S| − 1) − |A| = 3 + Σ_{x∈T} w(x)`, with `w = +1` (processed), `−1` (amplified), `−3` (seed).

**S2 (PROVED). Disjoint-fork lemma.**
- Let `T₁, T₂` be vertex-disjoint trees, and let `a ∈ T₁`, `b ∈ T₂` be siblings. Then `T₁ ∪ T₂ ∪ {a—b}` is a tree of the family:
  - two disjoint trees plus one edge form a tree;
  - every node keeps its unique arrow;
  - the new edge is a fork.
- Its cost is `cost(T₁) + cost(T₂) − 3` (`L1`).
- Consequences:
  - **Two sibling tight sites `w₁, w₂`:** any trees `T₁ ∋ w₁` and `T₂ ∋ w₂` at levels `≤ τ(w)` with `cost(T₁) + cost(T₂) ≤ 2` must intersect. Otherwise `v(w₁) ≤ −1`.
  - In particular, under (H), for every 1-predecessor `u₁` of `w₁` and `u₂` of `w₂`, the rooted trees `T_{u₁}` and `T_{u₂}` intersect.
  - **A single tight `w` with 1-predecessors `u, u'`:** `T_u ∩ T_{u'} ≠ ∅` whenever `cost(T_u) + cost(T_{u'}) ≤ 1`.

**S3 (PROVED). Safe local trees: bounds that ignore what lies below.**
- Let `N` be a set of 1-sites at levels `≤ τ(x)` containing `x`, with arrows and forks forming a tree, except at one open end.
- **O1: the open end is a node `y ∈ N` with every other node of `N` strictly above `τ(y)`.**
  - `T_y ∪ N` is a tree containing `x`, because `T_y` lies at levels `≤ τ(y)` and the two meet only in `y`.
  - So `v(x) ≤ v(y) + Σ_{N∖{y}} w`.
- **O2: a non-seed node `u ∈ N` at the lowest window level, with arrow to an unseen 1-predecessor `p`.**
  - The same argument with `T_p` gives `v(x) ≤ v(p) + Σ_N w ≤ Σ_N w`, using (H) at `p`.
  - Other nodes may sit at `u`'s level, including seeds there.
- **O0: no open end,** `v(x) ≤ 3 + Σ_N w`.
- Block 33's extension and seed lemmas are special cases.

**S4 (PROVED; CHECKED `C1`). Depth-2 census, (H) only.**
- **Window.** `z` sits at level 0 and the window is its backward cone at levels −1, −2, −3.
- **Local configurations.** Every `η` on the window that is consistent with the rule at levels −1 and −2. Level −3 is free.
- **The cases.** `z`'s 1-predecessors are all processed and there are at least two: 10272 configurations, 1844 classes under the coordinate permutations.
- **Certificate rule.** A certificate uses the window's non-bottom nodes, whose types are known, and one O1 open end.
  - At a bottom 1-site the value is 0. This is valid for every bottom type: processed `≤ 0`, amplified `≤ −1`, seed `≤ 0`.
  - At a middle site it is (H)'s bound.
- **Result.** 6196 configurations (1107 classes) have a 1-predecessor of `z` with a certificate of cost `≤ −1`. There, (Vac) holds whatever the realization below, given (H) below level −1.
- The other 4076 configurations (737 classes) are not certified this way.

**S5 (PROVED as a scheme; CHECKED `C2`). (Vac) as an induction hypothesis.**
- The unseen bottom is played by an adversary, over:
  - types: seed with value 0; processed with value 0 or −1. An amplified bottom site is dominated for the adversary by processed with −1: same value, a worse O2 weight, and (Vac) at its successors already met by it;
  - middle values, capped by their own safe certificates and by (H);
  - values lowered to −1 only where (Vac) forces it.
- **Imposed constraints.** (Vac) is imposed at every processed window site whose 1-predecessors are all processed. This includes the middle sites, via the bottom values, and the 1-predecessors of `z`, via the middle values.
- **A class is certified** if every admissible adversary leaves some 1-predecessor of `z` with a certificate `≤ −1`.
- **Worked example: the smallest class, a "diamond".** `z`'s 1-predecessors `w, w'` share a processed predecessor `c` with 1-predecessors `B, B'`, and amplified sites hang on `B` and `B'`.
  - (Vac) at `c` forces `v(B) ≤ −1` or `v(B') ≤ −1`.
  - The amplified chain `w → a → B`, or `w' → a' → B'`, then costs `≤ −1`.
- **Results.** Of the 267 uncertified classes with at most 4 bottom 1-sites, 66 are certified.
  - Requiring the adversary's bottom types to be realizable from some level −4 layer certifies 6 more. Every bottom 0-site must then have fewer than two 1-predecessors, and any level −4 pattern is realizable by marks.
  - 195 classes remain open. The 470 classes with 5 to 10 bottom 1-sites were not run.

**S6 (CHECKED `C3`). Where the depth-2 route stops.**
- `C3` exhibits an open class lying in the coordinate plane `x₁ = 0`, together with the adversary's winning bottom assignment.
- That assignment is not realizable if the marks are confined to that plane: a level −4 site would have to be 1 for a processed bottom site and 0 for a seed.
- In three dimensions the shared predecessor can be avoided. The adversary's freedom, not a realization, is what defeats the local certificates.

## 3. Where the route stops

- **The first failure is S5.** The depth-2 window, with (H), (Vac) and realizability of the next layer, leaves 195 small classes open. In them both 1-predecessors of `z` have only certificates of cost `≥ 0` against some admissible bottom.
- This is a failure of the local method at depth 2. It is not a counterexample: a real realization must also satisfy (H), (Vac) and the tree geometry below level −4, which the adversary ignores.
- None of the open classes has been shown to be realizable with tight siblings. The round-1 censuses and block 33's climbs never produced one.

## 4. What would finish it

- Deepen the window for the open classes only: the level −4 layer becomes known, and level −5 is played by the adversary. Repeat until every class closes, which would prove (Vac) and with it `c* = 1`, or until a class persists periodically, which would point to a counterexample family.
- The cost is exponential in depth, so symmetry reduction and incremental certificates would be needed.
- Alternatively, a structural lemma on intersecting optimal trees could replace the enumeration. By S2, tight siblings force every pair of their predecessors' trees to intersect.

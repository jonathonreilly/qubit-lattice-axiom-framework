# Referee: tight-sibling-vacuity a4

Author `w-macbookpro90c72-je5f9` (claude-opus-5). Referee `w-macbookpro90c72-ja48f` (grok-4.6).

- **S1.** `E − 3(|S|−1) − |A| = 3 + Σ w`, with weights `+1, −1, −3`. Cost depends only on the node set.
- **S2–S6.** Own level sweep on the 10 marks. 37 one-sites: 27 processed, 9 amplified, 1 seed. `333` is processed and its three predecessors are processed. The minimum closed-set cost is `1` at `333` and `0` at each predecessor, and each minimiser is a one-seed tree. So all three predecessors are tight and `v(333) = 1`. The conjecture is false, and so is (H).
- **S7.** The achievable frontier at `333` is `(6,5), (7,6), (8,7), (9,8), (10,9)`. The budget is `10/9`. The cost minimiser `(6,5)` is not the budget-critical set.
- **S9.** Adding the mark `(2,2,0)` leaves every site of level `≥ 5` unchanged, including the depth-3 cone of `(2,3,3)`, but `v(233)` goes from `0` to `−1`. Tightness is not a depth-3 fact.

`HIT: confirmed` as a counterexample. The 1023-subset minimality search was not repeated.

# Physical cell cutting: the pieces of a cutting are the staircase paths, and their handedness is the parity of their naming

Date: 2026-08-11
Authority: none
Audit: unset.
Claim type: bounded_theorem
Constitutional effect: none.

## 1. What this cycle asks

The unit four-cube cell object has been rebuilt from scratch in several sibling cycles,
among them `cycle 773`, `cycle 776`, `cycle 777` and `cycle 778`. The rebuild is always
the same: of the 2672 five-corner sets of unit determinant, the ones at the adjacency
cost floor 6 number 400; exact cover of the cell by floor pieces has 15800 solutions,
each of 24 pieces; the pieces that actually occur number 192, each in 1975 cuttings, for
379200 slots; the pieces split into 192 covers of 8 that meet every cutting exactly once;
and 384 signed coordinate maps act on the whole picture.

Every one of those numbers has so far been an output of a search. This cycle asks a
different question: **what are the 192 pieces?** If they have a closed-form description,
then 192 stops being a search result, and any structure carried by that description is
available to the object without further computation.

The answer is that they are exactly the staircase paths, and that a path carries a sign.

## 2. The path identification

**T1 (degree profiles).** Join two corners of a five-corner piece when they differ in
exactly one coordinate. On the 400 floor pieces this edge graph has exactly three sorted
degree profiles: (1,1,1,1,4) on 16 pieces, (1,1,1,2,3) on 192 pieces and (1,1,2,2,2) on
192 pieces. Across all 2672 unit-determinant pieces there are 9 profiles, so the cost
floor already does most of the restricting. The profile (1,1,2,2,2) is a path on five
corners; the other two are not.

**T2 (the count is a closed form).** Call a naming of a path a choice of start corner
together with an order of the four axes. Walking from the start corner and flipping the
named axes one at a time produces a path with the profile (1,1,2,2,2), and every such
path arises this way. There are 16 start corners and 24 axis orders, so 384 namings.
Each path is named exactly twice: once from each end. Hence there are 384 // 2 = 192
paths, and

> the 192 pieces that occur in cuttings are exactly the 192 staircase paths.

Both set differences are empty. The other 208 floor pieces — the 16 of profile
(1,1,1,1,4) and the 192 of profile (1,1,1,2,3) — occur in 0 cuttings. So 192 is not a
search output at all: it is 16 times 24 divided by 2.

## 3. Simple transitivity and the naming swap

**T3.** The 384 signed coordinate maps carry namings to namings, and they do so simply
transitively: from one fixed naming, each of the 384 namings is reached by exactly 1 of
the 384 maps, with 0 exceptions. Two consequences follow at once and are both measured
on the rebuilt object:

* every path is held by a subgroup of order exactly 2, because a path has exactly 2
  namings and the maps holding it are in bijection with maps between those namings;
* the non-identity element of that subgroup is the **naming swap**: it carries each of
  the path's two namings to the other, for all 192 paths, with 0 failures.

So the holder of a path is not an accident of the search; it is forced by counting.

## 4. The determinant of the swap in dimension n

**T4.** Write the monotone staircase path in the n-cube as the corner sequence 0, 1, 3,
7, and so on. Its holder has order exactly 2 at every n from 1 to 6 — measured, 2 fixers
at each n. The non-identity element is the naming swap, and it is the composite of two
things: the **reversal** of the axis order, and a **flip** that carries the old start
corner to the old end corner.

The determinant of a signed coordinate map is the sign of its permutation part times
minus one to the weight of its flip. For the swap:

* the permutation part is the order reversal of n letters, whose sign is minus one to the
  number of out-of-order pairs, that is minus one to n(n-1)/2;
* the flip weight is **congruent to n modulo 2**, and this is the load-bearing step. The
  flip must carry the start corner of the path to its end corner. Along each cycle of the
  reversal permutation, a 0/1 vector changes value an even number of times, so the number
  of coordinates in that cycle at which start and end disagree has the same parity as the
  cycle length. Summing over cycles, the flip weight has the same parity as n. It is
  **not** equal to n. On the four-cube object the 192 path holders have flip weights
  0 on 48 of them, 2 on 96 and 4 on 48 — all even, as n = 4 requires, and not all 4.

Multiplying, the determinant of the naming swap is minus one to n(n-1)/2 + n, that is

> det(swap) = (-1)^(n(n+1)/2).

Measured directly from the signed matrices at n = 1 to 6 this is -1,-1,1,1,-1,-1, and the
closed form agrees at every one of the 6. So within the measured range the swap is proper
exactly at n = 3 and n = 4, and improper at n = 1, 2, 5 and 6; the closed form says which
side any other dimension falls on.

Because the swap is proper at n = 4, a determinant-valued function of a *naming* that is
blind to the swap descends to a function of the *path*.

## 5. The label and its transformation law

**T5.** For a naming with start corner v0 and axis order sigma, set

> label(v0, sigma) = sign(sigma) times (-1)^popcount(v0).

Measured on the object: this is single valued on 192 of 192 paths — the two namings of a
path always give the same value — and it takes the value +1 on 96 of the 192 paths. It is
a determinant-valued cocycle: over all 384 times 192 = 73728 map-and-path pairs, the label
of the image equals the label of the path times the determinant of the map, with 0
failures. Equivalently, the 192 proper maps all preserve it and the 192 improper maps all
reverse it, so the label is exactly the partition of the 192 paths into the 2 orbits of 96
under the proper half of order 192.

This is consistent with the holder computation: all 192 path holders have determinant +1,
so they sit in the proper half — which is what makes the label well defined in the first
place.

**T6 (neither factor alone).** Of the 192 proper maps, those preserving the axis order
sign by itself number 96, and those preserving the start corner parity by itself number
96. Those preserving the product number 192, all of them. So neither factor is an
invariant of the object; only the product is. The handedness is genuinely a property of
the path, not of either half of its naming.

## 6. What the label does to covers and to cuttings

The 192 covers of 8 are acted on differently from the paths: their holders are all single
axis flips, of determinant -1, and under the proper half of order 192 they form 1 orbit of
192 with holder of order 1, where the paths form 2 orbits of 96.

That difference has an immediate consequence. Every one of the 192 covers splits 4 and 4
by label. This is forced by counting once the split is known to be constant: each piece
sits in 8 covers, so 192 times 4 = 768 = 96 times 8.

On cuttings, write the left count of a cutting as the number of its 24 pieces with label
+1. Measured over all 15800 cuttings, the census is 8:120, 10:2832, 12:9896, 14:2832 and
16:120. The total is 189600 = 96 times 1975 left slots, so the mean left count is exactly
12. The census is symmetric about 12, the number of cuttings with an odd left count is 0,
and the range is 8 to 16.

The symmetry statement is explained by the maps: the improper half reverses the label, so
it carries a cutting of left count L to one of left count 24 - L. The evenness and the
range are not explained here, and section 7 says so.

Two further facts about how the group sees cuttings. Under the full 384 the cuttings fall
into 74 orbits, and under the proper 192 into 119; both generated sets are verified by
closure. The full orbit sizes are 8 on 1 orbit, 24 on 4, 32 on 1, 48 on 7, 64 on 1, 96 on
11, 192 on 24 and 384 on 25, and 25 of the 74 contain a cutting whose left count is not
12. The 240 cuttings of extremal left count 8 or 16 form 14 proper orbits, of sizes 12 on
8 orbits and 24 on 6 — all far below the group order 192. So the most one-sided cuttings
are also the most symmetric ones.

Across dimensions, closure gives group orders 4, 24, 192 and 1920 at n = 2, 3, 4 and 5,
every element of determinant +1; the path counts are 4, 24, 192 and 1920; and the orbit
sizes are 4:1, 12:2, 96:2 and 1920:1. The label exists — that is, the paths split into 2
orbits under the proper half — exactly at n = 3 and n = 4 within the swept range, which is
exactly where the swap determinant is +1. At n = 2 and n = 5 the proper half is already
transitive on paths, and there is nothing to label.

## 7. Boundary and honest auditor read

What is derived here: the identification of the 192 pieces with the staircase paths, the
closed form 16 times 24 divided by 2 for their count, the order-2 holder from simple
transitivity, the determinant (-1)^(n(n+1)/2) of the naming swap from the flip-weight
parity argument, the cocycle law over all 73728 pairs, and the 4-and-4 split of every
cover from 192 times 4 = 768 = 96 times 8.

What is **measured, not derived**, stated plainly:

* **the even left count of every cutting.** That all 15800 cuttings have an even left
  count is a measurement — 0 cuttings with an odd count. No argument here forces it.
* **the range 8 to 16, a spread of 8, on the left count.** That the imbalance never
  exceeds this bound is likewise a measurement over the 15800 cuttings, not a consequence
  of anything proved above.

That both are measured rather than derived is shown by a control, gate L16: replace the
lowest-indexed piece of a cutting by the lowest-indexed piece it omits, and the left count
comes out odd in 200 of 200 sampled cases and in 7900 of 15800 overall. So evenness is a
property of being a cutting, not of being a 24-piece set of paths. The control is
deliberately degenerate — all 200 sampled cases share the same replaced piece and the same
replacement — and it is reported as a control, not as a statistic.

The three corner statistics in gate L18 are **honest negatives at chance**: the parity of
the total corner weight agrees with the label on 96 of 192 paths, the parity of the corner
index sum on 96 of 192, and the sign of the determinant of the sorted corner matrix on 96
of 192. Each is exactly chance. None of them is the label, and none is offered as
evidence for it; they are recorded so that the label is not mistaken for a repackaging of
a simpler corner statistic.

The claim type is bounded_theorem because the derived part is a theorem about the cell
object as rebuilt, while the two cutting-level facts above remain measurements. The
natural next path is to ask what forces the evenness — a parity constraint on how a
cutting meets the 192 covers would do it, since each cover contributes 4 and 4.

## 8. Gate list with the measured numbers

All 19 gates are computational identities about the explicitly rebuilt finite object,
exact over the integers; no floating point enters any gate. The runner is
`scripts/physical_cell_cutting_path_handedness_cycle779_2026_08_11.py`.

* **L0** object anchor: 2672 unit pieces, cost floor 6, 400 at the floor, 15800 cuttings
  of 24, 192 pieces each in 1975, 379200 slots, 192 covers of 8, 384 maps.
* **L1** degree profiles at the floor: (1,1,1,1,4) 16, (1,1,1,2,3) 192, (1,1,2,2,2) 192,
  sum 400 of 400; all 2672 pieces show 9 profiles.
* **L2** the identification: the 192 used pieces are exactly the 192 staircase paths, both
  differences empty; the other 208 floor pieces occur in 0 cuttings.
* **L3** namings: 16 start corners times 24 axis orders = 384, every path named exactly 2
  times, 384 // 2 = 192 paths.
* **L4** simple transitivity: each of the 384 namings reached by exactly 1 of the 384
  maps; namings whose count is not 1: 0.
* **L5** holders: each of the 192 paths held by a group of order exactly 2 whose second
  map swaps its two namings; paths failing: 0.
* **L6** swap determinants at n = 1 to 6: -1,-1,1,1,-1,-1; 2 fixers at each n; the closed
  form (-1)^(n(n+1)/2) agrees; the n = 4 flip weights are 0 on 48, 2 on 96, 4 on 48, all
  even.
* **L7** all 192 path holders have determinant +1; the 192 cover holders are single axis
  flips of determinant -1.
* **L8** under the proper half of order 192 the paths fall into 2 orbits of 96 and the
  covers into 1 orbit of 192 with holder of order 1.
* **L9** the transformation law on all 384 times 192 = 73728 pairs; failures 0.
* **L10** the label is single valued on 192 of 192 paths, equals the orbit label on 192 of
  192, plus count 96.
* **L11** of the 192 proper maps, 96 keep the axis order sign alone, 96 keep the start
  corner parity alone, 192 keep the product.
* **L12** every one of the 192 covers splits 4 and 4; each piece sits in 8 covers;
  192 times 4 = 768 = 96 times 8.
* **L13** left count census 8:120, 10:2832, 12:9896, 14:2832, 16:120, sum 15800; left
  slots 189600 = 96 times 1975; mean 12; odd counts 0; range 8 to 16.
* **L14** cutting orbits 74 under 384 and 119 under the proper 192, generating sets
  verified by closure; sizes 8:1, 24:4, 32:1, 48:7, 64:1, 96:11, 192:24, 384:25; orbits
  meeting an unbalanced cutting 25.
* **L15** the 240 extremal cuttings form 14 proper orbits of sizes 12:8 and 24:6.
* **L16** the control: odd left count in 200 of 200 sampled and 7900 of 15800 overall.
* **L17** closure orders 4, 24, 192, 1920 at n = 2, 3, 4, 5, all of determinant +1; path
  counts 4, 24, 192, 1920; orbit sizes 4:1, 12:2, 96:2, 1920:1.
* **L18** honest negatives at chance: corner weight parity 96, corner index sum parity 96,
  sorted corner determinant sign 96, each of 192.

# Referee report: J:derive:formation-clauses-in-level-time:a1

- **Author:** w-macbookpro90c72-je0c4 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j33d0 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-je0c4__3811449d__20260919T011456Z`.

`check.py` is independent code: exact Fractions, with numpy integers for the `6^8` static sum. Nothing is taken from the author's script.

## The claim

The setting is the six-axis product rule at `(3,1,2)`.
1. **Product formula.** For a sequential order,
   `P_σ(all +x) = ∏ p^{kᵢ}/(p^{kᵢ} + q^{kᵢ} + 4r^{kᵢ})`, where `kᵢ` counts the neighbours already formed.
2. **Four distinct masses on the cube.**

   | law | `P(all +x)` |
   |---|---|
   | monotone, reverse and corner orders | `2187/44994560` |
   | opposite-corners-first | `81/2048000` |
   | static | `59049/775835648` |
   | uniform clocks | `338229/7997080000` |

3. **NEC kernels.** The unanimous and copy kernels of the NEC automaton are the `k = 3` and `k = 1` cases.
4. **Levels.** A level is an independent set.
5. **The slab.** On the `3×3×2` slab, the level and centre-first orders give different histograms and masses.
6. **Order independence.** "The unique order-independent recorded clause for a finished window is joint formation of that window."

## Step by step

**Step 1 (product formula): holds.** K1: the chain rule, computed from the rule itself, reproduces the product for four orders.

**Step 2 (cube k-multisets): holds.** K2:
- the monotone, reverse and corner-(1,1,1) orders give `(0,1,1,1,2,2,2,3)`;
- opposite-first gives `(0,0,1,1,1,3,3,3)`.

**Step 3 (four masses): holds.** K3:
- monotone `2187/44994560`;
- opposite-first `81/2048000`;
- static `59049/775835648`, with `Z = 6982520832` summed over all `6^8` configurations;
- uniform clocks `338229/7997080000`, averaged exactly over all `8!` orders.

The four are pairwise distinct.

**Step 4 (NEC kernels): holds.** K4:
- `ε₀ = 11/20`;
- on the triple `(+x,+x,+y)`, `P(+x), P(+y)` is `9/26, 3/13` at `(3,1,2)` and `1/26, 1/13` at `(1,3,2)`.

**Step 5 (a level is an independent set): holds.** Adjacent sites differ by 1 in `x + y + z`.

**Step 7 (slab): holds.** K5:
- the k-histograms are `{0:1, 1:5, 2:8, 3:4}` for the level order and `{0:2, 1:3, 2:9, 3:4}` for centre-first;
- the two masses are the ones the attempt prints.

**Step 6 (order independence): does not follow.** It fails on two counts.
- **Its lemma is false.** The step says the k-multiset "changes as soon as the order is not a linear extension of the same ranked poset".
  K6(a) finds otherwise:
  - 4224 of the `8!` orders carry the monotone multiset, and so the monotone all-+x mass;
  - 3936 of those are linear extensions of no corner ranking. The lexicographic order is one of them.
- **The rate clause is never examined.** The argument compares sequential orders with joint formation only.
  - The equal-rate clock law involves no chosen order. It is the uniform mixture, and the attempt computes it.
  - With unequal rates the law moves. K6(b): three random integer rate profiles give `4.120e-5`, `4.254e-5` and `4.295e-5`, against
    `4.229e-5` at equal rates.

  "Unique order-independent clause = joint formation" therefore needs two things the attempt does not supply. It must read
  order-independence to cover rate-independence, and it must argue the rate case. It would also need either a proof that sequential
  differs from joint on every window with a cycle, which is block 15's normalizer lemma, not re-proved or cited, or the citation itself.

## Verdict

The claim fails at step 6. All the finite results of steps 1–5 and 7 hold exactly.

`check.py` prints `SUMMARY: fails at step 6 - ...` and no HIT line.

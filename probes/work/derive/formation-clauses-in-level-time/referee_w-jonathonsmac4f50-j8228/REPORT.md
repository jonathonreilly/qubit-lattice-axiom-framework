# Referee report: J:derive:formation-clauses-in-level-time:a3

- **Author:** w-macbookpro90c72-j8dec (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j8228 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j8dec__033f9e6c__20260919T010154Z`.

**Disclosure.** This referee's model family has already refereed two other attempts of this problem:
- a1 (`referee_w-jonathonsmac4f50-j33d0`) failed at step 6;
- a2 (`referee_w-jonathonsmac4f50-jafa6`) failed at (c).

`check.py` is independent code: exact Fractions, integer enumeration of `6⁸` for the cube, and dynamic programming over subsets.

## The claim

The strong-coupling law is the north-east-centre noisy majority (NEC) iff three conditions hold:
- **(N1)** sites form independently;
- **(N2)** monotone level order;
- **(N3)** free window.

Each other recorded clause breaks one of these. The attempt adds:
- the closed-form noise map;
- four distinct all-`+x` probabilities on the cube, one per clause;
- "joint units fail (N1)", with a fork-pair witness;
- the unrecorded-exterior factor `M`;
- slab `k`-histogram order dependence;
- joint formation of the whole window as the unique order-independent clause.

## Step by step

**Step 1 (noise map): holds.** C1 gives `(11/20, 17/26, 35/44)` at `(3,1,2)` and `ε₂ = 33/1033` at `(10,1,2)`.

The step cites block 12's "majority is the mode iff `p > max(q,r)`", which is false for the antipodal pattern: it needs `p²q > r³` too
(#8413). The attempt uses it only at `(3,1,2)` and `(10,1,2)`, where `9 > 8` and `100 > 8` hold, so nothing downstream breaks.

**Step 2 (criterion): the sufficiency holds.** The role of (N1) is undercut by step 4 below.

**Step 3 (clocks, cube numbers): holds.** C2 re-derives all four numbers on the isolated cube (12 bonds):

| Clause | `P(all +x)` |
|---|---|
| monotone | `2187/44994560` |
| seeded jump chain | `84807/1799782400` |
| uniform mixture over `8!` orders | `338229/7997080000` |
| joint | `59049/775835648`, with `Z = 6982520832` |

`TV(monotone, joint) = 0.0505159881`, which equals the stated `1182193085/23402354976`.

**Step 4 (joint units fail (N1)): does not follow.**
- **No bond between same-level sites.** The fork offset `e_i − e_j` has squared length 2. On `Z³` with nearest-neighbour bonds, two sites on
  the same level are never neighbours, so the rule puts no `φ` factor between them.
- **The fork pair.** With three frozen `+x` predecessors each, joint formation of `{z − e₁, z − e₂}` is exactly the product of the two NEC
  kernels: `TV = 0`, `P(both +x) = 81/400` (C3). So is joint formation of a whole level, which has no internal bond (level 1 of the cube has
  0 bonds).
- **Where the attempt's numbers come from.** Its `2187/7876` and `TV(joint, NEC) = 360383/3544200` come back exactly when an extra
  `φ(s_u, s_v)` bond is added, a bond the rule does not have.
- **What remains true.** "Joint formation of a connected unit (in particular of a whole level …) is not the NEC automaton" is false for a
  level. Joint units differ from NEC only when they contain a bond, which means they span two levels. The joint whole-window (static) law
  does differ, and step 3's cube TV shows it.

**Step 5 (unrecorded exterior): holds.** C4 gives `M ∈ {22, 24, 26}` at `(3,1,2)` and `TV = 1/72`.

**Step 6 (six constants): holds** by covariance.

**Step 7 (order independence): holds on the finite facts.** C5 checks the `3×3×2` slab:
- a connected monotone order from a corner has histogram `(0:1, 1:5, 2:8, 3:4)` and `P = 94143178827/68428452520263680000`;
- a two-seed connected growth with histogram `(0:2, 1:3, 2:9, 3:4)` exists (found by random search);
- its `P = 282429536481/222392470690856960000` is smaller, as stated.

## Verdict

**Fails at step 4.** The fork-pair witness adds a bond that the rule on `Z³` does not have. Joint formation of a same-level unit, and of a
whole level, is exactly the NEC product. So "joint units fail (N1)" is not shown, and it is false for level units.

What survives, re-derived:
- the noise map;
- the four cube probabilities, the joint `Z` and the cube TV;
- block 24's `M` and `1/72`;
- the slab histograms and probabilities.

`check.py` prints `SUMMARY: fails at step 4 - ...` with no HIT line.

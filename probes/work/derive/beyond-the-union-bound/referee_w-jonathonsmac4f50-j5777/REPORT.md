# Referee report: J:derive:beyond-the-union-bound:a1

- **Author:** w-macbookpro90c72-j9773 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j5777 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j9773__10985cb5__20260919T014114Z`.

**Disclosure.** This referee's model family has already refereed a2 (`referee_w-jonathonsmac4f50-j3743`) and a4
(`referee_w-jonathonsmac4f50-j10d4`) of this problem.

`check.py` uses my own two-level automaton and exact enumeration. The histories come from the note's own block-30 construction
(`supervisor_control_block30_core.py`), read unmodified from PR #8174's branch, not from the author's explainer.

## The claim

The attempt presents a no-go for candidate (iii), second-order inclusion–exclusion.
- **(i)** The construction's history events `A_h` partition `{η'_x = 1}`, so inclusion–exclusion on them is vacuous.
- **(ii)** The order-2 truncation is a lower bound, not an upper bound.
- **(iii)** Cylinder overlaps "do not change the 4/27 grammar radius".

The HIT line adds that Chung–Erdős on the cylinders does not beat the union bound.

## Step by step

**Step 1 (Bonferroni order 2 is a lower bound): holds.**

**Step 2 (the construction partitions the 1-event): holds.** The map is deterministic. R1 re-derives the census:
- 308 `η'` patterns on the depth-2 cone, 234 of them with `η'_x = 1`;
- `P(η'_x = 1) = 384159107/2000000000 = 0.19208` at `(1/10, 1/5)`.

The note's own construction yields 92 distinct trees, with 90 distinct cylinders. The attempt's own explainer gave 96 keys, so it is not the
note's construction, although the difference is small.

**Step 3 (inclusion–exclusion on the `A_h` is vacuous): holds, but it is beside the point.** The union bound in blocks 25 and 30 sums over
cylinders `C_h ⊇ A_h`, not over the disjoint `A_h`. Candidate (iii) concerns overlaps of cylinders.

**Step 4 (no-go for inclusion–exclusion on cylinders): does not follow.**
- **The argument.** The attempt gives one constant ratio at one `(ε₁, ε₂)` and the sentence "the grammar-radius obstruction … is
  independent of those overlaps". That is an assertion, not a proof.
- **A valid second-order upper bound exists.** Hunter's bound is the first-order sum minus a maximum spanning tree of pairwise
  intersections. On the depth-2 cone (R2):
  - it gives `0.23640`, against the first-order `0.32810`, which is 72%;
  - the exact union of the cylinders is `0.19208`, equal to `P(η'_x = 1)`.

  So second-order inclusion–exclusion on cylinders does cut the count here. Whether it moves the radius `4/27` is not decided.

- **The order-2 truncation number is wrong.** The attempt's check C1 reports `0.139484`. Its code skips any pair where a site is a seed in
  one cylinder and amplified in the other, treating the cylinders as disjoint. They are not: `U < ε₁` satisfies both. With the
  intersections computed correctly, the truncation is `0.007041` on the note's trees. It remains a lower bound, which is the qualitative
  point.

- **The Chung–Erdős check (C2 and the HIT line) is not a bound.**
  - The number used is `(Σw)²/Σw²`, the diagonal only. It is `9.09` here, above 1.
  - The actual Chung–Erdős inequality, with the full double sum, is a lower bound on `P(∪)`. Here it is `0.1646 ≤ 0.19208`, so it could
    never "beat" an upper bound.

**Step 5 (reading of the truncation as an upper bound is the failing step of naive (iii)): holds.**

## Verdict

**Fails at step 4.** The no-go on cylinder inclusion–exclusion, which is the actual content of candidate (iii), is asserted, not proved.
On the depth-2 cone, Hunter's second-order upper bound improves the first-order union by 28%.

Two supporting numbers are also wrong:
- the order-2 truncation is `0.00704`, not `0.1395`;
- the "Chung–Erdős" quantity is not a bound.

What survives:
- steps 1–3;
- the census (308, 234, `P = 0.19208`).

`check.py` prints `SUMMARY: fails at step 4 - ...` with no HIT line.

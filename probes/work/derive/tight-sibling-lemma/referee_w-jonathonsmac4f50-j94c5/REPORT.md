# Referee report: J:derive:tight-sibling-lemma:a6

- **Author:** w-macbookpro90c72-jf526 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j94c5 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `69037d51`, and its log.

`check.py` in this directory re-realizes the three named windows with this referee's own automaton. The marks of `W1`,
`Z_A` and `Z_B` are read from `probes/lib/family.py` as data. The single-seed rooted values come from a 0-1 integer program
(scipy `milp`), not from `family.single_seed_min`. The program minimizes `#processed − #amplified` over node sets that hold
the site, contain at most one seed, and give every non-seed node a chosen 1-predecessor. It agrees with brute-force
enumeration over all node sets at the 45 sites small enough to enumerate (T5).

## The claim

Route (iv) of the task: block 31's two-level-period witness `W1` and the controls `Z_A`, `Z_B` are not counterexamples to
the tight-sibling lemma. The attempt gives these exact single-seed values:
- `v(W1 root) = −2`;
- `v(Z_A root) = 0`, with three processed 1-predecessors at `−1`;
- `v(Z_B root) = 0`, with predecessor values `{−1, −1, 0}`.

"The hard case … does not occur." `W2` and `W3` are set aside because they "have multiple seeds, so single-seed DP does not
apply".

## Step by step

**Steps 1–2 (W1): hold.**
- `W1` has one seed at levels up to its root's, so its single-seed values are its rooted values (T1).
- `v(root) = −2`.
- 10 processed sites have only processed 1-predecessors, and those predecessors' values reach at most `−1`. So no hard site
  occurs (T2).

**Step 3 (Z_A): the values hold as single-seed values; "the root is tight" does not follow.**
- The single-seed values match the attempt's: root `0`, and predecessors `(2,3,3)`, `(3,2,3)`, `(3,3,2)`, all processed, at
  `−1` (T3).
- `Z_A` has 3 seeds at levels up to its root's (T1). The rooted value is a minimum over the whole family, which contains
  multi-seed trees with forks. On a multi-seed window the single-seed value is only an upper bound on it.
- So "Root `(3,3,3)` is tight (`v = 0`)" is not established.
- The attempt's own reason for setting aside `W2` and `W3`, "multiple seeds", applies to `Z_A` too.
- The negative survives anyway. Every processed site of `Z_A` with only processed 1-predecessors has a predecessor of
  single-seed value `< 0`. Its rooted value is then `< 0` too, so it is not tight, and no hard site occurs (T3).

**Step 4 (Z_B): the same.**
- Single-seed values: root `0`, predecessors `{−1, −1, 0}` (T4).
- `Z_B` has 8 seeds at levels up to its root's (T1), so "the root is tight" is not established.
- Every all-processed site has a predecessor of single-seed value `< 0`, so no hard site occurs.
- No site lacks a single-seed tree (T4).

**Step 5 (no-go on the named set): holds** as a statement about `W1`, `Z_A` and `Z_B`. It is not a statement about `W2`
and `W3`, as the attempt says.

## Classic failure modes

- *A quantity used beyond its scope.* Single-seed values are read as rooted values on windows with several seeds
  (Steps 3–4).
- *Quantifier.* The negative is stated for the named set only. Correct.

## Verdict

**First failing step: 3.** The attempt treats `Z_A` and `Z_B` as single-seed windows. They have 3 and 8 seeds, so the
tightness of their roots, stated in Steps 3–4 and in the HIT line, is not established.

The substantive negative survives, re-derived independently: no hard site occurs on `W1`, `Z_A` or `Z_B`, because in each
window every candidate site has a predecessor whose rooted value is `< 0`.

`check.py` prints `SUMMARY: fails at step 3 - ...` and no `HIT: confirmed` line.

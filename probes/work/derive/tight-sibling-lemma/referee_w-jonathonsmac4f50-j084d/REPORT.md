# Referee report: J:derive:tight-sibling-lemma:a5

- **Author:** w-macbookpro90c72-jbe4a (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j084d (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jbe4a__4e191693__20260919T012832Z`.

**Provenance.** `check.py` uses its own automaton and its own family machinery:
- For the cube, it enumerates the family exhaustively, with forks and the level cap. That code is the one this referee's model family
  wrote for the a4 referee (`referee_w-jonathonsmac4f50-jc833`). a4 is a separate grok attempt with the same census, confirmed in #8354.
- For the witness windows, it solves a 0-1 program and then verifies the resulting tree exactly.

The only thing taken from `probes/lib/family.py` is the witness data `W1`, `W2`, `W3`. Nothing is taken from the author's script.

## The claim

1. **The cube.** On the isolated cube `{0,1}³`, take the 32 noise patterns in which the top is processed with at least two processed
   1-predecessors. In all of them, those predecessors have rooted values in `{−5, −2}` (48 each), never 0.
2. **Block 31's witnesses.** W1, W2 and W3 are not tight-sibling counterexamples.

The lemma on `Z³` is not claimed.

## Step by step

**Step 1 (cube census): holds.** C1 recomputes, with the level cap `≤ level(z)` of the task's definition and the full family including
forks:
- `η(top) = 1` in 212 of 256 patterns;
- the top is processed in 168;
- it has at least two processed 1-predecessors in 32;
- those predecessors' values are `{−5: 48, −2: 48}`.

**Step 2 (W1, W2, W3): holds, but not for the attempt's reason.**
- **The attempt's evidence is not what it says.** Its check prints `brute=` from `single_seed_min` whenever a window has more than 14
  1-sites. All three windows do: 36, 56 and 109 1-sites (C4).
  - W1's "brute_min = −2" is therefore a single-seed value.
  - For W2 and W3 both printed values are `None`, and the check counts `None` as "not tight".
- **The statement is still true, in a stronger form than claimed.**
  - C2: each declared root is processed, with one amplified and one processed 1-predecessor. So the lemma's hypothesis, that all
    1-predecessors are tight processed sites, fails at the declared roots whatever the tightness.
  - C3: check every processed site of each window whose 1-predecessors are all processed (10, 15 and 30 sites). At each one, some
    predecessor has an explicit single-seed tree of negative cost with all nodes at levels at or below its own. Each tree is verified
    exactly. So that predecessor has `v < 0`, and no site of W1, W2 or W3 meets the hypothesis.
  - The capped single-seed optima at the roots' processed predecessors are `−2`, `−3` and `−5`. These are upper bounds on `v`, so none
    of the three is tight.

**Step 3 (isolation): stated correctly as the limit** of the cube census.

## Classic failure modes

- **Scope.** Both results are finite facts: an isolated cube, and three recorded windows. They carry no evidence about marks below the
  cube, as the attempt says.
- **Vacuous check.** The attempt's W2/W3 check passes on `None`. It is replaced here by exact trees.

## Verdict

The partial claim survives, with the W1–W3 evidence corrected as in step 2 above.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.

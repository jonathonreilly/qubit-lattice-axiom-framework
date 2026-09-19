# Referee report: J:derive:tight-sibling-lemma:a4

- **Author:** w-macbookpro90c72-j4a4x (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jc833 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `10985cb5`, and its log.

`check.py` in this directory uses its own two-level automaton on the isolated cube `{0,1}³`, with sites outside it set to 0.
It also enumerates the counted family itself: node sets through 1-sites that contain the root, one arrow per non-seed node
to a 1-predecessor in the set, and arborescences joined by forks between siblings in the set, with `F = |S| − 1`. The value
is `E − 3(|S| − 1) − |A|`. Nothing from `probes/lib/family.py` is used.

## The claim

On the isolated `2×2×2` cube there are 32 noise patterns, out of 256, in which the top site is processed with at least two
processed 1-predecessors. In all of them the top's rooted value is `−4` or `−1`, 16 patterns each, and never positive. So
the lemma's conclusion holds on this cone although the predecessors are not tight. The attempt says the lemma on `Z³` is not
proved.

## Step by step

**Step 1 (census): holds.** R1 finds 32 patterns with values `{−4: 16, −1: 16}` and none positive.

**Step 2 (reading): holds.** R2 finds the processed predecessors in those patterns at `{−5: 48, −2: 48}`. None is tight,
so the lemma's hypothesis never occurs on the isolated cube, and the census is consistent with the lemma without testing it.

**Step 3 (isolation): stated as a limitation**, correctly.

## Classic failure modes

- *Scope.* The result is a finite fact on an isolated cube. It carries no evidence about configurations with marks below the
  cube, and the attempt says so.
- *Quantifier and circularity.* None.

## Verdict

The stated finite census survives, re-derived with independent code. Its scope is the isolated cube only.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.

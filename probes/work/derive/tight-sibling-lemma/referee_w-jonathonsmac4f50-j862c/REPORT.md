# Referee report: J:derive:tight-sibling-lemma:a2

- **Author:** w-macbookpro90c72-j7021 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j862c (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j7021__92a42390__20260919T014801Z`.

**Disclosure.** This referee's model family has already refereed four other attempts of this problem:

| Attempt | Referee directory |
|---|---|
| a1 | `referee_w-jonathonsmac4f50-jdedc` |
| a4 | `referee_w-jonathonsmac4f50-jc833` |
| a5 | `referee_w-jonathonsmac4f50-j084d` |
| a6 | `referee_w-jonathonsmac4f50-j94c5` |

The automaton and family enumeration in `check.py` are the referee family's own code, extended here with a switch for the level cap. None
of `probes/lib/family.py` is used.

## The definition

The task defines the rooted value as the minimum, over trees of the family containing `z` with **all nodes at levels ≤ level(z)**, of
`E − 3(|S| − 1) − |A|`. A site is tight when `v = 0`.

## The claim

The attempt claims a census on the isolated `2×2×2` cube:
- over all 256 noise patterns, `brute_min(c=1)` takes 1204 values at the 1-sites, with `n_none = 0`;
- the values lie in `{−6..0}`, and 48 of them are tight;
- none is positive, "so `v ≤ 0` is a local potential bound on this cone".

## Step by step

**Step 1 (census): does not follow.** The census is of `family.py`'s `brute_min`, and that function takes the other nodes from all 1-sites.
It omits the definition's cap at levels `≤ level(z)`.

- **R0.** With the cap removed, my code reproduces the author's counts exactly:

  | Value | Count |
  |---|---|
  | −6 | 90 |
  | −5 | 178 |
  | −4 | 226 |
  | −3 | 352 |
  | −2 | 222 |
  | −1 | 88 |
  | 0 | 48 |

- **The inference fails.** The uncapped family is larger, so `brute_min ≤ v`. "`brute_min` never positive, so `v ≤ 0`" draws the inequality
  the wrong way round, and the "48 tight" are not tight sites of `v`.
- **R1.** The rooted value itself, with the cap, is also never positive on the isolated cube. It has 1204 evaluations and none without a
  tree. The distribution is different:

  | Value | Count |
  |---|---|
  | −6 | 78 |
  | −5 | 124 |
  | −4 | 130 |
  | −3 | 300 |
  | −2 | 258 |
  | −1 | 106 |
  | 0 | 208 |

  So there are 208 tight sites, not 48.

The conclusion `v ≤ 0` on this cone is true, but the attempt's check does not establish it.

**Step 2 (reading): holds, with the corrected count.**
- **R2.** Under the definition, all 208 tight sites are seeds. None is a processed sibling of a processed successor, so the lemma's
  hypothesis never occurs on the isolated cube, as the attempt says (citing a5).
- **R3.** At the top site the cap is vacuous. There the capped and uncapped censuses agree: 32 patterns, `−4` and `−1`, 16 each. That is why
  a4's top-only census was unaffected.

**Step 3 (isolation): stated as a limitation, correctly.**

## Note for the tool owner

`probes/lib/family.py`'s `brute_min` does not apply the level cap in the rooted-value definition. At any non-top root it computes a lower
bound on `v`, not `v`. Other attempts that call it at non-top sites are affected in the same way.

## Verdict

**Fails at step 1.** The census computes the uncapped `brute_min`, which is a lower bound on `v`. Its "never positive" does not imply
`v ≤ 0`, and its 48 tight sites are not `v`'s.

What survives, recomputed with the definition's cap: `v ≤ 0` at every 1-site of the isolated cube (1204 evaluations), with 208 tight sites,
all of them seeds.

`check.py` prints `SUMMARY: fails at step 1 - ...` with no HIT line.

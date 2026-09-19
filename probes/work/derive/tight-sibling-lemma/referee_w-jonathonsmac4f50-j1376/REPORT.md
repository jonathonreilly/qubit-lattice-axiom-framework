# Referee report: J:derive:tight-sibling-lemma:a3

- **Author:** w-macbookpro90c72-jf5ff (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j1376 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jf5ff__65e00758__20260919T011420Z`.

**Disclosure.** This referee's model family has already refereed other attempts of this problem:

| Attempt | Referee directory | Outcome |
|---|---|---|
| a1 | `referee_w-jonathonsmac4f50-jdedc` | — |
| a2 | `referee_w-jonathonsmac4f50-j862c` | failed: `family.py`'s `brute_min` omits the level cap |
| a4 | `referee_w-jonathonsmac4f50-jc833` | — |
| a5 | `referee_w-jonathonsmac4f50-j084d` | — |
| a6 | `referee_w-jonathonsmac4f50-j94c5` | — |

`check.py` here is independent code, with its own automaton and family enumeration, capped and uncapped.

## The claim

The claim is a census on the isolated depth-2 cone of `z = (2,2,2)`:
- marks sit on 10 sites, and the automaton runs on the 20-site depth-3 cone with the exterior at 0;
- 512 of the 1024 mark patterns make `z` processed with at least two processed 1-predecessors;
- all 1248 such predecessors have rooted value in `{−5,−6,−8,−9,−11,−14}` and are never tight, and `z` is never positive.

So tight processed siblings sharing a processed successor do not occur on this cone. The lemma on `Z³` is not claimed.

## Step by step

**Step 1 (geometry): holds.** Predecessors of `z` differ by fork offsets. The depth-2 cone has 10 sites and the depth-3 cone has 20.

**Step 2 (kinds): holds.** R1 finds 512 of 1024 patterns and 1248 predecessor instances.

**Step 3 (rooted values): holds, including under the definition's level cap.**
- **The level cap.** The census uses `family.py`'s `brute_min`, which ignores the cap "nodes at levels ≤ level(z)". Referee a2 found this
  changes values at low roots.
- **Why it does not matter here.** The roots are `z`'s level-5 predecessors, and the only higher 1-site in the cone is `z` itself. Adding
  `z` costs `+1` and gives no fork, so the capped and uncapped minima coincide.
- **R2.** My capped and uncapped enumerations both reproduce the author's predecessor distribution exactly:

  | Value | Count |
  |---|---|
  | −5 | 240 |
  | −6 | 96 |
  | −8 | 432 |
  | −9 | 144 |
  | −11 | 288 |
  | −14 | 48 |

  None is tight.
- **The successor.** `z` reproduces as well: `{−4: 112, −6: 48, −7: 168, −8: 24, −9: 48, −10: 96, −13: 16}`, never positive.

**Step 4 (why negative): a heuristic reading.** The attempt says the "possible `(E, A, S)` combinations" produce these values. That is not a
proof, and the census does not need it.

**Step 5 (global gap): holds as a stated limitation.** Rooted trees on `Z³` may use 1-sites outside the cone, so the census does not touch
the lemma.

## Verdict

**The local census survives, re-derived independently.**
- The numbers are 512 patterns, 1248 instances, values `−5 … −14`, and none tight.
- The level-cap issue that sank a2 does not affect these roots.
- The scope is the isolated cone. The attempt says so, and it states that the lemma on `Z³` stays open.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.

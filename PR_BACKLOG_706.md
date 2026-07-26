# Cycle 706 — SELF-ABANDONED (duplicative)

Branch: `physics-loop/confusability-floor-20260725`
Science commit: `2a84603a47` (runner + note committed, cold-run PIN MATCH,
9 PASS / 0 FAIL). **No PR opened. Not sent to the cluster-cap evaluator.**

Abandoned by the campaign's own prior-art sweep, before the value gate was
finished — the same way cycle 703 was abandoned.

## What it duplicated

`docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`
already contains both headline theorems:

| cycle 706 | landed 2026-07-03 |
|---|---|
| **T2** nearest-neighbour occupancy carries no orientation; all 128 patterns have an improper symmetry | **Theorem 2** "Openness-level patterns are automatically achiral" — all 64 colourings proper-equivalent to their `P`-image, Burnside counts 10 and 10 |
| **T3** the alphabet threshold is three; `mult(det) = 3` at alphabet 3 | **Theorem 3** "Chirality requires three condition values, and at exactly three it is unique" — proper/full orbit counts 57 and 56, exactly **one** chiral pair |

My T3 count is not merely duplicative, it is **degraded**. I ran the census on
the seven-site star (six neighbours **plus the origin**). The origin is fixed
by the whole group and contributes an inert factor of 3, so my `3` is the
landed `1` multiplied by a redundant degree of freedom. The landed number is
the correct one.

The landed note also states the consequence I derived by hand — that chirality
"requires distinguishable record contents" — which is the same conclusion as my
scoped `A(m k) = g A(k)` argument, reached more directly.

## What was actually new, and why it is not enough

Only Theorem 1 survives the sweep: that the `L = 2` parity protection is
**general** — on `(Z/2)^3`, `-x = x`, so inversion acts trivially on sites and
every site-data odd channel vanishes at every range and every alphabet
richness, not merely `J2` at range 1. The sweep found no landed statement of
that mechanism.

But it is a one-line observation (`-I = I` on `(Z/2)^3`) plus a census table of
multiplicities. Under the brief's "a thin PR is worse than none", that does not
carry a PR on its own. It is recorded here so the observation is not lost.

## The process failure, which is the reusable part

The note I duplicated was **cited as a dependency in the very note I started
from**. The bootstrap continuation's authorities list contains:

> `ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_..._2026-07-03` — rule-level pair
> dichotomy and one-orientation-bit bookkeeping.

I read the parent, took its residual, and did not follow the parent's own
dependency links. Both duplicated theorems were one hop away the whole time.

**Rule for the next cycle: when working a residual, read the parent's
dependency list before building, not just the parent.** Searching on the
statement (which I did, and which eventually caught this) is the backstop; the
dependency list is the cheap front-line check I skipped.

## Sweep record

- Ref: `origin/main` at `0adcfef114`
- The catching search: `git grep -n -iE "alphabet[^.]{0,80}(threshold|three values|richness)" origin/main -- docs/*.md`
- Also searched: `"three condition values"`, `"small.alphabet"`, `"binary condition"`,
  `"det character.*multiplicit"`, `"odd channel.*(count|census|multiplicit)"`,
  `"improper (symmetry|stabilizer).*(pattern|occupancy|neighbour)"`,
  `"inversion acts trivially"`, `"L ?= ?2.*(every range|all ranges|any range)"`

This is the **sixth** duplication the sweep has caught in this campaign
(AC route (b), the admissibility-rule census, the cubic-orbit Reynolds prior
art, cycle 703, the two bootstrap theorems answering my formation leads, and
now cycle 706). The sweep continues to pay for itself.

## Recovery

```
git checkout physics-loop/confusability-floor-20260725   # 2a84603a47
python3 scripts/physical_odd_channel_quotient_threshold_census_cycle706_2026_07_25.py
```

The runner is correct and cold-run verified; it is kept for the `L = 2`
generalization and the census tables, should either become useful as a
component of a larger result.

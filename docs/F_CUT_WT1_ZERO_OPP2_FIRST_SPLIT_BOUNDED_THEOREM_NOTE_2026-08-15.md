---
claim_id: f_cut_wt1_zero_opp2_first_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed of size at most 3 at which F_cut (0,0,1,1,1) and (0,1,1,1,1) disagree on fill is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_wt1_zero_opp2_first_split_2026_08_15.py
---

# First |S|≤3 Fill Split of the wt1=0 Opp2 Pair

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock dynamics on the displayed twelve-vertex
two-cube with off-patch occupancy 0. The two F_cut maps with remaining-bit
tuples `(0,0,1,1,1)` and `(0,1,1,1,1)` are compared on every seed of size at
most 3. The first fill disagreement is displayed. The opp2 bit is not
adopted as axiom content.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_wt1_zero_opp2_first_split_2026_08_15.py`](../scripts/f_cut_wt1_zero_opp2_first_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write the two-cube as the lex-ordered twelve-site patch
`{0,1,2} × {0,1} × {0,1}` of `Z^3`. Off-patch neighbors have occupancy 0.
A cube-covariant complement-even predicate that vanishes on the empty and
full six-neighbor cells is an F_cut map, coded by the five remaining bits
`(wt1, opp2, adj2, tripod, ax1)`.

The maps

```text
f00 = (0,0,1,1,1),    f10 = (0,1,1,1,1)
```

both lie in `Max(11) \ Max(1)` on this patch. They agree on fill for every
seed of size at most 2. The lex-first seed of size at most 3 at which they
disagree on fill is

```text
S = {(0,0,0), (0,1,1), (2,0,0)}.
```

From `S`, `f00` halts at history `(3, 5)` and does not fill; `f10` halts at
history `(3, 6, 8, 11, 12)` and fills. This pair is new relative to the
mix0/L1, wt1=1 comparison: both maps here have `wt1=0` and differ only on
opp2. The split is displayed. It does not adopt opp2.

The predicate `f_L1` used only as vocabulary is `n ≠ 0` (some axis
unbalanced). It is not Hamming parity.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact two-cube occupancy ticks locate the lex-first |S|<=3 fill disagreement of the displayed wt1=0 F_cut pair."
trace_class: frontier_discovery
target_claim_id: f_cut_wt1_zero_opp2_first_split
target_blocker_text: "whether opp2 is dynamically free inside the wt1=0 F_cut pair"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube with off-patch o=0; opp2 is displayed, not adopted"
hypothetical_axiom_status: "none; remaining-bit data are displayed and are not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice, Admissibility, and Record
  sentences below supply the repository's site, nearest-neighbor, and lock
  vocabulary. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-vertex two-cube, off-patch
  occupancy 0, the six-neighbor occupancy cell, the F_cut remaining-bit
  coding, and the simultaneous lock tick are supplied mathematical data for
  this theorem. The axioms do not by themselves name this finite patch or
  the F_cut subclass.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of a remaining bit by Record or
  Admissibility, and any physical reading of opp2, remain separate open
  obligations outside the target proved here.

## Exact Objects

Sites are the lex-ordered tuples

```text
(0,0,0), (0,0,1), (0,1,0), (0,1,1),
(1,0,0), (1,0,1), (1,1,0), (1,1,1),
(2,0,0), (2,0,1), (2,1,0), (2,1,1).
```

The six-neighbor cell of a site `v` relative to a lock set `L` is the
`{0,1}^6` occupancy of `v ± e_i`, with any off-patch neighbor scored 0.
A tick locks every unlocked site whose cell is sent to 1 by the predicate,
all at once, and halts at a fixed point. Fill means the halt lock set is
the whole twelve-site patch. The lock-history of a run is the tuple of
lock-set cardinalities, beginning with `|S|`.

The ten cube-rotation types of `{0,1}^6` are empty, full, weight-1 (and its
complement), opposite-axis pairs `opp2` (and complement), adjacent-axis
pairs `adj2` (and complement), the one-per-axis tripods, and the full-axis
plus one extras `ax1`. Complement-even vanishing on empty and full leaves
five free bits. `f_L1` is the predicate that a cell has some axis with
`c_{+μ} ≠ c_{-μ}`; its remaining-bit tuple is `(1,0,1,1,1)`. Hamming
parity `|c|_1 mod 2` is the different tuple `(1,0,0,1,1)`.

`Max(k)` is the set of F_cut maps attaining the maximum number of filling
`k`-site seeds on this patch. There are `C(12,1) = 12` one-site seeds and
`C(12,11) = 12` eleven-site seeds. Seeds of size at most 3 are enumerated
by increasing cardinality and, within each cardinality, lexicographic order
of the lex-sorted site tuple. That census has `1 + 12 + 66 + 220 = 299`
seeds.

All runner quantities are exact integers. No float is used.

## Exact Target And Proof Obligations

The exact target is to place `f00` and `f10` in `Max(11) \ Max(1)` by a
full 32-map coverage recomputation, and to name the lex-first seed of size
at most 3 at which those two maps disagree on fill.

The obligation graph is:

1. recompute one-site and eleven-site coverage of every F_cut map;
2. confirm both displayed maps attain the eleven-site maximum and miss the
   one-site maximum;
3. scan every seed of size at most 3 in the stated order and report the
   first fill disagreement, together with both halt histories.

All three obligations are closed below and in the runner. Larger seeds,
other remaining-bit pairs, and any adoption of opp2 are outside this
theorem. There is no missing lemma for the bounded target.

## Theorem 1 — both maps lie in `Max(11) \ Max(1)`

Recomputing coverage of all 32 F_cut maps on this patch gives

```text
max cov_1  = 12,   |Max(1)|  = 4,
max cov_11 = 12,   |Max(11)| = 8.
```

The four one-site maximizers all have `wt1 = 1`. In particular
`f_L1 = (1,0,1,1,1)` fills every one-site seed, while

```text
cov_1(f00) = 0,    cov_1(f10) = 0.
```

The eight eleven-site maximizers are the four one-site maximizers together
with the four extras

```text
(0,0,1,1,0), (0,0,1,1,1), (0,1,1,1,0), (0,1,1,1,1).
```

Both `f00` and `f10` fill every eleven-site seed, so both lie in
`Max(11) \ Max(1)`. This is a recomputation of that four-element set, not a
citation of a listing.

## Theorem 2 — lex-first `|S| ≤ 3` fill disagreement

Every seed of size at most 2 produces the same fill bit on `f00` and on
`f10`. The first three-site seed in lex order at which the fill bits
differ is

```text
S = {(0,0,0), (0,1,1), (2,0,0)}.
```

No earlier three-site seed disagrees on fill. Two earlier long-axis
triples,

```text
{(0,0,0), (0,0,1), (2,0,0)}    and    {(0,0,0), (0,1,0), (2,0,0)},
```

already differ in lock history, but both miss fill. The target of this
note is fill, not history, so those triples are not the reported split.

## Theorem 3 — which map fills

From `S` the two runs are:

```text
f00 : history (3, 5),           fill = false,
f10 : history (3, 6, 8, 11, 12), fill = true.
```

The first wave of `f00` is `{(0,0,1), (0,1,0)}`, after which the process
halts with five locks. The first wave of `f10` is
`{(0,0,1), (0,1,0), (1,0,0)}`; the extra lock is the long-axis midpoint,
whose six-neighbor cell is the `opp2` representative with both `±e_1`
occupied. Subsequent waves of `f10` fill the patch.

This exhibits a seed on which the opp2 bit is dynamically visible inside
the `wt1 = 0` pair. Do not adopt opp2. The exhibition is not an adoption
of opp2, and no Admissibility sentence is rewritten.

## Physical-Interpretation Boundary

The proved output is the displayed seed and the two fill bits. This note
neither installs opp2 as a selected remaining bit nor changes the live
Admissibility or Record sentences. Remaining-bit tuples are displayed
predicate data, not axiom content, and no additional
axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. a map does not disagree with itself on any seed of size at most 3;
2. Hamming parity is not `f_L1` and is neither displayed map;
3. the swapped claim "`f00` fills `S` and `f10` misses" is false.

## What This Does Not Claim

- The two-cube is not claimed to be a physically derived finite world.
- The opp2 bit is not adopted, and `f10` is not selected as a physical law.
- No claim is made that Record locks on opp2 cells, or that Admissibility
  prefers either displayed map.
- Agreement on fill for `|S| ≤ 2` is not a claim that the two maps are
  dynamically identical: they already differ in history on earlier
  long-axis triples.
- Seeds of size greater than 3 are not classified.
- Independent class-`C` leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site, nearest-neighbor,
and lock vocabulary. This theorem separately supplies the two-cube, the
F_cut coding, and the seed census; physical interpretation of opp2 remains
outside its target.

## Runner Contract

The companion runner checks Theorems 1–3 with exact integer occupancy
ticks. It recomputes `Max(1)` and `Max(11)` over all 32 F_cut maps, scans
every seed of size at most 3 in lex order, and rejects the three mutations.
It quotes the live axiom sentences, prints substantive N5 scope
certificates, and records the import boundary. Declared review inputs are
this note and the axiom memo only.

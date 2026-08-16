---
claim_id: f_cut_q8_mixed3_cov8_equality_selector_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 15 Q8-true mixed3-pairs of F_cut on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals cov8-equality is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q8_mixed3_cov8_equality_selector_2026_08_15.py
---

# Remaining-Bit Search For Mixed3 Cov8 Equality Inside Q8

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact 8-site occupancy-to-lock coverage of the 30 Q8-true
cube-covariant complement-even maps in `F_cut`, on the twelve-vertex
two-cube, with off-patch occupancy `0`. Those 30 maps form 15 pairs that
differ only by the remaining bit `mixed3`. Whether a displayed 1-bit or
2-bit predicate on the four free bits `(wt1, opp2, adj2, vertex3)` equals
`cov8`-equality on those pairs is reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q8_mixed3_cov8_equality_selector_2026_08_15.py`](../scripts/f_cut_q8_mixed3_cov8_equality_selector_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment mix3c8 reported that only 1 of the 15 Q8-true mixed3-pairs has
equal `cov8`, and that the lex-first split is `(0, 0, 0, 1, 0)` versus
`(0, 0, 0, 1, 1)`. That residual asked an equality count. New selector on the 15 pairs: this note searches remaining-bit predicates on the four free
bits `(wt1, opp2, adj2, vertex3)` for whether
`Equal(f) := cov8(f) = cov8(f` with mixed3 flipped`)`. Not leftover-character of mix3c8: that was the count `N_eq = 1` and the named split, not an iff
against a displayed 1-bit or 2-bit family.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube `{0,1,2}×{0,1}×{0,1}`, each unordered 8-subset of vertices
is an 8-site seed. There are `C(12,8)=495` such seeds. Off-patch neighbors
have occupancy `0`. Each tick, every unlocked on-patch vertex evaluates
`f` on its six-neighbor occupancy tuple and locks if `f=1`. Fill means
the halt set has cardinality 12. Coverage is

```text
cov8(f) = |{ S : |S|=8 and f fills from S }|.
```

A blank-block is a different rule and is not used.

`Q8 = wt1 ∨ opp2 ∨ adj2 ∨ vertex3`. It ignores `mixed3`. The 30 Q8-true
maps form 15 pairs that share a four-bit prefix and differ only in
`mixed3`. For a prefix `p = (wt1, opp2, adj2, vertex3)`,

```text
Equal(p) := cov8(p+(0,)) = cov8(p+(1,)).
```

The displayed remaining-bit family, in this order, is:

1. each 1-bit: `bit:wt1`, `bit:opp2`, `bit:adj2`, `bit:vertex3`;
2. every 2-bit AND of those four bits, in remaining-bit order;
3. every 2-bit OR of those four bits, in remaining-bit order.

Then:

- Theorem 1. None of the displayed 1-bit or 2-bit predicates equals
  `Equal`. The lex-first miss of each displayed `Q` is named below.
- Theorem 2. `N_eq = 1`. For each displayed `Q`, `N_Q` and `N_both` are
  reported below.
- Theorem 3. The displayed family is displayed. Displayed, not adopted.
  Do not adopt a bit.

Do not write any displayed remaining-bit formula into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Independent 8-site coverage of the 30 Q8-true F_cut maps, grouped as 15 mixed3-pairs, is scored against a displayed 1-bit and 2-bit remaining-bit family for equality with Equal. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q8_mixed3_cov8_equality_selector
target_blocker_text: "whether a displayed remaining-bit predicate equals cov8-equality among the 15 Q8-true mixed3-pairs"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed remaining-bit search against cov8-equality; do not adopt a displayed bit"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Current premise boundary

The only scientific dependency is the current four-axiom authority linked
above. The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The axiom memo says the distribution concerns which possibility a forming
record locks, conditional on formation at that site; it does not supply the
formation site, probability, or rate.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no formation-site selector and no occupancy-to-lock
predicate. No displayed remaining-bit formula is axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different rule and is not used.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0.
Complement swaps `n_both` with `n_empty`. The five remaining bits of
`F_cut`, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values
on orbit types `(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`.
Complement partners are forced equal; empty and full are fixed at 0. Thus
`N_free = 5` and `|F_cut| = 32`.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The eight-site seeds are the `C(12,8) = 495` subsets of size 8 in `T`. Then
`cov8(f)` is the number of those subsets from which `f` fills.

`Q8` is true exactly when at least one of `wt1`, `opp2`, `adj2`, `vertex3`
is 1. The two Q8-false maps are `(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`.
The other 30 maps form 15 pairs ordered by the four-bit prefix in lex
order. `Equal` is a predicate on those 15 prefixes.

The displayed remaining-bit family is the four 1-bit predicates and every
2-bit AND or 2-bit OR of `(wt1, opp2, adj2, vertex3)`, listed in
Theorem 1. Displayed, not adopted.

## Theorems

### Theorem 1 — no displayed 1-bit or 2-bit `Q` equals `Equal`

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity. Its remaining
bits are `(1, 0, 1, 1, 1)`, so it is Q8-true.

`Q8` holds on exactly 30 of the 32 maps. Those 30 maps are 15 pairs
differing only by `mixed3`. Exhaustive `cov8` on all 495 eight-site seeds
gives `N_eq = 1` and `N_diff = 14`. The one equal pair is the `opp2`-only
prefix

```text
(0, 1, 0, 0, 0)  cov8 = 1
(0, 1, 0, 0, 1)  cov8 = 1
```

The lex-first pair that differs is still

```text
cov8((0, 0, 0, 1, 0)) = 44
cov8((0, 0, 0, 1, 1)) = 132
```

None of the sixteen displayed predicates equals `Equal`. None of the
displayed 1-bit or 2-bit predicates isolates the unique equal prefix
`(0, 1, 0, 0)`.

The lex-first remaining-bit miss of each displayed `Q`, in the prefix
order `(wt1, opp2, adj2, vertex3)`, is:

- `bit:wt1`: lex-first miss `(0, 1, 0, 0)`
- `bit:opp2`: lex-first miss `(0, 1, 0, 1)`
- `bit:adj2`: lex-first miss `(0, 0, 1, 0)`
- `bit:vertex3`: lex-first miss `(0, 0, 0, 1)`
- `wt1 AND opp2`: lex-first miss `(0, 1, 0, 0)`
- `wt1 AND adj2`: lex-first miss `(0, 1, 0, 0)`
- `wt1 AND vertex3`: lex-first miss `(0, 1, 0, 0)`
- `opp2 AND adj2`: lex-first miss `(0, 1, 0, 0)`
- `opp2 AND vertex3`: lex-first miss `(0, 1, 0, 0)`
- `adj2 AND vertex3`: lex-first miss `(0, 0, 1, 1)`
- `wt1 OR opp2`: lex-first miss `(0, 1, 0, 1)`
- `wt1 OR adj2`: lex-first miss `(0, 0, 1, 0)`
- `wt1 OR vertex3`: lex-first miss `(0, 0, 0, 1)`
- `opp2 OR adj2`: lex-first miss `(0, 0, 1, 0)`
- `opp2 OR vertex3`: lex-first miss `(0, 0, 0, 1)`
- `adj2 OR vertex3`: lex-first miss `(0, 0, 0, 1)`

### Theorem 2 — `N_eq` and, for each displayed Q, `N_Q` and `N_both`

Among the 15 Q8-true mixed3-pairs, `N_eq = 1` prefix has `Equal` true.

For each displayed `Q`, write `N_Q` for the number of prefixes with `Q`
true and `N_both` for the number of prefixes with both `Q` true and
`Equal` true:

- `bit:wt1`: N_Q = 8, N_both = 0
- `bit:opp2`: N_Q = 8, N_both = 1
- `bit:adj2`: N_Q = 8, N_both = 0
- `bit:vertex3`: N_Q = 8, N_both = 0
- `wt1 AND opp2`: N_Q = 4, N_both = 0
- `wt1 AND adj2`: N_Q = 4, N_both = 0
- `wt1 AND vertex3`: N_Q = 4, N_both = 0
- `opp2 AND adj2`: N_Q = 4, N_both = 0
- `opp2 AND vertex3`: N_Q = 4, N_both = 0
- `adj2 AND vertex3`: N_Q = 4, N_both = 0
- `wt1 OR opp2`: N_Q = 12, N_both = 1
- `wt1 OR adj2`: N_Q = 12, N_both = 0
- `wt1 OR vertex3`: N_Q = 12, N_both = 0
- `opp2 OR adj2`: N_Q = 12, N_both = 1
- `opp2 OR vertex3`: N_Q = 12, N_both = 1
- `adj2 OR vertex3`: N_Q = 12, N_both = 0

Every 1-bit predicate has `N_Q = 8 ≠ 1`. Every 2-bit AND has
`N_Q = 4 ≠ 1`. Every 2-bit OR has `N_Q = 12 ≠ 1`. No displayed row has
`N_Q = N_both = N_eq`.

`f_L1` has remaining bits `(1, 0, 1, 1, 1)` and prefix `(1, 0, 1, 1)`.
That pair is unequal (`cov8 = 446` versus `494`), so `Equal` is false on
the `f_L1` prefix. That is consistent with Theorem 2 and does not restore
equality for any displayed `Q`.

### Theorem 3 — display; do not adopt a bit

Every predicate above is displayed. Displayed, not adopted. Do not adopt a
bit. Do not write any displayed remaining-bit formula into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` remaining-bit order | enumerated |
| `Q8 = wt1 ∨ opp2 ∨ adj2 ∨ vertex3` | defined; ignores `mixed3` |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 495 eight-site seeds, off-patch `o=0` | declared finite patch |
| 15 Q8-true mixed3-pairs and `Equal` | enumerated |
| displayed 1-bit and 2-bit family on four free bits | displayed, not adopted |
| some displayed `Q` equals `Equal` | fails; none; lex-first miss of each named |
| `N_eq = 1` and per-`Q` `N_Q`, `N_both` | proved by exhaustive scoring |
| leftover-character of mix3c8 | refused; new selector on the 15 pairs |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of mix3c8: that displayed the equality count
`N_eq = 1` and the lex-first differing pair. The present object is whether
`Equal` iff any displayed 1-bit or 2-bit predicate on the four free bits.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt a bit.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed 1-bit or 2-bit remaining-bit predicate equals `cov8`-equality on the 15 Q8-true mixed3-pairs. |
| V2 | mix3c8 supplied the equality count and the lex-first split, but no landed 1-bit or 2-bit iff search for `Equal`. |
| V3 | The 30 maps, 495 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores `Equal` against a displayed remaining-bit family. |
| V5 | Equality fails for every displayed `Q`, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: none of the displayed 1-bit or 2-bit
predicates equals `Equal` among the 15 Q8-true mixed3-pairs on this
patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover mix3c8 | treat the search as leftover-character of the equality count | **ATTEMPTED** |
| leftover Q8-positivity | treat integer-`cov8` equality as leftover-character of `cov8>0` | **ATTEMPTED** |
| adopt a bit | write a displayed remaining-bit formula into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed 1-bit tests, the failed 2-bit AND/OR tests, the Hamming
contrast, the mix3c8 equality count, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 495 eight-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, the predicate
`Q8`, and the displayed 1-bit and 2-bit family are declared. Equality of
any displayed `Q` with `Equal` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether a displayed
1-bit or 2-bit remaining-bit predicate equals `cov8`-equality on the
declared 15 pairs, not leftover-character of mix3c8.

| Evidence path:line | Residual attacked | Residual claimed closed | Match? |
|---|---|---|---:|
| `docs/MINIMAL_AXIOMS_2026-06-29.md:37` | ambient lattice and cubic rotations | sites are `Z^3` with proper cubic rotations | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:57` | covariant nearest-neighbor rule | covariance is the class filter, not a selector | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:79` | lock permanence | a locked site stays locked | yes |
| `docs/MINIMAL_AXIOMS_2026-06-29.md:83` | unreadability of absence | unlocked and off-patch sites contribute occupancy `0`, not a readout | yes |

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 30 Q8-true maps on all 495 eight-site seeds | no physical law selection |
| per block | `Equal` versus each displayed `Q` on the 15 pairs | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

The runner prints the same five resolution statements.

### N6 — live partial-closure paths

The primitive registry at `docs/audit/data/axiom_premise_nodes.json` was
checked. The only dependency used is the registered `minimal_axioms` node.
None of the approved primitives supplies a Boolean occupancy map, a
seed-coverage ranking, or an Admissibility selector.

Live routes include a different Boolean combination of remaining bits, a
different seed cardinality, a different off-patch rule, a selector outside
the displayed 1-bit and 2-bit family, and any independently derived
physical map from `F_cut` into Admissibility. One partial-closure
mechanism is displayed rather than suppressed: the unique equal prefix is
the `opp2`-only pair. That pair does not select `opp2` or `mixed3`.

### N7 — hostile steelman

**Steelman:** because only one of the 15 prefixes is equal, a 1-bit or a
2-bit AND/OR on the four free bits must recover `Equal`.

**Answer:** Every 1-bit has `N_Q = 8 ≠ 1`. Every 2-bit AND has
`N_Q = 4 ≠ 1`. Every 2-bit OR has `N_Q = 12 ≠ 1`. The unique equal prefix
is `(0, 1, 0, 0)`, which is the conjunction of `opp2` with the three
complementary zeros — a four-bit predicate, not a displayed 1-bit or
2-bit predicate. No bit is adopted.

### N8 — cross-cycle echo

Investment mix3c8 already displayed `N_eq = 1` and the lex-first split
`(0, 0, 0, 1, 0)` versus `(0, 0, 0, 1, 1)`. Echoing that equality count is
not a substitute for scoring the displayed 1-bit and 2-bit family: the
sixteen lex-first misses and the per-`Q` pair `(N_Q, N_both)` are the new
search facts.

| Earlier surface | Similar issue | Mechanism considered here |
|---|---|---|
| `docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md` | proper-cubic covariance of a local rule | covariance is used only as the orbit filter for Boolean maps; that note's quaternion-axis pair is unused |
| `docs/PHYSICAL_SPATIAL_BLOCK_SEAM_DICHOTOMY_CYCLE728_NOTE_2026-08-04.md` | two-cell box `{0,1,2}×{0,1}×{0,1}` | the same twelve spatial vertices are the patch; the seam cost is unused |
| `docs/MINIMAL_AXIOMS_2026-06-29.md` | one covariant nearest-neighbor rule | the axiom names the contract; this note does not select the rule |

No-Go Discipline disposition: **PASS** for the finite search and the
narrow equality failure. FAIL / DO NOT SHIP for “a displayed remaining-bit
predicate equals `cov8`-equality” or “a displayed bit is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov8` on the
495 eight-site seeds, restricts to the 15 Q8-true mixed3-pairs, compares
`Equal` with each displayed 1-bit or 2-bit remaining-bit predicate,
reports that none equals `Equal`, names the lex-first miss of each
displayed `Q`, and reports `N_eq = 1` together with per-`Q` `N_Q` and
`N_both`. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.

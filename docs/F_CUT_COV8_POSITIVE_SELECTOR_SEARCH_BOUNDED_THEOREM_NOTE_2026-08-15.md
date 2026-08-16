---
claim_id: f_cut_cov8_positive_selector_search_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals positive 8-site coverage is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov8_positive_selector_search_2026_08_15.py
---

# Remaining-Bit Search for a Positive 8-Site Coverage Selector

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 495 eight-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`, against a displayed remaining-bit
family.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov8_positive_selector_search_2026_08_15.py`](../scripts/f_cut_cov8_positive_selector_search_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6527 showed that `cov8>0` is not `Q4`, with `N_Q4 = 24`,
`N_pos = 30`, and `N_both = 24`. Six `Q4`-false maps still have `cov8>0`.
This note searches a new displayed family on the same eight-site seeds:
each 1-bit, each `wt1`-AND-bit, `Q4 ∨ vertex3`, and every 2-bit OR of the
five remaining bits. New k-selector after Q4 failed at k=8, not
leftover-character of #6527 and not a unique-maximizer rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov8(f) = |{S : |S|=8 and f fills from S}|`. The boolean scored here is
`cov8(f)>0`. Then:

- Theorem 1. None of the displayed remaining-bit predicates equals `cov8>0`.
  The lex-first remaining-bit miss of each displayed `Q` is named below.
- Theorem 2. `N_pos = 30`. For each displayed `Q`, `N_Q` and `N_both` are
  reported below.
- Theorem 3. The displayed family is displayed. Displayed, not adopted.
  Do not adopt a bit.

Do not write any displayed remaining-bit predicate into Admissibility. The
extra that would have made a 1-bit, a `wt1`-AND-bit, `Q4 ∨ vertex3`, or a
2-bit OR the positivity selector at `k=8` is not present.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 495 eight-site seeds of the two-cube. Whether any displayed remaining-bit predicate equals cov8>0, and the counts N_pos, N_Q, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov8_positive_selector_search
target_blocker_text: "whether a displayed remaining-bit predicate equals cov8>0 among the 32 F_cut maps after Q4 failed at k=8"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded remaining-bit search against cov8>0; do not adopt a displayed bit"
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
`cov8(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov8(f)>0`.

The displayed remaining-bit family, in this order, is:

1. each 1-bit: `bit:wt1`, `bit:opp2`, `bit:adj2`, `bit:vertex3`, `bit:mixed3`;
2. each `wt1`-AND-bit other than `wt1` itself: `wt1&opp2`, `wt1&adj2`,
   `wt1&vertex3`, `wt1&mixed3`;
3. `Q4|vertex3`, where `Q4(f) := (wt1 = 1) or (adj2 = 1)`;
4. every 2-bit OR: `wt1|opp2`, `wt1|adj2`, `wt1|vertex3`, `wt1|mixed3`,
   `opp2|adj2`, `opp2|vertex3`, `opp2|mixed3`, `adj2|vertex3`,
   `adj2|mixed3`, `vertex3|mixed3`.

Displayed, not adopted. `wt1|adj2` is the same formula as `Q4`.

## Theorem 1 — none of the displayed Q equals `cov8>0`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov8` on the 495
eight-site seeds. For each displayed `Q`, compare the set of maps with
`Q` true to the set of maps with `cov8>0`.

None of the twenty displayed predicates equals `cov8>0`.

The two maps with `cov8 = 0` are `(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`.
The six `Q4`-false maps that still have `cov8>0` are

```text
(0, 1, 0, 0, 0), (0, 1, 0, 0, 1), (0, 0, 0, 1, 0),
(0, 1, 0, 1, 0), (0, 0, 0, 1, 1), (0, 1, 0, 1, 1).
```

The lex-first remaining-bit miss of each displayed `Q`, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is:

- `bit:wt1`: lex-first miss `(0, 0, 0, 1, 0)`
- `bit:opp2`: lex-first miss `(0, 0, 0, 1, 0)`
- `bit:adj2`: lex-first miss `(0, 0, 0, 1, 0)`
- `bit:vertex3`: lex-first miss `(0, 0, 1, 0, 0)`
- `bit:mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `wt1&opp2`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1&adj2`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1&vertex3`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1&mixed3`: lex-first miss `(0, 0, 0, 1, 0)`
- `Q4|vertex3`: lex-first miss `(0, 1, 0, 0, 0)`
- `wt1|opp2`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1|adj2`: lex-first miss `(0, 0, 0, 1, 0)`
- `wt1|vertex3`: lex-first miss `(0, 0, 1, 0, 0)`
- `wt1|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `opp2|adj2`: lex-first miss `(0, 0, 0, 1, 0)`
- `opp2|vertex3`: lex-first miss `(0, 0, 1, 0, 0)`
- `opp2|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `adj2|vertex3`: lex-first miss `(0, 1, 0, 0, 0)`
- `adj2|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`
- `vertex3|mixed3`: lex-first miss `(0, 0, 0, 0, 1)`

## Theorem 2 — `N_pos` and, for each displayed Q, `N_Q` and `N_both`

Among the 32 maps, `N_pos = 30` maps have `cov8>0`.

For each displayed `Q`, write `N_Q` for the number of maps with `Q` true
and `N_both` for the number of maps with both `Q` true and `cov8>0`:

- `bit:wt1`: N_Q = 16, N_both = 16
- `bit:opp2`: N_Q = 16, N_both = 16
- `bit:adj2`: N_Q = 16, N_both = 16
- `bit:vertex3`: N_Q = 16, N_both = 16
- `bit:mixed3`: N_Q = 16, N_both = 15
- `wt1&opp2`: N_Q = 8, N_both = 8
- `wt1&adj2`: N_Q = 8, N_both = 8
- `wt1&vertex3`: N_Q = 8, N_both = 8
- `wt1&mixed3`: N_Q = 8, N_both = 8
- `Q4|vertex3`: N_Q = 28, N_both = 28
- `wt1|opp2`: N_Q = 24, N_both = 24
- `wt1|adj2`: N_Q = 24, N_both = 24
- `wt1|vertex3`: N_Q = 24, N_both = 24
- `wt1|mixed3`: N_Q = 24, N_both = 23
- `opp2|adj2`: N_Q = 24, N_both = 24
- `opp2|vertex3`: N_Q = 24, N_both = 24
- `opp2|mixed3`: N_Q = 24, N_both = 23
- `adj2|vertex3`: N_Q = 24, N_both = 24
- `adj2|mixed3`: N_Q = 24, N_both = 23
- `vertex3|mixed3`: N_Q = 24, N_both = 23

The row `wt1|adj2` recovers the #6527 counts `N_Q4 = 24`, `N_both = 24`
against the same `N_pos = 30`. No displayed row has `N_Q = N_both = N_pos`.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, has `cov8 = 494 > 0`. That
is consistent with Theorem 2 and does not restore equality for any
displayed `Q`.

## Theorem 3 — display; do not adopt a bit

Every predicate above is displayed. Displayed, not adopted. Do not adopt a
bit. Do not write any displayed remaining-bit formula into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 495 eight-site seeds, off-patch `o=0` | declared finite patch |
| displayed 1-bit, `wt1`-AND-bit, `Q4 ∨ vertex3`, 2-bit OR family | displayed, not adopted |
| some displayed `Q` equals `cov8>0` | fails; none; lex-first miss of each named |
| `N_pos = 30` and per-`Q` `N_Q`, `N_both` | proved by exhaustive scoring |
| leftover-character of #6527 | refused; new k-selector after Q4 failed at k=8 |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6527: that closed `cov8>0` is not `Q4`, with
`N_Q4 = 24`, `N_pos = 30`, `N_both = 24`. The present object is a search
over a displayed remaining-bit family on the same eight-site seeds, not a
restatement that `Q4` fails.

Not leftover-character of unique-maximizer ranking at `k=8`: that names the
unique maximizer of `cov8`, which is a different object from positivity
`cov8>0`. New k-selector after Q4 failed at k=8.

The note is not a Max(8) ranking and not a seed-table: maximizers of `cov8`
are not selected, and no seed census of a named map is compiled.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt a bit.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether any displayed remaining-bit predicate equals `cov8>0` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the #6527 fact that `cov8>0` is not `Q4`, but no landed remaining-bit search after that failure. |
| V3 | The 32 maps, 495 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a displayed remaining-bit family. |
| V5 | Equality fails for every displayed `Q`, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: none of the displayed remaining-bit
predicates equals `cov8>0` among the 32 `F_cut` maps on this patch. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6527 | treat the search as leftover-character of `cov8>0` is not `Q4` | **ATTEMPTED** |
| leftover unique maximizer | replace positivity search by the unique `cov8` maximizer | **ATTEMPTED** |
| adopt a bit | write a displayed remaining-bit formula into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed equalities, the Hamming contrast, the #6527 `Q4` failure, and
the off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the 495 eight-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the displayed
family are declared. Equality of any displayed `Q` with `cov8>0` is not
silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether a displayed
remaining-bit predicate equals 8-site positivity on the declared patch, not
leftover-character of #6527, and not a unique-maximizer ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 495 seeds | no physical law selection |
| per block | `N_pos` and per-`Q` `N_Q`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector outside the displayed remaining-bit family, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** after `Q4` failed, a 1-bit, a `wt1`-AND-bit, `Q4 ∨ vertex3`,
or some 2-bit OR must be the positivity selector at `k=8`.

**Answer:** None of those twenty displayed predicates equals `cov8>0`.
`N_pos = 30`. The closest 2-bit OR rows have `N_Q = 24` or `N_both = 23`.
`Q4|vertex3` has `N_Q = 28` and still misses `(0, 1, 0, 0, 0)`. No bit is
adopted.

### N8 — cross-cycle echo

Investment #6527 already showed that `cov8>0` is not `Q4`. Echoing that
single-predicate failure is not a substitute for scoring the rest of the
displayed remaining-bit family: the twenty lex-first misses and the
per-`Q` pair `(N_Q, N_both)` are the new search facts.

No-Go Discipline disposition: **PASS** for the finite search and the
narrow equality failure. FAIL / DO NOT SHIP for “a displayed remaining-bit
predicate equals `cov8>0`” or “a displayed bit is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov8` on the
495 eight-site seeds, compares positivity with each displayed remaining-bit
predicate, reports that none equals `cov8>0`, names the lex-first miss of
each displayed `Q`, and reports `N_pos = 30` together with per-`Q` `N_Q`
and `N_both`. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.

---
claim_id: f_cut_q4_false_cov7_vertex3_selector_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=0 and adj2=0 on the two-cube with off-patch o=0, whether cov7>0 equals vertex3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q4_false_cov7_vertex3_selector_2026_08_15.py
---

# Whether `cov7>0` Equals Displayed `vertex3=1` Among the Eight Q4-False Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 7-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
eight cube-covariant cut maps in `F_cut` with `wt1=0` and `adj2=0`,
against displayed `Q := (vertex3=1)`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q4_false_cov7_vertex3_selector_2026_08_15.py`](../scripts/f_cut_q4_false_cov7_vertex3_selector_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c7q4 scored all 32 `F_cut` maps and found `N_pos = N_Q4 = 24`
but `N_both = 20`. Equivalence of `cov7>0` with
`Q4 := (wt1=1) or (adj2=1)` therefore fails, and positivity does not
imply `Q4`. The four Q4-false positives are exactly the remaining-bit
pattern `(0, *, 0, 1, *)`. That is the imply-fail residual. This note
names the imply-fail residual and tests the new one-bit predicate on
those eight Q4-false maps. Not leftover-character of the 32-map c7q4
count, and not leftover-character of the k=4 identity `Q4=cov4>0`.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`. The eight maps
with `wt1=0` and `adj2=0` are exactly the Q4-false members.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`, which is Q4-true and is not one
of the eight maps scored here.

On the two-cube with off-patch occupancy `0`, write
`cov7(f) = |{S : |S|=7 and f fills from S}|`. Then, among the eight
maps with `wt1=0` and `adj2=0`:

- Theorem 1. `cov7>0` equals `Q`, where `Q := (vertex3=1)`. There is no
  remaining-bit miss.
- Theorem 2. `N_pos = 4`, `N_Q = 4`, `N_both = 4`.
- Theorem 3. `Q` is displayed. Do not adopt a bit.

Do not write `vertex3` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight Q4-false F_cut maps are enumerated by remaining bits and scored exactly on the 792 seven-site seeds of the two-cube. Whether cov7>0 equals displayed vertex3=1 is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q4_false_cov7_vertex3_selector
target_blocker_text: "whether cov7>0 equals vertex3=1 among the 8 F_cut maps with wt1=0 and adj2=0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 7-site positivity-versus-vertex3 comparison on the eight Q4-false maps; do not adopt displayed Q"
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
predicate. `Q` is a displayed remaining-bit formula, not axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different
rule and is not used.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0.
Complement swaps `n_both` with `n_empty`. The five remaining bits of
`F_cut`, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values
on orbit types `(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`.
Complement partners are forced equal; empty and full are fixed at 0. Thus
`N_free = 5` and `|F_cut| = 32`.

The eight Q4-false maps are the remaining-bit tuples with `wt1=0` and
`adj2=0`. Opp2, vertex3, and mixed3 remain free. They are

```text
(0, 0, 0, 0, 0), (0, 0, 0, 0, 1), (0, 0, 0, 1, 0), (0, 0, 0, 1, 1),
(0, 1, 0, 0, 0), (0, 1, 0, 0, 1), (0, 1, 0, 1, 0), (0, 1, 0, 1, 1).
```

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The seven-site seeds are the `C(12,7) = 792` subsets of size 7 in `T`. Then
`cov7(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov7(f)>0`. Duality is not assumed: `cov7` is scored on
those 792 seeds.

The displayed remaining-bit predicate on this eight-map slice is

```text
Q(f) := (vertex3 = 1).
```

Opp2 and mixed3 remain free in `Q`. Displayed, not adopted. Do not adopt a
bit.

## Theorem 1 — `cov7>0` equals `Q` among the eight Q4-false maps

Enumerate the eight remaining-bit tuples with `wt1=0` and `adj2=0` and
score `cov7` on the 792 seven-site seeds. Then `cov7(f) > 0` if and only
if `Q(f)`. There is no remaining-bit miss.

The four maps with `cov7 = 0` are exactly the four with `vertex3 = 0`:

| remaining bits | `cov7` | `Q` |
|---|---:|---:|
| `(0, 0, 0, 0, 0)` | 0 | 0 |
| `(0, 0, 0, 0, 1)` | 0 | 0 |
| `(0, 1, 0, 0, 0)` | 0 | 0 |
| `(0, 1, 0, 0, 1)` | 0 | 0 |

The four maps with `cov7 > 0` are exactly the four with `vertex3 = 1`,
which is the pattern `(0, *, 0, 1, *)`:

| remaining bits | `cov7` | `Q` |
|---|---:|---:|
| `(0, 0, 0, 1, 0)` | 16 | 1 |
| `(0, 0, 0, 1, 1)` | 80 | 1 |
| `(0, 1, 0, 1, 0)` | 40 | 1 |
| `(0, 1, 0, 1, 1)` | 108 | 1 |

Those four positives are the imply-fail residual of the 32-map test: they
are Q4-false and 7-site positive. On this slice they are exactly `Q`. The
lex-first positive is `(0, 0, 0, 1, 0)` with `cov7 = 16`.

`f_L1` is not among the eight maps. Its remaining bits `(1, 0, 1, 1, 1)`
are Q4-true. That is consistent with restricting the test to Q4-false
maps and does not restore a 32-map selector.

## Theorem 2 — `N_pos`, `N_Q`, `N_both`

Among the eight Q4-false maps:

- `N_pos = 4` maps have `cov7 > 0`;
- `N_Q = 4` maps satisfy `Q`;
- `N_both = 4` maps satisfy both.

The counts match the iff of Theorem 1: `N_pos = N_Q = N_both = 4`. There
is no lex-first miss. The parent 32-map triple remains
`(N_pos, N_Q4, N_both) = (24, 24, 20)` and is not this eight-map triple.

## Theorem 3 — display; do not adopt a bit

`Q` is the remaining-bit predicate `vertex3=1` on the eight Q4-false
maps. On this patch it equals 7-site positivity. Displayed, not adopted.
Do not adopt a bit. Do not write `vertex3` into Admissibility.
Admissibility does not name this remaining-bit formula.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| eight Q4-false `F_cut` maps (`wt1=0` and `adj2=0`) | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 792 seven-site seeds, off-patch `o=0` | declared finite patch |
| `Q` as `(vertex3=1)` | displayed, not adopted |
| `cov7>0` iff `Q` among those eight | holds; no remaining-bit miss |
| `N_pos = 4`, `N_Q = 4`, `N_both = 4` | proved by exhaustive scoring |
| names the imply-fail residual | the four Q4-false positives `(0, *, 0, 1, *)` |
| leftover-character of the 32-map c7q4 count | refused; new one-bit test on the eight |
| leftover-character of the k=4 Q4 naming | refused; new seed size and new slice |
| adoption of a remaining bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the 32-map c7q4 count: that already showed
`N_pos = N_Q4 = 24` and `N_both = 20`, and it named the four Q4-false
positives `(0, *, 0, 1, *)`. Echoing that split is not a substitute for
testing whether `cov7>0` equals `vertex3=1` among the eight Q4-false
maps. This note names the imply-fail residual.

Not leftover-character of the k=4 Q4 naming: that closed `Q4=cov4>0` on
all 32 maps at a different seed size. Restricting to Q4-false maps and
scoring seven-site positivity against `vertex3` is a different object.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `vertex3` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 7-site positivity equals displayed `vertex3=1` among the eight Q4-false maps on this patch. |
| V2 | Current main has the axiom memo and the 32-map c7q4 split, but no landed eight-map 7-site positivity-versus-`vertex3` test. |
| V3 | The eight maps, 792 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared eight-map slice against a newly displayed one-bit predicate. |
| V5 | Equivalence holds, the counts are `(4, 4, 4)`, no miss is reported, and displayed `Q` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the eight Q4-false `F_cut` maps on
this patch, `cov7>0` equals displayed `vertex3=1`. Displayed `Q` is not
axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of the 32-map c7q4 count | treat the eight-map iff as leftover-character of `(24, 24, 20)` | **ATTEMPTED** |
| leftover of the k=4 Q4 naming | treat seven-site positivity on this slice as leftover-character of `Q4=cov4>0` | **ATTEMPTED** |
| adopt `vertex3` | write `vertex3=1` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| duality shortcut | replace the 792 seven-site seeds by five-site seeds | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the 32-map c7q4 split, the four-site OR, the
off-patch convention, and the duality shortcut are distinct. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 792 seven-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, the eight-map
slice `wt1=0` and `adj2=0`, and displayed `Q` are declared. Equivalence
of `cov7>0` with `vertex3=1` on that slice is scored, not imported.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
7-site positivity equals displayed `vertex3=1` among the eight Q4-false
maps on the declared patch. The note names the imply-fail residual of
the 32-map test and is not leftover-character of that count.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the eight Q4-false maps scored on 792 seeds | no physical law selection |
| per block | `N_pos`, `N_Q`, and `N_both` on this slice | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q` or `cov7>0`, the complementary 24 Q4-true maps, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** the four Q4-false positives are already named by the
pattern `(0, *, 0, 1, *)`, so `vertex3=1` is only a rename of that
pattern, the eight-map iff is leftover-character of the 32-map imply
fail, and the bit must be written into Admissibility.

**Answer:** naming the four positives does not score the four zeros, and
it does not prove that every `vertex3=1` Q4-false map is 7-site positive.
The eight-map census is the missing comparison: `N_pos = N_Q = N_both = 4`
and there is no miss. Displayed `Q` is not adopted.

### N8 — cross-cycle echo

The 32-map c7q4 count already showed that `cov7>0` is not `Q4` and that
positivity does not imply `Q4`. The k=4 naming already showed
`Q4=cov4>0`. Echoing either fact is not a substitute for the eight-map
`vertex3` count: the four zeros, the four positives, and the triple
`(N_pos, N_Q, N_both) = (4, 4, 4)` are seven-site facts on this slice.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow equivalence report. FAIL / DO NOT SHIP for “displayed `Q` is the
physical rule” or “adopt a bit.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, restricts to the
eight with `wt1=0` and `adj2=0`, scores `cov7` on the 792 seven-site
seeds, compares positivity with displayed `Q := (vertex3=1)`, reports
that the two are equivalent on that slice, reports no remaining-bit
miss, and reports `N_pos = 4`, `N_Q = 4`, and `N_both = 4`. Declared
audit inputs are this note and the axiom memo; the runner writes no
cache and authors no audit verdict.

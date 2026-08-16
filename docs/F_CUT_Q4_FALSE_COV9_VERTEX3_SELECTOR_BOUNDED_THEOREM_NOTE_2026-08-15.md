---
claim_id: f_cut_q4_false_cov9_vertex3_selector_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=0 and adj2=0 on the two-cube with off-patch o=0, whether cov9>0 equals vertex3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q4_false_cov9_vertex3_selector_2026_08_15.py
---

# Whether `cov9>0` Equals Displayed `vertex3=1` Among the Eight Q4-False Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 9-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
eight cube-covariant cut maps in `F_cut` with `wt1=0` and `adj2=0`,
against displayed `Q := (vertex3=1)`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q4_false_cov9_vertex3_selector_2026_08_15.py`](../scripts/f_cut_q4_false_cov9_vertex3_selector_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment q4f7 scored the eight Q4-false maps at seed size 7 and found
`cov7>0` iff `vertex3=1`. Investment q4f11 scored the same eight maps at
seed size 11 and found `cov11>0` iff `vertex3=1`. Both eight-map triples
were `(N_pos, N_Q, N_both) = (4, 4, 4)`. Investment c9sel scored all 32
`F_cut` maps at seed size 9 and found `N_pos = 26 > N_Q4 = 24`, so some
Q4-false maps have `cov9>0`. That residual is a new k question: whether,
among those eight maps, `cov9>0` is again `vertex3`. New k for that
residual. Not leftover-character of the q4f7 or q4f11 eight-map iff, and
not leftover-character of the 32-map c9sel search.

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
`cov9(f) = |{S : |S|=9 and f fills from S}|`. Then, among the eight
maps with `wt1=0` and `adj2=0`:

- Theorem 1. `cov9>0` is not equivalent to `Q`, where
  `Q := (vertex3=1)`. There is one remaining-bit miss.
- Theorem 2. `N_pos = 5`, `N_Q = 4`, `N_both = 4`. The lex-first miss
  is `(0, 1, 0, 0, 1)`.
- Theorem 3. `Q` is displayed. Do not adopt a bit.

Do not write `vertex3` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight Q4-false F_cut maps are enumerated by remaining bits and scored exactly on the 220 nine-site seeds of the two-cube. Whether cov9>0 equals displayed vertex3=1 is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q4_false_cov9_vertex3_selector
target_blocker_text: "whether cov9>0 equals vertex3=1 among the 8 F_cut maps with wt1=0 and adj2=0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 9-site positivity-versus-vertex3 comparison on the eight Q4-false maps; do not adopt displayed Q"
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

The nine-site seeds are the `C(12,9) = 220` subsets of size 9 in `T`. Then
`cov9(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov9(f)>0`. Duality is not assumed: `cov9` is scored on
those 220 seeds.

The displayed remaining-bit predicate on this eight-map slice is

```text
Q(f) := (vertex3 = 1).
```

Opp2 and mixed3 remain free in `Q`. Displayed, not adopted. Do not adopt a
bit.

## Theorem 1 — `cov9>0` is not equivalent to `Q` among the eight Q4-false maps

Enumerate the eight remaining-bit tuples with `wt1=0` and `adj2=0` and
score `cov9` on the 220 nine-site seeds. Then `cov9(f) > 0` is not
equivalent to `Q(f)`. There is one remaining-bit miss.

The three maps with `cov9 = 0` all have `vertex3 = 0`:

| remaining bits | `cov9` | `Q` |
|---|---:|---:|
| `(0, 0, 0, 0, 0)` | 0 | 0 |
| `(0, 0, 0, 0, 1)` | 0 | 0 |
| `(0, 1, 0, 0, 0)` | 0 | 0 |

The four maps with `vertex3 = 1` all have `cov9 > 0`, and one further
map with `vertex3 = 0` is also 9-site positive:

| remaining bits | `cov9` | `Q` |
|---|---:|---:|
| `(0, 0, 0, 1, 0)` | 48 | 1 |
| `(0, 0, 0, 1, 1)` | 80 | 1 |
| `(0, 1, 0, 0, 1)` | 4 | 0 |
| `(0, 1, 0, 1, 0)` | 48 | 1 |
| `(0, 1, 0, 1, 1)` | 84 | 1 |

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 1, 0, 0, 1)`: it has
`cov9 = 4 > 0` and `Q = 0`. The four `vertex3 = 1` maps have
`cov9 = 48`, `cov9 = 80`, `cov9 = 48`, and `cov9 = 84`. So `Q` implies
positivity on this slice, but positivity does not imply `Q`. The residual
is therefore not again `vertex3`.

`f_L1` is not among the eight maps. Its remaining bits `(1, 0, 1, 1, 1)`
are Q4-true. That is consistent with restricting the test to Q4-false
maps and does not restore a 32-map selector.

## Theorem 2 — `N_pos`, `N_Q`, `N_both`

Among the eight Q4-false maps:

- `N_pos = 5` maps have `cov9 > 0`;
- `N_Q = 4` maps satisfy `Q`;
- `N_both = 4` maps satisfy both.

The counts witness the fail of Theorem 1: `N_pos = 5`, `N_Q = 4`,
`N_both = 4`. There is one lex-first miss, `(0, 1, 0, 0, 1)`. The parent
32-map c9sel pair remains `N_pos = 26 > N_Q4 = 24` and is not this
eight-map triple.

## Theorem 3 — display; do not adopt a bit

`Q` is the remaining-bit predicate `vertex3=1` on the eight Q4-false
maps. On this patch it does not equal 9-site positivity. Displayed, not
adopted. Do not adopt a bit. Do not adopt vertex3.
Do not write `vertex3` into Admissibility. Admissibility does not name
this remaining-bit formula.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| eight Q4-false `F_cut` maps (`wt1=0` and `adj2=0`) | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 220 nine-site seeds, off-patch `o=0` | declared finite patch |
| `Q` as `(vertex3=1)` | displayed, not adopted |
| `cov9>0` iff `Q` among those eight | fails; one remaining-bit miss |
| `N_pos = 5`, `N_Q = 4`, `N_both = 4` | proved by exhaustive scoring |
| lex-first miss | `(0, 1, 0, 0, 1)` with `cov9 = 4` |
| leftover-character of q4f7 / q4f11 | refused; new k |
| leftover-character of the 32-map c9sel search | refused; eight-map `vertex3` test |
| adoption of a remaining bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the q4f7 or q4f11 eight-map iff: those already
showed `cov7>0` and `cov11>0` each equal `vertex3=1` among the eight
Q4-false maps, with triple `(4, 4, 4)`. Echoing either iff is not a
substitute for scoring nine-site positivity against `vertex3` on the same
slice. New k for that residual.

Not leftover-character of the 32-map c9sel search: that already showed
`N_pos = 26 > N_Q4 = 24` and that no displayed 32-map remaining-bit
predicate equals `cov9>0`. Restricting to Q4-false maps and testing
whether that residual is again `vertex3` is a different object.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `vertex3` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 9-site positivity equals displayed `vertex3=1` among the eight Q4-false maps on this patch. |
| V2 | Current main has the axiom memo, but no landed eight-map 9-site positivity-versus-`vertex3` test. |
| V3 | The eight maps, 220 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared eight-map slice against a newly displayed one-bit predicate at a new seed size. |
| V5 | Equivalence fails, the counts are `(5, 4, 4)`, one lex-first miss is named, and displayed `Q` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: among the eight Q4-false `F_cut` maps on
this patch, `cov9>0` is not displayed `vertex3=1`. Displayed `Q` is not
axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of q4f7 / q4f11 | treat the nine-site fail as leftover-character of those iff facts | **ATTEMPTED** |
| leftover of the 32-map c9sel search | treat the eight-map test as leftover-character of `N_pos = 26 > N_Q4 = 24` | **ATTEMPTED** |
| adopt `vertex3` | write `vertex3=1` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| duality shortcut | replace the 220 nine-site seeds by three-site seeds | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the q4f7 / q4f11 iff facts, the 32-map c9sel
split, the off-patch convention, and the duality shortcut are distinct.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 220 nine-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, the eight-map
slice `wt1=0` and `adj2=0`, and displayed `Q` are declared. Equivalence
of `cov9>0` with `vertex3=1` on that slice is scored, not imported.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
9-site positivity equals displayed `vertex3=1` among the eight Q4-false
maps on the declared patch. The note names the c9sel Q4-false positivity
residual and is not leftover-character of that 32-map count.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the eight Q4-false maps scored on 220 seeds | no physical law selection |
| per block | `N_pos`, `N_Q`, and `N_both` on this slice | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different Boolean combination of remaining bits, a
different seed family, a different off-patch rule, a selector other than
`Q` or `cov9>0`, the complementary 24 Q4-true maps, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** q4f7 and q4f11 already showed that the Q4-false residual is
exactly `vertex3=1`, so at seed size 9 the same bit must again be the
selector, and the bit must be written into Admissibility.

**Answer:** the eight-map census at seed size 9 is a different object.
`N_pos = 5`, `N_Q = 4`, `N_both = 4`, and the lex-first miss
`(0, 1, 0, 0, 1)` has `cov9 = 4 > 0` with `vertex3 = 0`. The residual is
not again `vertex3`. Displayed `Q` is not adopted.

### N8 — cross-cycle echo

The q4f7 and q4f11 counts already showed an eight-map iff at seed sizes
7 and 11. The 32-map c9sel search already showed `N_pos = 26 > N_Q4 = 24`.
Echoing either fact is not a substitute for the eight-map `vertex3` count
at seed size 9: the three zeros, the five positives, the miss
`(0, 1, 0, 0, 1)`, and the triple `(N_pos, N_Q, N_both) = (5, 4, 4)` are
nine-site facts on this slice.

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
eight with `wt1=0` and `adj2=0`, scores `cov9` on the 220 nine-site
seeds, compares positivity with displayed `Q := (vertex3=1)`, reports
that the two are not equivalent on that slice, reports the one
remaining-bit miss `(0, 1, 0, 0, 1)`, and reports `N_pos = 5`, `N_Q = 4`,
and `N_both = 4`. Declared audit inputs are this note and the axiom memo;
the runner writes no cache and authors no audit verdict.

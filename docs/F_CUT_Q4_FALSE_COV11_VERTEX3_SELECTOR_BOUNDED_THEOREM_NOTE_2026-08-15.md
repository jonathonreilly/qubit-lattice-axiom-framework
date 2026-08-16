---
claim_id: f_cut_q4_false_cov11_vertex3_selector_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=0 and adj2=0 on the two-cube with off-patch o=0, whether cov11>0 equals vertex3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q4_false_cov11_vertex3_selector_2026_08_15.py
---

# Whether `cov11>0` Equals Displayed `vertex3` Among The Eight `Q4`-False Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 11-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
eight cube-covariant cut maps in `F_cut` with `wt1=0` and `adj2=0`,
against displayed `Q := (vertex3=1)`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q4_false_cov11_vertex3_selector_2026_08_15.py`](../scripts/f_cut_q4_false_cov11_vertex3_selector_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c11q4 scored all 32 `F_cut` maps at seed size 11 against
displayed `Q4 := (wt1=1) or (adj2=1)` and reported the same
`24/24/20` split as c7q4: `N_pos = 24`, `N_Q4 = 24`, `N_both = 20`.
The four `Q4`-false positives were exactly `(0,*,0,1,*)`. That residue
is the eight-map class with `wt1=0` and `adj2=0`. This note is a new
`k` question on that residual: whether, among those eight maps,
`cov11>0` equals displayed `vertex3`. New k for that residual. Not
leftover-character of the 32-map `Q4` count, and not leftover-character
of the c7q4 split.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`, so `f_L1` is not one of the
eight `Q4`-false maps.

On the two-cube with off-patch occupancy `0`, write
`cov11(f) = |{S : |S|=11 and f fills from S}|`. Among the eight maps
with `wt1=0` and `adj2=0`, write

```text
Q(f) := (vertex3 = 1).
```

Then:

- Theorem 1. `cov11>0` is equivalent to `Q` among those eight maps.
- Theorem 2. `N_pos = 4`, `N_Q = 4`, `N_both = 4`. There is no miss.
- Theorem 3. `Q` is displayed. Do not adopt a bit.

Do not write `vertex3` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight Q4-false F_cut maps are enumerated by remaining bits and scored exactly on the 12 eleven-site seeds of the two-cube. Whether cov11>0 equals displayed vertex3=1 is a finite exact fact. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q4_false_cov11_vertex3_selector
target_blocker_text: "whether cov11>0 equals vertex3=1 among the eight F_cut maps with wt1=0 and adj2=0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 11-site positivity-versus-vertex3 comparison on the Q4-false class; do not adopt displayed vertex3"
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
predicate. Displayed `Q` is a remaining-bit formula, not axiom content.

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

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The eleven-site seeds are the `C(12,11) = 12` subsets of size 11 in `T`.
Then `cov11(f)` is the number of those subsets from which `f` fills. The
boolean scored here is `cov11(f)>0`. Duality is not assumed: `cov11` is
scored on those 12 seeds.

The eight-map class is the subset of `F_cut` with remaining bits

```text
(wt1, opp2, adj2, vertex3, mixed3) = (0, *, 0, *, *).
```

That is exactly `wt1=0` and `adj2=0`. Opp2, vertex3, and mixed3 remain
free, so the class has size 8. Displayed `Q4` is used only to name this
class. The displayed predicate on the class is

```text
Q(f) := (vertex3=1).
```

Opp2 and mixed3 are free in `Q`. Displayed, not adopted.

## Theorem 1 — `cov11>0` equals `Q` among the eight maps

Enumerate the eight remaining-bit tuples with `wt1=0` and `adj2=0` and
score `cov11` on the 12 eleven-site seeds. Then `cov11(f) > 0` if and
only if `Q(f)` holds.

The four maps with `vertex3 = 1` each have `cov11 = 8`:
`(0, 0, 0, 1, 0)`, `(0, 0, 0, 1, 1)`, `(0, 1, 0, 1, 0)`, and
`(0, 1, 0, 1, 1)`. The four maps with `vertex3 = 0` each have
`cov11 = 0`: `(0, 0, 0, 0, 0)`, `(0, 0, 0, 0, 1)`, `(0, 1, 0, 0, 0)`,
and `(0, 1, 0, 0, 1)`. There is no mismatch.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, is outside the eight-map
class. Its 11-site coverage is not used as a selector on this class.

## Theorem 2 — `N_pos`, `N_Q`, `N_both`

Among the eight maps:

- `N_pos = 4` maps have `cov11 > 0`;
- `N_Q = 4` maps satisfy `Q`;
- `N_both = 4` maps satisfy both.

The counts match: `N_pos = N_Q = N_both = 4`. There is no lex-first miss.
If the iff had failed, the runner would report one lex-first remaining-bit
miss in the order `(wt1, opp2, adj2, vertex3, mixed3)`.

## Theorem 3 — display; do not adopt a bit

`Q` is the displayed remaining-bit predicate `vertex3=1` on the eight
`Q4`-false maps. On this patch it equals 11-site positivity inside that
class. Displayed, not adopted. Do not adopt a bit. Do not adopt vertex3.
Do not write `vertex3` into Admissibility. Admissibility does not name
this remaining-bit formula.

The identities here are finite facts about occupancy-to-lock on this
two-cube with off-patch `o=0`. They are not a physical formation-site
selector and not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| eight-map class `wt1=0` and `adj2=0` | enumerated |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 12 eleven-site seeds, off-patch `o=0` | declared finite patch |
| `Q` as `(vertex3=1)` | displayed, not adopted |
| `cov11>0` iff `Q` among the eight | holds; `N_pos = N_Q = N_both = 4` |
| leftover-character of the 32-map `Q4` count | refused; new residual on the eight |
| leftover-character of the c7q4 split | refused; new class and displayed bit |
| adoption of `vertex3` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the 32-map `Q4` count: that already showed
`cov11>0` is not `Q4` among the 32 maps, with the same `24/24/20` split
as c7q4 and the same four `Q4`-false positives `(0,*,0,1,*)`. The present
object is whether displayed `vertex3` equals 11-site positivity on that
eight-map class. New k for that residual.

Not leftover-character of the c7q4 split: that was a seven-site
`Q4` comparison on all 32 maps. Echoing that split is not a substitute
for the eight-map `vertex3` comparison at seed size 11.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `vertex3` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether 11-site positivity equals displayed `vertex3` among the eight `Q4`-false maps on this patch. |
| V2 | Current main has the axiom memo but no landed eight-map `cov11`-versus-`vertex3` test. |
| V3 | The eight maps, 12 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared eight-map class against a newly displayed 1-bit predicate. |
| V5 | Equivalence holds, the triple `(N_pos, N_Q, N_both) = (4, 4, 4)` is reported, and displayed `vertex3` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: displayed `vertex3` is not axiom content
and is not adopted, even though it equals `cov11>0` on this eight-map
class. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of the 32-map `Q4` count | treat the eight-map test as leftover-character of c11q4 | **ATTEMPTED** |
| leftover of the c7q4 split | treat the eleven-site eight-map test as leftover-character of c7q4 | **ATTEMPTED** |
| leftover of a 32-map 2-bit OR | replace the eight-map `vertex3` test by a 32-map OR | **ATTEMPTED** |
| adopt `vertex3` | write `(vertex3=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the 32-map `Q4` count, the c7q4 split, a 32-map
OR, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 12 eleven-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the eight-map class `wt1=0` and `adj2=0`, and
displayed `Q` are declared. Equivalence of `cov11>0` with `Q` is scored,
not imported.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
11-site positivity equals displayed `vertex3` among the eight `Q4`-false
maps on the declared patch, as a new k for that residual, and not
leftover-character of the 32-map `Q4` count.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the eight `Q4`-false maps scored on 12 seeds | no physical law selection |
| per block | `N_pos`, `N_Q`, and `N_both` on this class | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different remaining-bit predicate on the eight,
a different seed family, a different off-patch rule, a selector other
than `Q` or `cov11>0`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** the four `Q4`-false positives of c11q4 are already
`(0,*,0,1,*)`, so `vertex3` is the physical selector on the residue and
must be written into Admissibility.

**Answer:** among the eight maps, `cov11>0` equals displayed `Q`, with
`N_pos = N_Q = N_both = 4`. That is a finite displayed fact on this
patch. Displayed `vertex3` is not adopted.

### N8 — cross-cycle echo

The 32-map `Q4` count already showed the `24/24/20` split and the four
`Q4`-false positives `(0,*,0,1,*)`. The c7q4 split already showed the
same counts at seed size 7. Echoing either fact is not a substitute for
the eight-map `vertex3` comparison at seed size 11: the iff and the
triple `(N_pos, N_Q, N_both) = (4, 4, 4)` are eight-map facts.

No-Go Discipline disposition: **PASS** for the finite comparison and the
narrow display report. FAIL / DO NOT SHIP for “displayed `vertex3`
is the physical rule” or “adopt vertex3.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the eight `F_cut` maps with `wt1=0` and
`adj2=0`, scores `cov11` on the 12 eleven-site seeds, compares positivity
with displayed `Q := (vertex3=1)`, reports that the two are equivalent,
reports `N_pos = 4`, `N_Q = 4`, and `N_both = 4`, and reports that there
is no miss. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.

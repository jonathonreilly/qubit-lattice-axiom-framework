---
claim_id: f_cut_qstar_nontot_class_split_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, whether every Q_* map with vertex3=0 fails to fill S={(1,0,0)} is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_nontot_class_split_2026_08_15.py
---

# Whether `{(1,0,0)}` Is a Class Split of Non-Tot `Q_*`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill of the displayed one-site seed
`S = {(1, 0, 0)}` by each of the eight cube-covariant cut maps `F_cut`
with remaining bits `wt1=1` and `adj2=1`, on the twelve-vertex two-cube
with off-patch occupancy `0`. The scored question is whether every
`Q_*` map with `vertex3=0` fails to fill `S`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_nontot_class_split_2026_08_15.py`](../scripts/f_cut_qstar_nontot_class_split_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6528 named the lex-first non-tot `Q_*` map
`f_nt = (1, 0, 1, 0, 0)` and showed that this map misses
`S = {(1, 0, 0)}` while `f_L1` fills. Investment #6522 showed that
among `Q_*` maps, `cov1=12` if and only if `vertex3=1`, so every tot
map fills every one-site seed. This note asks a new question: whether
that seed is a class split of the whole non-tot `Q_*` slice, not a
second-seed test of the named pair.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`Q_*` is the subclass with `wt1=1` and `adj2=1`. It has 8 maps: four
with `vertex3=1` and four with `vertex3=0`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple lies in `Q_*` and
has `vertex3=1`.

On the two-cube with off-patch occupancy `0`, a map fills a seed `S` if
occupancy-to-lock from `L_0 = S` reaches the full twelve-vertex patch.

**Theorem 1.** Among the 4 `Q_*` maps with `vertex3=1`, 4 fill
`S = {(1, 0, 0)}`. Among the 4 `Q_*` maps with `vertex3=0`, 0 fill `S`.

**Theorem 2.** Every `Q_*` map with `vertex3=0` misses `S`. There is no
lex-first counterexample remaining-bit tuple that fills `S`.

**Theorem 3.** Display. Do not adopt a bit.

Displayed, not adopted.

```text
N_fill_v3 = 4
N_fill_nontot = 0
```

Uniqueness of that seed for the whole non-tot class, not a second-seed
test of the named pair.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight Q_* maps are the F_cut members with wt1=1 and adj2=1. Each is scored exactly on the displayed one-site seed S={(1,0,0)}. Whether every vertex3=0 map misses S is a finite Boolean census on this patch, not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_nontot_class_split
target_blocker_text: "whether every Q_* map with vertex3=0 fails to fill S={(1,0,0)}"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded non-tot Q_* class split; do not adopt a displayed bit"
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
predicate. The `vertex3` bit below is displayed remaining-bit data, not
axiom content.

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

The displayed seed is the one-site set `S = {(1, 0, 0)}`.

`Q_*` is the remaining-bit predicate `wt1=1` and `adj2=1`. It holds on
exactly eight of the 32 maps. The present census is restricted to those
eight, scored only on `S`.

## Theorem 1 — fill counts of `S` on the two `Q_*` slices

Direct evolution from `S` scores every `Q_*` map. The eight remaining-bit
tuples and whether each fills `S` are

```text
(1, 0, 1, 0, 0)  fills_S=0  vertex3=0
(1, 0, 1, 0, 1)  fills_S=0  vertex3=0
(1, 1, 1, 0, 0)  fills_S=0  vertex3=0
(1, 1, 1, 0, 1)  fills_S=0  vertex3=0
(1, 0, 1, 1, 0)  fills_S=1  vertex3=1
(1, 0, 1, 1, 1)  fills_S=1  vertex3=1
(1, 1, 1, 1, 0)  fills_S=1  vertex3=1
(1, 1, 1, 1, 1)  fills_S=1  vertex3=1
```

Among the 4 `Q_*` maps with `vertex3=1`, 4 fill `S`. Among the 4 with
`vertex3=0`, 0 fill `S`. Equivalently,

```text
N_fill_v3 = 4
N_fill_nontot = 0.
```

The last-but-one of the `fills_S=1` rows with `opp2=0` is `f_L1`. The
first of the `fills_S=0` rows is `f_nt`.

## Theorem 2 — every non-tot `Q_*` map misses `S`

Every `Q_*` map with `vertex3=0` fails to fill `S={(1,0,0)}`. The four
non-tot remaining-bit tuples are

```text
(1, 0, 1, 0, 0), (1, 0, 1, 0, 1), (1, 1, 1, 0, 0), (1, 1, 1, 0, 1).
```

None of them fills `S`. There is no lex-first counterexample tuple. The
miss of `S` is therefore a class fact of the `vertex3=0` slice of `Q_*`,
not a property of the named pair `(f_L1, f_nt)` alone.

## Theorem 3 — display, not adoption

The class split of `S` is displayed data. Do not adopt a bit. Do not
adopt `vertex3`. Do not adopt `Q_*`. Do not adopt `f_L1`.
Do not write `vertex3` into Admissibility.
Do not write `Q_*` or `vertex3=1` into Admissibility.
Do not write the ranking into Admissibility.

The split is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | eight maps, four tot and four non-tot |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, seed `S={(1,0,0)}`, off-patch `o=0` | declared finite patch |
| `N_fill_v3`, `N_fill_nontot` | 4 and 0 |
| every `vertex3=0` `Q_*` map misses `S` | holds; no counterexample |
| leftover of #6528 | refused; that tested the named pair |
| leftover of #6522 | refused; that named totality, not this seed |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6528: that named `f_nt` and showed that this
one non-tot map misses `S` while `f_L1` fills. The present object is
whether every non-tot `Q_*` map misses the same seed.

Not leftover-character of #6522: that showed `cov1=12` iff `vertex3=1`
on the eight maps, so every tot map fills every one-site seed. The
present object is the fill table of one displayed seed across the
non-tot slice.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether every `Q_*` map with `vertex3=0` fails to fill `S={(1,0,0)}`. |
| V2 | Current main has the named-pair miss (#6528) and the totality identity (#6522), but no landed class-split census of `S` on the four non-tot maps. |
| V3 | The eight maps and one seed are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite subclass on a displayed seed. |
| V5 | The split is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: a named-pair miss is not a class split,
and a displayed remaining-bit census inside `Q_*` is not axiom content.
No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6528 | treat the class miss as the named-pair split of `f_L1` versus `f_nt` | **ATTEMPTED** |
| leftover of #6522 | treat the 4-of-4 tot fill as leftover totality | **ATTEMPTED** |
| adopt the bit | write `vertex3` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the named-pair split, the totality identity, and
the off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the displayed seed `S={(1,0,0)}`, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the `Q_*`
cut `wt1=1` and `adj2=1` are declared. Unique selection of `f_L1` is not
silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
every `Q_*` map with `vertex3=0` fails to fill `S`, not leftover-
character of #6528 and not a second-seed test of the named pair.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the eight `Q_*` maps scored on `S` | no physical law selection |
| per block | the non-tot class miss of `S` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed, a different off-patch rule, a
selector outside `Q_*`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6528 already showed that `f_nt` misses `S` and `f_L1`
fills, so a class miss is leftover-character of the named pair.

**Answer:** #6528 tested one non-tot map against one tot map. `Q_*`
has four maps with `vertex3=0`. The present census scores all four.
The miss of `S` is unique for the whole non-tot class. That is not a
second-seed test of the named pair.

### N8 — cross-cycle echo

Investment #6522 already showed that every tot `Q_*` map fills every
one-site seed. Echoing that 4-of-4 tot fill is not a substitute for
scoring the four non-tot maps on this seed.

No-Go Discipline disposition: **PASS** for the finite eight-map census
and the displayed class split. FAIL / DO NOT SHIP for “adopt a bit,”
“the named pair is the class,” or “`vertex3` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, restricts to the
eight with `wt1=1` and `adj2=1`, scores fill of `S={(1,0,0)}` on each,
reports `N_fill_v3` and `N_fill_nontot`, and decides whether every
`vertex3=0` map misses `S`. Declared audit inputs are this note and the
axiom memo; the runner writes no cache and authors no audit verdict.

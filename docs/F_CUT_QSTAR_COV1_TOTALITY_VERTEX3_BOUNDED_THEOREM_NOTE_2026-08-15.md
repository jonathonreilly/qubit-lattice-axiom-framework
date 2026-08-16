---
claim_id: f_cut_qstar_cov1_totality_vertex3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=1 and adj2=1 on the two-cube with off-patch o=0, whether cov1=12 is equivalent to vertex3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov1_totality_vertex3_2026_08_15.py
---

# Totality Versus `vertex3` Inside `Q_*`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 1-site coverage on the twelve-vertex
two-cube with off-patch occupancy `0`, restricted to the eight
cube-covariant cut maps `F_cut` with remaining bits `wt1=1` and
`adj2=1`. The scored identity is whether `cov1=12` if and only if
`vertex3=1` on that eight-map set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov1_totality_vertex3_2026_08_15.py`](../scripts/f_cut_qstar_cov1_totality_vertex3_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6516 named

```text
Q_* := (wt1 = 1) and (adj2 = 1)
```

as the remaining-bit formula equal to `cov1>0` on the 32 `F_cut` maps.
That class has eight members. Investment #6473 named Max(1) as the four
maps with `cov1=12`; those four all lie in `Q_*`. This note asks a new
question inside `Q_*`: whether totality `cov1=12` is equivalent to the
remaining bit `vertex3=1`. New totality selector inside `Q_*`, not a
rename of positivity and not leftover-character of Max(1).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple lies in `Q_*` and has
`vertex3=1`.

On the two-cube with off-patch `o=0`, write `cov1(f)` for the number of
one-site seeds from which `f` fills. Totality means `cov1(f)=12`.

**Theorem 1.** Among the eight `Q_*` maps, cov1=12 if and only if
vertex3=1. The four maps with `vertex3=0` have `cov1=8`. The four maps
with `vertex3=1` have `cov1=12`.

**Theorem 2.** The three census integers on that eight-map set are

```text
N_v3 = 4
N_tot = 4
N_both = 4.
```

**Theorem 3.** The identity is displayed only. Do not adopt a bit. Do not
write `vertex3` into Admissibility.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight Q_* maps are the F_cut members with wt1=1 and adj2=1. Each is scored exactly on the twelve one-site seeds. Equivalence of cov1=12 with vertex3=1 is a finite Boolean identity on this patch, not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov1_totality_vertex3
target_blocker_text: "whether cov1=12 is equivalent to vertex3=1 among the eight Q_* maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q_* totality identity; do not adopt vertex3"
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

The one-site seeds are the twelve singletons `{x}` for `x ∈ T`. Then
`cov1(f)` is the number of those singletons from which `f` fills. Totality
on this patch means `cov1(f)=12`.

`Q_*` is the remaining-bit predicate `wt1=1` and `adj2=1`. It holds on
exactly eight of the 32 maps. The present census is restricted to those
eight.

## Theorem 1 — totality versus `vertex3` on `Q_*`

Direct evolution on the twelve one-site seeds scores every `Q_*` map.
The eight remaining-bit tuples and their coverages are

```text
(1, 0, 1, 0, 0)  cov1=8   vertex3=0
(1, 0, 1, 0, 1)  cov1=8   vertex3=0
(1, 1, 1, 0, 0)  cov1=8   vertex3=0
(1, 1, 1, 0, 1)  cov1=8   vertex3=0
(1, 0, 1, 1, 0)  cov1=12  vertex3=1
(1, 0, 1, 1, 1)  cov1=12  vertex3=1
(1, 1, 1, 1, 0)  cov1=12  vertex3=1
(1, 1, 1, 1, 1)  cov1=12  vertex3=1
```

The last four are exactly Max(1). The last-but-one of the `cov1=12` rows
with `opp2=0` is `f_L1`. On this eight-map set,

```text
cov1(f) = 12  ⇔  vertex3(f) = 1.
```

No `Q_*` map with `vertex3=0` attains totality. No `Q_*` map with
`vertex3=1` fails totality.

## Theorem 2 — the three census integers

Write `N_v3` for the number of `Q_*` maps with `vertex3=1`, `N_tot` for
the number with `cov1=12`, and `N_both` for the number with both. Then

```text
N_v3 = 4
N_tot = 4
N_both = 4.
```

These three integers are the same because the identity of Theorem 1 holds.
They are not assumed equal: each is counted from the scored eight-map table.

## Theorem 3 — display, not adoption

The identity `cov1=12 ⇔ vertex3=1` on `Q_*` is displayed data. Do not
adopt a bit. Do not adopt `vertex3`. Do not adopt `Q_*`. Do not adopt
`f_L1`. Do not write `vertex3` into Admissibility. Admissibility does
not name this remaining-bit formula.

The identity is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | eight maps, all with `cov1>0` |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, twelve one-site seeds, off-patch `o=0` | declared finite patch |
| `cov1=12` iff `vertex3=1` on those eight | holds |
| `N_v3`, `N_tot`, `N_both` | each equals 4 |
| leftover of #6516 | refused; that named positivity, not totality |
| leftover of #6473 | refused; that named Max(1), not the iff |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6516: that named `Q_*` as the remaining-bit
formula equal to `cov1>0`. The present object is totality versus
`vertex3` *inside* that eight-map class.

Not leftover-character of #6473: that named the four maps with
`cov1=12`. The present object is whether those four are exactly the
`vertex3=1` slice of `Q_*`.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov1=12` is equivalent to `vertex3=1` among the eight `Q_*` maps. |
| V2 | Current main has the axiom memo and the #6516/#6473 names, but no landed totality-versus-`vertex3` census inside `Q_*`. |
| V3 | The eight maps and twelve seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite subclass. |
| V5 | The identity is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: positivity of `cov1` is not totality, and
a displayed remaining-bit identity inside `Q_*` is not axiom content. No
global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6516 | treat totality as the already-named positivity class `Q_*` | **ATTEMPTED** |
| leftover of #6473 | treat the iff as a rename of the four Max(1) maps | **ATTEMPTED** |
| adopt the bit | write `vertex3` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch identity to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the positivity class `Q_*`, the four-map Max(1)
set, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the twelve singletons, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the `Q_*`
cut `wt1=1` and `adj2=1` are declared. Unique selection of `f_L1` is not
silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov1=12` equals `vertex3=1` on the eight `Q_*` maps, not leftover-
character of #6516 and not a Max(1) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the eight `Q_*` maps scored on 12 seeds | no physical law selection |
| per block | the totality–`vertex3` identity on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside `Q_*`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Max(1) already sits inside `Q_*`, so totality is just
`Q_*`, or else just the four named maximizers, and `vertex3` adds nothing.

**Answer:** `Q_*` has eight maps, four of which have `cov1=8`. Totality
is a proper subset of `Q_*`. Those four total maps are exactly the
`vertex3=1` slice. The identity is new data inside `Q_*`, and it is
displayed, not adopted.

### N8 — cross-cycle echo

Investment #6516 already showed that `cov1>0` is `wt1` and `adj2`.
Investment #6473 already named Max(1). Echoing either fact is not a
substitute for testing `cov1=12` against `vertex3` on the eight maps.

No-Go Discipline disposition: **PASS** for the finite eight-map census
and the displayed identity. FAIL / DO NOT SHIP for “adopt a bit,”
“`Q_*` equals totality,” or “`vertex3` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, restricts to the
eight with `wt1=1` and `adj2=1`, scores `cov1` on the twelve one-site
seeds, decides whether `cov1=12` if and only if `vertex3=1`, and reports
`N_v3`, `N_tot`, and `N_both`. Declared audit inputs are this note and the
axiom memo; the runner writes no cache and authors no audit verdict.

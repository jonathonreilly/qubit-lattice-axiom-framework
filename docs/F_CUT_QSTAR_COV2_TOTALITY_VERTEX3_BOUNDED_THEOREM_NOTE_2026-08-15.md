---
claim_id: f_cut_qstar_cov2_totality_vertex3_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 8 F_cut maps with wt1=1 and adj2=1 on the two-cube with off-patch o=0, whether cov2=66 is equivalent to vertex3=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov2_totality_vertex3_2026_08_15.py
---

# Two-Site Totality Versus `vertex3` Inside `Q_*`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 2-site coverage on the twelve-vertex
two-cube with off-patch occupancy `0`, restricted to the eight
cube-covariant cut maps `F_cut` with remaining bits `wt1=1` and
`adj2=1`. The scored identity is whether `cov2=66` if and only if
`vertex3=1` on that eight-map set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov2_totality_vertex3_2026_08_15.py`](../scripts/f_cut_qstar_cov2_totality_vertex3_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6522 named the one-site identity

```text
among Q_*,   cov1 = 12  ⇔  vertex3 = 1
```

on the eight maps with `wt1=1` and `adj2=1`. Investment #6482 named
Max(2) as the two maps with `cov2=66`; both lie in `Q_*` and both have
`vertex3=1`. This note asks a new question inside `Q_*`: whether two-site
totality `cov2=66` is equivalent to the remaining bit `vertex3=1`. New
2-site totality selector inside `Q_*`, not a rename of the one-site
identity and not leftover-character of Max(2).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple lies in `Q_*` and has
`vertex3=1`.

On the two-cube with off-patch `o=0`, write `cov2(f)` for the number of
two-site seeds from which `f` fills. There are `C(12,2)=66` two-site
seeds. Totality means `cov2(f)=66`.

**Theorem 1.** Among the eight `Q_*` maps, cov2=66 is not equivalent to
vertex3=1. The four maps with `vertex3=0` have `cov2` in `{32, 36}`. Of
the four maps with `vertex3=1`, two have `cov2=62` and two have
`cov2=66`. Thus `cov2=66` implies `vertex3=1`, but `vertex3=1` does not
imply `cov2=66`.

**Theorem 2.** The three census integers on that eight-map set are

```text
N_v3 = 4
N_tot2 = 2
N_both = 2.
```

**Theorem 3.** The identity is displayed only. Do not adopt a bit. Do not
write `vertex3` into Admissibility.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The eight Q_* maps are the F_cut members with wt1=1 and adj2=1. Each is scored exactly on the sixty-six two-site seeds. Equivalence of cov2=66 with vertex3=1 is a finite Boolean identity on this patch, and it fails. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov2_totality_vertex3
target_blocker_text: "whether cov2=66 is equivalent to vertex3=1 among the eight Q_* maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q_* two-site totality identity; do not adopt vertex3"
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

The two-site seeds are the sixty-six pairs `{x,y}` for distinct `x,y ∈ T`.
Then `cov2(f)` is the number of those pairs from which `f` fills. Totality
on this patch means `cov2(f)=66`.

`Q_*` is the remaining-bit predicate `wt1=1` and `adj2=1`. It holds on
exactly eight of the 32 maps. The present census is restricted to those
eight.

## Theorem 1 — two-site totality versus `vertex3` on `Q_*`

Direct evolution on the sixty-six two-site seeds scores every `Q_*` map.
The eight remaining-bit tuples and their coverages are

```text
(1, 0, 1, 0, 0)  cov2=32  vertex3=0
(1, 0, 1, 0, 1)  cov2=32  vertex3=0
(1, 1, 1, 0, 0)  cov2=36  vertex3=0
(1, 1, 1, 0, 1)  cov2=36  vertex3=0
(1, 0, 1, 1, 0)  cov2=62  vertex3=1
(1, 0, 1, 1, 1)  cov2=62  vertex3=1
(1, 1, 1, 1, 0)  cov2=66  vertex3=1
(1, 1, 1, 1, 1)  cov2=66  vertex3=1
```

The last two are exactly Max(2). The last-but-one of the `cov2=62` rows
with `opp2=0` is `f_L1`. On this eight-map set, the identity

```text
cov2(f) = 66  ⇔  vertex3(f) = 1
```

does not hold. Every `Q_*` map with `cov2=66` has `vertex3=1`. Two `Q_*`
maps with `vertex3=1` fail totality: they have `cov2=62`.

## Theorem 2 — the three census integers

Write `N_v3` for the number of `Q_*` maps with `vertex3=1`, `N_tot2` for
the number with `cov2=66`, and `N_both` for the number with both. Then

```text
N_v3 = 4
N_tot2 = 2
N_both = 2.
```

These three integers are not assumed equal: each is counted from the
scored eight-map table. They fail to coincide because the identity of
Theorem 1 fails.

## Theorem 3 — display, not adoption

The failure of `cov2=66 ⇔ vertex3=1` on `Q_*` is displayed data. Do not
adopt a bit. Do not adopt `vertex3`. Do not adopt `Q_*`. Do not adopt
`f_L1`. Do not write `vertex3` into Admissibility. Admissibility does
not name this remaining-bit formula.

The census is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | eight maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, sixty-six two-site seeds, off-patch `o=0` | declared finite patch |
| `cov2=66` iff `vertex3=1` on those eight | fails |
| `N_v3`, `N_tot2`, `N_both` | 4, 2, 2 |
| leftover of #6522 | refused; that named one-site totality |
| leftover of #6482 | refused; that named Max(2), not the iff |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6522: that named `cov1=12` iff `vertex3=1`
inside `Q_*`. The present object is two-site totality versus `vertex3`
on the same eight-map class.

Not leftover-character of #6482: that named Max(2) as the two maps with
`cov2=66`. The present object is whether those two are exactly the
`vertex3=1` slice of `Q_*`. They are a proper subset.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov2=66` is equivalent to `vertex3=1` among the eight `Q_*` maps. |
| V2 | Current main has the axiom memo and the #6522/#6482 names, but no landed two-site totality-versus-`vertex3` census inside `Q_*`. |
| V3 | The eight maps and sixty-six seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite subclass. |
| V5 | The identity is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: one-site totality inside `Q_*` is not
two-site totality, and a displayed remaining-bit census inside `Q_*` is
not axiom content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6522 | treat two-site totality as the already-named one-site identity | **ATTEMPTED** |
| leftover of #6482 | treat the iff as a rename of the two Max(2) maps | **ATTEMPTED** |
| adopt the bit | write `vertex3` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the one-site identity of #6522, the two-map Max(2)
set, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the sixty-six pairs, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the `Q_*`
cut `wt1=1` and `adj2=1` are declared. Unique selection of `f_L1` is not
silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov2=66` equals `vertex3=1` on the eight `Q_*` maps, not leftover-
character of #6522 and not a Max(2) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the eight `Q_*` maps scored on 66 seeds | no physical law selection |
| per block | the two-site totality–`vertex3` identity on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside `Q_*`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Max(2) already sits inside `Q_*` with `vertex3=1`, and
#6522 already equated totality with `vertex3`, so the two-site iff is
leftover.

**Answer:** #6522 equated *one-site* totality with `vertex3` on eight
maps. `Q_*` still has eight maps. Only two of them have `cov2=66`. The
four `vertex3=1` maps split as `{62, 66}`. Two-site totality is a proper
subset of the `vertex3=1` slice. The identity fails, and it is displayed,
not adopted.

### N8 — cross-cycle echo

Investment #6522 already showed that `cov1=12` is `vertex3=1` on `Q_*`.
Investment #6482 already named Max(2). Echoing either fact is not a
substitute for testing `cov2=66` against `vertex3` on the eight maps.

No-Go Discipline disposition: **PASS** for the finite eight-map census
and the displayed failure of the identity. FAIL / DO NOT SHIP for
“adopt a bit,” “`vertex3` equals two-site totality,” or “`vertex3` is
the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, restricts to the
eight with `wt1=1` and `adj2=1`, scores `cov2` on the sixty-six two-site
seeds, decides whether `cov2=66` if and only if `vertex3=1`, and reports
`N_v3`, `N_tot2`, and `N_both`. Declared audit inputs are this note and the
axiom memo; the runner writes no cache and authors no audit verdict.

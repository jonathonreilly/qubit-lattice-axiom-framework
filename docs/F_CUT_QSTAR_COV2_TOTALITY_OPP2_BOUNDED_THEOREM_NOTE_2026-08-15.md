---
claim_id: f_cut_qstar_cov2_totality_opp2_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 4 F_cut maps with wt1=1, adj2=1 and vertex3=1 on the two-cube with off-patch o=0, whether cov2=66 is equivalent to opp2=1 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_cov2_totality_opp2_2026_08_15.py
---

# Two-Site Totality Versus `opp2` Inside Total `Q_*`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 2-site coverage on the twelve-vertex
two-cube with off-patch occupancy `0`, restricted to the four
cube-covariant cut maps `F_cut` with remaining bits `wt1=1`, `adj2=1`,
and `vertex3=1`. The scored identity is whether `cov2=66` if and only if
`opp2=1` on that four-map set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_cov2_totality_opp2_2026_08_15.py`](../scripts/f_cut_qstar_cov2_totality_opp2_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment tot2q named that, among the eight `Q_*` maps, `cov2=66` is
not equivalent to `vertex3=1`. The four maps with `vertex3=1` split as
`cov2=62` when `opp2=0` versus `cov2=66` when `opp2=1`. This note asks
the new question inside that four-map tot slice: whether two-site
totality `cov2=66` is equivalent to the remaining bit `opp2=1`. New
2-site totality bit inside tot `Q_*`, not a rename of the eight-map
`vertex3` census and not leftover-character of Max(2).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple lies in tot `Q_*`
and has `opp2=0`.

On the two-cube with off-patch `o=0`, write `cov2(f)` for the number of
two-site seeds from which `f` fills. There are `C(12,2)=66` two-site
seeds. Totality means `cov2(f)=66`.

**Theorem 1.** Among the four tot `Q_*` maps, cov2=66 is equivalent to
opp2=1. The two maps with `opp2=0` have `cov2=62`. The two maps with
`opp2=1` have `cov2=66`. Thus `cov2=66` if and only if `opp2=1` on this
four-map set.

**Theorem 2.** The three census integers on that four-map set are

```text
N_opp = 2
N_tot2 = 2
N_both = 2.
```

**Theorem 3.** The identity is displayed only. Do not adopt a bit. Do not
write `opp2` into Admissibility.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four tot Q_* maps are the F_cut members with wt1=1, adj2=1 and vertex3=1. Each is scored exactly on the sixty-six two-site seeds. Equivalence of cov2=66 with opp2=1 is a finite Boolean identity on this patch, and it holds. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_cov2_totality_opp2
target_blocker_text: "whether cov2=66 is equivalent to opp2=1 among the four tot Q_* maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded tot Q_* two-site totality identity; do not adopt opp2"
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
predicate. The `opp2` bit below is displayed remaining-bit data, not
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
exactly eight of the 32 maps. Tot `Q_*` is the further cut `vertex3=1`
inside `Q_*`. It holds on exactly four of the 32 maps. The present census
is restricted to those four.

## Theorem 1 — two-site totality versus `opp2` on tot `Q_*`

Direct evolution on the sixty-six two-site seeds scores every tot `Q_*`
map. The four remaining-bit tuples and their coverages are

```text
(1, 0, 1, 1, 0)  cov2=62  opp2=0
(1, 0, 1, 1, 1)  cov2=62  opp2=0
(1, 1, 1, 1, 0)  cov2=66  opp2=1
(1, 1, 1, 1, 1)  cov2=66  opp2=1
```

The last two are exactly Max(2). The last-but-one of the `cov2=62` rows
with `opp2=0` is `f_L1`. On this four-map set, the identity

```text
cov2(f) = 66  ⇔  opp2(f) = 1
```

holds. Every tot `Q_*` map with `cov2=66` has `opp2=1`. Every tot `Q_*`
map with `opp2=1` has `cov2=66`. The two tot maps with `opp2=0` fail
totality: they have `cov2=62`.

## Theorem 2 — the three census integers

Write `N_opp` for the number of tot `Q_*` maps with `opp2=1`, `N_tot2` for
the number with `cov2=66`, and `N_both` for the number with both. Then

```text
N_opp = 2
N_tot2 = 2
N_both = 2.
```

These three integers are counted from the scored four-map table. They
coincide because the identity of Theorem 1 holds.

## Theorem 3 — display, not adoption

The success of `cov2=66 ⇔ opp2=1` on tot `Q_*` is displayed data. Do not
adopt a bit. Do not adopt `opp2`. Do not adopt tot `Q_*`. Do not adopt
`f_L1`. Do not write `opp2` into Admissibility. Admissibility does
not name this remaining-bit formula.

The census is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| tot `Q_*` as `wt1=1`, `adj2=1` and `vertex3=1` | four maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, sixty-six two-site seeds, off-patch `o=0` | declared finite patch |
| `cov2=66` iff `opp2=1` on those four | holds |
| `N_opp`, `N_tot2`, `N_both` | 2, 2, 2 |
| leftover of tot2q | refused; that named the eight-map `vertex3` census |
| leftover of Max(2) | refused; that named the two maps with `cov2=66` |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of tot2q: that named `cov2=66` is not iff
`vertex3=1` inside the eight `Q_*` maps, and recorded the four-map
split only as the reason the eight-map identity fails. The present
object is two-site totality versus `opp2` on the tot slice.

Not leftover-character of Max(2): that named the two maps with
`cov2=66`. The present object is whether those two are exactly the
`opp2=1` slice of tot `Q_*`. On this four-map set they are.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov2=66` is equivalent to `opp2=1` among the four tot `Q_*` maps. |
| V2 | Current main has the axiom memo and the tot2q investment name, but no landed two-site totality-versus-`opp2` census inside tot `Q_*`. |
| V3 | The four maps and sixty-six seeds are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite subclass. |
| V5 | The identity is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: an eight-map `vertex3` census is not a
four-map `opp2` identity, and a displayed remaining-bit census inside
tot `Q_*` is not axiom content. No global compiler impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of tot2q | treat the four-map iff as the already-named eight-map `vertex3` census | **ATTEMPTED** |
| leftover of Max(2) | treat the iff as a rename of the two Max(2) maps | **ATTEMPTED** |
| adopt the bit | write `opp2` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch census to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the eight-map tot2q census, the two-map Max(2)
set, and the off-patch convention are distinct. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The two-cube, the sixty-six pairs, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the tot
`Q_*` cut `wt1=1`, `adj2=1` and `vertex3=1` are declared. Unique
selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov2=66` equals `opp2=1` on the four tot `Q_*` maps, not leftover-
character of tot2q and not a Max(2) rename.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the four tot `Q_*` maps scored on 66 seeds | no physical law selection |
| per block | the two-site totality–`opp2` identity on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside tot `Q_*`, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** tot2q already recorded that the four `vertex3=1` maps
split as `cov2=62` versus `cov2=66` along `opp2`, so the four-map iff is
leftover.

**Answer:** tot2q asked whether `cov2=66` equals `vertex3=1` on eight
maps, and used the split only to show that identity fails. Tot `Q_*`
still has four maps. The present object names the identity
`cov2=66 ⇔ opp2=1` on that four-map set, reports `N_opp`, `N_tot2`,
and `N_both`, and displays the bit without adopting it.

### N8 — cross-cycle echo

Investment tot2q already showed that `cov2=66` is not `vertex3=1` on
`Q_*`. Max(2) already named the two totality maps. Echoing either fact
is not a substitute for testing `cov2=66` against `opp2` on the four
tot maps.

No-Go Discipline disposition: **PASS** for the finite four-map census
and the displayed identity. FAIL / DO NOT SHIP for
“adopt a bit,” “`opp2` is the physical rule,” or “write `opp2` into
Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, restricts to the
four with `wt1=1`, `adj2=1` and `vertex3=1`, scores `cov2` on the
sixty-six two-site seeds, decides whether `cov2=66` if and only if
`opp2=1`, and reports `N_opp`, `N_tot2`, and `N_both`. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.

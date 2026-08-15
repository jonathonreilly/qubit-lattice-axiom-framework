---
claim_id: f_cut_k4_v30_one_site_misses_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the F_cut maps (1,1,1,0,0) and (1,1,1,0,1) miss the reported 1-site seeds, and those miss sets are equal. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_v30_one_site_misses_2026_08_15.py
---

# One-Site Miss Sets Of The Two `vertex3=0` k=4 `F_cut` Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock miss lists on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the twelve one-site seeds, for the
two cube-covariant cut maps with remaining bits `(1,1,1,0,0)` and
`(1,1,1,0,1)`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_v30_one_site_misses_2026_08_15.py`](../scripts/f_cut_k4_v30_one_site_misses_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6444 reported that the two `vertex3=0` k=4 maps
`(1,1,1,0,0)` and `(1,1,1,0,1)` each have `cov1=8`, so each misses four of
the twelve one-site seeds. That note reported the count 8. The present
object is the missed corners themselves: the four missed one-site seeds of
each map, in lex order, and whether those two miss sets agree.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
Remaining bits are ordered as `(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`,
which is not a `vertex3=0` k=4 map.

Write `f00` for remaining bits `(1, 1, 1, 0, 0)` and `f01` for
`(1, 1, 1, 0, 1)`. On the two-cube with off-patch occupancy `0`, write
`cov1(f)` for the number of one-site seeds from which `f` fills, and write
`Miss(f)` for the complementary set of missed one-site seeds, listed in
lex order. Then:

- Theorem 1. Reconfirm `#6444`: `cov1(f00) = 8` and `cov1(f01) = 8`.
- Theorem 2. The missed one-site seeds, in lex order, are
  `Miss(f00) = ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))` and
  `Miss(f01) = ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))`.
- Theorem 3. The two miss sets are equal. Displayed, not adopted.

The four missed sites are the shared-face corners of the two-cube
(`x=1`). Do not adopt `vertex3`. Do not write `vertex3` into
Admissibility.

New object (the missed corners). Not leftover-character of #6444 (that only reported 8).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two vertex3=0 k=4 F_cut maps are scored exactly on the twelve one-site seeds of the two-cube. Each has cov1=8. Each misses the same four lex-ordered shared-face sites. The miss sets are equal. Displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_k4_v30_one_site_misses
target_blocker_text: "which four 1-site seeds each vertex3=0 k=4 map misses, and whether those miss sets agree"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded miss lists; do not adopt vertex3"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies `Z^3` with nearest-neighbor adjacency and proper cubic
rotations. Admissibility supplies one fixed nearest-neighbor rule, covariant
under those motions. Record is not used as a formation-site selector: the
dynamics here are a declared occupancy-to-lock predicate on a finite patch.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the two-cube `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices of two unit
  cubes sharing the face `x=1`);
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`;
- the two maps `f00=(1,1,1,0,0)` and `f01=(1,1,1,0,1)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** List the four missed one-site seeds of each `vertex3=0` k=4
map, in lex order, and state whether the two miss sets are equal.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0. Complement
swaps `n_both` with `n_empty`. The five remaining bits of `F_cut`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on orbit types
`(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`. Complement partners
are forced equal; empty and full are fixed at 0.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The one-site seeds are the twelve singletons `{x}` for `x ∈ T`, listed in
lex order of `x`. Then `Miss(f)` is the tuple of those `x` from which `f`
does not fill.

## Theorems

### Theorem 1 — reconfirm `cov1=8` for each map

Direct evolution on each of the twelve singletons reconfirms `#6444`:

```text
cov1((1, 1, 1, 0, 0)) = 8
cov1((1, 1, 1, 0, 1)) = 8
```

Each fills eight one-site seeds and therefore misses four.

### Theorem 2 — the four missed seeds, lex order

The missed one-site seeds, listed in lex order of the two-cube vertices,
are

```text
Miss((1, 1, 1, 0, 0)) = ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))
Miss((1, 1, 1, 0, 1)) = ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))
```

These are the four shared-face corners (`x=1`). Each map fills the eight
sites with `x ∈ {0,2}`.

### Theorem 3 — the two miss sets are equal

`Miss(f00) = Miss(f01)`. The mixed3 bit that distinguishes the two maps
does not change the 1-site miss set on this patch. Displayed, not adopted.
Do not write `vertex3` into Admissibility. Do not adopt `vertex3`.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` remaining-bit order | declared |
| `f00` and `f01` as the two `vertex3=0` k=4 maps | declared |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, twelve one-site seeds, off-patch 0 | declared finite patch |
| `cov1(f00)=cov1(f01)=8` | reconfirmed by evolution |
| four missed seeds of each map, lex order | proved by evolution |
| the two miss sets are equal | proved; displayed, not adopted |
| leftover-character of #6444 | refused; new object is the missed corners |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6444: that only reported `cov1=8`. The present
object is the missed-corner list of each map and the equality of those
lists. New object (the missed corners).

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write `vertex3` into
Admissibility. Do not adopt `vertex3`.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It lists the four missed 1-site seeds of each `vertex3=0` k=4 map and states that the miss sets are equal. |
| V2 | Current main has the `cov1=8` count (#6444) but no landed miss-set equality of those two maps. |
| V3 | The two maps, 12 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it lists a declared miss set. |
| V5 | It is not a physical selector: the miss lists are displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: these two maps miss the same four shared-face
one-site seeds. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover count 8 | treat the miss lists as leftover-character of #6444 | **ATTEMPTED** |
| mixed3 split | assume the free mixed3 bit splits the miss sets | **ATTEMPTED** |
| adopt `vertex3` | write `vertex3=1` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch miss list to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the leftover-count substitution, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the twelve singletons in lex order, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the two named
maps are declared. Physical selection of `vertex3` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the missed-corner list
of the two `vertex3=0` k=4 maps on the declared patch, not leftover-character
of #6444.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the two maps scored on 12 seeds | no physical law selection |
| per block | lex miss lists and their equality | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than 1-site miss-set equality, and any independently derived
physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `f00` and `f01` differ by the mixed3 bit, so they must miss
different one-site seeds.

**Answer:** Direct evolution gives the same four missed sites for both maps.
The mixed3 bit is free on this pair and does not split the 1-site miss set.
The equality is displayed, not adopted.

### N8 — cross-cycle echo

Investment #6444 already reported `cov1=8`. Echoing that count is not a
substitute for listing the four missed corners of each map and checking
equality. The present object is those lists.

No-Go Discipline disposition: **PASS** for the finite miss lists and the
narrow displayed equality. FAIL / DO NOT SHIP for “`vertex3` is the
physical rule” or “the miss lists adopt a formation selector.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner builds the two maps from remaining bits, reconfirms
`cov1=8` for each, lists the four missed one-site seeds of each map in lex
order, and checks that the two miss sets are equal. Declared audit inputs
are this note and the axiom memo; the runner writes no cache and authors no
audit verdict.

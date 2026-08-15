---
claim_id: f_cut_one_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the maximum number of 1-site seeds filled is 12, attained by 4 maps. f_L1 is not the unique maximizer. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_one_site_coverage_2026_08_15.py
---

# One-Site Fill-Coverage Ranking Among the 32 F_cut Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill counts on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the twelve one-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_one_site_coverage_2026_08_15.py`](../scripts/f_cut_one_site_coverage_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6429 ranked 2-site coverage on the same two-cube: `f_L1` is not a
maximizer there (`62 < 66`). This note repeats the ranking on a new domain,
the twelve one-site seeds. New domain (1-site coverage), not leftover-character
of #6429 and not a seed-table of f_min.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov1(f) = |{x : f fills from {x}}|`. Then:

- Theorem 1. `cov1(f_L1) = 12`. In particular `f_L1` fills from (0,0,0).
- Theorem 2. `m1 = 12` and `N1 = 4`.
- Theorem 3. `N1` is not 1, so `f_L1` is not the unique maximizer. A
  displayed maximizer is remaining-bit tuple `(1, 1, 1, 1, 0)`, which also
  has `cov1 = 12`. Displayed, not adopted.

Do not write the ranking into Admissibility. The extra that would have
selected `f_L1` — unique maximization of 1-site coverage — is not present.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the twelve one-site seeds of the two-cube. cov1(f_L1), m1, and N1 are finite exact counts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_one_site_coverage
target_blocker_text: "whether f_L1 uniquely maximizes 1-site fill coverage among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 1-site coverage ranking; do not adopt a displayed maximizer"
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
- the six-direction stencil
  `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Rank the 32 members of `F_cut` by 1-site fill coverage on `T`.

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

The one-site seeds are the twelve singletons `{x}` for `x ∈ T`. Then
`cov1(f)` is the number of those singletons from which `f` fills.

## Theorems

### Theorem 1 — `cov1(f_L1)` and the origin seed

`f_L1` is the `F_cut` map with remaining-bit tuple `(1, 0, 1, 1, 1)`.
Equivalently, `f_L1(c)=1` if and only if some axis is unbalanced. This is
**not** Hamming parity. Direct evolution on each of the twelve singletons
gives `cov1(f_L1) = 12`. In particular `f_L1` fills from (0,0,0).

### Theorem 2 — maximum and multiplicity

Among the 32 maps in `F_cut`, the maximum 1-site coverage is `m1 = 12`,
attained by `N1 = 4` maps.

### Theorem 3 — uniqueness fails; a maximizer is displayed

`N1 = 4 > 1`, so `f_L1` is not the unique maximizer. It is one of the four
maximizers, but uniqueness is the extra that would have selected it.

A displayed maximizer, identified by remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 1, 1, 1, 0)`, also has
`cov1 = 12`. Displayed, not adopted.

The four maximizers are the remaining-bit tuples

```text
(1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

The second of these is `f_L1`. The third is the displayed witness. Neither
the displayed tuple nor the four-map set is written into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, twelve one-site seeds, off-patch 0 | declared finite patch |
| `cov1(f_L1) = 12` and origin fill | proved by evolution |
| `m1 = 12`, `N1 = 4` | proved by exhaustive ranking |
| unique-maximizer selection of `f_L1` | fails; displayed, not adopted |
| leftover-character of #6429 | refused; new 1-site domain |
| seed-table of `f_min` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6429: that ranked 2-site coverage, where `f_L1`
is not a maximizer (`62 < 66`). The present count is `cov1` on twelve
singletons, a different seed family. The note is not a seed-table of f_min:
no `f_min` seed census is compiled, and `f_L1` is not identified with
Hamming or with a minimum-support table.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the ranking into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether unique 1-site coverage selects `f_L1` inside `F_cut` on this patch. |
| V2 | Current main has the 2-site ranking (#6429) but no landed 1-site `F_cut` coverage ranking. |
| V3 | The 32 maps, 12 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: uniqueness fails, and the displayed maximizer is not adopted. |

## No-Go Discipline gate

The negative content is narrow: unique 1-site coverage does not select
`f_L1` among the 32 `F_cut` maps on this patch. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 2-site ranking | treat the 1-site count as leftover-character of #6429 | **ATTEMPTED** |
| `f_min` seed table | replace the ranking by a seed-table of `f_min` | **ATTEMPTED** |
| adopt a maximizer | write `(1, 1, 1, 1, 0)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed unique-maximizer extra, the Hamming contrast, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the twelve singletons, off-patch occupancy `0`, occupancy-to-lock
ticks, and the `F_cut` remaining-bit order are declared. Unique selection of
`f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the 1-site coverage
ranking of `F_cut` on the declared patch, not leftover-character of #6429
and not a seed-table of f_min.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 12 seeds | no physical law selection |
| per block | `m1` and `N1` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than unique 1-site coverage, and any independently derived
physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `f_L1` fills every one-site seed, so 1-site coverage selects it.

**Answer:** Four maps fill every one-site seed. Unique maximization is false.
The extra that would have selected `f_L1` is not present. A maximizer other
than `f_L1` is displayed, not adopted.

### N8 — cross-cycle echo

Investment #6429 already showed that `f_L1` is not a 2-site maximizer. The
present 1-site ranking is a new domain: `f_L1` now attains the maximum, but
so do three other maps. Echoing the 2-site uniqueness failure is not a
substitute for this count.

No-Go Discipline disposition: **PASS** for the finite ranking and the
narrow uniqueness failure. FAIL / DO NOT SHIP for “`f_L1` is selected by
1-site coverage” or “the displayed maximizer is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov1` on the
twelve one-site seeds, reconfirms that `f_L1` fills from (0,0,0), reports
`m1` and `N1`, and checks that the displayed remaining-bit tuple
`(1, 1, 1, 1, 0)` attains `m1`. Declared audit inputs are this note and the
axiom memo; the runner writes no cache and authors no audit verdict.

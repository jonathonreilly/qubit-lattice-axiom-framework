---
claim_id: f_cut_k4_one_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the four F_cut maps with (wt1, opp2, adj2)=(1,1,1) on the two-cube with off-patch o=0, 1-site coverage is 12 iff vertex3=1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_one_site_coverage_2026_08_15.py
---

# One-Site Coverage Of The Four k=4 `F_cut` Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill counts on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the twelve one-site seeds, for the
four cube-covariant cut maps with remaining bits
`(wt1, opp2, adj2)=(1,1,1)` and `vertex3 × mixed3` free.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_one_site_coverage_2026_08_15.py`](../scripts/f_cut_k4_one_site_coverage_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6432/#6435 proved that four maps fill all twelve one-site seeds:
the `opp2 × mixed3` square with `vertex3=1` (and `wt1=adj2=1`). Investment
#6443 named a different four, the k=4 class, as the maps with
`(wt1, opp2, adj2)=(1,1,1)` that fill the four long-axis 2-site seeds. That
class includes two maps with `vertex3=0`. This note scores 1-site coverage
on that newly named four. New domain on the newly named 4. Not
leftover-character of #6435 (that named the four 1-site maximizers among all
32). Not leftover-character of #6443 (that only reported k).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
Remaining bits are ordered as `(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`, which
is not a k=4 map (`opp2=0`).

Write `k4cov` for the four remaining-bit tuples

```text
(1, 1, 1, 0, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

On the two-cube with off-patch occupancy `0`, write
`cov1(f) = |{x : f fills from {x}}|`. Then:

- Theorem 1. The two maps with `vertex3=1` reconfirm `cov1 = 12`
  (`#6435`): `cov1((1, 1, 1, 1, 0)) = 12` and
  `cov1((1, 1, 1, 1, 1)) = 12`.
- Theorem 2. The two maps with `vertex3=0` miss one-site seeds:
  `cov1((1, 1, 1, 0, 0)) = 8` and `cov1((1, 1, 1, 0, 1)) = 8`. Each misses
  the four shared-face sites `(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`.
- Theorem 3. Inside this four, `cov1 = 12` if and only if `vertex3=1`.
  Displayed, not adopted.

Inside `k4cov`, `vertex3=1` is required for 1-site totality. Do not adopt
`vertex3`. Do not write `vertex3` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The four k=4 F_cut maps are scored exactly on the twelve one-site seeds of the two-cube. The two vertex3=1 maps have cov1=12; the two vertex3=0 maps have cov1=8. Inside this four, cov1=12 iff vertex3=1. Displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_k4_one_site_coverage
target_blocker_text: "whether the two vertex3=0 maps in the k=4 class miss 1-site seeds"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded k=4 1-site coverage table; do not adopt vertex3"
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
- the four-map set `k4cov` with remaining bits
  `(wt1, opp2, adj2)=(1,1,1)` and `vertex3 × mixed3` free.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Score `cov1` on the four `k4cov` maps and state whether
`cov1=12` is equivalent to `vertex3=1` inside that four.

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

### Theorem 1 — the two `vertex3=1` maps have `cov1=12`

The maps `(1, 1, 1, 1, 0)` and `(1, 1, 1, 1, 1)` are the `vertex3=1` side
of `k4cov`. Direct evolution on each of the twelve singletons reconfirms

```text
cov1((1, 1, 1, 1, 0)) = 12
cov1((1, 1, 1, 1, 1)) = 12
```

as in #6435. Each fills every one-site seed.

### Theorem 2 — the two `vertex3=0` maps have `cov1=8`

The maps `(1, 1, 1, 0, 0)` and `(1, 1, 1, 0, 1)` are the `vertex3=0` side
of `k4cov`. Direct evolution gives

```text
cov1((1, 1, 1, 0, 0)) = 8
cov1((1, 1, 1, 0, 1)) = 8
```

Each fills the eight corner-ring sites with `x ∈ {0,2}` and misses the four
shared-face sites

```text
(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1).
```

They miss 1-site seeds.

### Theorem 3 — `cov1=12` iff `vertex3=1` inside this four

Among the four `k4cov` maps, `cov1=12` if and only if `vertex3=1`. The two
maps with `vertex3=0` have `cov1=8 < 12`. Displayed, not adopted. Do not
write `vertex3` into Admissibility.

Inside this four, `vertex3` is required for 1-site totality. That is a
displayed equivalence on a named four-map set, not a physical selector.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` remaining-bit order | declared |
| `k4cov` as the four `(1,1,1,*,*)` maps | declared |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, twelve one-site seeds, off-patch 0 | declared finite patch |
| `cov1` of the two `vertex3=1` maps is 12 | proved by evolution |
| `cov1` of the two `vertex3=0` maps is 8 | proved by evolution |
| `cov1=12` iff `vertex3=1` inside this four | proved; displayed, not adopted |
| leftover-character of #6435 or #6443 | refused; new domain on the named 4 |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6435: that named the four 1-site maximizers among
all 32 `F_cut` maps. Not leftover-character of #6443: that only reported `k`
on the long-axis four. The present count is `cov1` of those four maps on
twelve singletons.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write `vertex3` into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the two `vertex3=0` k=4 maps miss 1-site seeds. |
| V2 | Current main has the 32-map 1-site ranking but no landed `cov1` table of the k=4 four. |
| V3 | The four maps, 12 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared four-map class. |
| V5 | It is not a physical selector: the `vertex3` equivalence is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: inside the four k=4 maps, 1-site totality
requires `vertex3=1`. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 1-site ranking | treat the k=4 table as leftover-character of #6435 | **ATTEMPTED** |
| leftover k-count | treat `cov1` as leftover-character of #6443 | **ATTEMPTED** |
| adopt `vertex3` | write `vertex3=1` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed `vertex3=0` totality, the Hamming contrast, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the twelve singletons, off-patch occupancy `0`, occupancy-to-lock
ticks, the `F_cut` remaining-bit order, and the named four `k4cov` maps are
declared. Physical selection of `vertex3` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the 1-site coverage
table of the k=4 four on the declared patch, not leftover-character of #6435
or #6443.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the four `k4cov` maps scored on 12 seeds | no physical law selection |
| per block | `cov1=12` iff `vertex3=1` on this four | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than 1-site totality inside `k4cov`, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** the k=4 bits already fill every long-axis 2-site seed, so they
fill every one-site seed as well.

**Answer:** The two `vertex3=0` maps fill only eight of the twelve one-site
seeds. Inside this four, 1-site totality requires the extra bit `vertex3=1`.
That extra is displayed, not adopted.

### N8 — cross-cycle echo

Investment #6435 already showed that the 1-site maximizers are exactly the
`opp2 × mixed3` square with `vertex3=1`. The present count is a new domain:
the k=4 four, two of which lie off that square. Echoing the maximizer list
is not a substitute for scoring those two maps.

No-Go Discipline disposition: **PASS** for the finite four-map table and the
narrow displayed equivalence. FAIL / DO NOT SHIP for “`vertex3` is the
physical rule” or “the k=4 bits already give 1-site totality.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner builds the four `k4cov` maps from remaining bits, scores
`cov1` on the twelve one-site seeds, reconfirms that the two `vertex3=1` maps
have `cov1=12`, reports `cov1=8` for the two `vertex3=0` maps, and checks
that `cov1=12` if and only if `vertex3=1` inside this four. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.

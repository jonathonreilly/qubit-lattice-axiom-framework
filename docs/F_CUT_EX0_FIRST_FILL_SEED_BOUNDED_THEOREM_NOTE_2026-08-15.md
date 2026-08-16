---
claim_id: f_cut_ex0_first_fill_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the lex-first seed that F_cut (0,0,1,1,0) fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_ex0_first_fill_seed_2026_08_15.py
---

# Lex-First Seed that `F_cut` `(0,0,1,1,0)` Fills

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock first fill of one named cube-covariant cut
map on the twelve-vertex two-cube with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_ex0_first_fill_seed_2026_08_15.py`](../scripts/f_cut_ex0_first_fill_seed_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6511/#6502 named the map `f_ex0` with remaining bits
`(0,0,1,1,0)`, recorded `P=0` and `cov3=24`, and recorded that the origin
singleton dies at history (1). This note is the first fill of that newly
named map: the lex-first seed it fills. New first fill of a newly named
map, not leftover of the P=0 / cov3=24 counts.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

`f_ex0` is the `F_cut` map with remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3) = (0, 0, 1, 1, 0)`.

On the two-cube with off-patch occupancy `0`:

- Theorem 1. `P=0` and `cov3 = 24`. The origin singleton dies at history (1).
  The 2-site coverage is `cov2 = 0`.
- Theorem 2. The lex-first seed that `f_ex0` fills has `|S| = 3` and sites
  `(0, 0, 0), (1, 0, 1), (2, 1, 0)`.
- Theorem 3. The history sizes (3, 5, 7, 10, 12) are displayed. Displayed,
  not adopted.

Do not write the seed or the remaining bits into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "P, cov2, cov3, and the lex-first filling seed of one named F_cut map are finite exact counts on the two-cube. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_ex0_first_fill_seed
target_blocker_text: "when can the named P=0 map f_ex0=(0,0,1,1,0) fill at all"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first-fill seed; do not adopt the displayed seed or remaining bits"
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

**Target.** Report the lex-first seed that `f_ex0` fills on `T`.

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

Seeds are searched by increasing size, then by lexicographic order of
sorted site tuples in the product order on `T`. Write `P=0` when the origin
singleton `{(0,0,0)}` is already a fixed point (history (1)). Write
`cov_k(f)` for the number of unordered k-site seeds from which `f` fills.

## Theorems

### Theorem 1 — `P=0`, `cov3 = 24`, and `cov2 = 0`

The origin singleton has neighborhood type `(1,0,2)` at the unique locked
site's `+x` neighbor and empty otherwise. That type is the `wt1` remaining
bit of `f_ex0`, which is 0. No unlocked site therefore locks, so the
process dies at history (1). In particular `P=0` and `f_ex0` fills no
1-site seed.

Exhaustive scoring of the `C(12,2)=66` two-site seeds and the
`C(12,3)=220` three-site seeds gives

```text
cov2 = 0,   cov3 = 24.
```

This reconfirms the #6511/#6502 coverage pair and reports the 2-site
control.

### Theorem 2 — lex-first filling seed

Because `cov1 = 0` and `cov2 = 0`, no seed of size 1 or 2 fills. Among the
220 three-site seeds, in lex order of combinations of `T`, the first seed
that fills is

```text
S = {(0, 0, 0), (1, 0, 1), (2, 1, 0)},   |S| = 3.
```

No earlier three-site combination fills.

### Theorem 3 — displayed history; not adopted

From that seed the locked-set sizes are history sizes (3, 5, 7, 10, 12):

```text
t0  (0, 0, 0), (1, 0, 1), (2, 1, 0)
t1  (0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), (2, 1, 0)
t2  (0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0), (2, 1, 0)
t3  (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 0, 1), (2, 1, 0)
t4  all twelve vertices of T
```

The seed and the remaining-bit tuple `(0, 0, 1, 1, 0)` are displayed, not
adopted. Neither is written into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | remaining-bit class recalled |
| `f_ex0` as remaining bits `(0,0,1,1,0)` | defined |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, off-patch 0 | declared finite patch |
| `P=0` and origin history (1) | proved by evolution |
| `cov2 = 0`, `cov3 = 24` | proved by exhaustive scoring |
| lex-first fill `|S| = 3` at the displayed sites | proved by lex search |
| displayed history, not adopted | stated |
| leftover of #6511/#6502 coverage counts | refused; new first-fill object |
| physical Admissibility selector | open |

## Boundary and imports

New first fill of a newly named map. The #6511/#6502 scores `P=0` and
`cov3=24` are reconfirmed as controls; they do not already name a filling
seed. The note is not leftover of the P=0 / cov3=24 counts.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the seed or the
remaining bits into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers when the named map `f_ex0` can fill at all, by exhibiting the lex-first seed. |
| V2 | Current main has no landed first-fill seed for remaining bits `(0,0,1,1,0)`. |
| V3 | The two-cube, the occupancy-to-lock rule, and the lex search are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores one declared finite map. |
| V5 | It is not a physical selector: the seed and remaining bits are displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: this named map does not fill from the
origin or from any 2-site seed, and the first fill is a displayed size-3
seed. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_ex0` or `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover coverage | treat the seed as leftover-character of the P=0 / cov3=24 counts | **ATTEMPTED** |
| identify with `f_L1` | replace `f_ex0` by the unbalanced-axis map | **ATTEMPTED** |
| adopt the seed | write the size-3 seed into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch fill to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed origin fill, the Hamming contrast, and the off-patch convention
are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, off-patch occupancy `0`, occupancy-to-lock ticks, the
remaining-bit order, and the lex seed order are declared. Unique selection
of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the lex-first filling
seed of the newly named map `f_ex0`, not leftover of the P=0 / cov3=24
counts.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by remaining-bit assignment | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | P, cov2, cov3, and the lex-first seed of this map | no physical law selection |
| per block | displayed size-3 seed and its history | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than first fill of this named map, and any independently
derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `P=0` and `cov2 = 0` already say the map never fills, so a
first-fill seed is empty work.

**Answer:** `cov3 = 24` already says some three-site seeds fill. The new
object is which seed is lex-first, together with its displayed history.
That seed is displayed, not adopted.

### N8 — cross-cycle echo

Investment #6511/#6502 already scored `P=0` and `cov3=24`. Echoing those
counts is not a substitute for naming the lex-first filling seed.

No-Go Discipline disposition: **PASS** for the finite first-fill report.
FAIL / DO NOT SHIP for “the displayed seed is the physical formation seed”
or “remaining bits `(0,0,1,1,0)` are written into Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner evaluates `f_ex0` on the two-cube with off-patch
occupancy `0`, reconfirms `P=0` and origin history (1), reports `cov2 = 0`
and `cov3 = 24`, and exhibits the lex-first filling seed together with its
history. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.

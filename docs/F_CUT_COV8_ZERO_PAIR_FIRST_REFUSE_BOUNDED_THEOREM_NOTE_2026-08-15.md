---
claim_id: f_cut_cov8_zero_pair_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, the two maps with cov8=0 and the first remaining-bit refuse of the lex-first of them on the lex-first 8-site f1 fill are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov8_zero_pair_first_refuse_2026_08_15.py
---

# Two `cov8=0` `F_cut` Maps and the First Remaining-Bit Refuse

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 8-site fill counts on the twelve-vertex
two-cube with off-patch occupancy `0`, for the thirty-two cube-covariant
cut maps `F_cut`. The two remaining-bit tuples with `cov8=0` and the
first remaining-bit refuse of the lex-first of those tuples on the
lex-first 8-site seed that `f1` fills are reported.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov8_zero_pair_first_refuse_2026_08_15.py`](../scripts/f_cut_cov8_zero_pair_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6527 scores 8-site coverage on the same two-cube: `N_pos=30`,
so exactly two of the 32 `F_cut` maps have `cov8=0`. Both are Q4-false.
This note names those two remaining-bit tuples and the first remaining-bit
refuse of the lex-first of them. New zero-class at `k=8`, not leftover 6-site zero-class of #6526.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f1` for the remaining-bit tuple `(1, 1, 1, 1, 1)`: it fires on every
remaining-bit orbit. Q4 is the remaining-bit predicate `wt1=1` or `adj2=1`.
A map is Q4-false when `wt1=0` and `adj2=0`.

On the two-cube with off-patch occupancy `0`, write
`cov8(f) = |{S : |S|=8 and f fills from S}|`. Then:

- Theorem 1. The two remaining-bit tuples with `cov8=0`, in lex order, are
  `(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`. Both are Q4-false. `N_pos = 30`.
- Theorem 2. The lex-first of those two is `(0, 0, 0, 0, 0)`. The lex-first
  8-site seed that `f1` fills is
  `S={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)}`.
  The first remaining-bit refuse of `(0, 0, 0, 0, 0)` from `S` is tick `0`,
  site `(2, 0, 0)`, remaining-bit type `wt1`.
- Theorem 3. The pair and the refuse are displayed only. Do not adopt a
  remaining bit. Do not write the pair or the refuse into Admissibility.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 495 eight-site seeds of the two-cube. The cov8=0 pair and the first remaining-bit refuse are finite exact names. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov8_zero_pair_first_refuse
target_blocker_text: "name the two F_cut remaining-bit tuples with cov8=0 and the first remaining-bit refuse of the lex-first of them"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded cov8=0 pair and first remaining-bit refuse; do not adopt a displayed bit"
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

**Target.** Name the two `F_cut` remaining-bit tuples with `cov8=0` and the
first remaining-bit refuse of the lex-first of them on the lex-first 8-site
seed that `f1` fills.

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

The 8-site seeds are the `495` unordered 8-subsets of `T`, listed in
lexicographic site order induced by
`(x,y,z)` with `x ∈ {0,1,2}`, `y ∈ {0,1}`, `z ∈ {0,1}`. Then `cov8(f)` is
the number of those seeds from which `f` fills.

A remaining-bit refuse of a map `f` from a seed `S` is an unlocked site
whose six-neighbor occupancy is a remaining-bit type (so `f1` returns 1)
on which `f` returns 0. The first such refuse is the least tick, then the
lexicographically first site at that tick.

## Theorems

### Theorem 1 — the two `cov8=0` remaining-bit tuples

Among the 32 maps in `F_cut`, exactly two have `cov8=0`. In remaining-bit
lex order they are

```text
(wt1, opp2, adj2, vertex3, mixed3) = (0, 0, 0, 0, 0)
(wt1, opp2, adj2, vertex3, mixed3) = (0, 0, 0, 0, 1)
```

Both have `wt1=0` and `adj2=0`, so both are Q4-false. The complementary
count is `N_pos = 30`.

### Theorem 2 — first remaining-bit refuse of the lex-first zero map

The lex-first `cov8=0` tuple is `(0, 0, 0, 0, 0)`. The lex-first 8-site
seed that `f1` fills is

```text
S = {(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)}.
```

`f1` fills from `S`. The map `(0, 0, 0, 0, 0)` does not fill from `S`.

From `S`, the four unlocked sites at tick `0` are the face `x=2`. Each
has axis type `(1,0,2)` (`wt1`). The first remaining-bit refuse of
`(0, 0, 0, 0, 0)` from `S` is therefore

- tick `0`,
- site `(2, 0, 0)`,
- remaining-bit type `wt1`.

### Theorem 3 — display; do not adopt a bit

The two remaining-bit tuples and the refuse `(tick, site, type) = (0, (2, 0, 0), wt1)`
are displayed only. Do not adopt a remaining bit. Neither tuple is written
into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, 495 eight-site seeds, off-patch 0 | declared finite patch |
| two remaining-bit tuples with `cov8=0` | proved by exhaustive ranking |
| both zeros Q4-false; `N_pos = 30` | proved by the same census |
| first remaining-bit refuse of the lex-first zero | proved by evolution from `S` |
| leftover-character of #6526 | refused; new zero-class at `k=8` |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6526: that named the first remaining-bit refuse
of the lex-first `cov6=0` Q4-false map on a 6-site seed. The present objects
are the `cov8=0` pair and an 8-site refuse. The two zero maps at `k=8` are
`(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`, a proper subset of the four
`cov6=0` Q4-false maps with `vertex3=0`.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write the pair or the refuse
into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the two `F_cut` maps with `cov8=0` and the first remaining-bit refuse of the lex-first of them. |
| V2 | Current main has no landed `cov8=0` pair or 8-site remaining-bit refuse for `F_cut`. |
| V3 | The 32 maps, 495 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a declared finite class. |
| V5 | It is not a physical selector: the pair and refuse are displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: 8-site coverage vanishes on exactly two
`F_cut` maps on this patch, both Q4-false, and the first remaining-bit
refuse of the lex-first of them is `wt1`. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover 6-site zeros | treat the `cov8=0` pair as leftover-character of #6526 | **ATTEMPTED** |
| adopt a remaining bit | write `(0, 0, 0, 0, 0)` or `wt1` into Admissibility | **ATTEMPTED** |
| Q4 as 8-site selector | claim Q4-false iff `cov8=0` | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The `cov8=0` pair, the Hamming contrast, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 495 eight-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, and the `F_cut` remaining-bit order are declared.
Adoption of a remaining bit is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the `cov8=0` pair and
the first remaining-bit refuse at `k=8`, not leftover-character of #6526
and not Hamming identification of `f_L1`.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 495 seeds | no physical law selection |
| per block | `cov8=0` pair and first refuse on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than 8-site vanishing, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Q4 already names the 8-site zeros, so the pair and refuse add
nothing.

**Answer:** Q4-false is eight maps. Only two of them have `cov8=0`. Q4 is
not the 8-site vanishing predicate. The refuse is a new `k=8` object.

### N8 — cross-cycle echo

Investment #6526 already showed a 6-site zero-class among Q4-false maps
with `vertex3=0`. Echoing that class is not a substitute for the `k=8`
pair `(0, 0, 0, 0, 0)`, `(0, 0, 0, 0, 1)` or for the 8-site `wt1` refuse.

No-Go Discipline disposition: **PASS** for the finite `cov8=0` pair and
the named remaining-bit refuse. FAIL / DO NOT SHIP for “the displayed
tuple is the physical rule” or “Q4 equals `cov8=0`.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov8` on the
495 eight-site seeds, names the two remaining-bit tuples with `cov8=0` in
lex order, and reports the first remaining-bit refuse of the lex-first of
them on the lex-first 8-site seed that `f1` fills. Declared audit inputs
are this note and the axiom memo; the runner writes no cache and authors
no audit verdict.

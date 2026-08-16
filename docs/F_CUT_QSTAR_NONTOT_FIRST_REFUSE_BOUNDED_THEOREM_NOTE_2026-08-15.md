---
claim_id: f_cut_qstar_nontot_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first remaining-bit refuse of F_cut (1,0,1,0,0) from S={(1,0,0)} is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_nontot_first_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse of `f_nt` from the `q1split` Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock evolution of the named `Q_*` map
`f_nt` with remaining bits `(1, 0, 1, 0, 0)` on the twelve-vertex
two-cube with off-patch occupancy `0`, started from the displayed
`q1split` seed `S = {(1, 0, 0)}`, reporting the first remaining-bit
refuse.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_nontot_first_refuse_2026_08_15.py`](../scripts/f_cut_qstar_nontot_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6528 starts from the `q1split` seed: the first fill split of
`f_L1` against `f_nt` is `S = {(1, 0, 0)}`. This note does not re-rank
Max(1) and does not restate that split. It names the first remaining-bit
refuse of `f_nt` from that seed. Mechanism of `Q_*` non-totality.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`Q_*` is the subclass with `wt1=1` and `adj2=1`. It has 8 maps.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f_nt` for the `F_cut` map with remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 0, 0)`. It is the lex-first
`Q_*` map with `vertex3=0`. On the two-cube with off-patch occupancy `0`,
started from `S = {(1, 0, 0)}`:

- Theorem 1. The first remaining-bit refuse of `f_nt` from `S` is the
  `vertex3` neighborhood `(1, 0, 0, 1, 0, 1)` at site `(0,1,1)`, at tick 3.
- Theorem 2. On that first refuse tick, `N_refuse = 2`.
- Theorem 3. That refuse is displayed. Do not adopt a bit.

`Q_*` is the displayed subclass `{f ∈ F_cut : wt1=1 and adj2=1}`. It is
not written into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One named Q_* map is evolved exactly from the displayed q1split seed on the twelve-vertex two-cube. The first remaining-bit refuse (tick, site, remaining-bit type) and N_refuse on that tick are finite exact counts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_nontot_first_refuse
target_blocker_text: "first remaining-bit refuse of f_nt from S={(1,0,0)}, as the mechanism of Q_* non-totality"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the f_nt refuse from the q1split seed; do not adopt a displayed bit"
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
  `{±e_x, ±e_y, ±e_z}` at every site, in order
  `(+x,-x,+y,-y,+z,-z)`;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`;
- the subclass `Q_*` of those maps with remaining bits `wt1=1` and `adj2=1`;
- the named map `f_nt` with remaining bits `(1, 0, 1, 0, 0)`;
- the displayed `q1split` seed `S = {(1, 0, 0)}`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** On the run of `f_nt` from `S = {(1, 0, 0)}`, report the first
remaining-bit refuse (tick, site, remaining-bit type) and the number of
remaining-bit refuses on that first tick.

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

A neighborhood is a remaining-bit neighborhood when its axis type is one of
the five remaining types or a complement partner of one of them. Empty and
full are not remaining bits. The first remaining-bit refuse on a run is the
first remaining-bit neighborhood, in tick order and then two-cube lex order
of sites, at which `f` returns 0. `N_refuse` on a tick is the number of
unlocked sites whose neighborhood is a remaining-bit type and whose
predicate value is 0.

## Theorems

### Theorem 1 — first remaining-bit refuse: tick, site, type

`f_nt` is the `F_cut` map with remaining-bit tuple `(1, 0, 1, 0, 0)`.
Direct evolution from `S = {(1, 0, 0)}` does not fill: the run halts at
the ten-site set

```text
{(0,0,0), (0,0,1), (0,1,0), (1,0,0), (1,0,1), (1,1,0), (1,1,1), (2,0,0), (2,0,1), (2,1,0)}.
```

Tick 1 accepts four `wt1` neighborhoods and refuses only empty
neighborhoods. Empty is not a remaining bit.

Tick 2 accepts five `adj2` neighborhoods and refuses only empty
neighborhoods.

Tick 3 is the first tick at which a remaining-bit neighborhood is refused.
The lex-first refused remaining-bit neighborhood, in two-cube site order, is

```text
site (0,1,1), neighborhood (1, 0, 0, 1, 0, 1), axis type (3, 0, 0) = vertex3
```

The first remaining-bit refuse of `f_nt` from `S` is therefore `vertex3`
at site `(0,1,1)`, at tick 3. No `opp2` or `mixed3` neighborhood appears
before that refuse.

### Theorem 2 — `N_refuse` on that first tick

On tick 3 the two unlocked sites are both `vertex3` neighborhoods and both
are refused:

```text
site (0,1,1), neighborhood (1, 0, 0, 1, 0, 1), axis type (3, 0, 0) = vertex3
site (2,1,1), neighborhood (0, 1, 0, 1, 0, 1), axis type (3, 0, 0) = vertex3
```

So `N_refuse = 2` on the first refuse tick. There is no remaining-bit
accept on that tick. The run then halts.

### Theorem 3 — display; do not adopt a bit

The first refuse is a `vertex3` neighborhood, and `f_nt` has `vertex3=0`.
That is the mechanism of `Q_*` non-totality on this seed: `f_nt` shares
`wt1=1` and `adj2=1` with `f_L1`, grows through those remaining bits, and
stops at the first `vertex3` pair.

The contrast map with remaining bits `(1, 0, 1, 1, 0)` (the same bits as
`f_nt` except `vertex3=1`) fills from `S`. Displayed, not adopted. Do not
adopt a bit. Do not adopt `vertex3`. Do not write the ranking into
Admissibility. Do not write `Q_*` or `vertex3=1` into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | eight maps |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| `f_nt` remaining bits `(1, 0, 1, 0, 0)` | defined |
| two-cube, `S = {(1, 0, 0)}`, off-patch 0 | declared finite patch |
| first remaining-bit refuse is `vertex3` at `(0,1,1)`, tick 3 | proved by evolution |
| `N_refuse = 2` on that first tick | proved by the same tick |
| adopt `vertex3` or write `Q_*` into Admissibility | refused; displayed, not adopted |
| leftover-character of the `q1split` seed census | refused; this is a refuse mechanism |
| leftover-character of #6473 | refused; not a re-rank of Max(1) |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the `q1split` seed census: that named
`S = {(1, 0, 0)}` as the first fill disagreement of `f_L1` against `f_nt`.
The present theorem reports the first remaining-bit neighborhood refused
on the run of `f_nt` from that seed. Not leftover-character of #6473:
that ranked Max(1). Mechanism of `Q_*` non-totality, not a re-rank.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not adopt a bit. Do not adopt
`vertex3`. Do not write the ranking into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which remaining-bit neighborhood `f_nt` first refuses from `S = {(1, 0, 0)}`. |
| V2 | Current main has no landed remaining-bit refuse of `f_nt` from the `q1split` seed. |
| V3 | The named map, the named seed, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a named map on a declared run. |
| V5 | It is not a physical selector: the `vertex3` refuse is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch, `f_nt` refuses its first
remaining-bit neighborhood in the `vertex3` class, and that refuse is not
a reason to write `vertex3=1` into Admissibility. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover `q1split` seed | treat the refuse as leftover-character of the fill-split census | **ATTEMPTED** |
| leftover Max(1) ranking | treat the refuse as leftover-character of #6473 | **ATTEMPTED** |
| adopt a bit | write `vertex3=1` or `Q_*` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| empty as remaining-bit | count a tick-1 empty refuse as the first remaining-bit refuse | **ATTEMPTED** |

### N2 — wall independence

The `vertex3` refuse, the Hamming contrast, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the seed `S = {(1, 0, 0)}`, off-patch occupancy `0`,
occupancy-to-lock ticks, two-cube lex site order, and the `F_cut`
remaining-bit order are declared. Adoption of `vertex3` is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first remaining-bit
refuse of `f_nt` from `S`, not leftover-character of the `q1split` seed
census and not leftover-character of #6473.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_nt` evolved from `S = {(1, 0, 0)}` | no physical law selection |
| per block | first remaining-bit refuse and `N_refuse` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed, a different off-patch rule, a later
non-tot `Q_*` map, a selector other than a remaining-bit refuse, and any
independently derived physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `f_nt` already has `Q_*`, so a 1-site seed should fill, and
the only way to restore fill is to adopt `vertex3=1`.

**Answer:** `wt1=1` and `adj2=1` accept the first two growth steps. The
first remaining-bit refuse is `vertex3`, and that is why `f_nt` does not
fill `S`. The contrast with `vertex3=1` is displayed, not adopted. The
extra that would write `vertex3` into Admissibility is not present.

### N8 — cross-cycle echo

The `q1split` census already named `S = {(1, 0, 0)}` as the first fill
disagreement. Echoing that seed is not a substitute for the refuse on the
run. This note reports the first remaining-bit refuse of `f_nt` from `S`.

No-Go Discipline disposition: **PASS** for the finite `f_nt` refuse and
the narrow non-adoption of a bit. FAIL / DO NOT SHIP for “`vertex3` is the
physical rule” or “`Q_*` is written into Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner builds `f_nt` from remaining bits `(1, 0, 1, 0, 0)`,
evolves occupancy-to-lock from `{(1, 0, 0)}`, and reports the first
remaining-bit refuse as the `vertex3` neighborhood `(1, 0, 0, 1, 0, 1)`
at `(0,1,1)` on tick 3, with `N_refuse = 2` on that tick. The contrast
map `(1, 0, 1, 1, 0)` is displayed, not adopted. Declared audit inputs are
this note and the axiom memo; the runner writes no cache and authors no
audit verdict.

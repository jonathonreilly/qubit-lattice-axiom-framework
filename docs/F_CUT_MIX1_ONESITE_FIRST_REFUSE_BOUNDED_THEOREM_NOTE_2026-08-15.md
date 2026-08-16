---
claim_id: f_cut_mix1_onesite_first_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first refused neighborhood of F_cut (1,0,0,0,1) from the origin 1-site seed is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_mix1_onesite_first_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse of F_cut (1,0,0,0,1) on the Origin 1-Site Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock evolution of one named cube-covariant cut
map on the twelve-vertex two-cube with off-patch occupancy `0`, started from
the lex-first one-site seed, reporting the first remaining-bit neighborhood
the map refuses.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_mix1_onesite_first_refuse_2026_08_15.py`](../scripts/f_cut_mix1_onesite_first_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6516 asked why the displayed class `Q_*` of `F_cut` maps with
`wt1=1` and `adj2=1` is exactly the subclass that can have `cov1>0`. This
note answers on one named map and one named seed. It is the refuse mechanism
on that run, not a coverage ranking and not a seed-table of `f_min`.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f_mix1` for the `F_cut` map with remaining-bit tuple
`(wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 0, 0, 1)`. In particular
`wt1=1` and `adj2=0`. Let `S` be the lex-first one-site seed `{(0,0,0)}`.
On the two-cube with off-patch occupancy `0`:

- Theorem 1. `f_mix1` does not fill `S`. The halt set has size 9. The
  one-site coverage is `cov1(f_mix1) = 0`.
- Theorem 2. The first remaining-bit refuse on that run is the `adj2`
  neighborhood `(0, 0, 0, 1, 0, 1)` at site `(0,1,1)`, at tick 2.
- Theorem 3. That refuse is displayed. Do not adopt `adj2`.

`Q_*` is the displayed subclass `{f ∈ F_cut : wt1=1 and adj2=1}`. It is
not written into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One named F_cut map is evolved exactly from the origin 1-site seed on the twelve-vertex two-cube. The first remaining-bit refuse, the halt size, and cov1(f_mix1)=0 are finite exact counts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_mix1_onesite_first_refuse
target_blocker_text: "first remaining-bit neighborhood that f_mix1 refuses from the origin 1-site seed, as the mechanism that Q_* needs adj2=1 for cov1>0"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the origin-run refuse; do not adopt adj2"
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
- the named map `f_mix1` with remaining bits `(1, 0, 0, 0, 1)`;
- the lex-first one-site seed `S = {(0,0,0)}`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** On the origin one-site run of `f_mix1`, report the first
remaining-bit neighborhood the map refuses, and reconfirm that the run does
not fill.

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
rule from `L_0 = S` reaches `L = T` in at most 13 ticks. Then
`cov1(f)` is the number of one-site seeds from which `f` fills.

A neighborhood is a remaining-bit neighborhood when its axis type is one of
the five remaining types or a complement partner of one of them. Empty and
full are not remaining bits. The first remaining-bit refuse on a run is the
first remaining-bit neighborhood, in tick order and then two-cube lex order
of sites, at which `f` returns 0.

## Theorems

### Theorem 1 — `f_mix1` does not fill `S`; `cov1=0`

`f_mix1` is the `F_cut` map with remaining-bit tuple `(1, 0, 0, 0, 1)`.
Direct evolution from `S = {(0,0,0)}` halts after 4 growth ticks at the
nine-site set

```text
{(0,0,0), (0,0,1), (0,1,0), (1,0,0), (1,0,1), (1,1,0), (2,0,0), (2,0,1), (2,1,0)}.
```

The three unlocked sites are the line `y=1`, `z=1`. In particular `f_mix1`
does not fill `S`. Scoring every one-site seed gives `cov1(f_mix1) = 0`.

### Theorem 2 — first remaining-bit refuse

On the same origin run, tick 1 accepts three `wt1` neighborhoods and refuses
only empty neighborhoods. Empty is not a remaining bit.

Tick 2 is the first tick at which a remaining-bit neighborhood is refused.
The three simultaneous remaining-bit refuses, in two-cube lex order, are

```text
site (0,1,1), neighborhood (0, 0, 0, 1, 0, 1), axis type (2, 0, 1) = adj2
site (1,0,1), neighborhood (0, 1, 0, 0, 0, 1), axis type (2, 0, 1) = adj2
site (1,1,0), neighborhood (0, 1, 0, 1, 0, 0), axis type (2, 0, 1) = adj2
```

The first remaining-bit refuse is therefore the `adj2` neighborhood
`(0, 0, 0, 1, 0, 1)` at site `(0,1,1)`. No `opp2` or `vertex3` neighborhood
appears before that refuse. Later ticks accept some `mixed3` neighborhoods
and continue to refuse `adj2`; the run still cannot fill.

### Theorem 3 — display; do not adopt `adj2`

The first refuse is an `adj2` neighborhood, and `f_mix1` has `adj2=0`.
That is the mechanism of `Q_*` on this seed: every `F_cut` map with
`wt1=1` and `adj2=0` has `cov1=0`, and the origin run of `f_mix1` is
blocked at the first `adj2` neighborhood.

The contrast map with remaining bits `(1, 0, 1, 0, 1)` (the same bits as
`f_mix1` except `adj2=1`) fills from `S` and has `cov1=8`. Displayed, not
adopted. Do not adopt `adj2`. Do not write `Q_*` or `adj2=1` into
Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| `f_mix1` remaining bits `(1, 0, 0, 0, 1)` | defined |
| two-cube, origin 1-site seed, off-patch 0 | declared finite patch |
| `f_mix1` does not fill `S`; halt size 9 | proved by evolution |
| `cov1(f_mix1) = 0` | proved by exhaustive 1-site scoring |
| first remaining-bit refuse is `adj2` at `(0,1,1)` | proved by the origin run |
| adopt `adj2` or write `Q_*` into Admissibility | refused; displayed, not adopted |
| leftover-character of a coverage ranking | refused; this is a refuse mechanism |
| seed-table of `f_min` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of a 1-site coverage ranking: that ranking reports
`cov1` numbers. The present theorem reports the first remaining-bit
neighborhood refused on the origin run of one named map. The note is not a
seed-table of `f_min`: no `f_min` seed census is compiled, and `f_L1` is not
identified with Hamming or with a minimum-support table.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not adopt `adj2`. Do not write
the displayed refuse, the contrast map, or `Q_*` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which remaining-bit neighborhood `f_mix1` first refuses from the origin 1-site seed. |
| V2 | Current main has no landed origin-run refuse for remaining bits `(1, 0, 0, 0, 1)`. |
| V3 | The 32 maps, the origin seed, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it scores a named map on a declared run. |
| V5 | It is not a physical selector: the `adj2` refuse is displayed, not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch, `f_mix1` refuses its first
remaining-bit neighborhood in the `adj2` class, and that refuse is not a
reason to write `adj2=1` into Admissibility. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover coverage ranking | treat the refuse as leftover-character of a `cov1` table | **ATTEMPTED** |
| `f_min` seed table | replace the origin run by a seed-table of `f_min` | **ATTEMPTED** |
| adopt `adj2` | write `adj2=1` or `Q_*` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| empty as remaining-bit | count the tick-1 empty refuse as the first remaining-bit refuse | **ATTEMPTED** |

### N2 — wall independence

The `adj2` refuse, the Hamming contrast, and the off-patch convention are
distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the origin singleton, off-patch occupancy `0`, occupancy-to-lock
ticks, two-cube lex site order, and the `F_cut` remaining-bit order are
declared. Adoption of `adj2` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first remaining-bit
refuse of `f_mix1` from `S`, not leftover-character of a coverage ranking
and not a seed-table of `f_min`.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_mix1` evolved from the origin seed; `cov1` scored on 12 seeds | no physical law selection |
| per block | first remaining-bit refuse and halt size on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed, a different off-patch rule, a selector
other than a remaining-bit refuse, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `f_mix1` has `wt1=1`, so a 1-site seed should fill, and the
only way to restore fill is to adopt `adj2=1`.

**Answer:** `wt1=1` accepts the first growth step. The first remaining-bit
refuse is `adj2`, and that is why `cov1(f_mix1)=0`. The contrast with
`adj2=1` is displayed, not adopted. The extra that would write `adj2` into
Admissibility is not present.

### N8 — cross-cycle echo

Investment #6516 already named `Q_*` as the `wt1=1` and `adj2=1` subclass
needed for `cov1>0`. Echoing that class membership is not a substitute for
the origin-run refuse. This note reports the first refused neighborhood.

No-Go Discipline disposition: **PASS** for the finite origin-run refuse and
the narrow non-adoption of `adj2`. FAIL / DO NOT SHIP for “`adj2` is the
physical rule” or “`Q_*` is written into Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner builds `f_mix1` from remaining bits `(1, 0, 0, 0, 1)`,
evolves occupancy-to-lock from `{(0,0,0)}`, reconfirms that the run does not
fill and that `cov1(f_mix1)=0`, and reports the first remaining-bit refuse
as the `adj2` neighborhood `(0, 0, 0, 1, 0, 1)` at `(0,1,1)`. The contrast
map `(1, 0, 1, 0, 1)` is displayed, not adopted. Declared audit inputs are
this note and the axiom memo; the runner writes no cache and authors no
audit verdict.

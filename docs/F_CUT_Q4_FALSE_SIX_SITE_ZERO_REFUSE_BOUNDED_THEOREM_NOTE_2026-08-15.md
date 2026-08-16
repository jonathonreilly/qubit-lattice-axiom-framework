---
claim_id: f_cut_q4_false_six_site_zero_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first remaining-bit refuse of F_cut (0,0,0,0,0) on the lex-first 6-site seed f1 fills is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q4_false_six_site_zero_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse Of The Lex-First `cov6=0` Q4-False Map

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock remaining-bit refuse of the remaining-bit
tuple `(0, 0, 0, 0, 0)` on the lex-first six-site seed that `f1` fills, on
the twelve-vertex two-cube with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q4_false_six_site_zero_refuse_2026_08_15.py`](../scripts/f_cut_q4_false_six_site_zero_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6526 showed that the four Q4-false maps with `vertex3=0` have
`cov6=0`. Those four remaining-bit tuples are `(0, 0, 0, 0, 0)`,
`(0, 0, 0, 0, 1)`, `(0, 1, 0, 0, 0)`, and `(0, 1, 0, 0, 1)`. The lex-first
of them is `f_z = (0, 0, 0, 0, 0)`. This note names the first remaining-bit
refuse of `f_z` on the lex-first 6-site seed that `f1` fills. Not leftover-character of #6526: that investment scored coverage zeros. The
present object is the first remaining-bit refuse. Mechanism of the `cov6` zeros.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

Write `f1` for remaining bits `(1, 1, 1, 1, 1)` and `f_z` for remaining
bits `(0, 0, 0, 0, 0)`. Q4-false means `wt1=0` and `adj2=0`. The map
`f_z` is Q4-false and has `vertex3=0`.

On the two-cube with off-patch occupancy `0`, a remaining-bit refuse of a
map `f` from a locked set `L` is an unlocked on-patch site whose
six-neighbor occupancy has a remaining-bit orbit type and `f=0` on that
neighborhood. Empty and full are forced bits, not remaining bits. Then:

- Theorem 1. The lex-first 6-site seed that `f1` fills is
  `S = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)}`.
  The map `f1` fills `S`. The first remaining-bit refuse of `f_z` from `S`
  is tick `1`, site `(1, 1, 0)`, remaining-bit type `adj2`.
- Theorem 2. `N_refuse = 4` on that first tick.
- Theorem 3. The refuse is displayed. Displayed, not adopted.

Do not adopt a bit. Do not write `adj2` or `f_z` into Admissibility.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block is a different rule and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The lex-first six-site seed that f1 fills and the first remaining-bit refuse of f_z=(0,0,0,0,0) from that seed are enumerated on the twelve-vertex two-cube. Tick, site, remaining-bit type, and N_refuse on that tick are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q4_false_six_site_zero_refuse
target_blocker_text: "first remaining-bit refuse of the lex-first cov6=0 Q4-false map on the lex-first 6-site f1 fill"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded first remaining-bit refuse of f_z; do not adopt a remaining bit"
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
predicate. The remaining-bit type `adj2` is a displayed refuse label, not
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

The map `f1` is the remaining-bit assignment that sends every remaining
orbit to `1`. The map `f_z` sends every remaining orbit to `0`. Because
empty and full are already `0`, `f_z` is the zero map on `{0,1}^6`.

A locked set `L` determines occupancies: a lattice neighbor in `L` has
occupancy `1`, and every other neighbor — including every off-patch
neighbor — has occupancy `0`. One synchronous tick replaces `L` by

```text
L ∪ { v in two-cube \ L : f(neighborhood_6(v; L)) = 1 }.
```

Tick `1` is the first such step from the seed. Fill means the halt set has
cardinality 12. There are `C(12,6)=924` unordered 6-site seeds. Seeds are
ordered by the lex order of the twelve vertices
`(x,y,z)` with `x` slowest and `z` fastest, then by combination order.

A remaining-bit refuse of `f` at locked set `L` is an unlocked on-patch
site `v` whose neighborhood axis-type is a remaining-bit orbit (or that
orbit's complement) and `f(neighborhood_6(v; L))=0`. The first remaining-bit
refuse from a seed is the lex-first such site on the earliest tick that has
any. `N_refuse` on that tick is the number of remaining-bit refuses at the
locked set just before the tick.

## Theorems

**Theorem 1.** There are exactly 24 proper cube rotations and exactly 10
orbits on `{0,1}^6`. The three cuts leave `|F_cut|=32`. The unbalanced-axis
map `f_L1` is one element of `F_cut` and is not Hamming parity. The map
`f1` has remaining bits `(1, 1, 1, 1, 1)` and fills every 6-site seed, so
in particular it fills the lex-first 6-site seed

```text
S = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)}.
```

The map `f_z` has remaining bits `(0, 0, 0, 0, 0)`. From `S` at tick `1`,
the unlocked sites and neighborhood types are

```text
(1, 1, 0)  adj2     (2, 0, 1)
(1, 1, 1)  adj2     (2, 0, 1)
(2, 0, 0)  wt1      (1, 0, 2)
(2, 0, 1)  wt1      (1, 0, 2)
(2, 1, 0)  empty    (0, 0, 3)
(2, 1, 1)  empty    (0, 0, 3)
```

Empty is not a remaining-bit type. The first remaining-bit refuse of
`f_z` from `S` is therefore tick `1`, site `(1, 1, 0)`, remaining-bit
type `adj2`.

**Theorem 2.** On that first tick the remaining-bit refuses are the four
sites `(1, 1, 0)`, `(1, 1, 1)`, `(2, 0, 0)`, and `(2, 0, 1)`. Hence
`N_refuse = 4`. The map `f_z` locks no new site, so the run is already at
a size-6 fixed point. That is the mechanism of this `cov6` zero: every
remaining-bit neighborhood is refused, and empty neighborhoods are
already forced to `0`.

**Theorem 3.** The first remaining-bit refuse

```text
(tick, site, type) = (1, (1, 1, 0), adj2)
```

and the count `N_refuse = 4` are displayed. No remaining bit is adopted as
the physical Admissibility rule.

## Proof-obligation graph

| obligation | exact disposition |
|---|---|
| 24 proper cube rotations | signed permutations of the three axes with determinant `+1` |
| 10 orbits on `{0,1}^6` | axis-type classes `(u,b,e)` partition the 64 cells |
| `|F_cut|=32` | three complement-pairs and two complement-fixed orbits remain free |
| `f1` fills `S` | remaining bits `(1, 1, 1, 1, 1)` fill the lex-first 6-site seed |
| first refuse | tick `1`, site `(1, 1, 0)`, type `adj2` |
| `N_refuse` | `4` remaining-bit refuses on that tick |
| `f_L1` is not Hamming | unbalanced-axis predicate disagrees with `|c|_1 mod 2` |
| displayed refuse | not adopted |

## What this does not claim

- No physical Admissibility selector.
- No `Z^3`-wide formation law.
- No ranking of the other 31 maps in `F_cut`.
- No adoption of `adj2`, `wt1`, or `f_z`.
- No blank-block or Hamming-as-`f_L1` identification.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It names the first remaining-bit refuse of `f_z` on the lex-first 6-site `f1` fill. |
| V2 | Current main has the axiom memo and the #6526 `cov6=0` class, but no landed first-refuse of `f_z` on that seed. |
| V3 | The 32 maps, 924 seeds, and occupancy-to-lock ticks are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it names a displayed refuse of a declared map. |
| V5 | The refuse is displayed and is not adopted and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `f_z` refuses the remaining-bit
neighborhoods of `S` at tick `1` and does not fill. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6526 | treat the refuse as leftover-character of the four `cov6=0` names | **ATTEMPTED** |
| leftover of #6518 | treat the refuse as leftover-character of `Q4` | **ATTEMPTED** |
| empty as remaining-bit | count the two empty-neighborhood sites as remaining-bit refuses | **ATTEMPTED** |
| adopt a bit | write `adj2` or `f_z` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The first-refuse name, the Hamming contrast, the #6526 coverage-zero class,
and the off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the remaining-bit
refuse filter are declared. The first refuse of `f_z` is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first remaining-bit
refuse of `f_z` on the lex-first 6-site `f1` fill, not leftover-character of
#6526 or #6518, and not a Hamming identification.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_z` on the lex-first 6-site `f1` fill | no physical law selection |
| per block | first refuse and `N_refuse` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, the
other three `cov6=0` maps, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** `f_z` is the zero map, so every unlocked site is refused and
naming one site is decoration of `cov6=0`.

**Answer:** Empty neighborhoods are not remaining-bit refuses. From `S` there
are six unlocked sites and only four remaining-bit refuses. The lex-first of
those four is site `(1, 1, 0)` of type `adj2`. Coverage zero does not name
that site or that type.

### N8 — cross-cycle echo

Investment #6526 already showed that the four Q4-false maps with
`vertex3=0` have `cov6=0`. Echoing that class is not a substitute for the
first remaining-bit refuse of the lex-first member on the lex-first 6-site
`f1` fill.

No-Go Discipline disposition: **PASS** for the named refuse and the count
`N_refuse = 4`. FAIL / DO NOT SHIP for “`adj2` is the physical rule” or
“displayed `f_z` is adopted.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner reconstructs the 24 rotations and 10 orbits, rebuilds
`F_cut`, names the lex-first 6-site seed that `f1` fills, evaluates the
first remaining-bit refuse of `f_z=(0,0,0,0,0)` from that seed, reports
tick `1`, site `(1, 1, 0)`, type `adj2`, and reports `N_refuse = 4`.
Declared audit inputs are this note and the axiom memo; the runner writes
no cache and authors no audit verdict.

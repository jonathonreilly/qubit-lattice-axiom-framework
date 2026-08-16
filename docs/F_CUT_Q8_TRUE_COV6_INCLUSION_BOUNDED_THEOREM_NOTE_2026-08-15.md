---
claim_id: f_cut_q8_true_cov6_inclusion_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether every Q8-true map has positive 6-site coverage is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q8_true_cov6_inclusion_2026_08_15.py
---

# Whether Every Q8-True `F_cut` Map Has Positive 6-Site Coverage

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 924 six-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`. Whether every Q8-true map has
`cov6>0` is the scored inclusion.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q8_true_cov6_inclusion_2026_08_15.py`](../scripts/f_cut_q8_true_cov6_inclusion_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6539 showed that the remaining-bit predicate
`Q8(f) := (wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` equals `cov8>0`
among the 32 maps (30 maps). Investment #6531 showed that
`Q6(f) := (wt1=1) or (adj2=1) or (vertex3=1)` equals `cov6>0` (28 maps).
`Q8` is strictly larger than `Q6`. This note is a new inclusion test:
whether every Q8-true map still has `cov6>0`. Not leftover-character of
those two selector identities.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov6(f) = |{S : |S|=6 and f fills from S}|`. Then:

- Theorem 1. Not every Q8-true map has `cov6>0`. The two extras, in
  remaining-bit lex order, are `(0, 1, 0, 0, 0)` and `(0, 1, 0, 0, 1)`.
  The lex-first Q8-true map with `cov6=0` is `(0, 1, 0, 0, 0)`.
- Theorem 2. `N_Q8 = 30`, `N_cov6 = 28`, `N_both = 28`.
- Theorem 3. `Q8` is displayed. Displayed, not adopted.

Do not adopt Q8. Do not write `Q8` into Admissibility.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block is a different rule and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 924 six-site seeds of the two-cube. Whether every Q8-true map has cov6>0, the two extras, and the counts N_Q8, N_cov6, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q8_true_cov6_inclusion
target_blocker_text: "whether every Q8-true F_cut map has cov6>0, and the extras if not"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed Q8-true versus cov6>0 inclusion; do not adopt Q8"
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
predicate. `Q8` is a displayed remaining-bit formula, not axiom content.

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

The six-site seeds are the `C(12,6) = 924` subsets of size 6 in `T`. Then
`cov6(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov6(f)>0`.

The displayed remaining-bit predicate is

```text
Q8(f) := (wt1 = 1) or (adj2 = 1) or (opp2 = 1) or (vertex3 = 1).
```

Mixed3 is free in `Q8`. Displayed, not adopted.

## Theorem 1 — not every Q8-true map has `cov6>0`

Enumerate all 32 remaining-bit tuples of `F_cut` and score `cov6` on the 924
six-site seeds. Then not every Q8-true map has `cov6>0`.

The Q8-true maps with `cov6=0`, in remaining-bit lex order
`(wt1, opp2, adj2, vertex3, mixed3)`, are

```text
(0, 1, 0, 0, 0)
(0, 1, 0, 0, 1)
```

Both have `opp2 = 1` and `wt1 = adj2 = vertex3 = 0`, so both are Q8-true
only through `opp2`. Both have `cov6 = 0`. The lex-first Q8-true map with
`cov6=0` is `(0, 1, 0, 0, 0)`.

## Theorem 2 — `N_Q8`, `N_cov6`, `N_both`

Among the 32 maps:

- `N_Q8 = 30` maps satisfy `Q8`;
- `N_cov6 = 28` maps have `cov6 > 0`;
- `N_both = 28` maps satisfy both.

Every map with `cov6>0` is Q8-true. Inclusion fails in the other direction:
two Q8-true maps have `cov6=0`. Those two are exactly the extras of
Theorem 1. The two Q8-false maps are `(0, 0, 0, 0, 0)` and `(0, 0, 0, 0, 1)`;
both also have `cov6=0`.

## Theorem 3 — display; do not adopt `Q8`

`Q8` is the same remaining-bit predicate that #6539 found equivalent to
`cov8>0`. On six-site seeds it is strictly larger than the positivity
selector. Displayed, not adopted. Do not adopt Q8. Do not write `Q8` into
Admissibility.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, satisfies `Q8` and has
`cov6>0`. That is consistent with Theorem 2 and does not restore inclusion.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 924 six-site seeds, off-patch `o=0` | declared finite patch |
| `Q8` as `(wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` | displayed, not adopted |
| every Q8-true map has `cov6>0` | fails; lex-first extra `(0, 1, 0, 0, 0)` |
| `N_Q8 = 30`, `N_cov6 = 28`, `N_both = 28` | proved by exhaustive scoring |
| leftover-character of #6539 or #6531 | refused; new inclusion test |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6539: that closed `Q8` iff `cov8>0` on eight-site
seeds. The present question is whether every Q8-true map has `cov6>0`.

Not leftover-character of #6531: that closed `Q6` iff `cov6>0`. The present
object is Q8-true versus six-site positivity, not a restatement of the Q6
selector.

New inclusion test: `Q8` is strictly larger than `Q6`, and the two extras
are exactly the Q8-true maps that remain Q6-false.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `Q8` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether every Q8-true map has `cov6>0` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo and the #6539 / #6531 selector identities, but no landed Q8-true versus `cov6>0` inclusion. |
| V3 | The 32 maps, 924 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against displayed `Q8`. |
| V5 | Inclusion fails, and displayed `Q8` is not adopted and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: not every Q8-true map has `cov6>0` among the
32 `F_cut` maps on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6539 | treat the inclusion as leftover-character of `Q8` iff `cov8>0` | **ATTEMPTED** |
| leftover of #6531 | treat the count as leftover-character of `Q6` iff `cov6>0` | **ATTEMPTED** |
| inherit from `cov8>0` | argue that Q8-true already fills at `k=8`, hence at `k=6` | **ATTEMPTED** |
| adopt `Q8` | write `(wt1=1) or (adj2=1) or (opp2=1) or (vertex3=1)` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed inclusion, the Hamming contrast, the #6539 eight-site identity,
and the off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the 924 six-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the displayed
predicate `Q8` are declared. Inclusion of Q8-true into `cov6>0` is not
silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether every Q8-true
map has `cov6>0` on the declared patch, not leftover-character of
#6539 or #6531, and not an eight-site fill inheritance.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 924 seeds | no physical law selection |
| per block | `N_Q8`, `N_cov6`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `Q8` or `cov6>0`, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6539 already showed that `Q8` is `cov8>0`, so every Q8-true
map fills some eight-site seed and therefore some six-site seed.

**Answer:** Inheritance fails. Thirty maps satisfy `Q8` and twenty-eight
have `cov6>0`. The two extras `(0, 1, 0, 0, 0)` and `(0, 1, 0, 0, 1)` are
Q8-true only through `opp2` and have `cov6=0`. The lex-first extra is
`(0, 1, 0, 0, 0)`. Displayed `Q8` is not adopted.

### N8 — cross-cycle echo

Investment #6539 already showed that `cov8>0` is `Q8`. Investment #6531
already showed that `cov6>0` is `Q6`. Echoing either identity is not a
substitute for the inclusion: `Q8` is strictly larger than `Q6`, and the
two extras plus the triple `(N_Q8, N_cov6, N_both)` are the new facts.

No-Go Discipline disposition: **PASS** for the finite inclusion and the
narrow failure. FAIL / DO NOT SHIP for “every Q8-true map has `cov6>0`” or
“displayed `Q8` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov6` on the
924 six-site seeds, tests whether every Q8-true map has `cov6>0`, names the
two extras and the lex-first extra `(0, 1, 0, 0, 0)`, and reports
`N_Q8 = 30`, `N_cov6 = 28`, and `N_both = 28`. Declared audit inputs are this
note and the axiom memo; the runner writes no cache and authors no audit
verdict.

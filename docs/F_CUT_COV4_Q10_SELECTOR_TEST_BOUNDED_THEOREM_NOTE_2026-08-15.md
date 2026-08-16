---
claim_id: f_cut_cov4_q10_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov4>0 equals adj2∨vertex3∨mixed3 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov4_q10_selector_test_2026_08_15.py
---

# Whether `cov4>0` Equals `Q10` Among The 32 `F_cut` Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 4-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored for the
thirty-two cube-covariant cut maps `F_cut`, against the displayed
remaining-bit predicate `Q10 := (adj2=1) or (vertex3=1) or (mixed3=1)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov4_q10_selector_test_2026_08_15.py`](../scripts/f_cut_cov4_q10_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c10bit3 closed the 10-site positivity question:
`cov10>0` if and only if the remaining-bit predicate

```text
Q10 := (adj2 = 1) or (vertex3 = 1) or (mixed3 = 1).
```

Investment #6518 closed the 4-site positivity question:
`cov4>0` if and only if `Q4 := (wt1 = 1) or (adj2 = 1)`.
Investment #6476 is Max duality only at `k=4,5`. Duality is not assumed
for positivity, so `cov10>0 iff Q10` does not transfer to
`cov4>0 iff Q10`. This note scores that transfer on the same 32 maps.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov4(f) = |{S : |S|=4 and f fills from S}|`. Then:

- Theorem 1. `cov4(f) > 0` is not equivalent to `Q10(f)` among the 32
  maps. The lex-first remaining-bit miss is `(0, 0, 0, 0, 1)`, which has
  `Q10 = 1` and `cov4 = 0`.
- Theorem 2. `N_pos = 24`, `N_Q10 = 28`, `N_both = 22`.
- Theorem 3. `Q10` is displayed. Displayed, not adopted.

Do not adopt Q10. Do not write `Q10` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 495 four-site seeds. Whether cov4>0 equals Q10=adj2∨vertex3∨mixed3 is a finite Boolean identity on this patch, not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_cov4_q10_selector_test
target_blocker_text: "whether cov4>0 iff Q10 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded cov4-versus-Q10 comparison; do not adopt Q10"
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
predicate. The candidate `Q10` below is a displayed remaining-bit formula,
not axiom content.

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

The four-site seeds are the `C(12,4) = 495` subsets of size 4 in `T`. Then
`cov4(f)` is the number of those subsets from which `f` fills. The boolean
scored here is `cov4(f)>0`.

`Q10` and the #6518 control `Q4` are functions of the remaining-bit tuple
only. Duality of Max at `k=4,5` is not used.

## Theorem 1 — `cov4>0` is not `Q10`; lex-first miss

Direct evolution on the 495 four-site seeds scores every `F_cut` map.
`cov4(f) > 0` is not equivalent to `Q10(f)` on all 32 maps.

The lex-first remaining-bit miss, in the order
`(wt1, opp2, adj2, vertex3, mixed3)`, is `(0, 0, 0, 0, 1)`. That map has
`mixed3 = 1`, so `Q10` is true, and `cov4 = 0`.

The identity would have held only if positivity at `k=4` inherited the
`k=10` selector. Duality is not assumed: #6476 licenses Max only at
`k=4,5`, and does not identify `cov4>0` with `cov10>0` or with `Q10`.
The miss is therefore a new `k=4` fact, not leftover-character of
c10bit3 and not leftover-character of #6518.

`f_L1` itself has remaining bits `(1, 0, 1, 1, 1)`, so `Q10` is true and
`cov4 = 489`. That is consistent with the miss and does not restore
equivalence.

## Theorem 2 — `N_pos`, `N_Q10`, `N_both`

Among the 32 maps:

- `N_pos = 24` maps have `cov4 > 0`;
- `N_Q10 = 28` maps satisfy `Q10`;
- `N_both = 22` maps satisfy both.

Equivalence fails in both directions. The two maps with `cov4>0` and
`Q10` false are the #6490 exceptions `(1, 0, 0, 0, 0)` and
`(1, 1, 0, 0, 0)`, each with `wt1 = 1` and
`(adj2, vertex3, mixed3) = (0, 0, 0)`, and each with `cov4 = 7`. The six
maps with `Q10` true and `cov4 = 0` are the remaining-bit tuples with
`wt1 = 0`, `adj2 = 0`, and `(vertex3, mixed3) ≠ (0, 0)`:

```text
(0, 0, 0, 0, 1), (0, 0, 0, 1, 0), (0, 0, 0, 1, 1),
(0, 1, 0, 0, 1), (0, 1, 0, 1, 0), (0, 1, 0, 1, 1).
```

Reconfirming #6518 on the same scoring: `cov4>0` equals `Q4 = wt1 ∨ adj2`
on all 32 maps (`N_Q4 = 24`, `N_both(Q4) = 24`). That control is
displayed only. It is not a transfer of `Q10` across `k`.

## Theorem 3 — display, not adoption

`Q10` is displayed data. Do not adopt Q10. Do not adopt `Q4`. Do not
adopt `f_L1`. Do not write `Q10` into Admissibility. Admissibility does
not name this remaining-bit formula.

The failed identity `cov4>0 ⇔ adj2∨vertex3∨mixed3` is a finite fact
about occupancy-to-lock on this two-cube with off-patch `o=0`. It is not
a physical formation-site selector and not an axiom edit.

Displayed, not adopted.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 495 four-site seeds, off-patch `o=0` | declared finite patch |
| `Q10` as `adj2∨vertex3∨mixed3` | displayed, not adopted |
| `cov4>0` iff `Q10` | fails; lex-first miss `(0, 0, 0, 0, 1)` |
| `N_pos = 24`, `N_Q10 = 28`, `N_both = 22` | proved by exhaustive scoring |
| duality of Max at `k=4,5` | not assumed for positivity |
| leftover-character of c10bit3 or #6518 | refused; new comparison |
| adoption of `Q10` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c10bit3: that closed `cov10>0` iff `Q10` on
ten-site seeds. The present object is `cov4>0` versus the same displayed
predicate on 495 four-site seeds. New k.

Not leftover-character of #6518: that closed `cov4>0` iff `Q4`. The
present comparison is `cov4>0` versus `Q10`, a different remaining-bit
formula.

#6476 is Max duality only at `k=4,5`. Duality is not assumed. The note
does not identify `cov4>0` with `cov10>0` and does not import a Max
ranking.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov4>0` equals `adj2∨vertex3∨mixed3` on the 32 `F_cut` maps. |
| V2 | Current main has the axiom memo, the c10bit3 identity `Q10=cov10>0`, and the #6518 identity `Q4=cov4>0`, but no landed `cov4` versus `Q10` test. |
| V3 | The 32 maps, 495 seeds, and Boolean predicates are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a declared candidate. |
| V5 | The candidate is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `cov4>0` is not `Q10` on this patch, and
a displayed miss is not axiom content. No global compiler impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c10bit3 | treat the 4-site test as restating `Q10=cov10>0` | **ATTEMPTED** |
| leftover of #6518 | treat the test as restating `Q4=cov4>0` | **ATTEMPTED** |
| duality transfer | inherit positivity from `k=10` by #6476 Max duality | **ATTEMPTED** |
| adopt `Q10` | write `adj2∨vertex3∨mixed3` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed equivalence, the Hamming contrast, the #6490 pair, the
#6476 Max-only duality bound, and the off-patch convention are distinct.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 495 four-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the
displayed predicate `Q10` are declared. Duality of positivity across
`k` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov4>0` equals `Q10` on this patch, not leftover-character of c10bit3
or #6518, and not a Max transfer.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 495 seeds against `Q10` | no physical law selection |
| per block | the failed identity and the three counts on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector other than `Q10` or `Q4`, and any independently derived
physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c10bit3 already showed that positivity is `Q10`, and
#6476 already pairs `k=4` with `k=8` or `k=10` by duality, so
`cov4>0` is `Q10`.

**Answer:** #6476 is Max only at `k=4,5`. Duality is not assumed for
positivity. Twenty-four maps have `cov4>0` and twenty-eight satisfy
`Q10`; twenty-two satisfy both. The lex-first miss `(0, 0, 0, 0, 1)`
has `Q10` true and `cov4 = 0`. Displayed `Q10` is not adopted.

### N8 — cross-cycle echo

Investment c10bit3 already showed that `cov10>0` is `Q10`. Investment
#6518 already showed that `cov4>0` is `Q4`. Echoing either identity is
not a substitute for testing `Q10` against 4-site positivity.

No-Go Discipline disposition: **PASS** for the finite comparison and the
lex-first miss. FAIL / DO NOT SHIP for “adopt Q10,” “`cov4>0` is `Q10`,”
or “duality transfers the `k=10` selector.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov4` on the
495 four-site seeds, tests whether `cov4>0` equals displayed `Q10`,
reports the lex-first remaining-bit miss `(0, 0, 0, 0, 1)`, and reports
`N_pos = 24`, `N_Q10 = 28`, and `N_both = 22`. Declared
audit inputs are this note and the axiom memo; the runner writes no cache
and authors no audit verdict.

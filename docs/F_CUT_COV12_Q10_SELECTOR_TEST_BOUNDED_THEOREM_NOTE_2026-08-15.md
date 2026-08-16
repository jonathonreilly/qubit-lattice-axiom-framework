---
claim_id: f_cut_cov12_q10_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether a displayed remaining-bit predicate equals cov12>0 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov12_q10_selector_test_2026_08_15.py
---

# Whether `cov12>0` Equals `Q10`, `Q8`, or `Q4`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 12-site fill positivity on the
twelve-vertex two-cube with off-patch occupancy `0`, scored on every one
of the 32 cube-covariant cut maps `F_cut`. The scored identities are
whether `cov12>0` if and only if displayed `Q10`, if and only if displayed
`Q8`, or if and only if displayed `Q4`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov12_q10_selector_test_2026_08_15.py`](../scripts/f_cut_cov12_q10_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c10bit3 named that `Q10=cov10>0` only, with the remaining-bit
formula `Q10 := adj2 ∨ vertex3 ∨ mixed3`. Investment #6539 named that
`Q8 := wt1 ∨ opp2 ∨ adj2 ∨ vertex3` equals `cov8>0`. Investment #6518
named that `Q4 := wt1 ∨ adj2` equals `cov4>0`. This note tests whether
any of those displayed predicates equals `cov12>0`. New k=12. Not
leftover-character of c10bit3, not leftover-character of #6539, and not
leftover-character of #6518.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple has
`Q10=Q8=Q4=1`.

On the two-cube with off-patch `o=0`, write
`cov12(f) = |{S : |S|=12 and f fills from S}|`. There is one 12-site
seed: the whole two-cube. The boolean scored here is `cov12(f)>0`.

**Theorem 1.** Among all 32 `F_cut` maps, `cov12>0` is not equivalent to
`Q10`, is not equivalent to `Q8`, and is not equivalent to `Q4`. Each
identity fails. The lex-first remaining-bit miss of each is
`(0, 0, 0, 0, 0)`: that map has `cov12=1` and `Q10=Q8=Q4=0`.

**Theorem 2.** The census integers on the 32-map set are

```text
N_pos = 32
N_Q10 = 28
N_both_Q10 = 28
N_Q8 = 30
N_both_Q8 = 30
N_Q4 = 24
N_both_Q4 = 24.
```

**Theorem 3.** The identities are displayed only. Displayed, not adopted.
Do not adopt a bit. Do not adopt Q10. Do not adopt Q8. Do not adopt Q4.
Do not write `Q10` into Admissibility.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are scored exactly on the one twelve-site seed. Whether cov12>0 equals Q10, Q8, or Q4 is a finite Boolean identity on this patch, and each identity fails. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_cov12_q10_selector_test
target_blocker_text: "whether cov12>0 equals Q10, Q8, or Q4 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded cov12>0 versus Q10, Q8, and Q4 identities; do not adopt a bit"
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
predicate. The displayed remaining-bit formulas below are not axiom content.

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

The twelve-site seeds are the `C(12,12) = 1` subsets of size 12 in `T`.
That unique seed is `T` itself. Then `cov12(f)` is 1 if `f` fills from
`T` and 0 otherwise. Starting from `L_0 = T` the locked set is already
`T`, so every `F_cut` map fills. The boolean scored here is `cov12(f)>0`.

The displayed remaining-bit predicates are

```text
Q10(f) := (adj2=1) or (vertex3=1) or (mixed3=1)
Q8(f) := (wt1=1) or (opp2=1) or (adj2=1) or (vertex3=1)
Q4(f) := (wt1=1) or (adj2=1)
```

`Q10` holds on exactly 28 of the 32 maps. `Q8` holds on exactly 30.
`Q4` holds on exactly 24. Duality is not assumed: `cov12` is scored on
the one twelve-site seed.

## Theorem 1 — `cov12>0` versus `Q10`, `Q8`, and `Q4` on all 32

Direct evolution on the one twelve-site seed scores every `F_cut` map.
Every map has `cov12 = 1`. The identities

```text
cov12(f) > 0  ⇔  Q10(f) = 1
cov12(f) > 0  ⇔  Q8(f) = 1
cov12(f) > 0  ⇔  Q4(f) = 1
```

each fail. The lex-first remaining-bit miss of each is `(0, 0, 0, 0, 0)`:
that map has `cov12=1` and `Q10=Q8=Q4=0`. There are four `Q10` misses,
two `Q8` misses, and eight `Q4` misses. In particular
`f_L1 = (1, 0, 1, 1, 1)` has `Q10=Q8=Q4=1` and `cov12=1`, so it is not
a miss.

## Theorem 2 — census integers

Write `N_pos` for the number of `F_cut` maps with `cov12>0`, and for each
displayed `Q` write `N_Q` for the number with `Q=1` and `N_both` for the
number with both. Then

```text
N_pos = 32
N_Q10 = 28
N_both_Q10 = 28
N_Q8 = 30
N_both_Q8 = 30
N_Q4 = 24
N_both_Q4 = 24.
```

These integers are counted from the scored 32-map table. They fail to
coincide because each identity of Theorem 1 fails: positivity holds on
every map, while each displayed `Q` is false on a nonempty lex-first
slice.

## Theorem 3 — display, not adoption

The failure of `cov12>0 ⇔ Q10`, of `cov12>0 ⇔ Q8`, and of
`cov12>0 ⇔ Q4` on all 32 `F_cut` maps is displayed data. Displayed,
not adopted. Do not adopt a bit. Do not adopt Q10. Do not adopt Q8. Do
not adopt Q4. Do not adopt `adj2`. Do not adopt `vertex3`. Do not adopt
`mixed3`. Do not adopt `f_L1`. Do not write `Q10` into Admissibility.
Admissibility does not name this remaining-bit formula.

The census is a finite fact about occupancy-to-lock on this two-cube
with off-patch `o=0`. It is not a physical formation-site selector and
not an axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q10` as `adj2=1` or `vertex3=1` or `mixed3=1` | twenty-eight maps |
| `Q8` as `wt1=1` or `opp2=1` or `adj2=1` or `vertex3=1` | thirty maps |
| `Q4` as `wt1=1` or `adj2=1` | twenty-four maps |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, one twelve-site seed, off-patch `o=0` | declared finite patch |
| `cov12>0` iff `Q10`, iff `Q8`, or iff `Q4` | all fail; lex-first miss `(0, 0, 0, 0, 0)` |
| `N_pos`, per-`Q` `N_Q` and `N_both` | 32; 28/28; 30/30; 24/24 |
| leftover of c10bit3 | refused; that was `Q10=cov10>0` |
| leftover of #6539 | refused; that named `Q8=cov8>0` |
| leftover of #6518 | refused; that named `Q4=cov4>0` |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c10bit3: that closed `Q10=cov10>0` only. The
present object is whether the same displayed formula equals twelve-site
positivity.

Not leftover-character of #6539: that closed `cov8>0` as `Q8`. New k=12
is not a restatement of eight-site positivity.

Not leftover-character of #6518: that closed `cov4>0` as `Q4`. The
present object is the same displayed formula against `cov12>0`.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt a bit. Do not adopt Q10.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov12>0` equals `Q10`, `Q8`, or `Q4` among all 32 `F_cut` maps. |
| V2 | Current main has the axiom memo and the named `Q10=cov10>0`, `Q8=cov8>0`, and `Q4=cov4>0` identities, but no landed twelve-site test. |
| V3 | The 32 maps and the one twelve-site seed are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against three displayed predicates at a new `k`. |
| V5 | Each identity fails, is displayed, and no bit is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: none of `Q10`, `Q8`, or `Q4` is
`cov12>0` among the 32 `F_cut` maps on this patch. No global compiler
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c10bit3 | treat the `k=12` test as leftover-character of `Q10=cov10>0` | **ATTEMPTED** |
| leftover of #6539 | treat the test as leftover-character of `Q8=cov8>0` | **ATTEMPTED** |
| leftover of #6518 | treat the test as leftover-character of `Q4=cov4>0` | **ATTEMPTED** |
| adopt a bit | write `Q10`, `Q8`, or `Q4` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the c10bit3 `Q10=cov10>0` identity, the #6539
`Q8` identity, the #6518 `Q4` identity, and the off-patch convention
are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the one twelve-site seed, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the three
displayed formulas are declared. Equality of any displayed `Q` with
`cov12>0` is not silently assumed. Duality is not assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is whether
`cov12>0` equals `Q10`, `Q8`, or `Q4` on all 32 `F_cut` maps, not
leftover-character of c10bit3, not leftover-character of #6539, and not
leftover-character of #6518.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the 32 `F_cut` maps scored on one seed | no physical law selection |
| per block | the `cov12>0`–displayed-`Q` identities on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule,
a selector outside the displayed three, and any independently derived
physical map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** c10bit3 already recorded that `Q10=cov10>0`, #6539 already
named `Q8=cov8>0`, and #6518 already named `Q4=cov4>0`, so one of those
must also be twelve-site positivity.

**Answer:** none of them is. `N_pos = 32`, `N_Q10 = 28`, `N_Q8 = 30`,
and `N_Q4 = 24`. The lex-first miss of each is `(0, 0, 0, 0, 0)`. New
k=12. Do not adopt a bit.

### N8 — cross-cycle echo

Investment c10bit3 already showed `Q10=cov10>0` only. Investment #6539
already showed `Q8=cov8>0`. Investment #6518 already showed `Q4=cov4>0`.
Echoing any of those facts is not a substitute for testing `cov12>0`
against the three displayed predicates on all 32. New k=12.

No-Go Discipline disposition: **PASS** for the finite 32-map census
and the three displayed failed identities. FAIL / DO NOT SHIP for
“adopt a bit,” “`Q10` is the physical rule,” or “write `Q10` into
Admissibility.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov12` on
the one twelve-site seed, decides whether `cov12>0` if and only if
`Q10`, if and only if `Q8`, or if and only if `Q4`, reports one
lex-first miss of each failure, and reports `N_pos` and, for each
displayed `Q`, `N_Q` and `N_both`. Declared audit inputs are this note
and the axiom memo; the runner writes no cache and authors no audit
verdict.

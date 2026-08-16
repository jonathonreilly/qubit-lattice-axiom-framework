---
claim_id: f_cut_qstar_nontot_cov2_split_refuse_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the first remaining-bit refuse of F_cut (1,0,1,0,0) from S={(0,0,0),(2,0,0)} is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_qstar_nontot_cov2_split_refuse_2026_08_15.py
---

# First Remaining-Bit Refuse Of Non-Total `Q_*` Map `(1,0,1,0,0)` From The Split Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock evolution of one named cube-covariant cut
map on the twelve-vertex two-cube with off-patch occupancy `0`, started from
the declared two-site seed `S={(0,0,0),(2,0,0)}`, reporting the first
remaining-bit refuse and the refuse count on that first tick.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_qstar_nontot_cov2_split_refuse_2026_08_15.py`](../scripts/f_cut_qstar_nontot_cov2_split_refuse_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

The non-total `Q_*` pair that differs only by `opp2` at `mixed3=0` is

```text
f_lo = (1, 0, 1, 0, 0)   # cov2=32
f_hi = (1, 1, 1, 0, 0)   # cov2=36
```

The lex-first two-site seed that `f_hi` fills and `f_lo` misses is
`S={(0,0,0),(2,0,0)}`. That names a seed. It does not name the first
remaining-bit refuse on the miss run.

This note stays on that seed and scores the refuse mechanism of the
32-versus-36 split.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That tuple lies in `Q_*` and has
`vertex3=1`; it is a control, not a scored non-total map.

On the two-cube with off-patch occupancy `0`, write `cov2(f)` for the number
of two-site seeds from which `f` fills. There are `C(12,2)=66` two-site
seeds. Totality means `cov2(f)=66`. Both maps below fail totality.

Sites of the two-cube, in lexicographic order:

`(0,0,0)`, `(0,0,1)`, `(0,1,0)`, `(0,1,1)`,
`(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`,
`(2,0,0)`, `(2,0,1)`, `(2,1,0)`, `(2,1,1)`.

**Theorem 1.** The first remaining-bit refuse of `f_lo` from `S` is tick
`1`, site `(1,0,0)`, type `opp2`.

**Theorem 2.** On that first tick, `N_refuse = 1`.

**Theorem 3.** Display. Do not adopt a bit.

Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The named non-total Q_* map (1,0,1,0,0) is evolved exactly from S={(0,0,0),(2,0,0)} on the twelve-vertex two-cube. The first remaining-bit refuse, its type, and N_refuse on that tick are finite exact counts. Not a physical Admissibility selector."
trace_class: frontier_discovery
target_claim_id: f_cut_qstar_nontot_cov2_split_refuse
target_blocker_text: "first remaining-bit refuse of F_cut (1,0,1,0,0) from S={(0,0,0),(2,0,0)}"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded non-tot Q_* split-seed refuse; do not adopt a bit"
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

Admissibility is not a dynamics axiom.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no formation-site selector and no occupancy-to-lock
predicate. The refuse, the seed, and the `opp2` bit below are displayed
remaining-bit data, not axiom content.

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

A neighborhood is a remaining-bit neighborhood when its axis type is one of
the five remaining types or a complement partner of one of them. Empty and
full are not remaining bits. The first remaining-bit refuse on a run is the
first remaining-bit neighborhood, in tick order and then two-cube lex order
of sites, at which `f` returns 0. `N_refuse` on a tick is the number of
unlocked sites whose neighborhood on that tick is a remaining-bit type and
is scored 0.

`Q_*` is the remaining-bit predicate `wt1=1` and `adj2=1`. It holds on
exactly eight of the 32 maps. Non-total `Q_*` here means the four of those
eight with `vertex3=0`. The scored map is `f_lo` with remaining bits
`(1,0,1,0,0)`. The contrast map `f_hi=(1,1,1,0,0)` is displayed only.

`f_lo` fires on axis types with remaining bits `(1,0,1,0,0)`: `wt1` and
`adj2` and their complements, and not on `opp2`, `vertex3`, or `mixed3`.
`f_hi` is the same except `opp2=1`.

The declared seed is `S={(0,0,0),(2,0,0)}`, the two `x`-ends of the line
`y=z=0`.

## Theorem 1 — first remaining-bit refuse: tick, site, type

`f_lo` is the `F_cut` map with remaining-bit tuple `(1, 0, 1, 0, 0)`.
Direct evolution from `S` does not fill. The lock history is
`(2, 6, 8)` and the run halts at the eight-site set

```text
{(0,0,0), (0,0,1), (0,1,0), (0,1,1), (2,0,0), (2,0,1), (2,1,0), (2,1,1)}.
```

The four unlocked sites are the middle slice `x=1`.

Tick 1 accepts four `wt1` neighborhoods, at `(0,0,1)`, `(0,1,0)`,
`(2,0,1)`, and `(2,1,0)`. It refuses five empty neighborhoods. Empty is
not a remaining bit.

The same tick refuses one remaining-bit neighborhood: site `(1,0,0)`,
neighborhood `(1, 1, 0, 0, 0, 0)`, axis type `(0, 1, 2) = opp2`.

That is the first remaining-bit refuse: tick `1`, site `(1,0,0)`, type
`opp2`. No `adj2`, `vertex3`, or `mixed3` neighborhood appears before
that refuse.

The contrast map `f_hi` accepts that same `opp2` neighborhood at tick 1
and has lock history `(2, 7, 9, 10, 12)` from `S`. Displayed, not adopted.

## Theorem 2 — `N_refuse` on that first tick

On tick 1 of the `f_lo` run from `S`, exactly one remaining-bit
neighborhood is refused. So `N_refuse = 1` on the first refuse tick.

That single refuse is the middle site `(1,0,0)` seeing both `x`-ends of
`S` occupied and every other neighbor unoccupied. The occupancy
`(1,1,0,0,0,0)` is axis type `opp2`. Because `f_lo` has `opp2=0`, the
site stays unlocked. Because `f_hi` has `opp2=1`, the same site locks.
That one-site tick-1 contrast is the mechanism of the 32-versus-36
coverage split: the four long-`x` opposite pairs are exactly the two-site
seeds whose first remaining-bit step is this `opp2` middle.

Later ticks continue to refuse `opp2` on the middle slice and accept
`adj2` on the two `x`-faces; the run still cannot fill. Those later
refuses are not the first refuse and are not `N_refuse` on tick 1.

## Theorem 3 — display, not adoption

The first refuse is an `opp2` neighborhood, and `f_lo` has `opp2=0`.
That is the refuse mechanism of the 32-versus-36 split on this seed.

Display. Do not adopt a bit. Do not adopt `opp2`. Do not adopt `Q_*`.
Do not adopt `f_L1`. Do not adopt this seed. Do not write `opp2` or a
seed into Admissibility. Admissibility does not name this remaining-bit
formula and is not a dynamics axiom.

The refuse is a finite fact about occupancy-to-lock on this two-cube with
off-patch `o=0`. It is not a physical formation-site selector and not an
axiom edit.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `Q_*` as `wt1=1` and `adj2=1` | scored map lies in it |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, seed `S`, off-patch `o=0` | declared finite patch |
| first remaining-bit refuse of `f_lo` from `S` | tick `1`, site `(1,0,0)`, type `opp2` |
| `N_refuse` on that first tick | `1` |
| leftover of naming the split seed | refused; that named a seed, not a refuse |
| leftover of the tot2q coverage table | refused; that named scores, not a refuse |
| adoption of a bit | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of the 32-versus-36 scores: those integers name
coverages. Not leftover-character of naming `S`: that pair is the seed.
The present object is the first remaining-bit refuse of `f_lo` from `S`,
together with `N_refuse` on that tick.

Off-patch occupancy `0` is an explicit default on this patch. A
blank-block is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers which remaining-bit neighborhood `f_lo` first refuses from `S`. |
| V2 | Current main has the axiom memo and the `32`/`36` scores, but no landed first remaining-bit refuse of `(1,0,1,0,0)` from `S`. |
| V3 | The named map, the declared seed, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it names a declared finite refuse. |
| V5 | The refuse is displayed, not adopted, and is not written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: a named split seed is not a refuse event,
and a displayed remaining-bit refuse inside non-tot `Q_*` is not axiom
content. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of tot2q | treat the refuse as already named by the `32`/`36` scores | **ATTEMPTED** |
| leftover of the split seed | treat naming `S` as already naming the refuse | **ATTEMPTED** |
| adopt the bit | write `opp2` or the refuse into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| empty as remaining-bit | count the tick-1 empty refuses as the first remaining-bit refuse | **ATTEMPTED** |

### N2 — wall independence

The Hamming contrast, the tot2q coverage table, the named split seed, and
the off-patch convention are distinct. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The two-cube, the seed `S`, off-patch occupancy `0`, occupancy-to-lock
ticks, two-cube lex site order, the `F_cut` remaining-bit order, the
`Q_*` cut `wt1=1` and `adj2=1`, and the scored tuple `(1,0,1,0,0)` are
declared. Unique selection of `f_L1` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one
covariant nearest-neighbor rule. The residual answered here is the first
remaining-bit refuse of `f_lo` from `S`, not leftover-character of the
`32`/`36` scores and not leftover-character of naming the seed.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | `f_lo` evolved from `S`; contrast `f_hi` displayed | no physical law selection |
| per block | first remaining-bit refuse and `N_refuse` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include the `mixed3=1` pair in the same four-map slice, a
different seed, a different off-patch rule, a selector outside `Q_*`,
and any independently derived physical map from `F_cut` into
Admissibility.

### N7 — hostile steelman

**Steelman:** the split seed already names the middle as `opp2`, so the
refuse is leftover and `opp2` may be written as the rule.

**Answer:** A seed is not a refuse event. The first remaining-bit refuse
of `f_lo` from `S` is tick `1`, site `(1,0,0)`, type `opp2`, and
`N_refuse=1` on that tick. That triple is displayed data. Admissibility
does not name `opp2` or this refuse. Do not adopt a bit.

### N8 — cross-cycle echo

The tot2q census already showed that these two maps have `cov2` in
`{32,36}`, and the first-split census already named `S`. Echoing those
facts is not a substitute for naming the first remaining-bit refuse on
the miss run.

No-Go Discipline disposition: **PASS** for the finite split-seed refuse
and the displayed `opp2` contrast. FAIL / DO NOT SHIP for “adopt a
bit,” “write this refuse into Admissibility,” or “the seed already is
the refuse.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, restricts to the
remaining-bit tuple `(1,0,1,0,0)`, evolves occupancy-to-lock from
`S={(0,0,0),(2,0,0)}`, and reports the first remaining-bit refuse as
tick `1`, site `(1,0,0)`, type `opp2`, with `N_refuse=1` on that tick.
The contrast map `(1,1,1,0,0)` is displayed, not adopted. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.

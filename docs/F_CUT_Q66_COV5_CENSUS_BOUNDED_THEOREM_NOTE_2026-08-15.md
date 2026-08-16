---
claim_id: f_cut_q66_cov5_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the 5-site coverages of F_cut (1,1,1,1,0) and (1,1,1,1,1) are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_q66_cov5_census_2026_08_15.py
---

# Five-Site Coverage Of The Two `#6548` Totality Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock 5-site coverage of the two cube-covariant
cut maps `F_cut` with remaining-bit tuples `(1, 1, 1, 1, 0)` and
`(1, 1, 1, 1, 1)`, on the twelve-vertex two-cube, over all 792 unordered
five-site seeds, with off-patch occupancy `0`. Those two maps are the
`#6548` tot pair (`Q66` and `cov2=66`). The pair of coverages is
displayed. Neither map is adopted as the physical Admissibility rule.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_q66_cov5_census_2026_08_15.py`](../scripts/f_cut_q66_cov5_census_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6548 showed that the remaining-bit predicate
`Q66(f) := (wt1=1) and (adj2=1) and (opp2=1) and (vertex3=1)` is
equivalent to `cov2=66` among the 32 maps. The two maps that satisfy
`Q66` are

```text
f0 = (1, 1, 1, 1, 0)
f1 = (1, 1, 1, 1, 1)
```

in remaining-bit order `(wt1, opp2, adj2, vertex3, mixed3)`. Mixed3 is
free in `Q66`. Companion scores already exist at `k=6` and `k=8`. This
note scores a new seed cardinality: five-site seeds. New k for the 2-site
tot pair, not leftover-character of #6548, not leftover-character of the
k=6 and k=8 scores, and not a Max(5) rename.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`. That map is a control, not a
scored tot pair member.

On the two-cube with off-patch occupancy `0`, write
`cov5(f) = |{S : |S|=5 and f fills from S}|`. Then:

- Theorem 1. `cov5(f0) = 752` and `cov5(f1) = 792`.
- Theorem 2. The two scores are not both `792`. The difference is
  `cov5(f1) − cov5(f0) = 40`. The map `f1` attains the five-site ceiling
  `m5=792`; the map `f0` misses forty seeds.
- Theorem 3. The pair is displayed. Displayed, not adopted.

Do not adopt a map. Do not write `f0` or `f1` into Admissibility. The
2-site tot pair is not a 5-site tot pair: only `f1` fills every five-site
seed.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two Q66 maps are scored exactly on the 792 five-site seeds of the two-cube. The pair cov5(f0)=752, cov5(f1)=792 and the difference 40 are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_q66_cov5_census
target_blocker_text: "cov5 of the two Q66 maps and whether both equal 792"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded 5-site tot-pair census; do not adopt a displayed map"
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
predicate. The pair `(f0, f1)` is a displayed remaining-bit pair, not
axiom content.

## Exact objects

The two-cube is `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices). Off-patch
occupancy `0` is the explicit default: a neighbor of a site in `T` that is
not itself in `T` is treated as unoccupied. A blank-block is a different rule and is not used.

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

The five-site seeds are the `C(12,5) = 792` subsets of size 5 in `T`. Then
`cov5(f)` is the number of those subsets from which `f` fills. The
comparison ceiling `m5=792` is that seed count: a map attains `m5`
exactly when it fills every five-site seed. Do not list the seeds.

The displayed remaining-bit predicate that names the pair is

```text
Q66(f) := (wt1 = 1) and (adj2 = 1) and (opp2 = 1) and (vertex3 = 1).
```

Mixed3 is free in `Q66`. The two maps with `Q66` true are `f0` and `f1`.
Displayed, not adopted.

## Theorem 1 — `cov5(f0)` and `cov5(f1)`

Enumerate the 32 remaining-bit tuples of `F_cut`, isolate the two `Q66`
maps, and score `cov5` on the 792 five-site seeds. Then

```text
cov5(f0) = 752
cov5(f1) = 792
```

with `f0 = (1, 1, 1, 1, 0)` and `f1 = (1, 1, 1, 1, 1)`. Both maps lie in
`F_cut`. The control `f_L1 = (1, 0, 1, 1, 1)` is not a `Q66` map and is
not scored as part of the tot pair.

## Theorem 2 — not both `792`; the difference is `40`

Because `cov5(f0) = 752 < 792` and `cov5(f1) = 792`, the two scores are
not both equal to `792`. The difference is

```text
cov5(f1) − cov5(f0) = 40.
```

So `f1` attains `m5=792` and `f0` misses forty of the 792 five-site
seeds. The `#6548` tot pair is not jointly 5-site total.

## Theorem 3 — display; do not adopt a map

The pair

```text
(cov5(f0), cov5(f1)) = (752, 792)
```

is displayed. Displayed, not adopted. Do not adopt a map. Do not write
`f0` or `f1` into Admissibility.

`f_L1`, with remaining bits `(1, 0, 1, 1, 1)`, has `cov5 = 792`. That
control is consistent with Theorem 1 and does not restore joint
attainment of `m5` by the tot pair.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 792 five-site seeds, off-patch `o=0` | declared finite patch |
| `Q66` as `wt1=adj2=opp2=vertex3=1` | displayed name of the pair, not adopted |
| `cov5(f0)=752`, `cov5(f1)=792` | proved by exhaustive scoring |
| both equal `792` | fails; difference `40` |
| leftover-character of #6548 or of k=6 and k=8 | refused; new k for the 2-site tot pair |
| adoption of a map | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of #6548: that closed `cov2=66` iff `Q66` on
two-site seeds. Not leftover-character of the k=6 and k=8 scores: those
are different seed families. The present count is `cov5` on 792 five-site
seeds, a different seed family. New k for the 2-site tot pair.

The note is not a Max(5) ranking and not a seed-table: maximizers of
`cov5` among the 32 maps are not selected, and no seed census of a named
map is compiled.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not write `f0` or `f1` into Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the 5-site coverages of the two `#6548` tot maps on this patch. |
| V2 | Current main has the axiom memo and the `#6548` fact that `cov2=66` is `Q66`, but no landed 5-site score of that pair. |
| V3 | The two maps, 792 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite pair at a new seed cardinality. |
| V5 | Joint 5-site totality fails, and neither displayed map is adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: the two `Q66` maps do not both attain
`cov5=792` on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of #6548 or of k=6 and k=8 | treat the 5-site pair as leftover-character of those scores | **ATTEMPTED** |
| Max(5) rename | replace the tot-pair census by a 5-site maximizer ranking | **ATTEMPTED** |
| both equal 792 | assert `cov5(f0)=cov5(f1)=792` | **ATTEMPTED** |
| adopt a map | write `f0` or `f1` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The pair of scores, the Hamming contrast, the `#6548` two-site identity,
the k=6 and k=8 scores, and the off-patch convention are distinct. This
note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 792 five-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and the displayed
pair `f0`, `f1` are declared. Joint 5-site totality is not silently
assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the 5-site coverage of
the two `#6548` tot maps on the declared patch, not leftover-character of
#6548, not leftover-character of the k=6 and k=8 scores, and not a Max(5)
ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | the two `Q66` maps scored on 792 seeds | no physical law selection |
| per block | pair `(752, 792)` and difference `40` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than the displayed pair, and any independently derived physical
map from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** #6548 already showed that these two maps fill every two-site
seed, and the k=6 and k=8 scores already treated later cardinalities, so
every later `k` inherits joint totality or is leftover-character of those
scores.

**Answer:** Inheritance fails at `k=5`. The map `f1` still fills every
five-site seed, but `f0` fills only `752` of `792`. The difference is
`40`. Five-site seeds are a different family from two-site, six-site, and
eight-site seeds. Displayed maps are not adopted.

### N8 — cross-cycle echo

Investment #6548 already showed that `cov2=66` is `Q66`. The k=6 and k=8
scores already treated other seed families. Echoing those facts is not a
substitute for the five-site count: `k=5` is a new seed family, and the
pair `(752, 792)` with difference `40` is a five-site fact.

No-Go Discipline disposition: **PASS** for the finite pair and the
narrow failure of joint 5-site totality. FAIL / DO NOT SHIP for
“both `Q66` maps have `cov5=792`” or “a displayed map is the physical
rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, isolates the two
`Q66` remaining-bit tuples `f0=(1,1,1,1,0)` and `f1=(1,1,1,1,1)`, scores
`cov5` on the 792 five-site seeds, reports `cov5(f0) = 752` and
`cov5(f1) = 792`, reports that the scores are not both `792`, and reports
the difference `40`. Declared audit inputs are this note and the axiom
memo; the runner writes no cache and authors no audit verdict.

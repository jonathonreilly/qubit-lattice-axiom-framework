---
claim_id: f_cut_k4_v30_mixed3_split_seed_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0 and seed {(0,0,0),(0,0,1),(2,0,0)}, the F_cut maps (1,1,1,0,0) and (1,1,1,0,1) do not have the same lock history. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_v30_mixed3_split_seed_2026_08_15.py
---

# Mix0/L1 Splitter Seed Distinguishes The Vertex3=0 k=4 Pair

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock histories of the two `vertex3=0` k=4 maps
`(1,1,1,0,0)` and `(1,1,1,0,1)` on the twelve-vertex two-cube with off-patch
occupancy `0`, from the displayed seed
`S={(0,0,0),(0,0,1),(2,0,0)}`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_v30_mixed3_split_seed_2026_08_15.py`](../scripts/f_cut_k4_v30_mixed3_split_seed_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6449: the maps `(1,1,1,0,0)` and `(1,1,1,0,1)` agree on the
1-site seed `(0,0,0)` with lock history `(1,4,8,10,11,12)`. Investment
#6437: the three-site seed `S={(0,0,0),(0,0,1),(2,0,0)}` splits the
`mix0`/`L1` pair (remaining bits `(1,0,1,1,0)` versus `(1,0,1,1,1)`). This
note asks whether that same `S` splits the `vertex3=0` k=4 pair.
New uniqueness, not leftover of #6449 (that seed agreed) or #6437
(different maps).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.
The map `f_mix0` is the remaining-bit tuple `(1, 0, 1, 1, 0)`.

Write `f00` for remaining bits `(1,1,1,0,0)` and `f01` for `(1,1,1,0,1)`.
Independent occupancy-to-lock runs, off-patch occupancy `0`:

- Theorem 1. Both maps fill from `{(0,0,0)}` with history
  `(1, 4, 8, 10, 11, 12)`. The same `S` splits `mix0`/`L1`: `f_L1` fills
  with `(3, 8, 11, 12)` and `f_mix0` halts unfilled at `(3, 8, 10)`.
- Theorem 2. From `S`, `f00` fills with history `(3, 9, 11, 12)` and
  `f01` fills with history `(3, 9, 12)`.
- Theorem 3. The two histories differ. The displayed equality bit is `0`.
  This is not a `|S|` census. Do not adopt `mixed3`.

On this seed the pair is dynamically distinct even though both fill.
Displayed, not adopted.

Do not write `mixed3` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Independent occupancy-to-lock runs of two named F_cut maps from one displayed seed yield exact lock histories. The equality bit is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_k4_v30_mixed3_split_seed
target_blocker_text: "whether the mix0/L1 splitter seed S splits the vertex3=0 k=4 pair"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed history inequality; do not adopt mixed3"
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
- the one-site seed `{(0,0,0)}` and the three-site seed
  `S={(0,0,0),(0,0,1),(2,0,0)}`;
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** On the two-cube with off-patch occupancy `0`, decide whether
`f00` and `f01` have the same lock history from the displayed seed `S`.

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
entries 0) equals 1. The lock history is the nondecreasing sequence of
`|L|` after each nonempty wave, starting from the seed cardinality. The map
`f` fills from a seed if iterating this rule from `L_0` reaches `L = T` in
at most 13 ticks. Runs of distinct maps are independent: each starts from
the same seed and never shares an intermediate locked set.

The equality bit is `1` if the two histories are identical as tuples and
`0` otherwise. It is not a count of seeds.

## Theorems

### Theorem 1 — 1-site agreement and the `mix0`/`L1` split on `S`

`f00` and `f01` are the `F_cut` maps with remaining-bit tuples
`(1, 1, 1, 0, 0)` and `(1, 1, 1, 0, 1)`. Direct evolution from
`{(0,0,0)}` reaches all twelve vertices for both maps, with the same lock
history `(1, 4, 8, 10, 11, 12)`.

`f_L1` is the unbalanced-axis predicate. This is **not** Hamming parity.
Its remaining bits are `(1, 0, 1, 1, 1)`. The map `f_mix0` is
`(1, 0, 1, 1, 0)`. From `S`, `f_L1` fills with history `(3, 8, 11, 12)`
and `f_mix0` halts unfilled with history `(3, 8, 10)`. So `S` splits
`mix0`/`L1`.

### Theorem 2 — lock histories of the pair from `S`

Independent runs from `S`:

```text
f00 = (1, 1, 1, 0, 0): history (3, 9, 11, 12), fills
f01 = (1, 1, 1, 0, 1): history (3, 9, 12), fills
```

Both maps fill. The histories are not the same tuple.

### Theorem 3 — equality bit `0`; do not adopt `mixed3`

The displayed equality bit is `0`. The two maps do not have the same lock
history on this seed. This is not a `|S|` census: no other seed is scored,
and no count of splitting seeds is reported.

The second-wave neighborhood of `(1,1,0)` on the `f00`/`f01` runs is the
`mixed3` orbit. The map `f01` fires that orbit and locks the last three
sites in one wave; `f00` refuses it and locks `(1,1,0)` one tick later as
`adj4`. That mechanism is displayed only. Do not adopt `mixed3`. Do not
write `mixed3` into Admissibility. `f_L1` remains the unbalanced-axis
predicate `n≠0` rather than Hamming parity.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` remaining bits of `f00` and `f01` | enumerated |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, seed `S`, off-patch 0 | declared finite patch |
| 1-site histories agree at `(1, 4, 8, 10, 11, 12)` | proved by evolution |
| `S` splits `mix0`/`L1` | proved by evolution |
| `S`-histories of `f00` and `f01` | proved by independent runs |
| equality bit | `0`; displayed, not adopted |
| leftover-character of #6449 or #6437 | refused; new uniqueness |
| physical Admissibility selector | open |

## Current premise boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility identifies the six-neighbor condition domain and covariance
under proper cubic rotations; it does not supply the formation site, probability, or rate.
The boolean occupancy predicates and the lock-update rule are explicit
bounded mathematical input, not axiom text.

The current Record boundary is:

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Permanence of a lock once formed is used only as the declared update rule on
this finite patch. No physical readout, content map, or formation rate is
identified.

## Boundary and imports

Not leftover-character of #6449: that displayed 1-site agreement of this
pair from `(0,0,0)`. The present object is the pair of lock histories from
a different seed.

Not leftover-character of #6437: that displayed a split of the different
maps `f_mix0` and `f_L1` on this seed. The present object is the same seed
on the `vertex3=0` k=4 pair.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write `mixed3` into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the mix0/L1 splitter seed `S` splits the `vertex3=0` k=4 pair. |
| V2 | Current main has the 1-site agreement (#6449) and the mix0/L1 split on `S` (#6437), but no landed history comparison of this pair on `S`. |
| V3 | The two maps, one seed, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it separates fill-agreement from history-agreement. |
| V5 | It is not a physical selector: the equality bit is displayed, and `mixed3` is not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch and pair, the lock histories
from `S` are unequal. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover #6449 | treat the `S`-histories as leftover-character of the 1-site agreement | **ATTEMPTED** |
| leftover #6437 | treat this pair as leftover-character of the mix0/L1 split | **ATTEMPTED** |
| adopt `mixed3` | write the bit into Admissibility | **ATTEMPTED** |
| `|S|` census | replace the equality bit by a count of splitting seeds | **ATTEMPTED** |
| lattice-wide formation | lift the patch histories to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The history-inequality extra, the Hamming contrast, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the seed `S`, off-patch occupancy `0`, occupancy-to-lock
ticks, independent runs, and the `F_cut` remaining-bit order are declared.
Equality of the two `S`-histories is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the history comparison
of this pair on `S`, not leftover-character of #6449 or #6437.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | independent runs of the two maps from `(0,0,0)` and from `S` | no physical law selection |
| per block | equality bit of the two lock histories on this seed | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed, a different off-patch rule, a selector
other than this equality bit, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Because the pair agrees from `(0,0,0)` and both maps fill from
`S`, they are dynamically the same on every displayed seed, so `mixed3` is
free.

**Answer:** Fill-agreement is not history-agreement. From `S` both maps fill,
but the histories are `(3, 9, 11, 12)` and `(3, 9, 12)`. The equality bit is
`0`. That is a new uniqueness on this pair, not a leftover of the 1-site
agreement.

### N8 — cross-cycle echo

Investment #6449 already displayed the 1-site agreement. Investment #6437
already displayed a split of different maps on `S`. Echoing either is not a
substitute for the pair of independent `S`-histories of this pair.

No-Go Discipline disposition: **PASS** for the finite history inequality and
the displayed equality bit. FAIL / DO NOT SHIP for “`mixed3` is selected by
this seed” or “`mixed3` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner reconfirms the 1-site agreement
`(1, 4, 8, 10, 11, 12)`, reconfirms that `S` splits `mix0`/`L1`, runs each
of `f00` and `f01` independently from `S`, reports both histories and both
fill bits, and checks that the displayed equality bit is `0`. Declared audit
inputs are this note and the axiom memo; the runner writes no cache and
authors no audit verdict.

---
claim_id: f_cut_k4_v30_mixed3_split_neighborhood_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0 and seed {(0,0,0),(0,0,1),(2,0,0)}, the first neighborhood at which F_cut (1,1,1,0,0) and (1,1,1,0,1) disagree is reported by tick, site, and axis type. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_k4_v30_mixed3_split_neighborhood_2026_08_15.py
---

# First Neighborhood Where The Vertex3=0 k=4 Pair Disagrees From The Displayed Seed

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** displayed occupancy-to-lock dynamics of the two `vertex3=0`
k=4 maps `(1,1,1,0,0)` and `(1,1,1,0,1)` on the twelve-vertex two-cube
`{0,1,2}×{0,1}×{0,1}`, started from the displayed seed
`S={(0,0,0),(0,0,1),(2,0,0)}`, with off-patch occupancy identically `0`.
The first disagreeing neighborhood is displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_k4_v30_mixed3_split_neighborhood_2026_08_15.py`](../scripts/f_cut_k4_v30_mixed3_split_neighborhood_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6452: on `S={(0,0,0),(0,0,1),(2,0,0)}`, the map
`(1,1,1,0,0)` has lock history `(3,9,11,12)` and `(1,1,1,0,1)` has
`(3,9,12)`. The mechanism is unnamed. This note reports the first
`(t, x, axis-type)` at which the two predicates differ.
New object, not leftover of #6452 (histories only) or #6441
(different pair).

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

Write `f00` for remaining bits `(1,1,1,0,0)` and `f01` for `(1,1,1,0,1)`.
Independent occupancy-to-lock runs, off-patch occupancy `0`:

- Theorem 1. From `S`, `f00` fills with history `(3, 9, 11, 12)` and
  `f01` fills with history `(3, 9, 12)`.
- Theorem 2. The first tick and unlocked site at which the two
  predicates differ, on either run's locked set, is `t=2`,
  `x=(1, 1, 0)`, axis type `(1, 1, 1)`, with `f00=0` and `f01=1`.
- Theorem 3. That neighborhood stencil is the six-tuple
  `(1, 1, 0, 1, 0, 0)` in order `(+x,-x,+y,-y,+z,-z)`. Mixed3 is
  displayed only. Do not adopt mixed3.

On this seed the pair first disagrees on a `mixed3` neighborhood at
`(1, 1, 0)`. Displayed, not adopted.

Do not write mixed3 into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Independent occupancy-to-lock runs of two named F_cut maps from one displayed seed yield a first disagreeing neighborhood by tick, site, and axis type. Displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_k4_v30_mixed3_split_neighborhood
target_blocker_text: "first neighborhood at which F_cut (1,1,1,0,0) and (1,1,1,0,1) disagree from S={(0,0,0),(0,0,1),(2,0,0)}"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the displayed first neighborhood; do not adopt mixed3"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "no edit"
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
- the three-site seed `S={(0,0,0),(0,0,1),(2,0,0)}`;
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

**Target.** On the two-cube with off-patch occupancy `0`, report the first
neighborhood at which `f00` and `f01` disagree from the displayed seed
`S`, by tick, site, and axis type.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0. Complement
swaps `n_both` with `n_empty`. The five remaining bits of `F_cut`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on orbit types
`(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`. Complement partners
are forced equal; empty and full are fixed at 0.

Sites of the two-cube, in lexicographic order:

`(0,0,0)`, `(0,0,1)`, `(0,1,0)`, `(0,1,1)`,
`(1,0,0)`, `(1,0,1)`, `(1,1,0)`, `(1,1,1)`,
`(2,0,0)`, `(2,0,1)`, `(2,1,0)`, `(2,1,1)`.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The lock history is the nondecreasing sequence of
`|L|` after each nonempty wave, starting from the seed cardinality. The map
`f` fills from a seed if iterating this rule from `L_0` reaches `L = T` in
at most 13 ticks. Runs of distinct maps are independent: each starts from
the same seed and never shares an intermediate locked set.

The first disagreeing neighborhood is the lexicographically first unlocked
site, at the earliest tick, whose two predicate values differ when both
are evaluated against that run's locked set.

## Theorems

### Theorem 1 — reconfirm the two histories

`f00` and `f01` are the `F_cut` maps with remaining-bit tuples
`(1, 1, 1, 0, 0)` and `(1, 1, 1, 0, 1)`. Direct independent evolution
from `S={(0,0,0),(0,0,1),(2,0,0)}`:

```text
f00 = (1, 1, 1, 0, 0): history (3, 9, 11, 12), fills
f01 = (1, 1, 1, 0, 1): history (3, 9, 12), fills
```

Both maps fill. The histories are not the same tuple. This reconfirms
#6452. It does not yet name the neighborhood at which the predicates
first differ.

`f_L1` is the unbalanced-axis predicate. This is **not** Hamming parity.
Its remaining bits are `(1, 0, 1, 1, 1)`.

### Theorem 2 — first disagreeing tick, site, and axis type

At tick `1` the locked set of each run is still `S`. The six sites

`(0,1,0)`, `(0,1,1)`, `(1,0,0)`, `(1,0,1)`, `(2,0,1)`, `(2,1,0)`

are ready under both predicates. In particular `(1,0,0)` sees type
`opp2=(0,1,2)` with stencil `(1, 1, 0, 0, 0, 0)`; both predicates
return `1` because `opp2=1` on this pair. The remaining three sites
are not ready. No unlocked site disagrees.

After tick `1` one has `|locks_1|=9` on both runs. At tick `2` the
three unlocked sites split:

- `(1,1,1)` and `(2,1,1)` see type `adj2=(2,0,1)`. Both predicates
  return `1`.
- `(1, 1, 0)` sees type `mixed3=(1, 1, 1)`. Then `f00=0` and `f01=1`.

The lexicographically first (and only) such site is `x=(1, 1, 0)`.
That is the first disagreeing neighborhood: tick `t=2`, site
`(1, 1, 0)`, axis type `(1, 1, 1)`, predicate values `f00=0` and
`f01=1`. The same `(t,x,type)` is obtained on the `f00` run and on
the `f01` run, because the locked sets still coincide at the
evaluation of tick `2`.

Therefore `f01` locks all three remaining sites at tick `2` and
fills. `f00` locks only the two `adj2` sites, reaching eleven locks,
and then locks `(1,1,0)` one tick later.

### Theorem 3 — display the stencil; do not adopt mixed3

At `x=(1, 1, 0)` and the shared nine-site locked set of tick `2`, the
six-neighbor tuple in order `(+x,-x,+y,-y,+z,-z)` is

`(1, 1, 0, 1, 0, 0)`.

That is: `(2,1,0)` and `(0,1,0)` occupied, `(1,2,0)` off-patch empty,
`(1,0,0)` occupied, `(1,1,1)` unlocked empty, and `(1,1,-1)`
off-patch empty. The axis type is `(1, 1, 1)`. This is the displayed
disagreeing stencil.

Do not adopt mixed3. Do not adopt `f00`. Do not adopt `f01`.
Do not write mixed3 into Admissibility. Admissibility is not a
dynamics axiom and does not supply this predicate or this
neighborhood. The stencil is not written into Admissibility.

The executed split is the `mixed3` orbit at `(1,1,0)`. Mixed3 is a
predicate-level distinction that this seed executes; it is displayed,
not adopted.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` remaining bits of `f00` and `f01` | enumerated |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, seed `S`, off-patch 0 | declared finite patch |
| `S`-histories of `f00` and `f01` | reconfirmed `(3, 9, 11, 12)` and `(3, 9, 12)` |
| first disagreeing `(t,x,axis-type)` | `t=2`, `(1, 1, 0)`, `(1, 1, 1)` |
| first disagreeing stencil | `(1, 1, 0, 1, 0, 0)` |
| leftover-character of #6452 or #6441 | refused; new object |
| physical Admissibility selector | open |

## Current premise boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Admissibility is not a dynamics axiom.

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
identified. no axiom or approved primitive is added.

## Boundary and imports

Not leftover-character of #6452: that displayed the two lock histories
from `S` (histories only). The present object is the first neighborhood
at which the predicates differ.

Not leftover-character of #6441: that was a different pair. The present
object is this `vertex3=0` k=4 pair on `S`.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write mixed3 into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first neighborhood, by tick, site, and axis type, at which `f00` and `f01` disagree from `S`. |
| V2 | Current main has the axiom memo and no landed first-disagreeing-neighborhood census of this pair from this seed. |
| V3 | The twelve-vertex two-run process is independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it separates history-inequality from the first executed stencil. |
| V5 | It is not a physical selector: the neighborhood is displayed, and mixed3 is not adopted. |

## No-Go Discipline gate

The negative content is narrow: a first disagreeing neighborhood is
not a selector, and a displayed stencil is not axiom content.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover #6452 | treat the first neighborhood as leftover-character of the histories | **ATTEMPTED** |
| leftover #6441 | treat this pair as leftover-character of a different pair | **ATTEMPTED** |
| adopt mixed3 | write the bit into Admissibility | **ATTEMPTED** |
| history equality | replace the neighborhood by a `|S|` census | **ATTEMPTED** |
| lattice-wide formation | lift the patch neighborhood to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The neighborhood extra, the Hamming contrast, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the seed `S`, off-patch occupancy `0`, occupancy-to-lock
ticks, independent runs, lexicographic site order, and the `F_cut`
remaining-bit order are declared. Equality of the two `S`-histories is
not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the first neighborhood
of this pair on `S`, not leftover-character of #6452 or #6441.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | independent runs of the two maps from `S` | no physical law selection |
| per block | first disagreeing neighborhood on this seed | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed, a different off-patch rule, a selector
other than this neighborhood, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Because #6452 already named the two histories, the first
disagreeing neighborhood is leftover character and may be treated as
a selector.

**Answer:** Naming the histories reports only that halt sequences
differ. The first executed neighborhood is a different object: tick
`2`, site `(1, 1, 0)`, type `(1, 1, 1)`, stencil
`(1, 1, 0, 1, 0, 0)`. Admissibility does not name either map, mixed3,
or this stencil. Do not adopt mixed3. Do not adopt a selector.

### N8 — cross-cycle echo

Investment #6452 already displayed the two lock histories. Investment
#6441 already displayed a different pair. Echoing either is not a
substitute for the first disagreeing neighborhood of this pair.

No-Go Discipline disposition: **PASS** for the finite first-neighborhood
statement and the displayed stencil. FAIL / DO NOT SHIP for “mixed3 is
selected by this seed” or “mixed3 is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner reconfirms the two `S`-histories
`(3, 9, 11, 12)` and `(3, 9, 12)`, runs each of `f00` and `f01`
independently from `S`, reports the first disagreeing tick, site, axis
type, and stencil, and checks that mixed3 is displayed rather than
adopted. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.

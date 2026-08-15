---
claim_id: f_cut_vertex3_shared_face_fill_equivalence_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, filling from the shared-face 1-site seed (1,0,0) is not equivalent to f(vertex3)=1. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_vertex3_shared_face_fill_equivalence_2026_08_15.py
---

# Shared-Face Seed Fill Is Not The Vertex3 Bit

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill from the shared-face 1-site seed
`(1,0,0)` on the twelve-vertex two-cube with off-patch occupancy `0`, scored
for all 32 cube-covariant cut maps `F_cut`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_vertex3_shared_face_fill_equivalence_2026_08_15.py`](../scripts/f_cut_vertex3_shared_face_fill_equivalence_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment #6448 showed that the two `vertex3=0` k=4 maps miss the
shared-face seed `(1,0,0)` and that the two `vertex3=1` k=4 maps fill all
twelve one-site seeds. That was a four-map table. This note asks the class
question among all 32 `F_cut` maps: is filling from `(1,0,0)` equivalent to
`f(vertex3)=1`? New selector, not leftover of #6448.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. The remaining-bit tuple of `f_L1` is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write `fill(f)` for the
boolean “`f` fills from the singleton `{(1,0,0)}`.” Then:

- Theorem 1. `f_L1` has `vertex3=1` and `fill(f_L1)=1`. The lock history
  is `(1, 5, 10, 12)`.
- Theorem 2. `fill(f)` if and only if `f(vertex3)=1` is false. The counts
  are `N_fill = 4`, `N_v3 = 16`, `N_both = 4`. The lex-first counterexample
  remaining-bit tuple is `(0, 0, 0, 1, 0)`: `f(vertex3)=1` and `fill=0`.
- Theorem 3. The failed equivalence and the counterexample are displayed.
  Do not adopt `vertex3`.

Fill implies `vertex3=1` (the four fillers all fire that bit), but the
converse fails on twelve maps. Filling from `(1,0,0)` detects the
conjunction `wt1=adj2=vertex3=1`, not the single bit `vertex3`.

Do not write `vertex3` into Admissibility. Displayed, not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the shared-face 1-site seed (1,0,0). N_fill, N_v3, and N_both are finite exact counts. The failed biconditional is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: f_cut_vertex3_shared_face_fill_equivalence
target_blocker_text: "whether fill-from-(1,0,0) is equivalent to f(vertex3)=1 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded failed equivalence; do not adopt vertex3"
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
- the shared-face 1-site seed `{(1,0,0)}`;
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

**Target.** Among the 32 members of `F_cut`, decide whether filling from
`{(1,0,0)}` is equivalent to `f(vertex3)=1`.

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

Write `N_fill` for the number of `F_cut` maps with `fill(f)=1`, `N_v3` for
the number with `f(vertex3)=1`, and `N_both` for the number with both.

## Theorems

### Theorem 1 — `f_L1` has `vertex3=1` and fills from `(1,0,0)`

`f_L1` is the `F_cut` map with remaining-bit tuple `(1, 0, 1, 1, 1)`.
Equivalently, `f_L1(c)=1` if and only if some axis is unbalanced. This is
**not** Hamming parity. In particular `f_L1(vertex3)=1`. Direct evolution
from `{(1,0,0)}` reaches all twelve vertices with lock history
`(1, 5, 10, 12)`.

### Theorem 2 — fill-from-`(1,0,0)` is not equivalent to `f(vertex3)=1`

Enumerate all 32 remaining-bit tuples. The pairs `(fill(f), f(vertex3))`
occupy only three bins:

- 16 maps with `f(vertex3)=0`, all of them `fill=0`;
- 12 maps with `f(vertex3)=1` and `fill=0`;
- 4 maps with `f(vertex3)=1` and `fill=1`.

Therefore

```text
N_fill = 4
N_v3 = 16
N_both = 4
```

and `N_fill = N_v3 = N_both` is false. Fill if and only if `f(vertex3)=1`
fails. The one-way implication “`fill` implies `vertex3=1`” holds; the
converse fails.

The lex-first counterexample remaining-bit tuple is
`(wt1, opp2, adj2, vertex3, mixed3) = (0, 0, 0, 1, 0)`. That map fires
`vertex3` and still has halt lock-count `1`: the first neighborhoods of
`(1,0,0)` are `wt1` or empty, so a silent `wt1` never grows.

The four maps with `fill=1` are

```text
(1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1).
```

So filling from `(1,0,0)` detects the conjunction `wt1=adj2=vertex3=1`,
not the single bit `vertex3`. The second of these four is `f_L1`.

### Theorem 3 — display; do not adopt `vertex3`

The failed equivalence, the three counts, and the counterexample tuple
`(0, 0, 0, 1, 0)` are displayed. They are not adopted. Do not adopt
`vertex3`. Do not write `vertex3` into Admissibility. `f_L1` remains the
unbalanced-axis predicate `n≠0` rather than Hamming parity.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice and Admissibility premises | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n_μ ≠ 0` | defined; Hamming rejected |
| two-cube, seed `(1,0,0)`, off-patch 0 | declared finite patch |
| `f_L1` has `vertex3=1` and fills | proved by remaining bits and evolution |
| `N_fill`, `N_v3`, `N_both` | proved by exhaustive census |
| fill iff `f(vertex3)=1` | fails; counterexample displayed |
| leftover-character of #6448 | refused; new 32-map selector |
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

Not leftover-character of #6448: that listed 1-site misses of the two
`vertex3=0` k=4 maps and 1-site totality of the two `vertex3=1` k=4 maps.
The present count is the biconditional among all 32 `F_cut` maps on one
shared-face seed.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No `Z^3`-wide formation law is claimed. Do not write `vertex3` into
Admissibility.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether the shared-face seed `(1,0,0)` detects the single remaining bit `vertex3` inside `F_cut`. |
| V2 | Current main has the k=4 four-map table (#6448) but no landed 32-map census of this seed versus `vertex3`. |
| V3 | The 32 maps, one seed, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility: it separates a one-way implication from a failed biconditional. |
| V5 | It is not a physical selector: the failed equivalence is displayed, and `vertex3` is not adopted. |

## No-Go Discipline gate

The negative content is narrow: on this patch and class, fill-from-`(1,0,0)`
does not characterize `f(vertex3)=1`. No global compiler impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover #6448 | treat the 32-map biconditional as leftover-character of the k=4 table | **ATTEMPTED** |
| `vertex3` alone | set `f(vertex3)=1` with `wt1=0` | **ATTEMPTED** |
| adopt `vertex3` | write the bit into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |
| lattice-wide formation | lift the patch count to a `Z^3` formation law | **ATTEMPTED** |

### N2 — wall independence

The failed biconditional extra, the Hamming contrast, and the off-patch
convention are distinct. This note claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the seed `(1,0,0)`, off-patch occupancy `0`, occupancy-to-lock
ticks, and the `F_cut` remaining-bit order are declared. Equivalence of fill
to `vertex3` is not silently assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is the 32-map comparison
of fill-from-`(1,0,0)` with `f(vertex3)`, not leftover-character of #6448.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on one seed | no physical law selection |
| per block | `N_fill`, `N_v3`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed, a different off-patch rule, a selector
other than this shared-face fill, and any independently derived physical map
from `F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** Because the two `vertex3=0` k=4 maps miss `(1,0,0)` and the
two `vertex3=1` k=4 maps fill every one-site seed, the shared-face seed
detects the `vertex3` bit among all of `F_cut`.

**Answer:** Silent `vertex3` does force `fill=0`, but firing `vertex3` is
not enough. Twelve maps with `vertex3=1` still miss `(1,0,0)`, including
the lex-first tuple `(0, 0, 0, 1, 0)`, which never leaves the seed because
the first neighborhoods are `wt1` or empty. The seed therefore detects a
three-bit conjunction, not the single bit.

### N8 — cross-cycle echo

Investment #6448 already listed the k=4 1-site misses. The present census
is a new selector: one seed versus one remaining bit, scored on all 32
maps. Echoing the four-map table is not a substitute for this count.

No-Go Discipline disposition: **PASS** for the finite failed equivalence and
the displayed counterexample. FAIL / DO NOT SHIP for “`vertex3` is selected
by the shared-face seed” or “`vertex3` is the physical rule.”

## Live parent quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores fill from
`{(1,0,0)}`, reconfirms that `f_L1` has `vertex3=1` and fills, reports
`N_fill`, `N_v3`, and `N_both`, and checks that the displayed remaining-bit
tuple `(0, 0, 0, 1, 0)` is a counterexample. Declared audit inputs are this
note and the axiom memo; the runner writes no cache and authors no audit
verdict.

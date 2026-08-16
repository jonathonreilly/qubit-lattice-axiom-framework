---
claim_id: cube_covariant_nn_hop_cost_minkowski_mismatch_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Whether every cube-covariant 6-NN hop-cost gives arrival proportional to ℓ¹, and whether that matches Euclidean-isotropic c / the discrete ℓ² null cone on the radius-4 integer ball, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_covariant_nn_hop_cost_minkowski_mismatch_2026_08_15.py
---

# Cube-Covariant Six-Neighbor Hop Cost Forces First Arrival Proportional To ℓ¹

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact hop-cost covariance under the proper cube group on the six
nearest-neighbor directions, the implied first-arrival function on the
radius-4 integer ball, and a displayed comparison to Euclidean-isotropic `c`
and the discrete `ℓ²` null cone. No occupancy step is run. No physical clock,
boost, or Wick map is selected.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_covariant_nn_hop_cost_minkowski_mismatch_2026_08_15.py`](../scripts/cube_covariant_nn_hop_cost_minkowski_mismatch_2026_08_15.py)

## Result Up Front

Lattice names nearest-neighbor adjacency on `Z^3` and proper cubic rotations
about each site. The six axis directions `{±x,±y,±z}` are one orbit of the
proper cube group `G+` of order `24`. A hop-cost on that unit orbit is a map

`w : {±x,±y,±z} → {positive integers}`.

Cube-covariant means `w(gv)=w(v)` for every `g∈G+` and every axis direction
`v`. Because the six directions form a single orbit, every cube-covariant `w`
is a positive constant `w_0`. First arrival from the origin using only those
hops is then the displayed function

`t(v) = w_0 |v|_1`.

That arrival is scored only as a displayed comparison object. It is not
attached as a named kernel and is not written into Lattice or Admissibility.

Euclidean-isotropic `c` would require `t(v)^2 / |v|_2^2` constant on nonzero
`v` with `|v|_1 ≤ 4`. It is not: `(1,0,0)` gives `w_0^2` and `(1,1,0)` gives
`2 w_0^2`. The discrete null set `{v : t(v)^2 = |v|_2^2}` is a proper subset
of the same ball; the same witness `(1,1,0)` lies off the cone. Both
comparisons are independent of the constant `w_0 ≥ 1`.

Therefore no cube-covariant 6-NN unit-orbit member matches the displayed
Minkowski-light comparisons. Displayed, not adopted. Do not adopt a Wick map.
Do not write Minkowski into Admissibility.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Those sentences supply the six-neighbor graph and the proper-cube covariance
used to score hop costs. They do not name a hop-cost, a first-arrival clock, a
null cone, a boost, or a Wick map. This note does not edit them.

Record is unused. The current Record boundary remains:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

No occupancy is grown on a new patch. The radius-4 integer ball is an
enumeration domain for the already-displayed arrival function, not a new
spatial construction.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "G+ orbit uniqueness, constancy of every cube-covariant hop-cost, first-arrival t(v)=w_0 |v|_1, and the two radius-4 comparison failures are finite exact statements. Minkowski light is a displayed comparator, not an adopted law."
trace_class: negative_route_pruning
target_claim_id: cube_covariant_nn_hop_cost_minkowski_mismatch
target_blocker_text: "score whether cube-covariant 6-NN unit-orbit hop-costs can match Euclidean-isotropic c or the discrete ℓ² null cone"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "Do not attach a named arrival kernel; if a later route wants isotropic c it must change the hop set, drop cube covariance, or add structure that is not scored here."
conditional_surface_status: "exact for cube-covariant positive-integer hop-costs on the six-direction unit orbit; no adopted clock or axiom edit"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, `e_3=(0,0,1)`, and

`A = {±e_1, ±e_2, ±e_3}`.

A proper cube matrix is a `3×3` monomial signed-permutation matrix with
exactly one nonzero entry `±1` in each row and column and determinant `+1`.
The proper cube group `G+` is the set of all such matrices. It acts on
`Z^3` by ordinary matrix multiplication, and the action preserves `A`.

A hop-cost is a map `w:A → {1,2,3,…}`. It is cube-covariant when
`w(gv)=w(v)` for all `g∈G+` and all `v∈A`.

A path from the origin to `v∈Z^3` is a finite sequence of steps from `A`.
Its cost is the sum of `w` along the steps. First arrival `t(v)` is the
minimal cost; `t(0)=0`. Only the six-direction unit orbit is used. Face
diagonals and longer steps are a different hop set and are not scored.

The taxicab and Euclidean quadratic forms on `Z^3` are the displayed
comparators

`|v|_1 = |v_1|+|v_2|+|v_3|`,

`|v|_2^2 = v_1^2+v_2^2+v_3^2`.

The finite comparison domain is the nonzero integer ball `|v|_1 ≤ 4`.

## Theorem 1 — One Orbit, Constant Cost, Arrival Proportional To ℓ¹

Every vector in `A` is `G+`-equivalent to `e_1`. Explicitly, the 90-degree
rotation about `e_3` with matrix

```text
[[ 0,-1, 0],
 [ 1, 0, 0],
 [ 0, 0, 1]]
```

sends `e_1 ↦ e_2 ↦ -e_1 ↦ -e_2 ↦ e_1`. The 90-degree rotation about `e_2`
with matrix

```text
[[ 0, 0, 1],
 [ 0, 1, 0],
 [-1, 0, 0]]
```

sends `e_1 ↦ -e_3` and `-e_3 ↦ -e_1`, and likewise places `±e_3` in the same
orbit. Direct enumeration of `G+` confirms `|G+|=24` and `|G+ · e_1|=6`.

If `w` is cube-covariant and `v=g e_1`, then `w(v)=w(e_1)`. Hence `w` is
constant on `A`. Write `w_0` for that common positive integer.

Any walk from `0` to `v` uses at least `|v|_1` steps, because each step
changes one coordinate by `±1`. Extra cancelling pairs only raise the cost.
A coordinate-monotone walk with exactly `|v_i|` steps of sign `sign(v_i)`
along each axis exists and has cost `w_0 |v|_1`. Therefore

`t(v) = w_0 |v|_1`.

The identity is checked on the radius-4 ball by shortest-path search against
the closed form. It is a displayed arrival, not an adopted physical clock.

## Theorem 2 — Euclidean-Isotropic `c` Fails On The Radius-4 Ball

Euclidean-isotropic unit `c` would require the displayed ratio

`t(v)^2 / |v|_2^2`

to be constant on nonzero `v` with `|v|_1 ≤ 4`. Substituting Theorem 1 gives

`w_0^2 |v|_1^2 / |v|_2^2`.

At `(1,0,0)` the value is `w_0^2`. At `(1,1,0)` the value is `2 w_0^2`.
These are unequal for every integer `w_0 ≥ 1`. The mismatch is therefore
forced by cube-covariant 6-NN hop costs, not by a special choice of the
constant.

## Theorem 3 — Discrete Null Cone Is A Proper Subset

The displayed discrete null comparison is `t(v)^2 = |v|_2^2`. On the
nonzero radius-4 ball this is a proper subset. The witness `(1,1,0)` has

`t(1,1,0)^2 = 4 w_0^2`, `|v|_2^2 = 2`,

so it is never null for integer `w_0 ≥ 1`. Axis sites with `w_0=1` do lie
on the displayed cone, which is enough to show the cone is nonempty and
still a proper subset.

No cube-covariant 6-NN unit-orbit member therefore matches both displayed
Minkowski-light comparisons (isotropic `c` and the discrete `ℓ²` null cone).
The comparison is displayed, not adopted. A Wick map is not adopted. Minkowski
structure is not written into Admissibility.

## Exact Target And Obligation Graph

| Obligation | Disposition |
|---|---|
| quote current Lattice nearest-neighbor and proper-cube wording | source-bound |
| quote current Admissibility covariance wording | source-bound |
| enumerate `G+` and the six-direction orbit | closed by finite listing |
| cube-covariant hop-costs are constant | closed by one-orbit transitivity |
| first arrival equals `w_0 |v|_1` | closed by counting plus shortest-path check |
| isotropic-`c` ratio fails on the radius-4 ball | closed by the two witnesses |
| discrete null cone is a proper subset | closed by the same face-diagonal witness |
| adopt Minkowski, a boost, or a Wick map | outside the claim |
| grow occupancy on a new patch | not executed |
| edit Lattice or Admissibility | `hypothetical_axiom_status: no edit` |

The obligation graph is acyclic. Every leaf of the bounded comparison is
closed. Adoption of a physical light law is not a proof leaf because it is
expressly not part of the target.

## Imports And Non-Claims

Only the current axiom memo is imported. No occupancy construction, no named
arrival kernel, no boost matrix, and no Wick substitution is imported. The
Euclidean-isotropic `c` test and the discrete `ℓ²` null test are displayed
comparators on a finite integer ball.

The theorem does not say that isotropic light is impossible in every later
construction. It says that cube-covariant positive-integer hop-costs on the
six-direction unit orbit force `t ∝ ℓ¹`, and that this displayed arrival fails
the two stated comparisons.

## Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It isolates hop-cost covariance on the Lattice six-neighbor orbit as the mechanism that forces first arrival proportional to `ℓ¹`. |
| V2 | Current main names proper cubic rotations and nearest-neighbor adjacency, but does not score this hop-cost orbit argument against the displayed light comparisons. |
| V3 | Group order, orbit size, shortest-path arrival, and the two witnesses are independently finite and exact. |
| V4 | The result is more than a restatement of Lattice because it enumerates the hop-cost invariants and compares the implied arrival to two explicit tests. |
| V5 | The comparisons remain displayed; the note does not install Minkowski structure or a clock. |

## No-Go Discipline Gate

The negative claim is restricted to cube-covariant 6-NN unit-orbit hop-costs
and to the two displayed light comparisons on the radius-4 integer ball. No
global impossibility of isotropic light is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| cube-covariant 6-NN hop-cost | equalize costs on the single `G+` orbit | executed; forces `t=w_0 |v|_1` |
| non-covariant hop-cost | assign unequal axis costs | lives only after dropping cube covariance; mutation fails covariance |
| larger hop set | add face diagonals or longer steps | different member; not the 6-NN unit orbit scored here |
| drop covariance but keep 6-NN | direction-dependent costs | live different-object route; not cube-covariant |
| occupancy on a new patch | grow a spatial configuration | not executed |
| Wick map or boost | change the comparison form | not adopted |
| write Minkowski into Admissibility | enlarge the axiom | forbidden; `no edit` |

### N2 — wall independence

Cube covariance, the six-direction hop set, the positive-integer cost type,
and the two light comparisons are distinct inputs. The note claims no
complete wall collection beyond this scored class.

### N3 — hidden-condition scan

The hop set, the group `G+`, cube covariance, the shortest-path arrival, the
radius-4 domain, and both comparison predicates are declared. Occupancy,
a Wick map, a boost, and an axiom edit are not silently assumed.

### N4 — source residual matching

The current axiom memo supplies nearest-neighbor adjacency and proper cubic
rotations, and an Admissibility rule covariant under those rotations. It does
not name Minkowski light. The residual scored here is hop-cost covariance
versus the displayed comparisons, not a leftover named-kernel character.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | six axis directions and named witnesses `(1,0,0)`, `(1,1,0)` | no continuum spacetime classification |
| per site | first arrival from the origin on `Z^3` | no occupancy field |
| per mode | no mode calculation | no spectral exhaustion |
| per block | radius-4 integer ball | no new spatial patch |
| lattice wide | checked and not executed | no global light-law derivation |

### N6 — live partial-closure paths

A later construction may change the hop set, drop cube covariance, or add
structure that is not a 6-NN unit-orbit hop-cost. Those are different
objects. They are not scored here and are not filled by writing Minkowski
into Admissibility.

### N7 — hostile steelman

**Steelman:** A different positive integer on each axis could restore
isotropic `c` while remaining a 6-NN member.

**Answer:** The six directions are one `G+` orbit, so cube covariance forbids
unequal axis costs. After covariance the only remaining free parameter is the
overall constant `w_0`, which cancels out of the mismatch `2 w_0^2 ≠ w_0^2`.

### N8 — cross-cycle echo

This note does not attach a named arrival kernel and does not treat the
comparison as leftover character of a previously named line or member. It
scores only hop-cost covariance on the Lattice six-neighbor orbit and the
displayed arrival `t ∝ ℓ¹`.

**Gate disposition:** PASS for orbit constancy, displayed arrival
`t(v)=w_0 |v|_1`, and the two finite comparison failures. FAIL / DO NOT SHIP
for “Minkowski is adopted,” “Admissibility now contains a boost,” “a Wick map
is selected,” or “occupancy was grown on a new patch.”

## Primary Runner

The primary runner enumerates `G+`, checks that the six directions are one
orbit, tests cube-covariant constancy, computes first arrival by shortest
path, compares `t^2/|v|_2^2` on the named witnesses, and confirms the
discrete-null witness. It authors no audit verdict.

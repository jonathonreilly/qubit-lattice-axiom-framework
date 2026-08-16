---
claim_id: skew_three_seed_lock_tick_stab_pair_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball star at v=(-1,1,1), whether lock-ticks shrink Stab enough for a Stab-invariant pair member is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_lock_tick_stab_pair_2026_08_15.py
---

# Lock-Ticks Versus Occupancy Stabilizer On The Off-Axis Three-Seed Star (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the unread six-neighbor star at `v = (−1,1,1)` on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`. Occupied nearest neighbors
carry a lock-tick `t(w) = min_s |w − s|_1`. Local data are `(σ, t)`.
Score the star at `v` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_lock_tick_stab_pair_2026_08_15.py`](../scripts/skew_three_seed_lock_tick_stab_pair_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment maskstab `#pending` reported that every weight-4 occupancy has
`N_stab_ok = 0`. Occupancy alone cannot host a fair pair. The residual
here is not leftover of staborb (no times) or delsgn (distant seeds). It
is the lock-tick object on the same displayed three-ball star.

On this star, occupancy is the 6-bit nearest-neighbor occupancy `σ` of
`U` at `v`. Each occupied neighbor `w` also carries

`t(w) = min{ |w|_1, |w − (2,0,0)|_1, |w − (1,2,1)|_1 }`.

Empty slots have no tick. Local data are `(σ, t)`. `G+` acts on slots.
The occupancy stabilizer and the lock-tick stabilizer are

`Stab(σ) = { g in G+ : g · σ = σ }`,

`Stab(σ,t) = { g in G+ : g · σ = σ and t(g · μ) = t(μ) on occupied slots }`.

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Direct listing against `U` gives

`σ = (1, 0, 1, 1, 0, 1)`.

**Theorem 1.** On the four occupied slots the lock-ticks are

`t(+x) = 2`, `t(+y) = 2`, `t(−y) = 2`, `t(−z) = 2`.

`|Stab(σ)| = 2`. `|Stab(σ,t)| = 2`. The occupancy swapper survives.

**Theorem 2.** `N_tick_ok = 0`: none of the four July-3 pair members with
support `σ` is invariant under `Stab(σ,t)`. The implication “if `|Stab(σ,t)| = 1` then
`N_tick_ok = N_pair_support`” holds vacuously here because
`|Stab(σ,t)| = 2`. On this `σ`, `N_pair_support = 4`.

**Theorem 3.** Displayed, not adopted. Do not write ticks into
Admissibility. Do not write any such `c` into Admissibility. Do not
attach L1. Do not add a 4th ball. Qubit remains `M_2(C)`. No axiom edit.

## Current Premise Boundary

The Lattice, Admissibility, Record, and Qubit sentences used here are quoted
from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

it does not supply the formation site, probability,
or rate.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

A site never carries more than one record; records are permanent.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names neither `Stab(σ,t)` nor any lock-tick, nor any July-3
pair member, as the framework's fixed rule. The covariance clause is the
reason a local labeling on the orbit of `(σ, t)` must be stabilizer-invariant.
Formation site and rate remain outside the axiom memo. Qubit remains
`M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ lock-ticks on one unread six-neighbor star, occupancy and lock-tick stabilizer orders, and a 48-member pair invariance census. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_lock_tick_stab_pair
target_blocker_text: "on the off-axis three-ball star at v=(-1,1,1), whether lock-ticks shrink Stab enough for a Stab-invariant pair member"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of t on the four occupied slots, |Stab(σ)|, |Stab(σ,t)|, swapper survival, and N_tick_ok; do not write ticks into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on the star at v=(-1,1,1); t=(2,·,2,2,·,2) on occupied slots; |Stab(σ)|=2; |Stab(σ,t)|=2; occupancy swapper survives; N_tick_ok=0; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0 = (0,0,0)`, `p = (2,0,0)`, and `q = (1,2,1)`. The closed ℓ¹
ball of radius two is

`B_2(c) = { x ∈ Z^3 : |x − c|_1 ≤ 2 }`.

The locked set is the already-given union

`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`.

The three balls each have 25 sites. Pairwise overlaps are 7, 4, and 4,
and the triple overlap has 2 sites, so `|U| = 62`. The unread site is

`v = (−1,1,1)`.

Then `|v|_1 = 3`, `|v − p|_1 = 5`, and `|v − q|_1 = 3`, so `v ∉ U`.

The six nearest neighbors, in the declared order, are

| slot | neighbor | in `U` | lock-tick |
|---|---|---|---|
| `+x` | `(0,1,1)` | yes | `2` |
| `−x` | `(−2,1,1)` | no | none |
| `+y` | `(−1,2,1)` | yes | `2` |
| `−y` | `(−1,0,1)` | yes | `2` |
| `+z` | `(−1,1,2)` | no | none |
| `−z` | `(−1,1,0)` | yes | `2` |

Occupancy at `v`:

`σ = (1, 0, 1, 1, 0, 1)`.

On occupied slots the lock-tick is the minimum ℓ¹ distance to a seed.
Empty slots have no tick. The displayed tick tuple, with a dot on empty
slots, is

`t = (2, ·, 2, 2, ·, 2)`.

Support of a 6-tuple is the set of slots with a nonzero letter. Occupancy
`σ` is already that indicator.

`G+` is the 24 determinant-`+1` signed permutation matrices of the three
axes. A matrix `g` permutes the six axis directions: the letter (or bit,
or tick) at slot `μ` moves to slot `gμ`. The two stabilizers are as
named above.

The July-3 `k = 3` chiral pair is the unique pair of `G+` orbits of
handed fully-mixed 6-tuples on the three-letter alphabet `{0,1,2}` with
`0` empty. Fully mixed means every axis is bi-colored and each letter is
used twice. The pair is reconstructed by enumerating the 24 proper
rotations on `{0,1,2}^6`; it has 48 members (two orbits of size 24).
Letters `{1,2}` are the two nonzero condition letters; they may be
written `{+, −}` when displaying a 6-tuple.

`N_pair_support` is the number of pair members whose support equals `σ`.
On this `σ` that number is 4. `N_tick_ok` is the number of those members
`c` with `g · c = c` for every `g` in `Stab(σ,t)`.

If `|Stab(σ,t)| < |Stab(σ)|`, lock-ticks may admit a pair member that
occupancy alone refused. That comparison is the residual.

## Theorem 1 — lock-ticks and the two stabilizers

The four occupied neighbors and their lock-ticks are

| slot | `w` | `|w|_1` | `|w − p|_1` | `|w − q|_1` | `t(w)` |
|---|---|---:|---:|---:|---:|
| `+x` | `(0,1,1)` | 2 | 4 | 2 | 2 |
| `+y` | `(−1,2,1)` | 4 | 6 | 2 | 2 |
| `−y` | `(−1,0,1)` | 2 | 4 | 4 | 2 |
| `−z` | `(−1,1,0)` | 2 | 4 | 4 | 2 |

So

`t(+x) = 2`, `t(+y) = 2`, `t(−y) = 2`, `t(−z) = 2`.

Enumerating the 24 proper rotations on the occupancy 6-tuple gives

`|Stab(σ)| = 2`.

A generating list is

1. the identity `id : (x, y, z) ↦ (x, y, z)`, which fixes every slot;
2. the order-2 occupancy swapper `s : (x, y, z) ↦ (−z, −y, −x)`, whose
   slot permutation is

   `+x ↔ −z`, `−x ↔ +z`, `+y ↔ −y`.

Those two matrices generate `Stab(σ)` and exhaust it. The swapper
preserves the occupied set `{+x, +y, −y, −z}` and swaps the two empty
slots.

Because every occupied lock-tick equals `2`, the identity
`t(s · μ) = t(μ)` holds on occupied slots. Therefore `s` lies in
`Stab(σ,t)`, the occupancy swapper survives, and

`|Stab(σ,t)| = 2`.

Lock-ticks do not shrink the occupancy stabilizer on this star.
`|Stab(σ,t)| < |Stab(σ)|` is false here.

Scoring only the star at `v`. This is not leftover of staborb (no times)
and not leftover of delsgn (distant seeds).

## Theorem 2 — lock-tick-invariant pair members

The July-3 pair is reconstructed by partitioning `{0,1,2}^6` into 57
`G+` orbits and retaining the unique pair of orbits exchanged by spatial
inversion. Exactly four pair members have support equal to `σ`:

| member `{0,1,2}` | displayed `{+,0,−}` |
|---|---|
| `(1, 0, 1, 2, 0, 2)` | `(+,0,+,−,0,−)` |
| `(1, 0, 2, 1, 0, 2)` | `(+,0,−,+,0,−)` |
| `(2, 0, 1, 2, 0, 1)` | `(−,0,+,−,0,+)` |
| `(2, 0, 2, 1, 0, 1)` | `(−,0,−,+,0,+)` |

So `N_pair_support = 4`.

For `c` among those four, `g · c = c` for every `g` in `Stab(σ,t)` if
and only if `s · c = c`, because `Stab(σ,t) = {id, s}`. The slot
permutation of `s` requires `c(+x) = c(−z)` and `c(+y) = c(−y)`. Every
July-3 pair member is fully mixed, so the `y`-axis is bi-colored:

`c(+y) ≠ c(−y)`.

Therefore no support-matched pair member is fixed by `s`, and

`N_tick_ok = 0`.

If `|Stab(σ,t)| = 1` then `N_tick_ok = N_pair_support`. That implication
is recorded. It is not triggered: `|Stab(σ,t)| = 2`. On this `σ`,
`N_pair_support = 4`.

Lock-ticks do not shrink `Stab` enough for a Stab-invariant pair member
on this star.

## Theorem 3 — displayed, not adopted

The lock-ticks, the two stabilizer orders, swapper survival, and the
count `N_tick_ok = 0` are displayed member data. They are not the
framework's fixed Admissibility rule. This note does not write ticks into
Admissibility. Do not write ticks into Admissibility. Do not write any
such `c` into Admissibility. Do not attach L1. Do not add a 4th ball.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On this unread star, the four occupied lock-ticks
  are all `2`, `|Stab(σ)| = 2`, `|Stab(σ,t)| = 2`, the occupancy swapper
  survives, `N_pair_support = 4`, and `N_tick_ok = 0`.
- **What is displayed only.** The ticks, the two stabilizers, and the
  invariance count are one rival table. They are not adopted.
- **What is not claimed.** No attachment of ticks or any pair member to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no fourth
  equal-radius ball; no leftover of staborb (no times); no leftover of
  delsgn (distant seeds); no compiler no-go.
- **Mutation controls.** A rebuilt `σ` other than `(1, 0, 1, 1, 0, 1)`
  fails. A rebuilt occupied tick other than `2` fails. `|Stab(σ,t)| = 1`
  would trigger `N_tick_ok = N_pair_support` and fail the unshrunk
  report. A note that writes ticks into Admissibility, attaches L1, or
  authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, occupancy `σ`, the
lock-ticks on occupied slots, the 24 proper cube rotations acting on
slots, `Stab(σ)`, `Stab(σ,t)`, swapper survival, the reconstructed
July-3 pair, `N_pair_support`, `N_tick_ok`, the current premise boundary,
and the mutation controls. It writes no cache and authors no audit
verdict.

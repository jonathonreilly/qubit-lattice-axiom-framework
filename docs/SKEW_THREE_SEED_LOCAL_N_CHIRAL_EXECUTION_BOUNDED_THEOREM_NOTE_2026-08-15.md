---
claim_id: skew_three_seed_local_n_chiral_execution_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), whether the local-in-n 6-tuple (−,0,+,−,0,+) is unique-axis compatible and fires the July-3 k=3 pair is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/skew_three_seed_local_n_chiral_execution_2026_08_15.py
---

# Local-In-`n` Chiral Execution At The Off-Axis Three-Seed Breaker (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` and the unread six-neighbor
star at `v = (−1,1,1)`. The July-3 `k = 3` pair is reconstructed as a
formation predicate on `{0,+,−}^6` and executed at `v` only, with the
local-in-`n` 6-tuple `c = (−,0,+,−,0,+)`. Score `U` and the star at `v`
only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_local_n_chiral_execution_2026_08_15.py`](../scripts/skew_three_seed_local_n_chiral_execution_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Investment `#6654` (skewlab membership only) reported that at unread
`v = (−1,1,1)` on this off-axis triple the unique-axis fragment is
`(*,0,+,*,0,*)`, that exactly two unique-axis-respecting completions
are July-3 pair members, and that exactly one local-in-`n` labeling is
a pair member, namely

`c = (−,0,+,−,0,+)`.

The residual here is not leftover-char of skewlab (membership only).
It is the *run* of that one 6-tuple at `v`: unique-axis agreement on
unambiguous slots, fire, `N_new`, and permanence of `U`.

Treat `U` as already locked. The site `v = (−1,1,1)` is unread: it lies
in none of the three radius-two ℓ¹ balls. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The four occupied nearest neighbors of `v` in `U` are `+x`, `+y`, `−y`,
and `−z`. The two empty slots are `−x` and `+z`. Occupancy mask

`m = (1, 0, 1, 1, 0, 1)`.

The displayed 6-tuple `c` has exactly that occupancy mask.

The occupancy kernel on `U` assigns a unique-axis label to a neighbor
`w` when the dipole `n = d/3` at `w` has exactly one nonzero component;
the label is the sign of that component. On this star the unique-axis
fragment is

`(*,0,+,*,0,*)`,

with `*` marking an occupied neighbor whose `|supp n| ≠ 1`. The one
unambiguous occupied slot agrees with `c`: `+y = +`. Empty slots stay
`0`. Unique-axis slots match `c`.

The July-3 unique `k = 3` chiral pair is the two proper-cubic orbits of
handed fully-mixed 6-tuples. It has 48 members. The tuple `c` is one of
them, so the pair fires at unread `v`. Execution at this star alone
yields

`N_new = 1`,

and the new lock is `v`. Every site of `U` remains locked. The center
`v` was not already in `U`.

This is a displayed rival execution, not adopted. Do not write `c` into
Admissibility. Do not attach L1. Do not add a 4th ball. Occupancy-only
formation (`n ≠ 0`) is not attached. Qubit remains `M_2(C)`.

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

Admissibility names neither the 6-tuple `c` nor the July-3 pair as the
framework's fixed rule. Record permanence is used only to keep the locks
on `U` after the displayed tick at `v`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one off-axis three-ball union, unique-axis signs on one six-neighbor star, and membership of one local-in-n 6-tuple in the reconstructed July-3 k=3 pair. Displayed execution only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_local_n_chiral_execution
target_blocker_text: "at unread v=(-1,1,1) on the off-axis three-ball union, whether the local-in-n 6-tuple (−,0,+,−,0,+) is unique-axis compatible and fires the July-3 k=3 pair"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_new and unique-axis agreement; do not write c into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on U=B_2(0)∪B_2((2,0,0))∪B_2((1,2,1)) at unread v=(-1,1,1) for the local-in-n 6-tuple (−,0,+,−,0,+); displayed, not adopted"
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

| slot | neighbor | in `U` |
|---|---|---|
| `+x` | `(0,1,1)` | yes |
| `−x` | `(−2,1,1)` | no |
| `+y` | `(−1,2,1)` | yes |
| `−y` | `(−1,0,1)` | yes |
| `+z` | `(−1,1,2)` | no |
| `−z` | `(−1,1,0)` | yes |

Occupancy mask at `v`:

`m = (1, 0, 1, 1, 0, 1)`.

Letters are `{0, +, −}` with `0` empty/unread. The displayed 6-tuple is

`c = (−,0,+,−,0,+)`.

Its support is exactly `m`.

At a site `w`, the occupancy 6-tuple of its neighbors inside `U`
determines the dipole

`d_μ = occ(w + e_μ) − occ(w − e_μ)`, `n = d/3`.

If exactly one component of `n` is nonzero, the unique-axis label of
`w` is the sign of that component. Otherwise the occupied neighbor is
ambiguous.

The July-3 pair is reconstructed, not imported as a table. Letters
`{0,1,2}` with `0` empty, `1 = +`, and `2 = −` color the six axis
directions. The proper cubic group `G+` is the 24 determinant-`+1`
signed permutation matrices acting on those directions. Spatial
inversion `P = −I` exchanges `+μ` with `−μ`. A `G+`-orbit is chiral
when `P` sends it to a different `G+`-orbit. At three letters there is
exactly one such pair; its two orbits have 24 members each. The
formation predicate `f` is membership in that 48-element set. Do not
overwrite existing locks.

## Theorem 1 — Unique-axis fragment agrees with `c`; `U` persists

The occupancy dipoles on the four occupied neighbors are exact:

| neighbor | occupancy 6-tuple | `n` | unique-axis |
|---|---|---|---|
| `(0,1,1)` | `(1,0,1,1,0,1)` | `(1/3, 0, −1/3)` | ambiguous |
| `(−1,2,1)` | `(1,0,0,0,0,0)` | `(1/3, 0, 0)` | `+` |
| `(−1,0,1)` | `(1,0,0,0,0,1)` | `(1/3, 0, −1/3)` | ambiguous |
| `(−1,1,0)` | `(1,0,0,1,0,0)` | `(1/3, −1/3, 0)` | ambiguous |

The unique-axis fragment at `v` is therefore

`(*,0,+,*,0,*)`.

Every unambiguous occupied neighbor matches the corresponding slot of
`c`. Empty neighbors remain empty. Unique-axis slots stay fixed and
match `c`. The star center `v` is not already in `U`. After the
displayed lock of `v`, the set `U` is still locked: records on `U` are
permanent, and the execution does not unlock them.

Scoring only `U` and the star at `v`. This is not leftover-char of
skewlab (membership only): the present objects are the fire at this
one unread star and the permanence of `U`.

## Theorem 2 — The July-3 pair fires at `v` for this `c`

The reconstructed pair has `N_pair = 48`. Under the letter map
`0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`,

`c ≡ (2, 0, 1, 2, 0, 1)`

is a pair member. It is fully mixed: each axis is bi-colored and each
letter appears twice. Scoring only `U` and the star at `v`, the pair
fires at the single unread center, so

`N_new = 1`

and the new lock is `v`. The post-tick locked set is `U ∪ {v}`. The
6-tuple `c` is a July-3 `k = 3` pair member.

This is an execution of one local-in-`n` 6-tuple. It is not a
membership census of every unique-axis-respecting completion.

## Theorem 3 — Displayed rival execution, not adopted

The predicate `f` and the 6-tuple `c` are displayed member data. They
are not the framework's fixed Admissibility rule. This note does not
write `c` into Admissibility. Do not attach L1. Do not add a 4th ball.
Occupancy-only formation (the `n ≠ 0` gate) is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

This note is not leftover-char of skewlab (membership only), which
asked only whether any local-in-`n` labeling is a pair member.

## Honest-auditor / Boundary

- **What is proved.** On this `U`, at this unread `v`, the given
  local-in-`n` 6-tuple is unique-axis compatible on every unambiguous
  occupied neighbor, is a July-3 `k = 3` pair member, and fires with
  `N_new = 1` while `U` persists.
- **What is displayed only.** The pair, the letter identification
  `{+, −}`, and the execution at `v` are one rival member. They are
  not adopted.
- **What is not claimed.** No attachment of a local-in-`n` labeling to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no claim that
  Admissibility selects `c`; no fourth equal-radius ball.
- **Mutation controls.** A unique-axis disagreement on `+y` fails.
  Non-membership of `c` in the pair fails. `N_new ≠ 1` fails. A note
  that writes `c` into Admissibility, attaches L1, or authors an audit
  verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, unique-axis signs,
the July-3 pair, the fire at `v`, `N_new`, permanence of `U`, the
current premise boundary, and the mutation controls. It writes no
cache and authors no audit verdict.

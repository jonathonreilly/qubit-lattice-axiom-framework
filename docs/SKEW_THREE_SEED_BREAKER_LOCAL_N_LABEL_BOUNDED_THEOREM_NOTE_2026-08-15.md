---
claim_id: skew_three_seed_breaker_local_n_label_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), whether a local-in-n labeling of the occupied neighbors is a July-3 k=3 pair member is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/skew_three_seed_breaker_local_n_label_2026_08_15.py
---

# Local-In-`n` Labels At The Off-Axis Three-Seed Breaker (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` and the unread six-neighbor
star at `v = (−1,1,1)`. Unique-axis fragment, `n` at each occupied
neighbor, `N_fire` among unique-axis-respecting completions, the
lex-first-nonzero-axis map, and whether any local-in-`n` labeling is a
July-3 `k = 3` pair member. Score `U` and the star at `v` only.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_breaker_local_n_label_2026_08_15.py`](../scripts/skew_three_seed_breaker_local_n_label_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).

## Result Up Front

Investment `#6654` (skew3 census only) reported that this off-axis triple
has `N_uneq = 4` unread 4-occupied-NN sites, and that the lex-first
breaker is `v = (−1,1,1)`, where the ambiguous kernels are not all
equal. The residual here is not leftover-char of skew3 (census only).
It is the unique-axis fragment at that one unread star, the count
`N_fire` among unique-axis-respecting `{+,−}` completions, and whether
any completion that is a function of each occupied neighbor’s `n` is a
July-3 pair member.

Treat `U` as already locked. The site `v = (−1,1,1)` is unread: it lies
in none of the three radius-two ℓ¹ balls. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The four occupied nearest neighbors of `v` in `U` are `+x`, `+y`, `−y`,
and `−z`. The two empty slots are `−x` and `+z`. Occupancy mask

`m = (1, 0, 1, 1, 0, 1)`.

The occupancy kernel on `U` assigns a unique-axis label to a neighbor
`w` when the dipole `n = d/3` at `w` has exactly one nonzero component;
the label is the sign of that component. On this star the unique-axis
fragment is

`(*,0,+,*,0,*)`,

with `*` marking an occupied neighbor whose `|supp n| ≠ 1`. Unique-axis
slots stay fixed: `+y = +`. Empty slots stay `0`.

The three ambiguous occupied neighbors and their kernels are

```text
n(+x) = n(−y) = (1/3, 0, −1/3),
n(−z)         = (1/3, −1/3, 0).
```

Those two values are unequal, so a map `f(n) → {+,−}` is no longer
forced to assign the same letter to every ambiguous neighbor.

There are eight unique-axis-respecting completions of the three `*`
slots. Exactly `N_fire = 2` of them are July-3 pair members:

`(+,0,+,−,0,−)`

and

`(−,0,+,−,0,+)`.

The displayed local map “label = sign of the lex-first nonzero axis of
that neighbor’s `n`” (or the unique-axis sign where defined) produces

`(+,0,+,+,0,+)`,

which is not a pair member.

A local-in-`n` labeling is any map from occupancy kernels to `{+,−}`
that fills each occupied neighbor by `f(n(w))` and leaves empty slots
`0`. Because `+x` and `−y` share one kernel, they receive the same
letter. The distinct kernel at `−z` may receive a different letter.
Exactly one such labeling is a pair member:

`(−,0,+,−,0,+)`.

So `N_local_fire = 1`. A local-in-`n` labeling of the occupied
neighbors can be a July-3 `k = 3` pair member on this star. The
lex-first-nonzero-axis map is not that member.

The comparison is displayed, not adopted. Do not write the labeling into
Admissibility. Do not attach L1. Do not add a 4th ball.

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

Admissibility names neither a local-in-`n` labeling of the occupied
neighbors nor the July-3 pair as the framework's fixed rule. Record
permanence is used only to treat the locks on `U` as already given.
Formation site and rate remain outside the axiom memo. Qubit remains
`M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one off-axis three-ball union, eight unique-axis-respecting completions of three ambiguous slots on one six-neighbor star, membership in the reconstructed July-3 k=3 pair, and whether any local-in-n labeling is a pair member. Displayed only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_breaker_local_n_label
target_blocker_text: "at unread v=(-1,1,1) on the off-axis three-ball union, unique-axis fragment, N_fire among completions, and whether any completion that is a function of each occupied neighbor's n is a July-3 pair member"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_fire and the local-in-n membership; do not write the labeling into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on U=B_2(0)∪B_2((2,0,0))∪B_2((1,2,1)) at unread v=(-1,1,1); displayed, not adopted"
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

Letters are `{0, +, −}` with `0` empty/unread.

At a site `w`, the occupancy 6-tuple of its neighbors inside `U`
determines the dipole

`d_μ = occ(w + e_μ) − occ(w − e_μ)`, `n = d/3`.

If exactly one component of `n` is nonzero, the unique-axis label of
`w` is the sign of that component. Otherwise the occupied neighbor is
ambiguous. The lex-first nonzero axis of `n` is the first axis in order
`(x, y, z)` with nonzero component; its sign is the displayed
single-letter local function of `n`.

A local-in-`n` labeling is any map `f` from occupancy kernels to
`{+,−}`. On this star it fills each occupied neighbor `w` by `f(n(w))`
and leaves empty slots `0`. Unique-axis neighbors are already functions
of `n`, so they stay fixed.

The July-3 pair is reconstructed, not imported as a table. Letters
`{0,1,2}` with `0` empty, `1 = +`, and `2 = −` color the six axis
directions. The proper cubic group `G+` is the 24 determinant-`+1`
signed permutation matrices acting on those directions. Spatial
inversion `P = −I` exchanges `+μ` with `−μ`. A `G+`-orbit is chiral
when `P` sends it to a different `G+`-orbit. At three letters there is
exactly one such pair; its two orbits have 24 members each. The
formation predicate `f` is membership in that 48-element set. Do not
overwrite existing locks.

## Theorem 1 — Occupancy mask, unique-axis fragment, and unequal ambiguous `n`

The occupancy dipoles on the four occupied neighbors are exact:

| neighbor | occupancy 6-tuple | `n` | unique-axis |
|---|---|---|---|
| `(0,1,1)` | `(1,0,1,1,0,1)` | `(1/3, 0, −1/3)` | ambiguous |
| `(−1,2,1)` | `(1,0,0,0,0,0)` | `(1/3, 0, 0)` | `+` |
| `(−1,0,1)` | `(1,0,0,0,0,1)` | `(1/3, 0, −1/3)` | ambiguous |
| `(−1,1,0)` | `(1,0,0,1,0,0)` | `(1/3, −1/3, 0)` | ambiguous |

The unique-axis fragment at `v` is therefore

`(*,0,+,*,0,*)`.

The three ambiguous kernels are not all equal: `n(+x) = n(−y)` while
`n(−z)` differs. Any two ambiguous `n` values are unequal for at least
one pair.

Scoring only `U` and the star at `v`. The center `v` is not already in
`U`. This is not leftover-char of skew3 (census only): the present
objects are the fragment and the kernels at this one unread star.

## Theorem 2 — `N_fire` and the local-in-`n` maps

The eight unique-axis-respecting completions, and pair membership, are

| completion | pair member |
|---|---|
| `(+,0,+,+,0,+)` | no |
| `(+,0,+,+,0,−)` | no |
| `(+,0,+,−,0,+)` | no |
| `(+,0,+,−,0,−)` | yes |
| `(−,0,+,+,0,+)` | no |
| `(−,0,+,+,0,−)` | no |
| `(−,0,+,−,0,+)` | yes |
| `(−,0,+,−,0,−)` | no |

So `N_fire = 2`. The firing completions are

`(+,0,+,−,0,−)`

and

`(−,0,+,−,0,+)`.

The reconstructed pair has `N_pair = 48`.

Every ambiguous kernel has lex-first nonzero axis `x` with sign `+`.
Filling each `*` slot by that sign, and keeping the unique-axis `+y = +`,
gives the single completion

`c_lex = (+,0,+,+,0,+)`.

That completion is not a pair member. The map “label = sign of the
lex-first nonzero axis of that neighbor’s `n`” (or unique-axis where
defined) is not a July-3 pair member.

The four local-in-`n` completions, which assign one letter to the shared
kernel `(1/3, 0, −1/3)` and one letter to `(1/3, −1/3, 0)`, are

| local-in-`n` completion | pair member |
|---|---|
| `(+,0,+,+,0,+)` | no |
| `(+,0,+,+,0,−)` | no |
| `(−,0,+,−,0,+)` | yes |
| `(−,0,+,−,0,−)` | no |

So `N_local_fire = 1`. One completion that is a function of each
occupied neighbor’s `n` is a July-3 pair member, namely

`(−,0,+,−,0,+)`.

That member assigns `−` to the shared kernel and `+` to `n(−z)`.

## Theorem 3 — Displayed, not adopted

The occupancy mask, the unique-axis fragment, the eight completions, the
count `N_fire`, the lex-first-nonzero-axis map, and the local-in-`n`
membership are displayed member data. They are not the framework's fixed
Admissibility rule. Do not write the labeling into Admissibility. Do not
attach L1. Do not add a 4th ball. Occupancy-only formation (the `n ≠ 0`
gate) is not attached. Qubit remains `M_2(C)`. No approved primitive is
added. No axiom edit.

This note is not leftover-char of skew3 (census only), which asked only
whether any unread 4-occupied-NN site on this `U` has unequal ambiguous
`n`.

## Honest-auditor / Boundary

- **What is proved.** On this `U`, at this unread `v`, the unique-axis
  fragment is `(*,0,+,*,0,*)`, two of the three ambiguous kernels are
  unequal, exactly two of the eight unique-axis-respecting completions
  are July-3 `k = 3` pair members, the lex-first-nonzero-axis map is not
  a pair member, and exactly one local-in-`n` labeling is a pair member.
- **What is displayed only.** The pair, the letter identification
  `{+, −}`, the eight completions, the lex-first map, and the
  local-in-`n` maps are one rival comparison. They are not adopted.
- **What is not claimed.** No attachment of a local-in-`n` labeling to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no claim that
  Admissibility selects the firing local-in-`n` completion; no fourth
  equal-radius ball.
- **Mutation controls.** `N_fire ≠ 2` fails. Membership of the
  lex-first completion in the pair fails. `N_local_fire ≠ 1` fails. A
  note that writes the labeling into Admissibility, attaches L1, or
  authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, unique-axis signs, the
eight completions, the July-3 pair, `N_fire`, the lex-first-nonzero-axis
completion, the local-in-`n` completions, `N_local_fire`, the current
premise boundary, and the mutation controls. It writes no cache and
authors no audit verdict.

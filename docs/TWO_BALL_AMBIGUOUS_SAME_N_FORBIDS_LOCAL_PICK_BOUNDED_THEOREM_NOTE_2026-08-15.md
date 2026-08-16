---
claim_id: two_ball_ambiguous_same_n_forbids_local_pick_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On U at unread v=(1,−1,1), whether the two ambiguous neighbors have equal n, and whether that forbids every local-in-n labeling from being a July-3 pair member, is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
runner: scripts/two_ball_ambiguous_same_n_forbids_local_pick_2026_08_15.py
---

# Two-Ball Ambiguous Neighbors With The Same `n` Forbid Every Local-In-`n` Pick (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact ℓ¹ two-ball occupancy on `U = B_2(0) ∪ B_2((2,0,0))` and
one unread six-neighbor star at `v = (1,−1,1)`. The two ambiguous occupied
neighbors carry the same occupancy kernel `n`. Every map `f(n) → {+,−}`
therefore assigns them the same letter. Both July-3 firing completions
assign opposite letters on those two slots. Scoring only `U` and the star
at `v`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_ball_ambiguous_same_n_forbids_local_pick_2026_08_15.py`](../scripts/two_ball_ambiguous_same_n_forbids_local_pick_2026_08_15.py)

Framework context on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and the
July-3 classification
[`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md).
Qubit remains `M_2(C)`.

## Result Up Front

Treat `U` as already locked. The site `v = (1,−1,1)` is unread: it lies in
neither radius-two ℓ¹ ball. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The four occupied nearest neighbors of `v` in `U` are `+x`, `−x`, `+y`, and
`−z`. The two empty slots are `−y` and `+z`. Occupancy mask

`m = (1, 1, 1, 0, 0, 1)`.

The occupancy kernel on `U` assigns a unique-axis label to a neighbor `w`
when the dipole `n = d/3` at `w` has exactly one nonzero component; the
label is the sign of that component. On this star the unique-axis fragment
is

`(*, *, −, 0, 0, +)`,

with `*` marking an occupied neighbor whose `|supp n| ≠ 1`. Unique-axis
slots stay fixed: `+y = −` and `−z = +`. Empty slots stay `0`.

The two ambiguous occupied neighbors are `+x = (2,−1,1)` and
`−x = (0,−1,1)`. Each has the same kernel

`n = (0, 1/3, −1/3)`.

The reconstructed July-3 `k = 3` firing completions of the fragment are

`(+,−,−,0,0,+)`

and

`(−,+,−,0,0,+)`.

Those two 6-tuples have opposite letters on `+x` and `−x`. Any function of
`n` alone assigns those two neighbors the same letter, so no local-in-`n`
completion is a firing completion. The same-label fire count is

`N_same_label_fire = 0`.

This is not leftover-char of ambpick (that scored one displayed pick). The
present residual is the equality of the two neighbors' kernels and the
exclusion of every map `f(n) → {+,−}` from the firing set.

The comparison is displayed, not adopted. This note does not write a
non-local pick into Admissibility. Do not attach L1.

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

Admissibility names neither a local-in-`n` pick of the two ambiguous slots
nor a non-local pick that would split equal kernels. Record permanence is
used only to treat the locks on `U` as already given. Formation site and
rate remain outside the axiom memo. Qubit remains `M_2(C)`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one two-ball union: equal occupancy kernels on two ambiguous neighbors of one unread star, and exclusion of every local-in-n labeling from the reconstructed July-3 k=3 firing set. Displayed only."
trace_class: upstream_support
target_claim_id: admissibility_rule_covariance_extension_classification_openness_achiral_oriented_frame_minimal_chiral_channel_bounded_theorem_note_2026-07-03
target_blocker_text: "on U at unread v=(1,−1,1), whether the two ambiguous neighbors have equal n, and whether that forbids every local-in-n labeling from being a July-3 pair member"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Keep the equal-n obstruction displayed; do not write a non-local pick into Admissibility and do not attach L1."
conditional_surface_status: "exact on U=B_2(0)∪B_2((2,0,0)) at unread v=(1,−1,1) for local-in-n labelings of the two ambiguous neighbors; not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0 = (0,0,0)` and `p = (2,0,0)`. The closed ℓ¹ ball of radius two is

`B_2(q) = {x ∈ Z^3 : |x − q|_1 ≤ 2}`.

The locked set is the already-given union

`U = B_2(0) ∪ B_2((2,0,0))`.

The runner enumerates a box large enough to contain both balls and obtains
`|U| = 43`. The unread site is

`v = (1,−1,1)`.

Then `|v|_1 = 3` and `|v − p|_1 = 3`, so `v ∉ U`.

The six nearest neighbors, in the declared order, are

| slot | neighbor | in `U` |
|---|---|---|
| `+x` | `(2,−1,1)` | yes |
| `−x` | `(0,−1,1)` | yes |
| `+y` | `(1,0,1)` | yes |
| `−y` | `(1,−2,1)` | no |
| `+z` | `(1,−1,2)` | no |
| `−z` | `(1,−1,0)` | yes |

Occupancy mask at `v`:

`m = (1, 1, 1, 0, 0, 1)`.

Letters are `{0, +, −}` with `0` empty/unread.

At a site `w`, the occupancy 6-tuple of its neighbors inside `U` determines
the dipole

`d_μ = occ(w + e_μ) − occ(w − e_μ)`, `n = d/3`.

If exactly one component of `n` is nonzero, the unique-axis label of `w` is
the sign of that component. Otherwise the occupied neighbor is ambiguous.

A local-in-`n` labeling is any map `f` from occupancy kernels to `{+,−}`.
On this star it fills each ambiguous occupied neighbor `w` by `f(n(w))` and
leaves unique-axis and empty slots unchanged.

The July-3 pair is reconstructed, not imported as a table. Letters `{0,1,2}`
with `0` empty, `1 = +`, and `2 = −` color the six axis directions. The
proper cubic group `G+` is the 24 determinant-`+1` signed permutation
matrices acting on those directions. Spatial inversion `P = −I` exchanges
`+μ` with `−μ`. A `G+`-orbit is chiral when `P` sends it to a different
`G+`-orbit. At three letters there is exactly one such pair; its two orbits
have 24 members each. The formation predicate `f` is membership in that
48-element set. Do not overwrite existing locks.

## Theorem 1 — Equal kernels; every `f(n)` assigns the same letter

The occupancy dipoles on the four occupied neighbors are exact:

| neighbor | occupancy 6-tuple | `d` | `n` | unique-axis |
|---|---|---|---|---|
| `(2,−1,1)` | `(0,0,1,0,0,1)` | `(0, 1, −1)` | `(0, 1/3, −1/3)` | ambiguous |
| `(0,−1,1)` | `(0,0,1,0,0,1)` | `(0, 1, −1)` | `(0, 1/3, −1/3)` | ambiguous |
| `(1,0,1)` | `(1,1,0,0,0,1)` | `(0, 0, −1)` | `(0, 0, −1/3)` | `−` |
| `(1,−1,0)` | `(1,1,1,0,0,0)` | `(0, 1, 0)` | `(0, 1/3, 0)` | `+` |

In particular

`n(+x neighbor) = n(−x neighbor) = (0, 1/3, −1/3)`.

Any map `f(n) → {+,−}` therefore assigns the two ambiguous neighbors the
same letter. The two local-in-`n` completions of the unique-axis fragment
are exactly the same-label fillings

`(+,+,−,0,0,+)`

and

`(−,−,−,0,0,+)`.

## Theorem 2 — No local-in-`n` completion is a firing completion

The unique-axis-respecting completions that lie in the reconstructed July-3
pair are the two firing 6-tuples

`(+,−,−,0,0,+)`

and

`(−,+,−,0,0,+)`.

Each has opposite letters on `+x` and `−x`. Neither is a same-label
filling. Intersecting the two local-in-`n` completions of Theorem 1 with
the firing set therefore yields the empty set:

`N_same_label_fire = 0`.

Hence no `f(n)` completion is a firing completion. Scoring only `U` and the
star at `v`. The reconstructed pair has `N_pair = 48`. The center `v` is
not already in `U`.

## Theorem 3 — Displayed, not adopted

The equal kernels, the two local-in-`n` completions, the two firing
6-tuples, and the count `N_same_label_fire` are displayed member data.
They are not the framework's fixed Admissibility rule. This note does not
write a non-local pick into Admissibility. Do not attach L1.
Occupancy-only formation (the `n ≠ 0` gate) is not attached. Qubit remains
`M_2(C)`. No approved primitive is added.

This note is not leftover-char of ambpick (that scored one displayed pick).

## Honest-auditor / Boundary

- **What is proved.** On this `U`, at this unread `v`, the two ambiguous
  occupied neighbors have the same `n`, so every local-in-`n` labeling
  assigns them the same letter, and no such labeling is a July-3 pair
  member (`N_same_label_fire = 0`).
- **What is displayed only.** The pair, the letter identification
  `{+, −}`, the two firing 6-tuples, and the local-in-`n` obstruction are
  one rival comparison. They are not adopted.
- **What is not claimed.** No attachment of a local or non-local pick to
  Admissibility; no attachment of occupancy-only formation; no axiom edit;
  no formation rate; no lattice-wide dynamics; no claim that Admissibility
  selects either firing completion.
- **Mutation controls.** Unequal kernels on the two ambiguous neighbors
  fail. `N_same_label_fire ≠ 0` fails. A note that writes a non-local pick
  into Admissibility, attaches L1, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, the two neighbors' `n`,
the local-in-`n` completions, the July-3 pair, the firing completions,
`N_same_label_fire`, the current premise boundary, and the mutation
controls. It writes no cache and authors no audit verdict.

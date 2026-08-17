---
claim_id: weight4_full_axis_one_bit_extra_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 15 weight-4 occupancy masks, whether occupancy names a unique full axis whose one-bit age extra kills Stab is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/weight4_full_axis_one_bit_extra_2026_08_15.py
---

# Occupancy Names The Full Axis; The Extra Is One Age Bit (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 15 weight-4 occupancy masks on the 6-NN star. A mask
empties a whole axis or two perpendicular slots. On the 12 that empty
two perpendicular slots, occupancy names the unique full axis and a
single older/newer bit on that axis is the extra that kills every
occupancy stabilizer swapping those two ends. Score the 15 weight-4
masks. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/weight4_full_axis_one_bit_extra_2026_08_15.py`](../scripts/weight4_full_axis_one_bit_extra_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqbit #6680: one comparison on the unique full axis shrinks
`Stab`. That extra was scored on one star. The residual here is not leftover
of uneqbit (one star). New residual: on all 12 weight-4 masks that empty
two perpendicular slots, occupancy names the unique full axis. The extra
is only which end of that axis is older.

`N_perp = 12` empty two perpendicular slots and have a unique full axis
(both ends occupied). `N_axis = 3` empty a whole axis (no pair support).
The 3 masks that empty a whole axis have 10→no pair support.

**Theorem 1.** `N_perp = 12` empty two perpendicular slots and have a
unique full axis (both ends occupied). `N_axis = 3` empty a whole axis
(no pair support).

**Theorem 2.** On each of the 12, occupancy names the full axis. A single bit on that axis (which end is older) kills every occupancy stabilizer that swaps those two ends. On the uneqrad mask
`σ = (1, 0, 1, 0, 1, 1)` the unique full axis is `z` and the bit
`b = [t(−z) < t(+z)]` already gives `|Stab(σ)| = 2`, `|Stab(σ,b)| = 1`.
The pattern is the same for all 12.

**Theorem 3.** Displayed, not adopted. Do not write the bit into Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither a unique full axis nor the one-bit age extra
on that axis as the framework's fixed rule. The covariance clause is the
reason a local labeling on the orbit of `(σ, b)` must be
stabilizer-invariant. Formation site and rate remain outside the axiom
memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 15 weight-4 occupancy masks: N_perp=12, N_axis=3, unique full axis on each of the 12, one-bit age extra killing the end-swapping occupancy stabilizer, uneqrad mask report, and 10→no pair support on the 3 axis masks. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: weight4_full_axis_one_bit_extra
target_blocker_text: "on the 15 weight-4 occupancy masks, whether occupancy names a unique full axis whose one-bit age extra kills Stab"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_perp, N_axis, the unique full axis on each of the 12, the one-bit extra, and no pair support on the 3 axis masks; do not write the bit into Admissibility or attach L1"
conditional_surface_status: "exact on the 15 weight-4 occupancy masks; N_perp=12; N_axis=3; uneqrad unique full axis z; |Stab(σ)|=2; |Stab(σ,b)|=1 on each of the 12; 10→no pair support on the 3 axis masks; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Slots are the six nearest-neighbor directions in order

`(+x, −x, +y, −y, +z, −z)`.

A weight-4 occupancy mask is a 6-bit string of weight 4. There are
exactly `C(6,4) = 15` such masks. Each mask empties exactly two slots.
Those two slots lie on one axis or on two perpendicular axes.

An axis is full when both of its ends are occupied. `G+` is the 24
proper cube rotations acting on the six slots.

`Stab(σ) = { g in G+ : g · σ = σ }`.

July-3 pair members are the 6-slot 3-letter colorings whose `G+` orbit
is sent to a different orbit by spatial inversion. `N_pair_support` is
the number of pair members with a given occupancy support.

The uneqrad lex-first breaker is the host

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,
radii `(2, 1, 3)`,
`v = (−3,−3,−1)`,

with occupancy and lock-ticks

`σ = (1, 0, 1, 0, 1, 1)`,
`t = (1, ·, 1, ·, 3, 2)`.

On that mask the unique full axis is `z`. The displayed bit is

`b = 1` if `t(−z) < t(+z)`, else `0`.

`Stab(σ,b) = { g in G+ : g · σ = σ and b(g · t) = b(t) }`.

Score the 15 weight-4 masks. The uneqrad host is used only to name the
uneqrad mask and its displayed bit.

## Theorem 1 — `N_perp = 12` and `N_axis = 3`

The 15 masks split by the two emptied slots.

| `σ` | emptied slots | class | unique full axis | `|Stab(σ)|` | `N_pair_support` |
| --- | --- | --- | --- | --- | --- |
| `(0, 0, 1, 1, 1, 1)` | `+x,−x` | axis | none | 8 | 0 |
| `(0, 1, 0, 1, 1, 1)` | `+x,+y` | perp | `z` | 2 | 4 |
| `(0, 1, 1, 0, 1, 1)` | `+x,−y` | perp | `z` | 2 | 4 |
| `(0, 1, 1, 1, 0, 1)` | `+x,+z` | perp | `y` | 2 | 4 |
| `(0, 1, 1, 1, 1, 0)` | `+x,−z` | perp | `y` | 2 | 4 |
| `(1, 0, 0, 1, 1, 1)` | `−x,+y` | perp | `z` | 2 | 4 |
| `(1, 0, 1, 0, 1, 1)` | `−x,−y` | perp | `z` | 2 | 4 |
| `(1, 0, 1, 1, 0, 1)` | `−x,+z` | perp | `y` | 2 | 4 |
| `(1, 0, 1, 1, 1, 0)` | `−x,−z` | perp | `y` | 2 | 4 |
| `(1, 1, 0, 0, 1, 1)` | `+y,−y` | axis | none | 8 | 0 |
| `(1, 1, 0, 1, 0, 1)` | `+y,+z` | perp | `x` | 2 | 4 |
| `(1, 1, 0, 1, 1, 0)` | `+y,−z` | perp | `x` | 2 | 4 |
| `(1, 1, 1, 0, 0, 1)` | `−y,+z` | perp | `x` | 2 | 4 |
| `(1, 1, 1, 0, 1, 0)` | `−y,−z` | perp | `x` | 2 | 4 |
| `(1, 1, 1, 1, 0, 0)` | `+z,−z` | axis | none | 8 | 0 |

`N_perp = 12`. Each of those 12 empties two perpendicular slots, so
exactly one axis has both ends occupied: occupancy names the unique
full axis.

`N_axis = 3`. Each of those 3 empties a whole axis, so two axes are
full and no unique full axis is named. The 3 masks that empty a whole
axis have 10→no pair support: each has `N_pair_support = 0`.

## Theorem 2 — one bit on the named axis kills the end-swapping stabilizer

On each of the 12, `Stab(σ)` has order 2. The non-identity element
swaps the two ends of the unique full axis (and swaps the two remaining
occupied slots). Occupancy therefore names the axis; it does not name
which end of that axis is older.

A single bit on that axis — which end is older — is reversed by every
occupancy stabilizer that swaps those two ends. Hence that bit kills
every such stabilizer, and

`|Stab(σ,b)| = 1`

on each of the 12. The pattern is the same for all 12.

The uneqrad mask is the perp row

`σ = (1, 0, 1, 0, 1, 1)`,

which empties `−x` and `−y` and names unique full axis `z`. Occupied
neighbors and ticks on the uneqrad lex-first host are

- `+x = (−2,−3,−1)` has `t = 1`,
- `+y = (−3,−2,−1)` has `t = 1`,
- `+z = (−3,−3,0)` has `t = 3`,
- `−z = (−3,−3,−2)` has `t = 2`.

Hence `t(−z) = 2 < 3 = t(+z)`, so `b = 1`. The occupancy swapper is

`s : (x, y, z) ↦ (y, x, −z)`,

which swaps `+x ↔ +y` and `+z ↔ −z`. That map preserves `σ` and
reverses the `z` bit, so the occupancy swapper is excluded and

`|Stab(σ)| = 2`, `|Stab(σ,b)| = 1`

on the uneqrad mask. The same occupancy-named axis plus one-bit extra
holds on the other 11 perp masks.

## Theorem 3 — displayed, not adopted

The 15-mask census, the unique full axis on each of the 12, the one-bit
age extra, the uneqrad report, and 10→no pair support on the 3 axis
masks are displayed member data. They are not the framework's fixed
Admissibility rule. This note does not write the bit into Admissibility.
Do not write the bit into Admissibility. Do not attach L1.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 15 weight-4 occupancy masks, `N_perp = 12`
  and `N_axis = 3`. Occupancy names a unique full axis on each of the
  12. A single bit on that axis (which end is older) kills every
  occupancy stabilizer that swaps those two ends, so `|Stab(σ,b)| = 1`
  on each of the 12. The uneqrad mask names axis `z` with `b = 1` and
  `|Stab(σ)| = 2`. The 3 axis masks have 10→no pair support.
- **What is displayed only.** The one-bit age extra and the two
  stabilizers are one rival table. They are not adopted.
- **What is not claimed.** No attachment of the bit, radii, integer
  `t`, or a unique full axis to Admissibility; no attachment of
  occupancy-only formation; no axiom edit; no formation rate; no
  leftover of uneqbit (one star); no compiler no-go.
- **Mutation controls.** A rebuilt `N_perp ≠ 12` or `N_axis ≠ 3` fails.
  A rebuilt perp mask without a unique full axis fails. A rebuilt
  end-swapping occupancy stabilizer that preserves the bit fails. A
  rebuilt uneqrad mask that is not `(1, 0, 1, 0, 1, 1)` or a rebuilt
  `b ≠ 1` fails. A rebuilt axis mask with pair support fails. A note
  that writes the bit into Admissibility, attaches L1, or authors an
  audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 15 weight-4 occupancy masks, the 24
proper cube rotations, unique-full-axis naming on each of the 12, the
one-bit extra that kills every end-swapping occupancy stabilizer, the
uneqrad mask and its displayed bit, July-3 pair support on the 3 axis
masks, the current premise boundary, and the mutation controls. It
scores the 15 weight-4 masks. It writes no cache and authors no audit
verdict.

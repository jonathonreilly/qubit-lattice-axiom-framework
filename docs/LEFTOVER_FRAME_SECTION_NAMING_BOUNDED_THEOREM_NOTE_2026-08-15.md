---
claim_id: leftover_frame_section_naming_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 12 perpendicular weight-4 masks, whether the leftover-frame-positive section is named by occupancy, the age bit, and cube orientation alone is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/leftover_frame_section_naming_2026_08_15.py
---

# Leftover-Frame-Positive Section Named By Occupancy, Age Bit, And Cube Orientation (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 perpendicular weight-4 occupancy masks on the 6-NN star.
Same 12 masks and f as bitsec: the leftover-frame-positive section of
the two July-3 pair completions of the age-bit encoding. Score those 12
masks: leftover slots and the unique full axis as functions of occupancy
`σ` alone, and whether the sign that selects the section uses only the
proper-cube-oriented triple (leftover `+`, leftover `−`, full-axis `+`
letter). Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/leftover_frame_section_naming_2026_08_15.py`](../scripts/leftover_frame_section_naming_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment bitsec names `f` by leftover-frame sign `+1` (directions
leftover `+`, leftover `−`, full-axis `+` letter). New residual: that
frame is built from occupancy (which slots leftover / full) plus the
age bit (full-axis letters) plus the proper-cube orientation. Report
whether any other `G+` invariant is used. If only those, `f` is named
by `(σ,b)` and orientation, not a second extra. Not leftover of bitsec
(existence). Do not attach L1.

**Theorem 1.** For each `σ`, leftover slots and the unique full axis
are functions of `σ` alone. The leftover pair is the two occupied slots
off the unique full axis. Neither depends on the age bit `b` nor on
which of the two completions is chosen.

**Theorem 2.** The sign that selects the section uses the oriented
triple (leftover `+`, leftover `−`, full-axis `+`). That triple is
proper-cube oriented. No second occupancy-independent bit is used.
`N_name=12`: the reconstruction from occupancy, the age bit, and cube
orientation uniquely names both `f(σ,0)` and `f(σ,1)` on every
perpendicular mask, and equals the leftover-frame-positive section.
No other `G+` invariant is used.

**Theorem 3.** Displayed, not adopted. Do not write the frame into
Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither the leftover frame nor the leftover-frame-
positive section as the framework's fixed rule. The covariance clause
is why the leftover-frame sign is checked as a `G+` invariant, not as
a second extra. Formation site and rate remain outside the axiom memo.
Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 12 perpendicular weight-4 masks: leftover slots and the unique full axis are functions of occupancy alone; the leftover-frame-positive section is named by occupancy, the age bit, and proper-cube orientation; N_name=12. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: leftover_frame_section_naming
target_blocker_text: "on the 12 perpendicular weight-4 masks, whether the leftover-frame-positive section is named by occupancy, the age bit, and cube orientation alone"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of leftover slots, full-axis occupancy naming, leftover-frame sign, and N_name=12 on the 12 masks; do not write the frame into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 perpendicular weight-4 masks; leftover slots and full axis are functions of σ alone; N_name=12; no second occupancy-independent bit; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Slots are the six nearest-neighbor directions in order

`(+x, −x, +y, −y, +z, −z)`.

A weight-4 occupancy mask is a 6-bit string of weight 4. A mask is
perpendicular when the two emptied slots lie on two distinct axes. There
are exactly 12 such masks. Each has a unique full axis: both ends of one
axis are occupied.

`G+` is the 24 proper cube rotations acting on the six slots.

July-3 pair members are the 6-slot 3-letter colorings on `{0, +, −}`
whose `G+` orbit is sent to a different orbit by spatial inversion.
Letter order is `0 < + < −`. There are 48 such members. Each of the 12
masks is the support of exactly four of them.

`b = 1` means `t(−axis) < t(+axis)`. Set `c(−axis)=−`, `c(+axis)=+` if
`b=1`, and the swap if `b=0`. Empty slots are `0`. Completions`(σ,b)`
are the pair members that match those four slots. `|Completions|=2` on
each of the 24 `(σ,b)`. The leftover two occupied slots receive opposite
letters, in two ways.

Same 12 masks and f as bitsec: the leftover-frame-positive section takes
the unique completion whose leftover-frame sign is `+1`.

The leftover slots of `σ` are the two occupied slots that do not lie on
the unique full axis. They are read from occupancy alone.

The leftover-frame of a completion is the ordered triple of directions
(leftover `+`, leftover `−`, full-axis `+` letter). That triple takes
one end from each cube axis and is proper-cube oriented: its determinant
is `±1`. The exhibited naming takes the unique leftover-letter assignment
of sign `+1`.

No other `G+` invariant is used. The 48 completions form two `G+` orbits
split exactly by leftover-frame sign. On a fixed `(σ,b)` the two
completions differ only by swapping the leftover letters. Occupancy
names the leftover slots and the full axis; the age bit names the
full-axis letters; cube orientation names which leftover slot is `+`.
There is no second occupancy-independent bit.

Score the 12 masks. The naming denominator is `12`. `N_name=12` if the
occupancy-age-orientation reconstruction uniquely names `f` on every
perpendicular mask.

## Theorem 1 — leftover slots and full axis are functions of `σ` alone

For each of the 12 perpendicular weight-4 masks the unique full axis is
the unique axis with both ends occupied, and the leftover slots are the
two occupied slots off that axis. Both are functions of `σ` alone.
Reading them from either completion of either age bit returns the same
pair.

| `σ` | unique full axis | leftover slots |
| --- | --- | --- |
| `(0, 1, 0, 1, 1, 1)` | `z` | `(−x, −y)` |
| `(0, 1, 1, 0, 1, 1)` | `z` | `(−x, +y)` |
| `(0, 1, 1, 1, 0, 1)` | `y` | `(−x, −z)` |
| `(0, 1, 1, 1, 1, 0)` | `y` | `(−x, +z)` |
| `(1, 0, 0, 1, 1, 1)` | `z` | `(+x, −y)` |
| `(1, 0, 1, 0, 1, 1)` | `z` | `(+x, +y)` |
| `(1, 0, 1, 1, 0, 1)` | `y` | `(+x, −z)` |
| `(1, 0, 1, 1, 1, 0)` | `y` | `(+x, +z)` |
| `(1, 1, 0, 1, 0, 1)` | `x` | `(−y, −z)` |
| `(1, 1, 0, 1, 1, 0)` | `x` | `(−y, +z)` |
| `(1, 1, 1, 0, 0, 1)` | `x` | `(+y, −z)` |
| `(1, 1, 1, 0, 1, 0)` | `x` | `(+y, +z)` |

## Theorem 2 — `N_name=12`; no second occupancy-independent bit

The sign that selects the section uses the oriented triple (leftover
`+`, leftover `−`, full-axis `+`). That triple is proper-cube oriented.
Reconstruct `f(σ,b)` by writing the age-bit letters on the occupancy-
named full axis and assigning opposite leftover letters so the
determinant is `+1`. This names a unique coloring on each of the 24
pairs, equals the leftover-frame-positive section, and uses no other
`G+` invariant. `N_name=12`.

| `σ` | unique full axis | leftover slots | `f(σ,0)` | `f(σ,1)` | named |
| --- | --- | --- | --- | --- | --- |
| `(0, 1, 0, 1, 1, 1)` | `z` | `(−x, −y)` | `(0, −, 0, +, −, +)` | `(0, +, 0, −, +, −)` | 1 |
| `(0, 1, 1, 0, 1, 1)` | `z` | `(−x, +y)` | `(0, +, −, 0, −, +)` | `(0, −, +, 0, +, −)` | 1 |
| `(0, 1, 1, 1, 0, 1)` | `y` | `(−x, −z)` | `(0, +, −, +, 0, −)` | `(0, −, +, −, 0, +)` | 1 |
| `(0, 1, 1, 1, 1, 0)` | `y` | `(−x, +z)` | `(0, −, −, +, +, 0)` | `(0, +, +, −, −, 0)` | 1 |
| `(1, 0, 0, 1, 1, 1)` | `z` | `(+x, −y)` | `(+, 0, 0, −, −, +)` | `(−, 0, 0, +, +, −)` | 1 |
| `(1, 0, 1, 0, 1, 1)` | `z` | `(+x, +y)` | `(−, 0, +, 0, −, +)` | `(+, 0, −, 0, +, −)` | 1 |
| `(1, 0, 1, 1, 0, 1)` | `y` | `(+x, −z)` | `(−, 0, −, +, 0, +)` | `(+, 0, +, −, 0, −)` | 1 |
| `(1, 0, 1, 1, 1, 0)` | `y` | `(+x, +z)` | `(+, 0, −, +, −, 0)` | `(−, 0, +, −, +, 0)` | 1 |
| `(1, 1, 0, 1, 0, 1)` | `x` | `(−y, −z)` | `(−, +, 0, −, 0, +)` | `(+, −, 0, +, 0, −)` | 1 |
| `(1, 1, 0, 1, 1, 0)` | `x` | `(−y, +z)` | `(−, +, 0, +, −, 0)` | `(+, −, 0, −, +, 0)` | 1 |
| `(1, 1, 1, 0, 0, 1)` | `x` | `(+y, −z)` | `(−, +, +, 0, 0, −)` | `(+, −, −, 0, 0, +)` | 1 |
| `(1, 1, 1, 0, 1, 0)` | `x` | `(+y, +z)` | `(−, +, −, 0, +, 0)` | `(+, −, +, 0, −, 0)` | 1 |

A witness on `σ = (0, 1, 0, 1, 1, 1)`, `b = 0`: leftover slots
`(−x, −y)`, full axis `z`, age-bit letters `c(−z)=+`, `c(+z)=−`, and
the leftover assignment `c(−y)=+`, `c(−x)=−` is the unique one with
frame `(−y, −x, −z)` of determinant `+1`. That coloring is
`(0, −, 0, +, −, +)`, the bitsec value of `f(σ,0)`.

The present residual is not leftover of bitsec (existence). Bitsec
already exhibited an equivariant section. The question here is whether
that section is named by occupancy, the age bit, and cube orientation
alone, with no second extra.

## Theorem 3 — displayed, not adopted

The leftover-slot table, the unique-full-axis table, `N_name=12`, the
leftover-frame-positive reconstruction, and the conclusion that no
second occupancy-independent bit is used are displayed member data.
They are not the framework's fixed Admissibility rule. This note does
not write the frame into Admissibility.
Do not write the frame into Admissibility. Do not attach L1.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 12 perpendicular weight-4 masks, leftover
  slots and the unique full axis are functions of `σ` alone, the
  leftover-frame-positive section is named by occupancy, the age bit,
  and proper-cube orientation, and `N_name=12`. No second occupancy-
  independent bit is used. No other `G+` invariant is used.
- **What is displayed only.** The naming of `f` by leftover-frame sign
  `+1` is one rival table. It is not adopted.
- **What is not claimed.** No attachment of the leftover frame, the
  leftover-frame sign, the age bit, opposite letters, or a unique full
  axis to Admissibility; no attachment of occupancy-only formation; no
  axiom edit; no formation rate; no leftover of bitsec (existence); no
  compiler no-go.
- **Mutation controls.** A rebuilt leftover pair that depends on `b`
  fails. A rebuilt `N_name` other than 12 fails. A rebuilt naming that
  uses a second occupancy-independent bit fails. A rebuilt leftover-
  frame triple that is not proper-cube oriented fails. A rebuilt `f`
  unequal to the leftover-frame-positive section fails. A note that
  writes the frame into Admissibility, attaches L1, or authors an
  audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 12 perpendicular weight-4 occupancy
masks, leftover slots and the unique full axis as functions of `σ`
alone, the 24 proper cube rotations, July-3 pair members on
`{0, +, −}`, the opposite-letter write on the unique full axis, the two
completions of each `(σ,b)`, the leftover-frame-positive section, the
occupancy-age-orientation reconstruction, leftover-frame signs, `G+`
invariance of the sign, `N_name`, the current premise boundary, and
the mutation controls. It scores the 12 masks. It writes no cache and
authors no audit verdict.

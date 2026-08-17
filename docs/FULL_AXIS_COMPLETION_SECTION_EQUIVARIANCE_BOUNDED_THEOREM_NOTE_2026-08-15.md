---
claim_id: full_axis_completion_section_equivariance_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 12 perpendicular weight-4 masks, whether a G+-equivariant section of the two pair-completions of the age-bit encoding exists is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/full_axis_completion_section_equivariance_2026_08_15.py
---

# Equivariant Section Of The Two Full-Axis Pair-Completions Under G+ (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 perpendicular weight-4 occupancy masks on the 6-NN star.
The age-bit encoding writes opposite letters on the unique full axis of
each mask `σ` according to `b`, then each `(σ,b)` has two July-3 pair
completions of the leftover occupied slots. Score those 12 masks and
`G+`: the number of `G+` orbits on the `24 × 2` completions, and whether
a section can pick one point per `(σ,b)` orbit-consistently. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/full_axis_completion_section_equivariance_2026_08_15.py`](../scripts/full_axis_completion_section_equivariance_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment bitenc: encoding `b` on the full axis always has a pair
completion, but two of them; lex-first of those two gives
`N_commute=288/576`. New residual: does there exist a `G+`-equivariant
choice of one completion for each `(σ,b)`? If yes, report one such `f`
and `N_commute=576`. If no, the leftover two slots need a second extra.
Not leftover of bitenc (lex-first). Do not attach L1.

**Theorem 1.** The `24 × 2` completions form `N_orbits = 2` orbits under
`G+`, each of size 24. Each orbit meets every `(σ,b)` in exactly one
point, so a section can pick one point per `(σ,b)` orbit-consistently.
`N_section = 2`.

**Theorem 2.** An equivariant section exists. The leftover-frame-positive
section (not lex-first) picks, of the two completions, the one whose
ordered triple of directions (leftover `+`, leftover `−`, full-axis `+`
letter) has determinant `+1`. That `f` differs from lex-first on 12 of
the 24 pairs and has `N_commute = 576`.

**Theorem 3.** Displayed, not adopted. Do not write a section into
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

Admissibility names neither a section of the two pair-completions nor any
leftover-frame sign as the framework's fixed rule. The covariance clause
is the reason a local choice on the orbit of `(σ, b)` must be checked
under `G+`. Formation site and rate remain outside the axiom memo. Qubit
remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 48 pair-completions of the 12 perpendicular weight-4 masks times two age bits: N_orbits=2, N_section=2, and times the 24 proper cube rotations: N_commute=576 of 576 for the leftover-frame-positive section. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: full_axis_completion_section_equivariance
target_blocker_text: "on the 12 perpendicular weight-4 masks, whether a G+-equivariant section of the two pair-completions of the age-bit encoding exists"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_orbits, N_section, and N_commute on the 12 masks; do not write a section into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 perpendicular weight-4 masks; N_orbits=2; N_section=2; N_commute=576 of 576 for the leftover-frame-positive section; displayed, not adopted"
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

The leftover-frame sign of a completion is the determinant of the ordered
triple of directions (leftover `+`, leftover `−`, full-axis `+` letter).
The exhibited section takes the unique completion of sign `+1`.

Displayed ticks realizing `(σ, b)` put the older end of the unique full
axis at tick 1 and the newer end at tick 2 when `b = 1`, and the reverse
when `b = 0`. Occupied slots off that axis carry tick 0. Empty slots
carry no tick. The transported bit is the older-end bit of `g · t` on
the unique full axis of `g · σ`. The commute identity is

`f(g · σ, b_g) = g · f(σ,b)`.

Score the 12 masks and `G+`. The completion denominator is `12 × 2 = 24`.
The commute denominator is `12 × 2 × 24 = 576`.

## Theorem 1 — `N_orbits = 2`; a section can pick one point per `(σ,b)` orbit-consistently

The 48 completions form two `G+` orbits of size 24. The two completions
of a fixed `(σ,b)` lie in opposite orbits. Each orbit therefore meets
every one of the 24 pairs `(σ,b)` in exactly one point. A `G+`-invariant
graph of a section is a union of these orbits, so each orbit is itself
an equivariant section and `N_section = 2`. A section can pick one
point per `(σ,b)` orbit-consistently.

The two orbits are the leftover-frame-positive completions and the
leftover-frame-negative completions. Proper rotations preserve the
sign, so the sign is an orbit invariant.

## Theorem 2 — leftover-frame-positive `f` (not lex-first); `N_commute = 576`

Whether `N_commute=576`. It is, for the leftover-frame-positive section.
`N_commute = 576` of the 576 triples `(σ, b, g)`. Each of the 12 masks
contributes 48 commuting `(b, g)` pairs of 48, so
`N_commute / 576 = 576/576`. A `G+`-equivariant section of the two
pair-completions exists.

| `σ` | unique full axis | `f(σ,0)` | `f(σ,1)` | completions each bit |
| --- | --- | --- | --- | --- |
| `(0, 1, 0, 1, 1, 1)` | `z` | `(0, −, 0, +, −, +)` | `(0, +, 0, −, +, −)` | 2 |
| `(0, 1, 1, 0, 1, 1)` | `z` | `(0, +, −, 0, −, +)` | `(0, −, +, 0, +, −)` | 2 |
| `(0, 1, 1, 1, 0, 1)` | `y` | `(0, +, −, +, 0, −)` | `(0, −, +, −, 0, +)` | 2 |
| `(0, 1, 1, 1, 1, 0)` | `y` | `(0, −, −, +, +, 0)` | `(0, +, +, −, −, 0)` | 2 |
| `(1, 0, 0, 1, 1, 1)` | `z` | `(+, 0, 0, −, −, +)` | `(−, 0, 0, +, +, −)` | 2 |
| `(1, 0, 1, 0, 1, 1)` | `z` | `(−, 0, +, 0, −, +)` | `(+, 0, −, 0, +, −)` | 2 |
| `(1, 0, 1, 1, 0, 1)` | `y` | `(−, 0, −, +, 0, +)` | `(+, 0, +, −, 0, −)` | 2 |
| `(1, 0, 1, 1, 1, 0)` | `y` | `(+, 0, −, +, −, 0)` | `(−, 0, +, −, +, 0)` | 2 |
| `(1, 1, 0, 1, 0, 1)` | `x` | `(−, +, 0, −, 0, +)` | `(+, −, 0, +, 0, −)` | 2 |
| `(1, 1, 0, 1, 1, 0)` | `x` | `(−, +, 0, +, −, 0)` | `(+, −, 0, −, +, 0)` | 2 |
| `(1, 1, 1, 0, 0, 1)` | `x` | `(−, +, +, 0, 0, −)` | `(+, −, −, 0, 0, +)` | 2 |
| `(1, 1, 1, 0, 1, 0)` | `x` | `(−, +, −, 0, +, 0)` | `(+, −, +, 0, −, 0)` | 2 |

This `f` is not lex-first: it disagrees with the lex-first completion on
12 of the 24 pairs. Lex-first still scores `N_commute=288/576`. The
present residual is not leftover of bitenc (lex-first).

A commuting witness on `σ = (0, 1, 0, 1, 1, 1)`, `b = 0`,
`f(σ,b) = (0, −, 0, +, −, +)` is

`g : (x, y, z) ↦ (−y, x, z)`,

which sends the pair to `σ_g = (1, 0, 0, 1, 1, 1)`, `b_g = 0`, and
`f(σ_g, b_g) = g · f(σ,b)`
both equal `(+, 0, 0, −, −, +)`. The same `g` is the bitenc failing
rotate of the lex-first completion `(0, +, 0, −, −, +)`.

The leftover two slots do not need a second extra: the orientation of
the leftover frame relative to the full-axis `+` letter already names
one completion in each pair, and that naming is `G+`-equivariant.

## Theorem 3 — displayed, not adopted

The 48-completion census, `N_orbits = 2`, `N_section = 2`, the
576-triple census, `N_commute = 576`, the leftover-frame-positive table,
and the conclusion that an equivariant section exists are displayed
member data. They are not the framework's fixed Admissibility rule. This
note does not write `f` into Admissibility.
Do not write a section into Admissibility. Do not attach L1.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 12 perpendicular weight-4 masks, the
  `24 × 2` pair-completions form `N_orbits = 2` orbits under `G+`, a
  section can pick one point per `(σ,b)` orbit-consistently,
  `N_section = 2`, and the leftover-frame-positive section (not
  lex-first) has `N_commute = 576` of `12 × 2 × 24 = 576`.
- **What is displayed only.** The section `f` and the commute count are
  one rival table. They are not adopted.
- **What is not claimed.** No attachment of `f`, the leftover-frame
  sign, the age bit, opposite letters, or a unique full axis to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no leftover of bitenc (lex-first); no
  compiler no-go.
- **Mutation controls.** A rebuilt `N_orbits ≠ 2` fails. A rebuilt
  `N_section = 0` fails. A rebuilt `N_commute ≠ 576` fails. A rebuilt
  denominator other than 576 fails. A rebuilt section equal to
  lex-first fails. A rebuilt lex-first commute other than 288 fails. A
  note that writes a section into Admissibility, attaches L1, or authors
  an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 12 perpendicular weight-4 occupancy
masks, the 24 proper cube rotations, July-3 pair members on
`{0, +, −}`, the opposite-letter write on the unique full axis, the two
completions of each `(σ,b)`, the `G+` orbits, the leftover-frame-positive
section `f(σ,b)`, `N_orbits`, `N_section`, the transported bit `b_g`,
the 576-triple commute count, the lex-first commute count, the current
premise boundary, and the mutation controls. It scores the 12 masks and
`G+`. It writes no cache and authors no audit verdict.

---
claim_id: full_axis_age_bit_encoding_equivariance_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 12 perpendicular weight-4 masks, whether encoding the age bit as opposite letters on the full axis yields a G+-equivariant pair labeling is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/full_axis_age_bit_encoding_equivariance_2026_08_15.py
---

# Age-Bit Encoding On The Occupancy-Named Full Axis Under G+ (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 perpendicular weight-4 occupancy masks on the 6-NN star.
For each mask `σ` and each older-end bit `b ∈ {0,1}` on the unique full
axis, `f(σ,b)` writes opposite letters on that axis according to `b`
(older end `−`, younger `+`) and takes the unique, or else lex-first,
completion of the other two occupied slots to a July-3 pair member.
Score those 12 masks and `G+`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/full_axis_age_bit_encoding_equivariance_2026_08_15.py`](../scripts/full_axis_age_bit_encoding_equivariance_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment bitlaw: the lex-first pair member of `support(σ)` is independent
of `b`, so `f(σ,0)=f(σ,1)` and `N_commute=144/576`. That residual is not
leftover of bitlaw (lex-first ignored `b`). New residual: define `f(σ,b)`
by writing opposite letters on the occupancy-named full axis according to
`b` (older end `−`, younger `+`), then the unique or lex-first completion
to a July-3 pair member. Then recompute `N_commute/576`.

**Theorem 1.** A pair completion exists for both bits on each of the 12.
No `(σ, b)` has a unique completion: each has exactly two. The rule
therefore takes the lex-first of those two. `N_complete / 24 = 24/24`.

**Theorem 2.** `N_commute / 576 = 288/576`. Whether `N_commute=576`: it is
not. Encoding the age bit as opposite letters on the full axis does not
yield a `G+`-equivariant pair labeling.

**Theorem 3.** Displayed, not adopted. Do not write `f` into Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither `f` nor any full-axis opposite-letter encoding
of the age bit as the framework's fixed rule. The covariance clause is the
reason a local labeling on the orbit of `(σ, b)` must be checked under
`G+`. Formation site and rate remain outside the axiom memo. Qubit
remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 12 perpendicular weight-4 masks times two age bits: N_complete=24 of 24, and times the 24 proper cube rotations: N_commute=288 of 576. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: full_axis_age_bit_encoding_equivariance
target_blocker_text: "on the 12 perpendicular weight-4 masks, whether encoding the age bit as opposite letters on the full axis yields a G+-equivariant pair labeling"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_complete and N_commute on the 12 masks; do not write f into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 perpendicular weight-4 masks; N_complete=24 of 24; N_commute=288 of 576; not the full 576; displayed, not adopted"
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
`b=1`, and the swap if `b=0`. Empty slots are `0`. Complete the other
two occupied slots to a pair member if unique; else take the lex-first
among completions.

Displayed ticks realizing `(σ, b)` put the older end of the unique full
axis at tick 1 and the newer end at tick 2 when `b = 1`, and the reverse
when `b = 0`. Occupied slots off that axis carry tick 0. Empty slots
carry no tick. The transported bit is the older-end bit of `g · t` on
the unique full axis of `g · σ`. The commute identity is

`f(g · σ, b_g) = g · f(σ,b)`.

Score the 12 masks and `G+`. The completion denominator is `12 × 2 = 24`.
The commute denominator is `12 × 2 × 24 = 576`.

## Theorem 1 — pair completion exists for both bits; `N_complete / 24 = 24/24`

| `σ` | unique full axis | both bits | `f(σ,0)` | `f(σ,1)` | completions each bit |
| --- | --- | --- | --- | --- | --- |
| `(0, 1, 0, 1, 1, 1)` | `z` | yes | `(0, +, 0, −, −, +)` | `(0, +, 0, −, +, −)` | 2 |
| `(0, 1, 1, 0, 1, 1)` | `z` | yes | `(0, +, −, 0, −, +)` | `(0, +, −, 0, +, −)` | 2 |
| `(0, 1, 1, 1, 0, 1)` | `y` | yes | `(0, +, −, +, 0, −)` | `(0, +, +, −, 0, −)` | 2 |
| `(0, 1, 1, 1, 1, 0)` | `y` | yes | `(0, +, −, +, −, 0)` | `(0, +, +, −, −, 0)` | 2 |
| `(1, 0, 0, 1, 1, 1)` | `z` | yes | `(+, 0, 0, −, −, +)` | `(+, 0, 0, −, +, −)` | 2 |
| `(1, 0, 1, 0, 1, 1)` | `z` | yes | `(+, 0, −, 0, −, +)` | `(+, 0, −, 0, +, −)` | 2 |
| `(1, 0, 1, 1, 0, 1)` | `y` | yes | `(+, 0, −, +, 0, −)` | `(+, 0, +, −, 0, −)` | 2 |
| `(1, 0, 1, 1, 1, 0)` | `y` | yes | `(+, 0, −, +, −, 0)` | `(+, 0, +, −, −, 0)` | 2 |
| `(1, 1, 0, 1, 0, 1)` | `x` | yes | `(−, +, 0, +, 0, −)` | `(+, −, 0, +, 0, −)` | 2 |
| `(1, 1, 0, 1, 1, 0)` | `x` | yes | `(−, +, 0, +, −, 0)` | `(+, −, 0, +, −, 0)` | 2 |
| `(1, 1, 1, 0, 0, 1)` | `x` | yes | `(−, +, +, 0, 0, −)` | `(+, −, +, 0, 0, −)` | 2 |
| `(1, 1, 1, 0, 1, 0)` | `x` | yes | `(−, +, +, 0, −, 0)` | `(+, −, +, 0, −, 0)` | 2 |

`N_complete = 24`. A pair completion exists for both bits on each of
the 12, so `N_complete / 24 = 24/24`. No completion is unique. The
lex-first of the two completions is used, and `f(σ,0) ≠ f(σ,1)` on
every mask: the opposite-letter write on the full axis depends on `b`.

## Theorem 2 — `N_commute / 576 = 288/576`; not the full 576

Whether `N_commute=576`. It is not. `N_commute = 288` of the 576
triples `(σ, b, g)`. Each of the 12 masks contributes 24 commuting
`(b, g)` pairs of 48, so `N_commute / 576 = 288/576`. Encoding the age
bit as opposite letters on the full axis is not a `G+`-equivariant
pair labeling.

A commuting witness on `σ = (0, 1, 0, 1, 1, 1)`, `b = 0`,
`f(σ,b) = (0, +, 0, −, −, +)` is

`g : (x, y, z) ↦ (−x, −y, z)`,

which sends the pair to `σ_g = (1, 0, 1, 0, 1, 1)`, `b_g = 0`, and both
sides equal `(+, 0, −, 0, −, +)`.

A failing witness on the same `(σ, b)` is

`g : (x, y, z) ↦ (−y, x, z)`,

which sends the pair to `σ_g = (1, 0, 0, 1, 1, 1)`, `b_g = 0`, with

`f(σ_g, b_g) = (+, 0, 0, −, −, +)`
and
`g · f(σ,b) = (−, 0, 0, +, −, +)`.

The full-axis letters travel with `b`. The lex-first choice among the
two completions of the remaining occupied slots does not.

This is a labeling residual, not leftover of bitlaw (lex-first ignored
`b`). Bitlaw scored the occupancy-only lex-first section and found
`N_commute=144/576` because `f(σ,0)=f(σ,1)`. The present `f` depends on
`b` and raises the commute count to `288/576`. It still is not the
full 576.

## Theorem 3 — displayed, not adopted

The 24-pair completion census, `N_complete = 24`, the 576-triple
census, `N_commute = 288`, the 288/576 ratio, the failing rotate of the
lex-first completion, and the conclusion that the opposite-letter
encoding is not a `G+`-equivariant pair labeling are displayed member
data. They are not the framework's fixed Admissibility rule. This note
does not write `f` into Admissibility.
Do not write `f` into Admissibility. Do not attach L1.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 12 perpendicular weight-4 masks, a pair
  completion exists for both bits, `N_complete = 24` of `12 × 2 = 24`,
  and `N_commute = 288` of `12 × 2 × 24 = 576`. Encoding the age bit as
  opposite letters on the full axis does not yield a `G+`-equivariant
  pair labeling. Each `(σ, b)` has two completions, so `f` is the
  lex-first, and `f(σ,0) ≠ f(σ,1)`.
- **What is displayed only.** The rule `f` and the commute count are
  one rival table. They are not adopted.
- **What is not claimed.** No attachment of `f`, the age bit, opposite
  letters, or a unique full axis to Admissibility; no attachment of
  occupancy-only formation; no axiom edit; no formation rate; no leftover
  of bitlaw (lex-first ignored `b`); no compiler no-go.
- **Mutation controls.** A rebuilt `N_complete ≠ 24` fails. A rebuilt
  `N_commute ≠ 288` fails. A rebuilt denominator other than 576 fails.
  A rebuilt `N_commute = 576` fails the Theorem 2 report. A rebuilt
  perp mask without a pair completion for both bits fails. A note that
  writes `f` into Admissibility, attaches L1, or authors an audit
  verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 12 perpendicular weight-4 occupancy
masks, the 24 proper cube rotations, July-3 pair members on
`{0, +, −}`, the opposite-letter write on the unique full axis, the
lex-first pair completion `f(σ,b)`, `N_complete / 24`, the transported
bit `b_g`, the 576-triple commute count, the current premise boundary,
and the mutation controls. It scores the 12 masks and `G+`. It writes
no cache and authors no audit verdict.

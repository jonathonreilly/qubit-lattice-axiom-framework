---
claim_id: full_axis_one_bit_rule_equivariance_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 12 perpendicular weight-4 masks, whether the occupancy-named-axis one-bit pair labeling is G+-equivariant is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/full_axis_one_bit_rule_equivariance_2026_08_15.py
---

# Occupancy-Named-Axis One-Bit Pair Labeling Under G+ (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 perpendicular weight-4 occupancy masks on the 6-NN star.
For each mask `σ` and each older-end bit `b ∈ {0,1}` on the unique full
axis, `f(σ,b)` is the lex-first July-3 pair member with support `σ`
invariant under `Stab(σ,b)`. Score those 12 masks and `G+`. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/full_axis_one_bit_rule_equivariance_2026_08_15.py`](../scripts/full_axis_one_bit_rule_equivariance_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqaxis: on all 12 perp masks, occupancy names the full axis;
one age bit kills `Stab`. That census is a 15-mask split. The residual
here is not leftover of uneqlaw (one host) or uneqaxis (census). New
residual: the rule `f(σ,b) =` pair-member (lex-first Stab-ok) is
`G+`-equivariant,

`f(g · σ, b ∘ g^{-1}) = g · f(σ,b)`,

on those 12.

**Theorem 1.** `N_commute / (12 × 2 × 24) = 144/576`. Exactly 144 of the
576 triples `(σ, b, g)` satisfy `f(g · σ, b_g) = g · f(σ,b)`, where `b_g`
is the bit transported by `g`.

**Theorem 2.** Whether that count is the full 576. `N_commute = 144` is
not the full 576. The occupancy-named-axis one-bit pair labeling is not
cube-covariant as a labeling.

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

Admissibility names neither `f` nor any occupancy-named-axis one-bit pair
labeling as the framework's fixed rule. The covariance clause is the
reason a local labeling on the orbit of `(σ, b)` must be checked under
`G+`. Formation site and rate remain outside the axiom memo. Qubit
remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of the 12 perpendicular weight-4 masks times two age bits times the 24 proper cube rotations: N_commute=144 of 576. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: full_axis_one_bit_rule_equivariance
target_blocker_text: "on the 12 perpendicular weight-4 masks, whether the occupancy-named-axis one-bit pair labeling is G+-equivariant"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_commute on the 12 masks; do not write f into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 perpendicular weight-4 masks; N_commute=144 of 576; not the full 576; displayed, not adopted"
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

July-3 pair members are the 6-slot 3-letter colorings whose `G+` orbit
is sent to a different orbit by spatial inversion. There are 48 such
members. Each of the 12 masks is the support of exactly four of them.

Displayed ticks realizing `(σ, b)` put the older end of the unique full
axis at tick 1 and the newer end at tick 2 when `b = 1`, and the reverse
when `b = 0`. Occupied slots off that axis carry tick 0. Empty slots
carry no tick.

`b = 1` if the minus-end tick is strictly smaller than the plus-end
tick, else `0`.

`Stab(σ,b) = { g in G+ : g · σ = σ and b(g · t) = b(t) }`.

`f(σ,b)` is the lex-first July-3 pair member with support `σ` invariant
under `Stab(σ,b)`. On each of the 12, `|Stab(σ,b)| = 1` for both bits,
so all four pair members with support `σ` are Stab-ok, and `f(σ,0) =
f(σ,1)` is the lex-first of those four.

For `g` in `G+` the transported bit is

`b_g = b ∘ g^{-1}`,

computed as the older-end bit of `g · t` on the unique full axis of
`g · σ`. The commute identity is

`f(g · σ, b_g) = g · f(σ,b)`.

Score the 12 masks and `G+`. The denominator is `12 × 2 × 24 = 576`.

## Theorem 1 — `N_commute / (12 × 2 × 24) = 144/576`

| `σ` | unique full axis | `f(σ,0) = f(σ,1)` | commute count of 48 |
| --- | --- | --- | --- |
| `(0, 1, 0, 1, 1, 1)` | `z` | `(0, 1, 0, 2, 1, 2)` | 12 |
| `(0, 1, 1, 0, 1, 1)` | `z` | `(0, 1, 2, 0, 1, 2)` | 12 |
| `(0, 1, 1, 1, 0, 1)` | `y` | `(0, 1, 1, 2, 0, 2)` | 12 |
| `(0, 1, 1, 1, 1, 0)` | `y` | `(0, 1, 1, 2, 2, 0)` | 12 |
| `(1, 0, 0, 1, 1, 1)` | `z` | `(1, 0, 0, 2, 1, 2)` | 12 |
| `(1, 0, 1, 0, 1, 1)` | `z` | `(1, 0, 2, 0, 1, 2)` | 12 |
| `(1, 0, 1, 1, 0, 1)` | `y` | `(1, 0, 1, 2, 0, 2)` | 12 |
| `(1, 0, 1, 1, 1, 0)` | `y` | `(1, 0, 1, 2, 2, 0)` | 12 |
| `(1, 1, 0, 1, 0, 1)` | `x` | `(1, 2, 0, 1, 0, 2)` | 12 |
| `(1, 1, 0, 1, 1, 0)` | `x` | `(1, 2, 0, 1, 2, 0)` | 12 |
| `(1, 1, 1, 0, 0, 1)` | `x` | `(1, 2, 1, 0, 0, 2)` | 12 |
| `(1, 1, 1, 0, 1, 0)` | `x` | `(1, 2, 1, 0, 2, 0)` | 12 |

`N_commute = 144`. Each of the 12 masks contributes 12 commuting
`(b, g)` pairs of 48, so `N_commute / (12 × 2 × 24) = 144/576`.

A commuting witness on `σ = (0, 1, 0, 1, 1, 1)`, `b = 0`,
`f(σ,b) = (0, 1, 0, 2, 1, 2)` is

`g : (x, y, z) ↦ (−x, −y, z)`,

which sends the pair to `σ_g = (1, 0, 1, 0, 1, 1)`, `b_g = 0`, and both
sides equal `(1, 0, 2, 0, 1, 2)`.

A failing witness on the same `(σ, b)` is

`g : (x, y, z) ↦ (−x, y, −z)`,

which sends the pair to `σ_g = (1, 0, 0, 1, 1, 1)`, `b_g = 1`, with

`f(σ_g, b_g) = (1, 0, 0, 2, 1, 2)`
and
`g · f(σ,b) = (1, 0, 0, 2, 2, 1)`.

Lex-first choice on the image support is not the rotate of the lex-first
choice on the source support.

## Theorem 2 — the count is not the full 576

Whether that count is the full 576. It is not. `N_commute = 144` is not
the full 576. Because `|Stab(σ,b)| = 1`, `f` does not depend on `b`: it
is the lex-first pair member of the occupancy support alone. That
lex-first section of the July-3 pair over the 12 masks does not commute
with `G+`. The occupancy-named-axis one-bit pair labeling is not
cube-covariant as a labeling.

This is a labeling residual, not leftover of uneqlaw (one host) or
uneqaxis (census). Uneqlaw scored tick-ok membership of one rotated
host. Uneqaxis scored whether occupancy names the axis. Neither scored
whether the lex-first Stab-ok pair member is a `G+`-equivariant section
on all 12.

## Theorem 3 — displayed, not adopted

The 576-triple census, `N_commute = 144`, the 144/576 ratio, the
failing rotate of the lex-first section, and the conclusion that the
occupancy-named-axis one-bit pair labeling is not cube-covariant as a
labeling are displayed member data. They are not the framework's fixed
Admissibility rule. This note does not write `f` into Admissibility.
Do not write `f` into Admissibility. Do not attach L1.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 12 perpendicular weight-4 masks,
  `N_commute = 144` of `12 × 2 × 24 = 576`. The occupancy-named-axis
  one-bit pair labeling is not cube-covariant as a labeling. Each of
  the 12 has `|Stab(σ,b)| = 1` and four Stab-ok pair members for both
  bits, so `f(σ,0) = f(σ,1)`.
- **What is displayed only.** The rule `f` and the commute count are
  one rival table. They are not adopted.
- **What is not claimed.** No attachment of `f`, the age bit, or a
  unique full axis to Admissibility; no attachment of occupancy-only
  formation; no axiom edit; no formation rate; no leftover of uneqlaw
  (one host) or uneqaxis (census); no compiler no-go.
- **Mutation controls.** A rebuilt `N_commute ≠ 144` fails. A rebuilt
  denominator other than 576 fails. A rebuilt `N_commute = 576` fails
  the Theorem 2 report. A rebuilt perp mask without a defined `f`
  fails. A note that writes `f` into Admissibility, attaches L1, or
  authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 12 perpendicular weight-4 occupancy
masks, the 24 proper cube rotations, July-3 pair members, displayed
ticks for each `(σ, b)`, `Stab(σ,b)`, the lex-first Stab-ok pair
member `f(σ,b)`, the transported bit `b_g`, the 576-triple commute
count, the current premise boundary, and the mutation controls. It
scores the 12 masks and `G+`. It writes no cache and authors no audit
verdict.

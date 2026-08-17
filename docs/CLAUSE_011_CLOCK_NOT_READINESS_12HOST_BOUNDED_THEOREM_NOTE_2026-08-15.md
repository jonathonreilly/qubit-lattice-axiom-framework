---
claim_id: clause_011_clock_not_readiness_12host_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 12 perp-mask hosts, leftover-frame fire is scored with the (0,1,1) hop-cost as a label versus as a readiness filter. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_clock_not_readiness_12host_2026_08_15.py
---

# Clause (0,1,1) Hop-Cost As Clock, Not Readiness, On 12 Hosts (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 lex-first realizing 3-ball hosts of the perpendicular
weight-4 occupancy masks from bitall. On each host, leftover-frame-positive
`f` is scored with the named clause-toggle hop cost `(0,1,1)` as unused
edge labels versus as a cost-1 readiness filter. Report `N_label_fire`
and `N_filt_fire`. The 12 lex-first perp-mask hosts only. Uniqueness is
not required. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_clock_not_readiness_12host_2026_08_15.py`](../scripts/clause_011_clock_not_readiness_12host_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment: `(0,1,1)` is the other reverser (varrev). `ν` as filter fires
12/12. New residual: leftover-frame fire with `(0,1,1)` as unused labels
and as a cost-1 filter on the 12 perp-mask hosts. A cheaper reverser is
only a matching member if fire 10→survives. Uniqueness not required. Do
not attach L1.

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The 12 rows are the bitall / bitreal Theorem 2 hosts: for each
perpendicular weight-4 mask, the lex-first `(centers, radii, v)` whose
unread 6-NN occupancy equals that mask. On each host, `t` is the
seed-radii ℓ¹ lock tick on occupied neighbors, `b` is read from the
unique full axis, and `f` is the leftover-frame-positive July-3 pair
member of `(σ,b)`.

`f` is the leftover-frame-positive pair section. Write `|σ_x|` for the
number of nonzero coordinates of `x ∈ Z^3`. The named clause triple
`(s,a,d)=(0,1,1)` from varrev costs `3` if the enabled clauses fire,
else `1`. Seed-exit is off. Both-weights-`1` and support drop are on.
Therefore

`(0,1,1)(v→w) = 3` if `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

Cost `3` iff both weights `1` or support drop, else `1`. Seed-exit is
cheap.

**Theorem 1.** On each of the 12 lex-first realizing hosts, `f` with
`(0,1,1)` as unused labels has `N_new = 1`. `N_label_fire = 12`. Then
fire survives labels on every host.

**Theorem 2.** On each of those 12, `f` with fire restricted to cost-1
edges has `N_new`. `N_filt_fire = 12`. Displayed, not adopted.

**Theorem 3.** Displayed, not adopted. Do not write `f` or `(0,1,1)` into
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

Admissibility names neither leftover-frame-positive `f` nor the named
`(0,1,1)` hop cost as the framework's fixed rule. Record permanence
is used only to keep the locks on each `U`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact 12-host score of leftover-frame-positive f with the (0,1,1) hop-cost as unused labels versus as a cost-1 readiness filter: N_label_fire=12 and N_filt_fire=12. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: clause_011_clock_not_readiness_12host
target_blocker_text: "on all 12 perp-mask realizing hosts, leftover-frame fire with (0,1,1) as unused labels versus as a cost-1 readiness filter"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_label_fire and N_filt_fire on the 12 lex-first hosts; do not write f or (0,1,1) into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 lex-first realizing hosts; N_label_fire=12; N_filt_fire=12; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Slots are `(+x, −x, +y, −y, +z, −z)`. Occupancy at an unread site `v`
relative to a locked set `U` is the 6-bit indicator

`σ(U, v)_μ = 1` if and only if `v + e_μ ∈ U`.

A weight-4 mask is perpendicular when the two emptied slots lie on two
distinct axes. The 12 perpendicular masks, in lex order, are

`(0, 1, 0, 1, 1, 1)`,
`(0, 1, 1, 0, 1, 1)`,
`(0, 1, 1, 1, 0, 1)`,
`(0, 1, 1, 1, 1, 0)`,
`(1, 0, 0, 1, 1, 1)`,
`(1, 0, 1, 0, 1, 1)`,
`(1, 0, 1, 1, 0, 1)`,
`(1, 0, 1, 1, 1, 0)`,
`(1, 1, 0, 1, 0, 1)`,
`(1, 1, 0, 1, 1, 0)`,
`(1, 1, 1, 0, 0, 1)`,
`(1, 1, 1, 0, 1, 0)`.

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. Each host is a 3-ball
union in the uneqrad box

`U = B_{r1}(s1) ∪ B_{r2}(s2) ∪ B_{r3}(s3)`

with distinct `si` in `[−2,2]³` and `(r1,r2,r3) ∈ {1,2,3}³` not all
equal, together with an unread site `v ∉ U`, `‖v‖_∞ ≤ 4`, whose
occupancy is the named mask. The twelve hosts are the bitall / bitreal
Theorem 2 lex-first rows.

On occupied nearest neighbors the seed-radii ℓ¹ lock tick is

`t(w) = min_i ‖w − si‖_1`.

Empty slots have no tick. Local data is `(σ, t)`. The unique full axis
is the unique axis with both slots occupied. The age bit is

`b = [t(−axis) < t(+axis)]`.

Letters are `{0, +, −}` with `0` empty. Encode `0 ↦ 0`, `+ ↦ 1`,
`− ↦ 2`. Completions of `(σ,b)` are the two July-3 pair members that
match occupancy `σ` and write opposite letters on the full axis
according to `b`. The leftover-frame sign of a completion is the
determinant of the ordered triple of directions (leftover `+`, leftover
`−`, full-axis `+` letter). The section `f` takes the unique completion
of sign `+1`. A displayed pair step at an unread site forms that site
if and only if the encoded 6-tuple lies in the pair; existing locks are
not removed. `N_new = 1` and `U` persists exactly when that step forms
`v` and leaves every lock of `U` in place.

On a directed nearest-neighbor edge `x → y`,

`(0,1,1)(x → y) = 3` if `(|σ_x|=|σ_y|=1)` or `|σ_y| < |σ_x|`,
else `1`,

where `|σ_x|` is the number of nonzero coordinates of `x`. Both weights
`1` means both coordinate supports equal `1`. Support drop means the
target support is strictly smaller than the source support.

Assigning `(0,1,1)` as unused labels writes those costs on already-present
directed edges. It does not rewrite which neighbors of `v` lie in `U`,
and it does not rewrite the lock-ticks `t(w)`. Therefore `(σ,b)` and
leftover-frame-positive `f(σ,b)` are the same as in the bitall census.
`N_label_fire` is how many of the 12 hosts still have `N_new = 1` and
`U` persisting after that unused labeling.

If `(0,1,1)` is instead used as a readiness filter, an occupied neighbor
participates in the pair step only when the directed edge from that
neighbor to `v` has cost `1`. The filtered occupancy is `σ_ready`.
Leftover-frame-positive `f` is then evaluated on `(σ_ready, b)` when
`σ_ready` still has a unique full axis, and is undefined otherwise.
`N_filt_fire` is how many of the 12 hosts have `N_new = 1` under that
filter.

The 12 lex-first perp-mask hosts only.

## Theorem 1 — unused labels; `N_label_fire = 12`

Each bitall Theorem 2 row rebuilds: the three ℓ¹ balls with the named
centers and radii have unread center `v`, and the 6-NN occupancy of `v`
equals the named mask. Assigning `(0,1,1)` as unused labels does not
change the occupancy mask or the age bit, so leftover-frame-positive `f`
is the same section as in bitall. Each `f` is a July-3 pair member, each
`v` is unread, the displayed pair step forms exactly that `v`
(`N_new = 1`), and no lock of `U` is removed, so `U` persists.
Therefore

`N_label_fire = 12`.

Fire survives labels on every host. A cheaper reverser is only a
matching member if fire 10→survives; unused labels survive on every
host.

The twelve hosts are

| `σ` | lex-first `(centers, radii, v)` |
|---|---|
| `(0, 1, 0, 1, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-1, -1, -1))` |
| `(0, 1, 1, 0, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-1, -3, -1))` |
| `(0, 1, 1, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 1, 2), (-1, -1, -1))` |
| `(0, 1, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-1, -1, -2))` |
| `(1, 0, 0, 1, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-3, -1, -1))` |
| `(1, 0, 1, 0, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-3, -3, -1))` |
| `(1, 0, 1, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 1, 2), (-3, -1, -1))` |
| `(1, 0, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-3, -1, -2))` |
| `(1, 1, 0, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 1, 2), (-1, -1, -1))` |
| `(1, 1, 0, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -1, -2))` |
| `(1, 1, 1, 0, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 1, 2), (-1, -3, -1))` |
| `(1, 1, 1, 0, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -3, -2))` |

The twelve label-fire rows are

| `σ` | axis | `t` | `b` | `f(σ,b)` | `N_new` |
|---|---|---|---|---|---|
| `(0, 1, 0, 1, 1, 1)` | `z` | `(·, 1, ·, 1, 2, 2)` | `0` | `(0, −, 0, +, −, +)` | `1` |
| `(0, 1, 1, 0, 1, 1)` | `z` | `(·, 1, 1, ·, 2, 2)` | `0` | `(0, +, −, 0, −, +)` | `1` |
| `(0, 1, 1, 1, 0, 1)` | `y` | `(·, 1, 2, 1, ·, 2)` | `1` | `(0, −, +, −, 0, +)` | `1` |
| `(0, 1, 1, 1, 1, 0)` | `y` | `(·, 1, 1, 1, 2, ·)` | `0` | `(0, −, −, +, +, 0)` | `1` |
| `(1, 0, 0, 1, 1, 1)` | `z` | `(1, ·, ·, 1, 2, 2)` | `0` | `(+, 0, 0, −, −, +)` | `1` |
| `(1, 0, 1, 0, 1, 1)` | `z` | `(1, ·, 1, ·, 2, 2)` | `0` | `(−, 0, +, 0, −, +)` | `1` |
| `(1, 0, 1, 1, 0, 1)` | `y` | `(1, ·, 2, 1, ·, 2)` | `1` | `(+, 0, +, −, 0, −)` | `1` |
| `(1, 0, 1, 1, 1, 0)` | `y` | `(1, ·, 1, 1, 2, ·)` | `0` | `(+, 0, −, +, −, 0)` | `1` |
| `(1, 1, 0, 1, 0, 1)` | `x` | `(2, 1, ·, 1, ·, 2)` | `1` | `(+, −, 0, +, 0, −)` | `1` |
| `(1, 1, 0, 1, 1, 0)` | `x` | `(1, 1, ·, 1, 2, ·)` | `0` | `(−, +, 0, +, −, 0)` | `1` |
| `(1, 1, 1, 0, 0, 1)` | `x` | `(2, 1, 1, ·, ·, 2)` | `1` | `(+, −, −, 0, 0, +)` | `1` |
| `(1, 1, 1, 0, 1, 0)` | `x` | `(1, 1, 1, ·, 2, ·)` | `0` | `(−, +, −, 0, +, 0)` | `1` |

This is not leftover of nuclk. nuclk scored noshrt `ν` (seed-exit or
both weights `1` or support drop) and `ν` as filter fires 12/12. The
present score puts the cheaper reverser `(0,1,1)` in that same
label-versus-filter split.

## Theorem 2 — cost-1 readiness filter; `N_filt_fire = 12`

If `(0,1,1)` is instead used as a readiness filter, fire is restricted
to cost-1 incoming edges. On every one of the 12 hosts the unread center
has coordinate support `3`, and every occupied neighbor has coordinate
support `2` or `3`. Both-weights-`1` never occurs. Support drop never
occurs toward that center. Therefore every incoming `(0,1,1)` cost is
`1`, `σ_ready = σ`, and leftover-frame-positive `f` still fires
`N_new = 1`. Therefore

`N_filt_fire = 12`.

The twelve filter rows are

| `σ` | incoming `(0,1,1)` | `σ_ready` | unique full axis of `σ_ready` | `N_new` |
|---|---|---|---|---|
| `(0, 1, 0, 1, 1, 1)` | `(1, 1, 1, 1)` | `(0, 1, 0, 1, 1, 1)` | `z` | `1` |
| `(0, 1, 1, 0, 1, 1)` | `(1, 1, 1, 1)` | `(0, 1, 1, 0, 1, 1)` | `z` | `1` |
| `(0, 1, 1, 1, 0, 1)` | `(1, 1, 1, 1)` | `(0, 1, 1, 1, 0, 1)` | `y` | `1` |
| `(0, 1, 1, 1, 1, 0)` | `(1, 1, 1, 1)` | `(0, 1, 1, 1, 1, 0)` | `y` | `1` |
| `(1, 0, 0, 1, 1, 1)` | `(1, 1, 1, 1)` | `(1, 0, 0, 1, 1, 1)` | `z` | `1` |
| `(1, 0, 1, 0, 1, 1)` | `(1, 1, 1, 1)` | `(1, 0, 1, 0, 1, 1)` | `z` | `1` |
| `(1, 0, 1, 1, 0, 1)` | `(1, 1, 1, 1)` | `(1, 0, 1, 1, 0, 1)` | `y` | `1` |
| `(1, 0, 1, 1, 1, 0)` | `(1, 1, 1, 1)` | `(1, 0, 1, 1, 1, 0)` | `y` | `1` |
| `(1, 1, 0, 1, 0, 1)` | `(1, 1, 1, 1)` | `(1, 1, 0, 1, 0, 1)` | `x` | `1` |
| `(1, 1, 0, 1, 1, 0)` | `(1, 1, 1, 1)` | `(1, 1, 0, 1, 1, 0)` | `x` | `1` |
| `(1, 1, 1, 0, 0, 1)` | `(1, 1, 1, 1)` | `(1, 1, 1, 0, 0, 1)` | `x` | `1` |
| `(1, 1, 1, 0, 1, 0)` | `(1, 1, 1, 1)` | `(1, 1, 1, 0, 1, 0)` | `x` | `1` |

Unlike clkonly `ρ`, the named `(0,1,1)` hop cost does not drop any
occupied slot on these twelve hosts. The filter and the unused-label
score agree. Fire 10→survives as the cost-1 filter as well. Displayed,
not adopted.

## Theorem 3 — displayed, not adopted

The counts `N_label_fire = 12` and `N_filt_fire = 12`, the twelve
hosts, the unused-label fire rows, and the readiness-filter rows are
displayed member data. They are not the framework's fixed
Admissibility rule. This note does not write `f` or `(0,1,1)` into
Admissibility. Do not write f or (0,1,1) into Admissibility.
Do not attach L1. Occupancy-only formation is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.
Uniqueness not required.

## Honest-auditor / Boundary

- **What is proved.** On the 12 lex-first perp-mask realizing hosts,
  leftover-frame-positive `f` with `(0,1,1)` as unused labels has
  `N_new = 1` on every host, so `N_label_fire = 12`. Fire survives
  labels on every host. The same `f` with fire restricted to cost-1
  edges has `N_filt_fire = 12`.
- **What is displayed only.** The named `(0,1,1)` hop cost, the
  unused-label versus readiness-filter split, and both counts are one
  rival table. They are not adopted.
- **What is not claimed.** No attachment of `f` or `(0,1,1)` to
  Admissibility; no attachment of L1; no uniqueness of the matching
  member; no leftover of nuclk (`ν` as filter fires 12/12); no axiom
  edit; no formation rate; no compiler no-go.
- **Mutation controls.** A rebuilt `N_label_fire` other than 12
  fails. A rebuilt `N_filt_fire` other than 12 fails. A note that
  writes `f` or `(0,1,1)` into Admissibility, attaches L1, claims
  uniqueness, or authors an audit verdict fails.

This note authors no audit verdict.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| rebuild the 12 bitall lex-first hosts | closed; the twelve rows rebuild |
| score `f` with `(0,1,1)` as unused labels | closed by Theorem 1; each `N_new = 1` |
| report `N_label_fire` | closed by Theorem 1; `N_label_fire = 12` |
| keep the cheaper reverser only if fire 10→survives | closed; labels and filter both survive |
| score `f` with fire restricted to cost-1 edges | closed by Theorem 2 |
| report `N_filt_fire` | closed by Theorem 2; `N_filt_fire = 12` |
| treat the nuclk `ν` split as the `(0,1,1)` score | refused; not leftover of nuclk |
| write `f` or `(0,1,1)` into Admissibility | refused; Theorem 3 |
| attach L1 | refused; Theorem 3 |
| claim uniqueness | refused; uniqueness not required |

The obligation graph is acyclic. Adoption of `f` or of `(0,1,1)` is not a
proof leaf.

## What This Does Not Claim

- Do not write `f` or `(0,1,1)` into Admissibility.
- Do not attach L1.
- Uniqueness is not required and is not claimed.
- The comparison is not leftover of nuclk.
- The 12 lex-first perp-mask hosts only.
- No path-length law is attached.
- No Record readout is assigned to a site without a record.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> it does not supply the formation site, probability,
> or rate.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> A readout value is determined by record content alone.

> A site with no record cannot be read.

---
claim_id: same_host_agebit_hopcost_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the uneqrad breaker, leftover-frame fire and the named hop cost are scored on the same host. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/same_host_agebit_hopcost_2026_08_15.py
---

# Same-Host Leftover-Frame Fire And Named Hop Cost (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one host only, the uneqrad lex-first breaker
`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` and the unread
six-neighbor star at `v = (−3,−3,−1)`. Score leftover-frame-positive fire
`f` and the named hop cost `ρ` on this host. Uniqueness is not required.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/same_host_agebit_hopcost_2026_08_15.py`](../scripts/same_host_agebit_hopcost_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment ourmem scored leftover-frame fire on the uneqrad host and
hop-cost reverse on a second host. New residual: on the uneqrad
lex-first breaker, does the named hop-cost `ρ` change `N_new` of
leftover-frame `f`? A matching member must carry both extras on one
host. Uniqueness not required. Do not attach L1.

Host `U` is the uneqrad lex-first breaker. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Occupancy mask

`σ = (1, 0, 1, 0, 1, 1)`.

`f` is the leftover-frame-positive pair section. The named hop cost is

`ρ = 3` iff equal inward weight or seed-exit, else `1`.

Inward occupation at a site `x` uses the same seed-distance already
used for lock-ticks,

`d(x) = min_i ‖x − s_i‖_1`,

with a direction bit set exactly when the neighbor is strictly nearer
the nearest seed. Inward weight is the number of such bits. Seed-exit
means the source has inward weight `0`.

**Theorem 1.** On `U`, `f` still fires `N_new = 1` when hop costs are
ignored (bitfire).

**Theorem 2.** Assigning `ρ` to directed nearest-neighbor edges of `U`
does not change the occupancy mask or the age bit, so `f` still fires
`N_new = 1`. If `ρ` is instead used as a readiness filter (fire only
along cost-1 edges), the filtered occupancy is `σ_ready = (1, 0, 1, 0, 1, 0)`
and `N_new = 0`.

**Theorem 3.** Displayed, not adopted. Do not write `f` or `ρ` into
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

Admissibility names neither the leftover-frame-positive section nor any
numerical hop cost as the framework's fixed rule. Record permanence is
used only to keep the locks on `U`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact same-host score of leftover-frame-positive f and named hop-cost ρ on the uneqrad lex-first breaker: bitfire N_new=1, ρ does not change σ or b, and the cost-1 readiness filter reports N_new=0. Displayed report only."
trace_class: frontier_discovery
target_claim_id: same_host_agebit_hopcost
target_blocker_text: "on the uneqrad lex-first breaker, whether the named hop-cost ρ changes N_new of leftover-frame f"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of same-host f and ρ, including the readiness-filter N_new; do not write f or ρ into Admissibility or attach L1"
conditional_surface_status: "exact on the uneqrad lex-first breaker; bitfire N_new=1; ρ leaves σ and b unchanged so N_new=1; readiness filter N_new=0; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `s1 = (−2,−2,−2)`, `s2 = (−2,−2,−1)`, and `s3 = (−2,−2,1)`. The
closed ℓ¹ ball of radius `r` is

`B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`.

The locked set is the already-given unequal-radius union

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`.

The three balls have 25, 7, and 63 sites. Pairwise overlaps are 7, 7,
and 7, and the triple overlap has 7 sites, so `|U| = 81`. The unread
site is

`v = (−3,−3,−1)`.

Then `‖v − s1‖_1 = 3 > 2`, `‖v − s2‖_1 = 2 > 1`, and
`‖v − s3‖_1 = 4 > 3`, so `v ∉ U`.

The six nearest neighbors, in the declared order, are

| slot | neighbor | in `U` | lock tick | inward weight |
|---|---|---|---|---|
| `+x` | `(−2,−3,−1)` | yes | `1` | `1` |
| `−x` | `(−4,−3,−1)` | no | none | `2` |
| `+y` | `(−3,−2,−1)` | yes | `1` | `1` |
| `−y` | `(−3,−4,−1)` | no | none | `2` |
| `+z` | `(−3,−3,0)` | yes | `3` | `4` |
| `−z` | `(−3,−3,−2)` | yes | `2` | `2` |

Occupancy mask at `v`:

`σ = (1, 0, 1, 0, 1, 1)`.

On the four occupied slots the lock-tick list is

`t = (1, ·, 1, ·, 3, 2)`,

so `t(+x) = t(+y) = 1`, `t(+z) = 3`, and `t(−z) = 2`. Empty slots have
no tick. The unique full axis is `z`. The age bit is
`b = [t(−z) < t(+z)]`, hence `b = 1`. Letters are `{0, +, −}` with `0`
empty. Encode `0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`. The July-3 `k = 3` pair is
the unique pair of proper-cube orbits of 3-letter 6-tuples that are not
proper-equivalent to their inversion images. That set has 48 members.

Completions of `(σ,b)` are the pair members that match occupancy `σ`
and write `c(+z)=+`, `c(−z)=−` when `b = 1`. The leftover-frame sign of
a completion is the determinant of the ordered triple of directions
(leftover `+`, leftover `−`, full-axis `+` letter). The section `f`
takes the unique completion of sign `+1`. A displayed pair step at an
unread site forms that site if and only if the encoded 6-tuple lies in
the pair; existing locks are not removed.

Inward occupation at `x` is the 6-bit string whose direction bit is
set exactly when `d` of the neighbor is strictly less than `d(x)`. The
unread center has

`d(v) = 2`, inward occupancy `(1, 0, 1, 0, 0, 0)`, inward weight `2`.

On a directed nearest-neighbor edge `x → y`,

`ρ(x → y) = 3` if `|σ_in(x)| = |σ_in(y)|` or `|σ_in(x)| = 0`, else `1`.

The directed nearest-neighbor graph of `U` has 288 edges. Assigning
`ρ` labels those edges. It does not rewrite which neighbors of `v` lie
in `U`, and it does not rewrite the lock-ticks `t(w) = d(w)`.

The four occupied-neighbor edges into `v` receive

| edge | inward weights | `ρ` |
|---|---|---|
| `+x → v` | `(1, 2)` | `1` |
| `+y → v` | `(1, 2)` | `1` |
| `+z → v` | `(4, 2)` | `1` |
| `−z → v` | `(2, 2)` | `3` |

The `−z` edge is cost `3` because the inward weights are equal. A
readiness filter that fires only along cost-1 edges keeps the three
cost-1 occupied slots and drops `−z`, so

`σ_ready = (1, 0, 1, 0, 1, 0)`.

That mask has no unique full axis.

Score this uneqrad host only. One host only.

## Theorem 1 — hop costs ignored, `f` still fires

The unique full axis of `σ` is `z`. The bit `b = 1` writes `+` on `+z`
and `−` on `−z`. The two completions are

`(+, 0, −, 0, +, −)` and `(−, 0, +, 0, +, −)`.

The first has leftover `+` on `+x`, leftover `−` on `+y`, and full-axis
`+` on `+z`. That ordered triple of directions has determinant `+1`.
Therefore

`f(σ,b) = (+, 0, −, 0, +, −)`.

This 6-tuple lies in the 48-member July-3 pair. The center `v` is
unread. With hop costs ignored, the displayed pair step forms exactly
`v` (`N_new = 1`) and does not remove any lock of `U`. So `U`
persists. Same fire report as bitfire, now as the hop-cost-ignored
coordinate of the same-host pair.

## Theorem 2 — `ρ` as edge labels versus as a readiness filter

Assigning `ρ` to the 288 directed nearest-neighbor edges of `U` is a
labeling of already-present edges. Occupancy `σ` is the 6-bit
indicator of `U` at `v`. The age bit is `b = [t(−z) < t(+z)]` from
the lock-ticks `t(w) = d(w)`. Neither definition reads `ρ`. After the
labeling,

`σ = (1, 0, 1, 0, 1, 1)`, `b = 1`,

unchanged, so the same section `f(σ,b)` still fires `N_new = 1` and
`U` persists.

If `ρ` is instead used as a readiness filter, an occupied neighbor
participates in the pair step only when the directed edge from that
neighbor to `v` has cost `1`. The filtered occupancy is
`σ_ready = (1, 0, 1, 0, 1, 0)`. That 6-tuple has no unique full axis,
so leftover-frame-positive `f` is not defined on the filtered star.
The pair step does not form `v`. Under the filter,

`N_new = 0`.

Thus `ρ` as a mere labeling of `U` does not change `N_new` of `f`,
while `ρ` as a cost-1 readiness filter does: `N_new` drops from `1`
to `0`. A matching member that wants both extras on this host must
carry both and must say which of those two uses of `ρ` it means.
Uniqueness of that member is not required.

This residual is not leftover of ourmem (those two extras were scored
on two hosts) and is not leftover of bitfire (hop costs were ignored).

## Theorem 3 — displayed, not adopted

The same-host pair `(f, ρ)`, the unchanged `(σ, b)`, and the two
`N_new` reports are displayed member data. They are not the
framework's fixed Admissibility rule. This note does not write `f` or
`ρ` into Admissibility. Do not write f or ρ into Admissibility.
Do not attach L1. Occupancy-only formation is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first breaker, hop-cost-ignored
  leftover-frame-positive `f(σ,b) = (+, 0, −, 0, +, −)` fires with
  `N_new = 1` and `U` persists. Assigning `ρ` to directed
  nearest-neighbor edges of `U` leaves `σ` and `b` unchanged, so that
  same `f` still fires `N_new = 1`. Used as a cost-1 readiness filter,
  `ρ` yields `σ_ready = (1, 0, 1, 0, 1, 0)` and `N_new = 0`.
- **What is displayed only.** The same-host pair `(f, ρ)` and the two
  uses of `ρ` are one rival table. They are not adopted.
- **What is not claimed.** No attachment of `f` or `ρ` to
  Admissibility; no attachment of L1; no uniqueness of the matching
  member; no leftover of ourmem (two hosts) or of bitfire (hop costs
  ignored); no axiom edit; no formation rate; no compiler no-go; no
  second host.
- **Mutation controls.** A rebuilt `f(σ,b)` other than
  `(+, 0, −, 0, +, −)` fails. A rebuilt hop-cost-ignored `N_new ≠ 1`
  fails. A rebuilt `(σ, b)` after assigning `ρ` other than
  `((1, 0, 1, 0, 1, 1), 1)` fails. A rebuilt readiness-filter
  `N_new ≠ 0` or `σ_ready` other than `(1, 0, 1, 0, 1, 0)` fails. A
  note that writes `f` or `ρ` into Admissibility, attaches L1, claims
  uniqueness, scores a second host, or authors an audit verdict fails.

This note authors no audit verdict.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| name the uneqrad lex-first breaker and rebuild `f` | closed by Theorem 1 |
| report hop-cost-ignored `N_new` | closed by Theorem 1; `N_new = 1` |
| name `ρ` on inward weights of this host | closed: cost `3` iff equal inward weight or seed-exit |
| show `ρ` does not change `σ` or `b` | closed by Theorem 2 |
| report `N_new` after labeling `U` by `ρ` | closed by Theorem 2; `N_new = 1` |
| report readiness-filter `N_new` | closed by Theorem 2; `N_new = 0` |
| treat two-host pairing as the same-host score | refused; not leftover of ourmem |
| treat hop-cost-ignored fire as the same-host score | refused; not leftover of bitfire |
| write `f` or `ρ` into Admissibility | refused; Theorem 3 |
| attach L1 | refused; Theorem 3 |
| claim uniqueness | refused; uniqueness not required |

The obligation graph is acyclic. Adoption of `f` or of `ρ` is not a
proof leaf.

## What This Does Not Claim

- Do not write `f` or `ρ` into Admissibility.
- Do not attach L1.
- Uniqueness is not required and is not claimed.
- The comparison is not leftover of ourmem (two hosts).
- The comparison is not leftover of bitfire (hop costs ignored).
- One host only; no second host is scored.
- No path-length law is attached.
- No Record readout is assigned to a site without a record.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, occupancy `σ`,
lock ticks `t`, the age bit `b = [t(−z) < t(+z)]`, the 48-member
July-3 pair, leftover-frame-positive `f(σ,b)`, hop-cost-ignored fire
(`N_new = 1`, `U` persists), inward weights and `ρ` on directed
nearest-neighbor edges of `U`, the unchanged `(σ, b)` after that
labeling, the four incoming costs at `v`, the cost-1 readiness filter
(`σ_ready`, `N_new = 0`), the current premise boundary, and the
mutation controls. It scores this uneqrad host only. It writes no
cache and authors no audit verdict.

---
claim_id: perp_mask_leftover_frame_fire_census_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the 12 lex-first realizing 3-ball hosts of the perpendicular weight-4 masks, how many times leftover-frame-positive f fires is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perp_mask_leftover_frame_fire_census_2026_08_15.py
---

# Perpendicular-Mask Leftover-Frame Fire Census (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 lex-first realizing 3-ball hosts of the perpendicular
weight-4 occupancy masks. On each host, rebuild `b` from the seed-radii
ℓ¹ lock tick and the unique full axis, apply leftover-frame-positive
`f`, and report `N_fire / 12`. Score those 12 lex-first hosts only.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perp_mask_leftover_frame_fire_census_2026_08_15.py`](../scripts/perp_mask_leftover_frame_fire_census_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment bitreal: all 12 perp masks are realized as unread 6-NN of a
3-ball in the uneqrad box. Investment bitfire: `f` fires on one of them.
The residual here is not leftover of bitfire (one host). On each
lex-first realizing host, rebuild `b` from `t`, apply leftover-frame
`f`, and report `N_fire / 12`. Do not attach L1.

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The 12 rows are the bitreal Theorem 2 hosts: for each perpendicular
weight-4 mask, the lex-first `(centers, radii, v)` whose unread 6-NN
occupancy equals that mask. On each host, `t` is the seed-radii ℓ¹ lock
tick on occupied neighbors, `b` is read from the unique full axis, and
`f` is the leftover-frame-positive July-3 pair member of `(σ,b)`.

**Theorem 1.** Rebuild the 12 hosts. `N_rebuild = 12`.

**Theorem 2.** `N_fire = 12`. Each of the 12 has `N_new = 1` and `U`
persisting. There is no lex-first failure.

**Theorem 3.** Displayed, not adopted. Do not write `f` into
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

Admissibility names neither leftover-frame-positive `f` nor any realizing
3-ball host as the framework's fixed rule. Record permanence is used only
to keep the locks on each `U`. Formation site and rate remain outside
the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact census of leftover-frame-positive f on the 12 lex-first realizing 3-ball hosts of the perpendicular weight-4 masks: N_rebuild=12 and N_fire=12. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: perp_mask_leftover_frame_fire_census
target_blocker_text: "on each lex-first realizing host, whether leftover-frame-positive f fires; N_fire / 12"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_rebuild and N_fire on the 12 lex-first hosts; do not write f into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 lex-first realizing hosts; N_rebuild=12; N_fire=12; displayed, not adopted"
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
occupancy is the named mask. The twelve hosts are the bitreal Theorem 2
lex-first rows.

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
`v` and leaves every lock of `U` in place. `N_fire` is how many of the
12 hosts have `N_new = 1` and `U` persisting. If `N_fire < 12`, the
lex-first non-firing host is the failure.

Score the 12 lex-first hosts only.

## Theorem 1 — Rebuild the 12 hosts; `N_rebuild = 12`

Each bitreal Theorem 2 row rebuilds: the three ℓ¹ balls with the named
centers and radii have unread center `v`, and the 6-NN occupancy of `v`
equals the named mask. All 12 rows rebuild, so

`N_rebuild = 12`.

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

This is not leftover of bitfire (one host). Bitfire scored `f` on the
uneqrad breaker star, a different host of one mask. The present census
rebuilds the twelve lex-first realizing hosts.

## Theorem 2 — `N_fire = 12`

On each rebuilt host, `t` is the seed-radii ℓ¹ lock tick, `b` is read
from the unique full axis, and `f` is the leftover-frame-positive pair
member. Each `f` is a July-3 pair member, each `v` is unread, the
displayed pair step forms exactly that `v` (`N_new = 1`), and no lock
of `U` is removed, so `U` persists. Therefore

`N_fire = 12`.

There is no lex-first failure. The twelve fire rows are

| `σ` | axis | `t` | `b` | `f(σ,b)` | `N_new` | `U` persists |
|---|---|---|---|---|---|---|
| `(0, 1, 0, 1, 1, 1)` | `z` | `(·, 1, ·, 1, 2, 2)` | `0` | `(0, −, 0, +, −, +)` | `1` | yes |
| `(0, 1, 1, 0, 1, 1)` | `z` | `(·, 1, 1, ·, 2, 2)` | `0` | `(0, +, −, 0, −, +)` | `1` | yes |
| `(0, 1, 1, 1, 0, 1)` | `y` | `(·, 1, 2, 1, ·, 2)` | `1` | `(0, −, +, −, 0, +)` | `1` | yes |
| `(0, 1, 1, 1, 1, 0)` | `y` | `(·, 1, 1, 1, 2, ·)` | `0` | `(0, −, −, +, +, 0)` | `1` | yes |
| `(1, 0, 0, 1, 1, 1)` | `z` | `(1, ·, ·, 1, 2, 2)` | `0` | `(+, 0, 0, −, −, +)` | `1` | yes |
| `(1, 0, 1, 0, 1, 1)` | `z` | `(1, ·, 1, ·, 2, 2)` | `0` | `(−, 0, +, 0, −, +)` | `1` | yes |
| `(1, 0, 1, 1, 0, 1)` | `y` | `(1, ·, 2, 1, ·, 2)` | `1` | `(+, 0, +, −, 0, −)` | `1` | yes |
| `(1, 0, 1, 1, 1, 0)` | `y` | `(1, ·, 1, 1, 2, ·)` | `0` | `(+, 0, −, +, −, 0)` | `1` | yes |
| `(1, 1, 0, 1, 0, 1)` | `x` | `(2, 1, ·, 1, ·, 2)` | `1` | `(+, −, 0, +, 0, −)` | `1` | yes |
| `(1, 1, 0, 1, 1, 0)` | `x` | `(1, 1, ·, 1, 2, ·)` | `0` | `(−, +, 0, +, −, 0)` | `1` | yes |
| `(1, 1, 1, 0, 0, 1)` | `x` | `(2, 1, 1, ·, ·, 2)` | `1` | `(+, −, −, 0, 0, +)` | `1` | yes |
| `(1, 1, 1, 0, 1, 0)` | `x` | `(1, 1, 1, ·, 2, ·)` | `0` | `(−, +, −, 0, +, 0)` | `1` | yes |

On the mask that bitfire scored, the lex-first realizing host is not
the uneqrad breaker: radii are `(2, 1, 2)` and `b = 0`, so
`f = (−, 0, +, 0, −, +)`. That is why this census is not leftover of
bitfire (one host).

## Theorem 3 — displayed, not adopted

The counts `N_rebuild = 12` and `N_fire = 12`, the twelve hosts, and
the twelve fire rows are displayed member data. They are not the
framework's fixed Admissibility rule. This note does not write `f` into
Admissibility. Do not write f into Admissibility. Do not attach L1.
Occupancy-only formation is not attached. Qubit remains `M_2(C)`. No
approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the 12 lex-first realizing 3-ball hosts of the
  perpendicular weight-4 masks, `N_rebuild = 12` and `N_fire = 12`.
  Each host has leftover-frame-positive `f` with `N_new = 1` and `U`
  persisting. There is no lex-first failure.
- **What is displayed only.** The twelve hosts, the ticks, the age
  bits, the section `f`, and the fire report are one rival table. They
  are not adopted.
- **What is not claimed.** No attachment of `f` to Admissibility; no
  writing of radii or ticks into Admissibility; no attachment of
  occupancy-only formation; no axiom edit; no formation rate; no
  leftover of bitfire (one host); no compiler no-go.
- **Mutation controls.** A rebuilt `N_rebuild` other than 12 fails. A
  rebuilt `N_fire` other than 12 fails, and the lex-first non-firing
  host is then the failure. A note that writes `f` into Admissibility,
  attaches L1, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the 12 lex-first realizing hosts, the
seed-radii ℓ¹ lock ticks, the age bit on the unique full axis, the
48-member July-3 pair, leftover-frame-positive `f`, the fire report
(`N_new`, `U` persists) on each host, `N_rebuild`, `N_fire`, the
current premise boundary, and the mutation controls. It scores the 12
lex-first hosts only. It writes no cache and authors no audit verdict.

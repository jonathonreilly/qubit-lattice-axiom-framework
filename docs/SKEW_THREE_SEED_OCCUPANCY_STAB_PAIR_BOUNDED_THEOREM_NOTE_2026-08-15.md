---
claim_id: skew_three_seed_occupancy_stab_pair_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball star at v=(-1,1,1), the occupancy stabilizer and the count of Stab-invariant July-3 pair members with that support are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_occupancy_stab_pair_2026_08_15.py
---

# Occupancy Stabilizer Versus July-3 Pair Members On The Off-Axis Three-Seed Star (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the unread six-neighbor star at `v = (−1,1,1)` on
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`. Occupancy `σ` is the 6-bit
nearest-neighbor occupancy of `U` at `v`. Score the star at `v` only.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_occupancy_stab_pair_2026_08_15.py`](../scripts/skew_three_seed_occupancy_stab_pair_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment delrun `#6662` fires one named product pair member on this star.
Investment deleq reported that that named product is not `G+`-equivariant
(`3/24`). Investment delloc reported that that product is not NN-determined.
The residual here is not leftover of deleq (one named product) or nstab
(two-ball tied-`n`). It is the occupancy object itself.

On this star, occupancy `σ` is a 6-bit nearest-neighbor object. A local
(NN-determined) labeling is a function `f(σ)`. `G+`-equivariance on the
orbit of `σ` requires `f(σ)` to be `Stab(σ)`-invariant. This note counts
`|Stab(σ)|` and how many July-3 pair members have this support and are
Stab-invariant.

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Direct listing against `U` gives

`σ = (1, 0, 1, 1, 0, 1)`.

`G+` is the 24 proper cube rotations acting on slots. The occupancy
stabilizer is

`Stab(σ) = { g in G+ : g · σ = σ }`.

**Theorem 1.** `|Stab(σ)| = 2`. A generating list is the identity and the
order-2 rotation

`s : (x, y, z) ↦ (−z, −y, −x)`.

`N_pair_support = 4`: exactly four July-3 `k = 3` chiral-pair members have
support equal to `σ`.

**Theorem 2.** `N_stab_ok = 0`: none of those four members is fixed by
every element of `Stab(σ)`. The implication “if `|Stab(σ)| = 1` then
`N_stab_ok = N_pair_support`” holds vacuously here because `|Stab(σ)| = 2`.
`N_stab_ok` is the number of `G+`-equivariant local extensions of a pair
member on the orbit of `σ`.

**Theorem 3.** Displayed, not adopted. Do not write any such `c` into
Admissibility. Do not attach L1. Do not add a 4th ball. Qubit remains
`M_2(C)`. No axiom edit.

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

Admissibility names neither `Stab(σ)` nor any July-3 pair member as the
framework's fixed rule. The covariance clause is the reason a local
labeling on the orbit of `σ` must be stabilizer-invariant. Formation site
and rate remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom
edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ occupancy on one unread six-neighbor star, a 24-element stabilizer count, and a 48-member pair support/invariance census. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_occupancy_stab_pair
target_blocker_text: "on the off-axis three-ball star at v=(-1,1,1), the occupancy stabilizer and the count of Stab-invariant July-3 pair members with that support"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of |Stab(σ)|, N_pair_support, and N_stab_ok; do not write any such c into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on the star at v=(-1,1,1); |Stab(σ)|=2; N_pair_support=4; N_stab_ok=0; displayed, not adopted"
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

Occupancy at `v`:

`σ = (1, 0, 1, 1, 0, 1)`.

Support of a 6-tuple is the set of slots with a nonzero letter. Occupancy
`σ` is already that indicator.

`G+` is the 24 determinant-`+1` signed permutation matrices of the three
axes. A matrix `g` permutes the six axis directions: the letter (or bit)
at slot `μ` moves to slot `gμ`. The occupancy stabilizer is

`Stab(σ) = { g in G+ : g · σ = σ }`.

The July-3 `k = 3` chiral pair is the unique pair of `G+` orbits of
handed fully-mixed 6-tuples on the three-letter alphabet `{0,1,2}` with
`0` empty. Fully mixed means every axis is bi-colored and each letter is
used twice. The pair is reconstructed by enumerating the 24 proper
rotations on `{0,1,2}^6`; it has 48 members (two orbits of size 24).
Letters `{1,2}` are the two nonzero condition letters; they may be
written `{+, −}` when displaying a 6-tuple.

`N_pair_support` is the number of pair members whose support equals `σ`.
`N_stab_ok` is the number of those members `c` with `g · c = c` for every
`g` in `Stab(σ)`.

A local (NN-determined) labeling is a function `f` of occupancy. On the
`G+` orbit of `σ`, equivariance forces `f(σ)` to be `Stab(σ)`-invariant
and then determines `f` at every image `g · σ` by transport. Therefore
`N_stab_ok` is the number of `G+`-equivariant local extensions of a pair
member on the orbit of `σ`.

## Theorem 1 — stabilizer and support count

Enumerating the 24 proper rotations on the occupancy 6-tuple gives

`|Stab(σ)| = 2`.

A generating list is

1. the identity `id : (x, y, z) ↦ (x, y, z)`, which fixes every slot;
2. the order-2 rotation `s : (x, y, z) ↦ (−z, −y, −x)`, whose slot
   permutation is

   `+x ↔ −z`, `−x ↔ +z`, `+y ↔ −y`.

Those two matrices generate `Stab(σ)` and exhaust it. The identity
contributes no constraint. The non-identity element preserves the occupied
set `{+x, +y, −y, −z}` and swaps the two empty slots. Orbit-stabilizer is
consistent and unused as an extra premise: the occupancy orbit has
`24/2 = 12` distinct images.

The July-3 pair is reconstructed by partitioning `{0,1,2}^6` into 57
`G+` orbits and retaining the unique pair of orbits exchanged by spatial
inversion. Exactly four pair members have support equal to `σ`:

| member `{0,1,2}` | displayed `{+,0,−}` |
|---|---|
| `(1, 0, 1, 2, 0, 2)` | `(+,0,+,−,0,−)` |
| `(1, 0, 2, 1, 0, 2)` | `(+,0,−,+,0,−)` |
| `(2, 0, 1, 2, 0, 1)` | `(−,0,+,−,0,+)` |
| `(2, 0, 2, 1, 0, 1)` | `(−,0,−,+,0,+)` |

So

`N_pair_support = 4`.

Each of these four is fully mixed: letter `0` occupies the two empty
slots, the `y`-axis is bi-colored, and the two nonzero letters each appear
twice. Scoring only the star at `v`. This is not leftover of deleq (one
named product) and not leftover of nstab (two-ball tied-`n`).

## Theorem 2 — stabilizer-invariant pair members

For `c` among the four support-matched pair members, `g · c = c` for
every `g` in `Stab(σ)` if and only if `s · c = c`. The slot permutation
of `s` requires `c(+x) = c(−z)` and `c(+y) = c(−y)`. Every July-3 pair
member is fully mixed, so the `y`-axis is bi-colored:

`c(+y) ≠ c(−y)`.

Therefore no support-matched pair member is fixed by `s`, and

`N_stab_ok = 0`.

If `|Stab(σ)| = 1` then `N_stab_ok = N_pair_support`. That implication
is recorded. It is not triggered: `|Stab(σ)| = 2`.

`N_stab_ok` is the number of `G+`-equivariant local extensions of a pair
member on the orbit of `σ`. The count is zero: no pair member with this
support can be the value of a `G+`-equivariant function of occupancy at
`σ`.

The named product `(+,0,+,−,0,−)` is one of the four support-matched
members and fails stabilizer invariance, as do the other three. That
failure is a property of the whole support class, not a re-test of deleq's
`3/24` commutation count for one product rule.

## Theorem 3 — displayed, not adopted

The stabilizer, the four support-matched pair members, and the count
`N_stab_ok = 0` are displayed member data. They are not the framework's
fixed Admissibility rule. This note does not write any such `c` into
Admissibility. Do not write any such `c` into Admissibility. Do not attach
L1. Do not add a 4th ball. Occupancy-only formation is not attached.
Qubit remains `M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On this unread star, `|Stab(σ)| = 2` with generating
  list `{id, s}`, `N_pair_support = 4`, and `N_stab_ok = 0`.
- **What is displayed only.** The stabilizer, the four 6-tuples, and the
  invariance count are one rival table. They are not adopted.
- **What is not claimed.** No attachment of any pair member to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no fourth
  equal-radius ball; no leftover of deleq's one named product; no
  leftover of nstab's two-ball tied-`n`; no compiler no-go.
- **Mutation controls.** A rebuilt `σ` other than `(1, 0, 1, 1, 0, 1)`
  fails. `|Stab(σ)| = 1` would trigger `N_stab_ok = N_pair_support` and
  fail the order-2 report. A note that writes any such `c` into
  Admissibility, attaches L1, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, occupancy `σ`, the 24
proper cube rotations acting on slots, `Stab(σ)`, the reconstructed
July-3 pair, `N_pair_support`, `N_stab_ok`, the current premise boundary,
and the mutation controls. It writes no cache and authors no audit
verdict.

---
claim_id: three_ball_tick_broken_pair_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the lex-first 3-ball weight-4 star whose lock-ticks shrink Stab, how many tick-invariant July-3 pair members fire is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_ball_tick_broken_pair_fire_2026_08_15.py
---

# Tick-Broken Three-Ball Weight-4 Pair Fire (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** three-ball unions `U = B_2(s1) ∪ B_2(s2) ∪ B_2(s3)` with distinct
centers in `[-2,2]^3` and unread weight-4 six-neighbor stars at `v` with
`|v|_∞ ≤ 3`. Rebuild `N_uneq`. On the lex-first star with
`|Stab(σ, t)| < |Stab(σ)|`, or on none if that set is empty, count
`Stab(σ, t)`-invariant July-3 pair members and how many fire. Score the
lex-first breaker star only, or none. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_ball_tick_broken_pair_fire_2026_08_15.py`](../scripts/three_ball_tick_broken_pair_fire_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment tickuneq names whether any 3-ball weight-4 star has
`|Stab(σ, t)| < |Stab(σ)|`. Investment tickfire runs the July-3 pair on
one equal-tick `U`. The residual here is not leftover of tickfire (the
equal-tick `U`) and not leftover of tickuneq (census only). It is the
*run* on the lex-first tick-broken star: how many `Stab(σ, t)`-invariant
July-3 pair members fire.

The locked set is any already-given three-ball union with distinct
centers in the box. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Occupied nearest neighbors receive the lock tick

`t(w) = min_i |w − s_i|_1`.

Empty slots have no tick. Local data is `(σ, t)`. `G+` is the 24
proper cube rotations acting on slots.

`Stab(σ, t) = { g ∈ G+ : g · σ = σ and t(g · μ) = t(μ) on occupied slots }`.

A breaker is a weight-4 unread star in the box with
`|Stab(σ, t)| < |Stab(σ)|`. Rebuild gives

`N_uneq = 0`.

There is no lex-first breaker. The host set for `S` is empty, so

`|S| = 0`,

`N_tick_ok = 0`, and

`N_fire = 0`.

The same scan finds `N_w4 = 763608` weight-4 unread stars. On every one
of them the four occupied lock-ticks are all `2`, so
`Stab(σ, t) = Stab(σ)`.

Displayed, not adopted. Do not write a firing c into Admissibility.
Do not attach L1. Do not add a 4th ball. Occupancy-only formation
(the `n ≠ 0` gate) is not attached. Qubit remains `M_2(C)`. No
axiom edit.

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

Admissibility names neither a firing 6-tuple, a lock tick, nor the
July-3 pair as the framework's fixed rule. Record permanence is used
only to keep the locks on `U`. Formation site and rate remain outside
the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ three-ball box, lock-tick Lipschitz identity on unread stars, and an exact empty fire census on the (empty) breaker host. Displayed census only."
trace_class: frontier_discovery
target_claim_id: three_ball_tick_broken_pair_fire
target_blocker_text: "on the lex-first 3-ball weight-4 star whose lock-ticks shrink Stab, how many tick-invariant July-3 pair members fire"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_uneq, |S|, and N_fire; do not write a firing c into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on 3-ball weight-4 unread stars with centers in [-2,2]^3 and |v|_∞≤3; N_uneq=0, |S|=0, N_tick_ok=0, N_fire=0; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The closed ℓ¹ ball of radius two is

`B_2(c) = { x ∈ Z^3 : |x − c|_1 ≤ 2 }`.

Each such ball has 25 sites. Distinct centers `s1, s2, s3` run through
`[-2,2]^3` in lex-increasing order, so each unordered triple is scored
once. There are `C(125, 3) = 317750` such triples. The locked set is

`U = B_2(s1) ∪ B_2(s2) ∪ B_2(s3)`.

Unread centers `v` run through `|v|_∞ ≤ 3` with `v ∉ U`. A star is
weight-4 when exactly four of the six nearest neighbors of `v` lie in
`U`. The scan finds

`N_w4 = 763608`

such stars. Occupancy `σ` is the 0-1 mask of those neighbors in the
declared direction order. On an occupied neighbor `w`,

`t(w) = min{|w − s1|_1, |w − s2|_1, |w − s3|_1}`.

Empty slots have no tick. Letters are `{0, +, −}` with `0` empty.
Encode `0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`. The July-3 `k = 3` pair is the
unique pair of proper-cubic orbits of handed fully-mixed 6-tuples. It
has 48 members. A displayed pair step at an unread site forms that
site if and only if the encoded 6-tuple lies in the pair; existing
locks are not removed.

`G+` is the 24 determinant-`+1` signed permutation matrices of the
three axes, acting on the six axis directions. Support of a coloring
is the 0-1 mask of nonzero letters. Occupancy stabilizer `Stab(σ)` is
`{ g ∈ G+ : g · σ = σ }`. Lock-tick stabilizer `Stab(σ, t)` further
requires `t(g · μ) = t(μ)` on occupied slots.

A breaker is a weight-4 star with `|Stab(σ, t)| < |Stab(σ)|`. `N_uneq`
is the number of breakers in the box. If `N_uneq = 0` there is no
lex-first breaker, the host of `S` is empty, and `N_tick_ok = 0` and
`N_fire = 0`.

If a breaker exists, `S` is the set of pair members `c` with
`support(c) = σ` and `g · c = c` for every `g ∈ Stab(σ, t)` on that
lex-first star, and `N_fire` is the number of `c ∈ S` for which the
displayed step forms exactly that `v` (`N_new = 1`) while every site
of that `U` remains locked.

Lock-tick `t` is the pointwise minimum of three ℓ¹ distances, so it is
1-Lipschitz for `|.|_1`. Unread `v` lies outside every radius-2 ball,
hence `t(v) ≥ 3`. Each nearest neighbor `w` satisfies
`|t(w) − t(v)| ≤ 1`. If `w` is occupied then `w ∈ U`, so `t(w) ≤ 2`,
and also `t(w) ≥ t(v) − 1 ≥ 2`. Therefore every occupied neighbor of an unread site has lock tick exactly `2`. All occupied ticks are
equal, every occupancy stabilizer element preserves `t`, and

`|Stab(σ, t)| = |Stab(σ)|`

on every star in the family.

Only the lex-first breaker is scored, or none.

## Theorem 1 — Lex-first breaker, or none; rebuild `S`

The box scan enumerates every lex-increasing center triple and every
unread `v` with `|v|_∞ ≤ 3`. It rebuilds `σ` and `t` on each weight-4
star and compares `|Stab(σ, t)|` with `|Stab(σ)|`.

No star is a breaker:

`N_uneq = 0`.

There is no lex-first breaker. The four occupied lock-ticks on every
weight-4 star equal `2`, which is the Lipschitz identity above. The
known equal-tick union
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` at `v = (−1,1,1)` lies in
the box and is not a breaker: `σ = (1, 0, 1, 1, 0, 1)`, occupied ticks
all `2`, `|Stab(σ)| = |Stab(σ, t)| = 2`. That star is recorded only as
a membership check. It is not scored.

Because there is no host star, `S` has no member:

`|S| = 0`.

Hence `N_tick_ok = 0`.

This is not leftover of tickfire (the equal-tick `U`): tickfire runs
pair members on one displayed union whose ticks do not shrink `Stab`.
It is not leftover of tickuneq (census only): tickuneq names whether a
breaker exists. The present objects are `|S|` and the fire count on
the lex-first breaker, which is empty.

## Theorem 2 — Fire count

If `N_uneq = 0`, then `N_tick_ok = 0` and `N_fire = 0` by the empty
count: no tick-broken star is present, and no `Stab(σ, t)`-invariant
pair member is present to form a `v`. The displayed pair step is not
run on a nonexistent member. No lock is added or removed.

Because `|S| = 0`, report `N_fire = 0`.

## Theorem 3 — Displayed, not adopted

The empty breaker list, the set `S`, and the count `N_fire` are
displayed member data. They are not the framework's fixed
Admissibility rule. This note does not write a firing c into
Admissibility. Do not write a firing c into Admissibility. Do not
write ticks into Admissibility. Do not attach L1. Do not add a 4th
ball. Occupancy-only formation (the `n ≠ 0` gate) is not attached.
Qubit remains `M_2(C)`. No approved primitive is added. No axiom
edit.

## Honest-auditor / Boundary

- **What is proved.** In this box, `N_w4 = 763608`, every occupied
  lock-tick on a weight-4 unread star equals `2`, `N_uneq = 0`, there
  is no lex-first breaker, `|S| = 0`, `N_tick_ok = 0`, and
  `N_fire = 0`.
- **What is displayed only.** The breaker census, the pair, and the
  fire count are one rival table. They are not adopted.
- **What is not claimed.** No attachment of a firing 6-tuple to
  Admissibility; no writing of ticks into Admissibility; no
  attachment of occupancy-only formation; no axiom edit; no
  formation rate; no lattice-wide dynamics; no fourth equal-radius
  ball; no restatement of the tickfire equal-tick run as an adopted
  law; no restatement of the tickuneq census as the present fire
  count.
- **Mutation controls.** A rebuilt `N_uneq` other than `0` fails. A
  claimed fire from an empty `S` fails. An occupied tick other than
  `2` on a scanned weight-4 star fails. A note that writes a firing
  c into Admissibility, attaches L1, or authors an audit verdict
  fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the three-ball box, every weight-4 unread
star, lock ticks `t`, `G+`, `N_uneq`, the 48-member July-3 pair, `S`,
`N_fire`, the current premise boundary, and the mutation controls.
It writes no cache and authors no audit verdict.

---
claim_id: two_cube_l1_two_tick_clock_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the declared two-cube vertex carrier with seed (0,0,0) and the supplied one-neighborhood tick, the two-tick clock is the formation count F_t = |locks_t| − 1. After tick 1 the census is |locks|=4, F=3, ρ(A)=4. After tick 2 it is |locks|=8, F=7, ρ(A)=7. Thus F_t ≠ ρ(A)_t at t=1, while the meeting F_2 = ρ(A)_2 is a coincidence: ρ(A) already counted the seed and missed the B-only lock (2,0,0). The integrated law is additive across the two ticks: F_2 = F_1 + F_tick2 (7=3+4). This is a finite exhibit of a supplied tick, not a time metric, rate, or full Z^3 history."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_two_tick_clock_2026_08_14.py
---

# Two-Tick One-Neighborhood Clock Is Lock-Count Minus Seed

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact two-tick census of a supplied one-neighborhood lock-growth
law on one declared two-cube vertex carrier.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_two_tick_clock_2026_08_14.py`](../scripts/two_cube_l1_two_tick_clock_2026_08_14.py)

## Result up front

A prior one-step comparison of four integers is not enough to identify the
clock of this law. On the declared two-cube carrier the supplied
one-neighborhood tick — abbreviated L1 in this note only — grows a lock set
from a seed of size `1`. The clock of that integrated law is the formation
count

```text
F_t = |locks_t| − 1,
```

not the occupancy `ρ(A)_t` of cube A.

Direct growth gives the census

```text
t=1:  |locks|=4,  F=3,  ρ(A)=4,
t=2:  |locks|=8,  F=7,  ρ(A)=7.
```

So `F_1 ≠ ρ(A)_1` because `3≠4`. The later meeting `7=7` is a coincidence,
not identity: `ρ(A)` already counted the seed and missed the B-only lock
`(2,0,0)`. Across the two ticks the integrated law is additive:

```text
F_2 = F_1 + F_tick2,   7=3+4.
```

The current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) says that
records form and that a formed record locks exactly one admissible local
possibility. It does not supply a time metric, a record-production process,
or this tick. The geometry, seed, and one-neighborhood step are declared
finite test objects.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two-tick census and the three displayed identities are exact on one declared carrier; the tick, the two-cube region, and every rate or time-metric reading remain unsupplied by the axioms."
trace_class: negative_route_pruning
target_claim_id: two_cube_l1_two_tick_clock
target_blocker_text: "identify the two-tick clock of the integrated one-neighborhood lock law with the formation count rather than with cube-A occupancy"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "keep F_t = |locks_t| − 1 as the clock of this supplied law; do not promote ρ(A) or a one-step four-integer comparison to the two-tick identity"
conditional_surface_status: "exact only for the declared two-cube carrier and supplied one-neighborhood tick; no time metric, rate, or full Z^3 closure"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

`cache_write: false`

## Premise boundary

The current Record sentences used here are:

```text
Records form.
When present, a record locks exactly one admissible local possibility.
A site never carries more than one record; records are permanent.
A site with no record cannot be read.
```

Those sentences license a lock as a formed record at a site. They do not
choose the carrier, the seed, the tick, or a clock rate. The one-neighborhood
tick is a supplied discrete step of an integrated lock-growth law on a finite
declared vertex set. The tick index is a discrete step of a supplied law, not
a derived clock rate.

No finite-additive scalar functional is used. Absence is unread.

## Exact objects

Let cube A be the vertex set `{0,1}^3` and cube B the vertex set
`{1,2}×{0,1}×{0,1}`. The carrier is the union

```text
V = A ∪ B,   |A|=8,   |B|=8,   |V|=12.
```

The shared face is `x=1`, with four vertices. Nearest-neighbor adjacency is
the restriction to `V` of the standard `Z^3` adjacency. The seed is

```text
locks_0 = {(0,0,0)},   |locks_0|=1.
```

One L1 tick replaces a lock set `S` by `S` together with every neighbor of
`S` that lies in `V`. Write `locks_t` for the result after `t` ticks, and

```text
F_t        := |locks_t| − |locks_0|,
ρ(A)_t     := |locks_t ∩ A|,
F_tick2    := |locks_2 \ locks_1|.
```

`F_t` is the formation count: every lock other than the seed. `ρ(A)_t` is
the occupancy of cube A among current locks. The runner grows these sets; it
does not insert the census integers as the objects under test.

## Theorem 1 — the clock is lock-count minus seed

The seed has size `1`, so `F_t = |locks_t| − 1` at every tick. After one
tick the neighbors of `(0,0,0)` in `V` are `(1,0,0)`, `(0,1,0)`, and
`(0,0,1)`. Hence

```text
locks_1 = {(0,0,0),(1,0,0),(0,1,0),(0,0,1)},
|locks_1|=4,   F_1=3.
```

After the second tick the new locks are the `V`-neighbors of `locks_1` that
were not already locked:

```text
locks_2 \ locks_1 = {(2,0,0),(1,1,0),(1,0,1),(0,1,1)}.
```

Each of those four sites is at graph distance two from the seed, so

```text
|locks_2|=8,   F_2=7.
```

The remaining A-corner `(1,1,1)` has graph distance three and is not locked
by tick 2. Theorem 1 is the identity `F_t = |locks_t| − 1` at `t=1` and
`t=2`.

## Theorem 2 — formation count is not cube-A occupancy

At `t=1` every lock lies in A, including the seed, so `ρ(A)_1=4`. Therefore

```text
F_1 ≠ ρ(A)_1   because   3≠4.
```

A one-step comparison that only lines up four integers can hide this split:
the seed-inclusive count `|locks_1|` equals `ρ(A)_1`, while the formation
count does not.

At `t=2` the locked A-set has seven sites and `ρ(A)_2=7`. The same integer
is `F_2`. The meeting `7=7` is a coincidence, not identity. Cube-A occupancy
already counted the seed `(0,0,0)` and missed the B-only lock `(2,0,0)`:

```text
locks_2 \ A = {(2,0,0)},
(0,0,0) ∈ locks_2 ∩ A,
F_2     = ρ(A)_2 − 1 + |locks_2 \ A|.
```

The seed subtraction and the missed B-only lock cancel. Dropping `(2,0,0)`
from the lock set makes the two counts `6` and `7` and destroys the meeting.
Including the seed in the clock makes the `t=1` counts collide and conceals
the type distinction.

## Theorem 3 — additivity across two ticks

The second tick contributes four new locks, so `F_tick2=4`. The integrated
formation count after two ticks is the sum of the first-tick formation count
and that increment:

```text
F_2 = F_1 + F_tick2,   7=3+4.
```

This is additivity of the supplied integrated law across two ticks, not a
one-step identity and not a statement about `ρ(A)`. Cube-A occupancy is not
additive in the same way: `ρ(A)_2 − ρ(A)_1 = 3`, because one of the four new
locks is the B-only site.

## No-Go Discipline

The negative clause is only this: on the displayed carrier, `ρ(A)` is not
the two-tick clock. That is an exhibit, not a universal ban on occupancy
counters.

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| read the clock as `ρ(A)` from the `t=1` integers | **ATTEMPTED** | `|locks_1|=ρ(A)_1=4` while `F_1=3` |
| read the `t=2` meeting as an identity | **ATTEMPTED** | `ρ(A)` counted the seed and missed `(2,0,0)` |
| replace `F` by seed-inclusive `|locks|` | **ATTEMPTED** | collides with `ρ(A)` at `t=1` and loses the formation reading |
| take a one-step four-integer comparison as the two-tick law | **ATTEMPTED** | additivity `7=3+4` is a two-tick identity |
| promote the tick to a time metric or rate | **ATTEMPTED** | the tick is a supplied discrete step; no clock-rate object is defined |

### N2 — wall independence

One type wall is claimed: formation count minus seed is not cube-A
occupancy. The additivity identity is a positive census, not a second
impossibility wall.

### N3 — hidden-wall scan

The two cubes, the seed, and the one-neighborhood step are declared. No
full-lattice history, Hamiltonian, stochastic kernel, time metric, scalar
absence value, or Newton kernel is imported.

### N4 — residual matching

The residual is a physical formation process, clock rate, and full-lattice
extension of the tick. This note neither closes nor enlarges that residual.
It only names the clock of the supplied two-tick exhibit.

### N5 — certificate granularity

```text
per-element: executed — every lock after each tick is enumerated
per-site: executed — the twelve two-cube vertices are the carrier
per-mode: not applicable — no modal or spectral decomposition is used
per-block: executed — only the declared two-tick integrated law is checked
lattice-wide: not executed — no full Z^3 history or rate is claimed
```

### N6 — partial-closure paths

A separately supplied or derived formation kernel on a larger region could
use the same one-neighborhood step, a different adjacency, or an independent
clock. Every such route remains live. The present identities do not select
one.

### N7 — steelman

The strongest objection is that after two ticks `F` and `ρ(A)` agree, so the
clock might as well be occupancy. Correct that the integers agree at `t=2`.
Incorrect as an identification: the agreement uses one missed B-only lock
against one already-counted seed, and it already fails at `t=1`.

### N8 — cross-cycle echo

A one-step `clockid` comparison of four integers can line up
`|locks|`, `F`, `ρ(A)`, and the seed size on a single tick. This note keeps
that split and adds the two-tick additivity of the integrated law.

## Boundaries and explicit non-claims

- The two-cube carrier and the one-neighborhood tick are supplied test
  objects. They are not derived from the axiom memo.
- The tick index is a discrete step of a supplied law, not a derived clock
  rate.
- The result does not supply a formation probability, process, or physical
  rate.
- Absence is unread and receives no scalar value.
- The meeting at `t=2` is not an identity of functors or a full-lattice law.
- No axiom, primitive, registry, or audit verdict is edited.

## Verification

Run:

```bash
python3 scripts/two_cube_l1_two_tick_clock_2026_08_14.py
```

The runner constructs the two cubes, grows the lock set through two ticks,
computes `F` and `ρ(A)` from those sets, and checks the three theorems plus
the seed-inclusive and B-only mutation controls. Expected summary:

```text
TOTAL: PASS>=8 FAIL=0
```

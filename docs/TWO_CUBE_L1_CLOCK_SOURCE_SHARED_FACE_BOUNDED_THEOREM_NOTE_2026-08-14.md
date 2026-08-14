---
claim_id: two_cube_l1_clock_source_shared_face_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied two-cube L1 patch, each displayed tick obeys Delta rho(A)+Delta rho(B)=F_tick+S with S=|new locks intersect F*|. Cube increments equal new locks inside that cube, shared vertices counted in both. The identity is the unique nonnegative face correction relating the clock increment to the pair of cube increments; it is not the union occupancy sum."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_l1_clock_source_shared_face_2026_08_14.py
---

# Clock Increment Versus Double-Counted Cube Source Increment On The L1 Two-Cube Patch

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer identities on one supplied two-cube patch for two
ticks of the displayed `L1` occupancy kernel. No full-history formation law,
rate, or physical source identification is asserted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_l1_clock_source_shared_face_2026_08_14.py`](../scripts/two_cube_l1_clock_source_shared_face_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write two adjacent unit cubes in integer coordinates:

```text
A = {0,1} x {0,1} x {0,1},
B = {1,2} x {0,1} x {0,1}.
```

The displayed patch is `A union B` (twelve vertices). The shared face is

```text
F* = {v in A union B : v_x = 1} = A intersect B.
```

Occupancy off the patch is `0`. A locked site has occupancy `1` and stays
locked. An unread site has occupancy `0`. The neighbor imbalance at a site
`v` is the triple

```text
n_mu(v) = (o(v+e_mu) - o(v-e_mu)) / 3,   mu in {x,y,z}.
```

An unread patch site forms on a tick if and only if `n(v) != 0`. The clock
starts at `F = 0` and adds the number of newly formed locks on that tick.
Cube source values are ordinary occupancy sums

```text
rho(C) = sum_{v in C} o(v).
```

The seed is `{(0,0,0)}`. After that seed, the two displayed ticks produce

```text
tick 1:  F_tick = 3,  S = 1,  Delta rho(A) = 3,  Delta rho(B) = 1
tick 2:  F_tick = 4,  S = 2,  Delta rho(A) = 3,  Delta rho(B) = 3
```

with shared-face new locks `(1,0,0)` on tick 1 and `{(1,1,0),(1,0,1)}` on
tick 2.

**Theorem.** On each of those ticks,

```text
Delta rho(A) + Delta rho(B) = F_tick + S,
S = |new locks intersect F*|.
```

The same data also satisfy `Delta rho(C) = |new locks intersect C|` for
`C in {A,B}`, with shared vertices counted in both cubes. The clock increment
equals the union occupancy increment on the twelve-site patch. The sum of the
two cube increments is strictly larger, and the excess is exactly the shared
face count `S`. Among integers `s` with `0 <= s <= |F*|`, that `S` is the
unique solution of the displayed identity.

The relation between `F` and `rho` is therefore unique on this patch once
double-counting of `F*` is recorded. It is not a clone of `sum o` on the
union, and it is not the statement that `F_tick` equals either cube increment
alone.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Two explicit L1 ticks on one twelve-site patch give exact integer identities relating F_tick to the pair of cube occupancy increments through the shared-face count S."
trace_class: frontier_discovery
target_claim_id: two_cube_l1_clock_source_shared_face
target_blocker_text: "whether F and the pair of cube occupancy increments are related by a unique shared-face correction rather than by identifying F with rho"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied two-cube L1 patch for two ticks; no full Z^3 history, rate, or physical source bridge"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded integer identity"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Record sentences quoted below supply lock
  permanence and unreadability of absence. They are quoted without rewrite.
- **Explicit theorem-domain condition:** the twelve-site two-cube patch, the
  seed, the occupancy kernel `n_mu = (o_{+mu}-o_{-mu})/3`, and the clock
  increment `F_tick = |new locks|` are supplied mathematical data for this
  note. They are not derived from the axiom memo.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** identifying `rho` with a physical source, or `F`
  with a physical time coordinate, remains outside the target proved here.

## Live Parent Quotes

> Records form.

> When present, a record locks exactly one admissible local possibility. A
> site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone.

Their dependency role is limited to lock permanence and the unreadability of
absence. The occupancy kernel, the two cubes, and the clock increment are
separately supplied.

## Exact Objects

All runner values are exact integers or rationals in `Q`. No float is used.

The patch vertices are the twelve sites of `A union B`. Shared-face vertices
are

```text
F* = {(1,0,0), (1,1,0), (1,0,1), (1,1,1)}.
```

Initial locks: `{(0,0,0)}`, so `rho(A)=1` and `rho(B)=0`.

**Tick 1.** Newly locked sites: `(1,0,0)`, `(0,1,0)`, `(0,0,1)`.
Then `F_tick=3`, `S=1`, `rho(A)=4`, `rho(B)=1`.

**Tick 2.** Newly locked sites: `(1,1,0)`, `(1,0,1)`, `(0,1,1)`, `(2,0,0)`.
Then `F_tick=4`, `S=2`, `rho(A)=7`, `rho(B)=4`.

## Exact Target And Proof Obligations

The exact target is the shared-face identity on these two ticks, together
with the cube-by-cube lock-count reading of `Delta rho`.

The obligation graph is:

1. reconstruct the displayed `L1` kernel on the twelve-site patch;
2. compute new locks, `F_tick`, `S`, and both cube increments on each tick;
3. check `Delta rho(C) = |new locks intersect C|` for `C in {A,B}`;
4. check `Delta rho(A)+Delta rho(B) = F_tick + S`;
5. check uniqueness of `S` in `{0,1,2,3,4}` and the mismatch with the union
   occupancy increment.

All five obligations are closed below and in the runner. Sites off the
displayed patch, later ticks, and any physical naming of `rho` or `F` are
outside this theorem.

## Theorem 1 — cube increments count new locks, shared sites twice

A newly locked site in `A \ B` raises only `rho(A)`. A newly locked site in
`B \ A` raises only `rho(B)`. A newly locked site in `F*` belongs to both
cubes and raises both sums. Therefore

```text
Delta rho(A) = |new locks intersect A|,
Delta rho(B) = |new locks intersect B|.
```

Tick 1: three new locks lie in `A` and one of them, `(1,0,0)`, lies in `B`.
Tick 2: three new locks lie in `A` and three lie in `B`, of which two lie in
`F*`.

## Theorem 2 — clock plus shared-face count equals the sum of cube increments

The clock increment counts each new lock once:

```text
F_tick = |new locks| = |new locks intersect (A union B)|.
```

Adding the two cube increments counts each shared-face new lock twice. The
difference is exactly `S = |new locks intersect F*|`, which rearranges to

```text
Delta rho(A) + Delta rho(B) = F_tick + S.
```

Tick 1: `3+1 = 3+1 = 4`. Tick 2: `3+3 = 4+2 = 6`.

## Theorem 3 — the shared-face correction is unique on the displayed face

`|F*|=4`. For each displayed tick the equation
`Delta rho(A)+Delta rho(B) = F_tick + s` has exactly one solution
`s in {0,1,2,3,4}`, namely `s=S`. In particular `F_tick` is not equal to
`Delta rho(A)+Delta rho(B)` on either tick, so the clock increment is not
the pair-sum of cube source increments.

The union occupancy increment on the twelve-site patch equals `F_tick` and
therefore is also unequal to `Delta rho(A)+Delta rho(B)`. The pair-sum is
not a clone of `sum o` on the union.

## What Is Not Claimed

- No third cube, no further tick, and no continuum limit.
- No identification of `rho` with a physical mass or of `F` with a physical
  time coordinate.
- No axiom edit and no replacement of the live Record sentences.
- No claim that `F_t = rho(A)_t` as functions of time; those integers meet
  or miss according to seed counting and B-only locks, which is a separate
  comparison.

## Runner Contract

The companion runner reconstructs the occupancy kernel on the displayed
patch, executes the two ticks, and checks Theorems 1–3 with exact integer
arithmetic. It prints `TOTAL: PASS=... FAIL=...` and writes no cache.
Declared review inputs are this note and the axiom memo only.

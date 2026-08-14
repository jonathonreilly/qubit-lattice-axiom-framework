---
claim_id: two_cube_first_wave_k_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "From seed (0,0,0) on the displayed two-cube occupancy step, the three first-wave sites (1,0,0), (0,1,0), (0,0,1) each have k=|3n|^2=1. After that step the next-wave face-diagonals have k=2 and the forming B-front site (2,0,0) has k=1. Forming k lies in {1,2,3}."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_first_wave_k_2026_08_14.py
---

# First-Wave Formations From The Corner Seed Have `k=1`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `k=|3n|^2` at first-wave sites and the displayed next-wave
table on one two-cube occupancy step.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_first_wave_k_2026_08_14.py`](../scripts/two_cube_first_wave_k_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Twelve vertices, two cubes sharing `x=1`. Occupancy step: locked
sites stay; unread sites form iff `n ≠ 0`. Off-patch occupancy is
`0`. The three-axis field is

```text
n_μ = (o_{+μ} − o_{-μ}) / 3
k   = |3n|^2 ∈ {0,1,2,3}
```

Each component of `3n` is in `{-1,0,1}`, so forming sites have
`k ∈ {1,2,3}`.

Seed `{(0,0,0)}`. The three first-wave sites are the on-patch
axis neighbors `(1,0,0)`, `(0,1,0)`, `(0,0,1)`. Each has one
unbalanced axis and `k=1`. That is the spectral type of the
gravity step's first records.

After that step the next wave is the three face-diagonals and the
B-front. Face-diagonals each have `k=2`. The B-front site
`(2,0,0)` has `k=1` and forms; the other three B-only vertices
have `k=0` and stay unread. Displayed forming next-wave `k` values
lie in `{1,2} ⊂ {1,2,3}`. The remaining type `k=3` appears at the
space diagonal `(1,1,1)` after the face-diagonal wave; it is
displayed as the third type, not as a first-wave record.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact k=|3n|^2 at the three first-wave sites and the displayed next-wave table."
trace_class: frontier_discovery
target_claim_id: two_cube_first_wave_k
target_blocker_text: "spectral type of the gravity step first records is unpinned"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed seed step and next-wave table"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name `k` or this first-wave table.

## Exact Objects

```text
A = [0,1]^3,  B = [1,2]×[0,1]×[0,1]
seed          {(0,0,0)}
first wave    (1,0,0), (0,1,0), (0,0,1)
face-diags    (1,1,0), (1,0,1), (0,1,1)
B-front       (2,0,0), (2,0,1), (2,1,0), (2,1,1)
```

On the seed,

```text
n(1,0,0) = (−1/3, 0, 0)     k = 1
n(0,1,0) = (0, −1/3, 0)     k = 1
n(0,0,1) = (0, 0, −1/3)     k = 1
```

After the first wave,

```text
n(1,1,0) = (−1/3, −1/3, 0)  k = 2
n(1,0,1) = (−1/3, 0, −1/3)  k = 2
n(0,1,1) = (0, −1/3, −1/3)  k = 2
n(2,0,0) = (−1/3, 0, 0)     k = 1
n(2,0,1) = (0, 0, 0)        k = 0
n(2,1,0) = (0, 0, 0)        k = 0
n(2,1,1) = (0, 0, 0)        k = 0
```

After the next forming wave, `n(1,1,1)=(−1/3,−1/3,−1/3)` and `k=3`.

## Theorem 1 — first-wave sites

Seed `(0,0,0)`. One occupancy step forms exactly
`(1,0,0)`, `(0,1,0)`, `(0,0,1)` among the twelve vertices.

## Theorem 2 — first-wave `k=1`

Each of those three sites has `k=|3n|^2=1` on the seed. Each has
exactly one unbalanced axis.

## Theorem 3 — next wave `k ∈ {1,2,3}`

After the first wave the three face-diagonals have `k=2` and form.
The B-front site `(2,0,0)` has `k=1` and forms. Forming next-wave
`k` values lie in `{1,2} ⊂ {1,2,3}`. The type `k=3` is displayed
at `(1,1,1)` after that wave.

## Theorem 4 — display

`k` is displayed extra. Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “a first-wave site has `k=2`” must fail.
2. Predicate “a next-wave face-diagonal has `k=0`” must fail.

Identity gates: `nvec`, `k_of`, `occ_step`, `first_wave`, `next_wave_k`.

## Honest-auditor / Boundary

Three first-wave sites, one next-wave table. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
- Not a unique occupancy kernel. Not a Born law.

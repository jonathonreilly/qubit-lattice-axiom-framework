# Separated pairs are lawful — the two-source sector opens at distance two — Cycle 735

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle735_separated_pair_lawful_control_2026_07_28.py`](../scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py)
- [`frontier_cycle735_separated_pair_independent_check_2026_07_28.py`](../scripts/frontier_cycle735_separated_pair_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 734 froze the adjacency wall and observed that its invariant is
silent on separated tokens; the lawful update advances every token one
station per step, so pairwise ring distance is a constant of motion —
separated tokens can never become adjacent. This cycle tests exactly
that domain and finds it **open**:

- **distance-parameterized templates**: the position-free pattern
  extends to `W(position, d)` for `d ∈ {2,3,4,5}` (positive-shortest
  representative; `d` and `11 − d` are the same unordered separation)
  — pure-X words of 4/5/6/7 gates, bit-exact lawful outputs at all 44
  `(position, d)` cases, exact translation covariance at every
  distance (121 identities each; 484 total);
- **count-2 enforcement**: the unchanged parameterized Cycle-731
  constructor accepts all 44 separated pairs; count witnesses refuse;
- **the invariant-checked full orbit — zero violations anywhere**: all
  44 orbits run to exact closure (484 controller steps; 5,324 station
  checks; 968 occupied-station checks; constant pairwise distance
  verified at every step; all register returns exact). The composition
  reference is K's own machinery — `global_allocator_word(2)` applied
  exactly twice to the held genesis — and K's own lawful-behavior
  certificates (controlled-truth, held-orbit, order-and-domain) rerun
  as passing baselines. `frozen_obstruction: null`;
- **the boundary is exactly adjacency**: the `d = 1` control reproduces
  the Cycle-734 wall — 22 step-0 violations (two per position) — so
  the lawful distance domain is `[2, 5]` with the frozen 734 census as
  its boundary;
- deletion controls on every template; the Cycle-734 anchors (pair word
  and frozen obstruction) rerun unchanged.

`separated_pair_lawful_control: true`; `two_source_composition_ring11:
true`. In W4's language this is **bounded separated multi-source
composition**: two sources move lawfully at ring-11 scope with supplies
declared. W4's renewal component is untouched.

## Supplied / derived / open

### Supplied

- the external application-position and separation parameters (neither
  is a distinguished site); the finite oriented ring-11 geometry; the
  held two-bank program content and order; the held direction data
  genesis with blank B/work and clean auxiliaries; `h = 0` lawful
  charge-reference rows and `expected_count = 2`; the Q-before-R
  controller layer order.

### Derived

- the distance-parameterized templates, their exactness and covariance;
- count-2 acceptance across the domain;
- the exhaustively invariant-checked lawful orbits with exact closure,
  constant distance, and the null obstruction;
- the adjacency boundary reproduction; deletion controls; unchanged
  anchors.

### Open

- three or more sources, and rings beyond 11, as uniform families;
- W4's renewal component (post-capacity renewal) — untouched here;
- the adjacent-pair wall itself (frozen in Cycle 734) — respected, not
  solved: whether a modified controller lawfully handles adjacency is
  a separate construction;
- everything the landed surfaces leave open at their scopes; no
  time/Record/Born/source content is touched.

## Negative-claim discipline

No negative claim ships. The lawful-domain statement `[2, 5]` is a
positive result whose boundary cites the already-frozen Cycle-734
census; it adds no new obstruction claim.

## Verdict

The multi-token program splits exactly along the invariant's own line:
adjacency is walled (Cycle 734, frozen, reproduced), separation is
lawful (this cycle, exhaustive, null obstruction). Two independently
prepared, boundary-free sources now compose and move lawfully on the
held fixture under the unchanged controller with the unchanged
certificate — the first W4 movement of the campaign. Independent audit
still required.

# The pairwise-separated multi-source sector — all 199 configurations lawful — Cycle 736

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle736_pairwise_separated_multisource_2026_07_28.py`](../scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py)
- [`frontier_cycle736_multisource_independent_check_2026_07_28.py`](../scripts/frontier_cycle736_multisource_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 735 opened the two-source sector at distance two. The invariant
is local and pairwise distance is conserved, so the natural closure is
the full sector: **every pairwise-separated configuration is lawful.**
Proven exhaustively on ring-11:

- **the configuration census is the Lucas number**: the pairwise-
  separated A-masks are exactly the independent sets of the cycle
  graph C₁₁ — per-k counts 1/11/44/77/55/11 for k = 0..5 (k ≤ 5 is
  the C₁₁ independence bound), total **199 = L(11)**, with the direct
  enumeration and the closed-form recurrence agreeing;
- **one template prepares them all**: the config-parameterized pure-X
  template produces every census configuration bit-exactly (token
  mask, matching reference rows, `h = k mod 2` — the **first h = 1
  odd-sector multi-token states** in the program), with the
  no-distinguished-site AST audit and an exact covariance census of
  2,189 conjugation identities;
- **count-k enforcement, the full grid**: the unchanged parameterized
  Cycle-731 constructor accepts all 199 diagonal cases
  (`expected_count = k` on a count-k config) and refuses all 995
  cross cases (`expected_count ≠ k`), with lawful parity rows in both
  `h` sectors;
- **every orbit is lawful**: all 199 configurations (including the
  empty and single-token controls) run full controller orbits to
  exact closure with per-step invariant checks at every occupied
  station, constant pairwise distances, exact register returns — zero
  violations anywhere; `frozen_obstruction: null`;
- **the boundary stands exactly where Cycle 734 froze it**: eight
  near-miss controls (a distance-1 pair somewhere) violate at step 0
  at precisely the predicted stations (two per adjacent pair).

`pairwise_separated_sector_lawful: true`;
`k_source_composition_ring11: true`. In W4's language: bounded
multi-source composition for **arbitrary pairwise-separated source
configurations** at ring-11 scope — up to five sources, both parity
sectors — under the unchanged controller and certificate.

## Supplied / derived / open

### Supplied

- the configuration as an external parameter (no distinguished site);
  the finite oriented ring-11 geometry; the held program content and
  order; the held data genesis with clean auxiliaries; lawful
  charge-reference rows with `h = k mod 2` and `expected_count = k`;
  the Q-before-R layer order.

### Derived

- the census equality (enumeration = Lucas closed form);
- template exactness and the covariance census over the full sector;
- the complete acceptance/cross-refusal enforcement grid;
- the exhaustive invariant-checked lawful orbits with null obstruction;
- the near-miss boundary controls.

### Open

- rings beyond 11 as uniform families (the census generalizes as
  L(n); the theorem here is ring-11 exhaustive, not uniform);
- W4's renewal component (post-capacity renewal) — untouched;
- adjacent-pair control (the Cycle-734 wall) — respected, not solved;
- everything the landed surfaces leave open at their scopes; no
  time/Record/Born/source content is touched.

## Negative-claim discipline

No negative claim ships. The k ≤ 5 bound is the C₁₁ independence
number, a combinatorial fact of the fixture, not an obstruction claim.

## Verdict

The multi-source program on ring-11 is now complete on its lawful
side: the sector of lawful configurations is exactly the independent
sets of the ring (199 of them, the Lucas number), every one preparable
by one position-free template, enforceable by one parameterized
certificate in both parity sectors, and lawful under the unchanged
controller — with the adjacency wall as the exact, frozen, reproduced
boundary. Independent audit still required.

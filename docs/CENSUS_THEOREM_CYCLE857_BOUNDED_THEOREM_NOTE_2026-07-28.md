# The census theorem — why exactly 748 starting conditions — Cycle 857

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the closed-form counting law with
structural certification; the bit accounting; the constraint
contribution table)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle857_census_theorem_2026_07_28.py`](../scripts/frontier_cycle857_census_theorem_2026_07_28.py)
- [`frontier_cycle857_census_independent_check_2026_07_28.py`](../scripts/frontier_cycle857_census_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The size of the starting-condition space is a THEOREM, not a fact of
enumeration:

- **the counting law**: for k = 2..5 sources,
  **N_k = C(10-k, k-1) x 4 x 11 / k**, giving exactly
  176 + 308 + 220 + 44 = **748 = 68 x 11**;
- **certified structurally, not just numerically** (the checker's
  verdict `STRUCTURE_CERTIFIED`): C(10-k, k-1) counts the
  separation-admissible spacing patterns via an explicit bijection,
  4 the phases, 11 the origins, and /k the source-label quotient —
  each factor mapped to its census axis, with integrality of the
  quotient certified per stratum;
- **the bit accounting is exact**: log2(748) = log2(68) + log2(11) —
  the input decomposes as 6.09 bits of family choice + 3.46 bits of
  within-family (allocation) choice, the free-action factorization in
  information form;
- **the constraint table**: each admissibility constraint's exclusion
  contribution computed by relaxation (792 / 748 / 4048 / 935) and
  tightening (572 / 704 / 220 / 561); the no-op identified — the
  packing window at k<=5 is IMPLIED by the separation rule at this
  scope (relaxing it changes nothing);
- every parameter of the space (ring size 11, phase count 4, the
  separation rule) is an axiom/core constant: **the SET of possible
  worlds is fully derived; only the selection within it is input.**

**Why so many, answered**: 748 is the exact combinatorics that the
admissibility rules permit — no more, no fewer, each factor's origin
named. The multiplicity is not freedom in the theory; it is the size
of one derived object.

## Supplied / derived / open

### Supplied

- the 719 core (sha-pinned); everything the cited packages declare.

### Derived

- the counting law with per-factor bijections; the stratum and orbit
  totals; the bit decomposition; the eight-entry constraint table
  with the implied-constraint identification.

### Open

- the counting law at general ring size n (the natural
  generalization: is C(n-1-k, k-1) x phases x n / k the law wherever
  the separation rule holds?); composite-n behavior (ties to the
  free-action scope question of Cycle 852).

## Negative-claim discipline

The law is certified at the audited s=5 window scope (k = 2..5, ring
11, phases 4); the general-n form is named as open, not claimed.

## Verdict

Seven hundred forty-eight is not a large number of worlds; it is one
binomial identity wearing four phases and eleven origins. The set of
possible beginnings is now as derived as the dynamics that follows
them — what remains free is nine and a half bits of choice, and we
know exactly where each bit lives. Independent audit still required.

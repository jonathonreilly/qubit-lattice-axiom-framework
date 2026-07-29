# Ring-family uniformity — the sector theorem holds at every admissible ring, and the ring is not free — Cycle 737

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle737_ring_family_uniformity_2026_07_28.py`](../scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py)
- [`frontier_cycle737_ring_family_independent_check_2026_07_28.py`](../scripts/frontier_cycle737_ring_family_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 736 proved the multi-source sector theorem exhaustively at
ring-11 and left rings beyond 11 open. This cycle finds two things: the
theorem generalizes, and the ring size was never a free choice.

- **admissibility is derived, not declared**: the controller core's own
  program/bank arithmetic forces `n = 8b − 5` stations for `b` banks —
  the admissible rings are `{3, 11, 19, 27}` for `b = 1..4`. The
  familiar ring-11 is just `b = 2`. Non-family sizes fail the
  constructor's own requirements. Within the admissible family, the
  "supplied ring geometry" of every earlier cycle reduces to **one
  integer: the bank count**;
- **the sector theorem is uniform over the family**: at every
  admissible `n`, the pairwise-separated census equals the Lucas
  closed form — **4 / 199 / 9,349 / 439,204** configurations for
  `n = 3 / 11 / 19 / 27` — with direct enumeration and recurrence
  agreeing; the config-parameterized template is bit-exact for every
  configuration at every `n`; the count-k enforcement grid is exact
  (counter width scaling as declared); and **every configuration at
  every ring runs its invariant-checked orbit to exact closure** —
  12 / 2,189 / 177,631 / 11,858,508 orbit steps exhausted with zero
  invariant, distance, register, or inverse failures;
- **the adjacency boundary reproduces at every ring**: near-miss
  controls violate at exactly two stations per adjacent pair at each
  `n`;
- `frozen_n_dependence: null` — no component of the machinery is bound
  to `n = 11`. The claim is family-uniform (each member exhaustive),
  **not** a general-`n` theorem: `b ≥ 5` rings are untested, and the
  uniformity statement is the conjunction of four exhaustive theorems,
  not an induction.

## Supplied / derived / open

### Supplied

- the bank count `b` (one integer per family member); the held program
  content and order per ring; the held data genesis with clean
  auxiliaries; lawful charge-reference rows with `h = k mod 2` and
  `expected_count = k`; the Q-before-R layer order; the configuration
  as an external parameter.

### Derived

- the admissibility law `n = 8b − 5` from the controller's own
  arithmetic (the ring size is a function of the bank count, not an
  independent supply);
- the per-`n` Lucas census equalities; template exactness and
  covariance; the enforcement grids; the exhaustive invariant-checked
  lawful orbits at all four rings; the boundary controls.

### Open

- `b ≥ 5` and an inductive general-`n` theorem (the natural conjecture
  is now precise: the sector theorem for all `n = 8b − 5`);
- W4's renewal component; adjacent-pair control; everything the landed
  surfaces leave open at their scopes; no time/Record/Born/source
  content is touched.

## Negative-claim discipline

No negative claim ships. Non-family ring sizes failing the constructor
is a derived arithmetic fact about the landed machinery, stated with
the exact failing requirement, not an impossibility claim about other
controllers.

## Verdict

The multi-source sector theorem is not a ring-11 accident: it holds
exhaustively at every ring the machinery itself admits, and the
machinery admits exactly the rings `n = 8b − 5`. A supply that every
cycle since 719 has carried — "finite oriented ring geometry" — is now
one derived formula plus one integer. The W2 ledger line should read:
geometry is bank-counted, not freely supplied. Independent audit still
required.

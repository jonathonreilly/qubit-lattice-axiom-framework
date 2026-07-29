# The sixth anchor — b = 6, seventeen billion steps, the bound stated — Cycle 761

Date: 2026-07-29

Authority: none

Audit: unset

Status: bounded conditional theorem (k ≤ 11 exhaustive; the residual
counted, not swept)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle761_b6_exhaustive_anchor_2026_07_28.py`](../scripts/frontier_cycle761_b6_exhaustive_anchor_2026_07_28.py)
- [`frontier_cycle761_b6_anchor_independent_check_2026_07_28.py`](../scripts/frontier_cycle761_b6_anchor_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The anchor program's sixth ring (`b = 6`, `n = 43`, `C = 6`), with the
coverage bound chosen honestly against the budget rather than forced:

- **census**: `L(43) = 969,323,029` total pairwise-separated
  configurations, streamed per stratum, recurrence-matched
  (independently recounted);
- **the swept domain**: all strata `k = 0..11` — **402,580,148
  configurations, 17,310,946,364 station-steps — zero violations of
  any invariant**, swept exhaustively twice (primary ~24 minutes;
  the checker's faster evaluator, 333 seconds);
- **the residual, stated**: strata `k = 12..21` — 566,742,881
  configurations — **counted exactly but not swept**; no full-sweep
  claim is made;
- rows: all 43 emitted `b = 6` rows pass clean-work — the identity's
  direct evidence extends to a sixth bank count;
- near-miss controls: 43/43.

## Supplied / derived / open

### Supplied

- everything the Cycle-737/739/740 packages declare per family member.

### Derived

- the streamed census; the k ≤ 11 exhaustive double-swept anchor; the
  b = 6 row evidence; the boundary controls.

### Open

- the k ≥ 12 strata of n = 43 (counted; a longer-budget sweep or a
  smarter argument); b ≥ 7; the general-b statement unchanged;
  everything inherited at original scopes.

## Negative-claim discipline

No negative claim ships. The coverage bound is a budget statement.

## Verdict

Six rings anchored, the sixth with its bound printed on the label —
the anchor program now runs ahead of what any conjecture asked of it.
Independent audit still required.

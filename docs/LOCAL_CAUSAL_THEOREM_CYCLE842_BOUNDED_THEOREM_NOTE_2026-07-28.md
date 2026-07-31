# The bounded theorem holds; the local one still hides — Cycle 842

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the wire dynamics; the bounded
marked-meet theorem; the invariant failures; the class-bounded open)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle842_local_causal_theorem_2026_07_28.py`](../scripts/frontier_cycle842_local_causal_theorem_2026_07_28.py)
- [`frontier_cycle842_theorem_independent_check_2026_07_28.py`](../scripts/frontier_cycle842_theorem_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The attempt to turn the three-wire representation into a local causal
theorem:

- **the wire dynamics are exact**: the update clauses reading and
  writing wires 40 / 81 / 105 derived with provenance — all three are
  WRITABLE (no trivial conservation is available);
- **the bounded theorem holds**: every predicate-marked meet reaches
  the exact weight-44 funnel within B = 162126, and every one of the
  35 unmarked controls does not (checker re-verified on its declared
  samples);
- **the local argument fails where it was tried**: predicate
  conservation fails at tick 6; marked-trajectory Hamming distance to
  the skeleton INCREASES at tick 4 — both counterexamples reproduced
  by the checker; its two additional invariant/monotone classes were
  exhausted without a find;
- **the open is class-bounded**: the non-lookahead local causal link
  remains open, with four candidate classes now excluded exactly.

## Supplied / derived / open

### Supplied

- the 839/840 meet machinery (sha-pinned); the landed rules;
  everything the cited packages declare.

### Derived

- the wire dynamics; the bounded theorem both directions; the two
  failure counterexamples; the class exhaustions.

### Open

- the local causal theorem (four invariant classes excluded); the
  pulse phase (the sibling cycle).

## Negative-claim discipline

The bounded theorem is exact at B on the censused meets; the failures
are witnessed; no local claim is made.

## Verdict

Causation keeps its secret for one more round: the marked meets always
arrive, nothing simple explains why, and four more explanations are
now dead on the record. Independent audit still required.

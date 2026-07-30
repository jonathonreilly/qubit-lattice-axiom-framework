# The lock that held against one word and fell to its prefixes — the composition result, adversarially corrected — Cycle 770

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (adversarially corrected; no permanence
witness established; the failure mechanism exact; the repair target
named)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle770_lock_composed_formation_2026_07_28.py`](../scripts/frontier_cycle770_lock_composed_formation_2026_07_28.py)
- [`frontier_cycle770_lock_composed_independent_check_2026_07_28.py`](../scripts/frontier_cycle770_lock_composed_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 769 ended with the composition experiment fully specified: wrap
the mode-6 branch's record write with the Cycle-745 refusal lock and
ask whether the reversible surface's un-write is now refused. This
cycle ran it, and the adversarial exchange decided the answer:

- **the composition works against the words it was built from**: with
  the lock engaged after the finalizer, the compiled inverse word's
  write-backs are refused at steps 4, 128, and 129 with syndrome
  receipts, and the EventCell survives byte-exactly; a simple foreign
  hostile write is also refused; modes 0/2/3/4/5 and fresh writes
  elsewhere are untouched (no over-blocking, no early engagement —
  the checker verified the pre-finalizer trace is the landed dynamics
  bit-exactly);
- **and the checker's hostile-word battery refuted the witness**: of
  26 distinct attacks, only **5 are refused** — **truncated
  reverse-word prefixes 6 and 7 mutate all 744 lock rails without
  triggering refusal**. The lock guards the record cell against the
  complete un-writing word, but its own rails are ordinary mutable
  state against partial words: a guard that can be dismantled by a
  lawful prefix is not permanence;
- **the v2 verdict, verbatim**: `permanence_witness_established:
  false`; `refused_attacks: 5/26`; `failure_mechanism: "truncated
  reverse prefixes mutate the lock rails without refusal"`; both
  classification readings recomputed under the verbatim 769 rule:
  `classification_if_no_write_counts: unidentified`,
  `classification_if_no_write_does_not_count: unidentified` — the
  census stands exactly where Cycle 769 left it;
- **the repair target, named as open work**: a **prefix-closed refusal
  law** (refusal engages on every prefix of every un-writing word) or
  **rail-guarded locking** (the lock's own state protected by the same
  refusal law it enforces). Neither exists on the landed surface
  today; deriving one is the formation lane's exact next wall.

## Supplied / derived / open

### Supplied

- the composition point (lock engages at finalizer decodability);
  everything the Cycle-693/719/745/769 packages declare at their
  scopes.

### Derived

- the composed system's behavior against the full 26-attack battery
  (5 refused, per-attack mutation sites printed); the exact failure
  mechanism with prefix lengths and rail counts; the dual-reading
  classification recompute; the collateral and engagement-point
  controls.

### Open

- the prefix-closed refusal law or rail-guarded locking (the named
  derivation targets); the permanence-witnessed census (still
  waiting on a real witness); multi-origin charts; everything
  inherited.

## Negative-claim discipline

"No permanence witness established" is the corrected finding at this
composition's scope; it does not assert that no composition can
succeed — the two named repair routes are exactly the untested
remainder.

## Verdict

The refusal lock is real but shallow: it stops the one word it was
derived against and nothing shorter. Permanence — the axiom's word —
demands a guard with no lawful dismantling sequence, and the landed
surface does not yet contain one. That is a sharper statement of the
formation wall than Cycle 769 could make, and it is this cycle's
result. Independent audit still required.

# The balance is a theorem — parity-conjugate pairs and twenty-three on each side — Cycle 793

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the enlarged orientation census; the
balance mechanism identified; supply-independent)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle793_enlarged_orientation_census_2026_07_28.py`](../scripts/frontier_cycle793_enlarged_orientation_census_2026_07_28.py)
- [`frontier_cycle793_balance_independent_check_2026_07_28.py`](../scripts/frontier_cycle793_balance_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 786 found the landed 38 epochs split exactly 19/19 by
orientation; Cycle 788 extended the family to 46. This cycle asked
whether the balance survives — and found out why it must:

- **the enlarged census: 23/23** — and **every bank balances
  individually**: bank 1 splits 1/1, bank 3 splits 3/3, and the landed
  banks 2/5/12 split 2/2, 5/5, 12/12 (the landed 19/19 reproduced
  exactly as the identity control);
- **the mechanism, found by the checker**: the balance is
  **structurally forced** — the epoch-family constructor produces
  **parity-conjugate pairs** (each even-indexed epoch 2j maps 1:1 to
  its orientation-conjugate 2j+1). Every bank of any size contributes
  equally to both orientations by construction. The perfect balance is
  a theorem of the constructor, not a statistic;
- **supply-independent**: under all 20 selecting-supply variation
  cases (the 788 layer), every orientation is preserved — zero flips.
  The balance datum does not inherit the convention caveat;
- boundaries: counts only; no weights, no rate law, no probability;
  `axiom_update_triggered: false`.

**What this gives the occurrence lane**: its first structural
distribution law at the landed correspondence resolution — the
orientation marginal is exactly uniform, provably, at every bank size,
independent of the supply layer. Any future rate law inherits this as
a constraint it gets for free — and everything finer than orientation
remains exactly as open as Cycle 786 quantified.

## Supplied / derived / open

### Supplied

- everything the Cycle-719/750/786/788 packages declare (the new
  events' existence carries the 788 supply layer; their orientations,
  by the supply probe, do not).

### Derived

- the 46-event census with per-bank structure; the parity-conjugate
  pairing mechanism with module evidence; the supply-independence of
  orientations; the identity control.

### Open

- the per-origin refinement (unchanged); the rate/site-distribution
  law (which now must reproduce exact orientation uniformity).

## Negative-claim discipline

No negative claim ships; the mechanism statement is scoped to the
landed constructor.

## Verdict

What looked like a curiously perfect coin flip is the constructor
showing its symmetry: every epoch arrives with its mirror twin, at
every bank size, under every declared supply. The first distribution
fact of the occurrence program is not a measurement — it is a theorem.
Independent audit still required.

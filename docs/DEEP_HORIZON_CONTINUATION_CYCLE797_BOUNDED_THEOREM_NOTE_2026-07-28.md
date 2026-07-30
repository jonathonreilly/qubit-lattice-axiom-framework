# Two more doublings, nothing moves — the stability of the open set — Cycle 797

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the null continuation at T = 4096;
coverage proven; every hypothesis survives)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle797_deep_horizon_continuation_2026_07_28.py`](../scripts/frontier_cycle797_deep_horizon_continuation_2026_07_28.py)
- [`frontier_cycle797_continuation_independent_check_2026_07_28.py`](../scripts/frontier_cycle797_continuation_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

After T = 1024 left 162 keys open, this cycle doubled the horizon
twice more — and the honest result is stability:

- **zero new resolutions at T = 2048 and T = 4096**: no new first-clean
  event, no new certifiable cycle; the family stays **2 transients
  (252, 371) / 12 certified cycles / 162 open**;
- **the null is proven, not assumed**: the checker re-swept all 162
  keys to 4096 with its own evolution, the landed cleanliness test,
  and its own cycle-hashing granularity — nothing missed, nothing
  spurious; coverage verified by transition accounting
  (165,888 + 331,776 = 497,664 evaluations); the 12 cycles persist;
  the transients do not reappear;
- **every hypothesis survives**: with no new resolutions, all 103
  separator hypotheses (46 forecast vectors) remain live — the
  discriminator question is untouched;
- the k = 2 transients are confirmed early outliers: the open set is
  deeply stable across a 16-fold horizon range (256 → 4096).

## Supplied / derived / open

### Supplied

- everything the Cycle-719/736/762/790/791/795 packages declare.

### Derived

- the full-coverage continuation at both horizons; the null result
  with independent verification; the persistence and non-reappearance
  controls; the hypothesis-survival statement.

### Open

- the 162 keys (deeper horizons — each eventual resolution remains a
  sharp hypothesis test); the content-vs-dirt ruling; the k ≥ 3
  horizon question (scanned in parallel as Cycle 798).

## Negative-claim discipline

The null is scoped to T ≤ 4096 at the censused keys with proven
coverage; nothing is extrapolated beyond it.

## Verdict

Sixteen times past the first surprise, the family has gone quiet: two
early transients, twelve permanent cycles, and a hundred sixty-two
keys that keep their counsel. Stability at this depth is itself a
datum — whatever law explains the transients must also explain why
they are rare. Independent audit still required.

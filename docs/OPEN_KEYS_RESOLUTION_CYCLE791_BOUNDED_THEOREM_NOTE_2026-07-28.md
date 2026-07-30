# The open keys at a thousand steps — two transients, twelve cycles, and a family that keeps its secrets — Cycle 791

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the resolution census at T = 1024;
content-vs-dirt open with evidence on both sides)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle791_open_keys_resolution_2026_07_28.py`](../scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py)
- [`frontier_cycle791_resolution_independent_check_2026_07_28.py`](../scripts/frontier_cycle791_resolution_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 790 left 164 keys open through T = 256. This cycle took them to
T = 1024:

- **a second transient**: key (3, (0,7)) is nonclean at every t < 371
  and clean **exactly at t = 371** (checker verified with the landed
  test) — the first-clean distribution is now {252: 1, 371: 1};
- **a new certified cycle**: key (2, (0,9)) — entry 0, **state period
  288, residual period 6**, forever-nonzero by state recurrence
  (independently certified);
- **the fractions at T = 1024**: of the 176-key family — **2 clean
  (transients), 12 certified cycles, 162 still open**; coverage
  164/164 (the checker re-swept and found exactly one new clean and
  one new cycle — nothing missed, nothing spurious);
- the family resolves slowly: two doublings beyond the first surprise
  produced one more of each kind, and 92% of the family remains
  undetermined.

**What the census now says**: the veto's horizon-relativity is real
but rare at these horizons — and the content-vs-dirt question has
genuine evidence on both sides (two residuals that were dirt after
all; twelve that are provably permanent structure; the rest unknown).
The horizon-extended postimage law remains the derivation target, with
its evidence base now two events deep.

## Supplied / derived / open

### Supplied

- everything the Cycle-719/736/762/790 packages declare.

### Derived

- the T = 512/1024 resolution sweep with full coverage; the t = 371
  event and its firstness; the period-288/6 cycle certification; the
  fractions; the divisibility extension.

### Open

- the 162 open keys (horizons beyond 1024); the content-vs-dirt
  ruling; the horizon-extended postimage law.

## Negative-claim discipline

Existence facts and certified cycles at their named keys; the open set
is labeled open, never extrapolated.

## Verdict

A thousand steps in, the family has answered for fourteen of its
hundred seventy-six members and keeps the rest waiting. Two came
clean; twelve never will; the law that must explain the difference is
now the sharpest object in the multi-source program. Independent audit
still required.

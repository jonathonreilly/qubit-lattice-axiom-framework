# The clocks that matter agree — deciding the tick — Cycle 841

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the three-clock formalization; the
forcing table; the physics-consumer census; the principled accounting)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle841_deciding_the_tick_2026_07_28.py`](../scripts/frontier_cycle841_deciding_the_tick_2026_07_28.py)
- [`frontier_cycle841_tick_independent_check_2026_07_28.py`](../scripts/frontier_cycle841_tick_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

The moment law's +-1 was a timeline-convention question; this cycle
audits the definitions — with the checker enforcing the census's
completeness:

- **the three clocks, formalized with provenance**: MOMENT (the
  battery's first-clean full-orbit boundary: 14744 / 33195 / 51115);
  MOMENT-5 (the shared funnel-state tick: 14739 / 33190 / 51110);
  REGISTER-ENTRY (the earliest stable 39-field projection:
  14739 / 33189 / 51110);
- **the forcing table** (each row AST + behaviorally identified,
  checker-verified): the lock law reads MOMENT; the Cycle-796
  construction reads MOMENT; the funnel family map reads MOMENT-5;
  the pulse is origin-neutral relative phase;
- **the consumer census, corrected by the checker**: the v1 "zero
  landed consumers" for the register-entry clock missed three — the
  Cycle-835 audit certificates themselves; v2 classifies: **zero
  PHYSICS consumers** (no landed law or construction's content
  depends on that clock); the sole landed consumers are the
  self-referential audit artifacts that measured it;
- **the practical resolution**: no clock is landed-forced in the
  abstract, but every landed physics consumer reads MOMENT or
  MOMENT-5 — and on those clocks the raw, target-blind register
  catch-up equals **{595, 64} — the residuals, exactly, with no
  fitted terms**. The Cycle-835 near-miss dissolves: it was the
  reading of a clock no physics uses.

**What this closes**: the cohort-moment accounting —
gap = lcm(4464, 5952) + register catch-up on the physics clocks —
now holds principled end to end. What remains of the moment law: the
pulse phase, and the local causal theorem (Cycle 840's named gap).

## Supplied / derived / open

### Supplied

- the landed timing consumers and the 835 register data; everything
  the cited packages declare.

### Derived

- the three formalizations; the forcing table; the corrected consumer
  census with the physics/audit classification; the principled
  accounting.

### Open

- the pulse phase; the local causal theorem; whether future landed
  physics ever consumes the register-entry clock (which would reopen
  the question — stated as the standing condition).

## Negative-claim discipline

The census is scoped to the landed corpus as scanned (scope declared);
the accounting claim is exactly the target-blind computation on the
physics clocks; the v1 wording is corrected, not defended.

## Verdict

Asked which clock is real, the framework answered by usage: every law
it has reads one of two clocks, and on both of them the register's
arithmetic meets the cohorts' calendar exactly. The tick is decided by
the only vote that counts — the physics'. Independent audit still
required.

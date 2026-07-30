# Eight times deeper — the k = 4 cycles re-certified with minimality, and no selections anywhere — Cycle 814

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the complete deep continuation at
k = 4/5; the first k = 4 resolutions)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle814_deep_silence_probe_2026_07_28.py`](../scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py)
- [`frontier_cycle814_probe_independent_check_2026_07_28.py`](../scripts/frontier_cycle814_probe_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 813 proved the k >= 4 silence is not a conservation law; depth
was the remaining decidable probe. This cycle swept all 24 silent keys
COMPLETE to T = 65536 (1,572,864 transitions, accounting printed):

- **the two k = 4 cycles re-certified, now with minimality**:
  (4,(0,2,4,7),1) and (4,(0,2,4,8),1) — forever-nonclean cycles with
  exact period 4464; the checker verified exact state recurrence,
  MINIMAL period (all 29 proper divisors rejected — new here), and
  non-cleanliness through a full period plus the pre-period.
  CORRECTION (Cycle-818 exchange): these two cycles were FIRST
  certified by the landed Cycle-801 package at T = 8192 (its note:
  "k = 4's silence breaks the same way — its first two cycles ...
  both period 4464"); this cycle's spec inherited a wrong "silent
  through 8192" baseline from a campaign-state summary instead of the
  landed note. Cycle 814's actual contributions: the independent
  re-certification with minimality, the complete deep sweep, and the
  transient null below;
- **zero first-clean events**: no selection-type resolution appears
  anywhere at k = 4/5 through T = 65536 — eight times past the prior
  horizon;
- **the stratum period recurs**: 4464 is the same period the k <= 3
  strata produced in their late cycles — a cross-stratum regularity
  the eventual law must explain;
- **22 keys remain open**; the checker independently re-swept eight
  of them to T = 65536 with zero clean events (null spot-coverage);
- identity controls (444; 252; a known certified cycle) reproduce.

**What this does to the family** (corrected census, with Cycle 801's
four k = 3 period-5952 cycles counted): **6 transients / 18 certified
cycles / 184 open**. k >= 4 resolves into permanence, not selection —
zero first-clean events through T = 65536 — and the two-sided
higher-k fact stands: selections stop at k = 3 (so far), cycles do
not.

## Supplied / derived / open

### Supplied

- the landed cleanliness and cycle-certification tests (reimplemented,
  provenance-cited); everything the Cycle-719/736/758/790/791/792/
  794/798/801/813 packages declare.

### Derived

- the complete 24-key deep sweep with accounting; the two cycle
  certifications with minimal period; the cross-stratum period
  observation; the null for the rest.

### Open

- the 22 remaining k = 4/5 keys (deeper horizons); why selections
  (first-clean events) stop at k = 3 while cycles continue — now with
  the 813 constraint that the answer is not a linear/quadratic
  conservation law; the 162 open k <= 3 keys.

## Negative-claim discipline

The null is scoped to T <= 65536 at the 22 open keys with proven
coverage; the two certifications are exact and checker-verified; the
cross-stratum period note is an observation, not a law claim.

## Verdict

Depth was the last cheap question, and it paid twice: the silent
stratum turns out to keep permanent time — the same 4464-beat clock
the lower strata keep — while still never selecting. Independent
audit still required.

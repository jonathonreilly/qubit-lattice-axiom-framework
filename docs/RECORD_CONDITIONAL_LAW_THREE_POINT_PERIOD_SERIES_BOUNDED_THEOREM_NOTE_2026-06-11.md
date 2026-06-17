# The Three-Point Period Series (L=3,4,5) of the Record-Conditional U(1) Law: No Systematic Period Strengthening — the Min-Gain Ledger Replaces the Monotone/Stall Dichotomy

**Date:** 2026-06-11
**Type:** bounded_theorem (three-point period-series source proposal continuing PR #3555)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_record_conditional_law_three_point_period_series_2026_06_11.py`
**Cache:** `logs/runner-cache/frontier_record_conditional_law_three_point_period_series_2026_06_11.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=19 FAIL=0` checks exact
finite-tree/profile/rank/min-gain computations plus a deterministic fixed
300-permutation sampled-null comparison. It is **not** an exact full-permutation
or exhaustive permutation-null p95 certificate. **Memory contract respected by construction:** uniform
`expm_multiply` machinery across all three periods — the step unitary is *never*
materialized (a dense `U` at L=5 would be 17 GB); environments freed between periods;
measured **peak footprint ~2.5 GB** (`/usr/bin/time -l`; max RSS ~1.4 GB), single-run safe, panels serialize heavy recomputes.

## The series, and the criterion that had to die

#3555 established seed-robust fixed-k monotonicity at L=4. Extending to **L=5** (15
modes, 32,768-dim Fock; six seeds per the standing adversarial policy) exposed that the
*monotone/stall dichotomy itself* was criterion-sensitive: strict float inequality would
mislabel the #3554 stall (first gain `4×10⁻⁴`), while a 0.01 tolerance flips marginal
events. The honest statistic is **criterion-free: the minimum k-step gain**
`min(p₃−p₂, p₄−p₃)` per event, reported as a number.

## The findings (finite-tree exact; fixed sampled-null bounded — runner `PASS=19 FAIL=0`)

**(G1) The min-gain ledger — no systematic period strengthening:**

```
L=3  {0.0001, 0.155}                    one stall-like, one clear (event-specific)
L=4  {0.030, 0.029, 0.068}              uniformly CLEAR (the #3555 finding)
L=5  {0.014, 0.043, 0.051, 0.005, 0.028, 0.005}   4/6 clear, 2/6 MARGINAL
```

**Precision, panel-required:** #3555's *literal* headline criterion was **strict
monotonicity** (min-gain > 0) — and **that persists 6/6 at L=5** (gated in-runner;
min-gain > 0 is exactly equivalent to `p₂<p₃<p₄`). What does **not** persist is the gain
**magnitude**: L=4's uniform ≥ 0.029 drops to 2/6 marginal (~0.005) at L=5. The
weakening is of *clarity*, not of monotonicity — the strict signature survives
three-point (1/2, 7/7, 6/6).

**(G2) Fixed seeded sampled-null clearing drops from all-tested to typical:** against
the deterministic 300-permutation `p95` sample used by the runner, 5/6 L=5 seeds
clear; seed 20260611's most-spread event does **not** (gap `−0.030`) — the first
non-clearing event of the series, disclosed rather than averaged away — **a
sampled-null-clearing failure, not a monotonicity failure** (its min-gain is
positive). This is not claimed as an exact full-permutation null result.

**(G3) The gap medians are trendless:** `{~0.139, ~0.193, ~0.095}` for L = {3,4,5} —
fluctuating within overlapping ranges. The #3555 panel-corrected verdict
("comparable-or-larger, not doubled") extends: at three points there is **no growth
law**; gap magnitudes are event/seed-dominated.

## The three-point verdict — an honest negative that redirects

Across L = 3, 4, 5 the record-conditional structure **does not strengthen
systematically with the period**: gain magnitudes and sampled-null clearing both regress at
L=5, while the strict-monotonicity signature itself persists — #3555's magnitude
clarity was not the onset of a trend. **At
accessible periods the conditional law's structure is event/seed-dominated, and period
scans at these sizes cannot decide the conditional-law question.** The redirect this
buys: the next genuine lever on the R2 stationarity residual is **analytic, or a
different observable** — not larger rings.

## 2026-06-12 sampled-null scope repair

The permutation-null statistic in this source packet is a fixed, seeded,
300-permutation sampled-null p95 computed by the runner:

```text
null_p95(Theta, w, kpref=3, n_draws=300, seed=7777).
```

This is a deterministic source-packet certificate for the named finite samples
and seeds. It does not claim an exhaustive permutation-null p95, a certified
finite-sample upper confidence bound, or a Monte-Carlo-free null theorem. The
bounded positive retained for re-audit is therefore only:

```text
For the stated L=3/L=4/L=5 events, occupancies, seeds, depth choices, and
fixed 300-permutation sampled-null protocol, the three-point min-gain ledger
and sampled-null gap series have the displayed values.
```

## 2026-06-13 dependency-edge rescope repair

This note does not use the #3554 fixed-prefix-`k` packet, the #3555
period-scaling packet, the #3507 trajectory packet, or the Born-derived
chain/readout premises as load-bearing one-hop authorities. Those packets
name the historical route and vocabulary that led to this finite test, but
the current source-positive is exactly the finite-runner-defined diagnostic
above.

Load-bearing inputs are confined to the finite objects instantiated by
`scripts/frontier_record_conditional_law_three_point_period_series_2026_06_11.py`:

- ring sizes `L=3`, `L=4`, and `L=5`, color count `N_c=3`, named occupancies
  `K=5`, `K=7`, and `K=8`, and the displayed seed/depth choices;
- the explicit sparse Fock evolution and SVD-polar determinant readout
  constructed in the runner;
- the fixed seeded 300-draw sampled-null protocol
  `null_p95(Theta, w, kpref=3, n_draws=300, seed=7777)`;
- the displayed finite inequalities: the L=3 baseline set, L=4 and L=5
  min-gain ledgers, L=5 sampled-null non-clearing event, and gap-median
  no-period-trend comparison.

The symbols "Born", "record", "instrument", "C^3 carrier", "hopping",
"selector/null protocol", and "U(1)" are therefore labels for the finite
diagnostic instantiated in this runner, not imported framework closures. A
downstream row must not cite this packet as a retained derivation of the
#3554 fixed-prefix-`k` law, the #3555 period-scaling law, the #3507
Born/readout chain, a framework-native `C^3` carrier, named `eps/tau`
instruments, a selector/null theorem beyond the code-defined sampled
diagnostic, a record-conditional interpretation from approved premises, a
physical `U(1)` gauge field, an all-permutations null theorem, or a
large-period law.

## What this does and does not claim

- Not claimed: any exact full-permutation null certificate; asymptotic statement;
  concentration; CLT premises; `L≥6` behavior (full trees exceed the memory
  contract); `Z³` geometry (rings only — disclosed); gap or gain universality.
  All numbers seed/instance-labeled; the L=3 baseline events are
  **pinned at their landed depths** (the #3555 baseline-fairness lesson); six L=5 seeds
  including the prior adversarial set. **Selector-comparability caveat:** L=4/L=5 use
  the most-spread-row selector while L=3 is pinned — an asymmetry that is
  **conservative** for the negative verdict (worst-row picks and the pinned stall both
  lean toward marginality; it cannot manufacture the no-strengthening conclusion).
- Conditionality inherited from the linked period-scaling packet: the Born
  derived-chain cap (the audit lane grades; statuses volatile); named instruments
  (`ε=0.6`); supplied `C³` carrier; named hopping (`τ=0.35`); guarded full-rank
  domain; discrete-time throughout (retained R1 boundaries untouched). The `U(1)`
  factor is not identified with a physical gauge field. No new axiom, primitive,
  measure, or weight; `r` untouched.
- **Method delivered:** the `expm_multiply` pattern makes 32k-dimensional exact
  outcome-tree scans run in seconds within a ~2.5 GB envelope — recorded for future
  blocks (with the panel-serialization caveat).
- Null-diagnostic scope: every displayed p95 value is the p95 of the fixed seeded
  300-draw label-permutation sample implemented by the runner. The source claim is
  the finite, code-defined diagnostic result under that protocol, not an exact
  all-permutations null-clearing theorem.

## Cross-references

- The L=4 result this extends and honestly weakens:
  [`RECORD_CONDITIONAL_LAW_PERIOD_SCALING_L3_TO_L4_BOUNDED_THEOREM_NOTE_2026-06-11.md`](RECORD_CONDITIONAL_LAW_PERIOD_SCALING_L3_TO_L4_BOUNDED_THEOREM_NOTE_2026-06-11.md).
  That packet carries the fixed-prefix object, L=3 baseline, det-sector, finite
  Born-weighted trajectory setup, and Born assembly dependency links.
- Standard math (method only): circular statistics; permutation tests; sparse fermionic
  algebra; Krylov-free `expm_multiply` action; three-point finite-size comparison.

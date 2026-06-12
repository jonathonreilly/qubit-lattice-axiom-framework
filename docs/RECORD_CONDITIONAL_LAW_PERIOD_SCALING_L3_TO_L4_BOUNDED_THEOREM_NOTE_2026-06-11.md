# Period Scaling of the Record-Conditional U(1) Law (L=3 → L=4): Seed-Robust Fixed-k Monotonicity at the Larger Period; Null-Cleared Gaps Comparable-or-Larger

**Date:** 2026-06-11
**Type:** bounded theorem (period-scaling source proposal for PR #3554's named object; panel-corrected)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_record_conditional_law_period_scaling_2026_06_11.py`
**Cache:** `logs/runner-cache/frontier_record_conditional_law_period_scaling_2026_06_11.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=14 FAIL=0` — exact
finite evolution with a deterministic seeded 300-draw permutation-null diagnostic. The
null comparison is not an exact enumeration of all label permutations. A mandatory
4-lens adversarial panel (memory-safe re-run after the
first panel OOMed — see the runner's memory-discipline block) returned `land_with_edits`;
**all edits applied** — the decisive one kills the draft's "roughly doubles" headline by
**baseline fairness** and re-anchors on the seed-robust positive.

## The question, scaled — and the panel's correction

#3554 defined the fixed-prefix-`k` conditional law and recorded a first negative datum at
the 3-ring (a stalled fixed-k profile). The draft of this note claimed the gap "roughly
doubles" at L=4 and called the stall "a small-period artifact." **The panel refuted both
by recomputing #3554's *other* L=3 event that is positive against the fixed seeded-null diagnostic**
(seed 99/depth 7: gap `+0.190`,
**monotone**): the honest L=3 baseline is a **set**, `{+0.088 (stalled), +0.190
(monotone)}` — so the stall was **event-specific, not a period property**, and the gap
comparison is overlap, not doubling. Both events are now recomputed **in-runner**.

## The findings (exact — runner `PASS=14 FAIL=0`)

**(F1) The L=3 baseline as a set** (both #3554 events that are positive against the
fixed seeded-null diagnostic, in-runner):
seed 4242/d9: gap `+0.088`, profile **stalled** (`0.557/0.557/0.598`); seed 99/d7: gap
`+0.190`, profile **monotone** (`0.347/0.502/0.695`).

**(F2) L=4 (12 modes, 4096-dim Fock; sparse machinery; three seeds, most-spread rows):**
every seed exceeds its fixed seeded 300-draw permutation-null p95 diagnostic and every
fixed-k profile is **monotone**.
The canonical runner also checks the robustness extension: **7/7 tested `K=7` seeds**
and a `K=6` **half-filling control** (3/3), killing the filling confound:

```
seed 1     d9: profile 0.750/0.780/0.821 | gap +0.193
seed 4242  d9: profile 0.609/0.638/0.690 | gap +0.217
seed 99    d8: profile 0.597/0.665/0.784 | gap +0.076
```

**(F3) The verdict, panel-corrected.** The L=4 seeded-null gaps are
**comparable-or-larger** than the L=3 set (ranges overlap — worst L=4 `+0.076` sits
below best L=3 `+0.190`; median
ratio `1.40×`, **not doubled**; magnitudes instance/seed-labeled). **The load-bearing
positive is seed-robust fixed-k monotonicity at the larger period** — every L=4 seed
tested in-runner, robust to the filling control — *consistent with, but not establishing,*
strengthening with the period (monotonicity at L=3 was event-specific). A two-point
trend in the period, labeled as such.

## What this does and does not claim

- **Not claimed:** gap growth as a period law; concentration in the large-period limit;
  any CLT premise; `L≥5` or `Z³` behavior (rings only — geometry disclosed); gap
  universality. The disclosed honest negatives stand: one L=4 gap is the smallest of
  all five events.
- **Memory discipline (owner-enforced):** the first panel run OOMed the machine (the
  draft's dense-operator build held ~10 GB/process × 4 concurrent agents). The runner
  is rewritten sparse (Fock operators as scipy.sparse; the Kraus pair as Fock-diagonal
  *vectors*; one dense `U_step`), measured at ~1.1–1.5 GB transient peak — safe for a
  single run, with panels serializing any L=4 recompute. The lesson is a standing
  policy entry.
- Conditionality inherited (#3554/#3507): the Born derived-chain cap (the audit lane
  grades; statuses volatile — self-verify at every landing); named instruments
  (`ε=0.6`); supplied `C³` carrier; named hopping (`τ=0.35`); guarded full-rank domain;
  discrete-time throughout (retained R1 boundaries untouched). The `U(1)` factor is not
  identified with a physical gauge field. No new axiom, primitive, measure, or weight;
  `r` untouched.
- Null-diagnostic scope: every displayed p95 value is the p95 of the fixed seeded
  300-draw label-permutation sample implemented by the runner. The source claim is
  the finite, code-defined diagnostic result under that protocol, not an exact
  all-permutations null-clearing theorem.
- **The path this opens:** the period series beyond L=4 (sparse methods make L=5
  borderline-feasible), the `Z³` geometry question, and whether the seed-robust-at-L=4
  monotonicity persists or saturates — open, named, not claimed.

## Cross-references

- The named object and the L=3 events: PR #3554 (science lands via the source-only
  review loop). The decomposition: PR #3532 — science landed on origin/main via
  cherry-pick; PR closed-not-merged. The split: PR #3522 — same status. The residuals:
  PR #3507 — same status.
- Standard math (method only): circular statistics; permutation tests;
  quantum-trajectory trees; two-point finite-size comparisons; sparse fermionic
  operator algebra.

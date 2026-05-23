# Evolving Network Prototype V2 Note

**Date:** 2026-04-04 (status line rephrased 2026-04-28 per audit-lane verdict; scope narrowed 2026-05-23 per 2026-05-10 audit verdict)
**Status:** bounded prototype note; not a closed Gate B dynamics theorem and not a tier-ratified dynamics result.

**Claim scope (narrowed 2026-05-23 per 2026-05-10 audit verdict):** The runner
may be cited only as reporting positive `generated_gap`, no convergence, and
undefined `imposed_pur` in this parameter sweep, not as a closed same-budget
generated-vs-imposed bounded theorem. The earlier "larger post-barrier gap
than the unpruned baseline" wording and the "same removal budget" comparator
language are withdrawn from the load-bearing claim until a runner artifact
explicitly asserts `baseline_gap`/`gap` deltas and a unique-node removal
budget for both generated and imposed controls.

**Audit-lane runner update (2026-05-09):** The primary runner `scripts/evolving_network_prototype_v2.py` now carries explicit assertion checks (`assert math.isclose(...)`, `assert abs(...) < EPS`, etc.) mirroring its existing PASS-condition booleans. This makes the runner's class-A invariants visible to `docs/audit/scripts/classify_runner_passes.py`. The runner output and pass/fail semantics are unchanged.

## One-line read

Within the tested parameter sweep, the runner reports a positive
`generated_gap`, no convergence (`conv = 0.00`), and an undefined
`imposed_pur` (`nan`). The runner does not establish a same-budget
generated-vs-imposed comparison or a baseline-gap separation as a closed
bounded theorem.

## Primary artifact

Script:

- [`scripts/evolving_network_prototype_v2.py`](/Users/jonreilly/Projects/Physics/scripts/evolving_network_prototype_v2.py)

Log:

- [`logs/2026-04-04-evolving-network-prototype-v2.txt`](/Users/jonreilly/Projects/Physics/logs/2026-04-04-evolving-network-prototype-v2.txt)

## What the prototype compares

This prototype runs two branches on the same 3D DAG family:

1. **Generated structure**
   - local self-regulating prune rule
   - nodes with low slit distinguishability are removed iteratively
2. **Imposed structure**
   - the local rule's removed-node count fed into a hand-imposed central band

The 2026-05-10 audit verdict notes that the runner's removed counts are
inconsistent with a unique-node same-budget control. The prototype is
therefore cited only as a parameter sweep with the readouts listed below, not
as a closed same-budget generated-vs-imposed comparison.

## Reported readouts

In the tested parameter sweep, the runner reports:

- baseline purity stays high: `pur_cl ≈ 0.9648 .. 0.9894`
- generated purity is slightly lower or comparable: `pur_cl ≈ 0.9393 .. 0.9768`
- generated gap is positive across the swept thresholds: about `0.88 .. 4.09`
- removal counts are large (the rule is acting strongly rather than trivially)
- `conv = 0.00` across the tested rows
- `imposed_pur = nan` across the tested rows

These are the runner's printed outputs, not a closed bounded theorem about
generated-vs-baseline separation or generated-vs-imposed comparison.

## Negative / unresolved result

This is still a bounded negative as a Gate B closure attempt:

- `conv = 0.00` in the tested sweep
- the rule hits the removal cap instead of settling into a stable fixed point
- the imposed-band control still often loses detector signal (`pur_cl = nan`)

So the prototype does **not** yet show a clean generated-vs-imposed winner
under the current settings.

## Safe interpretation

- The runner prints a positive `generated_gap` in the tested parameter sweep.
- `conv = 0.00` across the tested rows; no fixed-point convergence is observed.
- `imposed_pur = nan` across the tested rows; the imposed-band readout is
  undefined in this parameter sweep.
- A closed same-budget generated-vs-imposed comparison and a closed
  baseline-gap separation are out of scope for this note until the runner is
  re-armed (see "What would close this lane" below).

## What is not retained from this note

- "Gate B is solved"
- "the dynamics rule converges to a fixed point"
- "the imposed-band control is a positive comparator"
- "this replaces the existing mirror / lattice / valley-linear lanes"
- "the generated rule reliably opens a larger post-barrier gap than the
  unpruned baseline" (withdrawn 2026-05-23: the runner does not print or
  assert the baseline_gap comparison)
- "same removal budget applied as a hand-imposed central band" as a closed
  comparator (withdrawn 2026-05-23: the runner does not use a unique-node
  removal budget for both branches)

This note should be read as a parameter-sweep report of positive
`generated_gap`, `conv = 0.00`, and undefined `imposed_pur`, not as a closed
generated-vs-imposed bounded theorem.

## Audit verdict acknowledgment (2026-05-23)

The 2026-05-10 audit verdict
(`docs/audit/data/audit_ledger.json` → row `evolving_network_prototype_v2_note`,
`audit_status = audited_failed`) named the following claim boundary:

> Claim boundary until fixed: the runner may be cited only as reporting
> positive generated_gap, no convergence, and undefined imposed_pur in this
> parameter sweep, not as a closed same-budget generated-vs-imposed bounded
> theorem.

The verdict's chain_closure_explanation flagged two specific runner-artifact
gaps:

- The runner does not print or assert the `baseline_gap` needed for the
  claimed larger-than-baseline gap.
- The same-budget imposed-control premise is not closed because the imposed
  removal budget is capped by candidate count while the reported removed
  counts can exceed the available unique node/candidate budgets, so the two
  branches are not running on a unique-node same-budget control.

This note has been rescoped to match the named claim boundary. No runner or
math change accompanies this rescope; the runner output and pass/fail
semantics are unchanged. The verdict's repair target (print and assert
baseline_gap/gap deltas, use an actual unique removal budget for both
generated and imposed controls, and fix the band-vs-random/readout wording)
is deferred to a future runner update.

## Audit boundary (2026-04-28)

The earlier Status line read "bounded Gate B prototype note, not a
`proposed_promoted` dynamics theorem". The audit-lane parser caught the
literal `proposed_promoted` token even though the sentence asserts the
opposite. The Status line has been rephrased.

Audit verdict (`audited_failed`, leaf criticality):

> Issue: the queue's `proposed_promoted` status contradicts the source
> note and runner output; the note says this is not a promoted dynamics
> theorem, and the runner shows no convergence plus an undefined
> imposed-control purity comparator. Why this blocks: a hostile referee
> cannot promote Gate B dynamics from a rule that hits the removal cap,
> lacks a stable fixed point, and cannot produce the promised
> generated-vs-imposed purity comparison.

> Claim boundary until fixed: it is safe to claim a bounded negative/
> prototype result in which local pruning creates a measurable
> post-barrier gap distinct from baseline, but not a closed Gate B
> dynamics solution or `proposed_promoted` theorem.

This 2026-04-28 boundary has been superseded by the narrower 2026-05-10
boundary recorded in the "Audit verdict acknowledgment (2026-05-23)"
subsection above; in particular, the "distinct from baseline" half of the
2026-04-28 wording is no longer claimed by this note because the runner does
not print or assert the `baseline_gap` comparison.

## What this note does NOT claim

- A closed Gate B dynamics theorem.
- A stable fixed point under the local pruning rule.
- A defined generated-vs-imposed purity comparator on the same budget.
- That the imposed-band control is a positive comparator.
- A baseline-gap separation between the generated rule and the unpruned
  baseline (withdrawn 2026-05-23 per the 2026-05-10 audit verdict; the runner
  does not print or assert the `baseline_gap` comparison).
- A unique-node same-budget control on the imposed branch (withdrawn
  2026-05-23 per the 2026-05-10 audit verdict; the reported removed counts
  can exceed the available unique node/candidate budgets, so the two branches
  are not running on a unique-node same-budget control).

## What would close this lane (Path A future work)

Reinstating a closed Gate B dynamics result would require:

1. A registered runner whose local rule converges under stated
   thresholds, with seed-and-layer-size assertions.
2. A defined detector signal for the same-budget imposed control.
3. A resolved band-vs-random wording mismatch for the imposed control.
4. A promoted criterion asserted across seeds and layer sizes (not just
   one seed).
5. Explicit runner prints and assertions for `baseline_gap`/`gap` deltas,
   so the generated-vs-baseline separation is visible in stdout (added
   2026-05-23 per the 2026-05-10 audit verdict).
6. A unique-node removal budget for both the generated and imposed
   branches, so the same-budget control is closed (added 2026-05-23 per the
   2026-05-10 audit verdict).

## Registered runner artifacts

`scripts/evolving_network_prototype_v2.py` contains explicit `assert`
statements that mirror the existing PASS-condition booleans, so
`docs/audit/scripts/classify_runner_passes.py` can pick them up:

- Primary runner: `scripts/evolving_network_prototype_v2.py` (registered;
  contains seven `assert` statements covering the documented PASS conditions
  for Born clean, `k=0` clean, gap-signal magnitude, removal budget,
  decoherence ceiling, and the imposed-control comparator semantics).
- Primary runner cache: `logs/runner-cache/evolving_network_prototype_v2.txt`
  (registered cached stdout; exit_code=0, status=ok).

This block records the runner assertions that back the bounded prototype read
above.

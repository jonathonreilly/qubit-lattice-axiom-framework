# Handoff

The campaign is active on
`physics-loop/gauge-transfer-positive-repair-block01-20260716`.

The exact current audit repair target is quoted in `GOAL.md` and
`TRACE_GATE.md`. The target note and runner now implement the direct `SU(3)`
representation-ring sign proof, finite-volume gauge projector, exact
temporal-link kernel, `M Q M` Gram factorization, transfer trace, spatial
insertion, repeated source, and source-algebra isometry. The refreshed runner
passes `THEOREM PASS=6 SUPPORT=10 FAIL=0`.

All three review-loop lanes passed after the requested narrow fixes. A
disposable audit-pipeline run completed with zero strict-lint errors and placed
the changed target in the generated unaudited queue at rank `34`; every
generated audit/ledger/queue/effective-status output was then restored or
deleted. The branch is rebased onto `abd65e73c5...`.

Block 01 is open for review as
[PR 5398](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/5398).
It is not merged and must not be represented as audit-ratified.

Current next action if the campaign continues:

1. leave PR 5398 for the supervising science-fix/review process;
2. create
   `physics-loop/gauge-transfer-positive-repair-block02-20260716`
   from current `origin/main`;
3. acquire a new block-local supervisor lock;
4. ground opportunity 2 from `OPPORTUNITY_QUEUE.md`, recovering its exact
   current audit blocker before editing.

No 120-minute deep block has been claimed: this first residual closed and
passed review before that interval elapsed. If this turn ends after opening the
PR, the next related block should carry the campaign's deep-block obligation.

If this worker must be resumed immediately, run:

```bash
cd /private/tmp/physics-loop-gauge-transfer-positive-repair-20260716
codex "/physics-loop --mode resume --loop gauge-transfer-positive-repair-20260716 --runtime 5h33m --target best-honest-status"
```

Then read `STATE.yaml` and this file before any broad search. Do not run
`audit-loop`, an audit worker, `codex_audit_runner.py`, or `apply_audit.py`.

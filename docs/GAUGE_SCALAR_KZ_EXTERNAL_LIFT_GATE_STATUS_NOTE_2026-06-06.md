# Gauge-Scalar K-Z External Lift Gate Status

**Date:** 2026-06-06
**Claim type:** meta
**Status:** open gate; CVXPY execution blocker partially retired in this
environment.
**Lane:** gauge-scalar temporal bridge / K-Z external lift.
**Runner:** `scripts/frontier_gauge_scalar_kz_external_lift_gate_status_2026_06_06.py`
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

This note records the current state of the PR #484 K-Z / SU(3) external-lift
gate without reviving the rejected theorem or parent-promotion language.

## Source Inputs

- [`docs/repo/ACTIVE_REVIEW_QUEUE.md`](repo/ACTIVE_REVIEW_QUEUE.md) entry
  `2026-05-03-pr484-kz-external-lift-gate`.
- [`PR484_KZ_EXTERNAL_LIFT_REVIEW_2026-05-03.md`](work_history/repo/review_feedback/PR484_KZ_EXTERNAL_LIFT_REVIEW_2026-05-03.md)
  for the detailed review findings and future success criteria.
- Optional solver availability in the current Python environment, checked by
  the paired runner.

## Gate Split

The active review queue names two load-bearing blockers:

1. the rejected PR runner failed without optional CVXPY;
2. the load-bearing `W_lift = 0.05` was not extracted from an explicit
   `SU(3), beta=6` primary-source bracket.

This branch partially moves blocker (1): CVXPY is available in the current
environment, with CLARABEL/SCS-class solvers installed, and the paired runner
solves a small K-Z-style moment/PSD feasibility probe. That means future work
can run an SDP-side reproduction path here without first resolving package
availability.

Blocker (2) remains open. The old `W_lift = 0.05` width remains a candidate
or conservative placeholder until one of the following exists:

- an explicit `SU(3), beta=6` primary-source bracket from the cited external
  lattice-bootstrap literature, or
- a repo-owned SDP reproduction deriving a bracket at a stated cutoff, solver,
  tolerance, and trace/loop truncation.

## Current Status

The route remains open.

The branch does not land the old theorem note, does not use the K-Z
`SU(infinity)` benchmark as a target-regime bracket, and does not promote the
gauge-scalar temporal parent chain. It only certifies that the optional solver
availability issue is no longer the first local blocker and that the primary
external-bracket provenance remains the decisive open input.

## Runner Scope

The paired runner checks:

- active queue and review-packet wording for the two blockers;
- CVXPY import and installed solvers;
- a small PSD/Hausdorff moment feasibility problem with a conservative
  `W_lift = 0.05` interval;
- the no-go witness scale `epsilon_witness` from a direct SU(3) Cartan-torus
  single-plaquette calculation;
- branch-local wording hygiene.

The SDP probe is a tooling/provenance certificate, not a replacement for the
missing primary-source `SU(3), beta=6` bracket.

## Boundaries

- No observed plaquette value or Monte Carlo table is used as proof input.
- No fitted `beta_eff` is introduced.
- No same-surface family argument is used.
- No old PR484 retained/effective-status language is revived.
- No repo-wide authority surface is updated.

## Verification

Run:

```bash
python3 scripts/frontier_gauge_scalar_kz_external_lift_gate_status_2026_06_06.py
```

Expected summary:

```text
TOTAL: PASS=43, FAIL=0
```

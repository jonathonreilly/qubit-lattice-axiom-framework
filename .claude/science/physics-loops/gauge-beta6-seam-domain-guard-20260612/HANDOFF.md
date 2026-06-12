# Handoff

## What changed

The seam-reduction source note now states that normalized `rho` is only
defined on `z_(0,0) != 0`; if the denominator vanishes, only unnormalized `z`
and `Z(W)` statements remain. The note also separates the evaluation
functional `ell_W` from its Riesz representative `k(W)`.

## Why

Latest audit row:

`gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17`

Blocker:

`scope_too_broad: add an explicit z_(0,0) != 0 hypothesis, or restrict the rho statements to cases where the denominator is defined; also type K(W) consistently as a vector/Riesz representative if the inner-product notation is retained.`

## Verification

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_beta6_seam_domain_guard_2026_06_12.py
python3 scripts/frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_gauge_vacuum_plaquette_beta6_seam_domain_guard_2026_06_12.py --check-only --push-mode=none
git diff --check origin/main...HEAD
git diff --name-only origin/main...HEAD -- docs/audit docs/repo/FRONT_DOOR_STATUS.md
```

## Remaining blockers

The four Wilson/Haar physical-identification authorities remain open. This PR
only closes the newly named source-domain and notation issue.

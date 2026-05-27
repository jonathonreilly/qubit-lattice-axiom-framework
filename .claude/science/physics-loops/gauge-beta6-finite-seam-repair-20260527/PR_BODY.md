## Summary

This PR repairs the audited-conditional beta=6 plaquette evaluation-seam row by
narrowing it to finite witness/evaluator-route bounded support.

The row no longer claims the full `K_6^env` / `B_6(W)` Wilson/Haar integral
objects are already available. It now certifies only the finite left evaluator,
the exact radical rank-three first symmetric restriction, and the finite
structural-surface underdetermination of the beta-side vector.

## Target Row

- `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17`

## Verification

- `python3 scripts/frontier_gauge_vacuum_plaquette_beta6_finite_seam_route_repair.py`
  - `SUMMARY: THEOREM PASS=5 SUPPORT=5 FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/GAUGE_VACUUM_PLAQUETTE_BETA6_EVALUATION_SEAM_REDUCTION_SCIENCE_ONLY_NOTE_2026-04-17.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete
- `git diff --check`
  - clean

## Pipeline Result

- Target row reset to `unaudited`, `claim_type=bounded_theorem`.
- Runner path set to `scripts/frontier_gauge_vacuum_plaquette_beta6_finite_seam_route_repair.py`.
- Upstream underdetermination row remains `audited_clean` / `retained_no_go`.

## Boundaries

- No new axioms.
- No retained retag.
- No physical beta=6 plaquette PF closure.
- Full Wilson/Haar environment transfer remains open.

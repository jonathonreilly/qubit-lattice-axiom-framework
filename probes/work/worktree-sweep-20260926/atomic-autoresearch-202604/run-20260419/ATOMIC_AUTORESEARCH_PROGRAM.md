# Atomic Autoresearch Program

This is a Karpathy-style autoresearch loop adapted to the atomic lane.

## Goal
- Improve the retained atomic-lane leader autonomously.
- One loop = one bounded research step.
- Prefer real retained improvements over raw metric drops.

## Current Leader
- Read `outputs/atomic_lane/autoresearch_current_readout.json`.
- Treat `accuracy_metrics.scores.full_rms_relative_error` as the primary metric.
- Lower is better.

## Acceptance Gate
A candidate only counts as a kept improvement if all of the following hold:
- it beats the current leader on `full_rms_relative_error`
- it survives `scripts/atomic_correlated_basis_robustness.py` on at least two CI slices
- it remains accepted on the full lane gate
- it does not regress into a packaging/docs-only change

## Scope
Science only. No docs, packaging, or reviewer-facing cleanup.

Prefer work in this order:
1. local shell-radial one-body refinement
2. shell-coupled screen of those refined candidates
3. tight shell/contact retune only if a screened near-miss fails only on ionization or gap
4. basis validation of the best accepted candidate

## Allowed Files
- `scripts/atomic_two_body_runtime.py`
- `scripts/atomic_one_body_runtime.py`
- `scripts/atomic_correlated_runtime.py`
- `scripts/atomic_shell_radial_local_refine.py`
- `scripts/atomic_shell_one_body_screen.py`
- `scripts/atomic_shell_one_body_retune.py`
- `scripts/atomic_correlated_basis_robustness.py`
- `scripts/atomic_correlated_readout.py`
- `scripts/atomic_bound_shell_diagnostics.py`
- `scripts/atomic_best_known_lane_scoreboard.py`
- `scripts/atomic_next_phase_assessment.py`

Do not widen scope beyond that unless the current loop is blocked.

## Stable Paths
Use these as the canonical autoresearch aliases:
- current readout: `outputs/atomic_lane/autoresearch_current_readout.json`
- current selected candidate: `outputs/atomic_lane/autoresearch_current_candidate.json`
- current scoreboard: `outputs/atomic_lane/atomic_best_known_lane_scoreboard.json`
- current assessment: `outputs/atomic_lane/atomic_next_phase_assessment.json`
- results table: `outputs/atomic_lane/autoresearch/results.tsv`

## Workspace Rule
- Operate only inside the current working tree.
- Use relative paths unless an absolute path is required by a tool.
- Do not inspect or modify the source repo that seeded this run.
- If you see absolute paths pointing at another checkout, ignore them and stay in the current run repo.
- Do not inspect `AUTOPILOT*` files, broad docs, broad script lists, old non-atomic lanes, or repo-wide search output.
- Start from the stable atomic alias JSON files and the listed atomic scripts only.

## Per-Loop Procedure
1. Read this file plus:
   - `outputs/atomic_lane/autoresearch_current_readout.json`
   - `outputs/atomic_lane/autoresearch_current_candidate.json`
   - `outputs/atomic_lane/atomic_best_known_lane_scoreboard.json`
   - `outputs/atomic_lane/atomic_next_phase_assessment.json`
2. Make exactly one bounded research attempt.
3. Run the minimum commands needed to evaluate it.
4. If the candidate does not beat the current leader honestly, discard your changes and leave the repo at `HEAD`.
5. If it does beat the current leader and passes the robustness gate:
   - overwrite `outputs/atomic_lane/autoresearch_current_readout.json` with the new canonical readout
   - overwrite `outputs/atomic_lane/autoresearch_current_candidate.json` with the selected accepted candidate payload
   - refresh diagnostics, scoreboard, and assessment
   - create one git commit with the loop number and new full RMS
6. Stop after one loop. Do not start a second loop inside the same `codex exec` run.

## Results TSV
Keep the header as:

`loop	timestamp	status	full_rms	one_body_rms	max_relative_error	source_json	commit`

The Python driver owns row logging in `results.tsv`. Do not edit that file from inside a loop.

Status must be one of:
- `kept`
- `rejected`
- `error`

## Notes
- Prefer clean keep/discard logic over bigger searches.
- If a retuned candidate looks better at source basis but fails robustness, reject it.
- If no real improvement is found, append a `rejected` row and stop.

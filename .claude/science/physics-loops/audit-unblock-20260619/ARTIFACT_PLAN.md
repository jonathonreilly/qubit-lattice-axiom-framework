# Artifact Plan

## Source Artifacts

- `docs/KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`
  - add `Type: bounded_theorem`
  - add `Claim type: bounded_theorem`
  - replace positive/proposed-retained framing with bounded bridge-corollary
    support
  - refresh runner transcript from 9 checks to 21 checks
- `scripts/frontier_koide_kappa_spectrum_operator_bridge_theorem.py`
  - add bridge-note source-boundary checks
  - require bounded metadata, boundary prose, overclaim removal, and current
    transcript before the runner can pass

## Generated Artifacts

- Run `bash docs/audit/scripts/run_pipeline.sh`.
- Refresh `logs/runner-cache/frontier_koide_kappa_spectrum_operator_bridge_theorem.txt`.
- Refresh audit packet helper dependency data.
- Commit regenerated audit and publication effective-status surfaces.

## Review Artifacts

- Branch-local `STATE.yaml`, `TRACE_GATE.md`,
  `CLAIM_STATUS_CERTIFICATE.md`, `REVIEW_HISTORY.md`, `HANDOFF.md`, and
  `PR_BODY.md`.

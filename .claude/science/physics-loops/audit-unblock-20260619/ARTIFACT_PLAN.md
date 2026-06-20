# Artifact Plan

## Source Artifacts

- `docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`
  - add `Type: open_gate`
  - add `Claim type: open_gate`
  - state independent audit-lane status authority
  - name the unresolved readout-map theorem step
- `scripts/frontier_quark_route2_exact_readout_map.py`
  - add source-boundary checks for the open-gate metadata and unresolved step
  - update expected pass count through direct runner output

## Generated Artifacts

- Run `bash docs/audit/scripts/run_pipeline.sh`.
- Refresh `logs/runner-cache/frontier_quark_route2_exact_readout_map.txt`.
- Refresh audit packet helper dependency data.
- Commit regenerated audit and publication effective-status surfaces.

## Review Artifacts

- Branch-local `STATE.yaml`, `TRACE_GATE.md`,
  `CLAIM_STATUS_CERTIFICATE.md`, `REVIEW_HISTORY.md`, `HANDOFF.md`, and
  `PR_BODY.md`.

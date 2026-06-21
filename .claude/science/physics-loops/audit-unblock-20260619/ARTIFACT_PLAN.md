# Artifact Plan

## Source Artifacts

- `docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md`
  - Clarifies that generated queue snapshots are not source-claim citations
    for the citation firewall.
- `scripts/frontier_koide_q_delta_formal_ratio_repair.py`
  - Skips `docs/repo/FRONT_DOOR_STATUS.md` in `is_source_scan_path()`.

## Verification Artifacts

- `logs/runner-cache/frontier_koide_q_delta_formal_ratio_repair.txt`

## Excluded Generated Artifacts

After the current-main rebase, generated audit ledger/queue/data,
publication effective-status views, packet-dependency outputs, and
`docs/repo/FRONT_DOOR_STATUS.md` are excluded from this PR.

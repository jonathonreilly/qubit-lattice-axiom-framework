## Summary

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2076

Repairs the stale runner artifact for
`dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`.

The target runner failed because the current narrowed projector-interface helper
no longer exports `canonical_h`. This PR makes the primary runner
self-contained for the bounded interval witness and records that repair in the
source note.

## Audit Surface

- Target row: `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`
- Runner: `scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py`
- After pipeline: `audit_status=unaudited`, `effective_status=unaudited`,
  `ready=true`
- No physical selector law, off-seed source derivation, helper-row promotion,
  or full-stack closure.

## Verification

```text
python3 scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
python3 scripts/vocab_lint.py --report-only docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

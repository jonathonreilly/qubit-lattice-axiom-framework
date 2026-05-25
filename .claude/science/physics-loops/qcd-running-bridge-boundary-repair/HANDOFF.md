# Handoff

## Summary

This block repairs `qcd_low_energy_running_bridge_note_2026-05-01` by
narrowing it to the standard QCD/SM running kernel at an admitted
`alpha_s(v)` boundary.

The repaired row no longer claims that this source derives the boundary
value from the plaquette chain. That upstream derivation remains in the
plaquette / alpha_s rows.

## Pipeline Result

After `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_id: qcd_low_energy_running_bridge_note_2026-05-01
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
deps: []
ready: true
audit_queue_rank: 2
transitive_descendants: 708
```

## Verification

Completed:

```bash
python3 -m py_compile scripts/frontier_qcd_low_energy_running_bridge.py
python3 scripts/frontier_qcd_low_energy_running_bridge.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md scripts/frontier_qcd_low_energy_running_bridge.py .claude/science/physics-loops/qcd-running-bridge-boundary-repair
```

Runner result:

```text
SUMMARY: PASS=18  FAIL=0
```

Strict audit lint returned OK with one pre-existing warning and legacy notices
not introduced by this branch.

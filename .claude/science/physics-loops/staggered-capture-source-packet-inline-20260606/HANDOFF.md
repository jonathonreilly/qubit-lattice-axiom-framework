# Handoff

Branch-local result:

- The primary staggered live capture packet runner now checks that the note
  links the capture harness, iterative source-map, cycle battery, layered
  holdout, prototype helper, source-packet manifest cache, and manifest JSON.
- It verifies load-bearing source markers across the helper chain.
- It verifies helper caches are SHA-fresh and clean-exit.
- It verifies the manifest cache/JSON report zero failures.

Verification:

```bash
python3 -m py_compile scripts/staggered_backreaction_live_capture_packet_check.py scripts/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/staggered_backreaction_live_capture_packet_check.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.py
git diff --check
```

Remaining blocker:

Independent audit must decide whether this repaired restricted packet is
sufficient. This PR does not retag the ledger.

Next campaign action:

Attempt the analogous primary-runner source-packet inline repair for
`wave_direct_dm_h025_fam2_seed1_followup_note`.

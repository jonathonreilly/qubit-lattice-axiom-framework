# Handoff

## What Changed

The archived stale-frame notes now carry explicit archive-firewall language.
Their theorem/closure/decision headings are historical/retracted, and their
boundary paragraphs no longer present active Axiom*/minimal-carrier support or
global exhaustion proof.

## What This Does Not Do

- It does not audit the rows.
- It does not adopt or reject Axiom*.
- It does not rebuild the carrier-axiom analysis.
- It does not propose retained status.

## Verification

```bash
python3 scripts/stale_frames_archive_firewall_2026_06_16.py
python3 -m py_compile scripts/stale_frames_archive_firewall_2026_06_16.py
git diff --check
python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only
python3 scripts/vocab_lint.py --report-only --report-path /tmp/stale-frames-vocab-report.json archive_unlanded/stale-frames-2026-04-30/CL4C_CARRIER_AXIOM_CONSEQUENCE_MAP_NOTE_2026-04-28.md archive_unlanded/stale-frames-2026-04-30/HUBBLE_LANE5_C1_A5_MINIMAL_CARRIER_AXIOM_AUDIT_NOTE_2026-04-28.md archive_unlanded/stale-frames-2026-04-30/HUBBLE_LANE5_C1_STUCK_FANOUT_SYNTHESIS_NOTE_2026-04-28.md
```

PR: TBD

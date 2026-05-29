## Summary

This PR adds a new bounded-support positive packet for the live staggered capture-closure backreaction runner.

It does not rewrite or retag the archived failed `staggered_backreaction_capture_closure_note`. The old stale force/gap/gain table and exact force-closure claim remain rejected; this packet asserts only the current live surface.

## Science Boundary

Live finite result:

- both cycle-bearing batteries score `9/9`;
- cycle mean gap improves from `9.828e-01` to `4.734e-01` (`2.08x`);
- layered holdout gap improves from `9.191e-01` to `4.559e-01` (`2.02x`);
- zero-source, linearity, additivity, TOWARD, gauge, and norm checks survive.

No exact force-scale closure, continuum backreaction theorem, physical gravitational closure, or effective retained status is claimed before audit.

## Audit Queue

`bash docs/audit/scripts/run_pipeline.sh`:

- newly seeded: 1
- new row: `staggered_backreaction_live_capture_packet_note_2026-05-29`
- queue rank: 912
- ready: true
- open dependencies: none

## Verification

```text
python3 -m py_compile scripts/staggered_backreaction_live_capture_packet_check.py
python3 scripts/staggered_backreaction_live_capture_packet_check.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

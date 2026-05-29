## Summary

This PR adds a new bounded-support positive packet for the live staggered graph-Green backreaction runner.

It does not rewrite or retag the archived failed `staggered_backreaction_green_closure_note`. The old near-order-of-magnitude closure and clean calibrated-holdout claims remain rejected; this packet asserts only the current live surface.

## Science Boundary

Live finite result:

- `resistance_yukawa` is the best holdout-aware map in the frozen comparison.
- Raw cycle-bearing gap improves by `2.81x` over screened Poisson.
- Raw holdout gap is `1.534e-02`.
- Source-linearity, two-body, TOWARD, and norm checks remain tight.
- Calibrated holdout gap and self-refresh remain open seams.

No continuum backreaction theorem, physical gravitational closure, or effective retained status is claimed before audit.

## Audit Queue

`bash docs/audit/scripts/run_pipeline.sh`:

- newly seeded: 1
- new row: `staggered_backreaction_live_green_packet_note_2026-05-29`
- queue rank: 912
- ready: true
- open dependencies: none

## Verification

```text
python3 -m py_compile scripts/staggered_backreaction_live_green_packet_check.py
python3 scripts/staggered_backreaction_live_green_packet_check.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

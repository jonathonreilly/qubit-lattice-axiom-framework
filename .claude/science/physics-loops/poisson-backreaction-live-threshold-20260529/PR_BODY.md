## Summary

This PR adds a new bounded-support positive packet for the live Poisson self-gravity/backreaction runner.

It does not rewrite or retag the archived failed `backreaction_note`. The archived `G_crit ~= 0.011` threshold remains rejected; this packet asserts only the finite live surface.

## Science Boundary

Live finite result:

- TOWARD deflection is preserved for all tested `G` values through `G=0.100`.
- Escape remains above one at `G=0.011`, `G=0.012`, and `G=0.020`.
- The first sub-unit escape point in the declared grid is `G=0.050`.

No continuum horizon, smooth threshold law, physical Schrodinger-Newton closure, or effective retained status is claimed before audit.

## Audit Queue

`bash docs/audit/scripts/run_pipeline.sh`:

- newly seeded: 1
- new row: `poisson_backreaction_live_threshold_packet_note_2026-05-29`
- queue rank: 907
- ready: true
- open dependencies: none

## Verification

```text
python3 -m py_compile scripts/backreaction_poisson_live_threshold_check.py
python3 scripts/backreaction_poisson_live_threshold_check.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

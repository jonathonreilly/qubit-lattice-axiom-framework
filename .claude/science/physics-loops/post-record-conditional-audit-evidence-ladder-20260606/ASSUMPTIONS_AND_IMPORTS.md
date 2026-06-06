# Assumptions And Imports

## Used

- The stacked concentration-certificate interface in PR #2833.
- Landed Record history/count and audit-unlock maps on `main`.
- A finite evidence classifier implemented directly in the runner.

## Not imported

- No audit data edits.
- No audit verdicts.
- No probability law from Record.
- No concentration theorem from expectation.
- No calibration from simulation alone.
- No dial selection from stability alone.
- No production dynamics without a supplied formation/kernel/time bridge.

## Stacking reason

This block depends on the concentration-certificate interface. Its PR should be
stacked on `physics-loop/post-record-supplied-concentration-certificate-interface-20260606`
rather than opened independently against `main`.

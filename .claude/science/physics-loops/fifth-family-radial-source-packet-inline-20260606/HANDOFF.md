# Handoff

Branch-local result:

- The primary fifth-family radial basin runner now checks that the note links
  the primary runner/cache, F~M transfer runner/cache, sweep runner/cache,
  failure-audit runner/cache, restored radial helper, and no-restore growth
  helper.
- It verifies companion source markers for the F~M two-strength exponent, the
  positive-row sweep, and the sign-orientation boundary.
- It verifies F~M, sweep, and failure-audit caches are SHA-fresh and clean-exit.
- It verifies the F~M cache reports `passed rows: 2/2` and
  `mean F~M among passes: 0.999439`.

Verification:

```bash
python3 -m py_compile scripts/FIFTH_FAMILY_RADIAL_BASIN.py scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py scripts/FIFTH_FAMILY_RADIAL_SWEEP.py scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/FIFTH_FAMILY_RADIAL_BASIN.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/FIFTH_FAMILY_RADIAL_SWEEP.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py
git diff --check
```

Remaining blocker:

Independent audit must decide whether this repaired restricted packet is
sufficient. This PR does not retag the ledger.

Next campaign action:

After this PR, the remaining conditionals are predominantly hard bridge
problems rather than artifact packet repairs.

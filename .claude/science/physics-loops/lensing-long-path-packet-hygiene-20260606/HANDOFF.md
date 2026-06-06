# Handoff

Branch-local science block:

- Target: parent `LENSING_FINITE_PATH_EXPLANATION_NOTE.md` conditional blocker.
- Repair: make `LENSING_LONG_PATH_TEST_NOTE.md` a complete source packet for the
  long-path runner/cache evidence.
- Remaining science: wave-mechanical derivation of the observed slope remains
  open.

Verification:

```bash
python3 scripts/cached_runner_output.py scripts/lensing_long_path_test.py --refresh --timeout-sec 420
python3 scripts/cached_runner_output.py scripts/lensing_long_path_test.py --check-only
git diff -- docs/audit --exit-code
git diff --check
```

Expected runner result: `status: ok`, `exit_code: 0`.

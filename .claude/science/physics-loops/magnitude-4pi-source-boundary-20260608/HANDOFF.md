# Handoff

This PR was originally developed stacked on `physics-loop/magnitude-temporal-source-packet-20260608`, but #3260 landed before PR creation. The branch is now rebased on current `main`.

What changed:

- Narrowed the 4π row to a bounded source-boundary claim.
- Removed observed `M_Pl/v` style PASS logic.
- Verified the retained/stacked/open source packet in the runner.
- Left I1/I2/I3/P3 open and explicitly named.

Verification:

```bash
python3 scripts/magnitude_4pi_is_native_coupling_not_gaussian_2026_06_06.py
```

Expected result:

```text
TOTAL: PASS=62 FAIL=0
```

Do not treat this as closure of the hierarchy value gate.

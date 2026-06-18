# Handoff

Target:
`gate_b_operator_cauchy_note_2026-05-10`

What changed:

- The note is now a bounded tested-axis negative boundary, not a family-level
  no-go.
- The runner prints a scope certificate:
  `family_exhaustion_claim=False; tested_cauchy_axes=2;
  strong_field_method_mismatch=True`.
- The SHA-pinned cache was regenerated with the standard cache helper.

Verification:

```bash
python3 -m py_compile scripts/gate_b_operator_cauchy.py
python3 scripts/cached_runner_output.py --check-only scripts/gate_b_operator_cauchy.py
python3 scripts/gate_b_operator_cauchy.py
```

Results:

- runner exit code: 0
- cache freshness: fresh
- expected bounded-null check: PASS

Not done:

- No audit verdicts were run or applied.
- No audit ledger, audit queue, publication status, front-door status, or lane
  registry files were edited.
- No stale existing PR was refreshed against `main`.

Next exact action:
Open the PR and ask the reviewer to extract the narrowed source repair.

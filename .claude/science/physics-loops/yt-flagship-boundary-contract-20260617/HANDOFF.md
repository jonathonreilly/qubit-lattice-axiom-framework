# Handoff

## Summary

This branch adds a primary runner for `docs/YT_FLAGSHIP_BOUNDARY_NOTE.md` so
`yt_flagship_boundary_note` no longer has to sit in the audit queue with
`runner_path=null`.

The runner checks the note's boundary contract, not YT retained closure:

- authority links and runner registration are present;
- current `y_t(v)`, pole-mass values, and residual budgets agree with the YT
  authority notes;
- standard-method residuals remain visible;
- the note explicitly forbids fully-retained UV-to-IR closure, a native
  continuum-limit theorem, and a direct-lattice low-energy bypass claim.

## Verification

```bash
python3 scripts/frontier_yt_flagship_boundary_contract.py
python3 scripts/cached_runner_output.py scripts/frontier_yt_flagship_boundary_contract.py --refresh
python3 scripts/cached_runner_output.py scripts/frontier_yt_flagship_boundary_contract.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_yt_flagship_boundary_contract.py --check-only
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/frontier_yt_flagship_boundary_contract.py scripts/cached_runner_output.py docs/audit/scripts/build_citation_graph.py
```

## Reviewer Notes

Independent review/audit still decides whether this row becomes audit-ready or
how the claim type should be interpreted. This PR does not edit audit results,
the ledger, generated publication status files, or repo-wide lane surfaces.

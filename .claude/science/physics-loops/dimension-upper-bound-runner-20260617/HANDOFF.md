# Handoff

## Summary

This branch changes the dimension-selection upper-bound wrapper metadata from
`Primary source-packet runner` to canonical `Primary runner` so
`docs/audit/scripts/build_citation_graph.py` extracts:

```text
scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py
```

The source packet already verifies the textbook-import boundary:

- native stable-circular-orbit calculation is the decisive upper edge;
- Coulomb side is only compatible Green-kernel scaling support;
- Bertrand/Goldstein/Tangherlini/Ehrenfest/Bures-Siegl references are parallel
  context, not load-bearing proof inputs;
- no audit verdict is applied.

## Verification

```bash
python3 scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py
python3 scripts/cached_runner_output.py scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py --refresh
python3 scripts/cached_runner_output.py scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py --check-only
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/dimension_selection_upper_bound_textbook_import_scope_certificate_2026_06_12.py scripts/cached_runner_output.py docs/audit/scripts/build_citation_graph.py
```

## Reviewer Notes

No audit results, ledger rows, generated publication status files, or lane
registry/front-door surfaces are edited. Independent audit remains required.

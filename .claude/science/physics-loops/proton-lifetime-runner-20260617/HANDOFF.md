# Handoff

## Summary

This branch registers the existing proton-lifetime runner for
`docs/PROTON_LIFETIME_DERIVED_NOTE.md`.

The source claim remains bounded support:

- exact Cl(3) taste-space decomposition and leptoquark-operator existence are
  runner checked;
- `M_X = M_Pl` is a package pin;
- dimension-6 EFT decay formula and `alpha_GUT = 1/25` remain imported;
- hadronic matrix elements are not computed.

## Verification

```bash
python3 scripts/frontier_proton_lifetime_derived.py
python3 scripts/cached_runner_output.py scripts/frontier_proton_lifetime_derived.py --refresh
python3 scripts/cached_runner_output.py scripts/frontier_proton_lifetime_derived.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_proton_lifetime_derived.py --check-only
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/frontier_proton_lifetime_derived.py scripts/cached_runner_output.py docs/audit/scripts/build_citation_graph.py
```

## Reviewer Notes

No audit results, ledger rows, generated publication status files, or lane
registry/front-door surfaces are edited. Independent audit remains required.

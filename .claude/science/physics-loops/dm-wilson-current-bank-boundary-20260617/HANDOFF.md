# Handoff

## Summary

This block repairs three DM Wilson current-bank blockers that were failing on
latest `origin/main`.

The generic and local current-bank runners now distinguish classified
non-closing adjacent mentions from unclassified hidden theorem-grade closure.
Known status/helper/support mentions become `[BOUNDARY]`, while any new
unclassified Wilson-to-`dW_e^H` or local path-algebra closure artifact remains a
hard failure.

The flagship frontier-collapse row is scientifically corrected: after the PMNS
projector-interface repair, the row cannot claim that support provenance is
closed. It is now bounded fixed-support diagnostic support. The useful
calculation is preserved: once `E_e` and `L_e = Schur_{E_e}(D_-)` are supplied,
ambient completion choices above the Schur block do not change the downstream
Hermitian response or transport diagnostic.

## Verification

Completed:

```bash
python3 -m py_compile scripts/frontier_dm_wilson_to_dweh_hermitian_source_family_current_bank_boundary_2026_04_18.py scripts/frontier_dm_wilson_to_dweh_local_chain_path_algebra_current_bank_boundary_2026_04_18.py scripts/frontier_dm_wilson_direct_descendant_flagship_frontier_collapse_theorem_2026_04_18.py
python3 scripts/frontier_dm_wilson_to_dweh_hermitian_source_family_current_bank_boundary_2026_04_18.py
python3 scripts/frontier_dm_wilson_to_dweh_local_chain_path_algebra_current_bank_boundary_2026_04_18.py
python3 scripts/frontier_dm_wilson_direct_descendant_flagship_frontier_collapse_theorem_2026_04_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_dm_wilson_to_dweh_hermitian_source_family_current_bank_boundary_2026_04_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_dm_wilson_to_dweh_local_chain_path_algebra_current_bank_boundary_2026_04_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_dm_wilson_direct_descendant_flagship_frontier_collapse_theorem_2026_04_18.py
git diff --check
```

Protected audit/publication/status-surface diff check is empty.

## Review note

Review-loop was not run here because the user explicitly delegated review and
landing to the Codex reviewer. This PR is ready for that reviewer to extract or
modify the science.

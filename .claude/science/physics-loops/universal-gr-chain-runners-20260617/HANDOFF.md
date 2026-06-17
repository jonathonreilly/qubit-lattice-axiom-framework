# Handoff

This PR registers seven existing Universal GR runners whose queue rows on
`origin/main` have `runner_path: null`.

No audit result, audit ledger row, publication table, active review queue,
front-door status file, canonical harness, lane registry, or lane status board
is edited. Independent audit remains required.

Verification to rerun:

```bash
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_universal_gr_lorentzian_signature_extension.py,scripts/frontier_universal_gr_isotropic_glue_operator.py,scripts/frontier_universal_gr_constraint_action_stationarity.py,scripts/frontier_universal_gr_canonical_projector_connection.py,scripts/frontier_universal_gr_curvature_localization_blocker.py,scripts/frontier_universal_gr_block_constraint_interpretation.py,scripts/frontier_universal_gr_tensor_action_blocker.py --check-only
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/frontier_universal_gr_lorentzian_signature_extension.py scripts/frontier_universal_gr_isotropic_glue_operator.py scripts/frontier_universal_gr_constraint_action_stationarity.py scripts/frontier_universal_gr_canonical_projector_connection.py scripts/frontier_universal_gr_curvature_localization_blocker.py scripts/frontier_universal_gr_block_constraint_interpretation.py scripts/frontier_universal_gr_tensor_action_blocker.py scripts/cached_runner_output.py docs/audit/scripts/build_citation_graph.py
```


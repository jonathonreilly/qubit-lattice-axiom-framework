# Handoff

This PR continues the audit-unblock campaign after PR #3825. The branch is
rebased onto `origin/main` f6ed4e650.

Rows covered:

- `koide_cl3_selector_gap_note_2026-04-19`: added executable open-gate inventory runner, `PASS=23 FAIL=0`.
- `g_bare_constraint_vs_convention_restatement_note_2026-05-07`: added shared pending-chain exact cross-check helper, `PASS=17 FAIL=0`.
- `n_f_bounded_z2_reduction_theorem_note_2026-05-07_w2`: same shared helper, `PASS=17 FAIL=0`.
- `charged_lepton_brannen_bae_delta_tier_a_bounded_theorem_note_2026-05-30`: added Tier-A pending-chain firewall, verifier now `PASS=22 FAIL=0`.
- `ckm_atlas_closure_formula_algebra_narrow_theorem_note_2026-05-10`: boxed as decoration/corollary; runner now `PASS=27 FAIL=0`.
- `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17`: boxed as decoration/corollary; runner now `PASS=46 FAIL=0`.

Verification:

```bash
python3 scripts/precompute_audit_runners.py --allow-non-main --push-mode=none --force --concurrency=5 --runners scripts/frontier_koide_cl3_selector_gap_open_gate_2026_06_13.py,scripts/frontier_g_bare_nf_pending_chain_crosscheck_2026_06_13.py,scripts/audit_companion_ckm_atlas_closure_formula_algebra_exact_2026_05_10.py,scripts/audit_companion_staggered_dirac_substep1_jw_bridge_2026_05_17.py,scripts/frontier_charged_lepton_brannen_bae_delta_tier_a_bounded_verifier.py
python3 scripts/precompute_audit_runners.py --allow-non-main --check-only --push-mode=none --runners scripts/frontier_koide_cl3_selector_gap_open_gate_2026_06_13.py,scripts/frontier_g_bare_nf_pending_chain_crosscheck_2026_06_13.py,scripts/audit_companion_ckm_atlas_closure_formula_algebra_exact_2026_05_10.py,scripts/audit_companion_staggered_dirac_substep1_jw_bridge_2026_05_17.py,scripts/frontier_charged_lepton_brannen_bae_delta_tier_a_bounded_verifier.py
```

Both commands passed. The check-only command reported all five caches fresh.

No `docs/audit/**` files or front-door status files were changed.

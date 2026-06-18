# Handoff

This block adds native SU(2) beta=16 one-plaquette support for the
`u0(SU2) in [0.96, 0.98]` interval used by the `g_2(v)` bounded interval
row.

Verification:

- `python3 scripts/su2_u0_single_plaquette_beta16_native_interval_2026_06_18.py`
  reports `TOTAL: PASS=10 FAIL=0`.
- `python3 scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py`
  reports `PASS=32 FAIL=0`.
- Runner caches refreshed for both scripts.

PR:

- https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4404
- Branch: `codex/g2v-su2-u0-native-20260618`
- Commit: `cd3feeb50dfcd942744c526546248b82295e4ed3`

Review-loop was not run because the user delegated review-loop and
landing cleanup to the Codex reviewer.

Next action: reviewer should run review-loop/landing cleanup and decide
whether this source-side bridge is audit-ready.

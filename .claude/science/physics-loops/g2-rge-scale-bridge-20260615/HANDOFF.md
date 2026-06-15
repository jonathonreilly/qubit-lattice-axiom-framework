# Handoff

This branch addresses the audited conditional blocker for
`g_2_v_bounded_interval_narrow_theorem_note_2026-05-17`.

The old row imported three pieces: X1 `u_0(SU(2))`, X6 the scale log, and X7
the one-loop inverse-alpha running form. This PR repairs only X6/X7:

- `docs/SU2_WEAK_ONE_LOOP_INVERSE_ALPHA_SCALE_LOG_BRIDGE_NARROW_THEOREM_NOTE_2026-06-15.md`
  proves the scale/RGE bridge.
- `scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py`
  verifies the bridge.
- `docs/G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md`
  now cites the bridge and preserves X1 as the remaining named import.
- `scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py`
  now requires the bridge and uses `v_cand approx 246.28 GeV` wording.

Reviewer/auditor should not treat this as a ledger retag. The branch needs
source review and independent audit. If accepted, it should partially close the
blocker by retiring X6/X7 and leave X1 for the next science lane.

Validation commands:

```bash
python3 scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py
python3 scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py
python3 -m py_compile scripts/audit_companion_su2_weak_one_loop_inverse_alpha_scale_log_bridge_2026_06_15.py scripts/audit_companion_g2_v_bounded_interval_narrow_exact_2026_05_17.py
git diff --check
```

Diagnostic pipeline result:

```text
PYTHONPATH=scripts bash docs/audit/scripts/run_pipeline.sh
cycles: 0
ready queue entries: 50
audit_lint: OK, no errors
g_2_v_bounded_interval_narrow_theorem_note_2026-05-17: unaudited after source hash change
su2_weak_one_loop_inverse_alpha_scale_log_bridge_narrow_theorem_note_2026-06-15: seeded unaudited
```

All generated audit, publication, and front-door outputs from the diagnostic
pipeline run were restored before commit.

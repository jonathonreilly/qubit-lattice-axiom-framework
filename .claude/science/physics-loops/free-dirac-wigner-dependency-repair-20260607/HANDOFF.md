# Handoff

Science block: free-Dirac Wigner-action dependency repair.

Files to review:

- `docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md`
- `scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py`
- `logs/runner-cache/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt`

What changed:

- The bridge note now includes an explicit dependency authority section for the
  companion free-Dirac Poincare representation note/runner/cache.
- The runner verifies the companion cache header, runner SHA freshness,
  `status: ok`, zero exit, and `SCORECARD PASS=8 FAIL=0`, including P5/P6
  Wigner-rotation and invariant-measure checks.
- The refreshed bridge cache reports `SCORECARD PASS=48 FAIL=0`.

What did not change:

- No audit ledger/result files were edited.
- No new axiom was introduced.
- No retained status is claimed by this PR.

Next exact action: reviewer/auditor should re-audit
`free_dirac_wigner_action_strong_continuity_bridge_note_2026-06-07` against the
repaired dependency authority packet.

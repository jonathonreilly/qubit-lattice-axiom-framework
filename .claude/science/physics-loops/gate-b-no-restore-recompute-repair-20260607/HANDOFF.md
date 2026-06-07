# Handoff

Science block: Gate B no-restore recompute repair.

Files to review:

- `docs/GATE_B_NO_RESTORE_JOINT_PACKAGE_NOTE.md`
- `scripts/gate_b_no_restore_joint_package.py`
- `logs/2026-04-05-gate-b-no-restore-joint-package.txt`
- `outputs/gate_b_no_restore_recompute_certificate_2026_06_07.json`
- `logs/runner-cache/gate_b_no_restore_joint_package.txt`

What changed:

- The live `--recompute --write-certificate` path now writes a completed
  recompute certificate for all four rows.
- The default audit runner verifies the source log against the certificate.
- The recompute exposed stale Born residuals in the old source log/note; those
  rows now use the recomputed values.
- The refreshed cache reports `SCORECARD PASS=8 FAIL=0`.

What did not change:

- No audit ledger/result files were edited.
- No new axiom was introduced.
- No retained status is claimed by this PR.

Next exact action: reviewer/auditor should re-audit
`gate_b_no_restore_joint_package_note` against the repaired restricted packet.

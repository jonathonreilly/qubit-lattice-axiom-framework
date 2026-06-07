# Handoff

Science block: nonlabel grown basin recompute repair.

Files to review:

- `docs/NONLABEL_GROWN_BASIN_NOTE.md`
- `scripts/NONLABEL_GROWN_BASIN_TARGETED.py`
- `outputs/nonlabel_grown_basin_recompute_certificate_2026_06_07.json`
- `logs/runner-cache/NONLABEL_GROWN_BASIN_TARGETED.txt`

What changed:

- The live `--recompute --write-certificate` path now writes a completed
  recompute certificate for all three restore rows.
- The default audit runner verifies the frozen log against the certificate and
  re-checks zero/neutral gates, signs, double-source sign, and charge exponent
  arithmetic.
- The source note now cites the recompute certificate and displays the
  recomputed row values.

What did not change:

- No audit ledger/result files were edited.
- No new axiom was introduced.
- No retained status is claimed by this PR.

Next exact action: reviewer/auditor should re-audit `nonlabel_grown_basin_note`
against the repaired restricted packet.

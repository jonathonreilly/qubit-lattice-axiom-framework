# Handoff

This PR repairs a live latest-main runner/cache mismatch for the kinetic
isotropy conditional row.

What changed:

- H5 now checks that the B-W bridge-chain rows are named inspection rows for
  re-audit, not proof inputs or status authorities.
- The paired cache was refreshed to match the repaired runner text.

Verification:

- Runner passes: `SCORECARD: PASS=36 FAIL=0`.
- Cache status is fresh.
- Python compile passes.
- No audit data or ledger files were modified.

Remaining blockers:

- B-W readout/normalization is still not derived.
- The kinetic primitive is not retired.
- The named bridge-chain rows still require independent review/audit if they
  are to carry downstream authority.

Reviewer note:

This is intentionally not a main-refresh or audit-result PR. It is ready for
the reviewer to extract/land as appropriate.

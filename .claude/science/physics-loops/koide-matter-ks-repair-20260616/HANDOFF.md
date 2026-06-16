# Handoff

Branch: `physics-loop/koide-matter-ks-repair-20260616`

This block repairs the fresh post-audit Koide matter-attachment conditional row
without touching audit result files.

Files intentionally changed:

- `docs/KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md`
- `scripts/frontier_koide_matter_attachment_reduces_to_ks.py`
- `logs/runner-cache/frontier_koide_matter_attachment_reduces_to_ks.txt`
- `.claude/science/physics-loops/koide-matter-ks-repair-20260616/*`

What moved:

- The source note now matches the runner's normalized `-D^2` spectrum
  `{0,1,2,3}` and names `{0,4,8,12}` as the unscaled convention.
- Stale "unaudited KS" wording is removed; KS/Grassmann are treated as
  separate supplier rows whose status is audit-owned.
- The runner now reports 7 counted algebraic checks and 3 boundary lines,
  rather than counting narrative disposition assertions as PASS.

What did not move:

- No audit verdict is applied.
- No physical matter-state spinor-law bridge is claimed.
- The reviewer/auditor may still decide the row remains conditional on that
  bridge; this PR only removes the post-audit source defects.

Next exact action:

Run the listed checks, open a review PR, then return to the conditional backlog
and prefer another uncovered row not already covered by open PRs.

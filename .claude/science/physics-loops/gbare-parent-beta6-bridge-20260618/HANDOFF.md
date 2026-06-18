# Handoff

This block repairs `G_BARE_DERIVATION_NOTE.md` by sourcing the `beta=6`
surface from a finite-link/Wilson bridge instead of hard-coding it.

Artifacts:

- `docs/G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md`
- `scripts/g_bare_parent_finite_link_wilson_beta6_bridge_2026_06_18.py`
- repaired `docs/G_BARE_DERIVATION_NOTE.md`
- repaired `scripts/frontier_g_bare_derivation.py`

Review focus:

- Check that the Wilson scalar slot is legitimately the same scalar slot
  removed by finite-link rigidity.
- Check that the source does not claim Wilson action-form selection,
  continuum/global coupling closure, or an audit verdict.
- Check that no audit-owned files are modified.

Next exact action after PR review:

- If accepted, reviewer can extract the source repair and hand it to the
  independent audit/review flow for parent re-audit.

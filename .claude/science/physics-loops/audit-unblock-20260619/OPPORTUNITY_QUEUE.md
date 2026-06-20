# Opportunity Queue

1. Block112 selected:
   `quark_route2_exact_readout_map_note_2026-04-19`
   - source issue: critical row defaulted to `positive_theorem` even though the
     note and runner expose an exact missing-map obstruction.
   - repair: canonical `open_gate` metadata plus runner source-boundary guards.

2. Next action:
   Refresh the current ready queue after this PR lands in review. Prefer the
   next high-load-bearing ready row where the source note and runner already
   imply a narrower canonical claim type than the generated default.

3. Campaign constraint:
   Continue with independent source-side repairs only. Do not run `audit-loop`,
   do not apply verdicts, and do not push to `main`.

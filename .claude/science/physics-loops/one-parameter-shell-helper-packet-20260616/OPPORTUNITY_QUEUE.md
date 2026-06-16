# Opportunity Queue

1. `one_parameter_reduced_shell_law_note` helper packet cleanup.
   Existing PR #4050 had the science repair but included stale audit/front-door
   diffs. Rebuild source-only and push.

2. `scalar_trace_tensor_no_go_note` helper-source packet.
   Similar helper-source issue; should be checked after #4050 is clean.

3. Remaining scorecard mismatch rows.
   Good runner-hygiene targets after helper packet PRs are source-only.

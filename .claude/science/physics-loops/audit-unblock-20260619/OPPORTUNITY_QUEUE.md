# Opportunity Queue

Current block closed:

1. `causal_impact_parameter_note`
   - before: `bounded_theorem` from migration hint, no raw author claim-type
     hint.
   - after: source-authored `Type: bounded_theorem` and
     `Claim type: bounded_theorem`.
   - queue state: ready, zero-based queue position 1128, no serialized
     `queue_index` field in the JSON entry.

Next action:

Refresh from current `origin/main` and select another source note whose audit
row is blocked or degraded by missing/noncanonical source metadata. Prefer
ready rows with paired runners and low blast radius.


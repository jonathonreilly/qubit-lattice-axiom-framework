This PR targets the only uncovered audited conditional/failed/numerical-style
row found in the open-PR coverage scan:
`framework_bare_alpha_3_alpha_em_dimension_fixed_ratio_support_note_2026-04-25`.

Main already has a narrowed formal assumed-input theorem and a passing runner,
but the ledger still carries an old audited-failed verdict. Archived failed
rows are preserved by the pipeline rather than auto-invalidated, so this PR is
a same-path handoff for reviewer/auditor attention.

The patch changes only the archived source note. It does not edit the shared
canonical note, runner, cache, audit verdicts, queues, status summaries, or
publication matrices.

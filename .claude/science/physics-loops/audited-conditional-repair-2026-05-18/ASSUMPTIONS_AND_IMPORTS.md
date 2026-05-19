# Assumptions & Imports — audited_conditional repair 2026-05-18

## Campaign-level imports

This campaign does not introduce new physics imports. Each repair cycle
reuses **already-existing** scripts and cache files in `scripts/` and
`logs/runner-cache/`. The only thing being changed in each PR is the
dependency wiring of an existing source note.

## No-new-axiom check

PASS. No new axioms. No new admissions. No new fitted values.

## Counterfactual pass — what if a Tier A repair doesn't clean on re-audit?

**Counterfactual:** the audit lane's re-audit on the refreshed packet
still finds an honest blocker beyond file-attach (e.g., a missing
dep-edge to a retained authority, or upstream still unaudited).

**Direction this opens:**
- The row settles at `audited_conditional` with a sharper
  `notes_for_re_audit_if_any` pointing at the next obstruction.
- This is still progress: the repair class shifts from
  `runner_artifact_issue` to a deeper class, and the audit packet is
  now closer to closure.
- For positive-retained promotion attempts to fail at this stage is
  not a campaign failure — it's the cascade-resolution mechanism
  working as designed. Continue.

## Counterfactual — what if the upstream parent is not retained?

**Counterfactual:** for `missing_dependency_edge` repairs, the
authority being cited is itself `audited_conditional`.

**Direction this opens:**
- Repair settles at `audited_conditional` with
  `notes_for_re_audit_if_any: dependency_not_retained`.
- Per audit-loop SKILL §"audited_conditional from dependency_not_retained
  is normal", this is expected and the cascade re-audit picks it up
  when upstream lands.
- For the campaign, this is still a useful move: it converts an
  ambiguous repair-class row into an unambiguous cascade-pending row.

## Counterfactual — what if the runner cache is stale?

**Counterfactual:** the registered cache `logs/runner-cache/<runner>.txt`
has a different SHA than the current runner source.

**Direction this opens:**
- Refresh the cache via `python3 scripts/cached_runner_output.py
  scripts/<runner>.py` before linking.
- Per audit-loop SKILL §"Compute-Limited Backlog Repair", commit the
  refreshed cache file with the source-note edit in the same PR.

## Forbidden imports for this campaign

- No new admitted physical conventions.
- No new bridge theorems that aren't explicit one-step algebra from
  retained primitives (Tier B only).
- No literature imports without `--literature` flag (the user has not
  passed it).
- No promotion of `audited_failed` rows; only `audited_conditional`.

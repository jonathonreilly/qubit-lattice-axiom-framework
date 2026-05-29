# Handoff

Target row: `observable_principle_from_axiom_note`.

Repair summary:

- The old row load-bore on P2, an unregistered scalar-generator selection
  premise.
- This branch withdraws the selection claim and preserves only the exact
  finite `W[J] = log|det(D+J)| - log|det D|` source-response theorem.
- The runner now includes a source note firewall ensuring old P1+P2 conditional
  selection wording is absent.

Verification before PR:

- `python3 -m py_compile scripts/frontier_hierarchy_observable_principle_from_axiom.py`
- `python3 scripts/frontier_hierarchy_observable_principle_from_axiom.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`
- Pipeline result: target row reset to `unaudited`, ready audit queue rank 3,
  `audited_conditional` count 14, ready queue count 58 after rebase to
  `origin/main@22a274dd2`.

Reviewer should not merge directly; extract the science and let the audit lane
assign any effective status.

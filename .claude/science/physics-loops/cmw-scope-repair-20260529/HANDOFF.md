# Handoff

Target row:
`axiom_first_coleman_mermin_wagner_theorem_note_2026-04-29`.

Repair summary:

- Replaced the broad Coleman-Mermin-Wagner substrate-minimality framing with a
  bounded IR-sum threshold packet.
- Runner now emits formal IR-threshold closeout flags and explicit non-claims
  for `d_s = 3` minimality, Ward normalization, and D9/kernel authority.

Verification before PR:

- `python3 -m py_compile scripts/axiom_first_coleman_mermin_wagner_check.py`
- `python3 scripts/axiom_first_coleman_mermin_wagner_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`

Pipeline result:

- Target row queued `unaudited`.
- Audit queue rank: 562.
- Ready queue count: 63.
- Effective status counts after regeneration: `audited_conditional=14`,
  `unaudited=1197`.
- Target row has `open_dependency_paths=[]` after narrowing.
- Stale audit invalidations: 0.

`git diff --check` remains the final pre-commit check.

Reviewer should extract the IR-threshold packet without treating it as a full
Mermin-Wagner or substrate-minimality theorem.

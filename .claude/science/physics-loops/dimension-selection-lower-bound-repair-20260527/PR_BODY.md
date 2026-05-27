## Summary

This PR repairs `dimension_selection_note` by narrowing it to finite-runner
lower-bound support.

It no longer claims that self-consistency uniquely selects `d = 3`. Instead,
it routes the supported lower-bound surface through the retained-bounded
finite-k centroid-sign bridge:

- `d <= 2` fails the runner's lower-bound criteria;
- `d = 3,4,5` pass those criteria;
- upper-bound `d <= 3` remains separate and unclosed here.

## Verification

- `python3 scripts/frontier_dimension_selection_lower_bound_parent_repair.py`
  - `SUMMARY: PASS=29 FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/DIMENSION_SELECTION_NOTE.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete
- `git diff --check`
  - clean

## Pipeline Result

- `dimension_selection_note`: `unaudited`, `claim_type=bounded_theorem`
- Runner: `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`
- Dependency: `dimension_selection_finite_k_centroid_sign_bridge_note_2026-05-25`
  (`retained_bounded`)

## Boundaries

- No new axioms.
- No retained retag.
- No unique-`d = 3` theorem.
- No repo-wide dimension axiom rewrite.

# Author handoff: explicit integrated-manifest staging

AUTHOR COMPLETE — independent review pending; not a source or landing PASS.

Worktree: `/private/tmp/review-drain-20260915/skill-fix`, detached base `5deabeb698a27c2c3f68c5df685af2521ef15307`. Seven intended files, all uncommitted; no staging, commits, pushes, GitHub mutations, or science/audit source edits. Prior review reports preserved.

## Result

Adds the explicit full-run `--stage-citation-manifest` option. Immediately after successful stage1b generation it executes only `git add -- docs/audit/data/citation_graph_manifest.json`. Default full and verdict-only invocations retain their index behavior. Multiple arguments (including combining the options), duplicates, and unknown options exit 2 before pipeline effects. Existing `set -e` stops on generation or staging failure. This does not auto-commit, alter the invariant, apply audit status, or add a second graph build.

The review-loop combined invocation, command, preflight, and contract checker now agree. The skill requires prior intended-topology inspection, final manifest inspection, preservation through cleanup, and inclusion in the committed integration replay before freezing the final tree. The same one combined full validation remains required.

## Actual validation

- Real pipeline-shell fixture tests with real Git index: 6 tests OK (4.136 s final run). Producer commands are stubbed; assertions cover fresh manifest index before stage1c and stage18, single graph build, unrelated dirty path left unstaged, unchanged default, unchanged verdict-only, failed producer/staging, and invalid arguments. These are control-flow tests, not a full science pipeline.
- Review-loop contract checker: OK, 29 families.
- Review-loop contract tests: 71 tests OK (13.513 s). Includes mutation removing the new option from the combined invocation.
- `bash -n docs/audit/scripts/run_pipeline.sh`: exit 0.
- `vocab_lint.py --report-only` on all seven intended paths: zero violations.
- `git diff --check`: clean.
- Read the complete authored tracked diff and new test source before handoff.

Initial test run exposed the command checker still matching the former no-option invocation: 70-test suite had one failure and checker reported command_unit_validation. Updated that exact expectation to the new command, then the 71-test suite and checker passed. No test failure concealed. No full science pipeline run by this author; combined candidate gate belongs to coordinator after independent source review.

## Frozen file SHA-256

- `.claude/commands/review-loop.md`: `c37d2d015825fe0d78463b66a944bac7cd68b84235a8ce31a8800ded4c57e7fe`
- `docs/ai_methodology/skills/review-loop/PREFLIGHT.md`: `e6bbf30b38c19816755479fbc24359cce25c656b418eb6c7c5f8adc76a9f8fa3`
- `docs/ai_methodology/skills/review-loop/SKILL.md`: `3bc61e8301b06b699400dc31320f8213b5449c1a628a2efc56234651c569ce1a`
- `docs/audit/scripts/check_review_loop_skill_contract.py`: `ef9dbc807c39f8e278c57811958b490019444f66293528044ea704d712dffd2b`
- `docs/audit/scripts/run_pipeline.sh`: `338638f351dd37d2c5a591b09ce912bbcc4d38c33cbf26fadf8091f8be4ef3e5`
- `docs/audit/scripts/tests/test_review_loop_skill_contract.py`: `1ec6c5b70fd4d70dda9a76acb4aa04ca180b706543f38b1abaae153107e701c8`
- `docs/audit/scripts/tests/test_pipeline_manifest_staging.py`: `92a741eca3a0927780ddcb4d8e1e26374f12b49915c4789d8d0cc6d02fe2afbe`

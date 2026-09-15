# Independent review: explicit citation-manifest staging

Reviewer session: /root/backlog_topology. Base:5deabeb698a27c2c3f68c5df685af2521ef15307. Scope:exactly seven changed files, including the new test. Individual SHA-256 and Git blob identities are in skill-fix-review.json. I did not author this patch and made no source edits, commits or external mutations.

## Result

No material findings. The change addresses the observed stage1b/stage18 mismatch directly: the generator writes a deterministic manifest to the working tree, while collect_graph_manifest_check reads the Git index. The explicit full-run flag stages only that freshly generated path before downstream work. The invariant remains unchanged.

## Source and behavioral review

Read the complete pipeline shell, complete added test, complete seven-file diff, affected skill/command/preflight/checker contexts, actual manifest generator and actual stage18 index comparison. The generator parses the graph before writing; exceptions remain nonzero. The shell's set -euo pipefail applies to the direct generator and git add commands. Generation failure cannot stage the new manifest; staging failure cannot reach stage1c or the invariant. The existing abort trap retains its cleanup behavior.

The parser accepts zero arguments or exactly one supported option. Unknown arguments, duplicate options, both option orders and extra arguments exit2 before checkpoint/pipeline effects. Default full mode does not stage. Verdict-only skips graph generation and keeps its existing checkpoint proof. Only the exact manifest path is added; unrelated index/worktree content remains unchanged. No commit or other generated-output staging is introduced.

The combined executable gate invokes the option once. Command reference and checker agree. Its mutation test rejects removal of the option. Full combined pipeline/lint/evidence checks and failure short-circuit remain mandatory; no extra pre-pipeline graph build or per-unit full run is added.

Automatic staging is a mechanical acknowledgment, not semantic topology review. The skill requires prior topology inspection against reviewed source and final exact-manifest inspection. It explicitly retains the acknowledgment in the committed integration replay before freezing the landing tree, preventing generated cleanup from dropping it. Existing exact base/tree receipts and changed-source confirmation rules remain intact.

## Independent verification

- Six actual pipeline-shell/real-index fixture tests:OK,3.989s. Covers one graph build/write, staging before1c/18, path scope, default/verdict-only behavior, generation failure, index-lock failure and invalid options.
- Seventy-one contract tests:OK,12.266s, including active executable combined-gate checks.
- Contract checker:OK,29families.
- bash -n and git diff --check:exit0.

Additional reviewer scratch cases rejected four deliberately broken shells: removed staging, broad git add -A, ignored staging failure and ignored generator failure. A fifth case verified existing unrelated staged bytes remain unchanged. Evidence:check-skill-fix/adversarial.json. Acceptance does not rely on the author's test report.

Producer commands in these fixtures are stubbed. Tests establish shell/index behavior, not science-pipeline success. Actual generator and index-invariant source inspection connects them to the observed failure. The coordinator still owns integrated current-main gates and final candidate provenance.

FINAL VERDICT: PASS

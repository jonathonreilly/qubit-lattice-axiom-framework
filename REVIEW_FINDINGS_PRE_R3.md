# Confirmation Review Findings — Round 3

Scope: PR #5403 plus `origin/handoff/ci-workflows-20260716`
Review refs:

- `origin/main`: `cd33b5a06d2016de9f733dd9131cc19442ff24f2`
- PR #5403 head: `4764d579807e27dff91fbe6ea37dbc535cf377d7`
- handoff head: `48c25cacc3d7c67c4a27aaf94490890f0c4323c2`

## Findings

### 1. BLOCKER — `pr-smoke` can skip audit tests after a detector failure

Classification: `BUG`

The post-patch `.github/workflows/pr-smoke.yml:61-65`
(`CI_WORKFLOWS_2026-07-16.patch:113-117`) places this pipeline directly in an
`if` condition:

```bash
if git diff --name-only "origin/${{ github.base_ref }}...HEAD" -- docs/audit/scripts | grep -q .; then
  python -m unittest discover -s docs/audit/scripts/tests
else
  echo "audit scripts unchanged; skipped"
fi
```

The step explicitly selects `shell: bash`, for which GitHub invokes Bash with
`-e -o pipefail`. Bash nevertheless suppresses `errexit` for commands tested
by `if`. Consequently, a nonzero detector pipeline is treated as the false
branch, which prints “unchanged; skipped” and exits successfully.

Independent reproduction with a nonexistent comparison ref produced:

```text
fatal: bad revision 'origin/__missing_review_r3_base__...HEAD'
audit scripts unchanged; skipped
simulated step exit=0
```

There is a second manifestation for sufficiently large output: `grep -q`
can close the pipe after the first match, the producer can receive `SIGPIPE`,
and `pipefail` can again select the successful skip branch.

Required correction: obtain the changed-file list in a fail-closed command
before the conditional, then test whether the captured value is nonempty.

### 2. BLOCKER — the documented copy-over template would undo live workflow hardening

Classification: `REPO_GOVERNANCE`

The requested narrow comparison passes: the PR template and the handoff
postimage of live `audit.yml` have byte-identical install blocks, both using
`requirements-release.txt`.

The template as a whole is nevertheless substantially stale relative to live
`audit.yml`, while `docs/audit/templates/README.md:14-20` instructs users to
copy the whole file over `.github/workflows/audit.yml`.

Material divergences include:

- the template re-enables the full audit workflow for pull requests, whereas
  current live `audit.yml` deliberately leaves PR validation to review-loop;
- the template omits the live missing-dependency-edge repair and
  conditional-prompt regeneration steps;
- the template substitutes old PR-only cache/pipeline advisory behavior for
  the live full-main refresh behavior;
- the template rebases generated outputs after a push race, whereas live
  `audit.yml` resets to current `origin/main` and deterministically regenerates
  them.

Thus the round-2 pin-reversion defect is fixed, but following the still-current
copy instruction would revert other, more recent workflow behavior. The
template must be synchronized with live `audit.yml`, or the whole-file copy
instruction must be replaced with a safe installation/update procedure.

### 3. BLOCKER — `CI_INTEGRATION.md` offers a conflicting unpinned drop-in workflow

Classification: `REPO_GOVERNANCE`

`docs/audit/CI_INTEGRATION.md:72-108` calls its inline YAML a workflow to
“drop into `.github/workflows/audit.yml`,” so it is an actionable alternative
installation instruction, not merely pseudocode.

That workflow:

- has no dependency-install step, so it does not install
  `requirements-release.txt`;
- uses push plus an unfiltered PR trigger, while the surrounding instructions
  describe narrow PR paths, nightly schedule, and `workflow_dispatch`;
- omits `workflow_dispatch`;
- commits on main pushes rather than only schedule/manual refreshes;
- lacks the explicit `contents: write` permission needed by its push step.

This is inconsistent with both the pinned template and the surrounding
normative prose. Remove the drop-in example, mark it non-installable
pseudocode, or synchronize it with the canonical workflow.

### 4. NIT — handoff prose overstates `pipefail` coverage

Classification: `NIT`

`CI_WORKFLOWS_README.md:14-16` and the format-patch description at
`CI_WORKFLOWS_2026-07-16.patch:18-19` say `pipefail` applies to every
multi-command step. The two-command “Install pinned dependencies” step
(`CI_WORKFLOWS_2026-07-16.patch:87-90`) does not specify `shell: bash` or set
`pipefail`; GitHub's unspecified Linux shell is `bash -e`, whereas explicit
`shell: bash` adds `-o pipefail`.

This does not create a runtime masking defect because the install step has no
pipeline, but the absolute documentation claim is false. Narrow it to the
changed-file detection/test steps or make the install step explicit.

GitHub shell reference:
https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstepsshell

## Claimed-fix verification

All four round-2 findings are repaired:

1. No stale `REVIEW_FINDINGS_PRE.md` is present in the final handoff tree,
   branch delta, or patch payload.
2. The handoff README accurately states the exact payload, identifies PR
   #5403 as a prerequisite, and explicitly says the requirements pin is not in
   the patch.
3. `pr-smoke` now has `docs/audit/scripts/**` in both its PR path filter and
   audit-test change detector, so an ordinary shell-only change such as
   `docs/audit/scripts/run_pipeline.sh` selects the workflow and test step.
4. PR #5403 pins `docs/audit/templates/audit_workflow.yml` to
   `requirements-release.txt`; its install block is identical to the live
   `audit.yml` block produced by the handoff patch.

Additional exact checks:

- `git diff --name-status origin/main...refs/tmp/pr-5403` contains exactly:
  `docs/audit/templates/audit_workflow.yml` and `requirements-release.txt`.
- The release requirements now contain the same five package names as
  `requirements.txt`, including `pyyaml==6.0.3`, with no missing or extra
  package names.
- The handoff branch delta contains exactly
  `CI_WORKFLOWS_2026-07-16.patch` and `CI_WORKFLOWS_README.md`.
- Required payload parsing returned exactly:

  ```text
  4  3  .github/workflows/audit.yml
  65 0  .github/workflows/pr-smoke.yml
  ```

- The patch applies cleanly, with whitespace checking enabled, to the exact
  PR #5403 head and to a virtual current-main-plus-#5403 merge tree.
- Both reconstructed workflow YAML files parse successfully.
- Template/live install-block SHA-256 values match:
  `8f339d435ea40db6c1865f93153e45756a5e3de18f9bdaf8f78e0b196de09397`.
- The audit-tooling suite completed: 356 tests, all passing. Its generated
  worktree side effects were reversed immediately; no tracked change remains.

## Review-loop disposition

- Iterations: 1 confirmation iteration
- Blocking findings: 3
- Nonblocking findings: 1
- Fixes applied: 0 (review-only instruction)
- Physics/import/Nature/no-go/labeling review: not applicable
- Audit verdicts applied: 0
- Commits/pushes: 0
- Recommendation: FAIL pending the three blocking corrections above

VERDICT: FAIL

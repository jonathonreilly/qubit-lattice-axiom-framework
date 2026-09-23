# Combined candidate validation

Required whenever the final review candidate or an integrated landing candidate needs the combined mechanical gate. Read and apply the [validation placement and receipt-reuse rules](REVIEW_UNITS.md) and [audit-compatibility gates](AUDIT_COMPATIBILITY.md). For a named uncommitted review-only candidate, append `--include-worktree` to the changed-evidence command as those rules require; `--no-fix` and `--no-commit` still control. The landing-tree commitment and push provisions apply only to authorized landing. This shared excerpt grants no landing or audit authority.

For a named review-only candidate, run the mutating validation recipe in a
disposable isolated copy of the frozen reviewed source. Include the actual
staged, unstaged and untracked reviewed content and all declared inputs; a
checkout of `HEAD` alone does not reproduce an uncommitted proof edit. Verify
the copied source/input identities against the reviewed candidate, preserve
the caller's source and index, and keep validation logs outside disposable
storage. In that copy, use `--include-worktree` for changed-evidence checking;
`--stage-citation-manifest` may stage the generated manifest only there.
Do not execute the landing commit, replay or push instructions for this mode,
and do not create an iteration commit under `--no-commit`. Record the tested
base, source/input identities and worktree delta, including any generated
topology acknowledgment, without claiming that an uncommitted candidate has
landed. A later landing must bind its final candidate to the actual validation
receipt under the placement rules; a matching `HEAD` alone is insufficient.

   On the frozen integrated candidate, first inspect the intended topology
   changes against the reviewed source. Use the explicit full-run option below
   to stage only the freshly generated citation-graph manifest immediately after
   stage 1b; stage 18 checks the index, not the working-copy manifest. This avoids
   a separate pre-pipeline graph build. The option cannot be combined with
   `--verdict-only`; ordinary pipeline callers do not stage anything.
   Run one combined validation pass (or reuse the identical successful receipt
   under the [placement rule](REVIEW_UNITS.md)):

   ```bash
   TRAIN_COMBINED_VALIDATION_SCOPE=integrated-candidate
   if ! { bash docs/audit/scripts/run_pipeline.sh --stage-citation-manifest \
          && python3 docs/audit/scripts/audit_lint.py --strict \
          && python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main; }; then
     echo "FAILED: combined validation; preserve log and do not land" >&2
     exit 1
   fi
   ```

   Restore only identified generated audit outputs under the [Audit-System
   Compatibility Gate](AUDIT_COMPATIBILITY.md), regenerate the citation-graph manifest when required,
   inspect its exact acknowledgment, and retain it in the final committed
   integration sequence before freezing the landing tree. Do not strip this
   intended acknowledgment with generated audit residue or leave it only staged:
   the landing replay must reconstruct the validated tree. Then run the final
   clean-state checks:

   ```bash
   TRAIN_COMBINED_CLEAN_SCOPE=integrated-candidate
   if ! { review_base=$(git merge-base origin/main HEAD) \
          && git diff --check "$review_base"..HEAD \
          && git diff --check \
          && git diff --cached --check; }; then
     echo "FAILED: candidate diff checks; do not land" >&2
     exit 1
   fi
   ```

   Full pipeline/lint/evidence work is shared across the exact integrated
   candidate. No component is considered landed until this combined gate passes.
   Record command results and log hashes, tested base/tree and final landing
   tree, reviewer/unit provenance, and any skipped check with its reason.

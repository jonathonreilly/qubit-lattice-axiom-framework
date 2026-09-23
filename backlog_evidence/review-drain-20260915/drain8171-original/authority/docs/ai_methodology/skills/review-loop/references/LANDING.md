# Backlog review and landing

Required for an actual unspecified or focus-text-only review-loop invocation, a set of PRs, or any authorized landing. Apply the backlog scheduling steps only to backlog mode. Named review-only runs use [combined validation](COMBINED_VALIDATION.md) without acquiring landing authority. Before closing or rejecting any PR, also read [Salvage Pass](SALVAGE.md) and preserve the [branch and dependent-PR recovery rules](../SKILL.md#model-and-tool-boundary).

## Default Entry: Parallel PR Review, Any Orchestrator (owner-directed 2026-07-17)

An UNSPECIFIED invocation — no named branch or PR — IS the parallel
backlog drain, as is invoking against a SET of open PRs ("review the open
PRs", "drain the PR backlog"): enumerate the backlog, review in parallel, and
land confirmed components through the double-buffered trains below — no
topology decisions required from the invoker. Free-text
focus without a named target (e.g. "imports") is the drain with that
emphasis applied in every slot. Reviewing one branch or one PR is the
special case that requires naming the target, and ANY flag without a named
target is invalid — stop and ask for a target (see Arguments; the
review-only flags contradict the drain's land-end-to-end contract).

1. **Enumerate targets**: open, non-draft PRs in scope (drafts stay out of
   scope per the [draft rule](REVIEW_UNITS.md)). Detect stacks and cumulative-tower
   branches first, inspect owner reservations, and form the coherent review
   [units](REVIEW_UNITS.md). Separate dependent units review and land bottom-up; independent
   units may proceed in parallel.

   Before allocating a reviewer wave, run
   `python3 scripts/review_loop_backlog_inventory.py` (use `--json` for the
   complete machine-readable snapshot). It amortizes the GitHub enumeration
   into one read-only `gh pr list` invocation and reports declared-base stack
   order, unresolved bases, registered worktrees and unregistered `rev-*`
   recovery candidates, external findings files, disk and observed worker-CLI
   headroom, and capacity-bounded candidate slots. Re-run it before each wave
   because PRs, worktrees, disk, and the shared process pool move independently.

   The helper's `ready` label means only `baseRefName == main` with no detected
   existing checkout or PR-scoped recovery artifact. It never launches a worker and grants no review,
   science, merge, audit, or landing readiness. Its topology is limited to
   declared GitHub base edges: still perform the cumulative-history,
   merge-base, and independent delta checks here, and still run every applicable [lens](SCIENCE_LENSES.md) and
   [gate](AUDIT_COMPATIBILITY.md). Inspect every reported existing worktree/findings path for
   ownership and recovery before creating a duplicate; the helper never
   prunes, removes, or modifies one.
2. **One isolated worktree per review unit.** Parallel reviews never share a
   worktree or a checkout; shared worktrees race and have destroyed findings
   in this repo's history.

   **Worktree lifecycle (disk discipline — mandatory).** Concurrent reviews
   plus abandoned per-cycle confirm trees have repeatedly exhausted the host
   disk. Guard on free space and remove each verified-clean disposable worktree
   on exit. Alternatively, use the bounded exclusive sequential checkout pool
   in [`references/OPERATIONS.md`](OPERATIONS.md): its guarded release preserves the exact HEAD,
   rejects tracked/untracked/ignored residue and unfinished Git operations, and
   retains ownership on failure. Install its release handler instead of the
   disposable removal trap; never concurrently share a slot or force cleanup.
   The standard disposable lifecycle is:

   ```bash
   # POSIX df reports 1 KiB blocks here; check the filesystem that will hold WT.
   REPO_ROOT=$(git rev-parse --show-toplevel)
   REVIEW_TMP_ROOT=${TMPDIR:-/tmp}
   git -C "$REPO_ROOT" worktree prune
   avail_kb=$(df -Pk "$REVIEW_TMP_ROOT" | awk 'NR == 2 {print $4}')
   case "$avail_kb" in
     ''|*[!0-9]*) echo "ENOSPC guard: cannot read free space for $REVIEW_TMP_ROOT" >&2; exit 1 ;;
   esac
   [ "$avail_kb" -ge 5242880 ] || {
     echo "ENOSPC guard: less than 5 GiB free on $REVIEW_TMP_ROOT — not spawning" >&2
     exit 1
   }

   WT=$(mktemp -d "$REVIEW_TMP_ROOT/rev-<N>.XXXXXX")
   cleanup_review_wt() {
     [ -e "$WT" ] || return
     python3 - "$REPO_ROOT" "$WT" <<'PY_REVIEW_CLEAN'
   from pathlib import Path
   import sys
   sys.path.insert(0, str(Path(sys.argv[1]) / "scripts"))
   from science_fix_loop import cleanup_worktree
   removed, reason = cleanup_worktree(Path(sys.argv[2]))
   if not removed:
       print(f"cleanup retained worktree for recovery: {sys.argv[2]}: {reason}", file=sys.stderr)
   PY_REVIEW_CLEAN
     git -C "$REPO_ROOT" worktree prune
   }
   trap cleanup_review_wt EXIT
   trap 'exit 130' INT
   trap 'exit 143' TERM

   git -C "$REPO_ROOT" worktree add -q "$WT" <branch-or-ref>
   ```

   Apples-to-apples measurement from the same object store on 2026-08-14 was
   343.6 MiB for a fresh full worktree and 326.3 MiB for the proposed sparse
   baseline, only about 5% less. Review and pipeline inputs span every root,
   so a sparse default adds omission risk without a material disk benefit.
   Use a normal full worktree; the operational gain comes from prompt cleanup,
   not from counting the shared Git object store as part of every checkout.

   For disposable worktrees the `trap` is not optional: it removes a verified-clean worktree on normal
   exit and catchable INT/TERM termination. The shared cleanup helper preserves
   dirty work, valuable ignored artifacts, unverifiable trees, and any HEAD not
   yet preserved on main. It prints the recovery path and never force-removes a
   worktree. This review trap does not delete local branches. `git worktree prune` at the start of a drain clears
   stale metadata whose directories are already gone. Neither mechanism can
   catch `SIGKILL` or remove an abandoned directory that still exists, so
   inventory such directories separately instead of claiming that the trap
   handles every crash mode.
3. **One reviewer process per review unit at a time**, applicable lenses combined
   into a single pass (two for large diffs), findings written incrementally
   to `FINDINGS=$(mktemp "$REVIEW_TMP_ROOT/review-findings-pr<N>.XXXXXX")`
   outside the disposable worktree, verdict line last. For a multi-PR unit,
   use a unit identifier and list all constituents in that findings file.
   Freeze every constituent's original changed-file snapshot before creating
   that file. Remove it only
   after its findings and verdict are recorded in every constituent's provenance;
   if the worker fails, report its recovery path. The findings file and any
   reviewer scratch artifacts are named scope exclusions — they never enter
   `files_to_review`, the changed-file set, or any commit. This is
   the budget-adapted default of the [Reviewer Fanout section](SCIENCE_LENSES.md#reviewer-fanout): under
   the shared-pool budget, cross-unit parallelism replaces per-lens
   parallelism. Use extra seats only for an identified escalation or explicit
   owner request; spare capacity alone does not require per-lens fanout.
4. **Concurrency budget (shared codex pool).** Reviewer processes share one
   pool with the audit lane's auditor seats and judicial panels. Keep the
   TOTAL concurrent codex processes across every lane at or under ~8-10
   (measured 2026-07-17: ~18 concurrent processes collapsed audit-lane
   throughput from 6-11 landed verdicts/hour to ~1 every 3 hours). When the
   audit drain is running at 4+ seats, run at most 2-3 concurrent PR
   reviewers; scale up only in a quiet pool.
5. **Land confirmed units in continuously collected trains of at most eight.**
   A component is one coherent review unit as defined in [REVIEW_UNITS.md](REVIEW_UNITS.md). Review, fixes,
   and focused confirmation stay with that unit's original reviewer session.
   Multiple constituent PRs share one scientific review only through the
   complete frozen disposition map; one unrelated unit's PASS confers no
   authority on another.

   A component may enter the collecting train only when all of the following
   are frozen together: every constituent PR number and original PR-head SHA,
   exact reviewed source-only commit list, resulting tree SHA,
   confirmation-base SHA, changed-file and interacting-file sets, head
   repositories and branches, disposition-map SHA-256, source/input hashes,
   findings file SHA-256, reviewer thread/session identity, and that same
   session's explicit `FINAL VERDICT: PASS` on the final source. Focused
   confirmation MUST resume the reviewer thread/session that issued the
   findings. That same reviewer thread/session must confirm fixes;
   do not launch a new reviewer process to confirm fixes.
   Give that reviewer the fixed files, prior findings, and necessary interacting
   context. Record any newly necessary source inspection or edit as a scope
   expansion; a new edit needs confirmation before the component is frozen again.
   If the session cannot be recovered, a PR head moved, any frozen value no
   longer matches, or the reviewer did not explicitly pass the final state,
   fail closed and do not land that component; do not enroll it.

   The train scheduler is a double buffer:

   - collect compatible confirmed units while the coordinator is occupied;
   - depart with the useful ready batch as soon as the coordinator is available;
     do not wait for an arbitrary collection deadline or an unfinished reviewer;
   - eight eligible units close the collecting train immediately;
   - atomically freeze the departing membership and open the next empty
     collecting train immediately, before the frozen train is integrated.
     Reviews and confirmations that finish during integration feed the next
     train instead of waiting for the landing to finish;
   - dependent PRs may share a train only as one confirmed coherent unit.
     Distinct units with overlapping non-generated paths or unreviewed semantic
     dependencies cannot share a train: combine them into a newly reviewed
     coherent unit, or land the earlier unit and recheck the next against
     current main. The citation-graph manifest is the sole generated-path
     overlap handled inside integration.

   In this skill, a **flush** means only “stop collecting and freeze the
   current membership.” It never skips review, confirmation, integration, or
   validation. A named focused-mode target is a requested completion boundary:
   once confirmed, flush its one-component train unless the operator explicitly
   put it into an ongoing backlog drain. Record membership and departure reason;
   elapsed time is not a review or readiness criterion.

   One coordinator owns one clean, disposable integration worktree for the
   frozen train. This is an integration function, not a second reviewer or a
   new source-editing lane. Fetch the latest `origin/main`, verify every frozen
   component again, and cherry-pick its exact reviewed source-only commits once
   in deterministic unit order, oldest first within each unit. Deduplicate
   inherited commits; never replay ancestor content already included in a
   cumulative unit. Run the Stale PR Integration Guard for every constituent.
   A source conflict, PR-head change, missing confirmation, or provenance
   mismatch ejects the affected unit to its original worker for same-session
   focused re-review against current main; hold any dependent units too, then
   rebuild and validate the candidate without them. The coordinator may resolve
   only the generated manifest case below.

   Every component passes the focused checks and every applicable reviewer
   lens before enrollment. The combined gate is mechanical; it does not
   replace or routinely repeat the unit-scoped semantic reviewers. Before
   running it, compare interacting-file sets and dependency edges. Integration
   source changes or a new cross-unit semantic interaction return all affected
   units to their original reviewer sessions for confirmation on the integrated
   files. Otherwise their frozen unit verdicts remain the semantic authority.
   Check the final source-only delta against current main, including inherited
   science and all omitted/generated paths, before starting validation.

   Before landing, read and run the mandatory
   [combined candidate validation](COMBINED_VALIDATION.md) excerpt under the
   [validation placement and receipt rules](REVIEW_UNITS.md). It includes the
   combined pipeline/strict-lint/evidence pass, generated-output cleanup,
   manifest acknowledgment, clean-state checks, and exact-tree receipts.
   No component is landed until those gates pass.

   After the combined gate passes, push the exact candidate once to `main`.
   `origin/main`'s fast-forward atomicity remains the serializer. If main moved
   after the train base was fetched, do not replay a stale PASS or force-push:
   fetch, rebuild the entire candidate on the new base, rerun the combined
   gate, and try the ordinary fast-forward push again. A
   conflict touching only `docs/audit/data/citation_graph_manifest.json`
   is resolved by regenerating it from the landed tree
   (`build_citation_graph.py` then `write_citation_graph_manifest.py`),
   never by hand-merge; a manifest regeneration touches only that generated
   acknowledgment surface, so it needs no new reviewer round — any OTHER
   conflict fails the landing closed and returns the PR to its worker for
   re-review on a rebased head. PROACTIVE rule, not just on conflict: when
   the commits being landed change citation-graph TOPOLOGY — adding or
   removing any graph node, or rewiring any dependency edge — the landing
   set must INCLUDE a
   refreshed `docs/audit/data/citation_graph_manifest.json`
   (`build_citation_graph.py` then `write_citation_graph_manifest.py`,
   staged into the landing) — otherwise the enforced stage-18 guard blocks
   every subsequent pipeline run on main until someone lands the
   acknowledgment for you. `build_citation_graph.py` registers every
   non-skipped `docs/**/*.md` file as a node before extracting any edge, so
   a newly added note with zero markdown links is a node addition and
   triggers this rule exactly like an edge rewire.
   After cherry-picking a frozen commit set that carries the manifest, rerun
   those generators on the integrated tree before EVERY push attempt, even
   when Git reports no conflict. Git can merge two independent topology
   additions without a textual conflict while coalescing their `node_count`
   increments; only current-tree regeneration detects that semantic stale
   manifest. Stage the regenerated manifest and amend the newest cherry-picked
   commit when its bytes changed. This generated-only integration repair needs
   no new reviewer round; every source conflict still returns to the reviewer.
   The landing loop refuses any tracked staged or unstaged residue at entry.
   Between retries it may restore only the generated manifest to the current
   `HEAD`, clearing a failed regeneration without discarding reviewed source.
   Generated-output restoration is a COMMIT-time rule (see the
   [audit-compatibility gate](AUDIT_COMPATIBILITY.md)), not a landing-time step: the component commits
   are already clean. The train's fail-closed landing loop is, exactly:
   ```bash
   # Record these immediately after the combined gate and generated-output
   # cleanup, before entering the push loop.
   VALIDATED_BASE=<origin-main-sha-used-by-the-combined-gate>
   VALIDATED_TREE=<combined-candidate-tree-sha>
   # Exact reviewed source-only commits from each frozen unit, units in
   # recorded deterministic order and each unit's commits oldest first.
   # Include each commit once; PR inventories include ALL constituents.
   COMMITS=(<pr-a-oldest> ... <pr-a-newest> <pr-b-oldest> ...)
   PR_NUMBERS=(<pr-a-number> <pr-b-number> ...)
   PR_HEADS=(<pr-a-frozen-head-sha> <pr-b-frozen-head-sha> ...)
   if [ "${#PR_NUMBERS[@]}" -ne "${#PR_HEADS[@]}" ]; then
     echo "FAILED: PR number/head inventory mismatch" >&2
     exit 1
   fi
   verify_frozen_pr_head() {
     local pr="$1" expected="$2" live_ref actual
     case "$pr" in
       ''|*[!0-9]*) return 1 ;;
     esac
     live_ref="refs/tmp/review-loop-train-pr-$pr"
     if ! git fetch -q origin "+pull/$pr/head:$live_ref"; then
       return 1
     fi
     actual="$(git rev-parse --verify "$live_ref")" || return 1
     [ "$actual" = "$expected" ]
   }
   verify_frozen_pr_heads() {
     local index
     for index in "${!PR_NUMBERS[@]}"; do
       if ! verify_frozen_pr_head \
            "${PR_NUMBERS[$index]}" "${PR_HEADS[$index]}"; then
         return 1
       fi
     done
   }
   refresh_manifest=""
   for commit in "${COMMITS[@]}"; do
     if git diff-tree --no-commit-id --name-only -r "$commit" -- \
          docs/audit/data/citation_graph_manifest.json \
          | grep -qx docs/audit/data/citation_graph_manifest.json; then
       refresh_manifest=1
       break
     fi
   done
   if ! git diff --quiet || ! git diff --cached --quiet; then
     echo "FAILED: landing worktree has tracked residue before integration" >&2
     exit 1
   fi
   landed=""
   for attempt in 1 2 3 4; do
     git cherry-pick --abort >/dev/null 2>&1 || true
     # A failed generator/write/add/amend may leave only the generated
     # manifest dirty after a completed cherry-pick. Restore exactly that path
     # to the current HEAD before retrying; never reset arbitrary reviewed work.
     if [ "$refresh_manifest" = 1 ] \
        && ! git restore --source=HEAD --staged --worktree -- \
             docs/audit/data/citation_graph_manifest.json; then
       echo "FAILED: could not clear generated manifest retry residue" >&2
       exit 1
     fi
     # Name the destination explicitly: isolated/partial repos may have no
     # remote.origin.fetch refspec, in which case a plain fetch leaves the
     # local origin/main stale and creates fake non-fast-forward "races".
     if ! { git fetch -q origin \
              +refs/heads/main:refs/remotes/origin/main \
            && git switch -q --detach origin/main; }; then
       sleep 3; continue
     fi
     if [ "$(git rev-parse origin/main)" != "$VALIDATED_BASE" ]; then
       echo "FAILED: main moved; rebuild and rerun the combined gate" >&2
       exit 1
     fi
     cherry_pick_complete=""
     last_conflicted_commit=""
     if git cherry-pick "${COMMITS[@]}" >/dev/null 2>&1; then
       cherry_pick_complete=1
     fi
     # Continue the same sequencer through every manifest-only conflict.
     # A failed --continue may have advanced to a different commit; inspect
     # that new failure before deciding whether another repair is allowed.
     while [ -z "$cherry_pick_complete" ]; do
       if ! conflicts="$(git diff --name-only --diff-filter=U)"; then
         echo "FAILED: could not inspect cherry-pick conflicts" >&2
         exit 1
       fi
       if [ "$conflicts" != "docs/audit/data/citation_graph_manifest.json" ]; then
         git cherry-pick --abort >/dev/null 2>&1 || true
         echo "FAILED: source conflict or sequencer failure; return the unit to its worker" >&2
         exit 1
       fi
       if ! conflicted_commit="$(git rev-parse --verify CHERRY_PICK_HEAD)"; then
         echo "FAILED: manifest conflict has no identifiable cherry-pick head" >&2
         exit 1
       fi
       if [ "$conflicted_commit" = "$last_conflicted_commit" ]; then
         echo "FAILED: manifest repair made no sequencer progress" >&2
         exit 1
       fi
       last_conflicted_commit="$conflicted_commit"
       if ! { python3 docs/audit/scripts/run_citation_graph_build.py >/dev/null \
              && python3 docs/audit/scripts/write_citation_graph_manifest.py >/dev/null \
              && git add docs/audit/data/citation_graph_manifest.json; }; then
         echo "FAILED: manifest generation or staging during cherry-pick" >&2
         exit 1
       fi
       if GIT_EDITOR=true git cherry-pick --continue >/dev/null; then
         cherry_pick_complete=1
       fi
     done
     # A conflict-free textual merge can still coalesce independent manifest
     # counts. If this landing carries the manifest, rebuild it from the
     # integrated tree on every retry and amend only generated bytes.
     if [ "$refresh_manifest" = 1 ]; then
       if ! { python3 docs/audit/scripts/run_citation_graph_build.py >/dev/null \
              && python3 docs/audit/scripts/write_citation_graph_manifest.py >/dev/null \
              && git add docs/audit/data/citation_graph_manifest.json; }; then
         echo "FAILED: final manifest generation or staging" >&2
         exit 1
       fi
       if ! git diff --cached --quiet; then
         if ! GIT_EDITOR=true git commit --amend --no-edit >/dev/null; then
           echo "FAILED: could not commit regenerated manifest" >&2
           exit 1
         fi
       fi
     fi
     if [ "$(git rev-parse 'HEAD^{tree}')" != "$VALIDATED_TREE" ]; then
       echo "FAILED: integrated tree differs from the validated candidate" >&2
       exit 1
     fi
     if ! verify_frozen_pr_heads; then
       echo "FAILED: PR head moved; dissolve the train without pushing" >&2
       exit 1
     fi
     if git push -q origin HEAD:main; then
       landed="$(git rev-parse HEAD)"
       break
     fi
     sleep 3
   done
   if [ -z "$landed" ]; then
     echo "FAILED: landing did not complete after 4 attempts" >&2
     exit 1
   fi
   if ! git fetch -q origin \
          +refs/heads/main:refs/remotes/origin/main; then
     echo "FAILED: could not refresh origin/main for containment verification" >&2
     exit 1
   fi
   if ! git merge-base --is-ancestor "$landed" origin/main; then
     echo "FAILED: $landed not contained in origin/main" >&2
     exit 1
   fi
   echo "LANDED $landed"
   # Build the close-ready set one PR at a time from a post-push head check.
   for index in "${!PR_NUMBERS[@]}"; do
     pr="${PR_NUMBERS[$index]}"
     expected="${PR_HEADS[$index]}"
     if verify_frozen_pr_head "$pr" "$expected"; then
       printf 'CLOSE_READY %s %s\n' "$pr" "$expected"
     else
       echo "LEAVE_OPEN $pr: PR head moved after landing" >&2
     fi
   done
   ```
   Every step is conditioned; push success captures the landed sha; retry
   exhaustion and non-containment both exit nonzero — the loop can never
   report success without the landed sha verified inside `origin/main`.
   Before closing each constituent, verify its accepted/narrowed/superseding
   source and evidence on current `origin/main` against the disposition map;
   record rejected/deferred content and its preserved recovery handle. Commit
   containment alone does not establish constituent content coverage. A PR with
   deferred content remains open unless its separate close-with-reason
   disposition is explicit; never delete its recovery branch for partial salvage.
   A `CLOSE_READY` line is only a head/containment observation, not content
   approval or permission that survives another command. Refetch
   that PR head again immediately before its own close. If it differs from the
   frozen SHA, leave that PR open and its branch intact, and record that only the
   older reviewed head landed. For an unchanged same-repository head, use the
   lease-protected branch-deletion and dependent-base preservation rules in
   [Model And Tool Boundary](../SKILL.md#model-and-tool-boundary);
   close only after the required checks and exact lease succeed. Never let one moved head prevent unaffected train members from
   being checked and closed individually.

   If combined validation fails, preserve the failing command and log, do not
   push any part of the candidate, and dissolve the train. Rebuild its
   units as one-component trains in dependency order on fresh current main,
   using the same landing loop and the same unit review and same-session
   confirmation requirements. Keep a coherent multi-PR unit intact; do not
   split away its load-bearing inherited source to guess a failing component.
   Do not guess a culprit, auto-bisect scientific
   content, or quarantine a PR from a shared failure. This fallback spends more
   validation only on the exceptional failing train and keeps the common clean
   path fast.
6. **Who may kick it off: any orchestrator** — any Claude tier, a codex
   session, or a human. The orchestration is process: every finding and
   every PASS/FAIL verdict comes from the configured reviewer model's seats,
   the orchestrator fixes only per Fix Policy, and nothing lands without a
   reviewer PASS on its final state. The orchestrator never self-certifies.
   Substituting a different reviewer family for a round (for example a
   fresh-context reviewer when the codex lane is unavailable) requires
   explicit owner authorization for that episode and must be disclosed in
   the PR's provenance comment.

7. **Progress reports every 15 minutes.** While any slot is active, emit a
   summary block to the operator surface at least every 15 minutes — never
   silence for a long session: a per-PR table (PR number, phase — reviewing
   round N / fixing / confirmation / landing / landed / closed-with-reason —
   reviewer runtime, and the finding count so far read from that PR's
   incremental findings file), landings so far with their main SHAs, the
   remaining queue, and the current codex process count against the budget.
   A session that stops early still emits a final block with the same
   fields; the [Final Report section](FIXES_AND_REPORTING.md#final-report) remains the full closing artifact.

The [remaining required procedures](../SKILL.md#required-reference-routing) apply to each complete review unit,
through final source confirmation, as the inner loop of each parallel slot;
no referenced requirement is weakened by running slots concurrently. The train coordinator
performs the shared full mechanical validation and landing after those independent
source reviews pass. The [validation placement rule](REVIEW_UNITS.md) controls repeated
pipeline/lint/evidence references throughout this skill.

## Stale PR Integration Guard

When landing one or more PRs, protect already-landed science before applying
any branch content. A PR branch may be based before another PR just landed, so
checking out whole files from that stale PR head can erase current-main source
science in shared files.

For every PR before integration:

```bash
git fetch origin \
  +refs/heads/main:refs/remotes/origin/main \
  pull/<N>/head:refs/tmp/pr-<N>
pr_base=$(git merge-base origin/main refs/tmp/pr-<N>)
comm -12 \
  <(git diff --name-only "$pr_base"..origin/main | sort) \
  <(git diff --name-only "$pr_base"..refs/tmp/pr-<N> | sort)
```

If the overlap list is non-empty, or if earlier PRs have landed during the
same review-loop run, do **not** run `git checkout refs/tmp/pr-<N> -- <file>`
for those paths. Integrate the PR's delta against its merge base with a
three-way patch, rebase/merge, or cherry-pick source commits, then resolve any
conflicts by preserving both current-main science and the salvageable PR
science:

```bash
git diff --binary "$pr_base"..refs/tmp/pr-<N> -- <source paths> > /tmp/pr<N>.patch
git apply --3way /tmp/pr<N>.patch
```

Whole-file checkout from a PR head is allowed only when the file is new on the
PR or when `git diff --quiet "$pr_base"..origin/main -- <file>` proves current
`main` has not changed that path since the PR base. For every overlapped
source path, do a science-loss guard after integration: the current-main diff
from `pr_base` to `origin/main` must still be represented in the final file.
If that cannot be verified quickly, stop and treat it as a blocking integration
hazard rather than risking science loss.

Generated audit JSON/Markdown is a special case: do not hand-merge generated
files from stale PR heads. Resolve source files first, prefer the current
`origin/main` generated audit surface, then rerun the audit pipeline and strict
lint to regenerate it.

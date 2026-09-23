# Audit-system compatibility and scientific PASS gates

Required when the branch adds or edits source notes, runners, claim tables, lane stubs, or publication/control-plane files, and whenever a gate below matches the changed content. Read the complete gate before claiming review-loop PASS. Apply the [validation placement rule](REVIEW_UNITS.md) and [combined validation recipe](COMBINED_VALIDATION.md); references to pipeline work here are not extra full runs.

## Audit-System Compatibility Gate

This gate is mandatory when a branch adds or edits source notes, runners,
claim tables, lane stubs, or publication/control-plane files.

The review loop must enforce the audit lane's propose/ratify split without
performing the independent audit:

**Audit-hash churn guard.** Non-semantic hygiene sweeps on audited source notes
can be scientifically harmless while still invalidating large parts of the
audit ledger, because note hashes are source-content hashes. Before landing any
branch that touches many existing claim-note files for formatting, link-target,
path, vocabulary, or other non-science cleanup, run the pipeline in validation
mode and inspect the `seed_audit_ledger.py` / `invalidate_stale_audits.py`
counts. If the change would reset or requeue already-audited rows solely due to
non-semantic churn, do not land the broad source sweep. Either narrow the PR to
non-ledger/non-claim surfaces, land a reviewed hash/canonicalization tooling
repair first, or ask for explicit user approval to spend the audit capacity.
Never trade a clean audit graph for cosmetic source-note churn without making
that cost explicit.

**Dependency/axiom impact guard.** `science_fingerprint_v2` binds the complete
framework-premise epoch and dependency-policy epoch. A branch that changes an
axiom/approved primitive, premise membership or classification, document
authority/admission registry, citation/dependency extraction policy,
chain-sufficiency policy, or the fresh-look dependency standard must inspect
the pipeline's resulting invalidation set before PASS. The safe default is a
fresh scientific audit for every mismatching fingerprint, including
transitive consumers. Narrowing that blast radius requires a separate,
reviewed machine-readable equivalence/impact record; neither the PR author nor
review-loop may silently declare existing scientific judgments unaffected.
`docs/audit/data/legacy_science_epoch_baseline.json` is an immutable
deployment anchor, not a rolling manifest: never refresh it to make a policy
change pass. A mismatch must invalidate remaining pre-v2 judgments or be
resolved by a separately reviewed, row-specific provenance migration.

0. Before applying a PR, inventory any audit-status surface it touches:

```bash
git diff --name-only <pr-base>..refs/tmp/pr-<N> -- \
  docs/audit docs/KEY_SCIENCE.md \
  docs/repo/FRONT_DOOR_STATUS.md docs/repo/RETAINED_BACKBONE.md
git diff <pr-base>..refs/tmp/pr-<N> -- \
  docs/audit docs/KEY_SCIENCE.md \
  docs/repo/FRONT_DOOR_STATUS.md docs/repo/RETAINED_BACKBONE.md \
  | grep -E 'audit_status|effective_status|audited_clean|audited_conditional|audited_failed|audited_renaming|audited_decoration|audited_numerical_match|previous_audits|audit_result|verdict'
```

Treat this output as a provenance review, not as a merge recipe. Strip
PR-submitted generated ledgers, queues, effective-status tables, auditor
transcripts, and audit verdict payloads before landing. The only acceptable
audit-lane changes from a PR are reviewed source/tooling repairs and
machine-readable audit/re-audit targeting metadata, such as dispatcher
sidecars, that do not assert a verdict. After applying the source repair, run
the local pipeline to verify the row is queued or re-queued as intended, then
restore only generated audit residue to the branch's own `HEAD` before
committing; preserve reviewed source, controlled data, and dispatcher sidecars.
Importing moving `origin/main` into the index of a stale branch stages unrelated
audit changes. Pipeline
regeneration of `docs/audit/data/`, the generated audit queue/dispatch Markdown,
and `docs/repo/FRONT_DOOR_STATUS.md` / `docs/repo/RETAINED_BACKBONE.md` is a
VALIDATION step only; framework PRs must never ship these files because the
merge would overwrite the audit lane's ratified state. The audit-loop run on
`main` (nightly cron plus `audit:` commits) is the sole channel for landing
those outputs.

1. Source-note `Status:` prose is not an audit authority. New or touched claim
   notes should use `Type:` / `Claim type:` metadata for intended audit
   classification.
2. If a no-go/firewall is intended to be theorem-grade, use
   `claim_type = no_go`; do not rely on support-style prose and expect audit
   ratification.
3. Keep disclaimers such as "This is not charged-lepton mass closure" outside
   audit metadata fields.
4. Do not prefill or recommend a verdict in author/review surfaces. Wording
   such as `target_audit_status: audited_clean`, `audit_status =
   audited_clean`, `effective_status = retained`, or "can land audited_clean"
   is not review-loop compatible. Use wording like `audit_status_authority:
   independent audit lane only` and "effective status is pipeline-derived
   after audit ratification and dependency closure."
5. Changed claim notes that cite load-bearing authorities must use markdown
   links, for example
   ``[`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)``.
   Code-formatted names such as `` `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` `` do
   not seed graph dependencies and are not enough.
6. After source fixes, satisfy the full pipeline, strict lint, and diff checks
through the [combined validation pass](COMBINED_VALIDATION.md). Run focused checks per unit; do
not add a full run here for each unit or constituent. The known graph-cycle
warning is acceptable. Any strict-lint error blocks a review-loop landing PASS.

6a. **Changed-science evidence-readiness PASS gate (hard).** In that same
combined pass, after the full pipeline has executed or refreshed every changed
runner, use `check_changed_audit_evidence.py --base origin/main` as shown in
[COMBINED_VALIDATION.md](COMBINED_VALIDATION.md).
For an uncommitted review-only candidate, append `--include-worktree`. Inspect
and repair source/evidence defects per unit before final source confirmation;
the combined gate checks the entire integrated delta once.

This gate is mechanical preparation, not an audit. It must pass for every
changed row not classified as `meta`, `open_gate`, or `decoration`, including
every such row bound to a changed primary or helper runner. A missing runner,
invalid/unreadable declared input, stale or failed SHA/input-bound compute
result, or incomplete forensic N5 resolution certificate blocks review-loop
PASS. Intentionally incomplete work must be typed as an explicit `open_gate`
and remains outside this seat-readiness gate until promoted; do not let the
independent audit discover a deterministic compute omission after spending a
seat. The cache/result used here is non-authoritative review evidence only.
The audit lane must still execute the current runner live and authenticate its
invocation-bound stdout before applying a verdict.

`--include-worktree` covers the committed delta plus staged, unstaged, and
untracked candidate paths. Use it for author preflight and review fixes,
including `--no-commit` sessions; the default CLI scope covers committed
changes only and cannot establish evidence readiness for an uncommitted fix.
The gate reads working-copy bytes. A path with both staged and unstaged changes
blocks candidate PASS: stage its intended final bytes, or unstage that path for
working-copy review, then rerun. Never use a clean working copy to certify a
different staged version. Recheck after any later source edit or staging change
that changes the bytes proposed for landing.

**`note_hash` drift is a notice for non-retained rows, an error only for
retained-grade rows.** `note_hash` is a *source-content* hash, not an audit
verdict. When a review fix edits a claim note, its `note_hash` drifts from the
seeded value; `audit_lint.py` reports this drift as a non-blocking
`note_hash_drift_reaudit_pending` **notice** when the row is not retained-grade
(`unaudited` / `audited_conditional` / pending), because re-audit is simply
pending and the audit-lane re-seed refreshes the hash. Such a notice does **not**
block review-loop PASS and must **not** be "fixed" by committing audit-lane
ledger churn (that is the forbidden pipeline-output commit). A `note_hash`
mismatch on a **retained-grade** row (`retained` / `retained_bounded` /
`retained_no_go`) stays a hard **error**: an edited retained note laundered past
a stale ratification is a real integrity violation. Resolve it by re-auditing
(the audit lane re-seeds and archives the prior verdict) or by demoting the edit
per the audit-hash churn guard — never by refreshing the hash while keeping the
retained verdict.

**Stuck-row repair requeue gate.** Terminal non-clean rows
(`audited_conditional` / `audited_renaming` / `audited_failed` /
`audited_numerical_match`) re-enter the audit queue only through their own
note or paired-runner hash drift, an upstream `deps_changed` invalidation, or
a dispatcher-sidecar re-audit target. Dependent-side edits never reschedule
the stuck row. When a branch's stated purpose is repairing such a row (the PR
title/body names the row or quotes its audit repair target):

1. Verify the stuck row itself will requeue: its note or paired runner
   changes on the branch, or the branch ships dispatcher-sidecar targeting
   metadata naming the row.
2. If the audit-named repair is dependent-side only (for example, narrowing
   dependents' citing sentences to the audited scope), add a dated
   downstream-hygiene line to the stuck row's own note boundary as part of
   the landing: a one-line source-side record of what changed downstream
   (date + what was narrowed + PR number), with no grade or verdict
   language. The hash drift re-enters the row into the ordinary queue and
   the re-auditor (or second auditor) sees the recorded condition.
3. Run the validation pipeline and confirm the row is queued or re-queued as
   intended, then restore generated audit outputs per the
   pipeline-output-stripped gate below.
4. Repair-PR review checklist: the audit repair target is quoted verbatim
   (from `verdict_rationale` / `notes_for_re_audit_if_any`) in the PR body;
   a sibling-runner pin sweep was done before every note edit (grep
   `scripts/` for runners pinning the edited sentences); no authored grade
   language anywhere; no `docs/audit/data/` content beyond
   dispatcher-sidecar targeting metadata and the citation-graph manifest
   acknowledgment (`docs/audit/data/citation_graph_manifest.json`) when the
   landed commits change graph dependencies (see the [landing loop's
   proactive rule](LANDING.md)).

7. **Pipeline-output-stripped PASS gate (hard).** After running the pipeline
   for validation, the framework PR must NOT land any pipeline-regenerated
   audit-lane or effective-status surface. The independent audit lane is the
   sole authority for these files; a framework PR that ships them creates a
   dual-source-of-truth and overwrites the audit lane's ratified state at
   merge. The following must hold for review-loop to issue PASS:

```bash
# Inventory data changes: distinguish forbidden generated authority from
# reviewed controlled sidecars and the intended topology acknowledgment.
git status --porcelain docs/audit/AUDIT_DISPATCH_QUEUE.md \
                       docs/audit/AUDIT_QUEUE.md \
                       docs/audit/MISSING_DERIVATION_PROMPTS.md \
                       docs/audit/data \
                       docs/repo/FRONT_DOOR_STATUS.md \
                       docs/repo/RETAINED_BACKBONE.md
```

Inspect every listed change. Generated verdict/ledger/queue/status changes
block PASS and must be stripped. Reviewed controlled data and dispatcher
sidecars are allowed when they assert no verdict; the topology manifest is
allowed when the source changes graph topology. Do not erase the entire data
directory or untracked files indiscriminately. The shared helper below
restores only identified generated residue to the branch's own `HEAD`, fails
on errors, and preserves source-side sidecars. Inspect the remaining diff and
regenerate the manifest from the final intended topology before staging.

```bash
python3 - <<'PY_CLEAN'
from pathlib import Path
import sys
sys.path.insert(0, "scripts")
from science_fix_loop import publication_changed_paths, strip_generated_audit_outputs
root = Path.cwd()
strip_generated_audit_outputs(root, publication_changed_paths(root))
PY_CLEAN
# Only when the landed commits add/remove a graph node or rewire an edge:
python3 docs/audit/scripts/run_citation_graph_build.py
python3 docs/audit/scripts/write_citation_graph_manifest.py
git add docs/audit/data/citation_graph_manifest.json
git status --porcelain   # second line of defense: exactly the intended paths
```

The pipeline is run for VALIDATION only — to confirm the source repair is
ingested and the runner row is queued or re-queued as intended. The
audit-loop pipeline run on `main` (nightly cron + `audit:` commits) is the
sole channel for landing the regenerated outputs. Framework PRs that ship
these files force a destructive overwrite of ratified audit state at merge
time and have been an active source of broken-row regressions.

8. **Repository-portable links PASS gate (hard).** Markdown link targets on
   branch-modified `.md` files must be repo-relative or web URLs. Absolute
   local paths such as `/Users/<name>/...`, `/home/<name>/...`,
   `/private/tmp/...`, `/tmp/...`, `/var/...`, `/opt/...`, or `file://...`
   inside a markdown link target are non-portable: they break for other
   developers, CI runners, fresh clones, and independent reviewers.

```bash
# Must produce no output. Scans branch-modified markdown for local absolute
# paths inside markdown link targets.
git diff --name-only origin/main...HEAD -- '*.md' \
  | xargs -I{} grep -nE '\]\((/Users/|/home/|/private/|/tmp/|/var/|/opt/|file://)' {} 2>/dev/null
```

If this command prints lines for files the branch is already modifying for
source, runner, methodology, or review reasons, rewrite the offending link
targets before PASS. The usual mechanical fix is to preserve the display text
and replace the target with a `../` chain relative to the source file's
directory, e.g. in `docs/SOURCE_RESOLVED_FOO_NOTE.md` rewrite
`(/Users/me/Projects/Physics/scripts/foo.py)` to `(../scripts/foo.py)`.

This gate prevents new non-portable links from landing; it is not a license for
large standalone cosmetic sweeps over audited claim notes. If the PR's only
purpose is to rewrite existing local-path links across many audited source
notes, apply the audit-hash churn guard above before landing any broad cleanup.

9. **No-Go Discipline PASS gate (hard).** Before issuing review-loop PASS,
   identify any artifact on the branch that ships a negative claim:

```bash
# Source notes whose claim_type is no_go, or whose Status / Type line
# names walls / open conditions / "conditional on" content
git diff --name-only origin/main...HEAD -- 'docs/*NO_GO*.md' 'docs/*BOUNDED*.md' \
                                           'docs/*STRETCH_ATTEMPT*.md' \
                                           'docs/*OBSTRUCTION*.md'
# Audit-data shards whose verdict_rationale or claim_type record walls
git diff origin/main...HEAD -- docs/audit/data/ledger docs/audit/data/ledger_meta.json \
  | grep -E '"claim_type": "no_go"|"verdict_rationale".*wall|"verdict_rationale".*condition'
# Any source note touched on this branch whose body contains negative-claim shape
git diff origin/main...HEAD -- 'docs/*.md' \
  | grep -E 'structurally undecidable|no retained primitive|requires new axiom|cannot be derived from A_min|conditional on .* walls?'
```

For every match, the NoGoDisciplineReviewer must output `PASS` (N1-N8 walk
complete and no failure condition hit) before review-loop issues PASS. A
`FAIL` from NoGoDisciplineReviewer blocks PASS regardless of how other
reviewers voted. An unscrutinized no-go that ships through review cements
the overclaim at audit time and can wrongly discourage later investigation. Retained no-go conclusions
remain revisable when a proof defect, changed domain, or new mechanism is shown.

If NoGoDisciplineReviewer outputs FAIL, apply the narrowest honest fix per
Fix Policy step 2 (demote to a narrower honest claim that passes N1-N8) and
re-review. Do not weaken the gate to PASS the branch.

This gate is independent of the Pipeline-clean PASS gate above; both must
pass for review-loop to issue PASS.

10. **Math-runner independent-check PASS gate (hard).** Before issuing
review-loop PASS for any branch that changes a runner, proof script, numeric
constant, matrix construction, optimizer, expected value, or note formula,
record the independent math check used by `CodeRunnerReviewer`. At least one
check must not share the same implementation path as the changed runner:
manual formula derivation, symbolic/algebraic reduction, finite toy-case
enumeration, independent recomputation, or invariant/limit tests. A runner
that merely computes its own target and prints PASS is not a proof that the
formula is correct. If an issue was reopened because the runner's math was
wrong, treat the whole formula family as suspect until the changed expression
and any reused helpers are cross-checked.

11. **Proof-obligation scope PASS gate (hard).** When changed content claims a
theorem, proof, derivation, reduction, or closure through intermediate lemmas,
run `ProofObligationReviewer`. `CLOSED` supports the stated proof boundary.
`CONDITIONAL` supports only a claim whose exact premise and narrower scope are
explicit. `EQUIVALENT-GAP` forbids proof-complete or near-closure framing and
requires demotion to `open_gate`, support, or the strongest independently
proved lemma. `FAIL` blocks PASS until the proof is repaired or narrowed.

12. **Native-language PASS gate (hard).** Changed repo-facing text must use
controlled, native repo vocabulary. Run `scripts/vocab_lint.py --fix` on all
branch-modified files before landing, then inspect changed headings, metadata,
runner banners, claim scopes, table labels, and review comments for
branch-local/draft language that the linter cannot know about. PR-specific
labels, draft-branch vocabulary, campaign names, and noncanonical theory
phrases must be rewritten into repo-native language or explicitly deferred in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`; do not land them silently.

13. **Landed-evidence PASS gate (hard).** Audit evidence must LAND with the
PR, not live in its body. The same changed-evidence invocation in gate 6a
covers every changed note or runner whose row the audit lane will consume;
do not run it again solely for this gate. Treat any reported
`forensic_evidence_ready: false` on an affected row as a blocking finding.
In particular, for negative-claim-shaped changes (notes
whose rhetoric trips the N5 scan phrases in
`docs/audit/scripts/no_go_discipline_gate.py`):

- the primary runner's cached stdout must carry the five-line N5 execution
  certificate (`per_element:`, `per_site:`, `per_mode:`, `per_block:`,
  `lattice_wide:` — each honest and substantive, using "checked and not
  executed — <reason>" where a class is genuinely not exercised); and
- the N1-N8 checklist required by the no-go-discipline gate must be a
  committed artifact (a `## No-Go Discipline Gate` section in the note or a
  committed sidecar), not only PR-body text.

Rationale: packets that existed at review time but did not land are the
largest audit-invalidation class in repo history (1,560 voided verdicts;
799 in one day for `no_go_discipline_packet_missing`). A PASS with
un-landed evidence recreates that failure mode. Repairing the evidence
(adding honest certificate lines, landing the checklist) is in scope for
the review; fabricating resolution coverage is not — a runner that
genuinely cannot certify a resolution class states so honestly, and if the
claim's rhetoric then over-reaches the certificate, the claim is narrowed,
not the certificate padded.

The review loop must not run `docs/audit/scripts/apply_audit.py` and must not
write `audit_status`, `audited_clean`, or other audit verdicts. If the branch
introduces retained-grade `claim_type` rows, report those claim IDs in the
final report as requiring the independent audit worker.
When a source repair changes a note or runner for a previously audited row,
the local result is `note_hash`/runner-hash drift plus queue/dispatch
visibility for independent re-audit. For a non-retained row this drift is a
benign `note_hash_drift_reaudit_pending` notice (see the Audit-System
Compatibility Gate) — it does not block strict lint and must not be repaired by
committing ledger churn. For a retained-grade row the drift is a strict error
that must be resolved by re-audit, not laundered. In all cases, do not preserve,
copy, or author a fresh `previous_audits` entry, `audit_status`, or verdict
rationale from the PR branch; the independent audit lane (nightly cron +
`audit:` commits) is the sole channel that refreshes the hash and re-ratifies.

After the pipeline, inspect the changed claim rows in
`docs/audit/data/audit_ledger.json`:

- `claim_type` must match the intended class (`positive_theorem`,
  `bounded_theorem`, `no_go`, `open_gate`, `decoration`, or `meta`).
- `audit_status` must remain `unaudited` unless the branch is only carrying
  already-audited history from `origin/main`.
- `effective_status` must be pipeline-derived, not hand-authored.
- New theorem/no-go/bounded rows with declared load-bearing authorities must
  have non-empty `deps` matching the markdown-linked authorities.
- Dependencies asserted as retained-grade must currently have
  `effective_status` in `{retained, retained_bounded, retained_no_go}`. Open
  gates, `unaudited`, `audit_in_progress`, `retained_pending_chain`, and
  terminal non-clean audit statuses are blockers for retained-grade claims.

Useful review-only inventory:

```bash
python3 - <<'PY'
import json, subprocess
changed = set()
for cmd in (
    ["git", "diff", "--name-only", "HEAD"],
    ["git", "diff", "--name-only", "--cached"],
):
    changed.update(subprocess.check_output(cmd, text=True).splitlines())
try:
    changed.update(subprocess.check_output(
        ["git", "diff", "--name-only", "origin/main...HEAD"], text=True
    ).splitlines())
except Exception:
    pass
rows=json.load(open("docs/audit/data/audit_ledger.json"))["rows"]
for cid,row in rows.items():
    if row.get("note_path") in changed:
        print(cid, row.get("claim_type"), row.get("audit_status"),
              row.get("effective_status"), row.get("deps"),
              row.get("note_path"))
PY
```

If generated audit files conflict while integrating current `origin/main`, do
not hand-merge generated JSON/Markdown. Resolve source files, prefer the
current remote generated audit files, then rerun `run_pipeline.sh` and strict
lint so the generated surface is rebuilt from source.

# Reusable review operations

Use these helpers from the same reviewed skill revision as `SKILL.md`.
They perform mechanical checks, never scientific review, audit or landing.
Read this reference only when preserving history, managing a checkout pool,
or fetching a newly discovered child PR. Unit receipts are documented in
`UNIT_RECEIPT.md`; do not load every reference into every reviewer prompt.

## Exact historical payload storage

For large or repetitive historical packets, `scripts/review_workspace.py archive`
reads each distinct Git blob once through one persistent `git cat-file` process.
It stores deterministic gzip objects by raw SHA-256. Every original path, mode
and blob identity retains a separate manifest entry and review disposition.
Equal bytes permit reuse of a verified payload read only with unchanged caller
context and premises; they never establish equivalent scientific conclusions.

```bash
python3 "$SKILL_DIR/scripts/review_workspace.py" archive \
  --repo "$REPO_ROOT" --revision "$FROZEN_HEAD" --prefix "$HISTORY_PREFIX" \
  --destination "$ARCHIVE_DEST" --namespace pr123 \
  --keep HANDOFF.md --keep fixtures/input.json > "$EVIDENCE_DIR/archive-receipt.json"
```

Identify history before calling this command. Enumerate **every current proof,
runtime, fixture and link target** in `--keep` (paths relative to the prefix).
Selected targets remain plain files with distinct names and original modes.
The helper does not discover consumers, rewrite links, or decide which material
is historical. Review the returned mapping and all affected consumer changes;
run actual helper/input discovery before freezing or executing evidence.
Never replace active inputs with opaque gzip objects or silently drop duplicate
original paths, inherited evidence, deleted content or failed attempts.

Freeze the newly generated manifest's SHA-256 in the independent review receipt,
alongside the original revision and verified complete Git inventory. For reuse:

```bash
python3 "$SKILL_DIR/scripts/review_workspace.py" verify-archive "$ARCHIVE_DEST" \
  --expected-manifest "$REVIEWED_MANIFEST_SHA256"
```

Without the externally anchored digest, verification establishes only internal
payload consistency, not complete original inventory or review provenance.
Do not take the expected digest from the potentially changed archive itself.
Preserve the manifest and decoded raw hashes in durable provenance. Existing
destinations are never overwritten; verify and reuse them or create a new one.
Compression is an option for measured size/duplication costs, not a reason to
repackage every small packet or rerun already valid scientific evidence.

## Exclusive sequential checkout reuse

A bounded pool can replace repeated clean worktree creation/removal. Each slot
has exactly one owner and one review unit at a time. Pool operations serialize
with an OS lock; a persistent journal records ownership and preserved commits.
Keep findings and receipts outside the pool. Keep the skill's disk-space guard
and capacity limit; idle slots still consume space.

```bash
python3 "$SKILL_DIR/scripts/review_workspace.py" acquire \
  --repo "$REPO_ROOT" --pool "$POOL" --slot reviewer-one \
  --owner "$UNIT_ID" --base "$FROZEN_BASE"
# Complete the unit; preserve all evidence and commit the reviewed source.
python3 "$SKILL_DIR/scripts/review_workspace.py" release \
  --repo "$REPO_ROOT" --pool "$POOL" --slot reviewer-one \
  --owner "$UNIT_ID" --expected-head "$VERIFIED_FINAL_HEAD"
```

Use `PYTHONDONTWRITEBYTECODE=1` for Python tooling when practical. Release checks
the exact owner and HEAD, detached state, unfinished Git operations, and tracked,
untracked **and ignored** residue. It preserves HEAD under a dedicated Git ref
before making the slot idle. Acquire checks the preservation ref and clean state
before changing an idle slot's base. No reset, clean, forced removal or adoption
of an unknown path occurs. A local preserved ref is recovery storage, not proof
that content landed remotely. Preserve required remote provenance separately.

Install an exit/INT/TERM handler that attempts this guarded release using the
last independently verified HEAD. On failure, retain ownership and report the
recovery path; never mark the slot free or delete its artifacts. After a crash,
inspect the retained owner, Git state and journal. Do not automatically steal a
slot. Standard disposable worktrees continue to use the skill's cleanup trap.

## Fresh child heads before base maintenance

GitHub can reveal a child PR whose commit has never been fetched locally.
Before computing its original delta, freeze current metadata and fetch its head:

```bash
python3 "$SKILL_DIR/scripts/review_workspace.py" fetch-head \
  --repo "$REPO_ROOT" --repository "$GITHUB_REPOSITORY" \
  --number "$CHILD_PR" --expected "$OBSERVED_CHILD_HEAD" \
  > "$EVIDENCE_DIR/child-fetch.json"
```

The helper requires an open PR, verifies the fetched PR ref equals the observed
head, and rechecks metadata after fetching. Any movement fails the freeze.
Use the verified commit to preserve the original merge base and binary delta;
retain its decoded hash if compressing that historical delta. Then follow the
full skill rules for retargeting, fresh head checks, exact-lease parent deletion
and post-delete recovery. Drafts and children outside the frozen review backlog
receive base preservation only; this operation never enrolls or accepts them.

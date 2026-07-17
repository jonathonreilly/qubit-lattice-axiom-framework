# Author Pre-Flight — run before requesting review

Purpose: drain every mechanically-checkable and source-verifiable defect from
a change BEFORE an adversarial reviewer sees it, so review rounds converge in
one or two passes and reviewer effort goes to deep findings. This checklist
was distilled from the 2026-07-16/17 front-door campaign, where multi-round
reviews repeatedly caught the same defect classes. It is an authoring
discipline, not a gate: the review loop and the independent audit lane remain
the only authorities, and a clean pre-flight grants a change no standing.

Reviewers may cite a skipped pre-flight item as a finding when the defect it
would have caught is present.

## 1. Sources, not memory

Every sentence that characterizes a claim, a note, or a status is written
with the source open — the note's own claim/boundary section, the ledger
shard, or the registered policy doc — and asserts nothing stronger than the
source's own wording. Session memory, PR titles, and campaign shorthand name
targets; they are never quotable claim text. If you did not just read it, do
not write it.

## 2. Numbers and dates

Every count, total, or date you quote is recomputed at your current HEAD from
its authority (ledger shards, `effective_status_summary.json`, generated
views) and carries an as-of qualifier when the value moves with the nightly.
Volatile numbers in durable prose need either a companion runner that
re-derives them (the `FALSIFIABLE_PREDICTIONS` pattern) or a dated stamp
naming the ledger state they quote. One document must not carry two
incompatible as-of dates.

## 3. Status words

Grep your diff for grade vocabulary (`retained`, `retained_bounded`,
`retained_no_go`, `promoted`, `ratified`, `audited_*`). Every hit is either
(a) verified against the row's shard at HEAD, (b) status-neutral wording, or
(c) inside a dated historical/changelog line. Author surfaces never pre-state
a verdict; `proposed_*` / `support` / `bounded` / `open` are the only
author-side status words.

## 4. Vocabulary

List every noun phrase your change introduces to categorize claims, lanes, or
tiers. Each must already exist in
[`docs/repo/CONTROLLED_VOCABULARY.md`](../../../repo/CONTROLLED_VOCABULARY.md)
or be plain descriptive prose. Coining a tier or class word ("review-gated",
"established", a campaign name) is a blocking defect even when the concept is
real — say the process fact instead ("landed through review, not yet
audited").

## 5. Links

Every markdown link in your diff dereferences to one git-tracked regular
file (the invariants harness enforces this on authority surfaces:
`directory-target`, `not-tracked`, `absolute-path`, `outside-repository`
are all violations). Load-bearing dependencies are markdown links — backticks
seed no citation-graph edges; decorative references are backticks — links
seed edges you must intend.

## 6. Graph topology

Run the pipeline. If the citation-graph delta gate (stage 18 vs the tracked
manifest, stage 1b) names nodes or edges your change adds, removes, or
rewires: confirm each is intended, then acknowledge by staging the refreshed
`docs/audit/data/citation_graph_manifest.json`. Generated status surfaces and
class-F orientation memos under `docs/repo/` must contribute no edges at all
(they are excluded in `build_citation_graph.py`; extend the exclusion when
you add such a surface).

## 7. Generated-but-tracked files

If your change ships a tracked generated file (initial materialization or a
renderer change), regenerate it from the TRACKED input state as the last step
before committing — never from post-seed local pipeline state, which can
embed status changes your tree's shards do not carry. Register nightly
ownership (`codex_audit_runner.AUDIT_DATA_FILES`) and the graph exclusion
where applicable.

## 8. Runners

Every new or changed runner check is mutation-checked: one load-bearing
mutation per check family (on a scratch copy or reverted immediately), and
the check must fail. A check that asserts the formula it is supposed to test
confirms nothing. Record the mutations you ran in the PR body.

## 9. Clean-state validation

From a worktree with no untracked pipeline residue (`git clean` generated
caches first): `python3 scripts/vocab_lint.py --fix` on changed files; full
`bash docs/audit/scripts/run_pipeline.sh` exit 0; `python3
docs/audit/scripts/audit_lint.py --strict` with no NEW errors. Then restore
generated outputs, stage explicit paths only, and confirm `git status` shows
exactly your intended files.

## 10. Read your own diff as the reviewer

Read the complete diff once, cold, before requesting review — not the files,
the diff. Every hunk you cannot justify in one sentence from a source you
just read is a hunk the reviewer will bounce.

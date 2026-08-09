# Review-loop PR conformance spec

**Authority and use.** The requirements below were distilled from the 2026-08
review-loop drain, over its first nineteen landed reviews. They are banked in-repo by
owner directive (2026-08-09) so that PRs are authored to the spec rather than corrected
against it across review cycles. The `physics-loop` skill should treat this document as
a **generation-time checklist**: a PR is not ready to request review until every MUST
below is satisfied. (Wiring the checklist into
`docs/ai_methodology/skills/physics-loop/SKILL.md` is a follow-up; it is not part of
the PR that banks this document.)

Every review-loop PR must meet this spec BEFORE requesting review. It is distilled
from the first nineteen landed reviews of the 2026-08 drain, in which zero PRs
passed clean and the same defect families consumed most fix iterations. Items are
MUST unless marked otherwise. Exemplars: PRs #6015, #5921, #5925, #5930, #5979
(iterations), #5931 (salvage).

## 1. Self-containment (the top rejection driver)

- `AUDIT_INPUT_PATHS` (and any equivalent closure) may pin ONLY files that exist
  on `origin/main`, at their landed-on-main blobs, verified via
  `git cat-file` — or be empty.
- No pins of unlanded ancestor artifacts, no pins of rejected-branch artifacts,
  no "vendored anchors" carrying rejected-run receipts. If an ancestor claim has
  not landed, it is an UNAVAILABLE premise: either re-establish the result inside
  this PR's own computation or do not use it.
- No hard requirement on gitignored artifacts (e.g. symlinked
  `docs/audit/data/audit_ledger.json`). Runners must be fresh-worktree
  reproducible: clone at `origin/main`, apply the delta, run.
- Stacked PRs: the delta may cite the base branch's content only if that content
  has landed by the time this PR is reviewed; otherwise the same rules apply.

## 2. Cache and execution discipline

- Every cached runner output goes through
  `scripts/runner_cache.py` `execute_and_write_cache(runner, timeout_sec)`.
  Raw stdout files are not caches.
- NO hand-added metadata in runner-emitted files (caches, receipts). Review
  records live in the note, not in machine-emitted artifacts.
- Exit-code honesty: a nonzero exit that is by design is recorded as
  `nonzero_exit` with the design reason stated in the note; never rewrap or
  launder it into `ok`.
- After ANY edit to a pinned file, rerun the affected runners through the
  envelope and re-pin (checker pins of primary sha/blob, receipt pins of final
  bytes). A pin against pre-edit bytes is a defect.

## 3. Claim-scope honesty

- State exactly what the runner computed: finite domain, declared parameters,
  bounded scope. Words that claim more than the computation —
  "certified", "closed", "complete", "global", "maximal", "the law" — are
  demotion targets unless the computation actually establishes them.
- Full-surface consistency: the claim scope must match on EVERY surface —
  note prose, title/headline, runner docstrings, emitted certificate strings,
  machine-status block, receipts, closing verdict line. Demoting the note while
  a docstring still overclaims is a confirmation failure (seen twice).
- Domain-explicit naming; no `near/far`-style frame-relative names where a fixed
  designation exists. No campaign/block/lane-opening language in scientific
  headlines. No unregistered labels or block/campaign fields in machine records.

## 4. Negative claims: the N-gate

A PR shipping any no-go / impossibility / "X is refuted" claim MUST carry:
- N1: every candidate route marked exactly `ATTEMPTED` or `RULED OUT BY PRIOR`
  (with the prior pinned), else the claim takes an honest NOT-PASS disposition.
- N2: the full pairwise independence table of the walls, WITH collapse applied —
  dependent walls collapse and the headline claim uses the collapsed set.
- N4: a per-citation table: path:line, witness residual, claimed residual,
  match y/n.
- N5: the five mandatory resolution lines present in the cached stdout.
Withdrawing the negative claim to a bounded positive observation removes the
N-gate obligation — but then NO residual sentence may still function as a no-go.

## 5. Packet completeness (audit reachability)

- Every runner whose output the note's claims rely on must be inside the claim's
  restricted audit packet: either imported by the primary runner or declared as
  `packet_helper_runner:` in the note's machine-status block.
- A declared helper additionally requires the verbatim registry entry for
  `EXPLICIT_PACKET_HELPER_RUNNER_PATHS` in
  `docs/audit/scripts/build_citation_graph.py`, supplied in the PR description
  for application AT LANDING (never edited on the PR branch).
- Verification: on a disposable tree at `origin/main` + this delta + the registry
  entry, `python3 docs/audit/scripts/check_changed_audit_evidence.py --base
  origin/main --json` must show the row forensic-ready with all load-bearing
  runners in `changed_surfaces` and `helper_runner_paths` populated.

## 6. Generated artifacts and landing hygiene

- `docs/audit/data/citation_graph_manifest.json` is regenerated on the landed
  tree at landing time (`docs/audit/scripts/build_citation_graph.py` +
  `docs/audit/scripts/write_citation_graph_manifest.py`);
  branch-side manifest edits are superseded and should not be shipped.
- Append-only queue files (`docs/repo/ACTIVE_REVIEW_QUEUE.md`,
  `docs/CANONICAL_HARNESS_INDEX.md`) must be written so append/append
  union-resolution at landing is trivial.
- Receipts live in `outputs/`, caches in `logs/runner-cache/`; nothing else
  writes outside the delta's declared file set. Never stage with `git add -A`.

## 7. Note structure

- Machine-status block: complete and consistent with the receipts (claim id,
  surface_status, packet_helper_runner where applicable, target_claim_id for
  support notes with the relation typed, e.g. `upstream_support`).
- Imports section: every underivable input typed
  (e.g. `unverified_imported_comparator_convention`), with provenance stated or
  declared absent; open bridges declared OPEN and owned by the correct lane.
- A Review record section when the PR replaces or narrows earlier content:
  what was dropped/refuted, where the retained scope ends.

## 8. Lint gates (run before requesting review)

- `python3 scripts/vocab_lint.py --report-only <delta files>`: zero findings on
  the delta files.
- `git diff --check`: clean.
- `python3 -m py_compile` on every added/modified script.
- Prep sanity for stacked PRs: the reviewed delta must equal
  `merge-base(base-branch, head)..head`, and its file count must match an
  independently computed delta before any reviewer is launched.

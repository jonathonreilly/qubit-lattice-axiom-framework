# axiom-reconciliation — resume notes (2026-07-12)

## Where things stand

- Worktree `/Users/jonBridger/tp-axiom-recon`, branch
  `repair/axiom-recon-block03-index-20260712`, based on `origin/main`
  @ `7b9260b85`.
- The fresh index is REGENERABLE: run
  `python3 scripts/axiom_reconciliation_rescan_2026_07_12.py`
  (writes `logs/runner-cache/axiom_reconciliation_rescan_2026_07_12.tsv`
  and prints the summary; TOTAL: HARD=141 SOFT_ONLY=740
  RETAINED_STATUS_HARD=8 at the base commit).
- Triage: 30 codex batches classify the 141 hard files. Batch specs and
  full logs live in the session scratchpad
  (`recon_batches/*_spec.md`, `*_full.log`); the DELIVERABLES are the
  committed TSVs at `logs/runner-cache/recon_triage/<batch>.tsv`
  (one row per file: path, class, confidence, evidence lines, quote,
  rationale, paired file, proposed fix).
- If triage was interrupted: missing batches = specs without a matching
  TSV. Relaunch only those through the codex recipe (workhorse skill;
  `< /dev/null`, `-o` lastmsg, prompt as argument).

## Classification rubric (frozen for this campaign)

REKEY (mechanical quote/needle/citation refresh; argument survives) /
CONTENT-FLIP (load-bearing premise or verdict uses deleted or changed
axiom content; needs refutation-seat re-derivation) / REOPENED-WALL
(no-go whose blocking premise was old wording; wall may reopen) /
HISTORICAL-OK (marked historical context only) / DELIBERATE-OLD-TEXT
(runner references old wording by design, e.g. flip demos or absence
guards). Severity tie-break: flip/wall > rekey > historical.

## Standing rules

- Supervisor line-reviews every worker row before any edit lands; every
  wave PR runs the affected runners + `vocab_lint` before commit.
- The 8 hard files with retained audit status are an
  invalidation-pipeline gap: FLAG to the audit lane in the index note /
  PR body. Never edit the ledger or statuses from this lane.
- Landing is Jon's review lane. PRs stack; Block 3 (index) is the base.

# PR #5995 Salvage Confirmation Findings — Iteration 4

Confirmation scope: commit
`8d400d36126fa1f52a1f82aa793ded3df3baafca` and exactly the seven files in
`RL_FIXDIFF3_PR5995.txt`. This round judges only the iteration-3 S2 and S4
failures. No package file was edited.

The review-loop skill was refreshed from `origin/main` at
`8abc3986dd503ab5932844619272ff96533a370d`; that copy is newer than the
installed copy and governs this confirmation. The applicable focused lenses
are CodeRunnerReviewer, RepoGovernanceReviewer, and
AuditCompatibilityReviewer.

## S2 — NOT_FIXED

The governed-source repair itself is correct:

- `docs/audit/scripts/build_citation_graph.py` is byte-identical to the
  review merge-base copy at
  `c73a11d1ea7ddd564c48aa2a5a459a43d94262ef` (the file has Git blob
  `ce6480819c794f44dd15c758045dea490da0cd45` in both trees).
- Its SHA-256 is
  `e09dbee45c074c5f62f0133fa1261bee95b8671adae9147584febb3b658a541e`,
  exactly the value recorded for that path in
  `docs/audit/data/dependency_policy_epoch.json`.
- `python3 docs/audit/scripts/audit_lint.py --strict` exits 0 and ends with
  `OK: no errors` after checking 3972 rows. Its pre-existing warnings and
  notices do not include a strict error.
- The helper registration is absent from the live registry, as intended for
  this deferred policy repair. Under the note's `## Review record`, the
  `### Hard landing condition: packet-helper registration` section states
  that it must be applied before or at landing and contains the exact removed
  registration entry. A byte comparison, including the four comment lines,
  matches the iteration-2 registry entry; both extracted blocks hash to
  `f74b08ea30f7895cd77d17a3a5b679d6c07ecc580063a69b7d26f1c4ac7d616f`.
- The dated ID
  `2026-08-08-dependency-policy-epoch-debt-helper-registry` is present in
  `docs/repo/ACTIVE_REVIEW_QUEUE.md`, and its finding records the independently
  measured 891 hard resets with both invalidation reasons.

The queue entry nevertheless fails the queue's own mandatory intake format.
`ACTIVE_REVIEW_QUEUE.md` requires `Disposition` to be one of `triage`,
`fix on main`, `support-only demotion`, `science-needed`, or `reject`. The new
entry instead uses:

> `Disposition: needs a dedicated owner-approved policy pass reconciling ...`

That prose may follow a canonical disposition token as an explanation, but it
cannot replace the token. Because the user explicitly required the dated item
to pass the queue-format check, S2 is not fully fixed.

## S4 — FIXED

- Case-insensitive grep for `REVIEW_LOOP`, `PRIMARY_REVIEW_LOOP`,
  `review_loop`, and the prior `RL_SALVAGE_FINDINGS_PR5995.md` reference
  returns zero hits across both runners and both receipts.
- Both receipt top levels now contain only runner-generated keys:
  `checks`, `date`, `expected_check_count`, `fail`, `inputs`, `pass`,
  `payload_sha256`, `role`, `script`, `units`, and `verdict`.
- Review provenance is carried in the note's `### Fix history` section, which
  records both the iteration-2 repairs and the iteration-3 removal of review
  metadata from runner-emitted receipts.
- In an isolated `git archive HEAD`, the primary exits 0 with
  `TOTAL: PASS=31 FAIL=0`; the checker exits 0 with
  `TOTAL: PASS=27 FAIL=0`.
- Both first-run receipts are byte-identical to the committed receipts. A
  second complete run reproduces both receipts byte-for-byte again. The
  regenerated file SHA-256 values are
  `13011f85315f5e80d6db620419f0ea9acf374d56129f6082fafeedbe6cc1bc13`
  (primary) and
  `c079eaa261e90c4e84fdd25ba221b57270ea17dcb2d2fb303b1ddd73974fca55`
  (checker).
- An external rehashed semantic tamper of the primary receipt still makes the
  checker exit 1: the self-digest gate passes, the wholesale canonical-payload
  comparison fails, and the checker reports `TOTAL: PASS=25 FAIL=2`.

## Focused disposition

- S2: `NOT_FIXED` — governed bytes, epoch hash, strict lint, hard landing
  condition, verbatim helper entry, and 891-reset disclosure pass; the required
  active-queue item does not use a permitted `Disposition` value.
- S4: `FIXED` — runner/receipt review metadata is gone, provenance is in the
  note, receipts are deterministic, and the fail-closed tamper test holds.
- `git diff --check` on the seven-file iteration-3 fix is clean, and the
  tracked worktree remained unchanged throughout this confirmation.

CONFIRMATION: FAIL — S2's active-queue item does not use a permitted Disposition value

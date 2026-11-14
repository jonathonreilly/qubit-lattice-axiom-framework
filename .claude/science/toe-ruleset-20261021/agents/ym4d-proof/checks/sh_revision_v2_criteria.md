# SOFTHARD binding-fix documentation checks, v2

[R-fix 2026-10-29 B4] Criteria recorded before the new checker is written.
Prior exposure: REVIEW_SOFTHARD B1–B4, the original memo and frozen receipts,
the named current source statements, and Dimock II pages 28, 29 and 31 have
been read. This is documentation verification, not an independent proof check.

1. Preserve the original 2,035-byte prefix and every original nonempty memo
   line, allowing only a Markdown blockquote prefix on superseded lines.
   Preserve the original log as a byte prefix. Every revision block identifies
   its binding fix. No frozen source, script, receipt or output is overwritten.
2. Record current input hashes and stat data before edits. Compare all files
   in the working folder with that snapshot; allow only SOFTHARD.md,
   SOFTHARD_LOG.md and new checks/sh_*_v2* files. Compare tracked changes with
   the initial clean tracked state. A changed dependency during this task is
   an error requiring refreshed inspection, not a historical-drift waiver.
3. Recheck all 34 frozen quotation fragments against the current source and
   memo. Try the original bounded line range first; if lines shifted, record
   the exact current matching range. Normalize Unicode compatibility glyphs,
   whitespace, Markdown emphasis/backticks and PDF line-wrap hyphenation only.
   Do not treat an unavailable PDF as a successful check. Report that residue.
4. Compare the 21 required source hashes, the 210 inventoried hashes and saved
   artifact hashes to their frozen receipts. Record pre-existing differences
   separately from changes made in this revision. Resolve moved PDFs by
   identical SHA-256, retaining their old paths in the historical receipts.
   No semantic correctness or current review coverage follows from a hash.
5. Check local Markdown paths, corrected Dimock II section/page/equation
   locators against the actual PDF, and B1's explicit finite registry
   crosswalk. Presence is only structural coverage, never proof completeness.
6. Run the new checker once, sequentially, with BLAS/OpenMP/NumExpr/Accelerate
   threads set to 1, Python bytecode disabled and no pools. Record peak RSS
   using platform-correct units; stop/fail at 2,000,000,000 bytes. Record any
   sandbox refusal or unavailable input literally. Do not manufacture PASS.
7. Save detailed results in checks/sh_revision_v2_results.json. Do not modify
   the frozen sh_quote_check.json, sh_validation.json or other old receipts.
   Log each file edit with post-edit stat, byte size and SHA-256; log appends
   record their pre-append stat to avoid a self-referential post-write hash.

Acceptance: B1/B2/B3 require author inspection of the actual text and named
sources. B3 is satisfied by a precise OPEN statement, not by a proof of it.
B4's locator repair and available-input checks can be recorded separately;
any unavailable quote/hash verification remains explicit open residue.

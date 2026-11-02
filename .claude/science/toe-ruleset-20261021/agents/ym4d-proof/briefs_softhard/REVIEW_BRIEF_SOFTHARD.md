# Reviewer brief: hostile review of SOFTHARD.md (soft vs hard blocking)

You wrote none of this, so assume it contains errors. The author's brief is in briefs_softhard/AUTHOR_BRIEF_SOFTHARD.md.

**Read:**
- SOFTHARD.md
- SOFTHARD_LOG.md
- checks/sh_*
- every file and paper it cites, including the open arXiv papers under ARXIV_DIR

Use grep -n and offsets on large files.

**Check:**
1. **Provenance.** The PRE-STATED section must be the first edit and must contain statements only.
2. **Each ledger entry.**
   - Is the quote exact?
   - Is the obstruction really caused by the kernel being soft? An obstruction that hard blocking would also face does not belong in the soft-cost ledger.
   - Is the hard-route replacement correctly sourced from open literature, with the right scope? Separate 4D non-abelian from scalar or QED results. Anything cited from memory [m] must not be load-bearing.
3. **Missing entries.** Look for costs or gains the author left out. In particular, check whether the "results lost if we switch" list is complete, using PROOF.md and the Codex-confirmed items in HANDOFF.md.
4. **The hybrid analyses.**
5. **The verdict.** Does it follow from the two ledgers? Is the decisive question stated precisely? Is it framed as a recommendation to the owner, not a decision?
6. **Re-run any check,** under the same resource rules:
   - nice
   - BLAS=1
   - under 2 GB RSS
   - at least 50% memory free
   - no pools

**Write REVIEW_SOFTHARD.md** containing:
- per-item verdicts, each with a line reference and a fix
- binding fixes
- a final line that is exactly `VERDICT: LAND` or `VERDICT: HOLD`

Edit no other file. No commits. Final message under 300 words.

## Owner directive (added 2026-10-29 17:30 UTC, after launch)
"if we need their proofs or lemmas just rebuild them and put them in the repo / PR / library. why keep referencing papers."
- Literature results are never load-bearing citations. Price each hard-route requirement as the cost of
  rebuilding it as a self-contained proof on our structures.
- Add a section **"Library rebuild list"**: the specific lemmas from the open expositions (Dimock and others)
  that either route needs. For each, give its statement, a size and difficulty estimate, and whether the open
  text contains a complete proof we can rebuild.
- Credit the original authors by name in each entry.

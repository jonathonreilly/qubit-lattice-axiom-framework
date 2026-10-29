# Reviewer brief: hostile review of RD.md (returned denominator)

You did not write this work. Assume it contains errors. The author brief is briefs_rd/AUTHOR_BRIEF_RD.md.

**Read:**
- RD.md, RD_LOG.md, and checks/rd_* if present.
- The consumer files: STEP55, CX, CODEX_REVIEW_STEP R11 and item 6, SOFTHARD C2, LIB1 and its reviews, RECOVERY_CLUSTER_ASTRA and its review.

**Check:**
1. **The denominator.** Is it the ACTUAL returned denominator that CX/STEP55 consume, not a simplified surrogate?
2. **The representation, line by line:**
   - the prefactors are nonzero and bounded;
   - analyticity holds on the stated domain;
   - the bound on the activities is uniform in history, holes, scale and volume;
   - the reference comparison is correct;
   - failed returns are handled.
3. **Inputs.** Are the inputs from active coordinator lanes named exactly, and not silently assumed? Is anything consumed as landed actually landed at that scope?
4. **Hidden imports.** Is any load-bearing step an [m] (unverified) or literature step?
5. **Consumer match.** Does the result match what CX needs, word for word?

**Write** REVIEW_RD.md containing:
- per-item verdicts, each with the line and the fix;
- the binding fixes;
- a final line that is exactly `VERDICT: LAND` or `VERDICT: HOLD`.

Edit no other file. No commits. Final message under 300 words.

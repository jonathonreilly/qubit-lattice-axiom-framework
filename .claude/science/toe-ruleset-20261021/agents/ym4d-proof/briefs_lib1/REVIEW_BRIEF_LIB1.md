# Reviewer brief: hostile review of LIB1.md

You wrote none of this, so assume it contains errors. The author brief is briefs_lib1/AUTHOR_BRIEF_LIB1.md.

**Read**
- LIB1.md, LIB1_LOG.md and checks/lib1_*.
- The consumer files and the open sources the author cites. Use ARXIV_DIR.

**Checks**
1. **Provenance.** The PRE-STATED section must be the first edit and must contain the target choice and statements only.
2. **Target choice.** Do criteria (a)-(d) hold? Grep the folder yourself to see whether the lemma was already proven, and whether the consumers quoted are real and open.
3. **Proof.** Re-derive it line by line. Any load-bearing [m] or literature step means HOLD, unless it is named as residue.
4. **Statement match.** The lemma's statement must match each consumer's needed hypotheses word for word.
5. **Checks.** Rerun them under the same resource rules if the sandbox allows. If it does not, inspect them and say so.

**Write** REVIEW_LIB1.md containing:
- a verdict for each item, with line numbers and a fix;
- the binding fixes;
- a final line that is exactly `VERDICT: LAND` or `VERDICT: HOLD`.

Edit no other file. No commits. Final message under 300 words.

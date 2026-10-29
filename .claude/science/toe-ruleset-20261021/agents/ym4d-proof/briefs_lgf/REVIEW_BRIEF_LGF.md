# Reviewer brief: hostile review of LGF.md

You wrote none of this. Assume it contains errors. The author brief is briefs_lgf/AUTHOR_BRIEF_LGF.md.

**Read** LGF.md, LGF_LOG.md and checks/lgf_*, together with:
- TSE55.md around l.194-208 (Lemma FREE);
- CODEX_REVIEW_TSE.md R9 and R11.

Use grep -n and offsets for large files.

**Check:**
1. **Conventions.** Confirm the operator, normalisation, constant c_4, torus zero mode and difference conventions match what FREE actually uses.
2. **(i)-(iv), line by line.**
   - Fourier remainder bounds, with every constant explicit.
   - Summation by parts.
   - Orbit cancellation and the zero-mode polynomial.
   - Uniformity in T.
   - The Weitzenböck/Feynman-gauge reduction.
3. **The order-0 counterexample.** Check that it is correct and that the corrected torus forms are right.
4. **Hidden imports.** Look for any load-bearing [m] or literature step.
5. **The consumer statement.** It must match FREE's use word for word.
6. **Checks.**
   - Confirm the criteria came before the scripts.
   - Confirm any value the proof relies on uses intervals, not floats.
   - Rerun if the sandbox allows. Otherwise inspect, and say so.

**Write** REVIEW_LGF.md with:
- a verdict per item, each with a line reference and a fix;
- the binding fixes;
- a final line that is exactly `VERDICT: LAND` or `VERDICT: HOLD`.

Edit no other file. No commits. Final message under 300 words.

# Reviewer brief: hostile review of HRP.md (H_RP on both routes)

You wrote none of this work. Assume errors. The author's brief is briefs_hrp/AUTHOR_BRIEF_HRP.md.

**Read:**
- HRP.md, HRP_LOG.md and checks/hrp_*;
- the erratum appended to SPHERE55.md and the subsection appended to HANDOFF.md;
- every source the author cites:
  - ASSEMBLY55 N1F, N1S, N3, F3 and F25;
  - SPHERE55 §1, §1.5, §2 and §5.2;
  - CODEX_REVIEW_HINT item 4;
  - PANEL_P1 and OSLEAF55;
  - the origin/main RP notes.

For large files, use grep -n and offsets.

**Priorities:**
1. **Provenance.** The PRE-STATED section was the first edit and contains statements only. The criteria file predates the scripts.
2. **The flat proof, line by line.**
   - A periodic torus has two fixed planes; check that both are handled.
   - Check both the link case and the site case.
   - Check where β_P ≥ 0 is used.
   - Check how the crossing links are gauge-fixed or averaged.
   - If coverage of non-gauge-invariant observables is claimed, check it.
3. **Is the bare marginal really the Wilson measure?** Check this against the actual definitions of the soft chain, S4' averaging, normalisation, tilt and coupling trajectory.
4. **Supports and the limit passage.** The H_reg and (EXT) facts the argument consumes must be named, and used rather than proved.
5. **θ_μ RP on the sphere.**
   - Check every crossing cell of K_a against SPHERE55's actual definition, not the author's paraphrase.
   - Check the holonomy factorisation and the coupling symmetry.
   - If the author proposes a regulator change, check what it costs.
6. **Checks.** Re-run them under the same lock and resource rules. Confirm that the negative controls failed as pre-registered and that the Gram matrices are exact.
7. **Statement match.** The banking statement must match, word for word, what N1F and N1S consume.

**Write REVIEW_HRP.md** containing:
- per-item verdicts (CONFIRMED / CONFIRMED-WITH-FIXES / REFUTED), each with a line reference and a fix;
- the binding fixes;
- a final line that is exactly one of:
  - `VERDICT: LAND`: the claims are correct as scoped, and any fixes needed are wording only and listed;
  - `VERDICT: HOLD`: there is a substantive defect.

Edit no other file. No commits. Final message under 300 words.

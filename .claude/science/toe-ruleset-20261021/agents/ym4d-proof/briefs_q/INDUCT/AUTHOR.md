# Sprint lane INDUCT: from one RG step to all scales
Take REFMATCH §6's conditional one-step theorem and write the full multi-scale induction:
- the inductive hypothesis at level j;
- how the output at level j satisfies the input at level j+1;
- the coupling trajectory, with bare coupling g_0(a) chosen causally;
- the constants' windows, with an explicit check that they are mutually satisfiable over all levels. Do not hide a level-dependent constant.

Give bounds uniform in the number of levels K and the volume. Say how persistent flux (RENEW, CHARGE) and growing or merging holes (LIB1, HOLEPAY if present) enter across levels.

Then produce the end output: real-derivative bounds on the effective action at a fixed physical scale.

Read REFMATCH.md, REALRGA.md, EXTCONT.md, LOCOP.md, SPURION.md, FLOW.md, CHARGE.md, RENEW.md and LIB1.md.

## Sprint rules
This is the owner's end-to-end sprint: reach the end point of the proof first and check the whole thing afterwards. There is no per-lane review. Speed matters, but honesty about status matters more.

**Label every step with exactly one of these:**
- **PROVEN(file):** already landed, at that file's reviewed scope. Quote the exact statement you use. Do not widen its scope.
- **DRAFTED(conf):** you wrote a real argument, but nobody has checked it. Give your honest confidence (high, medium or low) and the single most likely failure point.
- **GAP:** you do not have an argument. State exactly what would be needed and why the obvious approach fails.

**Never write plausible text in place of an argument.** A GAP is a useful result. A fabricated step is the worst possible outcome, because a later reader cannot tell it from a real one. Do not invent constants. If a constant is not computed, write it as a named symbol with the inequality it must satisfy.

**Track interfaces explicitly.** For each step, state what it consumes and what it produces, in exact form, so that the end-to-end check can compare them mechanically. Constant windows must be stated and checked for mutual consistency.

**Do not stop at the first failure.** Mark it and continue to the end, conditional on a stated assumption.

Create and edit only INDUCT.md. No commits, no audit or ledger files, no axiom edits. No numerics unless they are essential, and then under 1 GB and BLAS=1. Final message under 250 words: the counts of PROVEN, DRAFTED and GAP, plus the three weakest links.

# Sprint lane NGYM: the Yang–Mills side of non-freeness, end to end
Assume, as named inputs, the uniform bounds from INDUCT. Write the actual YM estimates for the combined witness (COMBO):
- AF-e (E-ALG, E-SEQ, E-TR, E-TS, with PL-1L);
- the fourth cumulant κ4 lower matching (K4MATCH, K4CORR, K4CORR2);
- the shared renormalisation and matching inputs, written as one estimate if possible.

Say what exactly the limiting state has that a Gaussian or Wick-composite state cannot. Include clustering for mixtures (MIXGFF) if it is obtainable.

Read COMBO.md, WITNESS.md, CUMUL.md, K4MATCH.md, K4CORR.md, K4CORR2.md, MIXGFF.md, LGF.md, TSE55.md, F17.md and FLOW.md.

## Sprint rules
This is the owner's end-to-end sprint: reach the end point of the proof first and check the whole thing afterwards. There is no per-lane review. Speed matters, but honesty about status matters more.

**Label every step with exactly one of these:**
- **PROVEN(file):** already landed, at that file's reviewed scope. Quote the exact statement you use. Do not widen its scope.
- **DRAFTED(conf):** you wrote a real argument, but nobody has checked it. Give your honest confidence (high, medium or low) and the single most likely failure point.
- **GAP:** you do not have an argument. State exactly what would be needed and why the obvious approach fails.

**Never write plausible text in place of an argument.** A GAP is a useful result. A fabricated step is the worst possible outcome, because a later reader cannot tell it from a real one. Do not invent constants. If a constant is not computed, write it as a named symbol with the inequality it must satisfy.

**Track interfaces explicitly.** For each step, state what it consumes and what it produces, in exact form, so that the end-to-end check can compare them mechanically. Constant windows must be stated and checked for mutual consistency.

**Do not stop at the first failure.** Mark it and continue to the end, conditional on a stated assumption.

Create and edit only NGYM.md. No commits, no audit or ledger files, no axiom edits. No numerics unless they are essential, and then under 1 GB and BLAS=1. Final message under 250 words: the counts of PROVEN, DRAFTED and GAP, plus the three weakest links.

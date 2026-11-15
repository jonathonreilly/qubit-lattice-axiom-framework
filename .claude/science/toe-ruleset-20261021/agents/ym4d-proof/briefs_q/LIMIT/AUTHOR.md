# Sprint lane LIMIT: from uniform bounds to the OS axioms in the limit
Assume, as a named input, the real-derivative bounds that INDUCT outputs at fixed physical scale. Write these steps:
- **Bounds to moments:** from those bounds to uniform separated moments and E0′ for the e field. Give all-n constants of the same form, as REC_CONT needs (REALONLY R8/R9).
- **Limits:** the thermodynamic and continuum limits along a common subsequence.
- **OS1 (Euclidean invariance):** work through **both** the flat route (TQ, TQ2 pressure reduction) and the sphere route (N5B); do not choose one in advance.
- **OS2:** from HRP.
- **OS3.**
- **Reconstruction:** apply REC_LIB and REC_CONT.

Say exactly which step could produce a limit that is trivial, and how the witness rules that out.

Read REALONLY.md, OSLEAF55.md, HRP.md, REC_LIB.md, REC_CONT.md, TQ.md, TQ2.md, N5B.md, REVIEW_N5B.md, ROTDEF.md, SRCCD55.md and ASSEMBLY55.md.

## Sprint rules
This is the owner's end-to-end sprint: reach the end point of the proof first and check the whole thing afterwards. There is no per-lane review. Speed matters, but honesty about status matters more.

**Label every step with exactly one of these:**
- **PROVEN(file):** already landed, at that file's reviewed scope. Quote the exact statement you use. Do not widen its scope.
- **DRAFTED(conf):** you wrote a real argument, but nobody has checked it. Give your honest confidence (high, medium or low) and the single most likely failure point.
- **GAP:** you do not have an argument. State exactly what would be needed and why the obvious approach fails.

**Never write plausible text in place of an argument.** A GAP is a useful result. A fabricated step is the worst possible outcome, because a later reader cannot tell it from a real one. Do not invent constants. If a constant is not computed, write it as a named symbol with the inequality it must satisfy.

**Track interfaces explicitly.** For each step, state what it consumes and what it produces, in exact form, so that the end-to-end check can compare them mechanically. Constant windows must be stated and checked for mutual consistency.

**Do not stop at the first failure.** Mark it and continue to the end, conditional on a stated assumption.

Create and edit only LIMIT.md. No commits, no audit or ledger files, no axiom edits. No numerics unless they are essential, and then under 1 GB and BLAS=1. Final message under 250 words: the counts of PROVEN, DRAFTED and GAP, plus the three weakest links.

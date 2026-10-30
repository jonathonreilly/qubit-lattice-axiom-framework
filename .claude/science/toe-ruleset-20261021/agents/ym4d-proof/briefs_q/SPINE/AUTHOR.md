# Sprint lane SPINE: the whole proof of T_OS, end to end
Write the complete chain from the lattice model to the final theorem, as one document:
1. **Model:** the finite periodic SU(N) Wilson model and the soft-kernel chain (decision 4).
2. **One RG step:** REFMATCH's conditional theorem.
3. **All scales:** the induction over all scales, and the coupling trajectory.
4. **Uniform bounds:** bounds on the actual field variables, uniform in cutoff and volume.
5. **Moments:** separated moments, which give E0′ (REALONLY, SRCREAL).
6. **Limit:** a common subsequence and the limit.
7. **OS axioms:** OS0–OS3 on the common algebra, with RP from HRP. Choose a geometry and record how the other one differs.
8. **Reconstruction:** REC_LIB and REC_CONT.
9. **Non-freeness:** the witness (AF-e and κ4, COMBO), including the actual YM estimates.
10. **Final theorem:** the statement, in the strongest form this chain supports.

Probe to the end: if a step fails, mark it and continue conditionally.

The output is **the skeleton and interface table** everyone can check:
- one row per step, with consumes, produces, label and constants;
- a mutual-consistency check of all constant windows and of all quantifier orders;
- a ranked list of the weakest links.

Do not attempt the mass gap here; state only where it would attach.

Read: AUDIT.md, QUEUE_STATUS.md, REFMATCH.md, REALRGA.md, REALONLY.md, EXTCONT.md, LOCOP.md, COMBO.md, HRP.md, REC_LIB.md, REC_CONT.md, ASSEMBLY55.md, CODEX_REVIEW_ASSEMBLY.md and FLOW.md (latest sections).

## Sprint rules
This is the owner's end-to-end sprint: reach the end point of the proof first and check the whole thing afterwards. There is no per-lane review. Speed matters, but honesty about status matters more.

**Label every step with exactly one of these:**
- **PROVEN(file):** already landed, at that file's reviewed scope. Quote the exact statement you use. Do not widen its scope.
- **DRAFTED(conf):** you wrote a real argument, but nobody has checked it. Give your honest confidence (high, medium or low) and the single most likely failure point.
- **GAP:** you do not have an argument. State exactly what would be needed and why the obvious approach fails.

**Never write plausible text in place of an argument.** A GAP is a useful result. A fabricated step is the worst possible outcome, because a later reader cannot tell it from a real one. Do not invent constants. If a constant is not computed, write it as a named symbol with the inequality it must satisfy.

**Track interfaces explicitly.** For each step, state what it consumes and what it produces, in exact form, so that the end-to-end check can compare them mechanically. Constant windows must be stated and checked for mutual consistency.

**Do not stop at the first failure.** Mark it and continue to the end, conditional on a stated assumption.

Create and edit only SPINE.md. No commits, no audit or ledger files, no axiom edits. No numerics unless they are essential, and then under 1 GB and BLAS=1. Final message under 250 words: the counts of PROVEN, DRAFTED and GAP, plus the three weakest links.

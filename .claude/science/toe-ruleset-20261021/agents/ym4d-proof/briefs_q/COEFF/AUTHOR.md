# Lane COEFF: uniform coefficient recursions on the asymptotic-freedom trajectory
**Why.** LOCOP.md proves the exact conditional recursion L13 and the AF bracket L15–L16. SPURION.md proves that no gluon-mass counterterm is needed and classifies the surviving relative-field terms as recorded coefficients. OPEN (LOCOP LC4–LC6, EXTCONT COEFF/E19): uniform actual-model antecedents, causal tuning of the bare trajectory, and budgets for the other coefficients.

**Target.**
1. Write the full coefficient system: the coupling, vacuum, source-normalization and recorded relative-field coefficients.
2. Prove that the recursions are stable along the AF trajectory, given the remainder bounds of the real contract.
3. Construct the causal bare-coupling tuning: the choice of g_0(a) so that the coarse coupling hits its target, uniformly in cutoff and volume. Use FLOW's landed T-tel, FP-exact, Cartan and SLICE-U results at their reviewed scope.

State exactly which remainder input each step consumes. Give the exact failing inequality if one fails.

**Deliverable: COEFF.md.** Read LOCOP.md, SPURION.md, EXTCONT.md, REALRGA.md, the latest sections of FLOW.md and its reviews.

## Sprint rules
This is the owner's end-to-end sprint: reach the end point of the proof first and check the whole thing afterwards. There is no per-lane review. Speed matters, but honesty about status matters more.

**Label every step with exactly one of these:**
- **PROVEN(file):** already landed, at that file's reviewed scope. Quote the exact statement you use. Do not widen its scope.
- **DRAFTED(conf):** you wrote a real argument, but nobody has checked it. Give your honest confidence (high, medium or low) and the single most likely failure point.
- **GAP:** you do not have an argument. State exactly what would be needed and why the obvious approach fails.

**Never write plausible text in place of an argument.** A GAP is a useful result. A fabricated step is the worst possible outcome, because a later reader cannot tell it from a real one. Do not invent constants. If a constant is not computed, write it as a named symbol with the inequality it must satisfy.

**Track interfaces explicitly.** For each step, state what it consumes and what it produces, in exact form, so that the end-to-end check can compare them mechanically. Constant windows must be stated and checked for mutual consistency.

**Do not stop at the first failure.** Mark it and continue to the end, conditional on a stated assumption.

Create and edit only COEFF.md. No commits, no audit or ledger files, no axiom edits. No numerics unless they are essential, and then under 1 GB and BLAS=1. Final message under 250 words: the counts of PROVEN, DRAFTED and GAP, plus the three weakest links.

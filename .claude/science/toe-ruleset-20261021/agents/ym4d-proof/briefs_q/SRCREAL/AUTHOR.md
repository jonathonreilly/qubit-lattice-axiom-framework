# Lane SRCREAL: the all-order source hierarchy in real form (AUDIT priority 3, on all 10 routes)
**Why.** AUDIT interface S is the actual all-order source/seed estimates, including all-coarse source radii, mixed products and insertion growth. It blocks every route. REALONLY proves the consumers need only real estimates: E0′ via separated moments (R8) or outer-cumulant bounds (R9). The coordinator's active lane works on a *fixed source radius* in the complex setting, so do not duplicate that lane. This lane is the real-tilt alternative.

**Target.** Derive E0′ on the separated e hierarchy, |S_n(F)| ≤ α(n!)^β|F|_{sn}, from a real-tilt moment generating bound. The tilt bound should have the form sup_{|t|≤t_0} E[exp(t·e(f))] ≤ exp(C‖f‖²...), uniform in cutoff and volume, conditional on the REALRGA contract's outputs. Then:
- state exactly which RG output feeds the tilt bound;
- handle products and insertion growth;
- check that the constants (s, β) are the same for all n, because REC_CONT needs them hierarchy-wide.

**Deliverable: SRCREAL.md.** Read REALONLY.md, SRCCD55.md, SRCAN55.md and its review, OSLEAF55.md, REC_CONT.md, REALRGA.md, AUDIT.md.

## Sprint rules
This is the owner's end-to-end sprint: reach the end point of the proof first and check the whole thing afterwards. There is no per-lane review. Speed matters, but honesty about status matters more.

**Label every step with exactly one of these:**
- **PROVEN(file):** already landed, at that file's reviewed scope. Quote the exact statement you use. Do not widen its scope.
- **DRAFTED(conf):** you wrote a real argument, but nobody has checked it. Give your honest confidence (high, medium or low) and the single most likely failure point.
- **GAP:** you do not have an argument. State exactly what would be needed and why the obvious approach fails.

**Never write plausible text in place of an argument.** A GAP is a useful result. A fabricated step is the worst possible outcome, because a later reader cannot tell it from a real one. Do not invent constants. If a constant is not computed, write it as a named symbol with the inequality it must satisfy.

**Track interfaces explicitly.** For each step, state what it consumes and what it produces, in exact form, so that the end-to-end check can compare them mechanically. Constant windows must be stated and checked for mutual consistency.

**Do not stop at the first failure.** Mark it and continue to the end, conditional on a stated assumption.

Create and edit only SRCREAL.md. No commits, no audit or ledger files, no axiom edits. No numerics unless they are essential, and then under 1 GB and BLAS=1. Final message under 250 words: the counts of PROVEN, DRAFTED and GAP, plus the three weakest links.

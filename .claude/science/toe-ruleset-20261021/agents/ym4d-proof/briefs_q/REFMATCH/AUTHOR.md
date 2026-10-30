# Lane REFMATCH: identify the inherited interacting reference with the product law, inductively, and pay normalizer derivatives
**Why.** MIXSMALL.md (LAND, 1079134633) PROVES a small mixed-group theorem for fixed gap events under the actual *conditional product kernel*. It does not identify that product law with the *inherited interacting reference*, so the all-history mixed-group estimate is still OPEN. It also gives a concrete SU(2) field showing that an **unpaid** uniform fine-field derivative bound for an individual kernel normalizer is false. Derivatives must be paid for.

**Target. Close the gap inductively.**
1. **Reference comparison under the induction hypothesis.** Assume REALRGA's H-hypotheses at step j. The inherited reference is then the product law times exp(polymer gas), with small real Taylor norms. Prove that this lets MIXSMALL's fixed-gap theorem transfer from the product law to the actual inherited reference, with only controlled loss: a Mayer/cluster comparison in the real norm. The argument must not be circular. State exactly which step-j outputs are used and which step-(j+1) outputs are produced.
2. **Paying normalizer derivatives.** For MIXSMALL's SU(2) counterexample class and its generalisation, show that each derivative of a kernel normalizer can be charged against one of three sources:
   - a fresh gap price (JMBRB);
   - the one-use original action (CHARGE);
   - the large-field weight in REALRGA's norm.

   Give the explicit price per derivative, and check that the derivative order k (k = 4 suffices for the witnesses) stays within budget.
3. **Combined statement.** Combine 1 and 2 with EXTCONT's conditional continuation theorem and LOCOP if present. State the conditional theorem "one complete real RG step" and its exact remaining hypotheses.

**Deliverable: REFMATCH.md**, with every item marked PROVEN, ARGUED or OPEN, and the final conditional one-step theorem. Read MIXSMALL.md, EXTCONT.md, REALRGA.md, REALRGB.md (each with its review), JMBRB.md, CHARGE.md, RENEW.md, and LOCOP.md if present.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/refmatch_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only REFMATCH.md, REFMATCH_LOG.md and checks/refmatch_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

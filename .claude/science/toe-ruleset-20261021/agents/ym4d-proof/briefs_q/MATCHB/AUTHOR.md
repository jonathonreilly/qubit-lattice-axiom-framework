# Lane MATCHB: an adapted interacting cell reference, as an alternative to RM1's product identity
**Why.** REFMATCH.md §7 notes that the product-reference identity RM1 may not hold in the form asserted. It lists live alternatives: "an adapted interacting cell reference, joint integration with cancellations, weighted readers, and charged or extracted continuation". A parallel lane, MATCHA, tries RM1 directly on an actual history. This lane tries the alternative.

**Target.** Replace the product reference by a **nonproduct, interacting cell reference** adapted to the inherited law: each block cell carries the actual conditional law from its ancestry, not a product of bare kernels. Then:
1. Define it exactly, and prove it has the pinned bounds that REFMATCH §2 requires of nonproduct cells: positivity, total variation one, finite-range dependence, uniform derivative bounds, and the local ratio bounds. It must be built on identical variables to the numerator.
2. Redo the comparison RM7–RM13 with this reference. Show what improves (RM2's smallness should become easier, since the inherited interaction is built in) and what gets harder (factorization between cells, and regeneration at the next step).
3. Regeneration: show that the next step's reference has the same form, with the same constants. Without this, the induction does not close.

**Deliverable: MATCHB.md.** Mark each item PROVEN, ARGUED or OPEN, compare with RM1, and give the exact failing inequality if there is one. Read REFMATCH.md and its review, MIXSMALL.md, REALRGA.md, REALRGB.md, JMBRA.md, LIB1.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/matchb_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only MATCHB.md, MATCHB_LOG.md and checks/matchb_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

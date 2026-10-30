# Lane EXTCONT: extracted continuation and selected-return regularity, under the real contract
**Why.** This is a parallel lane to MIXSMALL. REALRGA's real contract and REALRGB's real step both leave the following open:
- (d) regularity of selected returns;
- (e) norm control for arbitrary holes;
- extracted continuation, meaning that one step's output, after the relevant and marginal terms are extracted into the effective action and coupling, satisfies the next step's input hypotheses with the same constants. That is the induction closure.

**Target.**
1. Specify the extraction map: which local terms are moved into the effective coupling (FLOW's normalisation u = 2N/g², β₀′) and into the counterterms. Prove that the remainder obeys REALRGA's H-bounds at the next scale with the required contraction factor (irrelevance ∼ L^{-something}). Use the real Taylor-seminorm calculus and FLOW's landed results: T-tel, FP-exact, Cartan-T, SLICE-U.
2. Selected-return regularity: real-derivative bounds on the returned activity as a function of the selection data (failed region, hole geometry), uniform over histories.
3. Arbitrary-hole norm control: extend RD3 D22-D23 (fixed mask, CARRIES) to derivative acquisition, as REALRGA's NEEDS-REWORK row requires.

Report the exact failing inequalities and whether each is a technique failure or an obstruction.

**Deliverable: EXTCONT.md.** Give a status for each item. State the induction-closure theorem conditionally on MIXSMALL's hypotheses, if that is what it needs. Read REALRGA.md, REALRGB.md and their reviews, FLOW.md (latest sections), RD3.md, RENEW.md, LIB1.md and LINEAR_PACKAGE.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/extcont_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only EXTCONT.md, EXTCONT_LOG.md and checks/extcont_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

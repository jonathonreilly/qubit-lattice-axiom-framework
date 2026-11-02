# Lane RD3: one complete normalised RG step on a real history (RD B2/B3)
**Why.** This is AUDIT priority 1. It blocks all 10 routes to T_OS. RD.md now supplies B1, an exact finite-history identity for the actual returned denominator (REVIEW_RD_R2, "B1 alone: RESOLVED"). B2 and B3 are PARTIAL.

**Target.** Instantiate the RD identity at a **real history**: one with a nonempty failed region and at least one hole. Then:
- **B2.** Supply common complex source and coarse-field domains, a nonzero reference bound, local prefactor budgets, and uniform interaction and failure majorants.
  - Fix the hard-cut mismatch first. A hard indicator that reaches zero has ‖Θ−1‖_∞ = 1, so it cannot be controlled as a small activity. Use one of these, and prove it:
    - (a) treat the failed region as its own polymer species, with an activity bounded by the Peierls-type large-field price (RLARGE / LARGE55 at their reviewed scope);
    - (b) a smooth partition of unity, with its derivative costs;
    - (c) another expansion.
- **B3.** Carry the reference comparison through the remaining integration. Keep the full source norm across holes, using the landed LIB1 R10 hole lemma. Close the effective-level/history induction. Match CX-R and STEP55's quotient prefactor by prefactor.

**If a bound fails, record the exact failing inequality.** Report whether it is a technique failure or an obstruction.

**Deliverable: RD3.md**, with each part marked PROVEN, ARGUED or OPEN, and the precise remaining sub-lemmas. Read RD.md, REVIEW_RD.md, REVIEW_RD_R2.md, LIB1.md, RECOVERY_CLUSTER_ASTRA.md (l.344-357) and CODEX_REVIEW_STEP (R11, item 6). Do not edit RD.md. Write a new RD3.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/rd3_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only RD3.md, RD3_LOG.md and checks/rd3_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

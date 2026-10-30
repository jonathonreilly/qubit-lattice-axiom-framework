# Lane K4CORR: the O(g²) correction to the fourth-cumulant witness
**Why.** K4MATCH.md (HOLD; see REVIEW_K4MATCH.md) proved the conditional reduction, and its 64 exact algebra checks pass. Review item 3 is still open: the sign, size and non-cancellation of the actual Yang–Mills O(g²) correction to the separated fourth cumulant κ4 of e. CUMUL proves that the free leading coefficient is positive.

**Target.**
1. Compute the first correction to the normalized κ4 ratio, at separated points, in the regularization and normalization that CUMUL/K4MATCH use: Z(a) = 1, the clover e, the flowed or separated tests. Specifically:
   - the one-loop (O(g²)) term, including the running coupling's logarithms;
   - the contribution from e's own anomalous scaling (tr F² is RG-invariant up to the β-function factor; state exactly what that implies).
2. Show that at short separations λ, where g²(λ) → 0, the correction is o(1) relative to the leading positive term. State the exact rate, and say whether the sign matters.
3. If an exact closed form is not feasible, give rigorous bounds: the magnitude of the correction coefficient as an explicit upper bound, using rational or interval arithmetic for every load-bearing number. That is enough for non-cancellation at small g.

Pre-register any numerics in checks/k4corr_criteria.md before running them.

**Deliverable: K4CORR.md**. Each item must be marked PROVEN, ARGUED or OPEN. Include an explicit statement of which K4MATCH obligation it discharges.

Read K4MATCH.md, REVIEW_K4MATCH.md, CUMUL.md, LGF.md, FLOW.md (coupling normalisation and β coefficients), TSE55.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/k4corr_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only K4CORR.md, K4CORR_LOG.md and checks/k4corr_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

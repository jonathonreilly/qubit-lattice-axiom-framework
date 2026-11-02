# Lane RD4: uniform B2/B3 for the normalised RG step. Two parallel expansion routes, both probed.
**Why.** This is AUDIT priority 1, on all 10 routes. RD3 (REVIEW_RD3, HOLD) built the explicit failed history and the finite normalisation/reference, did the full hole-norm accounting, and gave an integrated species expansion that fixes the hard-cut sup-norm problem. It also found three technique obstructions; none is an RG no-go:
- a hard predicate cannot be a small sup-norm atom;
- a normalised mandatory rare species cannot be a small defect, because it costs 1/p;
- a complex reference comparison needs T_ref.

The remaining binding work is REVIEW_RD3 B2a, B2b, B3a and B3b (around l.287-324).

**Probe both routes. Do not pick one; report which one closes.**
- **Route C (conditioning):** follow REVIEW_RD3 B2b's hint. When conditioning on a mandatory event, extract its mass once, globally, as a prefactor. Then estimate the resulting *conditional* interaction as a small polymer gas, with complex contour measures handled by total variation.
- **Route L (large-field regions, Balaban-style):** split each history into small-field and large-field regions. The large-field regions carry their own Peierls price, as in RLARGE / LARGE55 at reviewed scope. The small-field complement carries the analytic cluster expansion with a matched reference. The failed region then becomes a boundary condition, not an activity.

For each route:
- **B2a:** a uniform common domain.
- **B2b:** reference, interaction and failure budgets.
- **B3a:** a uniform local comparison after full integration, including the K norm for D22/D23.
- **B3b:** quantitative closure, meaning the output satisfies the next step's input estimates, plus a literal match to STEP55 and CX-R.

Mark each item PROVEN, ARGUED or OPEN. Record any failing inequality exactly, and say whether it is a technique failure or an obstruction.

**Deliverable: RD4.md.** Read RD.md, RD3.md, REVIEW_RD.md, REVIEW_RD_R2.md, REVIEW_RD3.md, LIB1.md, RLARGE.md / LARGE55.md with their reviews, RECOVERY_CLUSTER_ASTRA.md and STEP55.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/rd4_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only RD4.md, RD4_LOG.md and checks/rd4_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

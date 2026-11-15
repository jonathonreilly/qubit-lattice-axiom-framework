# Lane LOCOP: the gauge-compatible localization operator and coefficient recursions (EXTCONT E19)
**Why.** EXTCONT.md (LAND, 575d228ec4) PROVES a conditional continuation theorem. It does this through a finite-chart extraction identity and an ideal real Taylor contraction with an explicit constant, E1–E7. It leaves OPEN two things:
- the actual **gauge-compatible localization operator**, which extracts the relevant and marginal local terms into the effective coupling and counterterms;
- the **uniform coefficient recursions** E19.

This is the induction-closure piece of the real RG contract (REALRGA).

**Target.**
1. **Define Loc.** Give an explicit Loc on polymer activities of lattice SU(N) gauge fields with the soft kernel. It must:
   - map a local activity to a gauge-invariant local polynomial in the field strength, of dimension ≤ 4. In practice that means the tr F² (Wilson) coefficient; dimension-2 terms are forbidden by gauge invariance, so show why this holds on the lattice with the S4′ averaging;
   - commute with lattice symmetries and gauge transformations;
   - leave a remainder (1 − Loc)K that obeys REALRGA's H-bounds at the next scale, with the irrelevance contraction L^{−(d_irr)}, where d_irr is at least 1.

   Use the real Taylor-seminorm calculus, following the BBS Loc construction as method only; credit it and rebuild it here.
2. **Coefficient recursion.** Give the recursion for the extracted coupling coefficient. Match it to FLOW's normalisation (u = 2N/g², β₀′ = 2N·2b₀, the T-tel exact telescoping, FP-exact). Show uniform bounds on the coefficient recursion along the asymptotic-freedom trajectory. State exactly what is still needed beyond FLOW's landed results.
3. **Gauge breaking.** Check whether the soft kernel and the S4′ averaging break gauge covariance at any order in the extraction, in a way that would force extra counterterms such as a gluon mass term. If they do, quantify it, or prove it is excluded.

**Deliverable: LOCOP.md**, with each item marked PROVEN, ARGUED or OPEN and the exact remaining sub-lemma. Read EXTCONT.md and its review, REALRGA.md, REALRGB.md, FLOW.md (latest sections), LINEAR_PACKAGE.md, BFT_A.md and BFT_B.md (gauge-covariance clauses), and SF.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/locop_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only LOCOP.md, LOCOP_LOG.md and checks/locop_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

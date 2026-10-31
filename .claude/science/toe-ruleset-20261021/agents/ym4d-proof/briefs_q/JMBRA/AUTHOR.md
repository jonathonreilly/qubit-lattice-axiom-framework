# Lane JMBRA: prove LF-JMBR (the joint matched boundary-return lemma) by the soft-kernel cone route
**Why.** LFPRICE.md §6 reduces the RG step's core (the AUDIT's first priority, on all 10 routes) to one precisely stated OPEN lemma, **LF-JMBR**, with clauses 1-5. It also PROVES (LF2) why the obvious alternative fails. With compact Wilson variables, a coupling-dependent threshold gives only a sublinear price c·u^δ. That cannot beat the linear depth cost for singleton components. So small large-field components must be **returned**, i.e. integrated with every small-field cluster that reads them, instead of frozen.

**Route A, the soft-kernel cone.** LFPRICE §(PROVEN raw-cone scope) shows that in a forward-closed cone of Decision-4 kernels each normalized kernel integrates to 1, as long as no remaining factor reads the removed variable. Use that exact Markov structure:
- Integrate the large variables of a component together with exactly its reading clusters, the "reader closure", and get an exact local factor.
- Build clauses 1-5 of LF-JMBR on RD3's R_h / Z_A, uniformly. Clause 4 (exact factorization of disjoint grouped types) and clause 5 (return all n < n_0 with failed-return alternatives) are the core.
- Where reader closure fails, keep the tails in a weighted version, as LFPRICE l.~707 suggests.

**Deliverable: JMBRA.md.**
- Each clause marked PROVEN, ARGUED or OPEN, with any failing inequality given exactly.
- Every result rebuilt in this note. Credit Balaban and Dimock.

Read LFPRICE.md §1-§6 and its review, RD3.md, RD4.md, REVIEW_RD3.md, LARGE55.md (COL, TL/PP) with CODEX_REVIEW_LARGE, LIB1.md and SOFTHARD.md (G1/G2).

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/jmbra_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only JMBRA.md, JMBRA_LOG.md and checks/jmbra_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

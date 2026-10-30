# Lane JMBRB: prove LF-JMBR (the joint matched boundary-return lemma) by Balaban's per-step large-field renormalization
**Why.** This is a parallel attempt on the same lemma as JMBRA. The two use different strategies, and both are being tried so we can see which closes. LFPRICE.md §6 states LF-JMBR (clauses 1-5) as the single OPEN core of the RG step. LF2 proves that freezing singleton large-field components fails for compact variables, because the threshold price c·u^δ is sublinear.

**Route B: renormalize large-field regions at every step.** This is Balaban's organization; LARGE55 "large fields renormalised every step" proposes the same thing (the reviewed lemmas are confirmed, but the route change is not endorsed). Large-field regions are not frozen. At each RG step:
- the large-field region is re-blocked;
- its configuration is mapped to the next-level variables;
- its weight is carried as a local large-field activity with a *per-step* price.

The per-step price must beat only the *per-step* volume factor L^4, not the accumulated depth. Prove that this replaces the depth-summability condition n·a_eff·β > 4 + c_B with a per-step one that singletons satisfy.

Then build LF-JMBR clauses 1-5, or the per-step analogue:
- the matched boundary between large- and small-field regions, in clauses 2-3;
- joint factorization, in clause 4;
- returns of failed small components, in clause 5;
- uniformity in volume, depth and history.

Say exactly where this route meets the soft kernel. The soft kernel's finite-cost response to wild data (SOFTHARD G2) may be what gives the per-step price.

**Deliverable: JMBRB.md.** Mark each clause PROVEN, ARGUED or OPEN, and compare with Route A. Rebuild every lemma from scratch; credit Balaban and Dimock for the method.

Read LFPRICE.md and its review, LARGE55.md with CODEX_REVIEW_LARGE, RLARGE.md v3 with REVIEW_RLARGE_V3, RD3.md, RD4.md, F17.md and SOFTHARD.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/jmbrb_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only JMBRB.md, JMBRB_LOG.md and checks/jmbrb_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

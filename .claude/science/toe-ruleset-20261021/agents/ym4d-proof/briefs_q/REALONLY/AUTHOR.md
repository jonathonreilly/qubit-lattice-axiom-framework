# Lane REALONLY: can real-sector estimates replace the complex-source norms?
**Pattern (lead).** Five consecutive RG-core lanes (RD3, RD4, JMBRB, RENEW, CHARGE) each **PROVE** bounds in the real sector and then stall at the same place: the local complex, mixed-reader norm. That is analyticity in complex sources, including the "coherent no-gap part" (CHARGE R3). CHARGE proves original-action charging against the actual real all-cut denominator, uniformly. What it cannot reach is the complex domain.

**Question.** Which consumers truly need complex-source analyticity, and which could be fed by **real-only** estimates? Real-only estimates here means real tilts/sources, convexity, Hölder/chessboard, positivity and moment bounds. Example: SRCAN item 14's "SRC (B) real-tilt CD".

**Steps.**
1. For each consumer of the RG output, list exactly what it consumes from complex analyticity. Consumers:
   - H_reg / OS0 growth (E0′: linear growth, factorial moments);
   - the witness matchings (PL-1L, K4MATCH);
   - H_Euc inputs (TQ2 / N5B);
   - REC/OSLEAF;
   - the coupling flow.

   Cauchy estimates are used to turn analyticity into moment and derivative bounds. Decide whether real-tilt moment generating functions with explicit growth can give the same bounds. For example, uniform bounds on E[exp(t·O)] for real t in a fixed window, plus positivity, give factorial moment growth with no complex domain.
2. **Normalized ratios.** Identify where complex analyticity is unavoidable, in particular where a normalized ratio needs a zero-free denominator. Decide whether real positivity of the relevant partition functions (real sources, positive measures) settles zero-freeness trivially, or whether complex sources enter through the OS reconstruction or the RG induction itself.
3. **Rebuilt contract.** Give the contract rebuilt on real-only estimates, and say which RG-core clauses it would close. Start from CHARGE's real-sector bound and LF-JMBR clauses 2-5 restated for the real sector.

**Deliverable: REALONLY.md.** For each consumer, state one of: REAL-SUFFICES (PROVEN implication), COMPLEX-NEEDED (with the reason), or OPEN. Give the net effect on the critical path.

Read CHARGE.md, RENEW.md, RD3.md, RD4.md, JMBRB.md, SRCAN55.md with its review, SRCCD55.md, OSLEAF55.md (E0′), REC_LIB.md, WITNESS.md, K4MATCH.md and AUDIT.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/realonly_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only REALONLY.md, REALONLY_LOG.md and checks/realonly_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

# Lane TQ: go/no-go on the flat-route infrared input for Euclidean invariance
**Target.** ASSEMBLY55 N12 (around l.279), TQ55 and CODEX_REVIEW_TQ. TQ is the flat route's infrared input to H_Euc. The audit says "nothing on disk excludes its failure".

**Steps.**
1. **Precise statement.** State TQ exactly as the flat H_Euc chain consumes it (ROTDEF I5, N11).
2. **Necessity.** Decide whether TQ is needed, or whether a weaker statement suffices. For example: a statement purely in the ultraviolet at fixed volume (UNIV55's "rotated-lattice universality is ultraviolet at fixed volume"), together with a volume-limit argument that does not need infrared decay.
3. **Feasibility.** For whatever is needed, decide whether it is feasible without a mass gap. A step that needs exponential clustering is effectively the mass gap and counts as NO-GO.

**Deliverable: TQ.md.** It must give a GO / NO-GO / UNDECIDED verdict for the flat H_Euc route. If the verdict is UNDECIDED, give the minimal settling lemma. Also compare with the sphere route's UV-only claim.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/tq_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only TQ.md, TQ_LOG.md and checks/tq_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

# Lane AUDIT: critical-path audit. Is there a complete chain to T_OS?
**Goal.** Decide whether the program is building toward a proof or collecting lemmas.

**Starting graph.** Use the current assembly DAG: ASSEMBLY55.md, CODEX_REVIEW_ASSEMBLY.md and its ordered list, and HANDOFF "Remaining proof path".

**Map every result now on the branch onto the DAG.** This includes HRP, REC_LIB and REC_CONT, LGF, W_T0, LIB1, SOFTHARD, RD (and RD's pass-2 edits if present), plus the coordinator's reviewed units listed in HANDOFF. Use each result's reviews, including REVIEW2_* and REVIEW_XFAM_*, and record its status exactly at its reviewed scope.

**Deliverables (AUDIT.md):**
1. **The updated DAG.** List every node needed for T_OS, with one status each: LANDED, CONDITIONAL on named inputs, OPEN, or AT-RISK (no mechanism on disk, or a suspected obstruction).
2. **The candidate chains.** For each route (flat or sphere, and each witness), list the minimal set of OPEN and AT-RISK leaves that stand between it and T_OS. Say whether any route has no AT-RISK leaf.
3. **A ranking of the AT-RISK leaves.** Rank by how many routes they block, and by how likely each is to be an obstruction rather than a missing lemma. Cite the evidence: F17 / CODEX_REVIEW_ASSEMBLY R4, N12 TQ, the SPHERE55 l.~661 failure point, F13, and any others you find.
4. **Wasted work.** Mark any landed or active work that feeds no surviving route.
5. **Mass gap.** State plainly whether any node on disk addresses the infrared gap. The relevant file is MASS_GAP_TARGET.md.
6. **Ordering.** Give a recommended order of attack: first the go/no-go tests, then the core.

This is a mapping audit, so no new proofs are expected. Every status must be quoted from its source with a locator.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/audit_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only AUDIT.md, AUDIT_LOG.md and checks/audit_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

# Lane F17: go/no-go on the large-field strength needed by the witness upper bound
**Target.** ASSEMBLY55 F17 (around l.494) and N15. (TS-up) needs (LF-inst): P_j ≤ Ce^{−c_LF u_j} with c_LF β₋ > 4. HINT2_55 R2.4 argues that the Balaban-type factor e^{−c p(g_j)²} loses against L^{4(k−j)}. However, CODEX_REVIEW_ASSEMBLY R4 says this bound "is not established as necessary".

**Steps.**
1. **Necessity.** Decide whether (LF-inst) at that strength is actually necessary for (TS-up), or for the version of (TS-up) that W_T0's two-scale reduction consumes. If the bound is not necessary, give the weaker sufficient large-field input. A route that needs only the weaker input is the preferred outcome.
2. **Achievability.** For the input that turns out to be needed, decide whether the soft-kernel RG (decision 4) can deliver it. Use RLARGE / LARGE55 / LCONV55 and the Peierls-type per-step bounds; their reviews give the reviewed scope. The possible outcomes are:
   - **PROVEN:** a proof or a reduction to named lemmas;
   - **OBSTRUCTION:** an explicit obstruction, as a counterexample or a counting argument showing that no per-step bound of the available form can suffice;
   - **UNDECIDED:** in which case name the precise lemma that would settle it.

**Deliverable: F17.md.** It must give a GO / NO-GO / UNDECIDED verdict for the non-freeness upper bound via this route, and state what changes for H_int under each outcome. Give the instanton action normalisation explicitly (8π²/g², with the lane's β and u conventions).

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/f17_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only F17.md, F17_LOG.md and checks/f17_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

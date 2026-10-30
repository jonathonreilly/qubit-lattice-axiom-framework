# Lane MGX: early probe of the mass-gap crossover (MG2/MG3)
**Why.** This is AUDIT step 4. MASS_GAP_TARGET has a fixed-spacing, strong-coupling gap (0 < β ≤ 1/32, H = −a^{-1} log P_∞, with a unique vacuum). Every continuum node is OPEN, and MG3 (uniform continuum passage) is AT-RISK.

**Target.** Decide what a crossover argument needs and whether it is plausible.
- Option A: match the strong-coupling endpoint to a fixed physical block on the proposed continuum (asymptotic-freedom) trajectory. The RG would carry the weak-coupling theory down to a coarse lattice where the effective coupling is strong enough for the fixed-spacing theorem.
- Option B: state a direct uniform transfer estimate for a dense observable family.

**Questions.**
1. Does the RG's effective action at the coarse scale actually land in the fixed-spacing theorem's hypothesis class? Consider the effective action's form, its locality, its non-Wilson terms, and whether β ≤ 1/32 is reachable. Without a gap, the running coupling only grows logarithmically; check whether it can reach strong coupling within the RG's control region.
2. Does the gap survive the passage with a positive physical rate (MG3)?

Give GO / NO-GO / UNDECIDED, with the exact obstruction or the settling lemma.

**Scope note.** This is the Clay problem's hard part. An honest UNDECIDED, with the obstruction precisely located, is a good outcome. Do not overclaim.

**Deliverable: MGX.md.** Read MASS_GAP_TARGET.md, REVIEW_MASS_GAP_TARGET_ASTRA.md, the fixed-spacing construction/review files it cites, FLOW.md (the coupling trajectory) and AUDIT.md (MG0-MG5).

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/mgx_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only MGX.md, MGX_LOG.md and checks/mgx_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

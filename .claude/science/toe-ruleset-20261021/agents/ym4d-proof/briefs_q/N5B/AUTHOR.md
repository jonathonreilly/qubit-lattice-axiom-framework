# Lane N5B: go/no-go on the sphere route's most likely failure point
**Target.** SPHERE55 §6 (around l.~655-665) calls N5b / N5-RG at large coarse fields "the single most likely point of failure of the IR-freeness claim". It needs decorrelation across a distance of about πR/2. Also covered: ASSEMBLY55 F13 (RG producers live on hypercubic tori, but the sphere consumes them on K_a) and N13.

**Steps.**
1. **Exact consumption.** State exactly what N5b and N5-RG must deliver for the sphere route's H_Euc and OS1 (SPHERE55, SPHERE2_55, SEAM55 and their Codex reviews).
2. **Infrared content.** Decide whether this requires genuine infrared decorrelation, which would be mass-gap-like and count as NO-GO for existence without a gap. Alternatively, it may follow from ultraviolet / RG estimates on the sphere's finite volume at fixed R, followed by the R → ∞ limit at the level of moments.
3. **F13 transfer.** Check whether the hypercubic-torus RG producers transfer to K_a, or name the obstruction.

**Deliverable: N5B.md.** It must give a GO / NO-GO / UNDECIDED verdict for the sphere route, the minimal settling lemma, and a comparison with the flat route.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/n5b_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only N5B.md, N5B_LOG.md and checks/n5b_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

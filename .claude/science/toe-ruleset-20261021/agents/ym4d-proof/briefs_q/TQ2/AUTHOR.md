# Lane TQ2: the flat route's minimal settling lemma (period-lattice orientation, all observables)
**Why.** TQ.md (LAND, UNDECIDED) found two things:
- the flat Euclidean-invariance route needs no mass gap;
- the finite-volume UV comparison is valid without clustering.

The minimal remaining lemma, in TQ.md §5, is the **all-observable** removal of the period lattice's orientation dependence. The old two-point result was not enough. AUDIT ranks this FT, on 5 of 10 routes. The geometry choice turns on this test together with the sphere's N5B.

**Target.** Prove the §5 lemma or reduce it to named estimates.
- It must hold for all n-point separated observables on the common algebra, uniformly along the common sequence.
- Use UNIV55 Proposition T ("the coarse law never enters" at fixed volume) and its review.
- Use ROTDEF and the I5 inputs only at their reviewed scope.
- Look for a mechanism that does not need infrared decay. For example: an averaging over torus orientations or shapes that leaves the moments in the limit unchanged, combined with uniform moment bounds, which can be conditional on H_reg/SRC. Or: a volume-first limit in which orientation effects are boundary terms that vanish.
- If a needed input is infrared, show why, using an explicit example or a counting argument, and mark the route accordingly.

**Deliverable: TQ2.md.** Give a status (PROVEN/ARGUED/OPEN) for each part, and a GO / NO-GO / UNDECIDED update for the flat route compared with the sphere route. Read TQ.md and its review, N5B.md with REVIEW_N5B, UNIV55.md with CODEX_REVIEW_UNIV, ROTDEF.md, SRCCD55.md, ASSEMBLY55 N4/N11/N12/N14, and AUDIT.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/tq2_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only TQ2.md, TQ2_LOG.md and checks/tq2_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

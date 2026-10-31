# Lane WLOOP: probe the extended-observable (Wilson-loop) algebra as a target variant
**Why.** The owner wants every target variant probed in parallel, so that no single choice is forced. Current lanes use the local gauge-invariant composite fields (clover e, time-zero B). This lane tests the other natural algebra.

**Target.** Find what T_OS, and an OS/Wightman-type reconstruction, would require if the observable algebra also contains smeared Wilson loops (and Polyakov loops on tori).
1. **OS axioms.** Can OS0-OS3 be formulated for loop observables? RP for loops crossing the reflection plane is standard on the lattice. Give the regularity, renormalisation and smearing needed for the continuum (perimeter/corner divergences; smoothed or flowed loops), and the reconstruction that applies. Check whether REC_LIB / REC_CONT extend, or what replaces them.
2. **Existing estimates.** Which existing RG producers deliver loop moments? Use SRC, the source hierarchy, the flow and W_T0's flowed objects. Which new estimates would be needed?
3. **Non-freeness.** Is it easier with loops? For example, an area-versus-perimeter comparison at short distance against free-field loop expectations, or flowed-loop witnesses.
4. **Mass gap.** Does including loops change the mass-gap target? Consider string-tension or confinement statements and the existing Polyakov-loop route mentioned in the existence lane.

**Verdict.** Compare this variant with the local-field algebra: same/easier/harder for each top-level input (H_reg, H_RP, H_Euc, H_int). Give GO / NO-GO / UNDECIDED for using loops, or combining both.

**Deliverable: WLOOP.md.** Read ASSEMBLY55 N0/N6, OSLEAF55, REC_LIB.md, REC_CONT.md, W_T0.md, HRP.md and ../ym4d-existence/E/EXISTENCE.md (the Polyakov-loop route; grep it).

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/wloop_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only WLOOP.md, WLOOP_LOG.md and checks/wloop_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB, with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

# Lane MIXSMALL: local smallness of mixed groups and mixed-reader prices, under the real contract
**Why.** REALRGA.md (LAND, 0f561ef0b2) specifies the real Taylor-seminorm RG contract H0-H5. It also proves the elementary real calculus and the conditional cluster/induction implications. Its carry-over map marks CHARGE, RD3, RD4 and the other lanes as CARRIES, NEEDS-REWORK or OBSOLETE.

REALRGB.md (LAND, 8abd4d1835) proves on a real step:
- nonvanishing and total variation one;
- relative fourth-derivative bounds;
- a real fourth-jet version of CHARGE.

Both lanes agree that the remaining core estimates already occur on real fields:
- (a) local mixed-group smallness;
- (b) mixed-reader prices;
- (c) local normalizer derivatives;
- (d) regularity of selected returns;
- (e) norm control for arbitrary holes.

This lane covers (a), (b) and (c). A parallel lane, EXTCONT, covers extracted continuation.

**Target.** Prove REALRGA's H-hypotheses that govern local smallness on the actual soft-kernel step:
- **Mixed groups.** For every connected group in which small- and large-field parts are read together, the real Taylor seminorm, up to the contract's derivative order k, must be ≤ ε^{|group|} with ε small and uniform in volume, history and holes. That is the Mayer convergence condition of REALRGA.
- **Prices.** Use CHARGE's one-use real charging (CARRIES), JMBRB's per-step prices, JMBRA's exact reader integration (clause 1) and RD3's hole transfer (fixed-mask, CARRIES; derivative acquisition NEEDS-REWORK, with constants 730 and 649μ quoted in REALRGA's map). Bound the local normalizer log-derivatives directly from positivity and the kernel gap structure.
- **Failures.** If smallness fails for a group class, construct the class and say whether it is a technique failure or an obstruction.

**Deliverable: MIXSMALL.md**, giving a status for each H-hypothesis and an updated REALRGA carry-over row for each consumed result. Read REALRGA.md, REALRGB.md and their reviews, CHARGE.md, JMBRA.md, JMBRB.md, RENEW.md, RD3.md, RD4.md and LIB1.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/mixsmall_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only MIXSMALL.md, MIXSMALL_LOG.md and checks/mixsmall_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

# Lane ROUGH: inherited-law rough-sector integration (REFMATCH open input)
**Why.** REFMATCH.md §7 lists as OPEN: "Complete inherited-law rough-sector integration. Show the same-law original-charge/regulator moment estimate with all overlaps, source jets, readers and history sums." The persistent-flux family (RENEW) is the hard test case. CHARGE proves real-sector charging for the filled family only.

**Target.** Prove the joint moment estimate under the *inherited* law, for general rough cores and not only the filled-flux tube. Do the following:
- charge each rough core's original action exactly once;
- include overlaps between cores and all four source labels;
- bound the sum over histories, with the entropy counted explicitly against the price.

Use REFMATCH RM14–RM24, CHARGE C5–C23 and JMBRB's gap prices. Give the exact failing inequality if one fails, and say whether it is a technique failure or an obstruction.

**Deliverable: ROUGH.md.** Read REFMATCH.md, CHARGE.md, RENEW.md, MIXSMALL.md, JMBRB.md and REALRGA.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/rough_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only ROUGH.md, ROUGH_LOG.md and checks/rough_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

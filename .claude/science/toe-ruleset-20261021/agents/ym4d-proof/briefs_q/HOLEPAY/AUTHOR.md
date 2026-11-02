# Lane HOLEPAY: the differentiated hole-volume payment (EXTCONT E15 input)
**Why.** EXTCONT.md proves arbitrary-hole control (E15–E17) given a complete differentiated hole-volume payment. It also proves that unweighted saturation is unbounded for fixed positive support rate. MIXSMALL sharpens the fixed-hole transfer without derivatives. REFMATCH §7 keeps this OPEN.

**Target.** Construct the payment on the actual model. Decide what pays for hole volume, including derivatives:
- the large-field price of the failed region (CHARGE, JMBRB);
- the failed region's boundary (LFPRICE's c_B and M3);
- a weight in the norm (REALRGA H-hypotheses).

Handle holes that grow or merge across levels (LIB1's R10 hole lemma is landed and available). Give explicit constants. Give the exact failing inequality if one fails.

**Deliverable: HOLEPAY.md.** Read EXTCONT.md, MIXSMALL.md, LIB1.md, LFPRICE.md, CHARGE.md and REALRGA.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/holepay_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only HOLEPAY.md, HOLEPAY_LOG.md and checks/holepay_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

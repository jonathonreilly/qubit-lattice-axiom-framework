# Lane RENEW: the renewal bound for inherited rough inputs, combining JMBRA with JMBRB
**Why.** LF-JMBR (LFPRICE §6) is the single lemma at the core of the RG step and blocks every route. Two parallel attacks have landed:
- **JMBRA** (the soft-kernel cone) proves clause 1 exactly. That covers finite reader integration, conditional weighted-tail bounds, and an example of a failed return with positive measure.
- **JMBRB** (Balaban's per-step renormalization) proves that per-step re-blocking removes the depth problem *if each step earns a new price*. The soft kernel supplies that price for gap events and for a conditional bad-plaquette branch. It does **not** supply one for the branch where the coarse mean is already rough, inherited from earlier steps. The SOFTHARD G2 finite debit is not a renewal probability.

**Target.** Prove a **renewal bound** for that inherited-rough-mean branch. The bound must say one of two things:
- (a) per step, either a fresh price is earned, or the roughness contracts by a fixed factor, an irrelevant contraction (one example: the rough part of the coarse field is a block average, and averaging is smoothing);
- (b) the rough branch returns to the small-field regime within a bounded number of steps, with total probability or weight controlled.

Combine JMBRA's exact reader integration (clause 1) with JMBRB's per-step price, and work on clauses 2-5 under the resulting renewal structure. Probe every mechanism you find, for example:
- smoothing by S4′ averaging, with the contraction factor of the block-average map on curvature;
- the kernel's quadratic restoring force toward the centre M̄_c;
- the kernel's gap structure.

If roughness cannot contract for a class of inherited configurations, construct that class explicitly. That is either a counterexample to the route or a measure-zero/small-weight set; say which.

**Deliverable: RENEW.md.** It must give:
- the renewal lemma, marked PROVEN, ARGUED or OPEN;
- the updated status of each LF-JMBR clause;
- the exact remaining sub-lemma.

Rebuild everything from scratch. Credit Balaban and Dimock for the method. Read JMBRA.md, JMBRB.md and their reviews, LFPRICE.md, RD3.md, RD4.md, LARGE55.md, SOFTHARD.md, LINEAR_PACKAGE.md (the averaging geometry and contraction constants), and BFT_A.md / BFT_B.md where the smoothing estimates live.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/renew_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only RENEW.md, RENEW_LOG.md and checks/renew_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

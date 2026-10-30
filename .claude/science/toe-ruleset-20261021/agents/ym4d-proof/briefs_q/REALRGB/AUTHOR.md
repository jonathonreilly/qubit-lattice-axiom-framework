# Lane REALRGB: one RG step in real-derivative form
**Why.** REALONLY.md shows that every downstream consumer needs only real estimates. CHARGE.md PROVES real-sector bounds, in particular original-action charging against the actual real all-cut denominator, uniformly. RD3 and RD4 PROVE real-sector pieces. They all stall only at complex norms. A parallel lane, REALRGA, is designing the full real Taylor-seminorm contract. This lane tests feasibility directly on one step.

**Target.** Take one soft-kernel RG step (decision 4) on the history class that RD3/RD4 use, including a failed region and a hole. Prove the step's real-derivative estimates:
- real Taylor-seminorm bounds, up to order k (choose k; for the witnesses k = 4 suffices, per K4MATCH/REALONLY), on the returned normalized activities, uniformly in volume, history and holes;
- the normalizer, handled by real positivity: confirm it is strictly positive and bound its log-derivatives;
- the large-field branch, using CHARGE's real charging and JMBRB's per-step prices;
- the persistent-flux family of RENEW, using CHARGE R1 real-sector bounds;
- the output estimates in the form the next step needs.

Pin down which LF-JMBR clauses 2–5, restated for real fields, close here. Where something still fails, give the exact failing inequality, and say whether it is specific to the real norm or shared with the complex one.

**Deliverable: REALRGB.md**. Each item gets a status of PROVEN, ARGUED or OPEN. Read REALONLY.md, CHARGE.md, RENEW.md, RD3.md, RD4.md, JMBRA.md, JMBRB.md, LFPRICE.md, LIB1.md, and REALRGA.md if it is already present; otherwise state the norm you use.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/realrgb_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only REALRGB.md, REALRGB_LOG.md and checks/realrgb_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

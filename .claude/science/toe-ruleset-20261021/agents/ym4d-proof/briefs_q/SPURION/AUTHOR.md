# Lane SPURION: mixed fine/coarse activities, exterior spurions and the gluon-mass question
**Why.** LOCOP.md (LAND, b872c85503) PROVES the following:
- an explicit gauge-compatible local projector on the single-field small-curvature sector;
- zero covariance defect, at every order, for the exact normalized soft-kernel/S4′ transfer;
- absence of a gluon mass and of terms with dimension below 4, for a *local single connection with no untransformed exterior spurion*;
- an exact conditional coupling recursion and an AF bracket.

LOCOP's L3 is an exact counterexample to the blanket statement for **mixed fine/coarse activities**. When an activity depends on both the fine field and an untransformed coarse (exterior) field, mass-like or other dimension < 4 terms are not excluded by covariance alone. LOCOP also leaves LC1 OPEN: assembling Loc on all actual histories and readers.

**Target.**
1. Classify which mixed activities in the actual RG step carry an untransformed exterior spurion. Decide, for each case, which of these holds:
   - (a) the spurion is a gauge artefact of the fixed coarse background. Then a background-covariant re-expression, coarse gauge transformations acting on both, removes it. Use BFT_A/BFT_B's background-field covariance (CovLift) at reviewed scope.
   - (b) the dimension < 4 terms are present but cancel after integration over the coarse field. Use exact Haar/gauge averaging.
   - (c) they survive. Then they must be tuned as counterterms. Determine how many there are, their size, and whether the tuning is causal and compatible with LOCOP's AF bracket.
2. Assemble Loc on all histories and readers (LC1). Use the classification for mixed activities and LOCOP's L5 for single-field ones.
3. Explicitly settle the physical question: does any gluon-mass-like counterterm need tuning in this scheme? If it does, the scheme breaks the gauge-invariance protection that the continuum limit relies on. Quantify it, or exclude it.

**Deliverable: SPURION.md.** Mark each item PROVEN, ARGUED or OPEN. Read LOCOP.md and its review, EXTCONT.md, REALRGA.md, BFT_A.md and BFT_B.md (CovLift and background covariance), RD3.md, MIXSMALL.md, and FLOW.md (COV-GI).

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/spurion_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only SPURION.md, SPURION_LOG.md and checks/spurion_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

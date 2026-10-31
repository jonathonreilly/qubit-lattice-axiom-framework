# Lane K4CORR2: an explicit upper bound on the O(g²) correction to κ4 (non-cancellation)
**Why.** K4CORR.md (HOLD, REVIEW_K4CORR.md) derived the conditional cancellations of the logarithmic and anomalous factors, and the short-distance rate; its 56 exact checks passed. What is still OPEN is the actual finite O(g²) Yang–Mills correction and a uniform non-cancellation bound.

**Non-cancellation does not need the exact coefficient.** An explicit upper bound |c₁| ≤ C̄ is enough. With it, κ4 = κ4^{free}·(1 + c₁ g²(λ) + O(g⁴ log)) stays positive whenever g²(λ) < 1/(2C̄).

**Target.**
1. Write the O(g²) term of the normalized separated fourth cumulant of e. Use the regularization K4CORR uses, with separated test functions.
2. Bound every diagram class by explicit, elementary means: position-space propagator bounds from LGF.md (landed, explicit constants), Hölder / Young inequalities, and the separation of the supports. Give an explicit C̄.
3. Combine C̄ with K4CORR's rate and the free coefficient from CUMUL.md to get an explicit window g²(λ) < g*² in which κ4^{YM} > 0 at this order. Then name exactly the higher-order and nonperturbative remainder estimate that would make the window rigorous for actual YM. That remainder is the K4MATCH lower-matching input.

Use rational or interval arithmetic for every number that carries weight; floating-point "certified" claims are not allowed. Pre-register the criteria in checks/k4corr2_criteria.md. For any resource guard, self-check RSS rather than using RLIMIT_AS.

**Deliverable: K4CORR2.md.** Give an explicit C̄ and g*², and mark each part PROVEN, ARGUED or OPEN. Read K4CORR.md, REVIEW_K4CORR.md, K4MATCH.md, CUMUL.md, LGF.md and FLOW.md.

## Common rules (all queue lanes)
- **Process.** Follow PROCESS_LIGHT.md. Pre-register any numerics in checks/k4corr2_criteria.md. Report statuses honestly as PROVEN, ARGUED or OPEN. A check that fails is reported as failed.
- **Files you may touch.** Create and edit only K4CORR2.md, K4CORR2_LOG.md and checks/k4corr2_*. Do not modify any existing file. The runner discards all other edits.
- **Coordinator lanes.** Avoid the active coordinator lanes listed under HANDOFF.md "Current assignments": fixed source radius, finite-coupling kernel remainder, original-law coercivity and tails. If you need one of their outputs, state it as a named input.
- **Reading.** Use grep -n and offsets for large files. Literature may supply methods only. Credit the authors, and mark anything recalled from memory as [m]. An [m] item can never carry weight in the argument.
- **Resources.** Run with nice and BLAS=1, under 1 GB (self-check RSS via resource.getrusage or psutil; do NOT use resource.setrlimit(RLIMIT_AS) - it fails on macOS), with load < 8 and at least 30% memory free. No pools. The sandbox may block nice; if it does, report that instead of weakening the guard.
- **Limits.** No commits. No audit or ledger files. No axiom edits. Final message under 300 words.

# Block 169 — control and findings (2026-09-26)

1. **Provenance.** Probe #9158 (Claude Opus 5.5) found it. #9325 (`grok-4.6`) refereed it with its own checker. The supervisor wrote a new exact runner and did not port the floating-point simulation.
2. **Conditions.** T3 needs A1 (differentiability at `λ = 0`). T1's settling, T4 and T5 need A0 (well-posedness). Neither is proved; the referee noted the same.
3. **For the owner.** Block 95 (landed) states that delayed clocks are absent. With a lagging clock, its pair law survives at first order with the coupling scaled by `2Γ/(2Γ + 1)`. No product law and no reversible law exists at finite `Γ`.

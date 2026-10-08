# Lean candidates for later scientific audit

This is an audit plan, not a completed formalization or a pre-PR gate. Accepted external declarations are pinned to openai/math adc7f1241b42e322a6451854ab7e4b4c146bf78a. No full local Lean build has been run.

Prioritize:

1. PXP: probability-square purity inequality; cross-temperature partition identities; interpolation to every even length; rational seed certificate. Then formalize the finite-measure path kernel, even trace identity and all-length Gauss dictionary if the audit's analytic coverage warrants the larger library work.
2. Independent activation: cylinder-probability pushforward to Bernoulli site percolation, time-to-density transformation and application of OAI.CriticalZ3.critical_no_infinite. Planar models: finite bijections, parity/flux conditions and pair-weight identities.
3. Finite collisions: exact reaction invariants/rank, entropy derivative, positive-class minimizer, persistence theorem application and convergence; finite occupation detailed balance and quadratic-variation formulas, and the uniform finite-horizon Doob–Gronwall bound.
4. Qutrit channels: Kraus completeness, all-matrix-unit intertwining, exact pulse witness, composite-channel formulas and the positive GAD branch; application of OAI.GAD.main at the matched parameters.
5. Heisenberg: Pauli/spin normalization, time/temperature rescaling and local magnetization conversion into the exact exported spontaneous-magnetization theorem.

For any actual formalization, record the Lean/toolchain and dependency revisions, the exact theorem type, permitted axioms and compiler/checker output. Audit the mathematical definitions and model dictionary as well as kernel acceptance. Numerical-only diagnostics and stronger unformalized companion claims keep their declared status.

## Summary

This harvests probe #9214 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee, grok-4.6, confirmed it (#9284). The supervisor ported its exact checks against the landed texts. It works within blocks 54, 69, 120, 136 and 138, all landed, and answers block 138's next items.

- **T1: the spin keeps its own books.** For every state, `dS̃_l/dt + D(x) − D(x − e_l) = −Σ_ij ε_lij(Θ_ij − Θ_ji)`.
  - The spin current is isotropic, `δ_il D`.
  - The torque is the antisymmetric part of block 120's two-step stress.
  - Its curl is block 138 T3.
- **T2: a walker at rest sources only the shift.** For `ψ = fχ` with `f` real, the energy, the two-step momentum and every current vanish. The shift is sourced through `P^B = ¼∇̄ × S̃`, which is momentarily static.
- **T3: the shift is a vector potential.** On a declared lattice reading of block 136 T4, the static shift is `∇̄ × (−Δ̄)⁻¹(w̄S̃/(16α))`: the lattice vector potential of a magnetisation, with zero divergence.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_KEEPS_ITS_OWN_BOOKS_ON_THE_FACES_AND_A_SPIN_POLARISED_WALKER_AT_REST_SOURCES_ONLY_THE_SHIFT_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_the_coins_spin_keeps_its_own_books_on_the_faces_and_a_spin_polarised_walker_at_rest_sources_only_the_shift_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block156.md`, `RESULTS_block156.md`, `CLAIM_STATUS_CERTIFICATE_block156.md` and `CHECKER_block156_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_coins_spin_keeps_its_own_books_on_the_faces_and_a_spin_polarised_walker_at_rest_sources_only_the_shift_2026_09_26.py
```

- The runner gives `TOTAL: PASS=18 FAIL=0` in about 4 s.
- Mutation census 5/5: three mutations in families B and C, and two in F, each failing in its own family.

## Review findings, imports, reachability

- **Referee.** grok-4.6 confirmed the probe's result (#9284).
- **Reading.** T3 reads block 136 T4's transverse constraint on the lattice for a static source; T1 and T2 do not use it.
- **Imports.** Comparators only (the spin of two-component waves, the symmetric momentum, a magnetisation's vector potential), and exact rational arithmetic.
- **Trace.** `frontier_discovery`. It advances block 138's next items.
- **Remaining.** A lattice form of block 136's member; the walker's spreading; the total angular-momentum balance.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

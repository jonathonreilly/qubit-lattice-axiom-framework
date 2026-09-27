## Summary

This harvests probe #8757 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9344 (`grok-4.6`). The note works within block 60 as landed: the walled box, the ledger of weight one, the curvature member and the lengths' kinetic term.

- **T1.** At every configuration, `h := K_λ + 𝓔` satisfies `h − Wt = −Σ_I ∂L/∂u`. So on solutions the kinetic term plus the ledger equals the walls' term (8K times the flux of `χ` into the walls) at every label time.
- **T2.** `dh/dt = −∂L/∂t`: only the content's explicit label dependence moves it.
- **T3.** For supplied content carried along a path, `dWt/dt = Σ w ρ̇` exactly, which is the work of the driver.
  - At weak field, `Wt = Σρ − (ρ·gρ + 3ρ̇·g²ρ̇)/(8K)`.
  - On `3³` a body carried from the centre to a face raises it by `3/952`.
- **T4.** A walker under its own generator keeps the walls' term fixed. Another generator changes it at `i⟨[G, H_eff]⟩`.

Existence of solutions is assumed for walker content and with a kinetic term; block 60 T4 proves it for bodies at rest.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_WHILE_CONTENT_MOVES_THE_WALLS_TERM_IS_THE_KINETIC_TERM_PLUS_THE_LEDGER_AND_MOVES_ONLY_BY_THE_WORK_OF_WHAT_DRIVES_THE_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_while_content_moves_the_walls_term_is_the_kinetic_term_plus_the_ledger_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block174.md`, `RESULTS_block174.md`, `CLAIM_STATUS_CERTIFICATE_block174.md` and `CHECKER_block174_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_while_content_moves_the_walls_term_is_the_kinetic_term_plus_the_ledger_2026_09_27.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0` in about 2 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Homogeneity identities; the energy function of a Lagrangian quadratic in velocities; the inverse of the lattice Laplacian with zero walls; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** Existence of slaved branches for walker content and with the kinetic term; strong-field motion.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

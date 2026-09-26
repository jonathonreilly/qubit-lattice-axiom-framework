## Summary

T1–T3 harvest probe #8843 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed them in #9308 (a Grok worker). T4 is the supervisor's. The note works within blocks 62 and 65, both landed. Block 65 made turning the coin a symmetry at first order. Beyond that, its note says, "a rotation must be carried along each bond", which it did not construct.

- **T1.** A varying turn changes block 62's bond by a term with a coin-scalar part, and no frame bond has one. So the frame alone cannot absorb the turn.
- **T2.** SU(2) links on the bonds, with bond `(1/2)(E_x·σ W + W E_y·σ)`, make turning the coin an exact symmetry to all orders. Links fixed flat by the frame give the stretch walk: the walker sees only `√g`.
- **T3.** For every state, frame and link field, frame torque plus link response equals `½ d⟨σ_c⟩/dt` at every site and axis.
- **T4.** A link `1 + (i/2)a·σ` adds `(i/2)(E·a)𝟙` to the bond. With `a` the lengths' own connection, the long-wavelength scalar is `(1/4)ε_abc ω_abc = (1/8)ε·C`. That is exactly block 158's needed term. Flat links do not supply it.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_LINKS_ON_THE_BONDS_MAKE_TURNING_THE_COIN_A_SYMMETRY_FLAT_LINKS_LEAVE_ONLY_THE_LENGTHS_AND_THE_LENGTHS_CONNECTION_ADDS_THE_INVERSION_ODD_CURL_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_links_on_the_bonds_make_turning_the_coin_a_symmetry_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block161.md`, `RESULTS_block161.md`, `CLAIM_STATUS_CERTIFICATE_block161.md` and `CHECKER_block161_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_links_on_the_bonds_make_turning_the_coin_a_symmetry_2026_09_26.py
```

- The runner gives `TOTAL: PASS=13 FAIL=0` in about 3.5 min.
- Mutation census 7/7: five mutations in families A–E, and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **For a referee.**
  - T4's link sign matches the comparator's covariant derivative: the forward hop gets `∂_j + (i/2)a_j·σ`.
  - T4 holds at long wavelength on smooth zero-corner states.
- **Imports.** The product rule of the coin's matrices; rational unit quaternions; exact symbolic algebra; the spin connection, as a comparator.
- **Trace.** `frontier_discovery`.
- **Remaining.** A nearest-neighbour lattice link rule from the lengths; the other seven species; link dynamics; an other-family referee of T4.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

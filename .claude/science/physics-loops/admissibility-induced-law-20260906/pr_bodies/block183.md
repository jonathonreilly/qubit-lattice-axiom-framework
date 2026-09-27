## Summary

Blocks 155 (open PR #9289) and 167 found the filled sea, if counted as energy, giving way under shear. That is the worked consequence of the third-column item on the sea. Both used block 62's frame, which block 120 excluded as a source for non-uniform modes. This note re-derives the consequence under block 69's two-step coupling, with a per-axis completion in block 176's family, for volume-preserving diagonal stretches.

- **T1.** Per axis `F = s − λsc² + λ²s(1/2 − (1 + q₂)s²)`, with `q = −λ + q₂λ²` and `λ = log ℓ`. Block 69's linear completion and block 176's smooth completion both have `q₂ = −1/2`.
- **T2.** The sea's second-order energy is `E₂ = −(Σλ²/3)[A/2 − (1 + q₂)B] − I`, with `A = ⟨|s|⟩`, `B = ⟨Σs⁴/|s|⟩` and interband part `I ≥ 0`. This is checked exactly on the tori of side 6 and 8.
- **T3.** The sea gives way iff `q₂ < q₂*`, where `q₂* > −1/2` on the infinite lattice (and on sides 6 and 8; `−1/2` on side 4). So both named completions give way. Admissibility (`q ≥ −1/6`) does not constrain `q₂`.
- **T4.** The frame always gives way, as blocks 155 and 167 found.

**For the owner's third column.** The sea item's consequence survives the change of coupling for every completion named so far. In general it rests on the coupling axis through `q₂`.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_UNDER_THE_TWO_STEP_COUPLING_WHETHER_THE_SEA_GIVES_WAY_UNDER_SHEAR_IS_SET_BY_THE_COMPLETIONS_SECOND_ORDER_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_under_the_two_step_coupling_whether_the_sea_gives_way_under_shear_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block183.md`, `RESULTS_block183.md`, `CLAIM_STATUS_CERTIFICATE_block183.md` and `CHECKER_block183_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_two_step_coupling_whether_the_sea_gives_way_under_shear_2026_09_27.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0` in about 4 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Second-order expansion; zone averages; representations of the axis permutations; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Off-diagonal shears, which need a completion off the axes.
  - Long shear waves under the two-step coupling.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Summary

Blocks 146 and 147 (landed) worked the lattice's uniform stretch with the rescaled walk `H(k)/ℓ`, a supplied rule. Under it every walker loses energy as `1/ℓ`, a massless sea presses `ρ/3`, and stretches commute, so a filled sea stays filled. This note computes the same things under block 69's two-step coupling, the member's own source (blocks 120 and 136), at first order in a uniform isotropic stretch: `H(k) = Σ_a σ_a s_a(1 + b c_a²)`, with `1 + b = 1/ℓ`.

- **T1.** `d log E/d log ℓ = −(1 − Σ_a s_a⁴/E²)`. This lies in `(−1, 0]`: long waves lose energy as `1/ℓ`, shorter waves more slowly, and modes whose active axes all have `s² = 1` not at all at first order.
- **T2.** With block 146's dilation pressure, a walker presses `(1 − Σs⁴/E²) ρ/3`. The filled sea presses strictly between `0` and `ρ/3` of its energy density: exactly `0`, `1/12` and an exact algebraic number (about 0.09) on the tori of side 4, 6 and 8, against `1/3` for the rescaled walk.
- **T3.** `[H(b₁), H(b₂)] = 2i(b₂ − b₁)(s × w)·σ`, with `w_a = s_a c_a²`. A stretch turns a walker's coin at fixed wave number unless its active axes share one `cos²`, so a stretch history can lift walkers out of the filled sea. This happens on 240 of 512 modes on side 8, and on none on sides 4 and 6.
- **T4.** The two rules agree near every species point.

**For the third column.** How a uniform stretch acts on the walk is a supplied choice. The rescaled walk is the uniform limit of block 62's nearest-neighbour frame, and block 120 excluded that frame as a source for non-uniform modes. If one local coupling acts on every mode, the uniform stretch is the two-step one, and blocks 146 and 147's equation of state and inert sea change as above.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_UNDER_THE_TWO_STEP_COUPLING_THE_FILLED_SEA_PRESSES_BELOW_A_THIRD_OF_ITS_ENERGY_AND_A_UNIFORM_STRETCH_CAN_EXCITE_IT_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_under_the_two_step_coupling_the_filled_sea_presses_below_a_third_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block180.md`, `RESULTS_block180.md`, `CLAIM_STATUS_CERTIFICATE_block180.md` and `CHECKER_block180_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_two_step_coupling_the_filled_sea_presses_below_a_third_2026_09_27.py
```

- The runner gives `TOTAL: PASS=17 FAIL=0` in about 4 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Differentiation; Pauli products; the cross-product identity; exact torus sums; series.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - The sea's excitation for a given stretch history.
  - The finite-stretch completion's `m_sea(ℓ)`, and block 147's turning point under it.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

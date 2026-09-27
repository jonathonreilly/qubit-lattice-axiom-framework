## Summary

Block 64 T5 found that the walk twists the bonds even in a uniform plane wave (`12/125`). This note shows the twist comes from the momentum that generates relabellings, and what a symmetric coupling does to block 178. It works within blocks 63, 64, 68, 69, 120 and 136 as landed, at first order.

- **T1: the twist is the momentum's.** On a single wave, every local current of a local momentum density is velocity times momentum, `v_a P_j`.
  - The one-step momentum `sin k` therefore forces the torque `(s_a s_j/E)(cos k_a − cos k_j)` on every local current and every local density.
  - This sharpens the placement exclusions of blocks 120 and 136.
  - The two-step momentum `½ sin 2k = E v` points along the velocity.
- **T2: a symmetric current without averaging.** The two-step momentum has a local density `P^s` whose current `K^s = (Â_a f_j + Â_j f_a)/2` is exactly conserved (a matrix-symbol identity) and symmetric at every wave vector. Block 136's symmetric stress uses an eight-neighbour average; `K^s` needs none. Its coupling to symmetric strains keeps relabellings exact at first order and has block 69 T4's uniform form, one geometry for all species.
- **T3.** Block 63's current and block 69's own current twist at an exact equal-energy pair; `K^s` does not.
- **T4: bond rotations unseen.** Through `K^s` every pure bond rotation is unseen, identically. So block 178's tie theorem, that the coin's rotation is not a bond strain, belongs to the one-step coupling.
- **T5.** With `K^s`, block 64's blind member balances every divergence-free source at leading order, and `β = 1`. This agrees with block 120.

**For the owner's third column.** Block 178's strains' energy fork is not a third-column item. It belongs to the one-step coupling, and block 178's second version (594029a423) says so. Records alone do not pick the momentum, but block 73 (species), blocks 120 and 136 (sources) and this note all favour the two-step one.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_BOND_TORQUE_BELONGS_TO_THE_MOMENTUM_AND_A_SYMMETRIC_TWO_STEP_COUPLING_DOES_NOT_SEE_BOND_ROTATIONS_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_the_bond_torque_belongs_to_the_momentum_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block179.md`, `RESULTS_block179.md`, `CLAIM_STATUS_CERTIFICATE_block179.md` and `CHECKER_block179_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_bond_torque_belongs_to_the_momentum_2026_09_27.py
```

- The runner gives `TOTAL: PASS=23 FAIL=0` in about 3 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Prior art.** Blocks 120, 136 and 138 (landed) were found mid-block. The symmetric-stress claim was narrowed to the unaveraged placement, and block 178 was corrected before any PR.
- **Imports.** Summation by parts; symbols of local forms; first-order expansion; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - Other-family referees for blocks 178 and 179.
  - The coin's rotation carried by bond rotations beyond first order.
  - Rates.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

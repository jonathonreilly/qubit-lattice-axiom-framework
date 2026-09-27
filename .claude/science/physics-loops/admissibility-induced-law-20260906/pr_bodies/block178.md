## Summary

Block 64 put a strain on every bond: nine numbers per site. Block 65 turned the coin at each site: three numbers per site. Block 65 named the next step: which variables carry the six symmetric numbers and which carry the three rotations. This note answers it within blocks 63–65 as landed.

- **T1.** On two plane waves, the response of a tie `B = Tθ` is a fixed bilinear in the tie's symbol and the pair's current. At equal energies that current is divergence-free.
- **T2 (own).** For wave vectors in an open set, the currents of equal-energy pairs span the six-dimensional divergence-free space. The proof uses six exact pairs of energy one at `q₀ = (q₁, 0, 0)`, `e^{iq₁/2} = (4 + 3i)/5`, and the implicit function theorem.
- **T3 (own).** A local linear tie of any finite reach that no bounded stationary state feels (`T†J = 0`) is a relabelling `B = d(Mθ)`, and conversely. This holds whether or not the tie is translation-invariant. The count is `3|Ball_r| = (2r+1)(2r²+2r+3)` per component. A relabelling has zero curls, so under block 64's coupling the coin's three rotations are not bond strains, and that coupling keeps nine strains plus three rotations.
  - At reaches one and two this agrees with probes #8853 and #9215. The other family (`grok-4.6`) confirmed those in #8977 and #9320.
  - The reach-one `6³` torus system is rerun mod p: rank 87 = 108 − 21.
- **T4 (harvest of #8853 (b), confirmed by #8977).** In block 64's quadratic family:
  - only the blind ratio `(1, 2, −4)` ignores bond rotations;
  - its kernel on transverse strains is the three bond rotations, so it cannot balance a bond torque;
  - every divergence-free source is balanced iff `(2c₁ − c₂)(2c₁ + c₂)(2c₁ + c₂ + c₃)(2c₁ + c₂ + 2c₃) ≠ 0`;
  - `β = c₄/(2(2c₁ + c₂ + 2c₃))`.

**Scope of the fork.** Under block 64's one-step coupling, the strains' energy can be asked for either of two things:
- blindness to bond rotations: `β = 1`, and the bond torque of stationary content is unbalanced;
- balance of every source: `β` is supplied.

The landed two-step programme (blocks 120 and 136) does not meet this fork. Its symmetric stress has no bond torque, and block 179 (pushed) shows the torque belongs to the one-step momentum. The first version of this note called the fork a third-column item and missed blocks 120, 136 and 138. That was corrected before any PR.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_NO_LOCAL_TIE_MAKES_THE_COINS_ROTATION_A_BOND_STRAIN_EVERY_TIE_STATIONARY_CONTENT_CANNOT_FEEL_IS_A_RELABELLING_AT_EVERY_REACH_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_no_local_tie_makes_the_coins_rotation_a_bond_strain_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block178.md`, `RESULTS_block178.md`, `CLAIM_STATUS_CERTIFICATE_block178.md` and `CHECKER_block178_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_local_tie_makes_the_coins_rotation_a_bond_strain_2026_09_27.py
```

- The runner gives `TOTAL: PASS=23 FAIL=0` in about 7 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Provenance.** T2 and T3 at every reach are the supervisor's own and unrefereed; an other-family referee is owed.
- **Imports.** The implicit function theorem; continuity of determinants; unique factorisation of polynomials; ranks mod p; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - Blindness at order rotation times strain, where block 65 N1.3 leaves the content's transformation open.
  - A lattice placement of block 64's family.
  - Nonlinear ties.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

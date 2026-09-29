## Summary

Block 158 (pushed) found that the walker which sees only the member's lengths needs the coin-scalar term `(1/8)ε·C`, the frame's inversion-odd curl, to keep relabellings at second order. That was at `k = 0`. Block 161 (pushed) supplied it from links on the bonds. This note harvests probe HIT #9367, which asks where on the lattice the term must sit so that all eight species of the walk get what they need.

- **T1.** `ε·C = X₁ + X₂ + X₃`, split by derivative direction. Species `A` sees `s ε·C[ρEρ] = Σ_d cos(A_d) X_d` (block 70, landed), so its comparator completion is `N_A = (1/8)Σ_d cos(A_d) X_d`.
- **T2.** A hop by `m` reaches species `A` with sign `Π_d cos(A_d)^{m_d mod 2}`. By the characters of `{±1}³`, the only coin-scalar placement serving all eight species puts `X_d/8` on hops odd along axis `d` alone, the nearest-neighbour hops along each axis.
- **T3.** With weight `(1/8)ε·C`, a site term or face diagonals serve `k = 0` only, and the body diagonal serves `k = 0` and `(π, π, π)`. With free weights, even-degree classes never serve a corner and its antipode together unless their need is zero.
- **T4.** On the lengths' frame every `X_d` vanishes at first order, but block 161's per-axis link scalars do not. The six mixed species receive a spurious first-order scalar (`−1` at `(π, 0, 0)` for the jet `∂₃η₁₂ = 1`).

"Needs" is the comparator completion of each species' own frame, by definition, not a relabelling requirement. The note works at long wavelength and covers coin-scalar placements with smooth weights only.

Provenance:
- derived by a Claude Opus 5.5 probe worker (HIT #9367);
- refereed by Claude Sonnet 5, same vendor family, which counts under the owner's ruling of 2026-09-28 (confirmed with scope corrections, all applied);
- harvested by the supervisor with its own runner.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_EACH_SPECIES_NEEDS_THE_INVERSION_ODD_CURL_SPLIT_BY_DERIVATIVE_DIRECTION_ONLY_PER_AXIS_HOPS_CARRYING_EACH_AXIS_PART_SERVE_ALL_EIGHT_BOUNDED_THEOREM_NOTE_2026-09-28.md`
- Runner: `scripts/admissibility_rule_each_species_needs_the_inversion_odd_curl_split_by_derivative_direction_2026_09_28.py`, with its cache
- Pack: `GOAL_block196.md`, `RESULTS_block196.md`, `CLAIM_STATUS_CERTIFICATE_block196.md` and `CHECKER_block196_findings.md`, plus appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_each_species_needs_the_inversion_odd_curl_split_by_derivative_direction_2026_09_28.py
```

- The runner gives `TOTAL: PASS=14 FAIL=0` in about 2 s.
- Mutation census 8/8.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

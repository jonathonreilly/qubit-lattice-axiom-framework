## Summary

Block 184 (pushed) found the stretch rule under which every wave slows as a free particle does (block 185). It has hops of every length at every stretch `ℓ ≠ 1`, decaying exponentially, at a rate block 184 did not compute. A same-family strategy lens named the rate as the decisive locality test. This note computes it, within block 69's coupling (landed).

- **T1.** With `M = 2k`, `E = 2k₀` and `e = 1 − ℓ²`, the rule is the inversion relation `M = E − e sin E` (Kepler's equation). The slope of the squared energy is `sin E = Σ (2/(ne)) J_n(ne) sin(nM)`. This is checked through order `e⁷` by exact inversion.
- **T2.** The nearest singularity is the fold `1 − e cos E = 0`, at `|Im M| = κ = arccosh(1/|e|) − √(1 − e²)`. So the hops of range `2n` decay like `exp(−nκ)`.
- **T3.** `κ > 0` at every `0 < ℓ² < 2`, and at `ℓ = 1` the reach is finite. `κ` depends only on `|1 − ℓ²|`. It is `ln(2/|e|) − 1 + O(e²)` near `ℓ = 1`, and `s³/3 + …` with `s = √(1 − e²)` near the ends, where the decay length diverges.

**For the owner's third column (the coupling axis).** The rule is a local law at every stretch inside its range. It is not uniformly local: its reach grows without bound near `√2`.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_STRETCH_RULES_HOPS_DECAY_EXPONENTIALLY_BELOW_ROOT_TWO_AND_ITS_DECAY_LENGTH_DIVERGES_ONLY_AT_THE_RULES_ENDS_BOUNDED_THEOREM_NOTE_2026-09-28.md`
- Runner: `scripts/admissibility_rule_the_stretch_rules_hops_decay_exponentially_2026_09_28.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block189.md`, `RESULTS_block189.md`, `CLAIM_STATUS_CERTIFICATE_block189.md` and `CHECKER_block189_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_stretch_rules_hops_decay_exponentially_2026_09_28.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0`.
- Mutation census 6/6: four in families A–D and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Kepler's equation and its Bessel series; Carlini's formula; the inversion series; analytic-strip decay; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - The walk's own decay rates.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

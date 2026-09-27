## Summary

This harvests probe #9018 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9341 (`grok-4.6`). The note works within blocks 59, 60 and 69, all landed, and the ray model of the principal symbol.

- **T1.** A massless ray crossing the one-body gradient bends `A[1 + ρ(R − 1)]` times a slow body's fall, with `R = 1 + 2w/(w + w₀)`.
- **T2.** For the frame (block 60's crossing), `A = Σ n_a² cos 2k_a ≤ 1` and `ρ = 1`. So the ratio is at most `R < 3`, short off-axis waves bend less (a diagonal at `tan(κ/2) = 3/10` has `A = 4681/11881`), and no wave outruns `w/ℓ`.
- **T3.** For block 69's reach-three coupling, completed as `1 + b = 1/ℓ`:
  - axis waves outrun `w/ℓ` wherever `ℓ > 7/6`, reaching `(19/6)√(19/45) ≈ 2.06` times it at `ℓ = 9/4`;
  - near a strong body, a diagonal ray bends `3 + (34ℓ − 42)κ²` times the fall;
  - an exact witness, a rational function of `Qg₀`, exceeds 4.

Block 69 states that its leading order does not determine this completion. The note shows that the simplest completion breaks the single speed limit where lengths are stretched.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_AT_EVERY_WAVE_NUMBER_THE_FRAMES_RAYS_BEND_NO_MORE_THAN_LONG_WAVES_BUT_THE_REACH_THREE_COUPLING_LETS_STRETCHED_REGIONS_CARRY_FASTER_WAVES_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_at_every_wave_number_the_frames_rays_bend_no_more_than_long_waves_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block173.md`, `RESULTS_block173.md`, `CLAIM_STATUS_CERTIFICATE_block173.md` and `CHECKER_block173_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_every_wave_number_the_frames_rays_bend_no_more_than_long_waves_2026_09_27.py
```

- The runner gives `TOTAL: PASS=14 FAIL=0` in about 2 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Hamilton's equations for a principal symbol; series expansion; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** A reach-three completion that keeps `w/ℓ` the fastest speed; exact trajectories at finite wave number; sub-principal terms.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

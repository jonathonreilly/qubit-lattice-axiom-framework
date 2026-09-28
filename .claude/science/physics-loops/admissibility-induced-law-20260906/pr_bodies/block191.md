## Summary

Block 190 (pushed) found that under the free-particle stretch rule the filled sea's energy rises under fixed-volume shear, while under the frame and the reach-three completions it falls. This note follows that into the member's own equations, if the member sees the sea (the zero-of-energy row). It works within blocks 135, 147 and 150 (landed).

- **T1.** In the member's landed quadratic action a uniform traceless strain has no curvature term and no trace rate. The seen sea's `E₂ε²` is its only restoring force, so `ω² = w̄E₂/(α tr S²)`, which is `2w̄E₂/K` at `α = K/4`.
- **T2.** Under the free-particle rule `E₂ > 0` for both shear classes (exact on sides 6 and 8). The uniform shear modes acquire a real gap.
- **T3.** Under the frame the sea's second-order energy is negative for every nonzero stretch on every lattice, by the identity `(Σλ²s²)(Σs²) − (Σλs²)² = Σ_{i<j} s_i²s_j²(λ_i − λ_j)²`. The modes grow.
- **T4.** Under the reach-three completions with `q₂ = −½`, they grow too.
- **T5.** A vacuum whose energy depends only on volume has no second-order term along `det g = 1`, so it gives no gap.

- **Second version.** With block 190 T5's exact enclosures, the gap holds on the infinite lattice: `ω²K/w̄ ∈ [1/32, 7/40]` for the diagonal class and `[1/20, 3/20]` for the off-diagonal class.

**For the owner's third column (the zero-of-energy row).** Seeing the sea costs the member twice. Its kinetic term leaves the closing line (block 150, landed), and its uniform shear modes are gapped (`ω² = 2w̄E₂/K`, small only if `K ≫ E₂ ≈ 0.1` per site), or grow under the frame.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_IF_THE_MEMBER_SEES_THE_SEA_ITS_UNIFORM_SHEAR_MODES_ACQUIRE_A_GAP_UNDER_THE_FREE_PARTICLE_RULE_AND_GROW_UNDER_THE_FRAME_BOUNDED_THEOREM_NOTE_2026-09-28.md`
- Runner: `scripts/admissibility_rule_if_the_member_sees_the_sea_its_uniform_shear_modes_acquire_a_gap_2026_09_28.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block191.md`, `RESULTS_block191.md`, `CLAIM_STATUS_CERTIFICATE_block191.md` and `CHECKER_block191_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_if_the_member_sees_the_sea_its_uniform_shear_modes_acquire_a_gap_2026_09_28.py
```

- The runner gives `TOTAL: PASS=13 FAIL=0`.
- Mutation census 8/8: six in families A–F and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Euler–Lagrange equations; the Cauchy–Schwarz inequality; the matrix exponential; exact radicals.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Non-uniform waves.
  - The sea's inertia in `α`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

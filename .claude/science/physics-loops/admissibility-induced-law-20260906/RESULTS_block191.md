# Block 191 — results (2026-09-28)

- **Runner.** `scripts/admissibility_rule_if_the_member_sees_the_sea_its_uniform_shear_modes_acquire_a_gap_2026_09_28.py`: `TOTAL: PASS=13 FAIL=0`. Eight mutations (six in families A–F, two in G), each failing in its own family only.
- **T1.** `ω² = w̄E₂/(α tr S²)`, which is `2w̄E₂/K` at `α = K/4`.
- **T2.** Under the free-particle rule `E₂ > 0`, a gap.
- **T3.** Under the frame, `E₂ < 0` on every lattice (an exact inequality): growth.
- **T4.** Under the reach-three completions (`q₂ = −½`), growth.
- **T5.** A volume-only vacuum gives no gap.
- **Second version.** Cites block 190 T5's exact infinite-lattice enclosures. The gap holds on the infinite lattice, with `ω²K/w̄ ∈ [1/32, 7/40]` for the diagonal class and `[1/20, 3/20]` for the off-diagonal class.
- **Referee (2026-09-28; Claude Sonnet 5, same vendor family, separate model and session): confirmed with scope corrections.** Applied: third version, retitled "on a static background": the sea's volume dependence must be subtracted (block 147 T3); along g = 1 + eps S without it, E2 drops by c tr(S^2)/2 and the modes grow (T6, exact on side 6); T3 and T4 diagonal class only; side 4 has no gap; 2 wbar E2/K is an upper bound. Runner `TOTAL: PASS=14 FAIL=0`.

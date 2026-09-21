# Block 44 — results (2026-09-20)

- Runner `scripts/admissibility_rule_records_with_inertia_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_2026_09_20.py`: `TOTAL: PASS=15 FAIL=0`; ten mutations, each in its own family.
- T1: 42 streaming cases and 36 scattering pairs conserve number and momentum; streaming and scattering commute with the 24 rotations.
- T2: all 12636 two-record configurations of the `3³` torus balance; 1458 fail if blocked attempts do nothing, 486 under the blocked-attempt head-on rule.
- T3: `J = (1−ρ)g` at three density sets; momentum flux `(ρ/3)I` at `ρ = 3/10, 1/2, 9/10` with the exchange term `ρ²/3`; scattering carries no net momentum; speed squared `(1−ρ)/3` (six axes), `(1−ρ)/9` (sphere).
- T4: `4³` torus, two separate reflecting solids, 68076 configurations: stationary, force on each exactly zero.
- T5: three rational instances of the sphere re-drawing.
- Executed sound (side 64, density 0.3, `γ = 1`): six axes `0.464` vs `0.483`; sphere `0.277`, `0.278` vs `0.279`.
- Executed forces (sphere menu, side 96, radius 3, 8000 ticks): reflecting pair `−0.004 ± 0.020`; single capturing body `+0.007 ± 0.012`; capturing pairs `+0.237, +0.144, +0.065, +0.043, +0.023` at separations 12, 16, 24, 32, 40 with `F r² = 34, 37, 38, 44, 37` (inverse-square; estimate from T3's current: 40); emitting reflecting pairs `−0.209, −0.061, −0.004` at 12, 20, 32.

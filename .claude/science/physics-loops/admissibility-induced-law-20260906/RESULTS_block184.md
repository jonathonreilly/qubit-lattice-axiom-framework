# Block 184 — results (2026-09-27)

- **Runner.** `scripts/admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_2026_09_27.py`: `TOTAL: PASS=28 FAIL=0` in about 12 s. Nine mutations (seven in families A–F and I, two in G), each failing in its own family only.
- **T1.** The books at every stretch hold iff `p = γ(b)F∂_kF`, which is the self-consistent flow up to reparametrisation. The fixed-generator flow and the linear completion fail at every `ℓ ≠ 1`.
- **T2.** In the length, `k = k₀ + ((ℓ² − 1)/2) sin 2k₀` and `F = sin k₀ (sin² k₀ + ℓ² cos² k₀)^{1/2}`. Its second order is block 182's.
- **T3.** A real-analytic relabelling for `0 < ℓ² < 2`. No wave is faster than `1/ℓ`, per axis or in three dimensions.
- **T4.** The band-top curvature is `−1/(2 − ℓ²)`, and at `ℓ² = 2` the band top is a cusp of order `4/3`.
- **T5.** A pole of `∂_k²u` off the real line gives infinite reach at every `ℓ ≠ 1`.
- **T6.** The energy current equals the momentum per unit strain at every stretch iff `γ ≡ 1`. Then `b = (1 − ℓ²)/2`, the long-wave metric `ℓ² = 1 − 2b` is exactly linear in it, and `∂F/∂(ℓ²) = −½F(∂_kF)²`. For anisotropic diagonal stretches, `P ∥ v` alone forces this.
- **T7 (second version).** Block 181's pair-level books hold for every walk `Σ_a F_a X_a + μΓ` whose square is a number, with arbitrary per-axis hops; an offset breaks them. So this family keeps exact symmetric books on pairs of waves at every stretch.
- **T8 (second version).** At fixed label momentum `d log E/d log ℓ = −ℓ²|v|² = −|u|²` for every wave, so content presses with `Σ E|u|²/(3V)` at every stretch. Block 180's first order is the `ℓ = 1` case.

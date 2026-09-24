# Referee: transparent bodies capture rate a1

Author `w-macbookpro90c72-j357b` (claude-opus-5-5). Referee `w-macbookpro90c72-j5184` (grok-4.6).

The executed capture rates are the task's numbers. The porous collisionless quadratures in the attempt were not re-integrated.

## Steps

1. **One record.** On three small bodies and three rational step laws, a forward walk that removes mass on first contact agrees with enumeration of every step sequence. The first body with weights `(1/2, 1/3, 1/6)` is captured with probability `7/9`.

2. **Face rate.** `⟨max(0, s_z)⟩ = 1/4` and `⟨|s|_1⟩ = 3/2` for the uniform sphere. Six faces at `ρ/(4√3)` equal `q₁ = ρ√3/2`. Lattice balls of radius 2–5 have `33, 123, 257, 515` sites and `78, 174, 294, 486` exposed faces. At `ρ = 0.29` the local kinetic rates round to `3.26, 7.28, 12.31, 20.34`. Against the task's `3.2, 7.8, 13.2, 21.8` the largest relative gap is under 7%. At radius 2 the kinetic rate sits above the task value; at 3, 4, and 5 it sits below.

3. **One diffusivity.** Fitting `Q ∝ R` to the task's radius-5 value `21.8` predicts `218/25 = 8.72` at radius 2, against `3.2`. The four task values give `Q/R²` in `[0.80, 0.88]`.

4. **Chords.** The density `ℓ/(2R²)` on `[0, 2R]` integrates to 1 and has mean `4R/3`. The absorbed fraction is `1 − (1 − (1+2μR)e^{−2μR})/(2μ²R²)`. With `τ = 2Rφ` the thin expansion is `1 − (9/16)τ + O(τ²)`. The crossover is `N* = (2π/3)R²`, which is `50π/3` at `R = 5`, not the integer 52.

5. **Porous arithmetic, without the quadrature.** The radius-5 ball has `1302` internal bonds. The expected exposed-face rates at `N = 51` and `164` round to `11.76` and `30.18`. The additive rates `N q₁` round to `12.81` and `41.19`. The task's `9.4` is about 27% under the additive value at `N = 51`.

## Verdict

Capture on these sizes follows the exposed faces, and one diffusivity proportional to `R` does not fit the task's solid balls. The optical-depth crossover is `(2π/3)R²`.

`HIT: confirmed`.

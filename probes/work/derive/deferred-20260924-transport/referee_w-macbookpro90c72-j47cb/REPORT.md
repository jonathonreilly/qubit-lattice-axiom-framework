# Referee: deferred-20260924-transport a1

Attempt `w-macbookpro9927a-j6ef6`. The re-draw and the viscous operator are recomputed here. The attempt's script is not imported.

The setting is block 44's sphere menu at small density: each of six bonds collides at rate `γρ`, and the re-draw is uniform on the circle orthogonal to `P = s + s'`. The first-harmonic closure and block 51's curl obstruction are used as stated there, not re-proved.

## Verdicts

**E1.** In the frame with one record on the axis, `s = P/2 + cosθ D/2 − sinθ (s₁×s₂)/|P|` is a unit vector and stays on the momentum class. Its circle average is `(1−c)/4 I + (1+3c)/(8(1+c)) PPᵀ`.

**E2.** The two routes agree for degrees `0` through `8`: the direct pair average of `P_l(s·s₁)`, and `a_l = 4∫₀¹ u P_l(u)² du`. The first six values are `2, 1, 1/2, 3/8, 9/32, 15/64`. For `2 ≤ l ≤ 20`, `a_l < 4/(2l+1) ≤ 4/5`, so every higher harmonic relaxes.

**E3.** For a general traceless symmetric matrix, the azimuth average of `PᵀBP` is `s₁ᵀBs₁ (1+c)(1+3c)/2`. The cosine average of `(1+3c)²/16` is `1/4`, so the multiplier on all five second harmonics is `a₂ = 1/2`. The stress therefore relaxes at `3γρ` in every direction.

**E4.** With that rate, `Π = −(2/(45γρ)) S` for the traceless strain `S`. On a plane wave the force is `(1/(45γρ))(∇²g + (1/3)∇ div g)`. There is no `∂ᵢ²gᵢ` term.

**E5.** `⟨|s_z|³⟩ = 1/4` and `⟨s_x²|s_z|⟩ = 1/8`. Both coefficients in the second-order axis streaming equal `√3/16`.

**E6.** `η = ν_lat/(ν_lat+ν_coll) = 45√3 γρ/(45√3 γρ+16)`. Its derivative is `720√3/(45√3 γρ+16)² > 0`, and `η → 1` as `γρ → ∞` while `η ∼ (45√3/16)γρ` as `γρ → 0`. At `(ρ,γ) = (0.1, 2)` and `(0.3, 1)`, `η` is `0.4935` and `0.5937`. An in-plane transverse wave along a face diagonal decays faster than an axial one by `ν_lat k²/2 = √3 k²/32`.

The bulk piece of the collisional force is `(1/(135γρ)) ∂ᵢ div g`, since `1/(45γρ)` times `1/3` is `1/135γρ`. The summed operator is therefore `ν(∇²gᵢ + η ∂ᵢ²gᵢ) + (1/(135γρ)) ∂ᵢ div g` with `ν = √3/16 + 1/(45γρ)`.

## What stays open

The 200000-sample re-draw was not repeated. The quoted creeping-flow ratios were not recomputed. Finite-density collisional transfer, exclusion, and block 51's curl obstruction were not re-proved. The mean-free-path prefactor in the attempt was not re-derived.

## Result

HIT: confirmed. Collisions restore a first-harmonic local law. The viscosity they add is isotropic, `1/(45γρ)`, so the lattice weight `η` stays strictly between 0 and 1 at every finite `γρ`.

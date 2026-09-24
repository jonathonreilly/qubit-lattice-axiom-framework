# Referee: odds-field sphere menu, a1

Author `w-macbookpro90c72-j00d0` (claude-opus-5-5). Referee `w-macbookpro90c72-jf237` (grok-4.6).

## Steps

1. **Spectrum.** `λ₁ = coth β − 1/β = β/3 − β³/45 + 2β⁵/945 − β⁷/4725 + …`. The recurrence gives `λ₂ = 1 − 3λ₁/β = β²/15 − 2β⁴/315 + β⁶/1575 + …`. At `β ∈ {0.3, 1, 4}`, `1 > λ₁ > … > λ₅ > 0`, and each ratio of modified Bessel functions lies in `(0, 1)`.

2. **Critical value.** `6L(β) − 1` changes sign on `[0.50855806178558212313, 0.50855806178558212315]`, and `L' = 1/β² − 1/sinh²β > 0`, so the root is unique. There `λ₂ = 0.016828 < 3/38`, so the cubic coefficient is negative and the lean is born continuously.

3. **Landau.** Substituting `λ → ρλ` and `6ρλ₁ = 1` turns the cubic into the quadratic `12λ₁² + 8λ₁λ₂ − 5λ₁ + 5λ₂`. Its root is `β_t = 0.957910880617496`, `ρ_t = 0.553095169776`. The longitudinal mass opens as `12(6L − 1)`.

4. **Mass strength.** If the neighbour factor has mean 1 and is not constant, `⟨b⁶⟩ > ⟨b⁵⟩ > 1`, so `(1−ρ)(1 − ⟨b⁵⟩/⟨b⁶⟩) > 0`.

5. **Capacities.** The walk Green function has `G(0) = 1.51638605915`, equal to Watson's product, and `G(e) = G(0) − 1`. Then `1/G(0) = 0.65946267`, two adjacent sites give `0.98387812`, distance 2 gives `1.1275724`, and the `2³` cube gives `1.8516546`.

The sector-mass grid, the spinodal densities and the `3³` cube were not rebuilt.

## Verdict

The neutral-scale ordered sea gives mass a first-order channel, with a tricritical point. The turn of the lean stays massless by the rotation symmetry. Capacities do not add.

`HIT: confirmed`.

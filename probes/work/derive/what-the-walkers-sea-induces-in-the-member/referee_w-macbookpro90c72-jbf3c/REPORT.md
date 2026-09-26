# Referee: what the walker's sea induces in the member, attempt 2

Attempt `w-macbookpro9927a-j5403` (Claude). The uniform-strain expansion and the adiabatic kinetic form are rebuilt here. The attempt's script is not imported. The floating-point `q²` kernel and the numerical `α/K` were not re-run.

Block 62 as landed supplies `H = ½ Σ_j {E^j·σ, S_j}`, `g^{ij} = Σ_a E^i_a E^j_a` and `h = −(ε+εᵀ)`. For a symmetric uniform strain, `1 − h/2 = E` and the bands are `±|(1 − h/2)s|` with `s_j = sin k_j`. The free sea is the filled lower band, `w̄ = 1`.

## Verdicts

**Step 1 — holds.** `E/N = −⟨|(1−h/2)s|⟩`. For `h = λ 1` and `1 − λ/2 > 0`, this is `−I(1 − λ/2)`. Then `det g = (1−λ/2)^{−6}`, so `(det g)^{−1/6} = 1−λ/2`.

**Step 2 — holds.** The expansion of `|(1−h/2)s|` through second order is `r − (s·hs)/(2r) + (s·h²s)/(8r) − (s·hs)²/(8r³)`. Cubic symmetry and the pointwise identities `3B+6A = I`, `3B′+6A′ = J` give

`E/N = −I + (I/6) tr h − (B/8) tr h² + (A/8)(tr h)² + ((B−3A)/8) Σ_i h_ii²`.

On traceless `h` the second order is `−(3A/8) Σ h_ii² − (B/4) Σ_{i<j} h_ij²`, with no cross term against the trace. `A` and `B` are averages of nonnegative integrands that are positive at `(π/2,π/2,0)` and `(π/2,0,0)`, so the shear form is negative definite.

**Step 3 — holds.** `c₀ + C √det g` matched to `−I(1−λ/2)` through first order forces `C = I/3` and `c₀ = −4I/3`. Order `λ²` then fails by `I/2`, because a dilation is exactly linear while `√det g = (1−λ/2)^{−3}` is not.

**Step 4 — holds.** For real unit vectors, `Tr(P₊(σ·w)P₋(σ·w))` equals `[|w|²(1+n·n′) − 2(n·w)(n′·w)]/2`. On the lower band it reduces to `|w|² − (n·w)²`.

**Step 5 — holds at the stated order.** With `Ḣ = σ·(−ḣ s/2)` and gap `2r`, the two-level excess is `|⟨+|Ḣ|−⟩|²/Δ³ = [s·ḣ²s − (s·ḣs)²/r²]/(32 r³)`. Averaging gives

`T = (1/32)[B′ tr ḣ² − A′(tr ḣ)² − (B′−3A′) Σ ḣ_ii²]`,

so `M₁ = A′/16`, `M₂ = −A′/16`, `M₃ = B′/16`. A dilation gives `T = 0`. `A′ > 0` and `B′ − A′ = ½⟨(s₁²−s₂²)²/r⁵⟩ > 0` are the same kind of integrand witness, so `M₁ ≠ 0` and the induced term is never `β = −α`. The nodes are integrable: the density is `O(1/|δ|)` in three dimensions.

**Steps 6 and 7 — the exact checks hold; the floats were not rebuilt.** The closed forms do not need the numerical values of `I, A, B, A′, B′`.

**Steps 8–10 — not confirmed.** The static `q²` kernel, the relabelling entries, and `α/K > 1/4` are floating point. The attempt already says the relabelling margin is not a proof. They are not part of the confirmed claim.

## Result

HIT: confirmed for (b) and (c) only. A uniform symmetric strain changes the sea energy per site by the formula in step 2. A dilation is exactly `−I (det g)^{−1/6}`, so the sea energy is not a multiple of `√det g`, and every shear lowers it. The induced kinetic term has `M₁ = −M₂ = A′/16`, `M₃ = B′/16`, vanishes on a dilation, and cannot have `β = −α`. The `q²` response and `α/K` stay open.

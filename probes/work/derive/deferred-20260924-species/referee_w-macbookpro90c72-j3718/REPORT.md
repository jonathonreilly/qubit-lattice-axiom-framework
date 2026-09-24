# Referee: deferred species recovery, a1

Author `w-macbookpro9927a-j45fd` (claude-opus-5-5). Referee `w-macbookpro90c72-j3718` (grok-4.6).

The even species maps and the reversal force every static level to be even, and they do not force fourfold or eightfold degeneracy. A rate field keeps the sixteen zero modes and, on a `4×2×2` torus, doubles every nonzero level.

## What was recomputed

1. **Corepresentation.** The assignment `V ↦ σ_z, σ_x, −σ_y` squares to 1, anticommutes, and satisfies `V₁₁₀ V₀₁₁ = i V₁₀₁`. For every Pauli matrix, `σ₂ conj(σ) σ₂ = −σ`, which is `Θ V Θ⁻¹ = −V`. Since `σ_y` is pure imaginary, `Θ² = −1`.

2. **Uniform `4×4×4`.** Momenta `k = π n/2` have `|h|²` equal to the number of odd coordinates. The shells have sizes `8, 24, 24, 8`, so the characteristic polynomial is `E¹⁶ (E²−1)²⁴ (E²−2)²⁴ (E²−3)⁸`. The multiplicities add to 128.

3. **Rate-field kernel.** `sin k` vanishes exactly on `{0, π}³`, eight momenta times two coins. `Φ H Φ (Φ⁻¹ ψ) = Φ H ψ`, so a positive rate field keeps those sixteen zero modes and no others.

4. **Doubling on `4×2×2`.** Over `F_1000033`, the free walk is `E¹⁶ (E²−1)⁸`. For the rate `1+3x+5y+7z` the characteristic polynomial is still divisible by `E¹⁶` exactly once at that order, and the quotient is a square `q²` with `q` squarefree and `q(0) ≠ 0`. That is eight nonzero levels, each of multiplicity exactly two.

The `4×4×4` and `6×4×4` modular certificates, and the frozen-source hashes, were not rebuilt. The algebra that stops the multiplicity at two does not depend on those sizes.

`SUMMARY: confirmed — symmetry forces doubling only, and a rate field keeps exactly sixteen zero modes.`

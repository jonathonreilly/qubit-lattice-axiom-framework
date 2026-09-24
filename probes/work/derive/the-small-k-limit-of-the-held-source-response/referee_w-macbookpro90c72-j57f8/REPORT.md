# Referee report: the small-k limit of the held-source response, attempt 2

- **Author:** `w-macbookpro90c72-j1804` (`claude-opus-5-5`).
- **Referee:** `w-macbookpro90c72-j57f8` (`grok-4.6`). Different model family.
- **Checks:** own Ward algebra and own Green sum on the 4-cube. The author's script is not called.

## The statement that survives

For every even box, every `β`, every `ε > 0` and every `k ≠ 0`,

`R̂(k) E(k) = ⟨m⟩² / (ρ(k) + ε⟨m⟩/E(k))`,

with `ρ(k) = ⟨P_b⟩ − (β/(2N E(k))) ⟨|G_⊥|²⟩`. Block 91's floor is this identity with the non-Goldstone piece dropped. Along one axis, `E(k) = |1 − e^{ik}|²` and the bond part of `G` is that phase times the longitudinal current. The limit `ρ(k) → ρ_s` is exactly the continuity at `k = 0` of the non-Goldstone current variance. Reflection positivity and the Ward identities bound `ρ(k)` and do not decide that continuity.

At order `β⁻²` on the 4-cube the coefficient `c(k)` exceeds `c_s = 0.008112` at every nonzero mode and rises to `0.010299` at `(π,π,π)`. The infinite-volume extrapolation `0.01111` and the Monte Carlo shells were not rebuilt.

## Steps

**1.** On a triangle with a pendant edge, `DF` is the weighted `s^z`, `DH` is the weighted spin current minus the field term, and `D̄(DH)` is minus the weighted bond sum.

**2.** The rotation `L` integrates to zero against 35 monomials of degree at most 4. The area and the second moment are `4π` and `4π/3`.

**3.** A `y`-twist has first derivative `−j` and second derivative `−P`. Rotating the two ends by different angles is the same as twisting the bond by the difference.

**4.** The bond current in spin-wave coordinates starts at `p₁' − p₁` minus a cubic, with no quadratic term.

**5.** The momentum Green of the bilayer, zero mode removed, inverts the 7-point laplacian on all 128 sites of the 4-cube: `Lap G = δ − 1/128`.

**6.** The two-loop sums give `c_s < c(k)` at all 63 nonzero modes, and the rise along `(1,0,0)` continues to the corner.

## Verdict

The identity and the exact obstruction survive. Whether the non-Goldstone variance is continuous at zero momentum is still open. The four-cube ordering is the finite evidence that, at order `β⁻²`, `ρ(k)` lies below `ρ_s` and the ratio rises with `k`.

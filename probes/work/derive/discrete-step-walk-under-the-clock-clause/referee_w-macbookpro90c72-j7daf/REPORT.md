# Referee: discrete-step-walk-under-the-clock-clause a3

Author `w-macbookpro90c72-jf02d` (claude-opus-5-5). Referee `w-macbookpro90c72-j7daf` (grok-4.6).

- **S1.** Follows. On a ring of 4, with four Pythagorean angles, `U†U = I` and the range is 2. On a ring of 8, `⟨up, x+4|U²|up, x⟩` is the product of the four sines, while doubling every angle keeps range 2. `(SR(π/2−ε))² = −GUG⁻¹` holds on the ring of 4.
- **S1(iii).** The two layer symbols sum to `2 cos k σ_x`. The gauge `ψ_x → i^x ψ_x` multiplies `T` by `i`, which is the shift `k → k+π/2`, and `cos(k+π/2) = −sin k`. That is twice `σ_x D` up to the sign of the branch.
- **S2.** Follows. `tr Û/2 = 1 − 2 sin²ε cos²k` and `det Û = 1`, so `sin²(ω/2) = sin²ε cos²k`.
- **S3.** Follows. `arcsin` through order `ε³` gives `ω = 2ε|cos k|(1 − ε² sin²k/6) + O(ε⁵)`.
- **S4.** Follows. The separable identity `dv/dt = −w²(f²/2)'' ∂_x u + 2v² ∂_x u` simplifies to zero identically. At `ε=0.35`, `k=0.8`, the closed `Ψ` matches a finite-difference Hamilton derivative.
- **S5.** No broken step. Vanishing on the `2R+1` nodes kills a mode in `T_R`. Power sums through `M = N(2R+2)` force every eigenvalue into the finite node set, because a new eigenvalue would have nonzero mass and unitary eigenvalues are not zero, so the Vandermonde factor `Π ζ` is safe. The characteristic polynomial is continuous on the circle and takes values in a finite set, hence is constant. Spectral projections of the constant eigenvalues then have range at most `(p−1)R`. S5b needs only the trace (`m=1`), which does lie in `T_R`; an open interval of clocks kills the exponential polynomial. The range-1 involution `H²=I` shows the conclusion is sharp.
- **S6.** The covariance half is the homogeneous bond angle. The clock half fails at `λ=2` by the matrix element in S1. The continuum limit in S6(iii) uses the stated locality and continuity; it is not a stronger claim than S5a.

`HIT: confirmed`. The 3D walk and the sideways drift are still open, as the attempt says.

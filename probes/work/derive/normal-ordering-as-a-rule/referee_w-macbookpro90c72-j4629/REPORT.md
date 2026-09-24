# Referee: normal ordering as a rule, a2

Author `w-macbookpro90c72-j8445` (claude-opus-5-5). Referee `w-macbookpro90c72-j4629` (grok-4.6).

Clauses that see only the uniform value, the first variation, and the absence of a `q = 0` second variation do not select the per-site counter-term. The counter-term is supplied.

## What was recomputed

1. **4-cube sea.** One negative branch `−√(Σ sin² k_a)` per momentum. `c₀ = −(3 + 3√2 + √3)/8`. On that grid, the mean of `sin²(k₁)/ε` is `−c₀/3`.

2. **Both counter-terms.** `T_site = c₀ Σ w` and `T_bond = (c₀/3) Σ_bonds √(w_x w_y)` have weight one. On a uniform rate both equal `E_sea`. At a uniform rate the derivative of `E_sea` with respect to one site's `u` is `c₀`. On a twisted 4-cube these were checked by diagonalising `φ H φ`.

3. **Chessboard.** `φ_x φ_y = 1` on every edge, so `E_sea` is independent of the amplitude. `R_site = N |c₀| (cosh ε − 1)` and `R_bond = 0`. The gradient member at `γ = 12/|c₀|` is `(|c₀|/6) Σ (φ_x − φ_y)²`, and `R_site = that member + R_bond`.

4. **Stiffness.** For a generic Fourier mode, `2q` not a reciprocal-lattice vector, the bond second variation in the attempt's normalisation is `(c₀/12) Σ_j (2 + 2 cos q_j)`. Then `M_bond − c₀ = (|c₀|/12) |q|²_lat`. The family `θ T_site + (1−θ) T_bond` therefore has long-wavelength stiffness `θ |c₀|/12`, and every `θ` has vanishing `q = 0` remainder. On the axis-chessboard `q = (π, 0, 0)` the cos-mode sum is `4 c₀/3`, twice the printed formula. That mode is not the long-wavelength limit.

5. **Sea on the twisted 4-cube.** For modes `(1,0,0)`, `(1,1,0)` and `(1,1,1)`, a five-point second derivative of `E_sea` equals the bond part plus the bubble `B(q) = −(1/4N) Σ (ε_{k+q} − ε_k)² (1 − d̂·d̂') / (ε + ε')`. `B(0) = 0` and `B(π,π,π) = 0`.

6. **Numbers not rebuilt at 256³.** Midpoint grids give `c₀ = −1.193804` on `32³` and `−1.193801` on `64³`. Watson's `g₀ = 1.516386059` matches `∫ e^{−t} I₀(t/3)³ dt`. On the `64³` grid, `|c₀|/12 = 0.099483` and `|c₀|/g₀ = 0.78727`.

`SUMMARY: confirmed - the counter-term is supplied; the long-wavelength stiffness is θ |c₀|/12.`

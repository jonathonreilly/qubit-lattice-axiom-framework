# spin-wave-diffusion, attempt 2 (worker w-macbookpro90c72-j8b6e, model grok-4.6)

Builds on the aligned-plane Jacobian of a3 (same problem, different route: insert block 34's `V_L` into `|M|`).
Own plan was formed before reading a3: expand `|M|` from the z-component `1 − |θ|²/2` using the exact mode sum.

## (1) The statement attempted

**Statement (PARTIAL).** Let `G_L = N^{−1} Σ_{k ≠ 0} 1/(1 − |φ(k)|²)` with `φ(k) = (1 + e^{ik_1} + e^{ik_2})/3`, `N = L²`.
Block 34 gives the linearized site variance of one transverse component as `σ² G_L`. Two components:
`E|θ_x|² = 2 σ² G_L`. Then `E[s_x · e] = 1 − σ² G_L + O(E|θ|⁴)` (the sphere constraint), and the plane average
has the same mean (by translation). Combined with a3's Jacobian `D_1 = (σ²/L²) / |M|²`,

    D_1 L² / σ² = 1 / (1 − σ² G_L)² + O(σ² G_L², N^{−1}).

`G_L` is a purely kinematic mode sum (independent of `β`). As `β → ∞` at fixed `L`, `σ² = A(3β)/(3β) → 0`, so the
ratio → 1 with explicit first correction `1 + 2 σ² G_L + O(σ⁴)`. Checked: `G_L` exactly (cyclotomic / high precision)
for `L = 4, 8, 16`; the predicted ratios at `β = 6, 12, 24, 48` for those `L`; the `β → ∞` coefficient `2 G_L`.
This does *not* yet prove the bound at the executed `L = 256` (where `G_L` grows as `log L`); that needs the
continuum Green function of `I − PP*` (block 34's `2γ log L`) with a remainder, not closed.

## (2) Steps

**Step 1 — `G_L` (CHECKED as T1).** Direct sum over the `L² − 1` nonzero modes. `1 − |φ|² =
(6 − 2 cos k_1 − 2 cos k_2 − 2 cos(k_1 − k_2))/9`. Checked by two routes: (i) real cosine formula, (ii) complex `φ`.
Values: `G_4 = 189/128`, `G_8 ≈ 2.06669`, `G_16 ≈ 2.64427`.

**Step 2 — magnetization expansion (PROVED).** `s = (θ_1, θ_2, √(1 − |θ|²)) = (θ, 1 − |θ|²/2 + O(|θ|⁴))`.
Average over the plane and over the Gaussian linearized field: `E|M · e| = 1 − σ² G_L + O(E|θ|⁴)`.
`E|θ|⁴ = O((σ² G_L)²)` for a Gaussian. ASSUMED: the linearized field's moments control the nonlinear law at large `β`
(block 35's executed structure factor → 1).

**Step 3 — insert into the Jacobian (PROVED, using a3's step 3 / the same 3×3 derivative).**
`D_1 L² / σ² = 1 / (E|M|)² + o(1) = 1/(1 − σ² G_L)² + O(σ² G_L²)`.
Checked as T2: the expansion `1/(1 − x)² = 1 + 2x + 3x² + …` at `x = σ² G_L` for the four `β` and `L = 4, 8, 16`.

**Step 4 — comparison (CHECKED as T3).** At `L = 16`, `β = 6, 12, 24, 48` the predicted `1/(1 − σ² G_{16})²` is
`1.348, 1.160, 1.077, 1.037`, against the executed `1.34, 1.14, 1.06, 1.02`. This is the first quantitative match
(the aligned-plane `1/A(3β)²` was `1.12, 1.06, 1.03, 1.01`). The executed `L` is not stated in the task; the match at
`L = 16` is evidence, not a proof that the table used `L = 16`. The `β → ∞` statement at fixed `L` is the content.

## (3) First unclosed step

Step 2's ASSUMED identification of nonlinear `|M|` with the linearized `1 − σ² G_L`, uniformly in `L` as `L → ∞`
at fixed large `β`. `G_L` diverges, so one needs `σ² log L → 0`, i.e. `β / log L → ∞`, not just `β → ∞` at fixed `L`.
The task asked for fixed `L`, which this partial does.

## (4) What would finish it

The exact Green-function asymptotic `G_L = (3/π) log L + c_0 + O(L^{−2})` (the factor 3 from `det M` of T2) plus
a remainder on `E|θ|⁴`, giving two-sided bounds `1 + 2 σ² G_L − C σ⁴ G_L² ≤ ratio ≤ 1 + 2 σ² G_L + C σ⁴ G_L²`
for `σ² G_L ≤ 1/2`.

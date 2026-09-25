# The walk's gap on the record-gas chessboard — attempt 2 of 2

Worker `w-macbookpro9927a-jfa9d` (claude-opus-5-5), unit `J-derive-the-walks-gap-on-the-record-gas-chessboard-a2`.
- **Checks:** exact, in `check.py` in this directory. Family letters (Q, S, P, W, G, N) refer to it, and only N is floating-point. It runs in a few seconds.
- **Prior attempts:** none were printed at claim time.

**Disclosure.** Block 117 (open PR #9160) harvests this machine's #9034 (`the-record-gas-chessboard-threshold:a2`). That is the source of the bound used below, out-of-step density at most 0.0897 for g ≤ 9/62500. The walk's gap is a new question.

**Sources** (pinned in family Q):
- block 79 as landed on main: the offset, the staggered term, the two clocking choices, and the line matrices;
- block 81 as landed: the gas law `z^|V| 6^|V| g^|E| Q`;
- block 117 on its branch at `24cc9059`, as the task directs;
- the task text.

## 1. Statement attempted

### Setting
- **The records.** `n_x ∈ {0, 1}`. Write `ε_x = (−1)^{x+y+z}` and `S_x = ε_x(2n_x − 1)`: `S_x = +1` in step with the A-chessboard and `−1` out of step.
- **The coupling.** The supplied coupling `c n` equals the offset `c/2` plus `m ε S`, with `m = c/2`.
- **The walk.** `H₀ = Σ_j σ_j D_j` is block 54's walk (`D_j = (i/2)(T_j − T_j†)`, symbol `Σ_j σ_j sin k_j`). With the offset removed, the operator is `K = H₀ + mεS`.
- **The clocking choice used.** `c n` is added to the unclocked walk. This is block 79 T1's model "c n AFTER clocking only the kinetic operator", which equals `H + c n` exactly when the rates follow the chessboard clock `φ = r^ε`. The other choice, clocking the whole generator, replaces `c` by `c·w` on occupied sites. It is not treated here.
- **The gas.** Block 81 without contents, at `ζ = g⁻³`.

### Question and answer
The question is whether, on typical arrangements, the spectrum of `K` stays gapped around 0, i.e. the offset.

The answer is (b): defects put states in the gap, through explicit mechanisms.
- **Walls.** For every `c`, walls carry a band down to `E_b = (√(1 + c²) − 1)/2 < |c|/2`.
- **Isolated flips.** For `|c| > c* = 1/√(2W₃) = 0.99458…`, where `W₃` is Watson's integral, isolated out-of-step sites add levels at `±ε*(c)`. These reach the offset at `c₀ ≈ 2.33`.
- **Typical arrangements.** Both kinds of defect occur on typical arrangements, with positive density.

## 2. Steps

**S1 (PROVED; CHECKED S). In-gap states live only on walls.**
- `ε` anticommutes with `H₀`, because every hop changes the parity of `x + y + z`, and `S² = 1`. Hence

  `K² = H₀² + m² + m ε[S, H₀]`, with `[S, H₀]_xy = (S_x − S_y)(H₀)_xy`.
- The commutator vanishes except on bonds joining in-step and out-of-step sites.
- With no such bond, `K² ≥ m²`, which is block 79's gap `|c|/2`.
- CHECKED exactly (Gaussian integers after scaling) on the 4³ torus for three arbitrary patterns.

**S2 (PROVED; CHECKED P). One out-of-step site.**

*The perturbation.* Flipping `S` at `x₀` adds `V = −2mε_{x₀}` at `x₀`. This has rank 2 and is scalar in the coin.

*The unperturbed resolvent.* For the perfect chessboard `K₀`, `K₀² = H₀² + m²` is scalar in the coin, and `H₀` has zero diagonal. So

  `(K₀ − E)⁻¹_{x₀x₀} = (E + mε_{x₀}) F(E) I`, with `F(E) = ∫ dk/(2π)³ · 1/(Σ sin²k_j + m² − E²)`.

CHECKED exactly on the 4³ torus at three rational `(m, E)`. There `F_L = (1/8) Σ_j C(3,j)/(j + m² − E²)`, and the Fourier-built candidate `v` satisfies `(K₀ − E)v = e_{x₀}` with `v_{x₀} = (E + mε_{x₀})F_L`.

*The level condition.* By the determinant identity for the rank-2 perturbation, the gap contains a level (doubly degenerate) iff

  `f(ε) := 2m(m + ε)F(ε) = 1`, where `ε = ε_{x₀}E`.

*Monotonicity.* `f(−m) = 0`. For `ε ∈ (−m, m)`, `f′ = 2m[F + 2ε(m + ε)F₂]` with `F₂ = ∫ 1/(Σ sin² + m² − ε²)²`. Since `F₂ ≤ F/(m² − ε²)`, for `ε < 0` we get `2|ε|(m + ε)F₂ ≤ 2|ε|F/(m + |ε|) < F`. So `f` is strictly increasing.

*Threshold.* A level exists iff `f(m) = 4m²W′ > 1`, where `W′ = ∫ dk/(2π)³ / Σ sin²k_j`.
- The substitution `q = 2k` is 8-to-1 and measure-preserving. With `sin²k = (1 − cos 2k)/2` it gives `W′ = 2W₃`, where `W₃ = ∫ dq/(2π)³ /(3 − Σ cos q_j) = 0.5054620197…` (CHECKED on grids).
- Hence the threshold **`|c| > c* = 1/√(2W₃) = 0.9945823…`**.
- Watson's closed form `W₃ = √6 Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)/(96π³)` is classical (ASSUMED; evaluated in N).

*The level itself.*
- It emerges at `E = mε_{x₀}` and crosses the gap as `c` grows.
- It reaches the offset where `2m²F(0) = 1`, at `c₀ = 2.3308…` (float N).
- Also in N: the secular value at the upper edge is `0.906` at `c = 0.95` and `1.107` at `c = 1.05`, on either side of 1.

**S3 (PROVED; CHECKED W). A planar wall.**

*The line problem.* Take the wall `S = −1` for `z ≤ 0` and `+1` for `z ≥ 1`. At transverse momenta `(0,0)` and `(π,π)`:
- the transverse terms vanish;
- `ε` couples the pair `k, k + (π,π)` through `τ_x`;
- the coin decouples, since the z-hop carries `σ₃`.

With the gauge `ψ_z = i^zφ_z`, each sector is the chain `(1/2)(φ_{z−1} + φ_{z+1}) + mS_z(−1)^zφ_z`.

*The exact bound state.*
- Its sites 0 and 1 carry the same potential `−m`.
- The even decaying solution is `φ_z = r^{⌊z/2⌋}` for `z ≥ 1`, extended by `φ_{1−z} = φ_z`, with `r = 2m − √(1 + 4m²)` and `|r| < 1`.
- Its energy is **`E = (1 + r)/2 − m = −(√(1 + c²) − 1)/2`**.
- CHECKED exactly at `c = 3/4, 4/3, 12/5`, which give `r = −1/2, −1/3, −1/5` and `E = −1/8, −1/3, −4/5`.
- The other pair sector is the negative of this operator under `φ_z → (−1)^zφ_z`. So it binds `+E_b`.

*The band.* The transverse part `T = τ_z ⊗ (σ₁ sin k_x + σ₂ sin k_y)` anticommutes with `σ₃D_z` and with the `τ_x` mass term, and `T² = sin²k_x + sin²k_y` (CHECKED symbolically). Hence the wall band is

  **`E² = E_b² + sin²k_x + sin²k_y`**,

which lies inside the gap wherever this is below `m²`. So every wall fills `E_b ≤ |E| < |c|/2` for every `c ≠ 0`, and the gap around the offset left by walls alone is `E_b`.

*CHECKED exactly by inertia counts* (realified LDLᵀ, Sylvester) on 4×4×16 slabs with two walls:

| `c` | block (0,0)/(π,π): `|E| < 0.9E_b` | block (0,0)/(π,π): `0.9E_b < |E| < 1.1E_b` | wall-free control: `|E| < 0.99m` | block `(π/2, 0)`: `|E| < 0.99m` |
|---|---|---|---|---|
| 3/4 | 0 states | 8 states | 0 states | 0 states |
| 4/3 | 0 states | 8 states | 0 states | 0 states |

The 8 states are 2 walls × 2 coins × 2 pair sectors.

**S4 (PROVED; CHECKED G). Both defects are typical in the gas.**

*The Ising form.* At `ζ = g⁻³` the content-less weight `ζ^N g^B` is, up to a constant, `g^{#unlike/2}` in `S`. The staggered field `(1/2)log ζ + (3/2)log g` vanishes (CHECKED). So the gas is the ferromagnetic Ising model with coupling `−(log g)/4 > 0`, and the FKG inequality holds for `S` (classical; ASSUMED).

*Isolated flips.*
- A flip whose six neighbours are in step has conditional probability exactly `g³/(1 + g³)`.
- With FKG and block 117's `P(S_x = −1) ≤ 0.0897` (valid for `g ≤ 9/62500`), a flip isolated within radius `R` has density `≥ g³/(1 + g³)·(0.9103)^{|B_R|−1}`. The factor is `0.569` for `R = 1` and `0.105` for `R = 2`.

*Large domains.* A cube of side `ℓ` entirely out of step has probability `≥ (g³/(1 + g³))^{ℓ³} > 0`, by FKG for decreasing events.

*Consequences* (by the standard trial-function estimate, ASSUMED: truncating an exponentially decaying eigenvector costs an error exponentially small in the truncation radius):
- an isolated flip carries a level within `e^{−κR}` of `±ε*`;
- a large domain carries levels near every energy of the wall band.

So on typical arrangements the spectrum reaches `E_b` for every `c`. For `|c| > c*` it also contains `±ε*(c)`, with density of states at least of order `g³`: two per isolated flip, from the coin.

## 3. Where the route stops

1. **Whether some gap survives around the offset is not settled.**
   - The residual gap is at most `min(E_b, |ε*(c)|)`, and it is zero at `c = c₀`, closed by point defects.
   - Other finite clusters of flips, and thick or corrugated walls, could put levels still closer. They are not enumerated here.
2. **The other clocking choice** (`H + c w n`) and wall-dependent rates are not treated.
3. **Density of states.** Only lower bounds (FKG) are given. Upper bounds would need block 117's contour sums, domain by domain.

## 4. What would finish it

- **The residual gap.** The infimum of `|E|` over all finite out-of-step patterns. One route: the Birman–Schwinger problem for clusters of 2 to 4 flips, with the resolvent kernel of S2.
- **The corrugated-wall spectrum.** Block 79 T2's odd-thickness walls need zero-mass sites, which the two-valued `S` does not have. Check whether steps in a wall act like them.
- **Upper bounds on the density of states in the gap**, from block 117's Peierls sums.

## Answer

The clocking choice is `c n` added to the unclocked walk. With it, the gap `|c|/2` does not survive on the gas's typical arrangements:
- walls of out-of-step domains carry `E² = E_b² + sin²k_x + sin²k_y` down to `E_b = (√(1+c²) − 1)/2`;
- isolated out-of-step sites, of density of order `g³`, bind doubly degenerate levels once `|c| > 1/√(2W₃) = 0.994582…`, and these reach the offset at `c₀ ≈ 2.33`.

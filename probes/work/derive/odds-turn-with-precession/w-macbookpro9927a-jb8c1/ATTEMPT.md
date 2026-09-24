# Waves of possibility's lean with precession — attempt 2 of 2

**Worker:** `w-macbookpro9927a-jb8c1` (claude-opus-5-5).

**Checks:** `check.py` in this directory has five families (Q, A, C, D, N) and runs in about 2 s. Families A, C and D are exact (sympy). Family N is floating point and labelled executed.

**Disclosures.**
- The claim tool printed no earlier attempt on this problem.
- My own units on possibility's odds fields worked on block 42's reading on the six-axis menu: #8723, #8766 and #8769 (capacities).
- None of them treats dynamics, precession or the sphere menu's turn channel.

## 1. Statement

**The setting.** Use block 42's odds on block 103's sphere menu (PR #8919):
- `K₁f(s) = ∫e^{βs·b}f(b)dσ(b)/Z`;
- `Φ(π)_x = Π_y(K₁π_y)/⟨Π_y(K₁π_y)⟩`;
- the task's supplied dynamics `dπ_x/dt = −Γ(π_x − Φ(π)_x) + Ω L_{h_x}π_x`. Here `L_h f(s) = (h × s)·∇f(s)` and `h_x` is the unit lean of `Φ(π)_x`.

**(a) Fixed points.**
- The ordered sea `F(s·n)` of block 103, `F = (K₁F)⁶/⟨(K₁F)⁶⟩`, is a fixed point for every `Ω`.
- So is the staggered sea: `F(s·n)` on one sublattice and `F(−s·n)` on the other, at `β < 0`.
- In both, every site is axially symmetric about its own target's lean, so the precession vanishes.

**(b) Exact turn frequencies of the ordered sea.**
- The turns are the site-wise infinitesimal rotations `δπ_x = F′(t)(s·τ_x)`, with `τ_x ⊥ n` and `t = s·n`.
- They form an invariant subspace of the full linearized dynamics.
- On them `τ̇ = −(Γ + Ω n×)(τ − τ̄)`, with `τ̄_x` the mean over the six neighbours.
- So the turn frequencies are exactly

  `ω(k) = (±Ω − iΓ) E(k)/6`,  with `E(k) = Σ_i(2 − 2cos k_i)`.

- The expectation in the task holds exactly, with the full distribution and not only its mean.
- These are circularly polarized waves with `ω ∝ k²` at small `k`. They have the same quality factor `Ω/Γ` at every `k`: they precess and diffuse in step.

**(c) The staggered sea (`β < 0`).**
- **Existence.** It exists exactly when `−β > β₀`, block 103's massless point with `0.5085 < β₀ < 0.5086`. The reason is that the sublattice flip `s → −s` maps it onto the ordered sea at `|β|`.
- **Turn frequencies.** Its turns obey `λ² + 2Γλ + (Γ² + Ω²)(1 − γ(k)²) = 0`, with `γ = (1/3)Σ_j cos k_j` and `e^{λt} = e^{−iωt}`. That is,

  `ω = −iΓ ± √((Γ² + Ω²)(1 − γ²) − Γ²)`.

- **Linear dispersion.** It is linear at small `k` only when `Γ = 0`. Then `ω = ±Ω√(1 − γ²) = ±Ω|k|/√3 + O(k³)`, so **`c = Ω/√3`** in lattice units.
- **With relaxation (`Γ > 0`).** The small-`k` branch is overdamped. Its slow root is diffusive, `λ = −(Γ² + Ω²)(1 − γ²)/(2Γ) + …`, with diffusion constant `(Γ² + Ω²)/(6Γ)`. Oscillation starts at `|k| ≈ √3 Γ/√(Γ² + Ω²)`. There, for `Γ ≪ Ω`, `ω ≈ ±Ω|k|/√3 − iΓ`.

**(d) Constraints on `Ω/Γ`.** None.
- The fixed points hold at every `Ω`.
- Both turn channels are stable for every `Ω/Γ`: `Re λ = −ΓE/6 ≤ 0` for the ordered sea, and `Re λ ≤ 0` for the staggered sea.

## 2. Steps

**S1 (definitions; quoted, family Q).** Block 103 supplies:
- `K₁` and `Z = sinh β/β`;
- the sea's equation;
- `β₀ ∈ (0.5085, 0.5086)`;
- T3(a), that the turn `√(1 − t²)F′(t)cos φ` has per-neighbour eigenvalue exactly `1/6`.

The dynamics is the task's supplied clause, and nothing is adopted.

**S2 (PROVED; CHECKED, family A). (a).**
- `L_n F(s·n) = F′(t)(n × s)·n = 0`, and likewise about `−n`.
- `Φ(F) = F` by definition, so `dπ/dt = 0`.
- For the staggered sea, S5's flip shows `Φ_A = F(s·n)` and `Φ_B = F(−s·n)`.

**S3 (PROVED; CHECKED, family N). The turns are invariant, and each neighbour contributes exactly 1/6.**
- Rotation covariance: `K₁` commutes with rotations, so `Φ(Rπ) = RΦ(π)`.
- Differentiate `Φ(π)_x = N Π_y K₁π_y` along an infinitesimal rotation `ω_y` of one neighbour.
  - Its derivative is `Φ_x·[δ_{ω_y}K₁F/K₁F − ⟨·⟩_Φ]`.
  - Since `F = N(K₁F)⁶`, `δ_ω log K₁F = (1/6) δ_ω log F`.
  - The mean `⟨δ_ω F/F⟩_F = ∫δ_ω F dσ` vanishes, because rotations keep the normalization.
- So a rotation of one neighbour produces exactly `1/6` of the same rotation at `x`, and the image is again a rotation. This is block 103's T3(a), reached here without its computation.
- Executed at `β = 1` on 60 order-one profiles, the per-neighbour eigenvalue is `1/6` to `8·10⁻¹⁴`.

**S4 (PROVED; CHECKED, family A). The precession of a turned site is a turn.**
- For `π = F(s·m)` with `m = n + τ` and `h = n + τ̄`: `L_hπ = F′(s·m)(h × s)·m`.
- At first order this is `F′(t) s·(n × (τ̄ − τ))`, verified symbolically with a concrete `F`.
- Here `τ̄` is the lean tilt of `Φ(π)_x`, which is `(1/6)Σ_yτ_y` by S3.
- So the turn subspace `T` is invariant under the whole linear map: relaxation, `L_n δπ` and `L_{δh}F`.
- In `T`: `τ̇ = −Γ(τ − τ̄) + Ω n × (τ̄ − τ) = −(Γ + Ωn×)(τ − τ̄)`.
- For a wave `k`, `τ̄ = γ(k)τ` with `1 − γ = E/6`. The eigenvalues are `−(Γ ∓ iΩ)E/6`, which is (b).

**S5 (PROVED; CHECKED, family N). Exact with the full distribution.** Split the `m = ±1` perturbations into `T` and a complement `C`.
- `T` is invariant (S3–S4).
- `C` maps into `C ⊕ T`: `L_n` keeps `m`, and the only new directions are the lean feeds `L_{δh}F ∈ T`.
- So the linear operator is block triangular, and its eigenvalues are those of `T` together with those of the compressed `C`.
- The turn frequencies are therefore exact eigenvalues of the full dynamics, not an approximation that keeps only the mean.
- Executed at `β = 1` with 60 order-one profiles and 120 Gauss nodes:
  - the predicted eigenvalues occur to `10⁻¹³` at `k = (0.7, 0, 0)` and `(0.4, 1.1, −0.3)`, for `(Γ, Ω) = (1, 2)` and `(1, 0.5)`;
  - every other eigenvalue is more damped: `Re ≤ −0.93`, against the turn's `−0.078` and `−0.223`. The ordered sea's turn is its slow, massless branch.

**S6 (PROVED; CHECKED, family D). The flip.**
- `λ_ℓ(−β) = (−1)^ℓλ_ℓ(β)` (symbolic for `ℓ ≤ 5`) and `P_ℓ(−t) = (−1)^ℓP_ℓ(t)`.
- So `K₁` at `−|β|` applied to `f(−s)` equals `K₁` at `|β|` applied to `f`, evaluated at `−s`.
- The staggered equations at `β < 0` are therefore the ordered sea's equations at `|β|`, sublattice by sublattice. The staggered sea exists iff `|β| > β₀`, with the same `F`.

**S7 (PROVED; CHECKED, families C and N). The staggered turns (c).**
- **Targets.** A sublattice-A site leans along `n`, and its target's lean is `n − τ̄_B`. A B site leans along `−n`, and its target's lean is `−n − τ̄_A`.
- **Precession.** The same algebra as S4 gives:
  - `τ̇_A = −(Γ + Ωn×)(τ_A + τ̄_B)`;
  - `τ̇_B = −(Γ − Ωn×)(τ_B + τ̄_A)`.
  The sense of precession flips on the sublattice that leans the other way.
- **Characteristic equation.** Per circular component it is `λ² + 2Γλ + (Γ² + Ω²)(1 − γ²) = 0`.
  - At `Γ = 0` the roots are `±iΩ√(1 − γ²)`.
  - Along an axis, `√(1 − γ²) = |k|/√3 + O(k³)`.
  - For `Γ > 0` the slow root has the expansion stated in (c).
- **Executed, `β = −1`.** The roots occur to `10⁻¹³` for `(Γ, Ω) = (1, 2)` and `(0.05, 1)`.
  - In the underdamped case the other modes also decay at about `Γ`.
  - So the staggered turn is set apart by its gapless dispersion, not by its damping.

**ASSUMED.**
- The supplied dynamics.
- Block 103's sea exists for `β > β₀`: its T2. Family N builds it at `β = 1`.
- The stability of the complement modes for every `Ω/Γ` is argued, not proved. The precession acts on them as `±iΩ` plus a feed into `T`, and their relaxation rates are `Γ(1 − 6γμ)` with the other order-one per-neighbour eigenvalues `μ < 1/6` (block 103's spectrum). It is executed at the parameters listed.

## 3. Where it stops

1. **The ordered sea's turn waves.** They are quadratic and damped at every `k`, with a fixed ratio `Ω/Γ`. They carry the precession but never outrun diffusion.
2. **The staggered sea.** It has linear waves only in the limit `Γ → 0`. With any relaxation, the longest wavelengths are overdamped.

So precession gives the turn channel oscillation, but a sound-like `ω ∝ |k|` needs both the staggered sea and `Γ ≪ Ω|k|`.

## 4. What would finish it

- A clause that fixes `Γ` against `Ω`: for example, relaxation that is itself a rotation, or `Γ` set by the records' formation rate.
- The staggered sea's other channels (`m ≠ ±1`) with precession, worked exactly.
- A source term: how a record's content off the lean (block 103 T3(b)) launches these waves.

# What the walker's sea induces in the member: no √det g, inertia only for shear, and a q² part that relabellings change

Worker `w-macbookpro9927a-j5403` (Claude Opus 5.5, `claude-opus-5-5`). The checks are in `check.py` in this directory. They run in about 15 seconds with a peak of about 300 MB. The families are:

- **Q**: the pinned sources.
- **E**: (b), exact.
- **K**: (c) and (d), exact.
- **C**: the lattice constants, floating point.
- **T**: two independent validations, floating point.
- **A**: (a), floating point.

Families E and K are exact: sympy, with rational unit vectors. Families C, T and A are floating point and marked `[float]`.

## Sources, provenance and overlap

**Source.** Block 62, as landed on main (pinned at `60c5f194`). It supplies the following, all checked verbatim by family Q:
- the generator `H = ½ Σ_j {E^j(x)·σ, S_j}`, where "the bond from `x` along `j` carries the mean of its two ends' coin vectors";
- `H(k)² = g^{ij} s_i s_j` for a uniform frame;
- `R₂`, and `F₂ = −K w̄ (u R₁ + R₂)` summed over wave vectors;
- the kinetic terms `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]` and their cubic form `M₁ Σḣ_jj² + M₂ Σ_{i<j} ḣ_ii ḣ_jj + M₃ Σ_{i<j} ḣ_ij²`, with `M₃ = 2M₁ − M₂` for the rotation-invariant one;
- "With `α = K/4` the disturbances' speed at long wavelength is the walker's top speed … nothing here forces that value."

**Other blocks.** Blocks 101, 129, 130 and 134 enter only through the task's setting, which is quoted by family Q.

**Provenance.** The claim printed no prior attempts on this problem. Three of my earlier units touch it:
- **#8749**, the sea's polarisability for the clock field. It evaluated the same constant `I = ⟨|s|⟩ = 1.19380112143` as a one-dimensional Bessel integral. Here `I` reappears as the uniform sea energy.
- **#8722**, the anisotropic state (label `w-macbookpro90c72-j5081`). It showed that the sea energy is concave along one traceless diagonal anisotropy, with exponential bond amplitudes. Part (b) here is the full second-order tensor for a linear frame, exact, and it contains that direction as a special case.
- **#8734**, the kinetic term. It found that `α = K/4` is declared and not forced. It is used here only as context.

None of these computed the induced `K`, `α` or `β`, or the relabelling test.

## Setting

**The walk and the sea.**
- The walk is block 62's framed walk on `Z³`, with `w̄ = 1`.
- The free sea fills every negative-energy state.
- For a uniform frame, `H(k) = σ·v` with `v_a = Σ_j E^j_a s_j`, where `s_j = sin k_j`. The energies are `±|v|`.

**The strain.**
- The strain is symmetric: `E = 1 + ε`, `εᵀ = ε`.
- So `h = −(ε + εᵀ) = −2ε`, and `g^{-1} = (1 − h/2)²`, block 62's convention.

**Notation.** `r = |s|` and `⟨·⟩` is the zone average.

**Lattice constants.** All are positive.

| Constant | Definition | Value `[float]` |
|---|---|---|
| `I` | `⟨r⟩` | 1.193801121430 |
| `A` | `⟨s₁²s₂²/r³⟩` | 0.104595847525 |
| `B` | `⟨s₁⁴/r³⟩` | 0.188742012094 |
| `J` | `⟨1/r⟩` | 0.910688103289 |
| `A′` | `⟨s₁²s₂²/r⁵⟩` | 0.073109602103 |
| `B′` | `⟨s₁⁴/r⁵⟩` | 0.157343496890 |

Pointwise, `Σ_{ij} s_i²s_j²/r³ = r` and `Σ_{ij} s_i²s_j²/r⁵ = 1/r`. Hence `3B + 6A = I` and `3B′ + 6A′ = J` exactly.

## (1) The statement attempted

**(b) The order-`q⁰` part, exact.**

*The formula.* For a uniform symmetric strain, the sea energy per site through second order is

`E/N = −I + (I/6) tr h − (B/8) tr h² + (A/8)(tr h)² + ((B − 3A)/8) Σ_i h_ii²`.

*Consequences.*
- **Dilations.** For `h = λ·1` the energy is exactly `−I(1 − λ/2) = −I (det g)^{−1/6}`, at every order.
- **No `√det g`.** No constant plus a multiple of `√det g` matches the sea energy. Matching orders 0 and 1 forces `C = I/3`, and then order 2 fails by `I/2`.
- **Shear.** On traceless `h` the second-order part is `−(3A/8) Σ h_ii² − (B/4) Σ_{i<j} h_ij²`. This is negative definite: the sea lowers its energy under every uniform shear. It has no cross terms with the trace.
- **Pressure.** The first-order term `(I/6) tr h` is a pressure.
- **Anisotropy.** The term `(B − 3A)/8`, with `B − 3A = −0.12505` `[float]`, is a cubic anisotropy.

**(c) The induced kinetic term, exact up to the constants.**

*The formula.* To leading adiabatic order, the sea's energy per site under a slow uniform strain rate `ḣ` is

`T = (1/32)[B′ tr ḣ² − A′(tr ḣ)² − (B′ − 3A′) Σ ḣ_ii²]`.

*In block 62's cubic form.*
- `M₁ = A′/16 = 0.0045693`;
- `M₂ = −A′/16`;
- `M₃ = B′/16 = 0.0098340` `[float]`.

A dilation has exactly zero inertia.

**(d) The comparisons.**

*`β = −α`, exact.* Block 62's `α ḣ_ijḣ_ij + β ḣ²` with `β = −α` has `M₁ = α + β = 0`. The sea's `M₁ = A′/16` is strictly positive, so the induced term is never of that kind.
- `B′ > A′` exactly.
- A rotation-invariant induced term would need `B′ = 3A′`, which would give `β/α = −1/3`.
- The lattice has `B′ − 3A′ = −0.06199` `[float]`, so the induced term is only cubic-invariant.

*`α/K`, `[float]`.* It is `0.285` to `0.386` in every transverse-traceless (TT) channel computed, all above `1/4`. So the disturbances the sea alone would carry are slower than the walker's top speed: `v² = K/(4α) = 0.65` to `0.88`.

**(a) The `q²` part, `[float]`.**
- **Not relabelling-invariant.** For `q ∥ e₃` the relabelling modes `h = n̂ξᵀ + ξn̂ᵀ` carry `q²` energy: 0.00228 for `ξ = e₁`, and 0.00395 for `ξ = e₃` (`h₃₃ = 2`). `R₂` gives exactly 0. So the `q²` part is not relabelling-invariant and does not have `R₂`'s form.
- **Stiffness.** In TT channels the stiffness `K = 8c₂/Σh_ij²` is positive but depends on direction and polarisation. It is 0.0172 and 0.0194 along `e₃`, 0.0132 and 0.0169 along `(110)`, and 0.0144 along `(111)`: a factor 1.47 overall.
- **Parts not of `R₂`'s form.** In the `q²` part: the relabelling modes, their couplings to the trace, and the TT anisotropy. In the `q⁰` part: the pressure and the negative shear term from (b).

**(e)** Not attempted.

## (2) Steps

**Step 1 (PROVED): the uniform sea.**
- By block 62's T1(a), a uniform frame gives `H(k)² = s·g^{-1}s` and bands `±|(1 − h/2)s|` for symmetric strain.
- So `E/N = −⟨|(1 − h/2) s|⟩` exactly.
- For `h = λ·1` this equals `−(1 − λ/2)⟨r⟩`. Since `det g = det(1 − h/2)^{−2}`, that is `−I(det g)^{−1/6}`.

**Step 2 (PROVED): the second-order form.**
- Expanding gives `−r + s·hs/(2r) − s·h²s/(8r) + (s·hs)²/(8r³)`.
- Cubic symmetry gives `⟨s_is_j/r⟩ = δ_ij I/3` and `⟨s_is_js_ks_l/r³⟩ = A(δδ + δδ + δδ) + (B − 3A)δ_ijkl`.
- Using `3B + 6A = I`, the result is (b)'s formula. Its trace part vanishes at second order, as Step 1 requires.
- The traceless form follows by setting `tr h = 0`. The absence of cross terms follows by expanding `h_T + μ·1`.

**Step 3 (PROVED): no multiple of `√det g`.** Write `c₀ + C(1 − λ/2)^{−3} = −I(1 − λ/2)` through order `λ²`.
- Orders 0 and 1 give `C = I/3` and `c₀ = −4I/3`.
- Order 2 then requires `(3/2)C = 0`, a contradiction.

**Step 4 (PROVED): the two-level matrix elements.**
- For unit vectors `n` and `n′`, `|⟨+,n′|σ·w|−,n⟩|² = [|w|²(1 + n·n′) − 2(n·w)(n′·w)]/2`. This comes from the trace with the projectors `(1 ± σ·n)/2`.
- For `n′ = n` it is `|w|² − (n·w)²`.

**Step 5 (PROVED at leading adiabatic order): the induced inertia.**
- *The adiabatic step.* A two-level system slowly driven from its lower state picks up the admixture `c ≈ −i⟨+|Ḣ|−⟩/Δ²`, where `Δ` is the gap. Its energy then exceeds the instantaneous ground energy by `|⟨+|Ḣ|−⟩|²/Δ³`.
- *For the sea.* With `Ḣ = σ·(−ḣs/2)` and `Δ = 2r`, this gives `T_k = [s·ḣ²s − (s·ḣs)²/r²]/(32 r³)`.
- *Averaging.* With `⟨s_is_j/r³⟩ = δ_ij J/3`, the fourth moments over `r⁵`, and `J = 3B′ + 6A′`, the average is (c)'s `T`.
- *The dilation.* `ḣ ∝ 1` gives `Ḣ ∝ H` and no interband element.
- *The comparisons.*
  - `B′ − A′ = ½⟨(s₁² − s₂²)²/r⁵⟩ > 0`, by the swap symmetry.
  - `β = −α` requires `M₁ = 0`, impossible since `A′ > 0`.
- *Convergence.* The Dirac points make the integrands behave like `1/|δ|`, which converges in three dimensions.

**Step 6 (CHECKED): families E and K.** Steps 1 to 5 are checked in sympy: the expansion, the cubic averaging, the two identities, the dilation, the `√det g` contradiction, the traceless form, the absence of cross terms, `M₁`, `M₂`, `M₃`, the dilation's zero, `B′ > A′`, and the matrix elements at rational unit vectors.

**Step 7 (CHECKED `[float]`): family C.**
- The constants come from `1/r^{2ν} = Γ(ν)^{−1}∫ t^{ν−1}e^{−tr²}dt` and `⟨e^{−t sin²k}⟩ = e^{−t/2}I₀(t/2)`. They reduce to one-dimensional integrals, evaluated by log substitution to 40 digits.
- Both identities hold to `10⁻¹²`, and a zone grid (`N = 160`) agrees to 0.2%.

**Step 8 (PROVED): the static response to `ε cos(q·x)`.**
- *The vertex.* The anticommutator gives `⟨k+q|V|k⟩ = σ·w` with `w = (1/4)ε(s(k) + s(k+q))`.
- *The energy.* The second-order energy per site is `−⟨[|w|²(ab + s·s′) − 2(s·w)(s′·w)]/(ab(a+b))⟩`, with `s′ = s(k+q)`, `a = r` and `b = |s′|`. This counts both transitions, `k → k ± q`, which give equal contributions.
- *The limit `q → 0`.* It gives half of (b)'s second order, the `cos²` mean. So the `q⁰` parts are `−B/8` for `h₁₂ = h₂₁ = 1` and `−A/2` for `h₃₃ = 2`.
- *The `q²` coefficient.* It is the zone integral of the pointwise second `q`-derivative, whose singularities go like `1/|δ|`. The region `|δ| ≲ q` changes the energy only at order `q⁴`.

**Step 9 (CHECKED `[float]`): family T, two validations.**
- *The formula.* The strained walk `E = 1 − d(h/2) cos(q·x)`, built bond by bond with the mean of the ends' coin vectors, is diagonalised exactly on the antiperiodic `6³` torus. It reproduces the formula summed over that torus to eight digits: −6.59992270 and −6.59992273 at `d = 10⁻³` and `2·10⁻³`, against −6.59992271.
- *The adiabatic step.* Direct time evolution of one `k` under a slow ramp reproduces the excess `|⟨+|Ḣ|−⟩|²/Δ³` within 1%, at two ramp rates.

**Step 10 (`[float]`): family A, the `q²` kernel.**
- *Method.* Second differences in `q` at `τ = 10⁻³`, independent of `τ` to `10⁻⁷`, on grids `N = 64` to `192`, with Richardson extrapolation in `N⁻²`.
- *Results.* The TT channels, the relabelling modes and the ratios `α/K` are as in (1).
- *Normalisation.* `K` is read off by matching the member's energy for `h cos(q·x)`. Per site that is `(1/2)(−K R₂)`, and on TT modes `R₂ = −(p²/4)Σh_ij²`, so `c₂ = (K/8)Σh_ij²`. `α` is `T/Σḣ_ij²` for the same polarisation, so `α/K = T/(8c₂)` and `v² = 2c₂/T`.
- *The kernels.* The full 6×6 kernels along `e₃`, `(110)` and `(111)` were computed as scratch exploration, not in `check.py`. The relabelling directions are non-zero in all three. `check.py` pins the two relabelling modes along `e₃`.

## (3) Where the route stops

1. **The relabelling non-invariance of the `q²` part is floating point.** Its margin is 0.00228 against grid errors below `10⁻⁵`, but it is not a proof. The per-`k` integrand for the relabelling mode has both signs, with `O(0.2)` values cancelling to `0.002`, so no pointwise argument is available. A proof would need rigorous quadrature with excised Dirac points.
2. **(c) is leading-order adiabatic perturbation theory.** The limits `ω → 0` and then `q → 0` are taken for a gapless sea with point nodes and no Fermi surface. The mass integrals converge.
3. **The shear instability.** The sea's `q⁰` response is negative on every shear. So member plus sea is unstable at long wavelengths unless the member supplies a `q⁰` term, which `R₂` does not. The TT speeds in (d) are therefore those of the `q²` parts alone.
4. **(e)**, the sea under one record per site, is not attempted.

## (4) What would finish it

1. Rigorous bounds for the relabelling entries of the `q²` kernel, by interval quadrature with singular cells, which would make (a)'s non-invariance a HIT on its own.
2. The full decomposition of the `q²` kernel into cubic invariants.
3. The sea of a relabelling-covariant coupling, such as block 63's second-neighbour strains, to see whether its `q²` part becomes invariant.
4. The record-per-site sea of (e).

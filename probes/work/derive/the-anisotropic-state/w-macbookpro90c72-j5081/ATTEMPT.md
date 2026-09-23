# J:derive:the-anisotropic-state:a1 — no global minimum for the anisotropy under a quadratic law; a metastable planar state below threshold; the anisotropic walk stays massless, and anisotropy and alternation promote each other

**Provenance.**
- Worker `w-macbookpro90c72-j5081`, model `claude-opus-5-5`, one session. The claim printed no prior attempts.
- Definitions come from four open PRs, all by the same model family and unrefereed:
  - block 59: the bond rates and their law (PR #8581);
  - block 84: the alternation's balance (#8652);
  - block 88: the anisotropy's cost `36βε²` and its sea integrand (#8665);
  - block 89: the law read in log rates, the alternation's exact mass, and the corrected thresholds (#8678).
- Block 76's free sea (#8611) is taken as the comparator reading.
- My plan (the concavity of the sea term, pointwise lower bounds for the runaway, the crossing function `R`) came before reading block 89's T4, which does the analogous thing for the alternation.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Setting.**
- **Rates and walk.** Bond amplitudes `t_j = e^{u_j}` per axis, with the traceless anisotropy `u = ε(2, −1, −1)`. The walk has `E_ε(k)² = e^{4ε}s_x² + e^{−2ε}s_⊥²`, where `s_j = sin k_j` and `s_⊥² = s_y² + s_z²`.
- **The law's cost.** In log rates it is `36βε²` per site (block 88 T1; block 89).
- **The sea.** Per site, `E_sea(ε) = −⟨E_ε(k)⟩`.
- **The balance.** `F(ε) = 36βε² + E_sea(ε)`.
- **Directions.** `ε > 0` raises one axis (towards decoupled chains). `ε < 0` raises the other two (towards decoupled planes).

**Claims.**

**(a) The balance.**
- **Exact.**
  1. `E_sea` is concave in `ε`.
  2. `F''(0) = 72β − (χ_a + 2⟨|s|⟩)`, with the pointwise integrand `(4a² + 14ab + b²)/|s|³`, where `a = s_x²` and `b = s_⊥²`. This re-derives block 89's threshold.
  3. **For every `β`, `F` has no global minimum.** `F(ε) < F(0)` for `ε ≥ max(1, (3π/8)(36β + √3))` (chains) and for `ε ≤ −max(1, 3π(36β + √3))` (planes).
  4. The critical points are the solutions of `R(ε) = 72β`, with `R(ε) = −E_sea′(ε)/ε`.
- **Executed.**
  - `E_sea‴(0) = −6.94`. `R` rises monotonically on the chains side. On the planes side it dips to `R_min = 2.593` at `ε = −0.97`. Hence three regimes:

  | `β` | isotropic `ε = 0` | towards chains (`ε > 0`) | towards planes (`ε < 0`) |
  |---|---|---|---|
  | `> 0.0593` | local minimum | small barrier, then runaway | distant barrier (`ε ≈ −2.4`), then runaway |
  | `0.0360 – 0.0593` | local maximum | runaway, no barrier | metastable planar state `ε*(β)`, then a barrier, then runaway |
  | `< 0.0360` | local maximum | runaway | runaway |

  - `ε*(β)` for the metastable planar state:

  | `β` | 0.058 | 0.055 | 0.050 | 0.045 | 0.040 |
  |---|---|---|---|---|---|
  | `ε*` | −0.027 | −0.091 | −0.204 | −0.338 | −0.528 |

  - At each `ε*` the balance lies below `F(0)`, and the barriers are at `−2.31 … −1.52`.

**(b) The walk (exact).**
- All eight species stay **massless** for every `ε`: the zeros of `E_ε` are exactly `k ∈ {0, π}³`. There is no rest energy.
- The speeds are `e^{2ε}` along the special axis and `e^{−ε}` across it. Their product is 1.
- In the planar state at `β = 0.05` the in-plane speed is `1.226` and the axial speed is `0.665`.

**(c) Anisotropy with the alternation.**
- **Exact.**
  - With per-axis alternations `t_j e^{±δ_j}`, the axis operators commute and `E² = Σ_j t_j²(sin²k_j + sinh²δ_j)`. The mass `m² = Σ_j t_j² sinh²δ_j` adds in quadrature to the anisotropic massless walk.
  - The alternation along axis `j` sets in when `α + 2β < t_j²⟨1/E_ε⟩/4`.
  - Along the runaway to chains this bound exceeds `(1/(2π)) e^{2ε} log(1 + πe^{3ε}/(2√2)) → ∞`.
- **Executed.**
  - In the planar state the two fast axes' threshold rises from `0.2276` (isotropic) to `0.2402, 0.2704, 0.3272, 0.3988, 0.5090` at `β = 0.058, 0.055, 0.050, 0.045, 0.040`.
  - Conversely, an equal alternation on the three axes raises the anisotropy's coefficient from `4.2703` to `4.3459, 4.8841, 5.8001` at `δ = 0.1, 0.3, 0.5`, i.e. its threshold `β` from `0.0593` to `0.0604, 0.0678, 0.0806`.
  - **Each instability raises the other's threshold, so they coexist whichever comes first.** Linearly, the alternation comes first when lowering `β` at fixed `α < 0.109`, and the anisotropy first at `α > 0.109` (block 89's crossing).

## 2. Steps

**S1 (PROVED; CHECKED A.concave). The sea term is concave.**
- For `a, b ≥ 0`, not both zero, put `f = a e^{4ε} + b e^{−2ε}`. Then

  `(√f)″ = (8a²X² + 28abXY + 2b²Y²)/(2f^{3/2}) ≥ 0`,  with `X = e^{4ε}`, `Y = e^{−2ε}`

  (sympy). So `E_sea = −⟨√f⟩` is concave.
- **At `ε = 0`.** The integrand of `−E_sea″` is `(4a² + 14ab + b²)/|s|³`.
- **The average.** Its difference from `9ab + 2(a + b)²`, namely `2a² + ab − b²`, has zero cyclic sum over the three axes (sympy). So the average is `9⟨s_x²s_⊥²/|s|³⟩ + 2⟨|s|⟩ = χ_a + 2⟨|s|⟩`.
- **The threshold.** Since the law's second derivative is `72β`, `F″(0) = 72β − (χ_a + 2⟨|s|⟩)`. This is block 89's threshold, re-derived pointwise.

**S2 (PROVED; CHECKED B.runaway). No global minimum, for every `β`.**
- **Pointwise bounds.** `√(e^{4ε}s_x² + e^{−2ε}s_⊥²) ≥ e^{2ε}|s_x|` and `≥ e^{−ε}|s_⊥| ≥ e^{−ε}|s_y|`. With `⟨|sin k|⟩ = 2/π` and `F(0) = −⟨|s|⟩ ≥ −√3`:

  `F(ε) − F(0) ≤ 36βε² − (2/π)e^{2ε} + √3`  and  `F(ε) − F(0) ≤ 36βε² − (2/π)e^{−ε} + √3`.
- **Chains.** For `ε ≥ 1`, `e^{2ε} ≥ (2ε)³/6`, so the first bound is negative once `(8/(3π))ε³ ≥ (36β + √3)ε²`, i.e. for `ε ≥ (3π/8)(36β + √3)`.
- **Planes.** Likewise, with `e^{η} ≥ η³/6`, the second bound is negative for `−ε ≥ 3π(36β + √3)`.
- CHECKED at rational `β` from `1/50` to 3, at the thresholds and beyond (30-digit evaluation of the resulting polynomial inequality).

**S3 (PROVED). The critical points.**
- `F′(ε) = 72βε − G(ε)`, with `G = −E_sea′ = ⟨(2e^{4ε}s_x² − e^{−2ε}s_⊥²)/E_ε⟩`.
- `G(0) = 0`: the cyclic sum of `2s_x² − s_⊥²` vanishes (block 88 T2). So the critical points other than 0 are the solutions of `R(ε) := G(ε)/ε = 72β`.
- **Endpoint values.** `R → χ_a + 2⟨|s|⟩` as `ε → 0`. `R → +∞` as `ε → ±∞`, since by S2 `G` grows like `e^{2ε}` and like `−e^{−ε}`.
- **Signs of `F′`.** For `ε < 0`, `F′ > 0` iff `R > 72β`. For `ε > 0`, `F′ > 0` iff `R < 72β`.

**S4 (executed; notes). The shape of `R`.**
- Midpoint zone grids of side 96, separable in `k_x` and `(k_y, k_z)`, give:
  - `χ_a = 1.8827` and `⟨|s|⟩ = 1.1938`, so `χ_a + 2⟨|s|⟩ = 4.2703` (block 89: `0.0593 = 4.2703/72`);
  - `E_sea‴(0) = −6.936`, so `R′(0) = −E_sea‴(0)/2 > 0`.
- **Chains side.** `R` rises monotonically on `(0.05, 2.5)`. So below threshold `F` decreases monotonically for all `ε > 0`, and above threshold it has exactly one barrier there:
  - `ε = 0.118`, height `0.00095`, at `β = 0.065`;
  - `ε = 0.427`, height `0.046`, at `β = 0.080`;
  - `ε = 0.729`, height `0.302`, at `β = 0.100`.
- **Planes side.** `R` falls to `R_min = 2.5929` at `ε = −0.97`, then rises. So for `72β ∈ (R_min, 4.2703)`, i.e. `0.0360 < β < 0.0593`, there is a local minimum `ε*(β)` and a barrier `ε**(β)`, as tabulated in §1.

**S5 (PROVED). The walk in the anisotropic state.**
- `E_ε(k) = 0` iff `s(k) = 0` (the amplitudes `t_j` are positive), i.e. `k ∈ {0, π}³`: the same eight species, with no gap for any `ε`.
- Near each species `E² = e^{4ε}κ_x² + e^{−2ε}(κ_y² + κ_z²)`, so the speeds are `e^{2ε}` and `e^{−ε}` and their product is 1.
- The sign of the linearised `s` (the species' handedness) does not depend on `ε`.

**S6 (PROVED; CHECKED C.walk). With the alternation.**
- With amplitudes `t_j e^{±δ_j}` alternating along axis `j`, each axis operator `D_j` depends only on its own coordinate's parity. So the `D_j` commute and `H² = Σ_j D_j²`, because the `σ_j` anticommute.
- By block 89 T1, `D_j²` has spectrum `t_j²(sin²k + sinh²δ_j)`. Hence `E² = Σ_j t_j²(sin²k_j + sinh²δ_j)`.
- CHECKED on the `4³` torus with `t = (2, 1/2, 1)` and `e^{δ} = (3, 1, 2)`. The lowest eigenvalue of `H²` equals `Σ t_j² sinh²δ_j = 1105/144` (floating point, to `10⁻⁹`).

**S7 (PROVED; CHECKED C.alternation). The alternation's threshold in the anisotropic state.**
- `∂²E_sea/∂δ_j²` at `δ = 0` is `−t_j²⟨1/E_ε⟩` (sympy). The `δ` Hessian is diagonal at `δ = 0`, and the law charges `2(α + 2β)δ_j²` per site per axis (block 88 T1, in log rates). So axis `j` alternates iff `α + 2β < t_j²⟨1/E_ε⟩/4`.
- **Along the chains.** `E_ε ≤ e^{2ε}|s_x| + √2 e^{−ε}` and `sin k ≤ k`, so

  `t_x²⟨1/E_ε⟩ ≥ (2/π)e^{2ε} log(1 + πe^{3ε}/(2√2))`

  (the integral is CHECKED symbolically). This diverges: along the runaway to chains the chains always alternate. That is the one-dimensional Peierls instability, recovered as a bound.

**S8 (executed; notes). The mutual promotion.**
- The fast-axis thresholds at `ε*(β)` are as in §1.
- **Anisotropy in the alternated state.** Take `δ_j = δ` on all three axes. The anisotropy's coefficient at `ε = 0` is `⟨(4a² + 14ab + b²)/(a + b)^{3/2}⟩` with `a = s_x² + sinh²δ`, `b = s_⊥² + 2sinh²δ` (S1 with the mass included). Its first-order term still vanishes by the cyclic sum. The values are those in §1.

**ASSUMED.**
- Block 88 T1's cost `36βε²`, and block 89's reading of block 59's law as quadratic in log rates. Both are supplied clauses, as the task states.
- The midpoint zone averages of S4 and S8. They are floating point and are not certified.

## 3. The first failing step

**The route "a balance at `ε*(β)` that stops the anisotropy" fails at S2, exactly:**
- under a law quadratic in log rates, the sea's energy falls exponentially in `|ε|` on both sides, so there is no global minimum for any `β`;
- the only finite anisotropic state is a local minimum on the planes side, which exists for `0.0360 < β < 0.0593` (executed);
- towards chains there is none: below threshold the lattice slides to decoupled chains without a barrier, and along that slide the chains alternate (S7).

## 4. What would finish it

1. **The law's completion.** A law that grows at least like `e^{2|ε|}` in the anisotropy, for example the arithmetic cost of rates rather than of log rates, would bound the runaway. The lane does not supply it; block 89 finds the same for the alternation.
2. **Certified numbers.** Interval zone integration to certify `E_sea‴(0) < 0`, the monotonicity of `R` on the chains side, and `R_min = 2.593`.
3. **The joint state.** Minimise `F(ε, δ)` jointly, with the law's cost for both. By S6 the sea term is exact, and by S7–S8 the two instabilities promote each other. The joint metastable states and their first-order boundaries in the `(α, β)` plane remain to be mapped.

## 5. Running it

```
python3 probes/work/derive/the-anisotropic-state/w-macbookpro90c72-j5081/check.py
```

The run takes under a second. It makes four exact checks:
- sympy identities and inequalities;
- integer-scaled matrices on the `4³` torus.

The `note` lines are floating-point zone averages on midpoint grids.

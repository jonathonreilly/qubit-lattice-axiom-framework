# J:derive:the-small-k-limit-of-the-held-source-response:a2 — worker w-macbookpro90c72-j1804

**Model:** claude-opus-5-5.

**Check:** `python3 probes/work/derive/the-small-k-limit-of-the-held-source-response/w-macbookpro90c72-j1804/check.py`
- sympy, Fractions and numpy; about 5 s.
- K1–K6 are exact; K7–K8 are floating point and deterministic.
- K8 also reads the executed control outputs committed next to it.

**Executed controls (floating point):**
- `mc_control.py` is my own simulator of the bilayer. Its outputs are `mc_b{1,2,3}_s*.txt`.
- `b91_control_rerun.txt` is block 91's own control, rerun with new seeds and longer runs.

**Provenance.**
- No attempt on this problem was printed at claim time.
- So the plan is my own, formed after reading the block 90 and 91 notes: make block 91's Bogoliubov step an identity, then compare its remainder with the twist stiffness by spin waves.
- Overlap with my own earlier units in the same lane:
  - #8714 (the level-ordered doubled graph as a diamond lattice; a census of reflections);
  - #8716 (the held and the free sea).
  Nothing from either is used here.
- Blocks 90 and 91 are same-family work. This attempt needs a referee from another family.
- Definitions come from the block 90 and 91 notes, read on the branches of PRs #8692 and #8696 for this unit.

## 1. The exact statement attempted

**Setting** (block 90, T1–T3; block 91, T1–T3).
- The bilayer is two copies (slabs `a = 0, 1`) of `(Z/L)³`, each with nearest-neighbour bonds, joined by one rung per site. It carries the sphere menu with
  `μ ∝ exp(βH)`, `H = Σ_edges s_u·s_v + ε Σ_u s^z_u`.
- `N = L³`, and `E(k) = 6 − 2Σ_j cos k_j`.
- Block 91's response (T2) is `R̂(k) = 2β N⁻¹⟨|Ŝ^x_+(k)|²⟩`. Its floor is `⟨m⟩²/(⟨P_b⟩E + ε⟨m⟩)`, where `P_b = s^x s'^x + s^z s'^z` on a slab bond.

**Notation.**
- `L_u` is the rotation of the record at `u` taking `s^x` to `s^z`: `L s = (s^z, 0, −s^x)`.
- `D = Σ_u c_u L_u`, with `c_u = e^{ik·x_u}` equal on both slabs.
- `F = Σ_u c̄_u s^x_u = 2Ŝ^x_+(k)`.
- `G = DH`, and `j_uv = s^z_u s^x_v − s^x_u s^z_v`, the spin current of a bond.

**(a) Result.**

*The stiffness.*
- `ρ_s := ⟨P_b⟩ − (β/2N)⟨J_μ²⟩`, where `J_μ = Σ_{μ-bonds} j`.
- This is the curvature per bond of the free energy when every μ-bond is twisted by `R_y(θ)`. At `ε = 0` it equals the stiffness of twisted boundary conditions.

*The identity.* For every even `L`, every `β`, every `ε > 0` and every `k ≠ 0`, **exactly**:

```
R̂(k)E(k) = ⟨m⟩² / (ρ(k) + ε⟨m⟩/E(k)),    ρ(k) := ⟨P_b⟩ − (β/(2N E(k))) ⟨|G_⊥(k)|²⟩,
```

- `G_⊥` is the part of `G` orthogonal, in `L²(μ)`, to `F̄`.
- Block 91's floor is this identity with `G_⊥` dropped.

*The obstruction, exact.*
- For `k = κe₁`: `G = (1 − e^{iκ}) Ĵ₁(κ) − εF̄`, where `Ĵ₁(κ) = Σ_{a,x} e^{iκx₁} j_{(x,a),(x+e₁,a)}` is the longitudinal lattice current.
- The **raw** variance `(β/2N)‖Ĵ₁(κ)‖²` tends to `⟨P_b⟩` as `κ → 0` (at `ε ↓ 0`). At `κ = 0` it is `⟨P_b⟩ − ρ_s`.
- The component along the Goldstone mode `F̄` carries exactly `ρ(k)`. The remainder is `⟨P_b⟩ − ρ(k)`.
- Hence `R̂E → m*²/ρ_s` holds **if and only if the non-Goldstone remainder `κ ↦ (β/2N)‖Ĵ₁(κ)_⊥‖²` is continuous at `κ = 0`**. Equivalently, the raw current variance's jump `ρ_s` at `κ = 0` is carried entirely by the Goldstone mode.
- Reflection positivity and the rotation Ward identities give only `m² − εm/E ≤ ρ(k) ≤ ⟨P_b⟩`. They say nothing about this continuity.
- At order `β⁻²` of the low-temperature expansion the continuity holds: `c(k) → c_s` (S5).

**(b) Result.**
- `⟨P_b⟩ − ρ_s = c_s β⁻² + O(β⁻³)`, with **no `β⁻¹` term**, and `⟨P_b⟩ − ρ(k) = c(k) β⁻² + O(β⁻³)`.
- Both are explicit two-loop sums of the bilayer Green function (S4).
- `c_s = 0.011105`. `c(k)` rises from `c_s` at `k → 0` to `0.0198` at `(π,π,π)`.
- Against the executed shells (S7):
  - The order-`β⁻²` ratio rises with `k` and lies below the executed values.
  - My own bilayer simulation, whose Ward identities hold, reproduces the order-`β⁻²` shape, at 1.1–1.5 times its size. The factor approaches 1 as `β` grows, like `1 + 0.5/β`.
  - Block 91's own control, rerun with new seeds, moves by `k`-independent offsets of up to 0.004 at `β = 2`.
  - So the executed flat `1.004–1.04` is not a measurement of `⟨P_b⟩/ρ_s`.

## 2. Steps

**S1. The identity. PROVED; K1, K2 check the algebra.**

1. **Integration by parts.** The rotation `L` preserves the uniform measure on the sphere (K2), so `⟨L_uΦ⟩ = −β⟨Φ L_uH⟩` for smooth `Φ`, and by linearity the same holds for `D`.
2. **Ward identity.** `DF = Σ_u |c_u|² s^z_u = M_z` (K1). Hence `⟨FG⟩ = −⟨M_z⟩/β = −2N⟨m⟩/β`.
3. **The norm of `G`.** Applying step 1 with `D̄` to `Φ = G` gives `⟨|G|²⟩ = −⟨D̄G⟩/β`.
   - K1 gives `D̄G = −(Σ_edges |c_u − c_v|² P_uv + ε Σ_u s^z_u)`.
   - Rungs join equal phases and carry no weight.
   - The slab bonds give `|c_u − c_v|²` summing to `2N E(k)`.
   - Every slab bond carries the same `⟨P_b⟩`, by the lattice's symmetries.
   - So `⟨|G|²⟩ = 2N(E⟨P_b⟩ + ε⟨m⟩)/β`.
4. **Decomposition.** Write `G = aF̄ + G_⊥` with `⟨F G_⊥⟩ = 0`. Then `⟨FG⟩ = a⟨|F|²⟩` and `⟨|G|²⟩ = |a|²⟨|F|²⟩ + ⟨|G_⊥|²⟩`. So
   `⟨|F|²⟩ = |⟨FG⟩|² / (⟨|G|²⟩ − ⟨|G_⊥|²⟩)`,
   which is Cauchy–Schwarz with its defect written out.
5. **Normalization.** With `R̂ = (β/2N)⟨|F|²⟩` (block 91 T2, since `F = 2Ŝ_+`), step 4 gives the identity of §1.
6. **Where `G_⊥` lives.** `G`'s field term `−εF̄` lies along `F̄`, so `G_⊥ = (G_bond)_⊥`, with `G_bond = Σ_edges (c_u − c_v) j_uv`.
7. **Bounds on `ρ(k)`.**
   - `ρ(k) ≤ ⟨P_b⟩` is block 91's floor.
   - `ρ(k) ≥ m² − εm/E` follows from block 90's infrared bound `R̂E ≤ 1`.

**S2. The stiffness. PROVED; K3.**

1. **The twisted free energy.** Replace `s_u·s_v` by `s_u·R_y(θ)s_v` on every μ-bond. By K3, `∂_θ` of a bond is `−j` and `∂²_θ` is `−P`. Hence
   `−β⁻¹ ∂²_θ log Z|₀ = Σ⟨P⟩ − β(⟨J_μ²⟩ − ⟨J_μ⟩²)`.
2. **The mean current vanishes.** `⟨J_μ⟩ = 0` by the reflection `x_μ → −x_μ`, which reverses every μ-bond's current.
3. **Normalization.** Dividing by the `2N` μ-bonds gives `ρ_s`.
4. **Twisted boundary conditions.** At `ε = 0`, rotating each record by `R_y(θx_μ)` turns the uniform twist into a twist of `Lθ` on one plane of bonds (K3). So `ρ_s` is the twisted-boundary stiffness there.

**S3. The reduction. PROVED.**

1. **The current along `e₁`.** For `k = κe₁`, only the bonds along `e₁` carry `c_u − c_v ≠ 0`, and `c_u − c_v = e^{iκx₁}(1 − e^{iκ})`. So `G_bond = (1 − e^{iκ})Ĵ₁(κ)` with `E = |1 − e^{iκ}|²`. Therefore
   `(β/(2NE))‖G_⊥‖² = (β/2N)‖Ĵ₁(κ)_⊥‖²`.
2. **At `κ = 0`.** `Ĵ₁(0) = J₁` is orthogonal to `F̄(0) = M_x`, by the reflection in `x₁`. So `(β/2N)‖J₁‖² = ⟨P_b⟩ − ρ_s`.
3. **The raw variance.** By S1 step 3, `(β/(2NE))‖G‖² = ⟨P_b⟩ + εm/E`. Of this, the part along `F̄` is `ρ(k) + εm/E` and the part orthogonal is `⟨P_b⟩ − ρ(k)`.
   - Since `G_bond = G + εF̄` and `⟨FG⟩ = −2Nm/β`, the raw current variance is
     `(β/2N)‖Ĵ₁(κ)‖² = ⟨P_b⟩ − εm/E + ε²R̂/E`, which tends to `⟨P_b⟩` as `ε ↓ 0` at fixed `κ ≠ 0`.
   - At `κ = 0` it is `⟨P_b⟩ − ρ_s`. The jump is `ρ_s`.
4. **Conclusion.** In the order "`L → ∞`, then `ε ↓ 0`, then `κ → 0`", the statement `ρ(k) → ρ_s` is exactly the continuity at `κ = 0` of `(β/2N)‖Ĵ₁(κ)_⊥‖²`.
   - The same holds along any direction, with the longitudinal current `k̂·Ĵ(k)`.
   - The limit, if it exists, cannot depend on `k̂`. At order `β⁻²` this is shown in S5.
   - Nonperturbatively, continuity is a decay property of the non-Goldstone current correlations in the ordered state. The window's two tools do not reach it: the infrared bound bounds spin correlations from above, and the Ward identities of S1 are used up in defining `ρ(k)`.
   - Limits are taken along a subsequence on which the bounded quantities `⟨m⟩`, `⟨P_b⟩` and `ρ(k)` converge.
   - That `(β/2N)⟨J_μ²⟩` itself stays bounded as `L → ∞`, so that `ρ_s` has a finite limit, is a statement of the same kind at `κ = 0`. At order `β⁻²` it holds (S4).
   - This is the exact obstruction.

**S4. Order `β⁻²`. PROVED; K4, K5.**

1. **Coordinates and measure.**
   - Write `s = (π₁, π₂, σ)` with `σ = √(1 − π²)`. The measure is `dσ(s) = dπ/σ`.
   - The Gaussian part has propagator `(βΔ)⁻¹`, where `Δ` is the bilayer Laplacian with symbols `Γ_aa = (E+1)/(E(E+2))` and `Γ_{a≠b} = 1/(E(E+2))`.
   - Limits are taken as `L → ∞`, then `ε → 0`. On finite tori the symmetric zero mode is removed.
2. **Expansions** (K4):
   - `j_uv = (π₁(v) − π₁(u)) − (π_u² π₁(v) − π_v² π₁(u))/2 + O(π⁵)`;
   - `F̄ = Σ_u c_u π₁(u)` exactly;
   - `G_bond`'s linear part is `−E(k)F̄` exactly, because `c` is an eigenvector of `Δ`;
   - `J_μ`'s linear part telescopes to zero.
3. **The contracted linear parts.** The linear part left by contracting `G₃` is `(Γ₀ − Γ_b)E(k)F̄/β` (K4, exact on `4³`). `J₃`'s contracted linear part telescopes.
4. **What survives.** The normal-ordered cubic is orthogonal to `F̄` (K5). Hence
   `‖G_⊥‖² = ‖:G₃:‖²_Gauss + O(β⁻⁴)` and `‖J‖² = ‖:J₃:‖²_Gauss + O(β⁻⁴)`.
   - The Jacobian `1/σ` and the quartic terms correct the measure only at relative `O(1/β)`.
   - There is no `β⁻¹` term because every linear piece either lies along `F̄` or telescopes.
5. **The sums.** Wick's formula (K5, checked by the generating function) gives
   ```
   c_s = ½ Σ_{a,b} Σ_r [Γ_ab(r)² (2Γ_ab(r) − Γ_ab(r−2e) − Γ_ab(r+2e)) − Γ_ab(r)(Γ_ab(r−e) − Γ_ab(r+e))²],
   c(k) = (1/(2E)) Σ_{a,b} Σ_r e^{−ik·r} Σ_{e,f ∈ ±e_j} (1 − e^{ik·e})(1 − e^{−ik·f}) [Γ_ab(r)² Γ_ab(r+f−e) + Γ_ab(r)Γ_ab(r+f)Γ_ab(r−e)].
   ```
6. **ASSUMED:** that the low-temperature expansion is asymptotic for the infinite-volume ordered state. It is standard at fixed volume with `ε > 0`; uniformity in the volume is assumed. This is the scope of "strong coupling" here.

**S5. `c(k) → c_s` as `k → 0`. PROVED, given the ASSUMED decay; CHECKED numerically in K7.**

1. **The leading vertex.** Expanding `1 − e^{ik·e} = −ik·e + O(k²)` gives
   `:G₃(k): = −iΣ_j k_j J₃_j(k) + (k² remainders)`,
   with `J₃_j(k) = −½ Σ_u c_u :π_u² ∇_j π₁(u):` and `∇_j f(u) = f(u+e_j) − f(u−e_j)`.
2. **Cubic symmetry.** `⟨J₃_j J₃_l⟩(0) = δ_jl ⟨J₃_μ²⟩`: the reflection in `x_j` reverses `J₃_j` only, and the cubic group permutes the axes.
3. **Continuity.** After the antisymmetrizations the Wick terms decay like `|r|⁻⁵`, so their `r`-sums converge absolutely and uniformly in `k`. The remainders are `O(k³)` and `O(k⁴ log(1/k))` against `E ~ k²`.
4. **Conclusion.** `c(k) → (β³/2N)‖:J₃_μ:‖² = c_s`, independently of `k̂`.
5. **ASSUMED:** the lattice Green function bounds
   `|Γ(r)| ≤ C/(1+|r|)`, `|∇Γ| ≤ C/(1+|r|)²`, `|∇∇Γ| ≤ C/(1+|r|)³`
   for the symmetric branch; the antisymmetric branch decays exponentially.
6. **CHECKED (K7).** On `48³`, `c(k_min) = 0.010878` against `c_s(48) = 0.010856`.

**S6. Values. CHECKED; K6 exact, K7 floating point.**
- Exact rationals, with the zero mode removed:
  - `c_s(4) = 4019269/495452160 ≈ 0.008112`;
  - `c_s(6) ≈ 0.009199`;
  - `c(k;4)` at all 63 wave vectors, and `c(k;6)` at five.
  - The FFT code reproduces all of these to `10⁻¹⁷`.
  - Every computed `c(k)` exceeds `c_s` exactly.
- Floating point:
  - `c_s(L) = 0.010371, …, 0.010980` for `L = 16 … 96`, extrapolated to `c_s = 0.011105`;
  - on `48³`, `c(k)` rises monotonically along `(1,0,0)` and `(1,1,1)`, to `0.014242` at `(π,0,0)` and `0.019830` at `(π,π,π)`;
  - `c(k) > c_s(L)` at every `k` on `16³` and `48³`.
- With the field's mass (`ε = 0.02`, zero mode kept, `L = 16`), `c_s = 0.01069`.

**S7. Comparison with the executed window. Executed, floating point; K8.**

Ratios are `R̂E` over block 91's floor, per `|k|` shell, at `L = 16` and `ε = 0.02`.
- The executed column covers all six shells.
- The other columns cover the five shells with `|k| > 0.5`, first → last. The shell `|k| < 0.5` has only 6 modes.
- The order-`β⁻²` column uses the propagator with the field's mass, `(Δ + ε)⁻¹`, and block 91's `m`, `P_b`.

| `β` | block 91 executed (3000 levels) | order `β⁻²` | my bilayer MC | block 91's control, new seeds 1 and 2, 30000 levels |
|---|---|---|---|---|
| 1 | 1.0389 – 1.0436, flat | 1.0177 → 1.0278 | 1.0272 → 1.0377 (3 seeds) | 1.018 – 1.028; 1.019 – 1.040 |
| 2 | 1.0094 – 1.0114, flat | 1.0034 → 1.0052 | 1.0042 → 1.0059 (4 seeds) | 1.000 – 1.002; 1.004 – 1.006 |
| 3 | 1.0031 – 1.0051, flat | 1.0014 → 1.0022 | 1.0011 → 1.0023 (3 seeds) | 0.999 – 1.000; 1.001 – 1.003 |

**My simulator** (`mc_control.py`; outputs `mc_b*_s*.txt`):
- It runs heat bath plus two overrelaxation sweeps on the bilayer itself. By block 90 T1 that is the stationary law of formation.
- Each run is 40000 sweeps with the first 2000 discarded.
- **Ward identities.** In every run, `−β⟨FG⟩/⟨M_z⟩` and `β⟨|G|²⟩/(2N(E⟨P_b⟩ + εm))` equal 1 within `10⁻⁴`, averaged over `k`. So the sampler is at the stated `β`, in equilibrium.
- **Seed scatter.** Beyond the first shell it is at most `0.0006`, and at most `0.0001` in the outer shells.
- **Stiffness directly.** `β²(⟨P_b⟩ − ρ_s) = 0.0165, 0.0127, 0.0119` at `β = 1, 2, 3`, with seed scatter `≤ 0.0001`. Against `c_s(16, ε) = 0.01069` these are 1.54, 1.19, 1.11 times it, about `1 + 0.5/β`. That is the leading order plus a next order of relative size `≈ 0.5/β`.
- The shell ratios converge onto the order-`β⁻²` ones in the same way.

**The small-`k` end, tested nonperturbatively.**
- At `β = 1`, `ρ(k_min) − ρ_s = −0.0020 ± 0.0002` (3 seeds) at `k_min = 2π/16`. The order-`β⁻²` value there is `−0.00024`, so the approach to `ρ_s` at this `k` is slower than the leading order says.
- At `β = 1`, `ρ(k) < ρ_s` in every shell and every seed.
- At `β = 2, 3` the first shell is too noisy (`±0.002`) to test.
- Finite `L` and `ε` do not allow `k → 0`. This is consistent with the Goldstone limit, not a test of it.

**Reading of the table.**
- My simulation and the order-`β⁻²` ratio agree in shape: in both, the excess over 1 grows by a factor of about 1.4–1.6 from the second shell to the last. They also agree in size up to the next order.
- Block 91's executed ratios come from single 3000-level runs. They are flat and larger.
- Its own code, rerun with fresh seeds and ten times longer, moves by `k`-independent offsets of up to `0.004` (`β = 2`). At `β = 3`, one seed falls below the proven floor. So its error exceeds the effect there.
- The source sits at one site, whose local direction follows the global direction. That direction wanders slowly (maximum tilt `|m_x|/|m|` 0.16–0.31), which makes the two-copy estimate's gain a slow, `k`-independent random variable.
- Block 91's reading survives: the answer is very nearly `⟨m⟩²/(⟨P_b⟩E + ε⟨m⟩)` at every wave vector, within 4 per cent at `β = 1`. The flatness and size of its excess do not survive: they are not a measurement of `⟨P_b⟩/ρ_s`.

## 3. Where the route stops

A proof of `R̂E → m*²/ρ_s` stops at S3. What remains is the continuity at `k = 0` of the non-Goldstone current variance, in the ordered state and beyond perturbation theory. This is the precise obstruction.
- **What is not assumed:** no rule of formation, no bridge, no imported value.
- **The two ASSUMED items** are both on the strong-coupling side: the asymptotic low-temperature expansion (S4) and the Green function decay bounds (S5).
- **The executed parts** are floating point and are labelled as such.

## 4. What would finish it

1. **Summability of the non-Goldstone current correlations** in the ordered state at large `β`, for example by a controlled spin-wave or renormalization-group expansion. That gives continuity, hence `ρ(k) → ρ_s`.
2. **A one-sided inequality `ρ(k) ≤ ρ_s` for all `k`.**
   - It holds at order `β⁻²`: `c(k) > c_s` at every computed `k` (S6), with the minimum at `k_min`.
   - It holds in my simulation at `β = 1`, in every shell and seed. At `β = 2, 3` the differences are inside the noise.
   - It would sharpen block 91's floor to `m²/(ρ_s E + εm)` at every wave vector.
3. **The `β⁻³` coefficient.** My simulation suggests it is about `0.5 c_s` for the uniform current, i.e. `c₃ ≈ 0.005`, and similar for `c(k)`.
4. **A referee of another model family** for S1, S3 and S4.

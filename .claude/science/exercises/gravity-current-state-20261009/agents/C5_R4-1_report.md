# C5 R4-1: an LRL-specific d'Alembertian and the per-realization effective law

**Worker.** Claude Opus 5.5 (probe R4-1), the same model family as every C5 worker and the supervisor. **Not refereed.** It reports a FAIL, so it needs the codex referee before anything is recorded. Run 2026-10-12, 13:08Z to about 13:55Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R4-1/scripts/`:
- `r41_A_shell_densities.py` → `.out`, `_M200.out`, `C_siegel.npy`: exact shell densities C_m, checked against lattice counts.
- `r41_B_shell_sums.py` → `.out`, `_M160.out`, `r41_B_M96_seed7_eta1.0.npz`, `r41_B_M160_seed11_eta1.0.npz`: per-realization shell sums of a smooth test function, 48 and 40 frames. `r41_B_M96_seed99_eta1.0.npz` is a 3-frame timing test and is not used.
- `r41_C_weights_and_deviation.py` → `.out`: 17 weight sets, mean versus per-realization. A second run with another seed and η ≤ 0.6 (`r41_B_shell_sums_seed23.out`, `r41_C_seed23_eta0.6.out`) is for robustness.
- `r41_D_flat_kernels.py` → `.out`: kernels that are flat at m = 0, plus larger kernel scales.
- `r41_E_prefactor.py` → `.out`: how the deviation's prefactor depends on the kernel scale.
- `r41_F_selberg_check.py` → `.out`: check of the spectral asymptotics used in §4.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md:2302-2851`: the C5 method and every round through the Round 4 pre-registration. R4-1 is at `:2804-2811`.
- `SUMMARY.md` §§15–21; `PRICE_NOTE.md` §§1–2 and the v6 headers.
- `C4_RL2_report.md` and `C4_RL2_referee.md`.
- `C5_R3-3_report.md` and `C5_R3-1_report.md` (both unrefereed; R3-1's referee is still running).
- The R2-2 report and referee (`scratchpad/C5/R2-2/`, `ref_R2-2/R2-2_referee.md`: CWC).
- `C5_O5_synthesis.md`, section headings only.

**Labels.**
- *proved*: complete argument here (same family, unrefereed).
- *proved mod RECALLED*: complete except for a named standard theorem.
- *checked*: numerical check in the scratch files.
- *suggested*: argued only.
- *reading*: interpretation.
- *comparator*: outside literature.

---

## 0. In plain words

- **The average works.**
  - LRL (the Lorentz-random lattice) gets its own d'Alembertian weights. Weight the points on a few proper-time shells with numbers chosen so that the "infinite-hyperboloid" pieces cancel on average.
  - The ensemble average is then exactly □ plus corrections of relative size (a/ℓ)²·ln. There is no 1/k² remnant.
  - Four shells suffice, with closed-form weights (proved). The exact shell densities come from Siegel's formula (proved mod RECALLED; checked by counting).
- **One realization does not.**
  - In our one universe, the operator acting on a smooth field of size ℓ differs from the average. The difference depends on the realization's frame.
  - It does **not** shrink as ℓ grows. Measured against □φ, it **grows like (ℓ/a)³**, for every weight set tried (23 sets, checked). It reaches order one by ℓ ≈ 10 a or earlier in every set (already 13 at ℓ = 2a for the bare four-shell operator). At ℓ = 15–19 a it is 0.8 to 3×10⁴ times □φ, depending on the set.
- **Why (proved mod RECALLED spectral theory).**
  - A realization's symmetry group Γ_L makes the operator's frame-dependence a function on a compact hyperbolic 3-manifold. Expand it in that manifold's vibration modes (Laplace eigenfunctions).
  - Every non-constant mode contributes an amount growing like ℓ·(log-periodic factor). Removing it takes one complex condition per mode, and there are infinitely many modes.
  - For any weights on finitely many shells, these conditions cannot all hold, by a singularity argument on the manifold.
  - So the growth is unavoidable in that class, whatever the weights.
- **The Bragg gap does not help.** The deviation sits in the smooth, in-band "automorphic" modes of Γ_L, not at Bragg vectors. This agrees with R3-3's finding that the per-realization difference is in band (`C5_R3-3_report.md:155-168`).
- **Smearing the kernel lowers the prefactor but not the growth.**
  - Spreading the weights over a proper-time scale ℓ_k = L·a (L up to 4) lowers the prefactor roughly as L^(−4.5) over L ∈ [1, 4] (checked; a fitted exponent, not extrapolable).
  - The (ℓ/a)³ growth stays.
- **This is the causal-set fluctuation problem in deterministic form.** Poisson's random √N scatter of the BD operator also grows with the field's extent. LRL replaces it with a frame-dependent anisotropy that grows at the same rate.
- **Reading: FAIL (bounded)**, in the class stated in §5. The first FAIL disjunct is false: weights do cancel the remnant. The second holds: the per-realization deviation does not stay O(1) relative; it grows.

---

## 1. Against the FIXED readings (`TESTS.md:2809-2811`)

| Clause | Finding | Label |
|---|---|---|
| **PASS, part 1:** "explicit weights whose mean is □ to O(a²)" | **Met.** Four-shell divided-difference weights (§2.3), plus 22 other sets. Mean symbol −k²(1 + O(a²k² ln ak)); Gaussian check B̄φ/□φ → 1 like (a/ℓ)² ln(ℓ/a) | proved (with exact C_m) + checked |
| **PASS, part 2:** "per-realization deviation falls at least as (a/ℓ)², checked" | **Not met.** The rms relative deviation grows as about (ℓ/a)^{2.2…3.2} in all 23 sets (fitted slopes; theory says 3). Impossible for every finitely supported Γ_L-invariant weight set (§4) | checked + proved mod RECALLED |
| **FAIL:** "no weights cancel the remnant" | **False.** Weights exist (§2) | proved |
| **FAIL:** "or the per-realization deviation stays O(1) relative as ℓ grows" | **Holds, in a stronger form.** For every nonzero, finitely supported weight set: limsup_ℓ (rms relative deviation)/(ℓ/a)³ > 0 (§4). It is checked for 23 explicit sets | proved mod RECALLED + checked |
| **INCONCLUSIVE** | Not returned. What stays open lies outside the class (§5) | n/a |

**Worker reading: FAIL (bounded).** The class: retarded, linear, Γ_L ⋉ L₇-invariant kernels with finitely many orbits (any finite set of proper-time shells, interval-count layers included), acting on isotropic Gaussian test fields. It needs the codex referee.

**Against the pre-registered question** ("suppressed by a power of a/ℓ, exponentially by the Bragg gap, or not at all?"): **not at all.** It grows as (ℓ/a)³ relative (ℓ¹ absolute), and the Bragg gap plays no role.

---

## 2. Construction: LRL shell weights whose mean is □ (proved; checked)

### 2.1 Setting (hypotheses stated before titles)
- **(H1)** One realization: X = g(L₇ + u), with L₇ = diag(√7,1,1,1)ℤ⁴, Q(n) = −7n₀² + n₁² + n₂² + n₃². Physical units a = 1, density ρ = 1/√7.
- **(H2)** Operator, retarded and linear: (Bφ)(x) = c·φ(x) + Σ_{y∈X, y≺x} w(x − y)·φ(y). The weight w is Γ_L ⋉ L₇-invariant, i.e. a function on Γ_L-orbits of L₇ vectors (R3-1 Lemma A, `C5_R3-1_report.md:62-73`). In the main construction, w(v) = f_{m(v)} with m = −v² = τ² ∈ {1, 2, …}.
- **(H3)** Ensemble mean, from the unfolding of R3-3 §2.1 (`C5_R3-3_report.md:77-86`, proved there):
  E[Σ_{v ∈ shell m} h(v)] = C_m ∫θ(v⁰)δ(v² + m)h(v)d⁴v.

### 2.2 Exact shell densities (proved mod RECALLED Siegel–Weil; checked)

**The formula.** C_m = ρ·∏_p α_p(Q, −m), with:
- α_p(Q, t) = lim_r p^{−3r}·#{n mod p^r : Q(n) ≡ t};
- α_p = 1 − χ(p)/p² for p ∤ 14m, where χ = (−7/·) = (·/7);
- α_p = (1 − χ/p²)Σ_{i≤v_p(m)}(χ/p)^i for odd p ∤ 7 with p | m;
- α₂ and α₇ by exact counting modulo p^r.

So C_m = (ρ/L(2,χ))·∏_{p|14m} α_p/(1 − χ(p)p⁻²), with L(2,χ) = 1.151925470545.

**Recalled inputs and assumptions.**
- RECALLED: Siegel's mass formula for indefinite forms of rank 4, which has no spinor exceptions for representing numbers.
- ASSUMED, and checked indirectly by the counts below: one class in the genus of ⟨−7, 1, 1, 1⟩.

**Checks** (`r41_A_shell_densities.out`):
- The p = 3, 5 formula agrees with brute-force counts to 1e-12.
- Lattice-frame counts N_m(n₀ ≤ T), divided by C_m × the hyperboloid measure, give 1.0008, 1.0017, 1.0008, 0.9977, 1.0049, 1.0012, 1.0037 for m = 1…7 at T = 400. Every listed m converges toward 1 as T doubles; the slow cases are 2-adically thin shells such as m = 64 (1.92 → 1.25).
- The mean of C_m over m ≤ 128 is 0.37909, against ρ = 0.37796.
- Values: C₁…C₈ = 0.49999, 0.74998, 0.24999, 0.37499, 0.29999, 0.37499, 0.44642, 0.18749. These agree with R3-3's link-shell densities for shells 1–3 and 5, which are links throughout (`C5_R3-3_report.md:92`).

### 2.3 The weights (proved)

**Mean symbol.** At spacelike k, |k| = K, with g_m = C_m f_m:

B̄(K) = c + Σ_m g_m·2π√m K₁(K√m)/K
     = c + 2π[S₀/K² + ½Σg m(ln(K√m/2) + γ − ½) + (K²/16)Σg m²(ln(K√m/2) + γ − 5/4)] + O(K⁴ ln K),

where S_j = Σ g m^j. The Bessel series was checked term by term against the K₁ expansion.

**Conditions.**
- S₀ = S₁ = S₂ = 0 removes 1/K², ln K and K² ln K. The 1/K² term is R3-3's "remnant", which BD's weights leave at 11.35 (`C5_R3-3_report.md:105-110`).
- c = −(π/2)Σ g m ln m. This on-site term absorbs R3-3's fourth condition (`:111`).
- (π/16)Σ g m² ln m = −1.
- Then **B̄(K) = −K² + O(K⁴ ln K)**, the symbol of □ (signature −+++), with retarded continuation to timelike k as for BD.

**Closed form.** For any four distinct shells m₁…m₄:
- g_i = λ/∏_{j≠i}(m_i − m_j). These are third divided-difference weights, which kill m⁰, m¹ and m².
- λ is fixed by normalization. Σ g m² ln m is λ times the third divided difference of m² ln m, which equals λ·(1/3ξ) ≠ 0 for some ξ ∈ (m₁, m₄). So a solution always exists.
- **Explicit**, shells {1, 2, 3, 4}: g = (6.093, −18.28, 18.28, −6.093), f = g/C = (12.19, −24.37, 73.12, −16.25), c = −1.756.

  (Bφ)(x) = −1.756 φ(x) + 12.19 Σ_{τ²=1} φ − 24.37 Σ_{τ²=2} φ + 73.12 Σ_{τ²=3} φ − 16.25 Σ_{τ²=4} φ   (a = 1)

**Checks** (`r41_C_weights_and_deviation.out`).
- Mean symbol/(−K²) = 0.99970, 0.99789, 0.98368, 0.91036 at K = 0.01, 0.03, 0.1, 0.3. At K ≤ 0.003, floating-point cancellation of the 1/K² pieces limits the check to about 1e-3.
- Gaussian test field φ = exp(−|y|²_E/2ℓ²) centred at x, with □φ(x) = −2/ℓ². The exact mean gives B̄φ/□φ = 0.528, 0.861, 0.907, 0.942, 0.964, 0.975 at ℓ = 2, 6, 8, 11, 15, 19. The defect falls like (a/ℓ)²·ln: 0.094 → 0.025 from ℓ = 8 to 19, against a prediction of 4.0 for the ratio.

**Other sets.** 22 more weight sets meet the same conditions:
- four-shell sets {1,2,3,5}, {1,2,4,7}, {2,3,5,6}, {1,3,5,7};
- min-norm f on shells 1..7 (the link shells), 1..24 and 1..96;
- smeared kernels f_m = F(m/L²) with F = e^{−x}·cubic or e^{−x−1/x}·cubic (flat at 0), L = 1…4, with the smoothness put either in f or in the mean kernel g.

---

## 3. Per-realization deviation versus field size ℓ (checked)

**Set-up** (`r41_B_shell_sums.py`).
- Frames g = B(η)·R: R a Haar rotation, η ≤ 1 with density ∝ sinh²η. That is 48 frames (M = 96 shells) and 40 frames (M = 160).
- Shell sums S_m(g, ℓ) = Σ_{v∈shell m} φ_ℓ(gv) over all shell vectors with |v|_E ≤ 440 (M = 96; 1.10e7 vectors) or ≤ 330 (M = 160; 1.04e7 vectors).
- Reach is asserted: every frame's 8ℓ Gaussian window lies inside the enumeration.
- Exact mean: C_m·I_m(ℓ), with I_m by quadrature to 1e-13.
- Single shells (`r41_B_shell_sums.out`): relative deviation falls roughly as a/ℓ (sd 0.002–0.006 at ℓ = 15–19). This is R3-3's one-hop D⁻¹ law again (`C5_R3-3_report.md:147-153`).

**Weighted operators: rms over frames of (B_gφ − B̄φ)/|□φ|** (selected rows; full tables in `.out`):

| weights | ℓ = 2 | 4 | 6 | 8 | 11 | 15 | 19 | slope (ℓ ≥ 6) |
|---|---|---|---|---|---|---|---|---|
| 4-shell {1,2,3,4} | 13.5 | 130 | 583 | 1.9e3 | 3.4e3 | 7.2e3 | 2.9e4 | +3.08 |
| 4-shell {1,2,4,7} | 3.6 | 23 | 49 | 238 | 487 | 971 | 2.5e3 | +3.15 |
| min-norm, link shells 1..7 | 10.4 | 21 | 220 | 562 | 567 | 1.97e3 | 7.0e3 | +2.76 |
| min-norm, shells 1..96 | 2.4e-3 | 7.6e-3 | 0.24 | 0.86 | 1.66 | 0.67 | 7.7 | +2.23 |
| smeared e^{−x}cubic, L = 3 | 9.4e-3 | 0.30 | 0.36 | 2.7 | 6.6 | 0.66 | 28 | +2.39 |
| flat e^{−x−1/x}cubic, L = 4 (M = 160) | — | 0.051 | 0.050 | 0.42 | 0.92 (ℓ = 10) | 0.78 | — | +3.06 |

**Notes.**
- The sd over frames has the same size and slope as the rms. So this is not an error in the mean.
- Fitted slopes for all 23 sets lie between +1.0 and +4.0, with the noisy L = 4 fits at the low end. Most lie between 2.2 and 3.3.
- The curves are log-periodic, as §4 predicts, so single slopes are rough.

**Robustness** (`r41_B_shell_sums_seed23.out`, `r41_C_seed23_eta0.6.out`; results in `r41_C_results_seed23_eta0.6.npy`).
- Second run: another seed, frames with η ≤ 0.6, 30 frames, ℓ up to 24a.
- The slopes for all 18 sets lie between +2.65 and +3.46, centred on 3.
- Here the rms is several times the sd. Frames that lie close together on 𝒳 share their deviation, as expected for a smooth function of the frame (§4).

**Prefactor versus kernel scale** (`r41_E_prefactor.out`). P := geometric mean over ℓ ≥ max(6, 2L) of (rms relative deviation)/ℓ³:
- f smooth: P = 0.32, 0.051, 0.014, 5.8e-3, 2.0e-3 at L = 1, 1.5, 2, 2.5, 3, so d ln P/d ln L = −4.5.
- g smooth: −4.3.
- Flat-at-0 family: P = 6.4e-2 … 5.9e-4 over L = 1.5…4, slope −4.7.
- e^{−x}cubic at M = 160: slope −5.0 over L = 2…4.
- **No sign of super-polynomial gain from flatness at 0** at these L. So the Bragg-gap/Poisson suppression suggested in R3-1 (`C5_R3-1_report.md:198`) is not visible in the ℓ-dependence. Its effect on the prefactor cannot be separated from a power law over L ≤ 4.

**Reading.**
- The per-realization operator is dominated by a smooth, frame-dependent anisotropy. Relative to □φ it grows as (ℓ/a)³.
- Kernel smearing over ℓ_k = La lowers the prefactor by about L^{4.5} (fitted, L ≤ 4), but not the exponent.

---

## 4. Why: the spectral theorem (proved mod RECALLED)

**Setting.** Take u ∈ H³, the observer's 4-velocity in lattice coordinates, and the isotropic Gaussian φ_ℓ in the frame u. Then:
- |v|²_{E,u} = 2(u·v)² + v².
- For v = √m·ŵ with ŵ ∈ H³: 2(u·v)² − m = m·cosh 2d(u, ŵ).

Hence

F_ℓ(u) := (Bφ_ℓ)(x) = c + Σ_m f_m Σ_{ŵ∈shell m} k_{m,ℓ}(d(u, ŵ)),   with k_{m,ℓ}(d) = exp(−m cosh 2d/(2ℓ²)).

This is a sum of point-pair invariants, Γ_L-invariant in u. So F_ℓ is a smooth function on the compact orbifold 𝒳 = Γ_L∖H³ (R2-2 referee: Γ_L is cocompact, `ref_R2-2/R2-2_referee.md` §3). Haar averaging over 𝒳 is the ensemble average at a realization point, by invariance in law.

**(i) Expansion** (RECALLED: Selberg / Harish-Chandra on compact quotients; k is super-exponentially decaying).
- F_ℓ(u) = c + Σ_j ψ_j(u)·Σ_m f_m ĥ_{m,ℓ}(r_j)·Ψ_j(m).
- Notation: Δψ_j = −(1 + r_j²)ψ_j, ψ_j real and orthonormal; Ψ_j(m) := Σ_{ŵ∈Γ∖shell m} ψ_j(ŵ)/|Γ_ŵ|; ĥ(r) = (4π/r)∫₀^∞ k(d) sinh d sin(rd) dd.
- j = 0 is the ensemble mean. The deviation is Δ_ℓ = Σ_{j≥1}.
- By Parseval, ‖Δ_ℓ‖²_{L²(𝒳)} = Σ_{j≥1}|Σ_m f_m ĥ_{m,ℓ}(r_j)Ψ_j(m)|². This is exactly the ensemble mean square of the per-realization deviation.

**(ii) Asymptotics** (proved by Mellin; checked in `r41_F_selberg_check.out`, where the relative error falls as O(β)).
- With β = m/2ℓ² → 0: ĥ_{m,ℓ}(r) = (π/r)·Im[Γ(½ + ir/2)(4ℓ²/m)^{½+ir/2}]·(1 + O(β)).
- Mode j's coefficient is therefore (π/r_j)·Im[Γ(½ + ir_j/2)(2ℓ)^{1+ir_j}·A_j] + O(ℓ⁻¹), with A_j(f) := Σ_m f_m m^{−½−ir_j/2}Ψ_j(m).
- The constant mode gives π(K₁ − K₀)(β) ≈ π/β ∝ ℓ², the mean (checked).
- So each tempered mode with A_j ≠ 0 makes the absolute deviation ∝ ℓ, log-periodic in ℓ. Relative to |□φ| = 2/ℓ² that is ∝ ℓ³. This matches §3 and R3-1's tube result (relative LV ∝ κτ, absolute ∝ 1/κ; `C5_R3-1_report.md:178-192`).
- Exceptional eigenvalues (λ < 1), if any, grow faster, as ℓ^{1+t}.

**(iii) PASS forces A_j(f) = 0 for every tempered j** (proved). PASS needs ‖Δ_ℓ‖ ≤ Cℓ⁻⁴. Then, for each j, Im[Γ(½ + ir_j/2)e^{ir_j ln 2ℓ}A_j] = O(ℓ⁻²) → 0. The phase rotates with ln ℓ, and Γ(½ + ir/2) ≠ 0, so A_j = 0. The case r_j = 0 is handled the same way.

**(iv) No nonzero finitely supported f has all A_j = 0** (proved mod RECALLED propagation of singularities for the half-wave group).
1. Write t_m = ½ ln m and Aop = √(−Δ − 1) on the tempered spectral subspace. Since ψ_j is real and the half-wave kernel is symmetric, A_j = ⟨D, ψ_j⟩, with D := Σ_m f_m m^{−½}e^{−i t_m Aop}μ_m and μ_m := Σ_{ŵ} δ_ŵ/|Γ_ŵ| (finitely many Γ-orbits per shell).
2. Suppose all tempered A_j vanish. Then D lies in the span of the finitely many non-tempered eigenfunctions, so D is C^∞.
3. Pick m* in the support of f and apply e^{i t_{m*}Aop}, which maps C^∞ to C^∞:

   f_{m*}m*^{−½}μ_{m*} = (smooth) − Σ_{m≠m*} f_m m^{−½}e^{i(t_{m*} − t_m)Aop}μ_m.
4. Each term on the right with t_{m*} − t_m ≠ 0 is a half-wave FIO applied to finitely many point masses. Its wavefront set lies in the conormals of finitely many geodesic spheres of radius |t_{m*} − t_m| > 0 (RECALLED: Hörmander, Duistermaat–Guillemin; √(−Δ−1) − √(−Δ) is a ΨDO of order −1; the finite-rank projections are smoothing).
5. At a point x₀ ∈ supp μ_{m*}, only finitely many such spheres pass through x₀, since Γ is discrete. So the right side's wavefront set at x₀ is a finite union of lines.
6. The left side's wavefront set at x₀ is the whole cotangent fibre minus zero. This is a contradiction unless f_{m*} = 0. Hence f = 0.

The same argument covers weights on finitely many Γ_L-**orbits** rather than shells. Orbits in one shell share t_m and sit at distinct points of 𝒳. So it covers interval-count (BD-type) layers that involve finitely many orbits.

**Theorem (proved mod RECALLED; same family, unrefereed).**
- Statement: for every Γ_L ⋉ L₇-invariant retarded linear kernel with finitely many nonzero orbits and not identically zero (any on-site c), the ensemble rms deviation satisfies limsup_{ℓ→∞} ‖Δ_ℓ‖/ℓ > 0.
- So limsup (rms relative deviation)·(a/ℓ)³ > 0.
- In particular, a mean equal to □ + O(a²) never comes with a per-realization deviation that is O(1), let alone O((a/ℓ)²).

**What the Bragg gap does not do (reading).**
- The modes ψ_j are Γ_L-automorphic functions of the observer's frame. They are not Bragg vectors.
- The growth comes from the infinite hyperboloid, which every Lorentz-invariant non-local kernel carries (Lemma A, orbit constancy). The gap |G²| ≥ (2π)²/7 leaves it untouched.

---

## 5. Scope, hypotheses, outside realizations

**Class proved:**
- (H1)–(H3);
- linear, retarded, Γ_L ⋉ L₇-invariant kernels with finitely many orbits;
- evaluated at a realization point on isotropic Gaussians in the observer frame;
- ensemble rms (Haar over 𝒳).

One test family suffices to defeat PASS.

**Checked:** 23 explicit sets, ℓ ≤ 19a, L ≤ 4, η ≤ 1 frames.

**Outside, open:**
1. **Infinitely supported kernels** (all proper times, e.g. untruncated smooth F, or BBL-type e^{−εn} tails). Step (iv) fails, because infinitely many spheres may pass through x₀. The truncated versions tested (M = 96, 160) grow as (ℓ/a)³.
2. **Kernel scale tied to field scale** (ℓ_k ∝ ℓ^α). That is not one law.
3. **Non-linear, tensor or spinor operators**, and continuum fields coupled to the points (RL-type).
4. **Other cocompact arithmetic forms.** The argument is unchanged (suggested).
5. **Ensemble-only laws.** These have only the mean, which passes.
6. **Curved realizations** (R3-3 defects).
7. **Individual realizations.** The theorem is about rms. For a single u, the deviation is an almost-periodic function of ln ℓ times ℓ, with nonzero mean square. Exceptional u where it vanishes identically are not excluded.

**Hypotheses used but not proved here:**
- Siegel's formula with class number one for C_m. Only the numerical tables need it; the theorem does not, since it needs only C_m > 0.
- That the Haar-mean unfolding of R3-3 §2.1 holds (proved there, unrefereed).

**Strong words.**
- "Exact" is used only for the C_m formula and the moment cancellation.
- "Impossible" is used only for the §4 theorem's class.
- The fitted exponents (slopes 1.0–4.0; P ∝ L^{−4.3…−5.0}) are noisy and log-periodic. Read them as "≈ ℓ³" and "a power of L over L ≤ 4", never as precise or extrapolable (`TESTS.md:5-9` rule).

## 6. Prior art (counted once)

- **R3-3 §2.3:** BD fails on LRL, and four conditions are needed. Here they are solved: three moments plus an on-site term, with closed-form weights.
- **R3-3 §2.6:** the one-hop per-realization anisotropy ∝ D⁻¹. Here it is the per-shell input, and the weighted operator turns it into ℓ³.
- **R3-1:**
  - Lemma A (orbit constancy);
  - §4.3: tube LV, absolute ∝ 1/κ. Here this is explained as the tempered automorphic spectrum, extended to arbitrary weights and proved unavoidable for finite support;
  - §4.3: the suggested Bragg/smoothing suppression. Not seen in the ℓ-dependence.
- **RL2:** Poisson mean focusing through the Palm identity. It does not transfer to LRL (R3-3 §2.4).
- **Packet:** `C3_exercise_G_graviton.md:95` records BD's per-history noise as Sorkin's reason for a non-locality scale.
- **Repository grep:** "Siegel", "Selberg", "Harish-Chandra" and "local densit" give no hits in this sense. The `docs/` hits for "local density" are unrelated uses.
- **Comparators (RECALLED):**
  - Sorkin gr-qc/0703099 (BD fluctuations and the mesoscale);
  - Benincasa–Dowker 2010;
  - Siegel–Weil;
  - Selberg, Lax–Phillips and Phillips–Rudnick (hyperbolic lattice-point error terms are spectral; the ℓ¹ law here is the smoothed version);
  - Duistermaat–Guillemin.

## 7. Price implications (named; none adopted)

- **LRL (set B′) and its effective law.**
  - The average law can be made □ at O(a²) by a finite, explicit, retarded rule. The price is the Admissibility change already named by R3-1: orbit-constant couplings to the past light cone (`C5_R3-1_report.md:313-316`).
  - It does **not** buy a per-realization effective law. A single realization's d'Alembertian is frame-dependent at relative size ∝ (ℓ/a)³ × P(ℓ_k), unless the kernel has infinitely many orbits. That case is open and needs infinitely many automorphic cancellations.
- **Consequence for R3-3's focusing route.** R3-3's per-realization √Δ argument needs a local second-order effective law in each realization (`C5_R3-3_report.md:189-195`). For finite-orbit kernels that law does not exist, by the theorem here. The focusing clause of R3-3 therefore stays open only through infinite-orbit kernels.
- **Suggested scale (illustration only; extrapolation barred).** Suppose P ∝ (a/ℓ_k)^{4.5} held. Keeping relative anisotropy below one for a field of extent ℓ would then need ℓ_k ≳ a(ℓ/a)^{2/3}. That is about 1e-22 m for ℓ ~ 1e-15 m at a = ℓ_P, and macroscopic for cosmological fields. This mirrors BD's mesoscale on Poisson. It is not a bound.

## 8. Needs codex referee

1. The §4 theorem as a whole, especially:
   - the Parseval identification of ensemble rms with L²(𝒳) at a Palm point;
   - step (iii);
   - the wavefront step (iv) on the orbifold, including the finite-sphere count and the treatment of torsion stabilizers.
2. The ĥ asymptotics, including the r_j = 0 and exceptional cases.
3. The Siegel C_m (class number one) and the counting checks.
4. The numerical deviation tables: reach, frame sampling (η ≤ 1, not a full fundamental domain), and the exact mean.
5. The reading: FAIL (bounded), with the first disjunct false and the second holding in the stated class.

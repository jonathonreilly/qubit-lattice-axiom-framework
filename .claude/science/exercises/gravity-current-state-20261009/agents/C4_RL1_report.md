# C4 lane RL, probe L1: weighted, multi-hop and operator-inverse link readouts on a curved sprinkling (worker report)

**Worker:** Claude Opus 5.5 (probe L1), the same model family as the exercise authors. **Unrefereed.** Worked 17:34–18:15Z on 2026-10-11. OMP_NUM_THREADS=2; every run took under 1 minute except one zero-locator, which took about 10 minutes. No repository file was edited.

**Read in full:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`;
- in TESTS.md: the C4 fourth wave, Lane RL, and the G-L registration and results;
- `C3_G-L_report.md` and `C3_G-L_referee.md`;
- `E1p_report.md` and `E1p_b_referee.md`;
- the G-L scratch scripts (`gl_A`, `gl_B`, `v2_conformal_quad`);
- `scripts/E1p/E1p_5_mean4d.py` and `e1p_core.py`. I reused the E1′ Volterra convolution and the G-L quadrature.

**Read in part:** `E1p_referee.md` §§1–3, plus the head of `C3_G-B_report.md` and `C3_G-B_referee.md`.

## Verdict (worker): FAIL, bounded to the readout classes tested

No tested readout meets PASS: an order-only readout whose mean gives √Δ, with noise bounded at physical parameters.

| class | mean on a curved sprinkling | noise | status |
|---|---|---|---|
| (a) Johnston multi-hop link sums (massless and massive-limit) | direct cone weight stays ν^{-1/2}: link/GR = (νΔ)^{-1/2}, as in G-L | no compounding (E1′) | **FAIL, mean.** Proved at needle order |
| (b) links weighted by interval volume or count, w(ρV)·L, layer kernels | (νΔ)^{-1/2} for every weight | as E1′ | **FAIL, mean.** Proved; checked |
| (c) Benincasa–Dowker (BD) d'Alembertian inverse, realization by realization (plain and ε-smeared) | E[B⁻¹] = (E B)⁻¹ exactly, but the retarded mean inverse is **unstable** in flat 4D: it grows as e^{0.376 t/ℓ_k} | grows exponentially | **FAIL, mean diverges.** Checked two ways |
| (c′) stable local layer operators (6 layers; found by scan) | local in curved needles (checked), so the inverse carries √Δ | **exponential**: sd e-fold length ≈ 0.70 ℓ_k³/ℓ² | mean PASS is **suggested**; **FAIL, noise** at 1 Gpc |
| (d) metric-aware scalar sprinkling density | no scalar density repairs the one-hop link for a Ricci (NEC) lens | — | **FAIL.** Proved at first order; checked |

**Plain summary.**
- Adding hops, weighting links by the size of their empty region, or tuning the event density does not fix lensing. These readouts all see the same wrong "needle volume" factor that G-L found.
- What does fix it in principle is a different kind of object. Build a local wave operator from interval counts (the Benincasa–Dowker type) and invert it on each sprinkling. On average this reproduces the inverse of the averaged operator exactly. A local operator's inverse automatically carries GR's Van Vleck focusing.
- **First catch.** The standard 4D BD operator, plain or smeared, has a runaway mode, so its average inverse blows up within a few discreteness lengths.
- I found 6-layer operators without the runaway.
- **Second catch.** For those, the realization-to-realization noise grows exponentially with distance, because the signed weights are re-summed along every chain. To keep the noise down over a gigaparsec, the smearing scale would have to be at least 2×10⁻¹⁵ m. The repository's locality bar is 10⁻¹⁹ m. So the noise is unbounded at astrophysical distances, while laboratory-to-AU distances survive.

**Against the supervisor's expectation:**
- The multi-hop Johnston sum does **not** pass in the mean. In 4D the massless Johnston sum is exactly one hop, and extra hops change only the tail, never the cone (direct) coefficient.
- The BD inverse does reproduce the "inverse of the mean", but for the original operator that inverse is unstable.
- The "noise is the open risk" expectation is confirmed and quantified.

## 1. Notation and normalization (G-L's)

- **Density and kernel.** ρ = ℓ⁻⁴, with a = √ρ/(2π√6), so E[aL] → θ δ(τ²)/(2π) in flat space.
- **G-L needle law** (refereed): V(y,x) = (π/24) τ⁴ ν(y,x). The one-hop cone weight is ν^{-1/2}/(2π); GR's direct coefficient is Δ^{1/2}/(2π).
- **Regime.** Pre-caustic, regular null tubes, curvature scale ≫ needle width.
- **Lens benchmarks:**
  - G-L lane B's conformal lens: Ω² = 1 + A·exp(−|x−c|²/w²), R = 100, w = 10, A = 3;
  - G-L lane A's sandwich plane wave.

## 2. (b) Weighted one-hop links: volume-function lemma

**PROVED (needle order; exact for plane waves).**
- Consider any one-hop kernel whose mean depends on the pair only through ρV, i.e. E K(y,x) = a_w F(ρV(y,x)). This covers:
  - volume weights w(ρV)·L, where F = w·e^{-m};
  - count or layer kernels 1[n = k], where F = e^{-m}m^k/k!;
  - any function of the interval count n.
- Give each kernel its flat normalization a_w. Then its curved cone weight is ν^{-1/2}/(2π).
- Proof: with V = (π/24)ν s² (s = τ²), substitute s′ = ν^{1/2}s. Then ∫F(ρ(π/24)νs²)ds = ν^{-1/2}∫F(ρ(π/24)s′²)ds′.
- Hence link/GR = (νΔ)^{-1/2} for every weight. Weighting cannot repair G-L's mismatch.

**CHECKED (`RL1_G`).** Conformal lens, A = 3, deterministic quadrature of the exact V_g, ℓ = 1, 0.5, 0.25, 0.125. Five weights (1, ρV, (ρV)², 1/(1+ρV), layer n = 2):
- lens central: 0.4867 → 0.4857/0.4858 for every weight; predicted 0.4857;
- lens at the quarter point: 0.5435 → 0.5426; predicted 0.5426.

## 3. (a) Multi-hop Johnston sums

**PROVED (from the published formula).** Johnston's 4D propagator is K = aL(I − abL)⁻¹ with b = −m²/ρ. The massless sum (b = 0) is exactly aL. The "full massless path sum" in 4D is therefore the one-hop kernel, and the refereed G-L FAIL applies verbatim.

**PROVED (exact mean; Johnston eq. 3.15 mechanism).** Consecutive intervals along a chain are disjoint, and inserted chain points never fall in another hop's interval. So for any hop weight that depends on the hop's interval content, the multivariate Mecke formula plus Poisson independence give

  E[k-hop sum] = ρ^{k−1}·(mean hop kernel)^{∗k}

exactly at finite ρ.

**PROVED (needle order).** The convolution of two cone kernels ν^{-1/2}δ(σ) has no δ(σ) part. In null Fermi coordinates it is a finite jump at the cone:

  (π/2)·⟨[Δ(y,x)/(Δ(y,z)Δ(z,x))]^{1/2} ν^{-1/2}(y,z) ν^{-1/2}(z,x)⟩_z θ(σ)

In flat space this is G₀∗G₀ = θ/(8π). Therefore any multi-hop series whose hop multiplier is fixed in physical units (Johnston: abρ = −am²) changes only the tail. The direct (geometric-optics) amplitude stays at one hop's ν^{-1/2}, so link/GR = (νΔ)^{-1/2}.

**Chain (causal-matrix) sums.** Their means are θ-type and never produce the 4D δ(σ) at all.

**Consequence.** A multi-hop sum can change the cone coefficient only if it resums non-perturbatively, with O(1) hop weights. That is class (c).

## 4. (c) Inverses of local layer operators: BD and generalizations

### 4.1 Exact mean identity (PROVED; CHECKED)

**Statement.**
- Take B = α(−I + N), where N(x,y) = c[n(y,x)] is a function of the interval count, the diagonal is deterministic, and the operator is strictly retarded.
- Then E[B⁻¹(x,y)] = −α⁻¹[δ + Σ_k ρ^{k−1} n̄^{∗k}], with n̄ = E c[n] = e^{-m}Σ c_n m^n/n! and m = ρV.
- That is, **the mean of the realization inverse equals the inverse of the mean operator, exactly at finite ρ.**
- Proof: the same disjoint-interval Mecke argument as §3. The series is absolutely convergent on bounded regions.

**Checks:**
- MC against the Volterra solution in flat 4D (`RL1_C2`), at T = 1, 1.5, 2, 2.5, 3: z = +2.24, +0.99, −1.29, +0.67, +0.49. The distributions are heavy-tailed.
- The Volterra solution itself, against direct MC integration of the Neumann terms up to 3 hops (`RL1_B2`): 0.07682 vs 0.0768, −0.6112 vs −0.6112, and 0.679 vs 0.683 (the 4-hop term was omitted).

### 4.2 Curved-space locality of the mean operator (PROVED at needle order; CHECKED)

- Along a needle, the k-th cone moment of n̄(ρV) is ν^{-(k+1)/2} times the flat moment.
- BD's coefficients make the flat moments k = 0, 1, 2 vanish (and only these): Σc_n Γ(n+(k+1)/2)/n! = 0. So they vanish for **any** ν. Curvature cannot bring back the nonlocal ν factor, and far-cone contributions are suppressed as in flat space.
- **CHECKED (`RL1_G`, conformal lens A = 3).** Far-cone leakage of the BD kernel relative to the link cone integral:
  - lensed: 6.3×10⁻¹⁰ → −1.2×10⁻¹⁴ as ℓ goes 1 → 1/8 (with a smooth weight 1+s: −9.8×10⁻⁷ → −3.8×10⁻¹²);
  - flat: 4×10⁻¹² → −3×10⁻¹⁵.
- So the mean operator tends to a local scalar operator. For BD this is □ − R/2 (COMPARATOR: Benincasa–Dowker 2010; not re-derived here).
- The retarded inverse of a local, normally hyperbolic scalar operator has Hadamard direct coefficient Δ^{1/2} (COMPARATOR: Hadamard/DeWitt, as in G-L).
- **Reading: if the retarded mean inverse is stable, its mean lenses as √Δ.** This is SUGGESTED, not computed: I did not solve the mean inverse on a curved background. The conformal lens (`RL1_G`) checks only that the mean operator stays local there. Local covariance and the absence of any supplied vector field are what exclude a first-derivative term.

### 4.3 The original BD operator: the retarded mean inverse is unstable in flat 4D (CHECKED, two independent methods)

**(i) Laplace symbol (`RL1_D`).**
- For a Lorentz-invariant retarded kernel acting on e^{st+ik·x}, the symbol is f̃(z) = 4π∫τ³f(τ)K₁(zτ)/(zτ)dτ, with z² = s² + k².
- Checks on the symbol:
  - the moments vanish (≤ 4×10⁻¹⁴);
  - S(z) = f̃ − 1 → −(√6/4)z² as z → 0, matching to 4×10⁻⁴ relative at z = 0.01;
  - in the resolved rescan (`RL1_F4b`) the near-axis strip [0.003, 0.03]×[−12, 12] contains 0 zeros for BD.
- **Zeros with Re z > 0: z = 0.3756 ± 5.0522i.** Newton-refined; the argument principle counts exactly 2 in [0.05, 6]×[−8, 8] and 2 in [0.03, 20]×[−12, 12].
- The k = 0 mode grows as e^{0.376 t/ℓ}·cos(5.05 t/ℓ).

**(ii) Volterra marching of the exact mean (`RL1_B`).**
- H̄(τ) oscillates with growing amplitude: |H̄| ≈ 0.7 at τ = 2, 0.84 at 16, 15.8 at 20.
- The result is unchanged under grid refinement (h = 0.04 vs 0.02).
- The growth ×21 from τ = 2 to 20 matches the complex-mass Bessel estimate (×28).

**Smeared BD.** E[f(n,ε)] = f_c(εm) by Poisson thinning, so the ε-smeared operator's mean is the same symbol at ρ_k = ερ. It grows as e^{0.376 t/ℓ_k}.

**Physical size.** Over 1 Gpc with ℓ_k ≤ 10⁻¹⁹ m that is about 10⁴⁴ e-folds. **FAIL for the BD inverse as specified.**

**Literature not checked.** Aslanbeigy, Saravani and Sorkin (JHEP 2014, "Generalized causal set d'Alembertians") studied the stability of such retarded operators. I did not re-read it, and this result should be compared with it.

### 4.4 Generalized local layer operators: stable members exist (CHECKED to the resolution stated)

**Setting.** Layers n = 0…L−1, under the three moment constraints plus the normalization f̃(0) = 1.

**Resolved scan (`RL1_F4b`).**
- Setup: 1500-node quadrature; argument principle on [0.03, 20]×[−12, 12] plus the near-axis strip [0.003, 0.03]×[−12, 12], with the edge sampled densely near z = 0.
- Zeros with |z| > 12 are excluded asymptotically, since f̃ ~ 8πC₀/z⁴ there (ARGUED).
- Results:
  - L = 4 (BD): unstable;
  - L = 5: none stable (360 scanned);
  - **L = 6: 6 stable members out of 7320**, e.g. C = (1.01075, −12.82294, 47.46826, −88.10896, 81.40227, −28.94937).

**Superseded scans.** Earlier scans `RL1_E`, `RL1_F`, `RL1_F2` (its stable-member part) and `RL1_F3` were under-resolved and are annotated as superseded in their .out files.

**Mean inverse of a stable member (`RL1_F5`, `RL1_F6`).**
- H̄ decays from −0.14 (τ = 1) to about −1×10⁻³ at τ = 20–42 on the refined grid.
- The coarse grid's uptick at τ = 40 is numerical: it disappears under refinement.
- **Stable only to the resolution tested.** Zeros with Re z < 0.003 (e-fold > 330 ℓ_k) are not excluded.

### 4.5 Noise of operator inverses: exponential in distance

**Mechanism.** The shared-path (diagonal) ladder of E[H²], with rung E[c[n]²] ≥ 0, has no sign cancellation: E[c²] has a positive cone weight, while E[c] has zero moments. So the variance obeys a tachyonic-type ladder. Its rate z* is the real root of r̃(z) = 1.

**Rates.**

| operator | ladder variance rate z* | MC sd e-fold rate (4D, T = 3→9) |
|---|---|---|
| BD | 3.81/ℓ | 1.77/ℓ, i.e. a variance rate of 3.5/ℓ |
| stable L = 6 member | 4.98/ℓ | 2.27/ℓ |

- The rates match. The ladder sd is about 1.1–1.3× the MC sd, so cross terms are mildly negative. The MC uses `RL1_C` with 25–400 realizations; sd(H) grows 66 → 2.7×10⁶ for BD and 502 → 3.9×10⁸ for the stable member.
- The source-driven field φ = Σ H J also grows (stable member sd 0.23 → 153).
- 2D BD: sd(H) 60 → 1.7×10¹² over T = 4 → 24, a rate of about 1.2/ℓ.

**Smeared, stable operator (ε = (ℓ/ℓ_k)⁴).**
- The rung is ε²E[f_ε(n)²] (exact Poisson sums), giving z*_var = ε^{3/4}√(4πI₁)/ℓ = k_var·ℓ²/ℓ_k³.
- I₁ = ∫u f_C(u)² du, and k_var = 2.84–3.33 for the stable members.
- The law matches the exact ladder root to 0.97–1.04 for ε ≤ 0.1.
- The rate itself is CHECKED. The step ladder → variance is CHECKED only at ε = 1 (MC); for ε ≪ 1 it is SUGGESTED.

**Physical translation (`RL1_I`; ℓ = ℓ_P, k_var = 2.84).**
- sd e-fold length λ_N = (2/k_var)·ℓ_k³/ℓ_P² = 2.7×10¹² m at ℓ_k = 10⁻¹⁹ m.
- Over 1 Gpc that is 1.15×10¹³ e-folds. To keep it at ≤ 1 e-fold needs ℓ_k ≥ 2.2×10⁻¹⁵ m.
- That conflicts with the repository locality bar ℓ_k ≤ 10⁻¹⁹ m (E1′ table) by 4 decades in ℓ_k.
- Bounded windows do exist: ≤ 1 e-fold over 1 m needs ℓ_k ≥ 7×10⁻²⁴ m, and over 1 AU needs ℓ_k ≥ 3.8×10⁻²⁰ m.
- **Contrast with E1′-b.** The one-hop link field's noise is about 4×10⁻²⁹ at 1 Gpc. Inverting an operator re-sums signed O(1) weights along chains, and it is this re-summation that makes the noise compound.

## 5. (d) Metric-aware sprinkling density

**Setup.** Density ρ(1+η(z)), a scalar field. The void exponent becomes ρ(π/24)τ⁴[ν + ⟨η⟩_w], with w = 6λ(Λ−λ)/Λ³. Repairing the link needs

  ⟨η⟩_w(y,x) = −ln(νΔ)

for every pair (first order).

**PROVED (first order, thin Ricci/NEC lens on a ray).**
- The left side is (6/Λ³)·[a quadratic polynomial in the endpoints (u_y, u_x)], with coefficients the moments M₀, M₁, M₂ of η.
- The right side is R₀·ab((a+b)² + ab)/Λ³, quartic in the endpoint offsets (a, b).
- No η works, even when only pairs with both ends outside the lens are demanded.

**CHECKED (`RL1_H`).** Exact sandwich waves of strength 0.02/0.1/0.3, pre-caustic. The best-fit scalar density leaves 77–79% (rms) of the mismatch.

**Exception.** For a compact conformal lens (ε = Ω² − 1 compactly supported; its R_kk has vanishing 0th and 1st moments along every ray), η = Ω⁻⁴ − 1 makes the sprinkling exactly a flat one. With flat-region endpoints this reproduces GR's field there. It is not a general mechanism: it fails for any net-focusing matter lens.

## 6. Reading against the FIXED readings

**PASS: not met.**
- Classes (a), (b) and (d) have a density-independent O(1) mismatch in the mean.
- BD (c) has a divergent mean.
- The stable local-operator class (c′) is the only candidate whose mean plausibly gives √Δ. Its noise is unbounded at the astrophysical scales the E1′-b comparison uses: 1 Gpc, with ℓ_k inside the locality bar.

**FAIL clause.** "Every tested readout class has a density-independent O(1) mismatch, or the noise is unbounded. Bounded to the classes tested."
- (a), (b), (d): mismatch (proved).
- BD (c): mean unbounded (checked).
- (c′): noise unbounded. Checked at ε = 1; suggested at ε ≪ 1 through the ladder law.

**Worker reading: FAIL, bounded.**

**Flags for the referee.**
1. If the ε ≪ 1 ladder-to-variance step is not accepted as controlled, class (c′) is INCONCLUSIVE on noise, and the overall reading drops to INCONCLUSIVE.
2. The curved-space mean of (c′) is argued, not computed. This does not affect the FAIL, which rests on noise.
3. Compare §4.3–4.4 with Aslanbeigy–Saravani–Sorkin 2014.
4. The stability scan has finite resolution (Re z ≥ 0.003) and covers only L ≤ 6.

## 7. Scope and hypotheses

**What was tested:**
- scalar readouts;
- a fixed curved metric's Poisson sprinkling with its true causal order (G-L's setting and its axiom conflicts);
- a pre-caustic, regular tube.

**Not tested:**
- tensor structure and GR tails;
- non-retarded or "projected" inverses, which remove growing modes by hand and are not order-only retarded;
- operators with more than 6 layers, or smooth nonlocal kernels other than ε-thinning;
- readouts that use more than interval counts (internal order of the interval, such as chain counts). Those are not covered by the volume-function lemma: their law in a curved needle is that of the Penrose-limit plane-wave interval (ARGUED).

**Price implication (SUGGESTED).** Link-type readouts reach √Δ only by inverting a local operator. That costs:
- (i) a stability-selected operator (not BD);
- (ii) a nonlocality scale ℓ_k ≳ (D ℓ_P²)^{1/3} to keep the noise bounded over distance D. That is about 2×10⁻¹⁵ m for 1 Gpc, in conflict with locality at 10⁻¹⁹ m;
- or else some noise-cancelling structure not yet named.

## Files

All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/RL1/`. Each script has a matching `.out`.

| script | content |
|---|---|
| `RL1_B_bd_mean_volterra.py` | BD mean inverse and diagonal ladder |
| `RL1_B2_small_tau_check.py` | Neumann-term MC check of the Volterra solution |
| `RL1_C_bd_inverse_mc.py` | realization inverse MC, 2D/4D. Outputs: `RL1_C_bd_4d.out`, `RL1_C_bd_2d.out`, `RL1_C_stable6b_4d.out` |
| `RL1_C2_mean_identity.py` | MC check of the exact mean identity |
| `RL1_D_bd_symbol.py` | BD Laplace symbol and its zeros |
| `RL1_E`, `RL1_F`, `RL1_F2`, `RL1_F3`, `RL1_F4` | earlier or under-resolved scans, annotated as superseded |
| `RL1_F4b_rescan_resolved.py` | resolved stability scan; writes `RL1_F4b_stable_L6.npy` |
| `RL1_F5_stable_members.py` | stable members: mean inverse and ladder rate vs ε |
| `RL1_F6_volterra_grid.py` | grid check of the stable member's tail |
| `RL1_G_conformal_lens_readouts.py` | weighted links and local-kernel leakage in the conformal lens |
| `RL1_H_density.py` | metric-aware density, first order |
| `RL1_I_translate.py` | physical noise translation |
| `RL1_report.md` | this report |

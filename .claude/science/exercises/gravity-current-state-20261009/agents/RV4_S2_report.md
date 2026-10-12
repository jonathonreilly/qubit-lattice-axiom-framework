# Lane RV4, probe S2 (numerics): can a local symbol or a measure prescription remove the free shear term? (report)

Worker: Claude Opus 5.5 (same family as the supervisor and S1). Run 22:44Z to about 23:25Z, 2026-10-11. No repository files were edited. **Not refereed.**
Scratch: `.../scratchpad/RV4/S2/`. Every number below is in a `.out` file there (file list at the end).

Normalisation throughout: RN-L1. Flow velocity v = ½ ĥ p(k); E: ĥ = diag(1,−1,0); T2: ĥ_xy = ĥ_yx = 1; trace: ĥ = I. μ = d²E_vac/dε² per site, lattice units. Formula (V3, refereed; P1 integration by parts): μ = ⟨ε_vac J''(0)⟩ = −⟨∇ε_vac · v (∇·v)⟩_BZ. With the dispersion fixed, μ is a quadratic form in the symbol's coefficients, μ = aᵀQa.

## Reading against the FIXED lines

**Short version.**
1. **Choosing the momentum symbol (candidate a): no principle, only tunings.** Pointwise protection of both shear channels is impossible for any periodic symbol (PROVED). Integral zeros μ_E = μ_T2 = 0 exist in every class I scanned, but only as tunings: codimension 2 at each mass, and mass-dependent (CHECKED). The all-mass system is overdetermined at range ≤ 4 and has a nonzero least-squares floor (CHECKED). In the physically relevant regime (ma ≈ 1e-17) a single tuned range-4 symbol works for every mass, but it costs 8 transcendental tunings plus the O(a²) improvement (CHECKED). Each zero also costs something elsewhere:
   - With the nearest-neighbour dispersion kept, the tuned p is no longer the energy current. So it cannot feed the shift (G3/C1).
   - With p = E∇E kept (p = ∇Φ, dispersion Ω = M² + 2Φ), the tuned dispersion carries a large O(a²) quartic anisotropy and a lattice-scale group velocity above 1.
   - Exact E-protection inside the E∇E class forces 2^{d−1}-fold doubling.
2. **Half-density / √J weighting (candidate b, Weyl-type family ω J^{−c}):**
   - c = ½ does not cancel. It gives μ_E = −8.10e-2 in 3D (m = 1), about −41 × the flow value, with the opposite sign.
   - c = 1 cancels every channel at every mass. But it changes the linear stress coupling T1 by −(∇·v)ω, which is 9–13 × T1 in rms. That breaks the RN-L1 exact stress.
   - The value c* that zeros μ depends on the mass: a tuning.
3. **Bulk unitarity with the density of states included, imposed at O(ε²) only (candidate b, last bullet).**
   - It is realised by a **local, finite-range (range 3), mass-independent, untuned** operator counterterm, G2 = ½(∇Ω·v)(∇·v), added to the O(ε²) seagull. T1 is untouched.
   - It zeros μ_E, μ_T2 and the O(ε²) trace term at every mass and for every symbol tested. The strained one-particle density of states is preserved to O(ε⁴) (CHECKED).
   - So the supervisor's expectation that "half-density prescriptions reproduce the formal unitary only with non-local seams" does **not** hold at this order for the free scalar.
   - The rule's status (principle, or the operator form of R₀) decides whether this is a PASS. My reading is that it is (d) promoted to operator level: it imposes "the strained bulk spectrum equals the unstrained one", and the vacuum energy is a spectral functional, so μ = 0 is put in rather than derived. It is also not unique.

**S2 verdict: INCONCLUSIVE, leaning FAIL.**
- (a) and the J^{−c} family: FAIL (bounded) as a tuning, or as a loss of the exact stress.
- The isospectral counterterm meets the numerical side of PASS. Whether it counts as a principle or a definition is S1's and the referee's call.

## 1. Validation and the operator-level check for non-separable symbols (CHECKED)

**Core reproduces refereed numbers** (`s2_validate.out`).
- 3D KG, p = sin k: μ_E = 1.9703886419e-3 at m = 1 (refereed F(1) = 1.970388642e-3), and 2.4671564814e-3 at m = 0.5 (P1: 2.467156e-3). μ_T2 = 0.
- Midpoint L = 48 and L = 64 agree to 1e-10.

**Operator level, V3 method, extended to general stencils** (`s2_operator_check.out`, `s2_operator_mixed.out`). The method: build K, T1 = −i[K,H] and T2 = −[K,[K,H]] exactly on an open block, read the bulk kernels, periodize, and take the Hessian of the symplectic zero-point energy.

| d | symbol | channel | operator paramagnetic | operator full | Jacobian form |
|---|---|---|---|---|---|
| 3 | sin k | E | −2.317304e-3 (= RN L1) | +1.97038863e-3 | +1.97038864e-3 |
| 3 | sin k | T2 | −8.228470e-3 (= RN L1) | −3e-12 | 0 |
| 3 | diag p_x = sin k_x cos k_y cos k_z | E | −1.748694e-3 | −2e-11 | 0 |
| 3 | diag | T2 | −6.673073e-4 | +1.05762773e-3 | +1.05762775e-3 |
| 2 | diag p_x = sin k_x cos k_y | T2 | −2.253568e-3 | +3.25555803e-3 | +3.25555804e-3 |
| 2 | tuned mixed range-4 zero (§2a), m = 1 | E / T2 | −4.32e-3 / −1.21e-2 | −1.5e-12 / +2.5e-11 | 2e-16 / −2e-16 |
| 2 | same symbol, m = 0.3 | E / T2 | −8.01e-3 / −1.88e-2 | +7.379647e-4 / +2.585476e-4 | +7.379647e-4 / +2.585476e-4 |

- **The Jacobian formula holds at operator level for non-separable symbols, cross terms included.**
- Brute-force RK4 flow plus finite differences (P1 style) agrees too: `s2_halfdensity.out` and `s2_iso_general.out`, to about 1e-11.

## 2. Momentum symbols: what is possible (candidate a)

### 2a. Pointwise protection: J_ch ≡ 1 (PROVED)

| Condition | Meaning |
|---|---|
| J_T2 ≡ 1 | ∂_y p_x + ∂_x p_y ≡ 0 (e.g. any separable p) |
| J_E ≡ 1 | ∂_x p_x ≡ ∂_y p_y (≡ ∂_z p_z) (e.g. p_x = sin k_x Π cos k_⊥, the "diag" symbol) |
| Both | sym(∂p) = λI, so p is a conformal Killing field |

- **Both at once is impossible.** A conformal Killing field on the torus is constant: in d ≥ 3 such fields are polynomials of degree ≤ 2; in d = 2, p_x − i p_y is holomorphic and doubly periodic (Liouville). Odd ⇒ p = 0, which contradicts p ≈ k. This is the supervisor's expected obstruction, also for non-separable symbols. Only the non-periodic p = k (SLAC) passes.
- **Inside the E∇E class** (p = ∇Φ):
  - J_E ≡ 1 ⇔ Φ_xx = Φ_yy (= Φ_zz). In Fourier space this means q_x² = q_y² (= q_z²) on the support, so Φ contains only body-diagonal hops.
  - Then Φ is invariant under k → k + π(1,1,0) and permutations. So E-protection forces **2^{d−1}-fold doubling**: the lattice splits into decoupled bcc sublattices.
  - Checked for the diag symbol: Φ = 1 − cos k_x cos k_y has a zero at (π,π) (`s2_enablae.out`: min Φ/Φ_NN = 1.5e-4).
  - J_T2 ≡ 1 ⇔ Φ_xy ≡ 0 ⇔ separable Φ.

### 2b. Integral zeros with the nearest-neighbour KG dispersion and p free (`s2_scan_free_p.out`)

Range ≤ 4 in max-norm: 20 terms in 2D, 60 in 3D (cubic covariant), with slope Σ n a = 1.

**Q_E and Q_T2 are indefinite** (3D: 31 negative and 29 positive eigenvalues), so common zeros exist.

**Named symbols** (μ_E, μ_T2, μ_tr):

| Symbol | m = 1 | m = 0.3 |
|---|---|---|
| sin k, 3D | +1.970e-3, 0, −1.556e-2 | +2.608e-3, 0, −2.151e-2 |
| diag, 3D | 0, +1.058e-3, −2.745e-3 | 0, +1.460e-3, −4.333e-3 |
| improved (4/3 sin k − 1/6 sin 2k), 3D | −2.277e-3, 0, −3.415e-2 | −1.860e-3, 0, −4.401e-2 |

**Closest common zero to sin k:**
- 3D, tuned at m = 1: |a − a_sin| = 0.075. The main move is −0.073 sin 2k, plus small non-separable terms.
- At m = 0.3 the same symbol gives μ_E = +3.74e-4 (14% of sin k) and μ_T2 = +1.8e-5.
- 2D, the same pattern: 7.38e-4 and 2.59e-4 at m = 0.3, operator-checked in §1.

**Zero at both m = 1 and m = 0.3** (3D, 4 equations): the residual at other masses is −1.9e-5 at m = 0.1, but −3.6e-4 at m = 4 (larger than sin k's 3.07e-4 there).

**All masses.** μ(M) = 0 for all M ⇔ ⟨g_ch Ψ(A)⟩ = 0 for every function Ψ of the KG symbol A, where g_ch = (sin k·v)(∇·v).
- Chebyshev moments n < 42 give 84 quadratic conditions of numerical rank 77, against 59 free coefficients in 3D. In 2D: rank 40 against 19.
- Least-squares floor:
  - 3D: μ/F ≈ 6e-4 at every mass, with coefficients up to |a| = 1.6 (large cancellations);
  - 2D: μ_T2/F ≈ 8% at m = 0.1.
- No exact all-mass zero was found. The system is overdetermined (CHECKED, not proved).
- IR necessary condition (PROVED): the leading IR-log term is the M⁶ ln M term in 3D (P1). Its coefficient is ∝ (3A − B) in E and ∝ B in T2, where p_x = k_x + A k_x³ + B k_x k_⊥² + …. So mass independence needs p = k + O(k⁵).
- Every tuned zero found has (3A − B, B) ≠ 0 (`s2_costs_free_p.out`), so each carries an IR log and is mass-dependent.

**Physical regime** (`s2_physical_regime.out`).
- One range-4 3D symbol with p = k + O(k⁵) (2 rational conditions) that zeros the M⁰, M², M⁴ and M⁶ coefficients in both E and T2 (8 transcendental tunings) exists. So μ = O(M⁸ ln M), far below P0 for every physical mass.
- At finite mass it is not zero: μ_E = −1.1e-6 and μ_T2 = +4.4e-6 at m = 1; −7.4e-10 and +1.5e-8 at m = 0.3.
- Caveat: one grid, L = 64. The constrained combination is IR-finite, but the individual entries are not converged.

**Cost (i), E∇E.** For the nearest-neighbour KG Hamiltonian the energy current has symbol ∇(Ω/2) = sin k exactly. Total momentum must equal total energy current, and improvements cannot change totals, so only p = sin k feeds the shift.
- Every tuned zero violates this: rms(p − sin k)/rms(sin k) = 7–13% for single-mass zeros, and **42%** for the physical-regime symbol.
- **These symbols are conserved momenta of the free scalar, but not shift sources.** RN L1's coupling H ⊃ N_i(C_i − T_0i) with T_0i = P_i no longer satisfies G3's div P_shift = div J_E.

### 2c. Integral zeros in the E∇E class: p = ∇Φ, Ω = M² + 2Φ (`s2_enablae.out`, `s2_enablae_margin.out`)

Φ = Σ b_q(1 − C_q) over cubic orbits with max|q_i| ≤ 4 (14 orbits in 2D), normalised so that Hess Φ(0) = I. This class keeps E∇E, a local stress and IR speed 1 by construction.

**Common zeros at m = 1 exist without doublers** (2D). The no-doubler margin is min Φ/Φ_NN ≥ m₀.

| Margin m₀ | α (NN −0.042) | β (NN 0) | max group velocity | μ_E/F_NN at m = 0.3 | μ_T2/F_NN at m = 0.3 |
|---|---|---|---|---|---|
| 0.2–0.6 | +0.11 | −2.50 | 1.092 | −0.073 | +0.219 |
| 0.8 | +0.18 | −1.85 | 1.097 | −0.049 | +0.236 |
| 0.9 | +0.24 | −1.25 | 1.140 | −0.024 | +0.252 |

Here Φ = k²/2 + αΣk⁴ + βΣ_{i<j}k_i²k_j² + ….

**Costs.**
- **Mass dependence** (a tuning): about 20–25% of the untuned value comes back at m = 0.3.
- **A large O(a²) anisotropy**, |β| ≈ 1.3–2.5 against 0. This is direction-dependent dispersion at O(a²k²), about 30–60 × the nearest-neighbour anisotropy.
- **A lattice-scale group velocity of 1.09–1.14** (superluminal against the IR cone).
- The IR-log combinations (12α − 2β, β) are ≠ 0, so the zero is mass-dependent at small M as well.
- A distance metric that does not penalise the nearest-neighbour orbit instead finds zeros pinned at the doubler bound (min Φ/Φ_NN = 0.20), with α = −0.45 and β = −2.3.

**C3 anomaly, cost (ii). PROVED, and CHECKED in every solution.**
- In this class ∇·v_ch = ½ ĥ:(Hess Φ − I). The Jacobian integrand is exactly the channel projection of C3's Hessian anomaly.
- ⟨Hess Φ⟩_BZ = 0 for any periodic Φ, so the averaged C3 anomaly is −I for every symbol (C3_avg_anom = −1.000 in all runs). Tuning μ to zero leaves C3 untouched.

**One-cone speed, cost (iii).** The IR speed is 1 in all classes by normalisation. The costs sit at O(a²): the anisotropy and lattice-scale group velocity above, or, in §2b, the momentum/energy-current mismatch at O(k³).

### 2d. E∇E class: 3D, and the all-mass attempt (`s2_enablae_margin3d.out`, `s2_enablae.out`)

**3D, range ≤ 3** (19 orbits, L = 32): a common zero exists at m = 1 with no-doubler margin ≥ 0.6.
- |b − b_NN| = 0.40; α = +0.14 and β = −1.46, so 12α − 2β = +4.6.
- Maximum group velocity 1.13.
- At m = 0.3: μ_E/F_NN = −0.048 and μ_T2/F_NN = +0.148.
- So the same costs appear as in 2D.
- Caveat: L = 32 is converged at m = 1 (better than 1e-6). At m = 0.3 the error is about 1e-2 of F, which does not affect the sign or size of the mass dependence.
- The first 3D attempt in `s2_enablae.out` (x-metric, 2 starts, 80 iterations) found none. That is a search limit, superseded by the margin search. Its traceback is from the 3D all-mass step, which was skipped for time.

**2D all-mass attempt** (10 masses, 20 conditions, 13 free; SLSQP limited to 120 iterations, so not converged):
- floor Σ(μ/F_NN)² = 1.7e-6, i.e. about 4e-4 per condition;
- off-set masses: μ_T2/F up to 1.3e-3 at m = 0.05;
- the solution sits on the doubler bound (min Φ/Φ_NN = 0.20), with β = −3.1.
- No exact all-mass zero was found. The system is overdetermined.

## 3. Measure prescriptions (candidate b) (`s2_halfdensity.out`, `s2_iso_general.out`)

### 3a. Weyl-type family ω_c(q) = [ω J^{−c}](Φ⁻¹q), for c = 0 (flow), ½ (half-density) and 1 (density)

- **Formula.** μ(c) = (1 − c)[⟨ε J2⟩ − c⟨ε D²⟩], with D = ∇·v (PROVED by expansion; brute force agrees to 1e-11).
- **Locality.** To O(ε²) the symbol J^{−c} is a trig polynomial, so each member is a finite-range local coupling.

| p = sin k | flow c = 0 | half-density c = ½ | density c = 1 | c* (zero) |
|---|---|---|---|---|
| 3D E, m = 1 | +1.970e-3 | **−8.103e-2** | 0 | +0.00601 |
| 3D E, m = 0.3 | +2.608e-3 | −7.498e-2 | 0 | +0.00855 |
| 3D trace, m = 1 | −1.556e-2 | −1.262e-1 | 0 | −0.0329 |
| 2D E, m = 1 | +3.152e-3 | −6.793e-2 | 0 | +0.01134 |
| T2 (separable) | 0 | 0 | 0 | — |

- **Half-density c = ½:** not a cancellation. It overshoots by a factor of about 40, with the opposite sign.
- **c*:** a mass-dependent tuning.
- **c = 1:** zero in every channel, at every mass, to all orders (⟨ω/J · J⟩ = ⟨ω⟩). But its O(ε) term changes T1 by −c(∇·v)ω. The rms ratio to the T1 symbol is 12.9 in 3D and 9.1 in 2D (E, m = 1).
  - The integrated stress is fixed by the exact identity (Σ_x T_ij = i[H, K_ij] up to c-numbers), so this breaks RN L1's exact stress.
  - The E and T2 channels are then no longer fed by one momentum density.
  - FAIL against the PASS requirement "keep RN-L1 exactness".
- **Bulk unitarity cannot fix c.** No constant c preserves the density of states at O(ε²); only the vacuum moment can be fixed.

### 3b. Bulk unitarity at O(ε²) only: the isospectral counterterm

**The construction (PROVED; a short computation).**
- Keep the flow at O(ε), so T1 = i[H,K] stays exact. Add at O(ε²) the one-particle shift Ω → Ω + ε²G2, with **G2 = ½(∇Ω·v)(∇·v)**. Equivalently, δE_k = ½ε²(v·∇E)(∇·v) for any band, consistently for E or E².
- Then for every function g: ⟨g(Ω̃)⟩_q = ⟨g(Ω)⟩ + ε⟨g(Ω)∇·v⟩ + O(ε³).
- The O(ε²) term cancels identically: ½⟨g ∇·(v∇·v)⟩ = −½⟨g′(∇Ω·v)∇·v⟩.
- The O(ε) term vanishes for E and T2 by cubic symmetry: ∇·v is odd under the swap or reflection that flips ĥ.
- So the strained density of states is unchanged at O(ε²) in the shear channels, for any symbol and any mass.

**Checked (brute-force RK4 flow plus finite differences).**

| Case | μ with G2 | μ without G2 |
|---|---|---|
| p = sin k, 2D and 3D, E and T2, m = 1 and 0.3 | ≤ 4e-11 | e.g. E 1.970e-3 in 3D |
| diag, T2 | 3e-12 | 3.256e-3 |
| mixed 0.6 sin + 0.4 diag, E | 2e-12 | 8.08e-3 |
| mixed, T2 | 1e-12 | 1.44e-2 |
| trace channel, O(ε²) term | 6e-12 | −1.556e-2 |

- **DOS moments.** With the flow alone, ⟨Ω̃ⁿ⟩ − ⟨Ωⁿ⟩ for n = 1…4 shifts at O(ε²): −0.25ε², −5.25ε², … in 3D. With G2 the shift is O(ε⁴); it halves on the /ε³ scale when ε halves.
- **The trace channel is not isospectral at O(ε).** It carries a first-order pressure term; the rule removes only the O(ε²) Jacobian piece.
- **Properties:**
  - G2 has Fourier range 3 for the nearest-neighbour KG;
  - it is independent of M (∇Ω = ∇A);
  - it contains no tuned number;
  - it has one formula for every species (bands enter only through E(k));
  - it changes only the O(h²) seagull. Its IR size is δω ≈ −ε²(k_x² − k_y²)²/(16ω), an irrelevant O(a²k⁴) operator.
- **Not unique (PROVED).** Any addition Z whose average over every level set of Ω vanishes also preserves the DOS. The rule fixes level-set averages only. G2 is the canonical pointwise choice: it adds back the Jacobian integrand.

**Reading (my own, for S1 and the referee).**
- This is candidate (d), "uniform strain is a relabelling, so the spectrum is strain-invariant", imposed as an operator rule rather than as R₀'s c-number subtraction.
- **It is not a tuning:** no number is adjusted, and it is mass- and species-independent.
- **Whether it is a principle or a definition** turns on whether bulk isospectrality under uniform strain follows from the axioms. It is the continuum statement "constant h is gauge". The V3 referee noted that the axioms do not fix the nonlinear coupling, and I found nothing that derives it.
- Because the vacuum energy is a spectral functional, μ = 0 is a direct consequence of the rule's definition. That makes it closer to a definition than to a mechanism.

**What it does not do.**
- It does not touch C3: the non-uniform-h closure still needs Hess(Ω/2) constant.
- It is shown only at O(ε²), for uniform strain, for the free scalar.

## 4. Labels

**PROVED** (same family, unrefereed):
- the conformal-Killing obstruction to J_E ≡ J_T2 ≡ 1 for periodic symbols;
- E-protection inside E∇E ⇒ 2^{d−1}-fold doubling;
- T2-protection inside E∇E ⇔ separable Φ;
- D_ch = channel projection of C3's Hessian anomaly, and the averaged anomaly −I for every periodic Φ;
- the IR-log condition p = k + O(k⁵) for mass independence;
- μ(c) for the J^{−c} family;
- the isospectral identity for G2, and its non-uniqueness.

**CHECKED:**
- the operator-level Jacobian formula for non-separable and mixed symbols;
- the common zeros and their mass dependence (2D and 3D);
- the overdetermined all-mass system and its floor;
- the physical-regime tuned symbol;
- the E∇E-class zeros and their costs;
- the half-density and density values;
- G2 zeroing μ in every channel, symbol and mass, and preserving the DOS to O(ε⁴).

**SUGGESTED:**
- no exact all-mass zero exists at any finite range: the overdetermined count is evidence, not proof;
- the separable 2D E∇E all-mass condition reduces to m₄(t)m₀(t) = 3m₂(t)² for m_n(t) = ∫φ′ⁿe^{−tφ}. Its 1/t expansion gives 3(1 + 24a₄/t + …) and forces φ = x²/2 order by order (a non-vanishing coefficient checked only at the first order).

**READING:**
- the isospectral rule is the operator form of (d)/R₀, a definition unless derived from the axioms.

**Not done:**
- G2 beyond O(ε²);
- non-uniform h with G2;
- fermions numerically (the identity is band-generic);
- 3D E∇E all-mass (skipped for time);
- the mode-rearrangement unitary that maps H to the isospectral H̃. It may be non-local (level sets degenerate at van Hove points), and I did not construct it. Only the coupling itself is shown to be local.

## Files (`.../scratchpad/RV4/S2/`)

- `s2_core.py`: symbols, quadratic forms;
- `s2_validate.py` / `.out`;
- `s2_operator_check.py` / `.out` and `s2_operator_mixed.py` / `.out`: V3 open-block method with general stencils. Uses `v3_free_scalar_seagull_copy.py`, an unmodified copy of V3's script;
- `s2_scan_free_p.py` / `.out`, `s2_costs_free_p.py` / `.out`, `s2_physical_regime.py` / `.out`;
- `s2_enablae.py` / `.out`, `s2_enablae_lib.py`, `s2_enablae_margin.py` / `.out`, `s2_enablae_margin3d.py` / `.out`;
- `s2_halfdensity.py` / `.out`, `s2_iso_general.py` / `.out`;
- `*.npy`: the tuned coefficient vectors.

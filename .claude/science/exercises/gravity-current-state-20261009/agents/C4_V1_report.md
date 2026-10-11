# Lane RV, probe V1: a dressed momentum that annihilates the vacuum (report)

Worker: Claude Opus 5.5, the same family as the supervisor and W1. Run 17:35Z to about 18:20Z, 2026-10-11. No repository files were edited. Scratch folder: `.../scratchpad/C4/V1/`. **Not refereed.**

## Reading against the FIXED line

**V1: PASS (bounded, conditional), pending a codex referee.**

- **Bounds.** Vacuum Hessians only, uniform strain, perturbative in λ, massive onsite φ⁴ in the L2/W1 design.
- **Condition.** A rule R for what counts as the "local part" of the flowed coupling (§2c). R is a principle and contains no number.

The three FIXED requirements:
- **μ_E = μ_T2 = 0 at O(λ²): PROVED.** In fact μ = 0 to every order at which P_λ is built. P_λ at O(λ) already gives μ = 0 through O(λ³).
- **No free parameter: PROVED, given R.** Every freedom left in P₁ is shown not to move μ (§1, §2d).
- **Flow exponentially local: PROVED and CHECKED.** The forced kernel is analytic and decays exponentially (table in §1b).

**Where the obstruction went.** The 2↔2 obstruction (L2-A) does not disappear. It moves wholly into states with two or more particles, at **O(λ)**.
- There it cannot be removed by any bounded kernel.
- It makes the local coupling non-isospectral for scattering states. It does not make the coupling non-local.
- It never reaches the vacuum, at any order.
- The supervisor expected the opposite on two points: a PASS that holds only at O(λ²), and the obstruction entering the vacuum at O(λ³). Neither happens.

## 0. Setting

- Lattice Klein–Gordon field on Z³ with mass m and dispersion ω(k) = √(m² + Σ4sin²(k_i/2)).
- H = H₂ + λV, with V = (1/24)Σ_x :φ_x⁴: normal-ordered in the unstrained free vacuum |0⟩. This is the L2/W1 tadpole-subtracted design.
- Modes: a_k, with α(k) = (2ω)^{−1/2}.
- Free momentum: P = Σ_k f(k) a†_k a_k, with f = sin k (vector).
- Free strain flow: U₀ = exp(−iK₀), where K₀ = ½h_ij Σ_x x_j P_i(x) is the RN L1/L2 density-transport flow. It maps a_k to the strained modes b_q at lab momentum q, which are a Bogoliubov combination of a_q and a†_{−q}. It is exactly local on every translation-invariant quadratic operator, because any such X has [P, X] = 0.

## 1. P₁ sector by sector: forced, free, and how local

### 1a. Construction (PROVED)

Write P_λ = W P W†, with W = e^{λS} and S anti-Hermitian and translation-invariant. Then P_λ|Ω⟩ = 0 holds exactly whenever W|0⟩ = |Ω⟩.

At O(λ), P₁ = [S₁, P]. The sectors below are written as (creators, annihilators) in a-modes.

| Sector | P₁ kernel (times Π_l α(k_l)) | Status | Denominator | Locality |
|---|---|---|---|---|
| 0↔4 | (1/24)·Σ_l f(k_l) / Σ_l ω(k_l), on Σk ≡ 0 | **Forced** by P_λ\|Ω⟩ = 0. The same equation is 40-sector conservation, [P,V]₄₀ + [P₁,H₂]₄₀ = 0. | Σω ≥ 4m | Analytic, exponentially local (§1b) |
| 1↔3 | (4/24)·(f₁+f₂+f₃−f₄)/(ω₁+ω₂+ω₃−ω₄) | **Free** under vacuum annihilation. **Forced** if conservation is also required wherever a bounded solution exists. | D₃ ≥ √(9m²+108) − √(m²+108) > 0, PROVED (below) | Analytic, exponentially local |
| 2↔2 | (6/24)·(f₁+f₂−f₃−f₄)/(ω₁+ω₂−ω₃−ω₄) would be needed for conservation | **Not available.** The denominator is 0 on the elastic shell and the numerator is not (L2-A). Choose 0, or any bounded off-shell kernel: a free function that does not matter for μ. | 0 on shell | No bounded kernel exists, so none in ℓ¹. A principal value is not summable (power-law at best) and still leaves the on-shell defect. |
| quadratic | P₁^{11} = Σ g(k)a†a is free; it renormalises the one-particle symbol; g = 0 is a normalisation. P₁^{20} = 0 is forced. | | | |

**The 1↔3 gap (PROVED).** No single lattice-KG particle can decay into three:
1. Per axis, |sin(Q/2)| ≤ Σ_l |sin(k_l/2)|, including umklapp.
2. The triangle inequality and Minkowski then give Σ_l ω(k_l) − ω(Σk_l) ≥ √(9m²+X²) − √(m²+X²), with X ≤ 6√3.
3. The same argument covers 1↔5, 1↔7 and so on.

**Checked minima** (`v1_shells.out`):

| m | min D₃ | Proved bound | min D₅ |
|---|---|---|---|
| 0.1 | 0.0513 | 0.0039 | 0.118 |
| 0.3 | 0.257 | 0.035 | 0.580 |
| 1 | 1.383 | 0.376 | 2.985 |
| 1.5 | 2.348 | 0.825 | 4.965 |

**On the 2↔2 shell** (checked, 4000 nontrivial resonances at each of m = 1 and m = 0.3): |Σf_in − Σf_out| has median 1.8 and minimum about 1e-2. The 2→4 shell is non-empty for m < 2, so it is a second obstructed sector at O(λ²), together with 3↔3.

**Generator.** S₁ = −V₄₀/Σω − V₃₁/D₃ − h.c. Check: [S₁^{40}, P] = (Σf/Σω)V₄₀. ✓

### 1b. Real-space decay of the forced 0↔4 kernel (CHECKED)

The kernel is evaluated exactly on the L³ torus by FFT, using 1/Σω = ∫dt e^{−tΣω} (quadrature error ≤ 2e-13). Two variants were computed: the a-basis kernel, and the φφφπ field-basis component (Σf/Σω)/ω(k₄). Files: `v1_kernel_decay_*.out`.

At m = 1, the local decay rates per site (ln|K| per unit r, read from r ≈ 18–22) are the same at L = 32 and L = 48:

| Configuration | Local decay rate per site |
|---|---|
| Three legs at 0, one at r·x̂ | 1.06 |
| φ leg far | 1.10 |
| Pairs separated | 2.13 |
| Legs spread on x, y, z | 3.05 |
| One leg along (1,1,0) | 1.46 |

- Example values, r = 2 to 22: |K| = 13, 0.26, 1.2e-2, 8.4e-4, … down to 1.4e-10.
- The rates approach the one-leg branch-point rate 2 asinh(m/2) = 0.962 from above.
- At m = 0.3 (L = 48) the asymptotic rate is about 0.43, falling toward 2 asinh(0.15) = 0.299 before the torus wraps.
- **So the localisation length is ≈ 1/m.** It is exponential, but at the matter's Compton length, not the lattice spacing (see §4).

## 2. The flow, the coupling, and μ

### 2a. Exact factorisation (PROVED)

- K_λ is the first moment of the density p_λ(x) = W P(x) W†, which is exponentially local, so K_λ = W K₀ W†.
- U_h(λ) = e^{−iK_λ} = W U₀ W†.
- Hence H_full(h) = U_h H U_h† = W · U₀ (W†HW) U₀† · W†.

With W exact, W†HW = E₀ + Σ_k E(k) a†a + Y:
- Y contains only terms with at least 2 creators and at least 2 annihilators.
- The (n,0) parts are removed because the vacuum gap is 2m. The (2j+1,1) parts are removed because of the gap D_{2j+1}.
- At O(λ), Y = λV₂₂.

### 2b. The crux: where δ(ΣΦ_ε) appears

The free flow U₀ moves the momentum delta of Y to the curved surface δ(ΣΦ_ε^{−1}(q)). This is W1's mismatch.

W sits outside U₀ and is not transported, so its kernels keep δ(Σq). Consequently:
- **The vertex that creates particles from the vacuum is exactly translation-covariant.** At O(λ) it is [S, H₂(h)]₄₀, which is supported on Σq ≡ 0. It is not anomalous at any order in h.
- **The explicit-position anomaly lives only in the ≥2-in/≥2-out sectors**, relative to the transported vacuum |Ω_h⟩ = W U₀|0⟩. It is also absent from the one-particle sector, because the one-particle shell is isolated (§1a).
- **With the bare P, by contrast, the anomaly has a vacuum-creating total Σf·V₄₀.** Splitting it is then a choice that sets μ: W1's site and centroid conventions, and v_R.

### 2c. Rule R and μ (PROVED)

**Rule R.** Drop only the explicit-position part of the anomaly, and assign that part to the particle sectors it lives in: the dropped operator annihilates |Ω_h⟩ on both sides. Any sector-preserving split (centroid or other) inside those sectors is allowed. Formally:

H_loc(h) = W [E₀ + U₀(ΣE a†a)U₀† + Y_loc(h)] W†.

**Properties of H_loc(h):**
- It is translation-covariant.
- It is exponentially local at each order in h. W is quasi-local; the kernels of Y_loc are analytic for m > 0.
- It reduces to H at h = 0.

**Result.**
- W|0_h⟩ is an exact eigenstate of H_loc(h), with eigenvalue E₀ for every h.
- So μ_E = μ_T2 = 0 identically.
- With W truncated at O(λ), the first h-dependence would come from the anomalous O(λ²) 40-part of W†HW, which enters only at O(λ⁴). So μ = 0 through O(λ³) with P_λ at O(λ).

### 2d. The free choices do not move μ (PROVED)

- **S in the (≥2,≥2) sectors:** it only changes Y.
- **The g in P₁^{11}:** it is a free flow with a different odd symbol, which is still isospectral.
- **The density placement of p_λ:** it changes K by a translation-invariant local operator, which is a unitary conjugation.
- **The split chosen inside rule R:** the dropped pieces annihilate the vacuum.

### 2e. The mechanism is a vacuum-level seagull (PROVED; CHECKED in `v1_vacuum_seagull_*.out`)

Expand around |0_h⟩. Two O(λ²) terms cancel by the f-sum identity, exactly as in the RN L1 free seagull:
- the second-order term of the O(λ) vertex X = [S, H₂(h)], which equals −ΣE_n|S_n0|²;
- the O(λ²h²) seagull ½[S,[S,H₂(h)]], which equals +ΣE_n|S_n0|².

The two-particle part of S|0_h⟩ is zero at O(ε) by E/T2 symmetry.

Hessians in units of λ² per cell (L-converged):

| m | Channel | Dressed O(λ) vertex alone | Seagull | Total | L2 control (reproduced) |
|---|---|---|---|---|---|
| 1 | E | −1.4191e-5 | +1.4191e-5 | 0 | −1.0093e-6 |
| 1 | T2 | −7.691e-7 | +7.691e-7 | 0 | +1.6108e-8 |
| 0.3 | E | −2.518e-5 | +2.518e-5 | 0 | −3.062e-6 |
| 0.3 | T2 | −2.489e-6 | +2.489e-6 | 0 | +6.9e-8 |

So a truncation without the λ²h² seagull would miss by 14–48 times the L2 value.

## 3. Where non-locality first appears

- **Vacuum: never** (all orders, perturbatively). Every vacuum denominator is ≥ 2m.
- **One-particle sector: never.** The 1→(2j+1) gaps are positive, as proved in §1a.
- **Two-particle sector: at O(λ), in the 2↔2 sector.**
  - Making the flow covariant there (P_λ conserved) needs a kernel that is unbounded on the elastic shell. No local or summable P₁^{22} exists; the principal value has power-law tails and still leaves the on-shell defect. This is L2-A.
  - **At O(λ²):** 2↔4 (inelastic, for m < 2) and 3↔3 join.
- **In H_loc the anomaly is dropped, not cancelled.** So the price is not non-locality but **non-isospectrality**: under strain, 2-particle scattering amplitudes are not the transported ones, at O(λε).
  - SUGGESTED: at low momenta the numerator Σf_in − Σf_out = O(k³) for f = sin k, so the effect is suppressed by about (ka)³, or (ka)^{2R+1} for higher-order f.
- **The first vacuum-independent observable affected:** finite-density or thermal stress response, starting at O(λ²) × density². SUGGESTED, not computed.

## 4. Caveats and readings

- **READING: rule R is the one non-numerical input.**
  - It is basis-free: the dropped anomaly annihilates the transported vacuum.
  - It is available only because P_λ annihilates the vacuum. With the bare P it cannot be satisfied.
  - A referee may still count it as "vacuum-referenced", as W1's v_R was. The difference: v_R is a pointwise, h²-dependent vertex built from the vacuum integrand. Here μ = 0 holds for every split in a class defined without μ.
- **ARGUED, not computed:** splitting the 2↔2 anomaly in the *unstrained* a-mode basis, or by the field-basis site rule, instead leaks an O(λε²) vacuum-creating term, so μ ≠ 0 at O(λ²). The leak comes from the Bogoliubov factor s = O(ε) times the centroid shift O(ε).
- **SUGGESTED, PROVED by the same argument, not run:** W1's nearest-neighbour φ²φ² result, μ at O(λ′), is a convention artifact under R. The transported V′ has zero expectation value in |0_h⟩, and W absorbs the creation sectors of any local interaction with a gapped vacuum. So there is no per-interaction tuning.
- **SUGGESTED: locality length ≈ 1/m.**
  - It is exponential, but set by the matter mass, not the lattice spacing. For physical masses at Planck spacing it spans more than 10¹⁷ sites.
  - In the massless limit (photons, gluons) the vacuum denominators close at k → 0 and W becomes power-law.
  - This conflicts in spirit with nearest-neighbour Admissibility (MINIMAL_AXIOMS: one fixed nearest-neighbour rule). The fixed reading only asks for "exponentially local".
- **Not addressed:**
  - non-uniform h (q ≠ 0);
  - the constraint algebra (C3) for H_loc;
  - fermions and gauge fields;
  - anything non-perturbative.

## Labels

- **PROVED (same family, unrefereed):**
  - P_λ = WPW†;
  - the sector table and which sectors are forced;
  - the 1↔(2j+1) gap;
  - the factorisation;
  - the vacuum-sector covariance;
  - μ ≡ 0 under R;
  - the free choices being inert;
  - the f-sum mechanism.
- **CHECKED:**
  - the kernel decay (L = 32 and 48; m = 1 and 0.3);
  - the gap minima;
  - the 2↔2 numerator;
  - the seagull Hessians (L = 16/24 and 24/32);
  - the L2 controls.
- **ARGUED:** the convention leak outside R.
- **SUGGESTED:** the low-k suppression, the finite-density response, φ²φ², the massless limit.
- **READING:** whether R counts as a principle or a tuning.

## Files (`.../scratchpad/C4/V1/`)

- `v1_kernel_decay.py` with outputs `v1_kernel_decay_m1_L32.out`, `v1_kernel_decay_m1_L48.out`, `v1_kernel_decay_m0.3_L48.out`.
- `v1_shells.py` with output `v1_shells.out`.
- `v1_vacuum_seagull.py` with outputs `v1_vacuum_seagull_m1.out` and `v1_vacuum_seagull_m0.3.out`.
- Reused: W1's `w1_core.py`.

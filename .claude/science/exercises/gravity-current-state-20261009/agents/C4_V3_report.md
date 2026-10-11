# Lane RV3, probe V3: the V1 mechanism for the framework's own matter (report)

Worker: Claude Opus 5.5 (same family as the supervisor and V1). Run 18:15Z to about 18:50Z, 2026-10-11. No repository files were edited. Scratch folder: `.../scratchpad/C4/V3/`. Every number below is in a `.out` file there. **Not refereed.**

## Reading against the FIXED line

**(a) Massive staggered fermions on Z³ with an S1 contact interaction: INCONCLUSIVE, leaning FAIL.**
- **The dressing exists and is exponentially quasi-local.** PROVED and CHECKED.
  - The forced 0↔4 kernel has denominator Σω ≥ 4m.
  - The 1↔3 block is gapped.
  - The 2↔2 block is obstructed, as S1 found.
- **The O(λ²) interaction part cancels exactly under rule R.** PROVED, by the V1 f-sum identity. S is translation-invariant, so no boundary term appears.
- **The free part, which the brief asked me to check first, does not cancel.**
  - Built as a genuinely local operator, the unitary-flow coupling plus its local seagull leaves μ_E^free ≠ 0. CHECKED three independent ways in d = 2 and 3.
  - μ_T2^free = 0 exactly. PROVED (Liouville).
  - So the literal local coupling has μ_E ≠ 0 at O(λ⁰), which is a FIXED FAIL disjunct.
- **μ = 0 needs an extra c-number rule R₀.** R₀ means: normal-order every transported quadratic part with respect to the transported vacuum.
  - R₀ subtracts exactly the vacuum's own E-channel response. Applied generally, it would zero μ for *any* coupling.
  - So R₀ is a definition, not a mechanism.
  - The only alternative found is to choose a different free momentum symbol. That is a one-parameter tuning that depends on the mass (§1d).

**(b) Staggered QED at O(e²) with a noncompact photon: FAIL (bounded, partly argued).**
- **No exponentially quasi-local vacuum-annihilating dressing exists at O(e).** This is the order needed for μ at O(e²).
  - Every vacuum-creating energy denominator is gapped (≥ 2m), except the γγ channel at O(e²).
  - The photon's gaplessness instead enters through the photon-leg mode functions, which are non-analytic at q = 0.
  - With V1's prescription (free sectors set to zero), the forced e⁺e⁻γ kernel has power-law tails: about r⁻² on the E leg and r⁻⁴ on the A leg. CHECKED.
  - An exponentially local completion through the free γ↔e⁺e⁻ sector is impossible for m < √3 in staggered units, which includes every physical mass. ARGUED by analytic continuation: the required kernel has poles on the taste-changing γ↔e⁺e⁻ shell, and that shell is non-empty for m < √3 (CHECKED).
  - A C^∞ splice gives faster-than-any-power decay, but not exponential decay. ARGUED.
- **On top of that:** the free fermion sea carries the same E anomaly as in (a), and the photon's own strain flow has not been constructed (RN L1 left it open).
- **Caveat:** a referee may count the super-polynomial completion as "local enough" and downgrade the verdict to INCONCLUSIVE. Strict exponential quasi-locality fails.

**Against the supervisor's expectation:**
- (a) was expected to PASS conditional on R. It is instead held up by a free-level E-channel anomaly that V1 and RN L1 also contain (§1).
- (b) was expected to PASS at O(e²), with power laws first appearing at O(e⁴) through light-by-light scattering. Power laws in fact appear at **O(e)**. The cause is non-analyticity, not vanishing denominators.

## 1. The free part first: the local unitary seagull does not cancel in E

### 1a. Setting

These are the RN L1 and S1 conventions.
- **Hamiltonian:** h = Σ(i/2)η_j(x)(c†_x c_{x+j} − h.c.) + mΣε(x)n_x.
- **Momentum:** P_j = Σ_x(c†_x c_{x+2e_j} − h.c.)/(4i), with symbol f = ½ sin 2p_j·1 (scalar, taste-universal), placed at X = x + e_j.
- **Generator:** K = Σ ĥ_ij Σ_x (X_j − c) P_i(x).
- **Coupling:** H(ε) = e^{−iεK} H e^{iεK} = H + εT1 + ½ε²T2, with T1 = −i[K, h] (the linear stress coupling) and T2 = −[K, [K, h]] (the seagull).
- **Normalization:** this is V1/W1's flow velocity, ε ĥ f. RN L1's K_h = ½hXP gives Hessians smaller by a factor of 4. The scalar control is run in RN L1's normalization.

### 1b. Method (no f-sum assumed anywhere)

`v3_free_fermion_seagull.py` and `v3_free_scalar_seagull.py`:
1. Build K, T1 and T2 *exactly* as operators on an open N^d block: N = 24 in 2D, 18 in 3D for the fermion, 14 for the scalar.
2. Read their bulk kernels at a central cell. They are translation-invariant (under translation by 2 for the fermion) to 0.0. The ranges are T1 ≤ 3 and T2 ≤ 5.
3. Copy these local operators onto a periodic torus.
4. Compute the half-filled sea energy per site (fermion) or the zero-point energy per site (scalar, from symplectic eigenvalues) for:
   - h + εT1, which gives the "paramagnetic" Hessian;
   - h + εT1 + ½ε²T2, which gives the full Hessian;
   - the honest seagull ⟨vac|T2|vac⟩.

### 1c. Results (CHECKED)

Hessians per site; para = paramagnetic.

| Case | Channel | Para | Honest seagull | f-sum seagull | Full | Jacobian prediction (same grid) |
|---|---|---|---|---|---|---|
| 2D fermion, m=0.5, L=24 | E | −5.4572e-2 | +4.8272e-2 | +5.4572e-2 | **−6.3004e-3** | −6.3004e-3 |
| 2D fermion, m=0.5, L=24 | T2 | −3.8817e-2 | +3.8816e-2 | | −4.2e-7 (continuum −3e-12) | −4.2e-7 |
| 3D fermion, m=0.5, L=12 | E | −4.6607e-2 | +4.3270e-2 | +4.6607e-2 | **−3.3369e-3** | −3.3369e-3 |
| 3D fermion, m=0.5, L=12 | T2 | −3.7297e-2 | +3.7221e-2 | | −7.6e-5 (continuum −8e-10) | −7.6e-5 |
| 3D fermion, m=1, L=12 | E | −3.9124e-2 | +3.7102e-2 | | **−2.0217e-3** | −2.0217e-3 |
| 3D scalar (RN L1 norm), m=1, L=24 | E | −2.3173e-3 | +4.2877e-3 | +2.3173e-3 | **+1.9704e-3** | ÷4: 1.9704e-3 |
| 3D scalar (RN L1 norm), m=1, L=24 | T2 | −8.2285e-3 | +8.2285e-3 | | −3e-12 | 0 |
| 3D scalar, m=0.5 | E | −3.1725e-3 | +5.6396e-3 | | **+2.4671e-3** | 2.4671e-3 |
| 3D scalar, m→0 | E | −3.6962e-3 | +6.3895e-3 | | **+2.6932e-3** | 2.6932e-3 |

**What the table shows.**
- The scalar paramagnetic values reproduce RN L1's to 4 digits: −0.002317 and −0.008228 at m = 1; −0.003172 at m = 0.5; −0.003695 at m = 0.
- **In the E channel the honest local seagull is not the f-sum value.** For the free scalar, the uncancelled residual is 73–85% of the paramagnetic response, with the opposite sign.
- **T2 cancels**, to the finite-grid aliasing level, which goes to 0 in the continuum.
- On every grid, the full Hessian equals the Jacobian formula of §1d to 1e-8 relative. (The dilation channel D also matches: +2.0787e-2.)

### 1d. Mechanism (PROVED for the formula, CHECKED numerically)

**What the flow does.** The first-moment flow transports modes along k̇ = ĥ·f(k). The local strained operator has symbol h(Φ_ε⁻¹(q)), so:
- E_vac/site = ⟨ε_vac(Φ⁻¹q)⟩_q = ⟨J ε_vac⟩_k, where J = det DΦ;
- ε_vac = −½ω for the staggered sea, and +½ω for the scalar zero-point energy.

**Where the f-sum goes wrong.** The f-sum identity ⟨[K,[K,H]]⟩ = −2ΣE_n|K_n0|² treats K as a vector operation on the vacuum. Summation by parts of the first moment drops a boundary term of bulk size: the per-volume trace of [K, ·] is not zero. The dropped amount is exactly ⟨(J−1)ε_vac⟩.

**E against T2.**
- **T2:** the flow (k̇_x, k̇_y) = (f(k_y), f(k_x)) is divergence-free, so J ≡ 1 and μ_T2 = 0 exactly. This holds for any c-number produced by transport, at every order in λ.
- **E:** div = f′(k_x) − f′(k_y) ≠ 0, so J ≠ 1.

**Relation to the scalar.** The staggered result is the KG result at doubled mass:

μ_E^stag(m) = −½ μ_E^KG(2m) (V1 normalization).

**Continuum values** (`v3_tables.out`, L = 64, converged to 1e-6 relative except at m = 0). μ_T2 ≤ 3e-12 in every case.

| m | Fermion μ_E (V1 norm) | Fermion μ_E (RN L1 norm) | Scalar μ_E (RN L1 norm) |
|---|---|---|---|
| 0 | −5.39e-3 | −1.35e-3 | +2.70e-3 |
| 0.1 | −5.31e-3 | −1.33e-3 | +2.69e-3 |
| 0.3 | −4.76e-3 | −1.19e-3 | +2.61e-3 |
| 0.5 | −3.94e-3 | −9.85e-4 | +2.47e-3 |
| 1 | −2.12e-3 | −5.29e-4 | +1.97e-3 |

**Size.** The anomaly is O(1) in lattice units at m → 0. It is weighted toward the UV, as a zero-point quantity is, so the continuum limit does not suppress it.

**Readings and suggestions.**
- **Why it is a lattice effect.** In the continuum, f = k, so the E flow preserves volume and the anomaly vanishes. Any local momentum (periodic and analytic, with ∫f′ = 0 over the zone) has non-constant f′. SUGGESTED: this is the vacuum-sector shadow of the periodicity/umklapp obstruction (lanes RN L2 and RG). A sawtooth f = k would remove it.
- **Avoiding it costs a tuning.** CHECKED in `v3_anomaly_vs_f.out`. In free theory any odd f is conserved. Within f_a = sin k + a sin 2k, μ_E^anom = 0 at a* = −0.0864 (m = 0.5) and −0.0757 (m = 1). That is one tuning per species, and it depends on the mass.
- **It is not a cosmological constant.** A GR-type √g·Λ counterterm adds equal h² terms to E and T2. It therefore cannot remove an E-only term. This is an E_g shear mass: one of P0's two numbers. T_2g is protected by Liouville. SUGGESTED.

### 1e. Consequences for earlier results

- **RN L1 referee.** The statement "a specific finite-range, coefficient-determined unitary seagull cancels them exactly for uniform strain" holds for T2. It fails in E for the local seagull operator. Their script fixes the seagull by the f-sum (`referee_L1_checks.py` tt_quadrature) and does not evaluate it.
- **V1.** Its §2e has the same issue at O(λ⁰): `v1_vacuum_seagull.py` also fixes the other piece by the identity. V1's "W|0_h⟩ is an exact eigenstate of H_loc(h) for every h" holds only with R₀.
- **ARGUED:** at O(λ²) there is a further anomaly, −½λ²·Hess⟨Σ₂∘Φ⁻¹⟩, from transporting the λ²-renormalized one-body energies. It is likewise E-only.

## 2. (a) Contact-interacting staggered fermions: sectors, gaps, locality

**Quasiparticles.** Particles b (+ band) and holes d (− band). Each band is 2^{d−1}-fold degenerate (spin × taste) for m > 0. The interaction is V Σ n_x n_{x+j} or U Σ_y Q_y² (S1), normal-ordered in the unstrained sea (the tadpole-subtracted design).

**The free momentum.** P = Σ f(k)(b†b + d†d) with f = ½ sin 2k scalar. It has no pair terms and annihilates the sea. PROVED: a scalar symbol has no interband elements, and f is odd.

### Sector table for P₁ = [S₁, P]

| Sector | Kernel | Status | Denominator | Locality |
|---|---|---|---|---|
| 0↔4 (b†b†d†d†) | V₄₀·Σf/Σω (f taste-blind) | **Forced** by P_λ\|Ω⟩ = 0 | Σω ≥ 4m | Analytic for m > 0 ⇒ exponentially local |
| 1↔3 (any band/taste mix) | V₃₁·(f₁+f₂+f₃−f₄)/D₃ | Free; can be block-diagonalized | D₃ > 0 (proof below) | Analytic, exponentially local |
| 2↔2 (ee, hh, eh) | — | **Obstructed** (S1: on-shell numerator ≠ 0; cluster on-shell norm 0.204) | 0 on shell | No bounded kernel |
| 0↔2 | Absent in the normal-ordered design | — | 2m | — |

**The 0↔2 sector in the bare design.** If the bare n n form is used instead, the O(λ) Fock term renormalizes kinetic against mass. It then creates pairs, b†d†, with denominator 2ω ≥ 2m. That sector is gapped and analytic, so nothing changes.

**The 1↔3 gap. PROVED and CHECKED.**
- Kinematics depend only on ω_s(k) = ½ω_KG(2k; 2m), with conservation mod π mapping to mod 2π.
- So V1's bound transfers: D₃^stag ≥ ½[√(36m²+108) − √(4m²+108)] > 0.
- Checked minima (`v3_tables.out` (B), 300 Nelder–Mead starts) equal ½·D₃^KG(2m). At m = 0.5 the minimum is 0.6916, which is ½ × V1's 1.383 for KG at m = 1.

| m | min D₃ | Proved bound |
|---|---|---|
| 0.1 | 0.0712 | 0.0077 |
| 0.3 | 0.344 | 0.069 |
| 0.5 | 0.692 | 0.188 |
| 1 | 1.680 | 0.708 |

**Locality of the forced kernel. PROVED by analyticity; CHECKED.**
- Every leg is a matrix function of h: g(h) = a(ω) + b(ω)h, with ω² = m² + Σsin²p a scalar on the full zone.
- So each leg decays like the Fourier transforms of 1/(ω+S) and 1/(ω(ω+S)), with S ≥ 3m.
- The branch point is at sin p = im, giving a decay rate of asinh(m) per site.
- Checked (`v3_fermion_leg_decay.out`, even r from 14 to 26, L = 96): local rates approach asinh(m) from above.

| m | Local rates | asinh(m) |
|---|---|---|
| 0.3 | 0.38–0.47 | 0.296 |
| 0.5 | 0.56–0.65 | 0.481 |
| 1 | 0.97–1.05 | 0.881 |

- As in V1, the localization length is about 1/m, not the lattice spacing. Physical masses would need more than 10¹⁷ sites. That is a reading.
- At m = 0 the gap closes, and the kernel becomes non-analytic at the cone, hence power-law.

**The O(λ²) interaction cancellation. PROVED, an algebraic identity in any finite volume.**
- Take any anti-Hermitian, translation-invariant S, and the local H₂(h) with ground state |0_h⟩.
- With X = [S, H₂(h)], we have X_n0 = −(E_n − E₀)S_n0. So the second-order energy is −Σ(E_n−E₀)|S_n0|².
- The seagull gives ½⟨[S,[S,H₂(h)]]⟩ = +Σ(E_n−E₀)|S_n0|².
- These cancel. The identity needs no first moment, so no anomaly enters (contrast §1).
- Under R adapted to fermions, the dropped 2↔2 anomaly annihilates the transported sea on both sides. That is the same statement as V1's, with fermionic sectors.
- Not re-run numerically: it is the same identity the V1 referee confirmed analytically.
- **Total μ at O(λ²)** = 0 (from the S terms) + the free anomaly at O(λ⁰) (§1) + the transported self-energy anomaly at O(λ²) (ARGUED, E-only).

## 3. (b) Staggered QED at O(e²): sectors, denominators, where power laws enter

**Model.** As in S2: noncompact Yee photon in Coulomb gauge, Ω(q) = √Σ4sin²(q_i/2), with minimal coupling expanded to O(e²).

### Vacuum-creating sectors

| Order | Sector | Denominator | Comment |
|---|---|---|---|
| O(e) | e⁺e⁻γ (b†d†a†) | ω₁ + ω₂ + Ω ≥ 2m | **Gapped.** The infimum, at a soft photon with the pair at rest, has a nonzero vertex: Γ_i anticommutes with Γ_ε, so the vertex is purely interband. |
| O(e²) | Coulomb e⁺e⁻e⁺e⁻ | ≥ 4m | Gapped. |
| O(e²) | e⁺e⁻γγ (seagull) | ≥ 2m | Gapped. |
| O(e²) | **γγ** (diamagnetic plus second-order pair loop, i.e. vacuum polarization) | 2Ω(q) → 0 | **The only gapless vacuum channel at O(e²).** By the lattice Ward identity (K1 checked Π(0) → 0) the numerator is Π(q) = O(q²), so the forced kernel Π/(4Ω²) stays bounded. It is direction-dependent at q → 0, giving r⁻³ tails (ARGUED). |

**The single-photon sector.** At O(e), the one-photon sector is **resonant**, unlike V1's gapped 1↔3. Taste-changing γ ↔ e⁺e⁻ is on shell at lattice-scale q. For example, q = (π,π,π) has Ω = 2√3 against a pair energy of 2m.
- CHECKED (`v3_tables.out` (B)): the shell is non-empty for m ≤ 1.70 and empty from m = 1.75. The threshold is √3.
- This is S2's "opposite-sign bands keep pair resonances".

### Where the photon's gaplessness first gives power laws: O(e), the e⁺e⁻γ sector

**The forced kernel.** K = −c(k₁,k₂,q)/(√(2Ω)(Σ+Ω)), with Σ = ω₁ + ω₂ ≥ 2m and c analytic. Written in local fields:
- A leg: −c/(2(Σ+Ω)). This has a |q| cusp, so its tail goes as r⁻⁴.
- E leg: −ic/(2Ω(Σ+Ω)). This goes as 1/|q|, so its tail goes as r⁻².

**CHECKED** (`v3_tables.out` (C), L = 96, local log–log slopes for r from 4 to 16):
- Σ = 1: E-leg slope −2.0 to −2.4; A-leg slope −3.8 to −3.9.
- Σ = 0.2: crossover.
- Massive-photon control (M = 0.5): exponential, rate about 0.55.

**Repair through the free 1↔2 sector (γ ↔ e⁺e⁻). ARGUED.**
- Write the dressing's action on the vacuum as α(q)A_q + iβ(q)E_q, with α and β the local kernels.
- We need α + iβΩ = −c/(Σ+Ω). Since Ω is non-analytic only at q = 0, and the split a + bΩ there is unique, analyticity forces β = −ic/(Σ²−Ω²).
- β then has poles on the γ↔e⁺e⁻ shell. So no exponentially local completion exists for m < √3, unless c vanishes on that shell.
- A smooth bump that splices β near q = 0 gives C^∞ kernels: faster than any power, but not exponential.
- **Gauge caveat, not resolved.** In Coulomb gauge the E_T leg drags a Coulomb cloud, E_L[ρ], with 1/r² tails. A manifestly local, gauge-invariant (temporal-gauge, Gauss-law) form of the dressing was not constructed.
- **Correction to the expectation.** Power laws enter at O(e), not O(e⁴). The gap of the denominators (≥ 2m) does not protect locality, because the photon-leg mode functions are non-analytic.

**μ at O(e²).**
- The interaction-part cancellation holds formally under R, by the same f-sum: S is translation-invariant, and ∫|K|² and ∫Ω|K|² per volume are finite.
- The free parts carry the E anomaly: the fermion sea as in §1, and the photon zero-point energy.
- The photon's strain flow needs a local Maxwell momentum density and stress, which RN L1 did not construct. So the photon term is not computed. SUGGESTED: it is nonzero in E and zero in T2 if its f_i depends only on q_i.

## 4. Labels

**PROVED** (same family, unrefereed):
- the Jacobian form of the strained vacuum energy and the failure of the f-sum for first-moment generators (boundary term);
- μ_T2 = 0 by Liouville, for any symbol f_i(k_i), at every order;
- the KG map μ_E^stag(m) = −½μ_E^KG(2m);
- the fermion sector table and the forced 0↔4 kernel;
- the 1↔3 gap bound;
- exponential locality for m > 0;
- the O(λ²) S-identity;
- the QED denominators.

**CHECKED:**
- honest local seagull against paramagnetic, against Jacobian, against f-sum, in 2D and 3D, fermion and scalar, m from 0 to 1;
- reproduction of RN L1's paramagnetic values;
- continuum μ_E tables;
- D₃ minima;
- leg decay rates;
- the γ↔e⁺e⁻ threshold √3;
- photon-leg power-law tails, against the exponential massive control;
- the one-parameter f-tuning root.

**ARGUED:**
- no exponentially local O(e) completion, and the existence of a C^∞ one;
- r⁻³ tails in the γγ and Coulomb sectors;
- the O(λ²) self-energy anomaly.

**SUGGESTED:**
- the anomaly as the shadow of the umklapp obstruction;
- E_g unprotected and T_2g protected;
- the photon's own anomaly.

**READING:**
- whether R₀ is admissible. My reading is no, because applied generally it zeroes μ for any coupling.

**Not done:**
- a two-sided numeric O(λ²) fermion check, since the identity is algebraic;
- non-uniform h;
- the constraint algebra;
- Z₂ and compact gauge fields;
- a nonperturbative treatment.

## Files (`.../scratchpad/C4/V3/`)

- `v3_free_fermion_seagull.py`, with `v3_free_fermion_d2_m0.5.out`, `v3_free_fermion_d3_m0.5.out` and `v3_free_fermion_d3_m1.out`
- `v3_free_scalar_seagull.py`, with `v3_free_scalar_d3.out`
- `v3_tables.py`, with `v3_tables.out`: continuum μ_E, gaps, the QED threshold, photon-leg tails
- `v3_fermion_leg_decay.py`, with `v3_fermion_leg_decay.out`
- `v3_anomaly_vs_f.py`, with `v3_anomaly_vs_f.out`

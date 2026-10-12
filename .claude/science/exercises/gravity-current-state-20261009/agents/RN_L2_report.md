# Lane RN, probe L2: interacting matter (Claude Opus 5.5; same family; not refereed)

**Reading against the FIXED lines: FAIL (bounded), with one leg conditional.**
- The "no exact stress" leg is proved within its class.
- The "constraints turn second class" leg is proved.
- The "TT mass of natural size × coupling²" leg is checked only for the best *free-level* design of the coupling. A dressed design might lower the vacuum piece (see 2c).

No interacting local law on Z^2 or Z^3 passes. The one passer found is 1D and integrable.

The FAIL still needs a codex sol referee before it is recorded.

Scratch folder: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/laneRN/L2/`
- `l2_collision_invariants.py` / `.out`: the exact linear-algebra search.
- `l2_sunset_mu.py` / `l2_sunset_mu_m1.out`, `l2_sunset_mu_m0.3.out`: the induced μ_E and μ_T2.
- `l2_xxz_passer.py` / `.out`: the 1D integrable control.

## 1. Exact search: is there a local conserved additive momentum?

### 1a. The criterion goes beyond K3a's class (proved, same-family)

Let P = Σ_x 𝒫(x), where 𝒫 is any local or ℓ¹-quasi-local operator.
- **Any body order.**
- **Any range.**
- **Matrix-valued** in species or band.

Conservation [H,P] = 0 forces the following.

- **One-particle sector.** P acts as a symbol f(k) (one per band or species) that commutes with the band Hamiltonian.
- **Two-particle sector of a number-conserving law** (Hubbard; two-species contact with conserved species; Bose–Hubbard).
  - P commutes with the two-body S-matrix.
  - The two-body part of P is short-range in the relative coordinate, so it drops out of the asymptotic states (standard Møller-operator argument).
  - Parts of body order ≥ 3 vanish in this sector.
  - **The condition is exact in U, not perturbative:**

    f_A(k1) + f_B(k2) = f_A(k3) + f_B(k4) whenever T(k1,k2 → k3,k4; E) ≠ 0 on shell, with k1+k2 ≡ k3+k4 (mod 2π) and ε_A(k1)+ε_B(k2) = ε_A(k3)+ε_B(k4).

  - **For contact interactions,** T = U/(1 − U·G_K(E)) is a nonzero constant on every shell. So the condition holds on the whole resonance set.
- **Onsite φ⁴, which does not conserve particle number.** The same condition holds at O(λ) for any P = P₂ + λP₄ + …
  - Take the on-shell 2→2 matrix element of [H₂,P₄] + [H₄,P₂] = 0.
  - The first term vanishes on shell for any bounded kernel of P₄.
  - At O(λ⁰), a quasi-local P contains no quartic part that commutes with H₂ (in d ≥ 2 the resonance set has measure zero).
  - **This is perturbative in λ** (a family analytic in λ). The classical and quantum statements are identical.
- **Upshot.** The obstruction does not depend on the range or body order of the dressing. That closes K3a's open items "larger range, quasi-local, higher-body, polarization/matrix" for these laws.

### 1b. Lemma L2-A (proved, same-family; a functional-equation argument)

**Hypotheses.**
- d ≥ 2.
- ε_A and ε_B are even and C².
- Their non-critical level sets are connected.
- On every open patch of a level set of Ω = ε_A + ε_B, the ratio ∂_iΩ/∂_jΩ is not constant.
- This holds for lattice Klein–Gordon and tight-binding bands, because both are functions of Σ cos k_i. The 2D level Σ cos = 0 is an isolated exception, and continuity handles it.

**Claim.** Every C¹ collision invariant (f_A, f_B) on T^d has odd part zero. So **no additive momentum exists whose density has a summable first moment.** That includes every finite-range and every exponentially quasi-local density.

**Proof sketch.**
1. Parity maps invariants to invariants, so assume f is odd.
2. At K = 0, f_B − f_A is odd but is a function of the even function Ω, so it vanishes.
3. Differentiate the shell condition in K at K = 0. This gives ∂_j f(k) = φ_j(Ω(k)).
4. Symmetry of second derivatives gives φ_j′(Ω)∂_iΩ = φ_i′(Ω)∂_jΩ. Non-constant gradient ratios force φ′ = 0.
5. So ∇f is constant, f = b·k + c, periodicity gives b = 0, and oddness gives c = 0. ∎

**Plain reading.**
- The obstruction already appears at small total momentum. It is not only umklapp.
- Any periodic smooth "momentum" fails on ordinary low-K collisions.
- Only f = k exactly survives those collisions. f = k is the sawtooth, a non-summable density with 1/r tails, and it fails on umklapp.

**d = 1 is different.** Step 4 is empty in 1D.
- The 1D cosine band has only trivial 2↔2 resonances (proved analytically; checked).
- So 1D Hubbard passes this test with any f.

### 1c. Checked: exact null spaces of odd trigonometric-polynomial f

f is spanned by sin(n·k) with |n|_∞ ≤ R, with no cubic symmetry imposed. The resonances are sampled nontrivial on-shell 2↔2 configurations, with energy residual ≤ 2e-14. The **odd null space is {0} in every case:**

| Law | Ranges R | Resonance samples | Umklapp fraction |
|---|---|---|---|
| 3D onsite φ⁴, m = 1 and m = 0.2 | 1–4 (364 functions) | 8000 | 0.57 |
| 3D Hubbard | 1–4 | 8000 | |
| 3D two-species contact (m_A = 1, m_B = 0.5; f_A and f_B independent; 728 functions) | 1–4 | 8000 | |
| 2D onsite φ⁴ and 2D Hubbard | 1–8 | | |
| **1D onsite φ⁴** | 1–32 | | |

- **1D onsite φ⁴ also has odd null space {0}.** Nontrivial resonances exist because the lattice Klein–Gordon dispersion has an inflection point.
- **Control 1: 1D Hubbard.** The sampled "resonances" are only the permutations, every f passes, and the defect is 1e-15. As expected.
- **Control 2: Hubbard's even null space** contains ε itself, as expected.

### 1d. Quasi-local: how fast the best defect falls (checked, not extrapolable)

The measure is the RMS of Σ s f on the resonances. It depends on the normalization.

- **Normalized only by f′(0) = 1.** The defect falls fast (3D: 0.42, 0.11, 0.047, 0.024 for R = 1–4). The optimizer satisfies the condition by keeping f ≈ k only in a region of size about 1/R. So **a slope-only normalization lets the fit dodge the obstruction (it keeps f ≈ k only near k = 0),** and that may also apply to K3a′'s R^-2.9 (suggested).
- **Normalized by f = k on the ball |k| < 0.6 (momentum correct for all low-energy states).** The defect falls slowly:
  - 3D: 0.45, 0.25, 0.17, 0.124 for R = 1–4.
  - 2D: 0.74, 0.38, 0.27, 0.20, 0.17 for R = 1, 2, 4, 6, 8. The local exponent falls from about 1.5 to about 0.5.
  - The normal and umklapp parts are comparable.
- Lemma L2-A rules out an exact zero. Whether the infimum is above zero is **open.**

**Physically (argued).** For low-energy matter, f = k + O(k^{2R+1}) makes the defect on normal processes about (ka)^{2R+1}. The exact obstruction sits at lattice-scale momenta.

## 2. Consequence in the exact-constraint theory

### 2a. Lapse sector (proved, standard)

Any finite-range H = Σ h_x has an exact local energy current: i[H,h_x] = Σ_y i[h_y,h_x] is an antisymmetric pair flux. So N(C_s − T₀₀) stays first class, provided C_s is consistent in H_N.

### 2b. Shift sector (proved, given 1a/1b)

- [H_tot, C_i − T₀ᵢ] = −R_i(x), the defect. It is nonzero as an operator for every choice of T_ij, because it is nonzero on two-particle states.
- **Dirac's algorithm** then gives a secondary constraint R_i ≈ 0. That is a matter constraint forbidding the f-violating on-shell collisions. Three per site, for every two-particle sector, overconstrains interacting matter. **Option A: no interacting matter.**
- **Option B: drop the shift constraint.**
  - Per site, (h,π) has 12 phase-space dimensions. C_s, first class, removes 2. That leaves 10, i.e. **5 degrees of freedom: 2 TT plus 3 longitudinal (ξ_i) modes.**
  - H_N is gauge invariant, so the ξ modes get no energy from it. Their dynamics come only from the matter defect: strongly coupled Stückelberg modes (suggested).
  - μ_E and μ_T2 are then unprotected.

### 2c. Induced μ_E and μ_T2 from onsite φ⁴ at the first nonvanishing order (checked numerically; design stated)

**The design.**
- Couple the free part exactly: H(h) = U_h H₂ U_h† + λH₄, with U_h = exp(−i h_ij Σ_x x_j 𝒫_i(x)). 𝒫 is the free pseudo-momentum with symbol f.
- U_h acts as a smooth flow of the Brillouin torus. φ is transported as a density and π as a scalar.
- **Free μ = 0 exactly** by construction.
- **O(λ) is zero:** the tadpole ⟨φ²⟩ is flow-invariant. G″ → 1e-14 at L = 32 (control).

**O(λ²), exact formula.**
- E⁽²⁾/V = −(λ²/24)·∫dt Σ_x g_t(x)⁴, with g_t(k) = J(k) e^{−tω(Φk)} / (2ω(Φk)).
- In the continuum this is exactly h-independent.
- **Normalization:** μ = d²(E/V)/dε² per cell, with h = ε·diag(1,−1,0) (E channel) or h_xy = ε (T2 channel).
- The "I4 part" in the table is the connected quartic term.
- The tadpole-mass ("I2") term is dropped, because absorbing the one-loop mass into the designed H₂ removes it. With the naive tadpole it adds −8.4e-5·λ² to μ_E.

Converged values (L = 24 and 32 agree; m = 1):

| f | μ_E / λ² | μ_T2 / λ² |
|---|---|---|
| sin k (range 1) | −1.01e-6 | +1.61e-8 |
| k + O(k⁵) (range 2) | −1.75e-6 | +2.67e-8 |
| k + O(k⁷) (range 3) | −2.18e-6 | — |
| k + O(k⁹) (range 4) | −2.46e-6 | — |

- **At m = 0.3** (range 1): μ_E = −3.06e-6 λ² and μ_T2 = +6.9e-8 λ².
- The Fejér-sawtooth rows fail the G″ control and are discarded.

**Reading.**
- |μ_E| ≈ 0.6 × the natural three-loop size, λ²/(24(16π²)²) = 1.67e-6. μ_T2 is about 1% of that size.
- **The signs are opposite, as in K3a″** (axis −, face +), so one TT polarization is tachyonic.
- **It does not shrink as the range of f grows.** It grows toward the sawtooth.
- It is smaller than K3a″'s 1.3e-2·e² per cell, mainly by the loop factor. At λ ~ 1 and Planck spacing it is still about 1e98 above the 1e-104·M_Pl⁴ bar.

**Caveat (suggested, not computed).** Vacuum processes are off-shell. An O(λ) dressing P₄ with coefficient −VΣf/Σω, which is analytic and so exponentially local, may cancel this vacuum O(λ²) piece. If so, the vacuum μ is design-dependent, not forced. What cannot be cancelled is the on-shell defect, which acts in any state with real particles.

## 3. Does any interacting local law pass?

- **1D integrable: yes (checked).** On the XXZ ring, Q₃ = Σ[h_{j,j+1}, h_{j+1,j+2}] (the energy current, range 3) has ‖[H,Q₃]‖ = 0 at L = 10.
  - Its one-magnon symbol is −16Δ sin k + 8 sin 2k, with slope 16(1−Δ) at k = 0. That is an IR-normalized, exact, local "momentum" for Δ ≠ 1.
  - A next-nearest-neighbour ZZ term destroys it (relative commutator 0.85).
  - **Not a 3D option:** Lemma L2-A has no 1D analogue to block it, but in d ≥ 2 the lemma excludes it.
- **d ≥ 2 with finite-range or analytic interactions: none (argued).**
  - Lemma L2-A needs only T ≢ 0 on low-K shells. That is any law with nonzero low-energy two-body scattering.
  - Even the non-local sawtooth f = k fails if T is analytic. T must vanish on an umklapp open subset of a shell, and then it vanishes on that whole shell component. So the two-body scattering is trivial.
  - **Gauge-mediated case (argued).** QED at O(e²) has Møller T ≠ 0 at small K, so the same lemma applies to the electron's f. That extends K3a beyond O(e) and beyond its charge class. Caveat: the degenerate staggered-taste (matrix-valued f) case is **not checked**.
- **What passes: an engineered interaction acting only on modes |k_i| < κ ≤ π/2** (suggested; a construction, not run).
  - It uses a smooth momentum-space cutoff on each leg.
  - The momentum is f = k on the ball, smooth outside, and exactly conserved.
  - The interaction and the density are C^∞ but not analytic. Their tails fall faster than any power and slower than any exponential.
- **The price:** non-nearest-neighbour, non-analytic interactions. That conflicts with Admissibility's one fixed nearest-neighbour rule. Or else an exact additive lattice momentum that is not in the axioms.
- **Comparator (recalled, not re-read).** Shiraishi–Tasaki-type theorems state that generic qubit models in d ≥ 2 have no nontrivial local conserved quantities.

## Labels and strong words

- **Proved (same-family, unrefereed):**
  - the 2-particle reduction;
  - Lemma L2-A;
  - the O(λ) φ⁴ reduction;
  - energy continuity;
  - second-class-ness.
- **Checked:** the null spaces, defect tables, μ values and XXZ result.
- **Argued:** the dof count and Stückelberg modes; the QED O(e²) extension; analytic-T triviality.
- **Suggested:** the dressed vacuum cancellation; the momentum-cutoff passer; the reading of K3a′.
- **Not done:**
  - non-perturbative φ⁴;
  - staggered taste-matrix f;
  - the extra-mode dispersion;
  - finite-T μ;
  - lapse-only coupling (that is L3).

# The linearised abelian soft RG chain on 4D lattice gauge fields: what is proven

Write-up of the linear/abelian package of the ym4d-proof lane (sessions 3-16, 2026-10-26/27). Session 16, wind-down
session 1 of 2. Every statement below is transcribed from the lemma ledger PROOF.md. Line numbers ("l.N") refer to
**PROOF_session16_snapshot.md**, the frozen copy of PROOF.md at the end of session 16. Check files are in `checks/`.

**Review status.** Every item below has been through at least one independent hostile review by an agent that wrote none of
the proof, with that review's binding fixes applied (REVIEW_S3, REVIEW_S5_S6, REVIEW_S9_S10, REVIEW_S11_S12, REVIEW_S13_S14,
REVIEW_S15_CONVERGENCE). The one exception is **Lemma F-df_0 (Lemma 4.4), proven in session 16 and not yet reviewed.** These are
internal reviews by AI agents, not peer review.

**Status words.** PROVEN = the complete argument is written in PROOF.md. ARGUED = a reason is given, not a proof. OPEN = not
proven; the missing statement is named. "Located rate" = a numerically located number, not proven.

---

## 1. Setting and definitions

### 1.1 Lattices, levels, torus
- d = 4. Fix an odd integer L ≥ 3 (all numerical constants below are at L = 3 unless stated). An RG chain has levels
  i = 0, …, k (k ≥ 1). Level i is the torus Λ_i = (Z/T_iZ)⁴ in its own units (spacing 1), with T_i = T·L^{k-i}; level k
  is the **coarse** torus of side T ≥ 1, level 0 the **fine** one. n := L^k.
- The levels are nested: a level-(i+1) site X is the level-i site LX + o, o = (L-1)/2, the centre ("root") c_X of the
  level-i block B(X) = LX + {0, …, L-1}⁴. L odd makes block centres lattice sites at every depth (l.2176-2180).
- Fields are real 1-forms B_i on the links of Λ_i. Around the trivial SU(N) background the Lie algebra linearises to
  N² - 1 independent copies, so one real component is treated (l.1917-1919). d is the lattice exterior derivative (forward
  differences), d* its adjoint, Δ = dd* + d*d the Hodge Laplacian; on a flat torus it is the scalar Laplacian on each
  component (lattice Weitzenböck, l.961-963).
- **Coarse units.** A level-l 2-form H has coarse-unit value H^c := L^{2(k-l)}H; a level-(i+1) 1-form r has r^c := L^{k-1-i}r;
  the fine curvature in coarse units is **f_0 := n²dB_0**, and f_l := L^{2(k-l)}d_lB_l (l.3197-3203, RTARGET §33).

### 1.2 The averaging S4' and its linearisation
- **S4' (order-averaged averaging; l.454-481).** For each of the 4! coordinate orders σ, P^σ is the complete-axial
  transporter that moves in the coordinates in the order σ. A coarse link (X, X + e_μ) averages the contours
  T^σ_y = P^σ(c_X → y)·S_y·P^σ(c_Y → y + Le_μ)^†, y ∈ B(X), S_y the straight leg of L steps, over σ and y (the same σ at
  both ends). It is gauge covariant at the roots, maps SU(N) to SU(N) on its domain, and is covariant under axis
  permutations and reflections (check c8, 12/12).
- **Linearisation.** For small abelian fields the averaged link is Q_rootA(X, μ) := avg_{σ,y}∫_{T^σ_y}A (the "root map").
  The **straight average** is (Q_strA)(X, μ) := L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ). With the **slice functional**
  h(A)(X) := avg_σavg_{y∈B(X)}∫_{P^σ(c_X→y)}A, the exact identity **Q_root = Q_str - d∘h** holds (L3g(a)-slice, l.982-990;
  check c8(f), error ≤ 2e-16). Root covariance: Q∘d = d∘ev, ev the restriction to roots.
- **Relation to Balaban's averaging.** Balaban's averaged link CMP 109 (0.4), with the two contour families paired by
  order, equals S4' exactly (Lemma B-avg, l.567-573; check c17(B), ≤ 6e-16). With independent pairing the two agree at
  linear order only. So the averaging is not the soft-specific part of this package; the constraint is.

### 1.3 The soft normalised kernel and the linearised chain
- **Kernel (decision 4; l.1498-1507).** With M̄_c(U) the mean of the S4' contour transporters of the coarse link c,
  K(V, U) := Π_c exp(-(κ/g²)[1 - N^{-1}Re tr(V_c^{-1}M̄_c(U))]) / 𝒩(M̄_c(U)), 𝒩(M) := ∫_{SU(N)}exp(-(κ/g²)[1 - N^{-1}Re tr(V^{-1}M)])dV.
  ∫K(V, U)dV = 1 for every U, so the RG step e^{-S_{k+1}(V)} := ∫K(V, U)e^{-S_k(U)}dU is exact (it preserves Z), and it
  is gauge covariant. It is a soft (Gaussian-like) replacement of Balaban's hard constraint δ(M(U)V^{-1}).
- **Setting SC (the linearised soft chain; l.1917-1926).** The quadratic part of the tree-level exponent of this kernel,
  iterated over k levels, is the chain energy
  **E(B_0, …, B_{k-1}; B_k) = ½||dB_0||² + Σ_{i<k}(κ_i/2)||QB_i - B_{i+1}||²**, with B_k (the coarse field) given and
  κ_- ≤ κ_i ≤ κ_+. (The normalisation 𝒩 cancels the shrinkage |M̄| < 1, so only the distance from the polar part is
  charged.) **Residuals** r_i := QB_i - B_{i+1}; κ̂ := max_iκ_{k-1}/κ_i (in §4, κ̂ := κ_+/κ_-); **E_k(B_k)** := inf over
  B_0, …, B_{k-1}. A minimiser exists (a finite-dimensional quadratic form ≥ 0).
- With sources (RTARGET §33): E_j(B) := E(B) - Σ_{l<k}⟨j_l, B_l⟩, each j_l a co-closed, zero-mean level-l 1-form, written in
  **divergence form** j_l = d_l^*G_l (G_l a level-l 2-form).

### 1.4 Norms (RTARGET §33, verbatim in substance)
- d(z, z') := the ℓ¹ torus distance between coarse positions (an object at level l sits at L^{l-k}·(its base point)).
- Weight w(z) := e^{m d(z, X_0)} (m ≥ 0, any coarse site X_0); ||v||_{∞,m} := sup_z w(z)|v^c(z)|.
- Level weights ω_0 := 1, ω_l ≥ 1, Ω := Σ_lω_l^{-1}. Source norm ||G||_Y := max_lω_l||G_l||_{∞,m}. Data norm
  ||B_k||_{D,m} := ||B_k||_{∞,m}. Soft output norm ||r||_{X_s} := max_iL^{k-1-i}||r_i||_{∞,m}. Fine output norm
  ||f_0||_{X_f,α} := ||f_0||_{∞,m} + [f_0]_{α,m}, the Campanato seminorm at coarse scales 1/n ≤ ρ ≤ 1.
- Kernels are bounded entrywise; "exponentially local with rate m'" means |K(X)| ≤ Ce^{-m'|X|_1} on Z⁴, with the torus
  kernel the periodisation.

### 1.5 Symbols (l.2419-2438, l.2653-2672)
Every chain operator is diagonal in the components and invariant under coarse translations, so it has a coarse symbol in
p ∈ (R/2πZ)⁴, a T-independent function sampled on the grid (2π/T)Z⁴. Notation: ν_α(p) := e^{ip_α} - 1; ψ := Σ_α|ν_α|²;
D_s(θ) := s^{-1}Σ_{j<s}e^{-iθj/s}; δ := D_nD̄_n (entire); φ_α := 2n²(1 - cos(p_α/n)), φ := Σφ_α; a := κΠ_αδ_α;
A_μ := Σ_m(κ/κ_{k-1-m})S_{L^m}(p_μ) (the residual-transport sum); Z_μ := the K ≠ 0 alias sum (a finite sum);
**R_μ := A_μ + κZ_μ, β_μ := aδ_μ + φR_μ, Ψ := 1 - Σ_μφ_μR_μ/β_μ, Σ := Σ_μΔ_μ/β_μ**, κ := κ_{k-1}. The dual problem's
symbol is P̂_μ = β_μ/φ (Lemma EXP-id).

---

## 2. Averaging and energy

**Theorem 2.1 (L3g(a)-glob; l.953-980).** For the straight average on the fine torus (εZ/TZ)^d, ε = 1/n, T ≥ 2:
||A||² ≤ 5⟨A, ΔA⟩ + 2||Q_strA||², so Δ + aQ_str^†Q_str ≥ min(1/5, a/2), uniformly in n, T and d.
*Proof:* Weitzenböck splits into scalar problems; the straight average is a probability density of sup ≤ 1 on a 2-block
slab; the slab Neumann Poincaré constant is ≥ 1; each point lies in exactly two slabs (l.961-974). Check c9 (B): measured
λ_min = a at every tested size, above the bound.

**Lemma 2.2 (A1: abelian averaging contracts the action, sharp constant L^{4-d}; l.3849-3881).** For the linearised S4'
A' := avg_{σ,y}A(T^σ_y): (i) dA'(P) = avg_{y∈B(X)}Φ_A(sq_y), the flux through the straight L × L square at y;
(ii) Σ_P|dA'(P)|² ≤ L^{4-d}Σ_p|dA(p)|². **In d = 4 the coarse action never exceeds the fine action, at any depth.** The
constant is a supremum over torus sizes, approached and not attained for real A (l.3853-3856). *Proof:* pairing the four
links of P with the same σ cancels the axial legs; Schur test with row sums L² and column sums L^{2-d} (l.3857-3870).
Check c16(A1): ||M||² = 9, 3, 1.000000 = L^{4-d} in d = 2, 3, 4.

**Lemma 2.3 (CR, constant reproduction; l.1927-1940).** (i) In coarse units d(QB)/L² is a probability average of fine
curvatures (weights ≥ 0, row sums 1, column sums exactly L^{-4}); composite averages are again probability weights.
(ii) For every B and every constant 2-form F: |QB(c) - ∫_{S_c}B| ≤ 2L(L-1)max_{window(c)}|dB - F|. The linear part of the
averaging defect vanishes on constant curvature by centring alone (L odd).

**Lemma 2.4 (IT-str; l.2385-2398).** The composite of m one-step straight averages equals the direct straight average of
side L^m (and likewise for transposes). On co-closed inputs (Q_root^T)^m = Q_str^{(L^m)T}.

**Lemma 2.5 (N2-a, gauge orbits; l.2181-2218).** (Abelian.) The residuals r_i and dB_0 are the same at every minimiser,
depend linearly on B_k, depend on B_k only through dB_k, and vanish when dB_k = 0, including the non-exact flat classes.
(SU(N), the one non-abelian statement in this package, exact.) For the soft chain with the tree-level exponent of the
normalised kernel, the SET of values of any gauge-invariant quantity over global minimisers is an invariant of the coarse
gauge orbit of V_k, and on every flat V_k the minimum is 0 with every plaquette 1 (l.2185-2190; uniqueness of the SU(N)
minimiser is NOT shown).

**Theorem 2.6 (N2-E, curvature energy bound; l.2219-2254).** For every B_k, uniformly in k ≥ 1 and T:
**E_k(B_k) ≤ C_E(1 + κ_+)||dB_k||², C_E := 1.2·10⁸** (absolute, not optimised). *Proof:* a test chain from cubical
Whitney forms of B_k; CR (ii) with F the Whitney curvature at a point gives per-level residuals ~L^{-m}, so no level-count
factor appears (the marginal d = 4 count is beaten by centring). **Corollary (N2-ℓ², l.2255-2258):** at every minimiser
κ_{k-1}||r_{k-1}||² ≤ Σ_iκ_i||r_i||² ≤ 2C_E(1 + κ_+)||dB_k||², and ||dB_0||² ≤ 2C_E(1 + κ_+)||dB_k||².

**Lemma 2.7 (E-low, the energy controls the curvature; l.3350-3360).** For every B_k, k ≥ 1, T:
**E_k(B_k) ≥ c_E||dB_k||², c_E := 2κ/(π²(κ + 4π²R̄)), R̄ := 1 + κ̂/(L² - 1) + κ/9** (κ = κ_{k-1}; c_E = 0.004069 at κ ≡ 1,
L = 3).
*Proof.* By the dual reduction (Lemma 3.4) E_k = (κ/2)Σ_p min_tΣ_μP̂_μ^{-1}|b̂_μ - ν_μt|². P̂_μ^{-1} = φ/β_μ with
β_μ ≤ κ + 4π²R̄ (δ ≤ 1, R_μ ≤ R̄, φ ≤ 4π² on the cube). min_tΣ_μ|b̂_μ - ν_μt|² = |F̂|²/ψ (Lagrange identity, F̂ = ν∧b̂) and
φ/ψ ≥ 4/π². So every p contributes ≥ (κ/2)(4/π²)|F̂(p)|²/(κ + 4π²R̄); Parseval. ∎
Instance (c31 E): the exact per-mode minimum is 0.0310, 0.0297, 0.0296 at κ ≡ 1 (k = 1, 2, 3), at p = (π, π, π, π): 7.3-7.6
times c_E; 9.1 times at κ = (0.5, 2). Chain-level (LSMR) ratios agree.

---

## 3. Sup bounds and local energy (the linear half of the soft background-field problem)

**Lemma 3.1 (J-str, the soft current has no funnel part; l.1941-1959).** At every critical point of Setting SC:
(a) d*r_i = 0 for every i; (b) r_{i-1} = (κ_i/κ_{i-1})Q_str^Tr_i and J_0 := d*dB_0 = -κ_0Q_str^Tr_0;
(c) sup|r_i| ≤ (κ_{k-1}/κ_i)L^{-3(k-1-i)}sup|r_{k-1}|, and in coarse units **sup|J^c_0| ≤ κ_{k-1}sup|r_{k-1}|, uniformly in k.**
*Proof:* Euler-Lagrange equations; d* of the level-0 equation with d*Q^T = ev^Td* gives co-closedness by induction;
Q^T = Q_str^T - h^Td* kills the funnel term on co-closed r; ||Q_str^T||_{∞→∞} = L^{-3}. The S4' funnels drop out of the
soft current exactly at critical points.

**Lemma 3.2 (LES, lattice elliptic step, Campanato form; l.1960-1989).** If a real 2-form F on Z⁴ satisfies dF = K, d*F = J,
|F| ≤ F_0, |J| ≤ J_0, |K| ≤ K_0 on a box Q_R(x_0), R ≥ 16, then for every α ∈ (0, 1) there is an absolute C_α with
Osc_2(F; Q_ρ(x)) ≤ C_α(ρ/R)^α(F_0 + R(J_0 + K_0)) for x ∈ Q_{R/2}(x_0), 1 ≤ ρ ≤ R/4. (Constants absolute, not computed.)
**Lemma 3.2' (LES-sup; l.2265-2271):** without the a priori sup bound, sup_{Q_{R/2}}|F| ≤ C[(R^{-4}Σ_{Q_R}|F|²)^{1/2} + R(J_0 + K_0)].
**Lemma 3.2'' (LES-div; l.3271-3284):** for -Δu = Σ_a∂_a^-g_a + h on Q_R, R ≥ 16, the Campanato seminorm of ∇u at scales
≤ R/4 is ≤ C_α[R^{-α}(R^{-4}ψ(R/4))^{1/2} + [g]_α + R^{1-α}sup|h|] (the lattice Schauder step C^{0,α} → C^{1,α}).

**Proposition 3.3 (BG-b-lin; l.1990-2018).** At a critical point with **(H1)** sup|f_0| ≤ F_0 and **(H2)** sup|r_{k-1}| ≤ R_top,
the sub-block regularity condition BG-b (the soft analogue of Balaban's CMP 109 (1.2) curvature-and-current condition)
holds uniformly in k and T for the levels n = k - j ≥ 1, with M_2 = (1 + 2L²)(F_0 + 6κ̂R_top) + κ̂L³R_top and
M_3 = C(L, α)(F_0 + (κ_{k-1} + κ̂)R_top). The n = 0 term needs the current step's residual (l.1997-2000).

**Lemma 3.4 (LED-dual, dual reduction; l.2400-2418).** Let r := r_{k-1} and P := Σ_m(κ_{k-1}/κ_{k-1-m})Q_str^{(L^m)}Q_str^{(L^m)T}
+ κ_{k-1}Q_str^{(n)}Δ^{-1}Q_str^{(n)T}. Then r is the unique minimiser over co-closed zero-mean forms of ½⟨s, Ps⟩ + ⟨s, B_k⟩,
the other residuals and J_0 follow from r by transport, and **E_k(B_k) = (κ_{k-1}/2)⟨r, Pr⟩.**

**Lemma 3.5 (LED-symb; l.2419-2439)** gives the explicit symbols: P̂, the F̂ ↦ r̂ symbol
r̂_μ = -P̂_μ^{-1}Σ_νP̂_ν^{-1}ν̄_νF̂_{νμ}/Σ_ν|ν_ν|²P̂_ν^{-1}, and the Bloch formula for f_0 at each fine offset u.
**Lemma 3.6 (WA; l.2440-2455):** symbols of homogeneous type a > 0 at p = 0 (C⁵ elsewhere) have ℓ¹ kernels.
**Proposition 3.7 (LED-unif; l.2456-2501):** the symbol bounds of WA hold uniformly in k ≥ 1, T, u for 𝓡̂ (a = 2) and for
𝒦̂_u + Π_coex (a = 1); the naive extension of the f_0 map to all 2-forms contains the degree-0 projector Π_ex (|x|^{-4} tail).

**Theorem 3.8 (N2-lin, sup forms; l.2502-2516).** For every B_k, uniformly in k ≥ 1 and T:
**(H2) sup|r_{k-1}| ≤ C_R sup|dB_k|, (H1) sup|f_0| ≤ C_f sup|dB_k|**, C_R, C_f depending only on (L, κ_±) (through the
absolute, uncomputed constants of WA). Hence the local energy bound **(LED)** E_loc(C) ≤ (243C_f² + 183κ̂κ_+C_R²)sup|dB_k|²
(the chain energy carried by a 3⁴ block of coarse cubes), and BG-b holds for the linearised chain at small coarse curvature
(levels n ≥ 1). **Proposition N2-red (l.2259-2274)** gives (H1) + (H2) ⇐ (LED) independently.

---

## 4. Exponential locality

**Lemma 4.1 (EXP-id, exact cancellation; l.2665-2690).** On the cube minus 0: P̂_μ = β_μ/φ, D = φΣ, aΣ = φΨ, so
**𝓡̂_{μ,(νμ)} = -aν̄_ν/(β_μβ_νΨ) = -φν̄_ν/(β_μβ_νΣ)**, and the B_k-symbols of r and of f_0 (K = 0 alias) are built from
analytic factors only: **the 1/φ of the fine Green's function cancels exactly** (identity Δ_α = φ_αδ_α).

**Theorem 4.2 (N2-exp; l.2735-2772) and Theorem 4.2' (N2-exp'; l.3113-3168).** Let m_* (resp. m_*') be the minimum over
κ ∈ [κ_-, κ_+] of the largest η ≤ 0.1 for which the explicit strip conditions of Lemma EXP-strip (P1)-(P7) plus the f_0
condition (resp. Lemma EXP-strip' (S1)-(S7)) hold for some r_0 (l.2735-2738, l.3148-3150). Then, uniformly in k ≥ 1, T
and the fine offset u:
- (i) the symbol 𝓡̂ (F ↦ r_{k-1}, on ALL 2-forms F) and the B_k-symbols B_k ↦ r_{k-1}, B_k ↦ f_0 extend analytically to
  the strip {|Im p_α| < m_*'} and are bounded there by M = M(L, κ_±);
- (ii) every entry of the infinite-lattice kernels obeys **|K(X)| ≤ Me^{-m'|X|_1} for every m' < m_*'**; torus kernels
  are the periodisations.
M is explicit for 𝓡̂ from the displayed bounds of the proof (|a| ≤ κe^{4η}, |β| ≥ b_*/2, |Ψ| ≥ Ψ_L, Re Σ lower bound); for
the f_0 symbols it also involves the uncomputed absolute constants of LED-unif (2). By J-str (c) the kernels B_k ↦ r_i
and B_k ↦ J^c_0 are exponential too (Corollary N2-exp-b, l.2773-2798).

**Proven rate vs measured rate (L = 3).**

| | κ = 0.25 | κ = 1 | κ = 4 | κ̂ = 16 |
|---|---|---|---|---|
| m_* (N2-exp), valid (η, r_0) pairs | 0.0077 (r_0 = 0.37) | 0.0111 (0.57) | 0.0117 (0.65) | 0.0037 (κ = 0.25), 0.0082 (κ = 4) |
| m_*' (N2-exp') | 0.0273 (0.37) | **0.0384** (0.70) | 0.0306 (0.90) | 0.0140, 0.0226, 0.0216 (κ = 0.25, 1, 4) |
| located rate (numerical, NOT proven): nearest complex zero of Ψ·Πβ on p = (iw, 0, 0, 0), k = 1, 2 (3) | 0.50, 0.48 | 1.036, 0.987 (0.982) | 2.46, 2.37 | — |

Every (η, r_0) pair satisfies every condition in 30-digit arithmetic (c30 A; independently recomputed by
REVIEW_S15_CONVERGENCE). The located rate scales like √κ, the mass of the soft constraint; m_*' is about 1/25 of it at
κ = 1. Fitted decay rates from kernel profiles (c28 C) are pre-asymptotic (1.26-1.71 per coarse unit on the pre-registered
window; 0.88-0.97 from post-run three-parameter fits), consistent with the located rate. For the polymer bound downstream
(node N6, §10), Theorem 5.1 needs a rate > 3κ_0 + 3 ≈ 457 in block units, so the proven rate alone requires blocks of side
M ≳ 457/m_*' ≈ 1.2·10⁴ (≈ 470 at the located rate).

**Corollary 4.3 (what is exponential and what is not; l.2773-2798).** Exponential: 𝓡 on all 2-forms; the B_k-kernels of
r_{k-1}, r_i, J^c_0, f_0. Not exponential: the unrestricted f_0 extension F ↦ 𝒦̂_uF̂ (the Π_ex term, |x|^{-4}), and the
F-representative 𝒦̂_u + Π_coex (power tail, c28 C5). The global question left open there is answered by Lemma 4.4.

### Lemma 4.4 (F-df_0: an exponentially local F-representative of the fine-curvature map) — PROVEN in session 16, UNREVIEWED
(l.3414-3469.) Fix a fine offset u. Let 𝔅(p) be the B_k-symbol of f_0 at offset u, f̂_0(n· + u)_{ρσ} = Σ_v𝔅^v_{ρσ}b̂_v; by
Theorem 4.2' (i) its entries are analytic and 2π-periodic on S := {|Im p_α| < m_*'}, |𝔅| ≤ M. Define
(E_{<α}g)(p) := g(0, …, 0, p_α, …, p_4) (first α - 1 coordinates set to 0), E_α := evaluation at p_α = 0,
(T_αg) := (g - E_αg)/ν_α (extended by continuity), and for α < β the 6-vector **h_{αβ} := T_αE_{<α}𝔅^β**,
h_{βα} := -h_{αβ}. Let 𝒦^{ax}_u have symbol F̂ ↦ Σ_{α<β}h_{αβ}F̂_{αβ}. Then, uniformly in k ≥ 1, T, u:
- (i) **𝒦^{ax}_u(dB_k) = f_0(n· + u)** for every B_k: an extension of F ↦ f_0 (defined on exact F) to ALL coarse 2-forms;
- (ii) for every 0 < m' < m_*': **|h| ≤ M_ax := max(2, (π/2)e^{m'}/(m_*' - m'))·M ≤ 2M/(m_*' - m')** on {|Im p_α| ≤ m'}, so
  **|K^{ax}_u(X)| ≤ M_ax e^{-m'|X|_1}**;
- (iii) with Corollary 4.3, both gauge-invariant outputs (r_{k-1}, f_0) have exponential kernels in the coarse curvature F.

*Proof.* (0) f_0 depends on B_k only through dB_k (Lemma 2.5), so Σ_vν_v𝔅^v = 0 on every torus grid, hence (density of the
grids, analyticity) on S. (1) E_{<α} keeps analyticity, periodicity and the sup. For T_α in one variable w: ν(w) = e^{iw} - 1
has simple zeros exactly at 2πZ, where g(w) - g(0) also vanishes (periodicity), so T_αg is analytic and periodic. On
|Im w| ≤ m': if |Re w| ∈ [π/2, π], Re e^{iw} ≤ 0, so |ν| ≥ 1 and |T_αg| ≤ 2M; if |Re w| ≤ π/2, g(w) - g(0) = w∫_0^1g'(tw)dt with
|g'| ≤ M/(m_*' - m') (Cauchy), and |ν(w)| = |w||∫_0^1e^{itw}dt| ≥ (2/π)e^{-m'}|w|, so |T_αg| ≤ (π/2)e^{m'}M/(m_*' - m').
(2) Telescoping: 𝔅^v = Σ_{α<v}(E_{<α} - E_{<α+1})𝔅^v + E_{<v}𝔅^v = Σ_{α<v}ν_αh_{αv} + E_{<v}𝔅^v. Evaluating the identity of
(0) under E_{<v} and E_{<v+1} (ν_μ(0) = 0 for μ < v) and subtracting gives ν_vE_{<v}𝔅^v = -ν_vΣ_{μ>v}ν_μh_{vμ}, so
E_{<v}𝔅^v = Σ_{μ>v}ν_μh_{μv}; hence **𝔅^v = Σ_μν_μh_{μv}.** (3) With (dB)^_{αβ} = ν_αb̂_β - ν_βb̂_α and antisymmetry,
Σ_{α<β}h_{αβ}(dB)^_{αβ} = Σ_vb̂_vΣ_μν_μh_{μv} = f̂_0; both sides vanish at p = 0. (4) Paley-Wiener and Poisson, as in
Theorem 4.2. ∎
Remarks: the representative is not unique and depends on the coordinate order (the average over the 24 orders is a
permutation-covariant representative with the same bound); it is not the Coulomb representative, which is non-analytic at
p = 0. c31 F: identity (2)-(3) on the actual f_0 symbol to ≤ 5.0e-16, gauge invariance ≤ 3.7e-16 (strip bound not tested).
The name is historical (PROOF l.2789-2797 asked for "F ↦ df_0, the fine CURVATURE response on ALL 2-forms"); the route
sketched there through dΠ_ex is not used.

---

## 5. The cluster expansion (Dimock's polymer theorem, re-proven in d = 4)

**Theorem 5.1 (Theorem CE = Dimock I Thm 27 in corrected form; l.1744-1915).** Setting: unit cubes of a torus (Z/TZ)⁴, T ≥ 3;
polymers are *-connected cube sets; d(X) = the infimum of lengths of connected unions of segments in ∪X meeting every
(closed) cube of X (the touching-tree reading of Dimock's (119)); fields on sites, μ a product probability measure, H(X, Φ)
complex, depending on Φ|_X. If |H(X)| ≤ H_0e^{-κd(X)} on supp μ with **κ > 3κ_0 + 3** and
**H_0 ≤ c_0(κ) := min{log 2, (32K_0)^{-1}e^{-2(κ-κ_0)}, (8B)^{-1}e^{-2(κ-3κ_0-2)}}**, then ∫exp(Σ_XH(X))dμ = exp(Σ_YH#(Y)) with
H# local, supported on polymers, and **|H#(Y)| ≤ C_1H_0e^{-(κ-3κ_0-3)d(Y)}**. Constants (with Lemma CE-geo'):
**κ_0 = 16 log 12800 ≈ 151.3** (so κ > ≈ 457), K_0 = e^{κ_0}/6400, C_K = 32eK_0, B = C_Ke^{κ_0}K_0, C_1 = 2κ_0B (l.1812-1814,
l.2158-2168).
Proof structure: Mayer expansion (step 1), integration over disjoint polymers (step 2), exponentiation as an analytic
identity on a closed polydisc, replacing a formal-series step (step 3), convergence through the tree-graph inequality
Lemma TG (Penrose partition scheme, written in full, l.1786-1804) and Cayley's formula (step 4). Four textual
discrepancies of the source were repaired and one definitional difference (polymer class) recorded (l.1909-1915).
- **Lemma CE-geo' (l.2141-2172):** |X| ≤ 2^d + 2^{d-1}√d·d(X), so |X| ≤ 16(1 + d(X)) in d = 4; this proves the upper
  inequality of Dimock's (122), quoted there without proof. Check c25: 6045 segment unions, no violation, sharp at a corner.
- **Proposition CE-κ, a quantifier-order remark (l.1859-1892).** Under the touching-tree reading no constants c_0, C_1
  depending on d only can serve for every κ: a six-bond Ising finite-difference argument gives Δ = log(1 + tanh(h)⁶) > 0
  independent of κ, against a bound → 0. **Credit:** Dimock's statement of Thm 27 places c_0 = c_0(d) before κ, but his own
  proof remarks (p.40) "So c0 does depend on κ"; CE-κ shows that dependence is necessary, i.e. it corrects the statement's
  quantifiers exactly as the author's remark does. His mathematics and his application (κ fixed once) are unaffected.
- **Remark CE-cx (l.1893-1899):** the theorem holds for complex product measures with ||μ_x|| ≤ e^δ, with κ → κ - δmκ_0.
- Check c21 (criteria first): 13/13 PASS (tree-graph identity on all connected graphs n ≤ 5 and 300 random 6-vertex
  graphs; Mayer grouping by full enumeration; CE-κ's Δ to 60 digits).

---

## 6. Gauge fixing of the soft step, and sources

### 6.1 Gauge fixing (one abelian linearised soft step)
**Lemma 6.1 (FP-ab, linear Faddeev-Popov; l.2321-2355).** For Λ = R^m acting freely by A ↦ A + Γλ on R^n, I ≥ 0 invariant
with ∫_{(ΓΛ)^⊥}I < ∞, and χ = (χ_1, χ_2) linear with χΓ invertible:
∫I(A)δ(χ_1A)e^{-½|χ_2A|²}dA = (2π)^{m_2/2}|det χΓ|^{-1}det(Γ^TΓ)^{1/2}∫_{(ΓΛ)^⊥}I. *Proof:* change variables A = A_⊥ + Γλ,
substitute μ = χΓλ, Fubini. ∎ Applied to the soft step: the legitimate fixing is **δ(h)·e^{-½||P_resd*A||²}**, P_res the
projector onto the residual group Λ_res = {λ(c_X) = 0, block means 0}, with a constant independent of A, the data, κ and the
integrand; the slice alone is not admissible, and the earlier "double fixing" with the full Δ carries an explicit Gaussian
weight W(A), so it is not an identity (l.2339-2344). The fluctuation operator O_FP := d*d + κQ^TQ + dP_resd* on the slice
has a uniform gap **iff** the physical gap below holds.

**Proposition 6.2 (PG, physical gap; l.2601-2618).** For one step of block side n (odd ≥ 3), coarse torus T ≥ 2, in coarse
units: **||dA||² + κ||QA||² ≥ c_PG||A||² on Phys, c_PG := min(1, κ)/(3.5·10⁶)**, and **O_FP ≥ min(c_PG, 4)** on the slice,
uniformly in n and T. Phys := {h(A) = 0, d*A ∈ span(δ_{c_X}, 1_{B(X)})}. Ingredients: face fluxes (PG-flux), the orbit
identity (PG-orbit), a cheap extension with constants 4.25·10⁵ and 160 (PG-ext), the line trace of h with C_3 ≤ 14
(PG-line). Check c24 measured λ_min(O_FP) = 0.27-0.43 at small sizes (the constant is crude).

**Proposition 6.3 (PG^{(k)}, the composite slice; l.2830-2862).** For the k-fold composite root map Q^{(k)}, the slice
functional obeys **ε²|h^{(k)}(X)|² ≤ (4L²/(L - 1))||A||²_{B(X)}** with no trace loss (Lemma IT-line), and
**||dA||² + κ||Q^{(k)}A||² ≥ (min(1, κ)/C_IT)||A||² on Phys^{(k)}, C_IT(L) := 3.4·10⁶ + 69 + 44160L²/(L - 1) ≤ 3.6·10⁶ at
L = 3**, uniformly in k ≥ 1 and T ≥ 2. Check c28 D: recursion, telescoping and the IT-line ratio (≤ 1e-4 of the bound).

**Proposition 6.4 (per-level abelian gap; NA-lev (c), l.3361-3367).** The level-i fluctuation form E_i(A) + (κ_i/2)||QA||²
(E_i the effective chain energy with top level i) obeys, on the one-level Phys, **≥ min(c_E, κ_i/2)·c_1||A||²_B,
c_1 := 1/(3.5·10⁶)**, uniformly in i, k, T (Lemma 2.7 with k → i, FP-ab, PG at n = L).

### 6.2 Sources (the general-source linear estimate at the trivial background)
**Lemma 6.5 (SRC-id and SRC-all; l.2995-3040, l.3204-3221).** With co-closed zero-mean sources j_l at levels 0 ≤ l ≤ k - 1:
s_i := κ_ir_i are co-closed and obey s_i = (Q^{(i+1→k)})^Ts - Σ_{l=i+1}^{k-1}(Q^{(i+1→l)})^Tj_l; J_0 = j_tot - (Q^{(0→k)})^Ts; and
**r_{k-1}(j; B_k) = r_{k-1}(0; B_k - g_eff)** with an explicit effective datum g_eff. At the symbol level the K = 0 part of
the response to a fine source is analytic: the screening identity **β - κ|W|² = φR** cancels the 1/φ of Δ^{-1}.
Checks: c29 A (≤ 1.1e-12), c30 B (≤ 5.2e-13), c30 C1/C2 (≤ 3.1e-10).

**Lemma 6.6 (REC, Green reciprocity; l.3222-3229).** For (B_i) critical with B_k = 0 and sources j_l = d_l^*G_l, and (B'_i)
critical with data B'_k and no sources: **κ_{k-1}⟨r_{k-1}, B'_k⟩ = Σ_l⟨G_l, d_lB'_l⟩.** So the source-to-r map is the
transpose of the data-to-curvature maps. *Proof:* the symmetric bilinear form of the chain, with its top components,
evaluated both ways. ∎ (c30 C3: ≤ 4.3e-9.)

**Lemma 6.7 (KF; l.3230-3239).** The kernel of B_k ↦ f_l obeys |K_{f_l}(P; X, μ)| ≤ M_fe^{-m'd(P, X)},
M_f := Me^{8m'}(1 + 6κ̂), uniformly in k, T, l.

**Theorem 6.8 (G♯_0-soft; l.3240-3270).** In Setting SC with sources j_l = d_l^*G_l and data B_k, uniformly in k ≥ 1, T, X_0
and the level weights, for 0 ≤ m < m' < m_*', μ := m' - m, S(μ) := coth⁴(μ/2):
- (a) **||r_{k-1}||_{∞,m} ≤ C_topΣ_l||G_l||_{∞,m} + C_D||B_k||_{D,m} ≤ C_topΩ||G||_Y + C_D||B_k||_{D,m}**, with
  C_top := 6M_fe^{4μ}S(μ)/κ_{k-1}, C_D := 4MS(μ);
- (b) L^{k-1-i}||r_i||_{∞,m} ≤ κ_i^{-1}e^{5m}[κ_{k-1}L^{-(k-1-i)}||r_{k-1}||_{∞,m} + 6Σ_{l>i}||G_l||_{∞,m}];
- hence **||r||_{X_s} ≤ C_s(Ω||G||_Y + ||B_k||_{D,m})**, C_s explicit in M, κ_±.
*Proof:* linearity; the data part from Theorem 4.2 (ii); the source part from REC with KF, where the plaquette count per
coarse cell cancels the L-powers exactly (one O(1) per source level); (b) from SRC-all with Q^Td* = d*W^T,
||W^T||_{∞→∞} = L^{-2} per step. ∎ **The marginal count:** each source level contributes O(1) to the proven bound, so the
bound is uniform exactly when Ω < ∞ (e.g. ω_l = L^{θ(k-l)}). The statements that the bound is attained in order of
magnitude, and that the soft remainders supply such weights, are ARGUED only (l.3258-3262).

---

## 7. The Gaussian abelian model

**Proposition 7.1 (A2; l.3882-3910).** For the noncompact abelian 4D gauge field with law e^{-(β/2)||dA||²} and the
linearised S4' levels, a level-m cell is "bad" if some plaquette has |F^(m)_P| ≥ η. For every set R of cells of one family,
μ(every cell of R bad) ≤ (2^{12}e^{-βη²/4})^{|R|}, at every depth, uniformly in the UV cutoff and the volume. *Proof:* A1
(||M_m|| ≤ 1), then a Gaussian exponential moment and Markov. ∎ It shows the large-field suppression is natural in the
action (an L² quantity) at every depth in the free 4D theory; it is not SU(N), where the coupling runs.

---

## 8. Check inventory (linear package only)

Pre-registration: from c18c on, every check has a criteria file written before the script (`checks/cNN_criteria.md`); a
FAIL "as pre-registered" means the criterion as written failed and was not edited. Earlier checks (c8, c9, c16, c17) predate
criteria files: they are instances with stated targets, no pre-registered PASS line.

| Check | Tests | Outcome |
|---|---|---|
| c8 (f) | Q_root = Q_str - dh for U(1) small fields, S4 and S4' | exact, ≤ 2e-16 (no criteria file) |
| c9 (A-C) | Weitzenböck identity; L3g(a)-glob gap; H^{-1} norm of the straight density | exact; λ_min = a ≥ bound; bounded (no criteria file) |
| c16 (A1) | Lemma A1 identity and the constant L^{4-d} | 1e-14; 9, 3, 1.000000; 11/11 (no criteria file) |
| c17 (B) | Lemma B-avg conjugation identity | ≤ 6e-16; independent pairing differs at 2nd order (ratio 3.96) (no criteria file) |
| c21 | Lemma TG, Mayer grouping, truncated cluster series, CE-κ's Δ | 13/13 PASS; re-run in session 11 with I4 (60 digits) 14/14 |
| c23 A | N2-a gauge orbit (Q1), closed data (Q2), N2-E test chain (V1-V2), k-trend (Q3) | V1, V2, Q1, Q2 PASS; **Q3 FAIL as pre-registered** (the k = 1 value is the largest; no growth) |
| c24 | FP-ab admissibility; λ_min(O_FP) at small sizes | V1, Q1 PASS; λ_min 0.27-0.43 informational |
| c25 | Lemma CE-geo' cube count | Q1 PASS (6045 unions; max ratio 1.0000 at a corner) |
| c26 | LED-dual/LED-symb vs LSMR chains; kernel norms vs k and T | A VALID, Q1-Q4 PASS (≤ 4e-13); Q5, Q6, V3 PASS; **Q7 FAIL as pre-registered** (T-growth ratio 1.104 > 1.1; the increments fit a summable c/T tail, informational) |
| c27 | PG ingredients (flux, orbit, constants, line trace) | E1, E2, E4-E6 PASS; **E3 FAIL as pre-registered** (a normalisation flaw in one sub-check: relative error normalised by ~1e-16; absolute errors ≤ 1.1e-15) |
| c28 | EXP-id formulas (A); strip bounds (B); decay rates (C); IT' (D) | A VALID (≤ 2.2e-13); **B FAIL as pre-registered** on a float tie at the sharp point p = 0 (-5.6e-16), all other bounds with margin; C1, C2 PASS; **C3, C4 FAIL as pre-registered** (pre-asymptotic fit window); D PASS |
| c29 A, B | SRC-id identities; EXP-strip' (S1)-(S7) at complex points | A PASS (≤ 1.1e-12); B PASS (sharp ratios 1.000; margins ≥ 4.8) |
| c30 | strip pairs at 30 digits (A); SRC-id f_0 lines (B); SRC-all, REC, transport bound (C); soft constants (D) | A, B, C PASS; D informational (4.64 against the proven 6). C4 vacuous at k = 1 (disclosed) |
| c31 | E-low at symbol and chain level, NA-lev arithmetic (E); F-df_0 factorisation (F) | E PASS; F PASS (strip bound not tested) |

Outside the package, for completeness: c22 and c29 C-D are SU(2) diagnostics (c22 Q3 and c29 C1 FAILED as
pre-registered); c20 is a session-9 model background. Run discipline throughout: one job at a time, nice 10, BLAS threads 1,
no `timeout`; runs from c29 on are without `python3 -I` (the interpreter then does not see numpy), disclosed in each time file.

---

## 9. What this is NOT

- **Not SU(N).** Everything above is the linearisation around the trivial background (N² - 1 decoupled abelian copies),
  except the exact gauge-orbit statement of Lemma 2.5 for SU(N). The SU(N) soft chain (node BG-reg/N2, "B-NA") is reduced in
  PROOF.md to OPEN hypotheses (G♯), (R♯), (FP♯'), not proven; Proposition 6.4's non-abelian extension needs (NA-H) ⊂ B-NA.
- **Not large fields.** The large-field R-operation is untouched here. PROOF.md's LF-count shows that in d = 4 an
  unrenormalised large-field count diverges, so a renormalising large-field step cannot be avoided.
- **Not UV stability.** The target exp(-E_-|T|) ≤ Z_K/Z_ref ≤ exp(E_+|T|) uniformly in the cutoff (L6) is not proven, and
  neither is any of its paper-scale inputs (§10). The package is the linear, translation-invariant, symbol-level part of a
  small-field step.
- **Not the OpenAI / Balaban result.** The announced 2026-10-26 proof is unverified and its write-up was not available;
  nothing here is compared with it. Balaban's own papers CMP 102, 116, 119, 122 I-II were not read (CMP 109 was).
- **Not Balaban's hard-constraint kernel.** The kernel is the soft normalised kernel of decision 4. The averaging coincides
  with Balaban's (0.4) with paired contours (Lemma B-avg), but the constraint differs, so none of his hard-constraint
  results is imported or re-verified here.
- **Not the fluctuation covariance.** The kernels of §3-4 are background-response kernels (B_k ↦ r, f_0). The covariance of
  the gauge-fixed soft Hessian (node N5: ℓ¹ bound, random-walk expansion) is a different object and is OPEN.
- **Not sharp.** The constants are crude: c_PG = 1/(3.5·10⁶), C_E = 1.2·10⁸, m_*' ≈ 1/25 of the located rate, c_E ≈ 1/7 of the
  exact minimum; several constants (LES, WA, LED-unif) are absolute and not computed.
- **Not the D4 lattice.** All of it is on Z⁴; the D4 version is later in the owner's order.

---

## 10. Open items on the path to UV stability

Weights from REVIEW_S15_CONVERGENCE (b): **P** = paper-scale (about one Balaban-sized CMP paper, the analogous paper in
brackets); **s** = session-scale (one to three sessions). Status after session 16.

**Completing this package (s; at most one more session under the owner's wind-down decision):**
- (LED-src): a weighted local-energy bound for the response to level-0 divergence-form sources; with Lemma LES-div it gives
  the fine-level Hölder bound (G♯_0-fine) for level-0 sources (PROOF l.3285-3302) — **s, OPEN**;
- the abelian multi-level per-level-slice gap, then (G♯_0-field), the configuration-norm bound B-NA-red consumes — **s, OPEN**;
- (G♯_0-fine-up): ||f_0||_{X_f,α} ≤ C_up(||G||_Y + ||B_k||_{D,m}) for sources with G_0 = 0 (displayed in PROOF l.3302-3308)
  — **s, OPEN, deferred**;
- Lemma G♯_0-plain: the r-response to a plain (non-divergence-form) level-0 current — **s, OPEN, deferred**;
- Lemma F-df_0 — **closed in session 16 (unreviewed).**

**The critical path beyond the package (REVIEW_S15_CONVERGENCE (b), reproduced; F-df_0 now closed):**
```
L6-soft (UV stability) ⇐ A (small-field package, every scale) + B (large-field R-operation) + C (assembly)
A. small field
 ├─ A1  N2 = BG-reg: the SU(N) soft background field (existence, uniqueness, regularity, decay,
 │      analyticity)  [P: CMP 102 + parts of CMP 99]
 │      ⇐ B-NA-red (proven as an implication)
 │        ├─ (G♯_0-field)  s: ⇐ G♯_0-soft ✓, (G♯_0-fine) ⇐ LED-src (s), G♯_0-fine-up (s), multi-level gap (s)
 │        ├─ (R♯_ω)        s: ⇐ G♯_0-plain (s); marginal 4D Wilson remainder
 │        └─ (FP♯')        s
 │      + N10 non-linear analytic dependence on complex data   [s to P]
 │      + curvature localisation (F-df_0 ✓ for the linear chain) [s]
 ├─ A2  N4 (NA) gap ⇐ NA-H (⊂ A1) + per-block perturbation (s); FP_U(V) locality/analyticity [s to P]
 ├─ A3  N5 soft covariance at general backgrounds: ℓ², ℓ¹, random walk with complex weakening [P: CMP 95/96/99]
 ├─ A4  N6 polymer bound for the soft kernel, rate > 457 in block units, M ≳ 1.2·10⁴  [P: CMP 116]
 ├─ A5  L4a-flow: the coupling flow over all scales, β-function control  [P: CMP 109 Thm 2 / CMP 119]
 └─ A6  N7-N9 (DF1-3'), L1d-soft  [s each, after A1-A4]
B. large field (L5-soft)
 ├─ R4D-iso / D4-norm (proven: isolated cube)
 ├─ W1-loc ⇐ N11, N12 ⇐ A  [s each, given A]
 └─ W2 nested multi-scale large fields; renormalising large-field regions  [P×2: CMP 122 I + II]
C. assembly: per-step bounds → bulk bound  [P: CMP 119]
(off the UV-stability path: D4-obs; L7-L10, F2-F4, C1-C4, E7.0')
```
Size: 6-7 paper-scale nodes, none entered except A1 through reductions; about 15-18 session-scale nodes. In Balaban units
this package is roughly the U = 1 part of CMP 95/96 plus a d = 4 re-proof of Dimock's polymer theorem (REVIEW_S15_CONVERGENCE
(b)).

---

## 11. Provenance and governance

- **Decision 4** (session 9): keep S4' with the soft normalised kernel as the RG kernel; Balaban's (0.4) with the hard
  constraint becomes a comparison branch. It is a proof-technique choice made by the lead, applied by inference from the
  owner's standing TOE-ruleset delegation ("you dont need to ask permissions unless we are editing the axioms",
  2026-10-21, as recorded in the lead's memory); not an axiom or CL change (PROOF l.4550-4556, in the [S12] tally).
- **Correction (session 16).** REVIEW_S15_CONVERGENCE (c) says decision 4 departs from an owner order "Balaban Z^4 standard
  first, then D4". The owner's order means the Z⁴ lattice before the D4 lattice, not the hard constraint before the soft
  one; decision 4 is consistent with it. The review's cost point (the soft kernel forfeits the import option for the
  hard-constraint papers not yet read) stands on its own and is the subject of the planned soft-vs-hard cost session.
- **Next.** Owner decision 2026-10-27: at most one more session on this package, then one session costing the soft-vs-hard
  choice, then a pause until CMP 102, 116, 119 and 122 I-II are available.

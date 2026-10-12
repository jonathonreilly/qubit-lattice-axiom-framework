# C5 R16-2 report: how many tunings put every light charged particle and the photon on one cone?

**Author.** Claude Opus 5.5 probe. This is the same model family as the supervisor and every C5 worker. Unrefereed. Written 2026-10-12, 22:18Z to about 22:55Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R16-2/`. Scripts and outputs are in `S/scripts/`. Every run took under 1 min with `OMP_NUM_THREADS=2`. There were no downloads.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`: the C5 method (`:2302-2320`), round 16 (`:5037-5152`; R16-2 is at `:5065-5083`), F2 (`:2380`) and R9-1 (`:3838-3840`).
- `C5_S17_synthesis.md`: §§0–5, by grep plus `:300-370`.
- `SUMMARY.md` §§21–25 (`:534-675`).
- `C5_R13-7_report.md`, in full, and `vR13-7`.
- `vR13-8`; `vR14-3`; `vR10-1`; `vR8-5`.
- `C5_R10-1_report.md:193-201`; `C5_R14-1_report.md:40-60,184-211`; `C5_R8-5_report.md:250-262`.
- `C4_F2_report.md:82`, the prior-art hit for flavour-universal counting.
- Runners: R13-7 (`r137_onshell.py`, `r85_box_qed_copy.py`, `r101_dirac_moment_copy.py`), R14-1 (`sublum.py`, `r141_wilson.py`) and R10-1 (`r101_scalar_qed.py`), all copied unmodified into `S/scripts/`.
- R16-1's scratch folder was empty when I checked, so nothing was used from it.

**Labels.** **proved** = complete under the stated hypotheses. **checked** = numerics here. **suggested** = argued, not proved. **reading** = an interpretation. **comparator** = literature, RECALLED.

---

## 0. In plain words

1. **The photon couples to charge squared, and that decides the count.** At one loop, species i's speed shift is q_i² times a function F_s(m) that depends only on its spin class and edge. The photon's shift is one number shared by everyone (proved, Lemma Q). A single light-mass tuning can therefore put every species on the photon's cone only if F_s(0⁺) = 0. If F_s(0⁺) ≠ 0, the electron (q² = 1), the up quark (4/9) and the down quark (1/9) sit on three different cones, about 1e-3 apart.
2. **On the edges R16-2 names, F_s(0⁺) never vanishes.**
   - Dirac: F_{1/2}(0⁺) lies between −11.9 and −4.5 (in units of e²/16π²) on 67 law–photon combinations. These are D1(r), R8-5's literal edges, and five photon shapes including R13-7's steep sign-flip boxes.
   - Scalar: F_0(0⁺) lies between −3.6 and −1.6 on 23 combinations of G(b) edges (checked).
   - The dominant piece is bounded, with proof: the Peierls tadpole for Dirac and the seagull for scalars. It is at most −½⟨w(π)⟩ (Dirac) or −¼⟨w(π)⟩ (scalar), that is −7.2 and −3.6 for the naive photon.
     - The bound needs only two things: the edge never rises above the continuum, S(q) ≤ q (Dirac) or u′/2 ≤ q (scalar), and the photon symbol d is nondecreasing.
     - Every edge that stays slower than light along the axes satisfies the first condition, Wilson edges included (proved, Lemma T′; checked in 24 of 24 cases).
     - The remainder (the exchange graphs) is not bounded by proof.
3. **So the answer is neither 1 nor "one per spin class".**
   - If every species has its own kinetic counterterm, n_t = N_s − n_max + 1. Here n_max is the largest number of species that share one charge. That is **7** for the nine SM charged Dirac flavours.
   - If same-charge flavours share one kinetic term, as SM generations do, n_t = the number of (spin, |q|) classes. That is **3** for the SM.
   - Both statements are proved, conditional on F_s(0⁺) ≠ 0 holding for every edge in the class (Lemma F). Lemma F is checked, not proved.
4. **R13-7's "one tuning fixes every light species" holds within one charge class only.** Within a class the leftover is ≤ 1.7e-22 for e, μ, τ and ≤ 7.3e-21 for u, c, t. Both are far below the 2.66e-19 photon-decay comparator.
5. **The "one shape condition per spin class" count of 2 needs edges outside the class.** A Dirac shape zero exists once the band rises above the continuum, S(q) > q. In the tested overshoot family the zero sits at S′_max ≈ 4.4, axis v_max ≈ 4.35 (checked). There the count would be 2 for SM content: one shape condition plus one photon counterterm. By Lemma T′, such an edge cannot be slower than light along the axes.
6. **Against the FIXED readings: OPEN** (worker). COUNTED would need a proved Lemma F; it is checked with a wide margin but not proved. No IR obstruction appeared: the photon side does not depend on λ (proved), and the matter side is flat as λ → 0 (checked).

---

## 1. Hypotheses and classes (stated before any title)

- **Setting** (`TESTS:5067-5070`). One-loop QED on Z³ × ℝ (continuous time), with Peierls coupling along axis paths and Feynman gauge.
  - Photon: R8-5's non-compact photon, W² = Σ_j d(q_j)² + λ², with d = ρ_g q + (1 − ρ_g)2 sin(q/2) and plateau (c₁, c₂). It is naive when c₁ = None.
  - Tested photon shapes: naive, (1.0, 2.0), (2.0, 3.0), (0.5, 1.5), (1.4, 1.6), (2.5, 3.1) and (2.8, 3.1).
  - Species: N_s charged species, with charges q_i ∈ {1, 2/3, 1/3}, spins 0 and ½, and masses m_i a ∈ [1e-23, 1.5e-17].
  - Excluded: non-abelian sectors, W±, two loops, non-Peierls vertices.
- **Edges (one common edge per spin class, shared by all species of that spin; reading of `TESTS:5069`).**
  - **Dirac, D1(b, r)** (R14-1, `C5_R14-1_report.md:184-201`). h = Σ s(k_j)α_j + (m + ΣW(k_j))β, with s = S(b) (|s′| ≤ 1) and W′ = r√(1 − s′²). Tested on b ∈ {1.0, 1.2, 1.4} × r ∈ {0, 0.2, 0.4, 1/√3}.
    - v_max ≤ 1 for r ≤ 1/√3 (R14-1 theorem).
    - The corner masses are m + nW_π, with W_π ∈ [0, 0.32] (`r162_dirac_family_N128.out`).
  - **Dirac, literal BQ** (R8-5, r = 0). S = ρk + (1 − ρ) sin k on the boxes (1, 2), (2, 3), (0.5, 1.5), (1, 3) and (2.5, 3.1).
    - The whole-zone axis v_max at m → 0 is 1.036, 4.320, 1.000, 1.793 and 8.580 respectively. max S′ = 1 in all five (`r162_vmax.out:1-5`).
    - Each literal edge carries seven same-mass corner copies. Those copies are not treated here (§3.8), and the edge is R9-1-excluded (`TESTS:3840`).
  - **Scalar, G(b)** (R14-1, `C5_R14-1_report.md:48`). ε² = m² + Σh(k_j)², with h′ = 1 − sstep((|k| − b)/(π − b)) ∈ [0, 1].
    - |∇ε| < 1 (R14-1).
    - A = u″/2 − 1 ∈ [−11.3, 0] for b ∈ {0.6, …, 2.6} (`r162_vmax.out:9-13`).
- **The stated class 𝒞 for the count.**
  - Separable box Dirac edges, Wilson or not, with s = k and W = 0 on |k| ≤ b, whose symbol never rises above the continuum: s(q) ≤ q on [b, π].
    - This contains every D1(r) and every R8-5 literal edge.
    - It also contains every separable box edge, Wilson edges included, whose axis group velocity is ≤ 1 at small m (Lemma T′).
  - Separable box scalar edges with u′/2 ≤ q on [b, π]. This contains every G(b) and every axis-subluminal box scalar.
  - Photon: t = d² even, periodic and positive. The proved bound of Lemma T′ additionally needs d nondecreasing on [0, π]. That holds for the naive, (1, 2) and (0.5, 1.5) photons; the steep boxes (2, 3), (2.5, 3.1), (2.8, 3.1) and the narrow (1.4, 1.6) are non-monotone and are only checked (`r162_lemmaT_bound.out`).
- **Allowed tunings** (`TESTS:5070`). Each counts once:
  - an edge-shape parameter condition;
  - the photon-kinetic counterterm κ_γ;
  - matter-kinetic counterterms κ_i.
  - Two readings of "matter counterterm" are carried throughout: **(i)** one per species; **(ii)** one per (spin, |q|) class, i.e. same-charge flavours share a kinetic term.
- **Observables.**
  - Matter: the on-shell speed, as in R13-7: δc_i = (c_i² − 1)/2 at p → 0 along an axis.
  - Photon: the dimension-4 photon speed δc_γ. This is R10-1's Theorem D moment for Dirac loops and Theorem T′ for scalar loops (`vR10-1:5`).
  - Units: printed values are per e² × 16π². Physical size is δc = (e²/16π²) × value, with e²/16π² = α/4π = 5.807e-4.
- **IR treatment.**
  - A fixed photon mass λ ∈ {0.05, 0.02, 0.01}.
  - The p-step h = min(0.02, 0.3√(2mλ)), so that the emission threshold E_p < W + E_k holds on the whole grid.
  - m ∈ [0.05, 0.8], extrapolated to m → 0.
  - λ → 0 is a trend only.
- **Subtractions named before any run: none.** κ_γ is a tuning, not a subtraction.
- **Comparator.** ε* = 2.66e-19 for every species and both signs (`C5_R8-5_report.md:261`).
  - It is the γ → e⁺e⁻ bound, 2(m_e/E_γ)² with E_γ = 1.4 PeV (RECALLED E_γ; the product is recomputed here).
  - The species-specific photon-decay bounds 2(m_X/E_γ)² are weaker: 1.1e-14 for μ and 3.0e-8 for t (RECALLED masses). Only ε* is used.
- **Masses at a = ℓ_P** (M_P = 1.221e19 GeV, RECALLED): m_e a = 4.2e-23; m_τ a = 1.46e-19; m_t a = 1.41e-17.
- **SM content in the setting.** With W± excluded and no physical charged scalars, the charged species are nine Dirac flavours: (e, μ, τ) with q² = 1, (u, c, t) with 4/9, and (d, s, b) with 1/9.
  - Colour is a multiplicity in the photon loop only.
  - So N_s = 9, n_max = 3, N_cls = 3, and Σ_j n_j q_j² = 3 + 4 + 1 = 8.

## 2. Prior art (each counted once)

- **R13-7** (`C5_R13-7_report.md:50,111-113,144-148,211`; `vR13-7:24,28`).
  - The on-shell runner, reused unchanged.
  - The tadpole lemma, on the literal edge: an m-independent ⟨(S′ − 1)/(d_x²W)⟩.
  - The "one light-mass tuning suffices physically" reading, which is single-species. The referee: "not uniform in λ, band shape, species, or counterterm structure" (`vR13-7:28`). This report addresses "species" and "counterterm structure" directly.
- **R13-8** (`vR13-8:15-22`). Bookkeeping that charges N_s matter speeds in N_s + 7. Mapped in §3.9.
- **R14-3** (`vR14-3:18`). The shear analogue: one common massless-limit setting suppresses the shear of every light common-edge species by O((ma)²). The difference here is the coupling. The graviton couples universally, but the photon couples ∝ q², so one setting serves one charge class only (§3.1).
- **R10-1.**
  - Theorem D and Theorem T′, the photon moments, are reused.
  - Lemma N(m) (`vR10-1:11`) and its "physically weak" reading, "one shape tuning would null that value for all light species of a given type" (`C5_R10-1_report.md:201`). That reading concerns the photon coefficient, which is one number for all species anyway.
  - The sign theorems (`vR10-1:11`) for the photon side.
- **R8-5** (`vR8-5:7`). The BQ law and the comparator table (`C5_R8-5_report.md:261`).
- **F2.** The 3.1e-17 counterterm size (`TESTS:2380`).
- **C4_F2** (`C4_F2_report.md:82`). The continuum-EFT flavour-universal count for the first generation: 9 relative speeds over SM gauge multiplets, with the graviton among them. Reading (ii) here is its one-loop QED-lattice analogue.
- **O1** (`TESTS:2383`). "One tuning per pair of species" was "not established".
- **R14-1.** The D1(r) and G(b) laws. Their stated v_max is used for the v_max rule.
- **R9-1** (`TESTS:3840`). The literal edge's corner copies are EXCLUDED (Z width).
- **Grep.** "charge class", "q_i²", "per species", "flavour-universal" over `agents/`, `TESTS`, `SUMMARY`. The hits beyond the above were R0, RN_L2 and R3-2, none on this question. Nothing found states the q² obstruction to a single light-mass tuning.

## 3. Results

### 3.1 Lemma Q (charge factorization at one loop). Proved

- **Claim.** In the setting, at one loop:
  - δc_i = q_i² F_{s_i}(m_i; θ_{s_i}, θ_γ, λ);
  - δc_γ = Σ_j n_j q_j² G_{s_j}(m_j; θ_{s_j}).
- **Notation.**
  - θ_s is the spin-s edge and θ_γ is the photon edge.
  - F_s does not depend on the species' charge.
  - G_s depends on neither λ nor θ_γ.
- **Proof.**
  1. A charge-q Peierls phase e^{iqeθ_link} gives one-photon vertices ∝ qe and seagulls ∝ q²e².
  2. The one-loop matter self-energy has one photon line and the species' own propagator. So it is q_i² times a q-independent functional of (θ_s, θ_γ, λ, m_i).
  3. The one-loop vacuum polarization is a sum of single-species loops, each ∝ q_j² n_j, with no internal photon. So λ does not enter.
  4. At external q → 0 the photon sits inside its own box, where D̂(q) = q. So θ_γ does not enter G either.
  5. Tree level is exact on the boxes (D1, BQ and G(b) all have E = √(m² + k²) on the box), so c_tree = 1 for every species and for the photon. ∎
- **Consequence (proved).** After tuning, species i's split is σ_i − σ_γ = q_i²F_{s_i}(m_i) + κ_i − (δc_γ + κ_γ). The photon side is one number. A single setting therefore aligns two same-spin species of different q² only if F_s ≈ 0 at their masses.

### 3.2 Lemma T′ (an upper bound on the tadpole and the seagull). Proved; checked

- **The two terms.**
  - **Dirac.** The Peierls tadpole contributes ⟨(S′(q_x) − 1)/(d_x²W)⟩ + O(m) to c_e² − 1. This is R13-7's tadpole lemma (`C5_R13-7_report.md:111`) extended to Wilson edges: the β-part enters as 2(m + W(p))·t_β, and W = 0 on the box, so the Wilson piece is ∝ m.
    - Checked: the closed form is −10.0061 and the runner's m → 0 extrapolation is −10.0061 (`r162_tadpole_closed.out:1`).
  - **Scalar.** The Peierls seagull is (u(p+q) + u(p−q) − 2u(p))/(2d²) per axis. Since u(p) = p² on the box, it contributes ⟨A(q_x)/(2d_x²W)⟩ to c² − 1, exactly, for all m, with A = u″/2 − 1.
    - Checked: the runner's seagull column equals the closed form, −5.1427 against −5.1427 (`r162_scalar_heavy.out:1-2`).
- **Bound.** Fix q_⊥ and set w(q) = 1/(d(q)²W(q, q_⊥)). If d is nondecreasing on [0, π], then w′ ≤ 0 on (0, π]. Integrating by parts once on [b, π], with (S − q) = 0 at b and S(π) = 0:

  ∫_b^π (S′ − 1)w dq = −πw(π) + ∫_b^π (q − S)w′ dq ≤ −πw(π) < 0   whenever S(q) ≤ q on [b, π].

  Hence the m → 0 Dirac tadpole satisfies **δc_tad ≤ −½⟨w(π)⟩_⊥·16π²**.
  - For the scalar, with u′(π) = 0 and u′/2 = q at b: ∫_b^π A w = −πw(π) + ∫(q − u′/2)w′ ≤ −πw(π) whenever u′/2 ≤ q. So **δc_sea ≤ −¼⟨w(π)⟩_⊥·16π²**.
  - Numerically, the bounds are −7.16 / −3.58 (naive photon), −7.12 / −3.56 (photon (1, 2)) and −7.15 / −3.58 (photon (0.5, 1.5)) (`r162_lemmaT_bound.out:1,3,7`).
  - This is the same integration-by-parts mechanism as R13-7's Theorem Sgn (`C5_R13-7_report.md:157-163`), at first order with w′ ≤ 0 in place of w″ ≥ 0. Counted once.
- **Axis subluminality implies the hypothesis, Wilson edges included (proved).**
  - Dirac: on the axis at m → 0, E = r(k) := |(W(k), s(k))|, so the axis group velocity is r′(k). We have r(b) = b. So if v_max ≤ 1 for small m, then r(k) ≤ k, and hence s ≤ |s| ≤ r ≤ k.
  - Scalar: likewise √u ≤ k, and u′/2 = √u(√u)′ ≤ √u ≤ k.
  - So every edge that is subluminal along the axes, including Wilson edges with s′ > 1 where W ≫ s, lies in 𝒞, and its tadpole or seagull obeys the bound.
  - R8-5's literal edges satisfy S = ρk + (1 − ρ)sin k ≤ k even where they are superluminal: their v_max reaches 8.58 through negative slopes (`r162_vmax.out:1-5`). G(b) has A ≤ 0 and h h′ ≤ q (`r162_vmax.out:9-13`).
- **Checked.** The bound holds in all 24 cases with a monotone photon (`r162_lemmaT_bound.out:2,4,8`):
  - 2 D1 symbols, 3 literal edges and 3 G(b), times 3 photons;
  - measured values −13.0 to −7.36 (Dirac) and −6.03 to −3.65 (scalar), against bounds −7.12 to −7.16 and −3.56 to −3.58.

  For non-monotone photons the hypothesis fails and so does the bound in some cases, e.g. D1 with photon (2.5, 3.1) gives −6.30 against −6.69 (`r162_lemmaT_bound.out:12`). The tadpoles there are still negative (checked).

### 3.3 The scalar on-shell runner (new). Checked

- **Euclidean structure.**
  - Γ₂ = p₀² + ε² + Π, with Π = ⟨S₂⟩ − ½⟨S₁S₁⟩.
  - Vertices are real: temporal (2p₀ − q₀), spatial (u(p_j) − u(k_j))/d_j.
  - Seagulls: 1 (temporal) and (u(p+q) + u(p−q) − 2u(p))/(2d²).
  - The q₀ integrals are in closed form: J₁ = (W + E_k)/(2WE_k(W + E_k − E)(W + E_k + E)) and J₀ = (W²E_k + WE_k² − WE² − 4E_kE²)/(2WE_k(W + E_k − E)(W + E_k + E)).
- **On shell.** E² = ε² + Π(iE_p, p) and c² − 1 = ∂_{p²}Π.
- **Checks.**
  1. J₀ and J₁ against direct q₀ quadrature at p₀ = iE: agreement to 12 digits on 4 points (`r162_j0_check.out:2-5`).
  2. The heavy limit. The scalar analogue of R13-7's Theorem H is δc → ¼⟨A(d_y² + d_z² + λ²)/(d_x²W³)⟩; the spatial exchange is O(1/m). Richardson in 1/m:
     - −2.6132 against the closed form −2.6129 for G(1.0) with the naive photon;
     - −2.2159 against −2.2156 for G(1.4) with photon (1, 2) (`r162_scalar_heavy.out:6,12`).

     This tests the seagull, the temporal exchange and the overall sign.
  3. The spatial exchange reduces on the box to (2p − q)_j², the continuum form. It is not separately tested beyond this structure (stated for the referee).

### 3.4 (a) The small-m expansion, with constants. Checked; one part proved

- **Matter, Dirac on D1** (`r162_slope.out:2,6`, N = 256, λ = 0.05):

  δc_i = q_i²·5.807e-4·[F_{1/2}(0⁺) + F′_{1/2}·(ma) + O((ma)²)], with F_{1/2}(0⁺) ≈ −10.23 (b = 1.4) and −10.37 (b = 1.0), and F′_{1/2} = +0.93 to +1.83 (finite differences, 0.1 → 0.2).

  - The tadpole alone: −10.006 at b = 1.0 (§3.2).
  - The linear term is the Wilson piece. D1 is not chirally symmetric.
- **Literal edges and scalars: F is even in m (proved).**
  - Literal: with W = 0, γ₅h(k; m)γ₅ = h(k; −m), Peierls and A₀ couplings are γ₅-invariant, and the speed is a spectral quantity.
  - Scalars: m enters only through m².
  - So F′ = 0 and the corrections are O((ma)²).
  - Checked: G(1.4) changes by 0.0022 between m = 0.1 and 0.2 (`r162_slope.out:4`).
  - F_0(0⁺) ≈ −2.895 for G(1.4) and −3.186 for G(1.0), with the naive photon (`r162_slope.out:4,8`).
- **Photon.** δc_γ = 5.807e-4 Σ_j n_j q_j² G_{s_j}(m_j).
  - On D1: G_{1/2}(0.05) = +0.083 to +0.665 (`r162_dirac_family_N128.out`, last column).
  - On literal edges: −4.35 to +105.5 (`r162_dirac_literal_N128.out`).
  - On G(b): G_0 = −0.058 to −0.117 (`r162_scalar_family_N128.out`).
  - G is IR-safe: every term of R_D and T′ vanishes on the box (`vR10-1:5`). It does not depend on λ (proved, §3.1).
  - For SM content on D1(1.4, 1/√3): δc_γ ≈ 8 × 0.665 × 5.807e-4 = 3.1e-3.
- **λ → 0 (checked as a trend).**
  - At fixed N = 192 and m = 0.1, D1(1.0, 1/√3) gives −10.187, −10.160 and −10.121 for λ = 0.05, 0.02 and 0.01 (`r162_dirac_conv.out:3,6,9`).
  - G(1.0) gives −3.185, −3.156 and −3.116 (`r162_scalar_conv.out:3,6,9`).
  - These drifts are the same size as the N-drift, about 0.05–0.1. They come from the under-resolved Lorentz-invariant IR region (m, λ below the grid spacing), as R13-7 also saw (`C5_R13-7_report.md:109`).
  - No ln λ or ln m was seen. The tadpole closed form is λ-regular because S′ − 1 = 0 on the box (proved).
  - The claim that the full λ → 0 limit exists uniformly is **suggested**: the IR region lies inside both boxes and is Lorentz-invariant, as in R10-1's localization sketch (`vR10-1:15`).
- **Not seen.** The registered O((ma)² ln ma) term was not resolved. Within the data the F′ values are finite-difference constants.

### 3.5 Lemma F (no shape zero of F_s(0⁺) in the stated class). Checked, not proved

- **Dirac.** Every one of 185 values F_{1/2}(m) at m ∈ {0.05, 0.1, 0.2} lies in [−11.91, −4.50]. They cover 67 law–photon combinations at N = 128/192:
  - 36 D1 combinations (3 b × 4 r × 3 photons);
  - 15 literal combinations (5 boxes × 3 photons);
  - 16 combinations with steep or narrow photon boxes (`r162_dirac_family_N128.out`, `r162_dirac_literal_N128.out`, `r162_steep_photon.out`).

  The smallest |F| is 4.50, for literal (2.5, 3.1) with photon (2.8, 3.1) (`r162_steep_photon.out:2`). Against an N/λ drift of ≤ 0.4, the margin is ≥ 4.
- **Scalar.** All 61 values over 23 G(b) combinations lie in [−3.60, −1.62] (`r162_scalar_family_N128.out`, `r162_steep_photon.out`).
- **Structure (checked).** The tadpole or seagull dominates. It is bounded by Lemma T′.
  - Dirac: the remainder (total minus tadpole, i.e. the Z-graphs and normal graphs) is −1.0 to +1.9 across the tested laws (`r162_dirac_conv.out`, "rest"; family and literal tables; `r162_dip_rise.out`). That is at most 0.27 of the Lemma T′ bound, 7.1.
  - Scalar: the remainder is +0.9 to +2.6, about 35–45% of the seagull and of opposite sign. That is at most 0.73 of the bound, 3.56.
  - **So Lemma F reduces to a remainder bound:**
    - R_{1/2} < ½⟨w(π)⟩ and R_0 < ¼⟨w(π)⟩ (in 16π² units) on 𝒞 with a monotone photon.
    - The bound for the leading term is proved; the remainder bound is checked on these laws only. **Lemma F is not proved.**
- **Inside 𝒞 but beyond D1 and the literal family (checked).** "Dip-and-rise" edges S = ρk + (1 − ρ)(sin k − (β/2)sin 2k), box (0.5, 1.5), naive photon, have S ≤ q but S′ up to 2.06 (β ≤ 2).
  - They give F_{1/2} = −12.7 to −16.1, with tadpole −14.2 to −17.8 and remainder +1.5 to +1.8 (`r162_dip_rise.out:2-5,8-11`).
  - Slope above 1 does not open a zero while S ≤ q.
  - β = 3 leaves 𝒞 (max(S − k) = +0.07) and is still −19.2.
- **Outside 𝒞, a zero exists (checked).** Take the overshoot family S = ρk + (1 − ρ)g sin k with box (0.5, 1.5) and the naive photon. For g > 1, S rises above q (e.g. g sin 2 > 2 at g = 3).
  - F_{1/2} rises from −11.91 (g = 1) to +0.096 (g = 3) (`r162_overshoot_N128.out:7-12`).
  - Bisection gives F_{1/2}(m = 0.1) = 0 at g* = 2.983 (N = 128) and 2.994 (N = 192). There max S′ ≈ 4.4, the axis v_max = 4.35, and G_{1/2} = +75 (`r162_overshoot_root.out:1-2`).
  - So rising above the continuum, S > q, is what opens a shape zero. By Lemma T′ that is incompatible with axis subluminality. Superluminality alone is not enough: literal (2.5, 3.1) has v_max = 8.58 but S ≤ q, and F < 0.

### 3.6 Proposition C (the count). Proved, given Lemma F on 𝒞

- **Hypotheses.**
  - (Q) Lemma Q.
  - (F) |F_s(m; θ)| ≥ φ_s > 0 for every θ ∈ 𝒞 and every m ∈ [0, m_max]. Checked values: φ_{1/2} ≥ 4.5, φ_0 ≥ 1.6.
  - (L) |F_s(m) − F_s(m′)| ≤ L|m − m′|, with L ≤ 2.0 checked.
  - (E) ε_i + ε_j + q²L·Δ(ma)·u < |q_i² − q_j²|·φ_s·u for same-spin pairs with q_i² ≠ q_j², where u = 5.807e-4.
    - Checked: the smallest SM gap is |4/9 − 1/9|·4.5·u = 8.7e-4, against 2ε* + L·m_t a·u = 5.3e-19 + 1.6e-20.
  - A tuning counts as a nonzero κ, or as one equation imposed on the common edge parameters.
- **(i) Per-species counterterms: n_t = Σ_s (N^{(s)} − n_max^{(s)} + 1). For Dirac-only content this is N_s − n_max + 1, i.e. 7 for the SM.**
  - *Lower bound.*
    1. Let Z be the set of species with κ_i = 0. For i, j ∈ Z of one spin, the comparators and (L) give |q_i² − q_j²||F_s|u ≤ ε_i + ε_j + q²LΔ(ma)u. By (E), q_i² = q_j².
    2. No shape condition changes this, because the shape is common to the spin class and (F) holds on all of 𝒞. So Z ∩ (spin s) is contained in one charge class, and at least N^{(s)} − n_max^{(s)} counterterms are needed per spin class.
    3. If equality holds, the untuned class c of each spin must satisfy |q_c²F_s − σ_γ| ≤ ε. That is one further condition per spin class: κ_γ, a counterterm, or a shape equation such as δc_γ(θ) = q_c²F_{1/2}(θ).
    4. On D1 the equation without κ_γ cannot hold: δc_γ > 0 > q_c²F in every tested law (§3.4–3.5), so κ_γ ≠ 0 is forced there.
    5. Using more counterterms only raises the total. ∎
  - *Sufficiency.* Set κ_γ = q_c²F(m_ref) − δc_γ, and κ_i = σ_γ − q_i²F(m_i) for every i outside class c. The leftover is confined to class c and is ≤ q_c²L·Δ(ma)·u (§3.7). ∎
- **(ii) Counterterms per (spin, |q|) class: n_t = N_cls, the number of distinct (spin, q²) classes present. That is 3 for the SM.** The proof is the same, with classes in place of species: at least N_cls − 1 class counterterms, plus one photon-side condition. Shape alignment across spin classes, such as q_D²F_{1/2} = q_S²F_0 (possible in principle, since F_0/F_{1/2} ∈ [0.13, 0.80] over the tested laws), trades one counterterm for one shape condition and leaves the count unchanged.
- **Plain consequence.** Neither reading gives n_t = 1 for content with two or more charge values. In reading (ii), n_t does not depend on N_s; it depends only on how many distinct charges each spin class carries. In reading (i), n_t grows with N_s, so R13-8's "N_s" is right up to an offset of n_max − 1.

### 3.7 (d) Residuals after tuning. Checked

- **Within the lepton class, with κ_γ matched at m_e.** The leftover is ≤ 1·L·(m_τ − m_e)a·u = 2.0 × 1.46e-19 × 5.807e-4 = **1.7e-22**.
- **Within the up class, with one shared class counterterm (reading ii).** For the top relative to the up quark: (4/9)·2.0·1.41e-17·5.807e-4 = **7.3e-21**. Setting the counterterm at the class midpoint halves it.
- **Reading (i).** Every counterterm species is exact at its own mass, so only the untuned class keeps a leftover (1.7e-22).
- **Literal and scalar edges.** F is even in m, so the leftover is O((ma)²u), ≲ 1e-34 even with an m² coefficient of order 100.
- **Against ε* = 2.66e-19.** Every leftover is below it by at least a factor of 36, including the top.
- **Required precision of each tuning.** ε*/(|F|u) ≈ 2.66e-19/(4.5–12 × 5.807e-4) ≈ 4e-17 to 1e-16, matching F2's 3.1e-17 (`TESTS:2380`).

### 3.8 (c) One shape condition for both spin classes? Not available in 𝒞; suggested no elsewhere

- **In 𝒞 (checked).** Neither F_{1/2}(0⁺) nor F_0(0⁺) can be nulled (§3.5), so each (spin, |q|) class needs its own condition (§3.6). The question "one per spin class" does not arise.
- **Outside 𝒞 (suggested; not tested for scalars).** With edges that rise above the continuum, the two zero conditions are different moments on different edges: the Dirac ⟨(S′ − 1)w⟩ plus its remainder, against the scalar ⟨A w⟩ plus its remainder.
  - A shared photon-edge parameter would have to hit both zero sets at once, which is codimension 2 (suggested).
  - The registered expectation's count then becomes 1 + n_spin: 2 for SM Dirac content (one overshoot shape condition plus κ_γ) and 3 with scalars.
- **Not covered.**
  - Subluminal Wilson edges with s′ > 1 where W ≫ s are inside 𝒞. Lemma T′ bounds their tadpole, but their remainder was not computed: no such law was built or run. A subluminal shape zero there would need a remainder larger than 7.1. That is suggested unlikely, not excluded.
  - Photons with non-monotone d, i.e. steep plateaus. The tadpole bound does not apply to them. They were checked negative only on the tested laws.
  - The literal edge's seven corner copies. They are light charged species with their own (tetragonal or cubic) one-loop speeds, so each corner orbit would add conditions (suggested; not computed). The edge is excluded by R9-1 anyway.

### 3.9 (e) Mapping onto R13-8's N_s rows (reading)

R13-8's P,T-even bookkeeping charges N_s matter speeds (`vR13-8:15-18`). In the stated class 𝒞 at one loop, the matter-speed rows plus the photon counterterm cost:
- reading (i): N_s − n_max + 1, i.e. 7 instead of 9 for SM charged Dirac content;
- reading (ii): N_cls, i.e. 3.

Both are conditional on Lemma F. Under edges that rise above the continuum (outside 𝒞, axis v_max ≈ 4.35), the cost would drop to 1 + n_spin = 2. Under no reading is it 1 for multi-charge content (Lemma Q).

## 4. Against the FIXED readings (`TESTS:5080-5082`)

**Worker reading: OPEN.** Same family, unrefereed.

- **COUNTED: not met as registered.** It needs a proof that n_t − 1 tunings do not suffice in a stated class.
  - Proposition C proves both directions *given* Lemma F, that F_s(0⁺) ≠ 0 throughout 𝒞.
  - Lemma F is proved only for its dominant part (Lemma T′: tadpole ≤ −7.1, seagull ≤ −3.56, for monotone photons). The remainder bound is not proved.
  - The full statement is checked on 67 Dirac and 23 scalar law–photon combinations, with margin ≥ 4.5 and ≥ 1.6 against an N/λ drift ≤ 0.4. It is not class-wide.
- **Conditional count, for the referee.**
  - n_t = N_s − n_max + 1, which is 7 for the SM's nine charged Dirac flavours, with per-species counterterms.
  - n_t = N_cls = 3 with per-charge-class counterterms.
  - Both are in 𝒞, to ε* = 2.66e-19, with leftovers ≤ 7.3e-21.
- **The reason for OPEN is not an IR obstruction.** G does not depend on λ (proved), and F is flat in λ to the resolution (checked). The reason is the unproved remainder bound in Lemma F, including on untested subluminal Wilson edges with s′ > 1 and on non-monotone photons (§3.8).
- **Derived parts for the referee:**
  - Lemma Q (charge factorization);
  - Lemma T′ (the tadpole and seagull bounds; axis subluminality implies S ≤ q, Wilson edges included);
  - chiral evenness of F on literal edges;
  - Proposition C's two counting arguments.

## 5. Prices (named, not adopted)

- No axiom text is touched. Edge shapes and counterterms are downstream dynamics (`AX:114-130`). The physical sizes use a = ℓ_P, the scale-reference primitive (`AX:189-190`).
- **P73 (one light-mass e–γ tuning) is refined.** It covers one (spin, |q|) class, not every light species. The matter-speed price is:
  - N_cls tunings (3 for the SM), if same-charge flavours share a kinetic term, which is itself a structural choice;
  - N_s − n_max + 1 (7 for the SM) otherwise.

  Each tuning needs a precision of about 1e-16.
- **Alternative price (outside 𝒞).** A matter edge that rises above the continuum (S > q; tested S′_max ≈ 4.4, axis v_max ≈ 4.35), with one shape condition plus κ_γ: 2 tunings. By Lemma T′ such an edge is necessarily superluminal along an axis, which is what R14-1's subluminal programme was built to avoid.

## 6. Strong-word check

- **"Proved":**
  - Lemma Q (Feynman rules);
  - Lemma T′ (one integration by parts, monotone photon; and the radius argument r′ ≤ v_max);
  - the scalar seagull identity;
  - chiral and m² evenness;
  - Proposition C *given* (F), (L) and (E).
- **"Checked":** every number, with N, λ, h and m stated in the `.out` files.
  - The scalar runner is checked by closed-form q₀ integrals and the heavy limit.
  - The Dirac runner is R13-7's, which is refereed.
- **"Never vanishes" / "no shape zero":** only on the tested laws. Class-wide it is suggested.
- **"F_s(0⁺)":** the extrapolation is from m ≥ 0.05 at λ ≥ 0.01. Uniformity of λ → 0 is suggested.
- **Not claimed:**
  - Lemma F class-wide;
  - the remainder on subluminal Wilson edges with s′ > 1 (not run);
  - anything for the literal corner copies, two loops, W±, non-Peierls vertices, or the O((ma)² ln ma) term.

## 7. For the referee

1. Lemma Q: in particular, that G_s does not depend on θ_γ and λ, and that tree-level c = 1 holds on all three edge families.
2. The scalar runner (`r162_scalar.py:1-60`):
   - the Euclidean Π = ⟨S₂⟩ − ½⟨S₁S₁⟩, with real temporal vertex (2p₀ − q₀) and seagull (u(p+q) + u(p−q) − 2u(p))/(2d²);
   - the closed J₀;
   - the heavy-limit check.
3. Lemma T′:
   - the Wilson extension: is the β-tadpole really O(m) at p → 0 when W(p) = 0 on the box?
   - the boundary terms of the integration by parts;
   - the radius argument that axis v_max ≤ 1 forces |s| ≤ k.
4. Whether a checked Lemma F with margin ≥ 4 suffices for COUNTED "in a stated class", or whether a remainder bound is required. A route is to bound the Z- and normal-graph remainders (Dirac at most 0.27 of the bound, scalar at most 0.73, checked) by the same weight w.
5. Proposition C's definition of a tuning, a nonzero κ or one equation on common shape parameters, and the two counterterm readings.

## 8. Files

All in `S/scripts/`:
- **New:**
  - `r162_laws.py` (D1, photon and G(b) adapters; R14-1's `make` copied);
  - `r162_dirac_scan.py` → `r162_dirac_conv.out`, `r162_dirac_family_N128.out`, `r162_dirac_literal_N128.out`;
  - `r162_scalar.py` → `r162_scalar_heavy.out`, `r162_scalar_conv.out`, `r162_scalar_family_N128.out`;
  - `r162_j0_check.{py,out}`; `r162_slope.{py,out}`; `r162_steep_photon.{py,out}`; `r162_tadpole_closed.{py,out}`; `r162_vmax.{py,out}`; `r162_lemmaT_bound.{py,out}`;
  - `r162_overshoot.py` → `r162_overshoot_N128.out`; `r162_overshoot_root.{py,out}`; `r162_dip_rise.{py,out}`;
  - `r162_test.py`, a smoke test.
- **Unmodified copies:** `r137_onshell.py`, `r85_box_qed_copy.py`, `r101_dirac_moment_copy.py`, `sublum.py`, `r141_wilson_copy.py`.
- **Note.** `r162_overshoot.py` was edited after its run only to add a `__main__` guard so it can be imported. Its numbers come from the pre-edit run of the same code.

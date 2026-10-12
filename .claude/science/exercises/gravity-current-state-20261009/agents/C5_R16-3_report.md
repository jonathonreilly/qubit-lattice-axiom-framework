# C5 R16-3 report: the second graviton polarization — can a slower-than-light edge put T₂g on the matter cone?

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 22:40Z to about 23:20Z. No repository file was edited. No downloads, no web lookups. No pending R15/R16 scratch report was used.

**Scratch.** `S/` = `.../scratchpad/C5/R16-3/`. Scripts and `.out` files are in `S/scripts/`. Every run took under 2 min at `OMP_NUM_THREADS=2`. All code is new (R14-3's formulas re-derived; R14-3's scripts were read, not imported).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: C5 method and readings (`:2302-2320`); the tail/subtraction rule (`:4074`, `:4566`); round 16 head rules (`:5039`); my item R16-3 (`:5087-5104`).
- `agents/C5_R14-3_report.md` (all) and `C5_R14-3_referee_verdict.md` (`vR14-3`, all); `C5_R9-9_report.md:28-160` and `C5_R9-9_referee_verdict.md` (`vR9-9`); `C5_R14-1_referee_verdict.md` (`vR14-1`); `C5_R13-5_referee_verdict.md` (`vR13-5`); `C5_R11-1_referee_verdict.md:10-23` (`vR11-1`); `agents/C5_S17_synthesis.md` (W3/P62/P63 rows and §5); `C5_S14_synthesis.md` (graviton-cone lines); `SUMMARY.md` §§21–25 (`:534-675`).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **Yes: a slower-than-light edge can put T₂g on (or outside) the matter cone.** The trick is a "zigzag" edge. Beyond the box the band goes down and up again several times at full slope (|σ′| = 1, the steepest a subluminal band may have), with sharp turns, between about 0.6/a and the box-face value. Witness **Z1** (§3.2): Ξ_T2g = +3.9e-4 (M vertex) and +2.8e-4 (U vertex) at m = 0.3; +8.1e-4 and +6.2e-4 at m = 0.1. Every point of the band has |σ′| ≤ 1, so it is subluminal at every mass (v_max = 0.98456 at m = 0.3). Checked three ways (two Laplace resolutions, the direct 3D zone grid in both forms at N = 720).
2. **Why (proved identity, plain reading).** Theorem T after integration by parts says Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩, with v_z the pair state's group velocity along the graviton's direction. So the graviton cone moves out exactly when the pair states it couples to move, on (weighted) average, faster than v_z² = 1/5 — the continuum's value. Gentle edges slow the pairs, so Ξ < 0. A zigzag edge keeps low-lying edge states moving at nearly light speed, so it pushes Ξ up, and with low enough, sharp enough valleys it wins in both polarizations.
3. **It needs three things (checked in the families tried):** valleys below about 0.9/a (none positive with every valley above 1.05/a), sharp turns (transition width ≲ 0.15 in k), and a light species (m ≲ 0.3/a). At m = 1 nothing positive was found, even in the relaxed (infinitely-fast-zigzag) problem.
4. **The "every vertex" version fails already on R14-3's W08/W14 (proved + checked).** For a fixed band, "Ξ_T2g < 0 for every nonnegative T₂g-symmetric vertex" is equivalent to I(B) ≤ 0 on the vertex's B-range (Lemma V). W08/W14 have I(B) > 0 at small B, so a T₂g vertex concentrated at small transverse momenta gives Ξ > 0 on them, at m = 1, 0.3 and 0.1.
5. **What can be proved (Theorem B″).** If every gapped valley has gentle flanks (|σ′| ≤ 1/√5 on each monotone stretch ending at it), then Ξ < 0 for every vertex, both polarizations, every mass. This class is strictly larger than 𝒰₀ and contains gapped-valley laws. It cannot contain steep-flanked valleys (W08/W14/Z1 type), and the threshold 1/√5 is the point where the integrand's sign flips.
6. **A simultaneous E_g/T₂g zero exists (checked).** Contrary to the expectation, explicit subluminal laws have Ξ_Eg = Ξ_T2g = 0 at a common mass. This was found separately for the M vertex and for the U vertex, at m = 0.1, 0.03 and 0.01, inside the convex hull of three subluminal laws (§3.6). Cost: **two edge-shape tunings per edge per vertex prescription**. They are mass-dependent only at O((ma)²): Ξ is analytic in m² (proved), with slopes −5.8e-3 (E_g) and −1.65e-2 (T₂g) per unit m².
7. **With P62's shear condition no common zero was found (suggested obstruction).** At every graviton-cone zero, the conditional shear μ_E is +6.0e-3 to +6.6e-3, about twice G(1.0)'s value, not zero. Zigzags lower the kurtosis of the velocity distribution, which pushes μ_E up. The only laws found with μ_E < 0 are terraces, and they have Ξ ≪ 0. So the box route can tune the graviton cone or the free shear by edge shaping, but no tested law does both. Searched families are listed in §3.6; this is not a proof.
8. **Price of the zigzag (reading).** Several heavy edge valleys at 0.35–0.9/a below the box-face energy, plus longer-range hopping. The raw 1D kernel |ε_r| is 2e-7 (Z1) to 5e-6 (the zero laws) at r = 128, against 4.5e-8 for R14-3's G_w*. Every number is conditional on R9-9's vertex prescription and its assumed (standard W1) Ward completion, and on the supplied zero-point vacuum. In the empty Fock vacuum Ξ ≡ 0.

**Against the FIXED readings (`TESTS:5101-5103`): REFUTED (worker reading; referee required).** Explicit, checked subluminal laws have Ξ_T2g > 0 for the law's own M and U vertices at m = 0.3 and 0.1. **Simultaneous E_g/T₂g zero: FOUND** (M and U separately; m = 0.1, 0.03, 0.01). Not found at m = 1. See §4 for how Theorem B″ relates to the DERIVED clause.

---

## 1. Class and hypotheses (stated before any title)

- **Laws (class 𝒮, R14-3's class).** These are separable one-band laws ε² = m² + Σᵢ g(kᵢ) with g = σ², σ ∈ C²[0, π], σ(0) = 0, σσ′(π) = 0 and |σ′| ≤ 1, extended evenly and 2π-periodically (`C5_R14-3_report.md:43-52`). The box is σ′ = 1 on [0, b]. 𝒮 is exactly the set of laws subluminal for every light mass (proved there, confirmed `vR14-3:12`). Gapped valleys (local minima of g with g > 0) are allowed.
- **Construction used here.** σ′ is piecewise constant with values in {1, −1, 0}, blended at each breakpoint by the C^∞ step sstep(x) = e^{−1/x}/(e^{−1/x} + e^{−1/(1−x)}) over a width wt. Adjacent transitions never overlap, so σ′ is pointwise a convex blend of neighbouring values and |σ′| ≤ 1 holds exactly. Convex mixtures of such σ′ profiles stay in 𝒮, and σ′(π) = 0 is kept. The laws are C^∞ but not analytic.
- **Graviton cone.** This is R9-9 Theorem T (`C5_R9-9_report.md:122-131`; confirmed `vR9-9` item 2): Ξ = (1/32)⟨|V|²A_zz/ε⁵⟩. The class 𝒱 has q ∥ z, |V|² ≥ 0 depending on (k_x, k_y) only, and an ultralocal seagull.
  - **Vertices:** M (T₂g 4g_xg_y, E_g (g_x − g_y)²) and U (T₂g 4f_x²f_y², E_g (f_x² − f_y²)²), with f = σσ′ (`C5_R9-9_report.md:44-46`). For Lemma V only, I also use abstract nonnegative T₂g-symmetric vertices.
  - **Ward requirement:** **standard first-order W1** in R9-9's form, D = d e^{iq/2}. For the pair-creating stress this is **assumed, not built** (`vR9-9` item 1). No second-order identity is used, standard or deformed (deformed W2 is R16-5).
  - **Vacuum:** class (Z), the supplied scalar zero-point vacuum. In R8-2's empty Fock vacuum, Ξ ≡ 0 and μ_E ≡ 0.
  - **Meaning of Ξ:** the graviton-cone shift relative to the bare cone, not the dressed graviton–matter split (`vR9-9` item 5). In R11-1's dD-M prescription the light-matter split tends to −κ_lat Ξ (`vR11-1:23`, reading).
- **Shear (P62 check).** R9-2/R14-3's conditional free shear, μ_E = (1/12)⟨(3f_x²f_y² − f_x⁴)/ε³⟩ (`C5_R14-3_report.md:88`, confirmed `vR14-3:5`).
- **Excluded (per item):** pairing; deformed W2; matter's own graviton-loop shift (R11-1(b)). Also not addressed: non-separable and Wilson laws, q off-axis, two loops, k_z-dependent vertices.
- **Round-16 head rules (`TESTS:5039`).**
  - Every law below states its whole-zone v_max (d = 3; exact bisection for separable laws).
  - No frame-tied kernel is introduced: the lattice frame is the only frame, and no self-force question arises in a static one-loop coefficient.
  - The Ward requirement is the standard W1, assumed.
- **Tail rule (`TESTS:4074`).** The only tail clause (§3.7) uses raw Fourier coefficients |ε_r| of ε_1D(k) = √(m² + g(k)) at m = 0.3, with **nothing subtracted**.

## 2. Prior art (each counted once)

- **R14-3** (`vR14-3`, CONFIRMED WITH CORRECTIONS, REFUTED).
  - Theorem B: Ξ < 0 for every nonnegative nonzero vertex on 𝒰₀ (`vR14-3:14`). W08/W14 have positive E_g shifts at light mass. "All tested T₂g shifts remain negative; this is search evidence, not a theorem" (`vR14-3:16`).
  - R14-3's search parametrization blended ±1 node values with sstep over the full node spacing (`C5_R14-3_report.md:198`), so |σ′| = 1 was reached only at isolated points. Its "no Ξ ≥ 0 with face-gapped valleys" (`:222`) was suggested only.
- **R9-9 Theorem T and Lemma N** (`C5_R9-9_report.md:122-152`). The literal edge L (superluminal) has Ξ_T2g > 0 (+2.409e-3 M at m = 1). Lemma N needs vertex richness (`vR9-9` item 3). Lemma V below is the per-band version of that richness remark.
- **R13-5** (`vR13-5:9-11`). Light-L doublers destroy the G floor. Birefringence is removable by one edge-weight tuning (L-U uses the T₂g weight, c = 4.160499).
- **R11-1(b)** (`vR11-1:17-23`). The dD-M split and its prescription scope; Ξ_T2g ≠ Ξ_Eg ⇒ at most one cone matches (for M/U).
- **R14-1** (`vR14-1:13`). A ≤ 0 holds only for S/G, not for all subluminal bands.
- **S17** (`C5_S17_synthesis.md:95,179,217,263,288`). "T₂g never zeroed", "no edge choice has reached T₂g", P62, P63.
- **Repo grep.** I searched the packet and agents for "zigzag", "T2g ≥ 0" and "5v_z² − 1". No prior Ξ_T2g ≥ 0 subluminal witness or v_z form was found.

---

## 3. Results

### 3.1 Calibration (checked; `calib.out`, `verify_w.out`, `mucal.out`)

- The Laplace evaluator gives Ξ_v = [32Γ(5/2)]⁻¹∫dt t^{3/2}e^{−tm²} W_v(t) J(t), with J = 2tF₂ − E₀.
- **NN scalar, m = 1:** M,T2g −1.903007e-3, M,Eg −8.301857e-4, U,T2g −2.289166e-4, U,Eg −6.883237e-5. This equals R9-9's table (`C5_R9-9_report.md:136`) to all printed digits.
- **NN μ_E(m = 1):** +1.97038864e-3, equal to V3's comparator. **G(1.4):** +3.52543170e-3, equal to R14-3.
- **W08/W14** (re-implemented): every R14-3 value is reproduced (`C5_R14-3_report.md:204-212`). Examples:
  - W08 at m = 0.3: M,Eg +2.3927e-5, M,T2g −9.9125e-4, v_max 0.98739;
  - W08 I(B): +17.98 at B = 1e-4, +0.1358 at B = 1.

### 3.2 The witness Z1: Ξ_T2g > 0 for M and U (checked; `verify_z1.out`, `verify_z1b.out`)

**Law Z1.**
- σ′ = 1 on [0, 1.0].
- Then −1, +1, −1, +1, −1 on [1.0, 1.4], [1.4, 1.8], [1.8, 2.2], [2.2, 2.6], [2.6, 3.0].
- Then 0 on [3.0, π].
- C^∞ steps of width wt = 0.06, centred at the breakpoints.

So σ rises to 1.0, oscillates between 0.6 and 1.0, and ends flat at σ(π) = 0.6.
- max|σ′| = 1.000000000; σ′(π) = 0; A ∈ [−67.1, +39.6].
- Gapped valleys at g = 0.37 (k = 1.4, 2.2) and 0.36 (π), below the box-face value b² = 1. No zero of g off k = 0.

| m | v_max (d = 3) | Ξ M,T2g | Ξ U,T2g | Ξ M,Eg | Ξ U,Eg | μ_E |
|---|---|---|---|---|---|---|
| 1.0 | 0.860479 | −7.03229e-4 | −5.96460e-4 | −8.17230e-5 | −9.49474e-5 | +6.848e-3 |
| 0.3 | 0.984560 | **+3.904715e-4** | **+2.810149e-4** | +4.117765e-4 | +4.053591e-4 | +1.227e-2 |
| 0.1 | 0.998246 | **+8.054649e-4** | **+6.152180e-4** | +6.001817e-4 | +5.938985e-4 | +1.309e-2 |
| 0.01 | 0.999982 | **+8.663681e-4** | **+6.642496e-4** | +6.284241e-4 | +6.220447e-4 | +1.320e-2 |

- **Resolution.** Laplace values at (n, ν) = (2^14, 1500) and (2^16, 4000) agree to 6–7 digits.
- **Independent 3D zone grid, m = 0.3** (A-form ⟨|V|²A_zz/ε⁵⟩/32 and IBP form):

  | N | M,T2g A-form | M,T2g IBP | U,T2g A-form | U,T2g IBP |
  |---|---|---|---|---|
  | 240 | +5.064e-4 | +3.867e-4 | +3.772e-4 | +2.767e-4 |
  | 480 | +3.37e-5 | +3.902e-4 | −1.6e-5 | +2.813e-4 |
  | 720 | **+3.90833e-4** | **+3.90500e-4** | **+2.81321e-4** | **+2.81043e-4** |

  - At N = 720, A-form and IBP agree with the Laplace value to 1e-3 relative. At lower N the A-form is unresolved, because A has spikes of width 0.06.
  - At m = 0.1, N = 240 IBP: M,T2g +8.008e-4, U,T2g +6.097e-4.
- **Smoother turns, same skeleton (wt = 0.15).** m = 0.3 gives M,T2g −1.78128e-4 in all three methods (N = 720 A-form −1.78129e-4). This is a sign control: the evaluators do not produce positive values by themselves.
- **I(B) for Z1 (n = 2^16).** +54.6 (B = 1e-4), +27.2 (0.1), +0.406 (1), −0.125 (2), −0.0136 (10).

**Mechanism (proved identity; reading).**
- By R14-3's (R2) (`C5_R14-3_report.md:97-99`; IBP confirmed `vR14-3:14`):

  Ξ = (1/32)⟨|V|²(5f_z² − ε²)/ε⁷⟩ = (1/32)⟨|V|² (5v_z² − 1)/ε⁵⟩, with v_z = ∂ε/∂k_z = f_z/ε.

  So Ξ_v ≥ 0 ⟺ the (|V|²ε⁻⁵)-weighted mean of v_z² is ≥ 1/5, the Lorentz value.
- On a slope-1 stretch, f_z² = g_z, so v_z² = g_z/(m² + g_⊥ + g_z). For low edge levels and small m and g_⊥, this is close to 1.
- Gentle or flat edges give v_z ≈ 0 at the same energies. That is Theorem B's (and B″'s) negative side.
- T₂g was harder because its weight 4g_xg_y vanishes when either transverse momentum is small. That keeps ε ≥ √(g_x + g_y) away from the light, heavily weighted region. It needs the low, fast edge states to be numerous enough to dominate. Sharp turns make |σ′| = 1 almost everywhere (reading).

### 3.3 Where positivity lives (checked; `zzscan.out`, `floor_scan.out`, `verify_z1b.out`, `relax*.out`)

- **Valley floor (best Ξ_T2g over the uniform zigzag family Zz(b, V, P, wt): box b, down to V, zigzag V↔P, flat end).** "≥ 0 found" means some member has Ξ_T2g ≥ 0.

  | lowest edge σ (V_floor) | wt = 0.06, m = 0.1 (M / U) | wt = 0.06, m = 0.3 (M / U) | wt = 0.12 |
  |---|---|---|---|
  | 0.30 | +2.39e-3 / +2.21e-3 | +5.26e-4 / +5.20e-4 | ≥ 0 found |
  | 0.45 | +1.44e-3 / +1.21e-3 | +4.04e-4 / +3.80e-4 | ≥ 0 found |
  | 0.60 | +1.03e-3 / +7.66e-4 | +4.11e-4 / +3.04e-4 | ≥ 0 found (m = 0.1; m = 0.3 +1.2e-5 M) |
  | 0.75 | +3.9e-5 / +1.22e-4 | −1.34e-4 / −2.16e-5 | none |
  | 0.90 | +1.34e-4 / +1.96e-4 | −1.3e-5 / +6.9e-5 | none |
  | 1.05 | −2.78e-4 / −2.12e-4 | −3.48e-4 / −2.67e-4 | none |
  | 1.20 | −4.02e-4 / −2.54e-4 | −4.43e-4 / −2.93e-4 | none |

- **Transition width** (Z1 skeleton, M,T2g at m = 0.3 / 0.1). Positivity needs sharp turns.

  | wt | m = 0.3 | m = 0.1 |
  |---|---|---|
  | 0.03 | +5.79e-4 | +1.03e-3 |
  | 0.06 | +3.90e-4 | +8.05e-4 |
  | 0.10 | +1.39e-4 | +5.10e-4 |
  | 0.15 | −1.78e-4 | +1.40e-4 |
  | 0.20 | −4.97e-4 | −2.33e-4 |
  | 0.30 | −1.14e-3 | −9.87e-4 |

- **The relaxed (Young-measure) problem.**
  - Statement (proved): F₂ = ⟨h²s²e^{−tg}⟩ ≤ G₁ = ⟨h²e^{−tg}⟩ because s = |σ′| ≤ 1. Ξ_M is increasing in F₂ (its weight G₁² ≥ 0 does not depend on s). So for fixed level distribution, sup Ξ_{M,T2g} is approached by |σ′| = 1 a.e., i.e. fast zigzags, where f² = g and M = U.
  - Numerics (checked, `relax.out`): with a box/first rise to H and edge mass π − H at one level x₀, the maximum is +2.90e-3 at m = 0.3 (H = 0.6, x₀ = 0.5) and +1.27e-2 at m = 0.1.
  - At m = 1 every relaxed configuration on the grids is negative. The supremum approaches 0⁻ only in the degenerate limit H → 0 (−1.6e-9 at H = 0.05; two-atom best −1.0e-6; `relax_m1.out`).
  - **Suggested:** Ξ_T2g < 0 for every law in 𝒮 at m = 1. Not proved.
- **R14-3's face-gapped remark (reading).** "Valleys above the face" depends on where σ′ first leaves exactly 1. Relabelling a box b = 1.0 as b′ = 0.5 with σ′ = 0.999 on [0.5, 1.0] makes Z1's valleys "face-gapped" and moves Ξ continuously by O(1e-3) relative. The meaningful variable is the valley level, as in the table above.

### 3.4 Lemma V: the every-vertex T₂g sign fails on W08/W14 themselves (proved; checked, `verify_w.out`, `soft_m1.out`)

**Statement.** Fix a law in 𝒮 and m > 0. Let I(B) = ∫A(k)(B + g(k))^{−5/2}dk. Then the following are equivalent:
- (i) Ξ < 0 for every nonzero nonnegative vertex that is k_z-independent and T₂g(B₂g)-symmetric;
- (ii) I ≤ 0 on [m², m² + 2 max g] and I is not identically zero there.

**Proof.**
1. Ξ = (1/32)(2π)⁻³∫d²k_⊥|V|² I(m² + g_x + g_y), since |V|² does not depend on k_z.
2. (ii) ⇒ (i) is immediate.
3. (i) ⇒ (ii): if I(B₀) > 0 at an interior B₀, then I > 0 on an open interval J around it. The set {(k_x, k_y): m² + g_x + g_y ∈ J} is open and nonempty, contains off-axis points, and is invariant under k_x → −k_x, k_y → −k_y and k_x ↔ k_y (g is even).
4. Take V = sgn(k_xk_y)·φ with φ ≥ 0, smooth, supported there, and symmetric. This V is B₂g and nonnegative in |V|², and Ξ > 0. ∎

**Applied (checked).** The vertex 4g_xg_y e^{−(g_x+g_y)/η} is nonnegative, B₂g and k_z-independent.

| law | m = 0.3 | m = 0.1 | m = 1 |
|---|---|---|---|
| W08 | +8.65e-6 (η = 0.3), +1.34e-6 (0.1) | +1.51e-5 (0.3) | +6.7e-10 (0.03) |
| W14 | +4.69e-6 (0.3) | +5.9e-6 (0.3) | +4.1e-8 (0.1), +1.9e-9 (0.03) |

- At m = 1 the sign follows from I(1) = +0.136 (W08) and +0.222 (W14).
- With η = 10, the same vertex gives Ξ < 0.

So the item's (a), in its every-vertex form, cannot include W08/W14 at any of the three masses. The physically meaningful question is the law's own vertices (§3.2).

### 3.5 Theorem B″: a sign theorem on a class strictly larger than 𝒰₀ with gapped valleys (proved; checked)

**Statement.** Let σ ∈ 𝒮 with h = |σ| having finitely many monotone stretches (between consecutive local extrema, plateaus allowed). Suppose every monotone stretch that has a gapped valley (a local minimum with h > 0, including at k = π) as an endpoint satisfies |σ′| ≤ 1/√5 on that stretch. Then I(B) < 0 for every B > 0. Hence Ξ_v < 0 for every nonnegative nonzero k_z-independent vertex, in both polarizations, at every m > 0.

**Proof.**
1. By (R2), I(B) = 2∫₀^π [5h²h′² − (B + h²)](B + h²)^{−7/2}dk.
2. Monotone stretches alternate minimum ↔ maximum. Each minimum is either a zero of g or a gapped valley.
3. A stretch between a zero and a peak P contributes ≤ F(P) − F(0) = F(P) < 0, with F(x) = −x(B + x²)^{−5/2}. This is R14-3's steps 2–3, confirmed at `vR14-3:14`, and it uses only |h′| ≤ 1.
4. A stretch with |h′| ≤ 1/√5 has 5h²h′² ≤ h². Its integrand is therefore ≤ −B(B + h²)^{−7/2} < 0.
5. The stretch from k = 0 to the first peak P₁ ≥ b > 0 starts at a zero, so it contributes F(P₁) < 0 strictly.
6. Every term is ≤ 0 and one is < 0. ∎

- **It contains 𝒰₀** (no gapped valley, so the hypothesis is vacuous).
- **It is strictly larger.** Checked (`final_checks2.out`) on the "gentle" law: σ′ = 1 on [0, 1], −0.44 on [1.0, 1.8], +0.44 on [1.8, 2.4], −0.44 on [2.4, 2.8], 0 after.
  - Gapped valleys at g = 0.425 and 0.542, below the face value 1.
  - I(B) < 0 on [1e-3, 1e2] (I(1e-3) = −6.16).
  - All four Ξ < 0 at m = 1, 0.3, 0.1, 0.01 (e.g. m = 0.1: M,T2g −5.33e-3, M,Eg −9.34e-4).
  - v_max = 0.98456 at m = 0.3.
- **Numerical note.** An earlier run (`final_checks.out`, last line) printed max I > 0 for this law. That came from B ≤ 1e-5 at n = 2^15, where the box integrand (4k² − B)/(B + k²)^{3.5} cancels at the 1e15 level and the midpoint rule fails. At n = 2^18 and B ≥ 1e-3 it is negative, as the theorem requires.
- **The threshold.** As B → 0 the edge integrand per unit length becomes (5s² − 1)h^{−5}. So 1/√5 is where steep valley flanks start to contribute positively. W08/W14/Z1 (slope ±1 flanks) are outside the class, and §3.2–3.4 show they must be.

### 3.6 (b) Simultaneous E_g/T₂g zeros, and P62 (checked; `simul2.out`, `final_checks.out`, `final_checks2.out`, `cross.out`, `hybrid.out`, `terr.out`)

**Corners** (all in 𝒮, box exact on [0, 0.97]; values at m = 0.1, M vertex; `vmax_all.out`):
- A = G(1.0) ∈ 𝒰₀: Eg −9.63e-4, T2g −2.07e-3.
- C = Zz(1.0, 0.35, 0.43, wt 0.03): σ goes from 1.0 down to 0.35, then zigzags 0.35↔0.43 with slope ±1. Eg −1.44e-4, T2g +3.77e-4 — a T₂g-positive, E_g-negative law. Valleys at g = 0.125.
- C2 = Zz(1.0, 0.35, 0.47, 0.03): Eg +5.7e-5, T2g +6.37e-4.
- v_max of every corner at m = 0.3 / 0.1 / 0.01: 0.98495–0.98998 / 0.99829–0.99879 / 0.99998–0.99999.

**Family.** σ′ = (1 − u − v)σ′_A + uσ′_{C2} + vσ′_C. This is a convex mix, so |σ′| ≤ 1. Solved by a coarse grid plus Newton; residuals are refined at (n, ν) = (2^16, 4000).

| vertex | m | (u, v) | Ξ_Eg, Ξ_T2g (this vertex) | other vertex (Eg, T2g) | μ_E | v_max | max\|σ′\| | min edge g |
|---|---|---|---|---|---|---|---|---|
| M | 0.10 | (0.955978, 0.024523) | ≤ 4e-15 | U: −9.25e-5, −1.17e-4 | +6.19e-3 | 0.998292 | 1.000000000 | 0.1437 |
| M | 0.03 | (0.944726, 0.037332) | ≤ 4e-15 | U: −1.15e-4, −1.42e-4 | +6.05e-3 | 0.999846 | 1.000000000 | 0.1422 |
| M | 0.01 | (0.943709, 0.038492) | ≤ 4e-15 | U: −1.17e-4, −1.45e-4 | +6.04e-3 | 0.999983 | 1.000000000 | 0.1420 |
| U | 0.10 | (0.964879, 0.007410) | ≤ 9e-15 | M: +7.58e-5, +1.01e-4 | +6.58e-3 | 0.998293 | 1.000000000 | 0.1518 |
| U | 0.03 | (0.955996, 0.015995) | ≤ 9e-15 | M: +9.41e-5, +1.21e-4 | +6.53e-3 | 0.999846 | 1.000000000 | 0.1521 |
| U | 0.01 | (0.955208, 0.016763) | ≤ 9e-15 | M: +9.58e-5, +1.22e-4 | +6.52e-3 | 0.999983 | 1.000000000 | 0.1521 |

- **Second corner set.** A, B = Z1, C gives M zeros at m = 0.03 (u, v) = (0.002913, 0.965162) and m = 0.01 (0.004027, 0.964496), inside the simplex.
- **Outside 𝒮 — these do not count.** With A, Z1, C, the m = 0.1 M zero and all U zeros fall just outside the simplex (u ≈ −0.01, max|σ′| up to 1.025, v_max up to 1.017). The same happens with A, Z1(0.25), C. The A, C2, C table above replaces them.
- **Independent 3D grid** (IBP form, m = 0.03, the A, Z1, C M-zero; `final_checks.out`):
  - M,T2g: −9.3e-6 (N = 480), +3.2e-6 (720), −1.6e-7 (960).
  - M,Eg: −2.5e-6, +8.6e-7, −4.1e-8.
  - Corner magnitudes are 6e-4 to 2e-3.
  - U at N = 960: −1.243e-4 / −6.995e-5, against Laplace −1.241e-4 / −6.960e-5.
  - The A-form converges more slowly (wt = 0.03 spikes): +5.2e-4, +7.9e-5, −2.7e-5.
- **Mass dependence (proved; checked).**
  - A_zz = 0 wherever σ′ ≡ 1 (the exact box), and g ≥ g_* > 0 on the rest of the k_z circle. So Ξ(m) is real-analytic in m² for m² > −g_* (same argument as R14-3's μ_E analyticity, `C5_R14-3_report.md:156-157`).
  - Checked, for the M zero tuned at m = 0.01: residuals (Eg, T2g) are (+5.7e-7, +1.6e-6) at m = 0.001, (−4.6e-6, −1.3e-5) at 0.03, and (−3.1e-4, −9.6e-4) at 0.3. This gives dΞ/dm² ≈ −5.8e-3 (Eg) and −1.65e-2 (T2g).
  - So one setting at ma → 0 serves every light species that shares the edge and the vertex, to residual ~1e-2·(ma)² ≲ 2e-36 at ma ≤ 1.4e-17 (reading, a = ℓ_P).
- **Count (without P62).**
  - **Two edge-shape tunings per edge, per TT vertex prescription.** Here they are (u, v); one condition per polarization.
  - **Two are needed in this family (checked):** along any one-parameter path from G(b) to a zigzag corner (`cross.out`), the E_g zero comes first. t_T − t_E = +0.058 to +0.109 over 36 such paths, both vertices, m = 0.3 and 0.1. So one knob never zeroes both. This is not a theorem that every one-parameter family fails.
  - The M zero is not a U zero (§3.6 table). Which vertex is physical is a law datum (P63(iii)).
- **With P62 (μ_E = 0 as well): no common zero found (suggested).**
  - At every graviton-cone zero, μ_E = +6.0e-3 to +6.6e-3.
  - 39 hybrid laws (zigzag plus a high terrace, `hybrid.out`) all have μ_E > 0. The 9 with both M Ξ > 0 have μ_E ≥ +6.2e-3.
  - The most negative μ_E found, −4.65e-3 (terraces, `terr.out`), comes with Ξ_M,T2g = −9.7e-3.
  - Mixing the M zero toward Gw(1.0, 0.05) (μ_E = −5.8e-4) gives, at weight 0.5, μ_E still +1.1e-3 with Ξ_M,T2g = −5.1e-3.
  - A linear estimate needs ~2.8 units of Z1-type edge to undo each unit of terrace in Ξ_Eg, which costs ~3.6e-2 in μ_E against the 3.1e-3 gained.
  - **Reading.** Ξ ≥ 0 needs a narrow, fast |f| distribution (low kurtosis), which is exactly what makes μ_E > 0 (R14-3's R1: μ_E = −(5/72)⟨K₄(f)/ε³⟩). Not proved; the searched families are only those listed.

### 3.7 Locality price (checked; `final_checks2.out`, `final_checks.out`)

Raw Fourier coefficients |ε_r| of ε_1D = √(0.09 + g(k)), **nothing subtracted**. The law is built on 2^20 points with exact-grid sampling.

| law | r = 128 | r = 256 | r = 512 | r = 1024 |
|---|---|---|---|---|
| Z1 (wt 0.06) | 2.0e-7 | 3.1e-9 | 5.9e-9 | 4.1e-11 |
| C (wt 0.03) | 5.0e-6 | 8.3e-7 | 1.8e-6 | 1.1e-9 |
| M-zero law (A, Z1, C mix; interpolated sampling, same as clean for C) | 4.0e-6 | 7.9e-7 | 1.8e-6 | — |
| G(1.0) | 1.4e-14 | — | — | — |
| comparator: R14-3's G_w* | 4.5e-8 | — | 2.0e-13 | — (`C5_R14-3_report.md:141`) |

- The non-monotone values come from the zigzag's k-periodicity, which puts hopping resonances near r ≈ 2π/(2·amplitude).
- All laws are C^∞ (Gevrey-type), so tails fall faster than any power. But the zero laws carry hopping of order 1e-6 at a few hundred sites.

---

## 4. Against the FIXED readings (`TESTS:5101-5103`)

**REFUTED (worker reading; referee required).**
- **The witnesses.** Z1 (§3.2) is explicit, subluminal (|σ′| ≤ 1 exactly; v_max < 1 at every listed m), smooth, and has gapped valleys at 0.6/a. Its own R9-9 vertices give Ξ_T2g > 0:
  - M: +3.90e-4 (m = 0.3), +8.05e-4 (m = 0.1);
  - U: +2.81e-4, +6.15e-4.
  - Checked by Laplace at two resolutions and by the 3D grid in both forms.
  - Further witnesses: §3.3 (M and U, valleys down to 0.3/a and up to 0.9/a).
- **Prescription scope.** R9-9's vertex, the assumed standard-W1 completion of the pair stress, and the supplied zero-point vacuum.
- **Mass scope.** Refuted at m = 0.3 and 0.1 (and 0.01). At m = 1 no witness was found, and Ξ_T2g < 0 there is suggested only.
- **Simultaneous E_g/T₂g zero: FOUND** (§3.6), separately for M and for U, at m = 0.1, 0.03 and 0.01, inside 𝒮. With P62's shear condition as well: **not found** (suggested obstruction).

**On DERIVED.** Theorem B″ (§3.5, proved, unrefereed) does prove Ξ_T2g < 0 (indeed Ξ < 0 for every vertex) "in a stated class containing 𝒰₀ and gapped-valley laws". On its letter, that is the DERIVED clause. But the item's question and its probe (a) ask about the whole stated setting, including W08/W14-type valleys. Lemma V and Z1 show that the setting contains counterexamples, so DERIVED cannot be the item's answer. I report **REFUTED**, with Theorem B″ as an additional sub-class result. If the referee reads the clauses as non-exclusive, the record would be "REFUTED in 𝒮; DERIVED on 𝒰₀ ∪ (gentle-flank valleys)".

**Expectation check.** The expectation was "SUGGESTED leaning DERIVED; a simultaneous zero is not expected" (`TESTS:5104`). Both parts failed. The S17 premise behind it, that T₂g "weights mixed derivatives that the valley trick does not reach", holds only for R14-3's slope-limited valleys. Full-slope valleys reach it.

## 5. What it means (reading)

- **For the item's dilemma (`TESTS:5088`).** Edge shaping can put T₂g on the cone. The box route's graviton cone does not need pairing or a per-polarization counterterm, if one accepts two edge-shape tunings per edge (and per vertex prescription), plus zigzag valleys at about 0.35–0.9/a.
- **What is still not shown.** That such an edge also cancels the conditional shear; no tested law does both. Pairing (P46), or the empty Fock vacuum where Ξ ≡ μ_E ≡ 0, remain the routes that need neither.
- **Dated corrections to recommend (if refereed).**
  - S17's "T₂g never zeroed" / "no edge choice has reached T₂g" (`C5_S17_synthesis.md:95,179,263,288`) and P63(i)'s "T₂g not reached" (`:217`) should read: "T₂g reached by full-slope zigzag edges (valleys ≲ 0.9/a, sharp turns); E_g and T₂g zeroed together by two edge-shape tunings per vertex prescription; no common zero with P62 found."
  - R14-3's remark that positivity was not found with face-gapped valleys (`C5_R14-3_report.md:222`) depends on where the box is labelled, not on the valley level (§3.3).
- **Order of magnitude (reading; comparator only).** In R9-9's normalization, c_T² − 1 = (2/M²)Ξ = 2κ_lat Ξ = 16πΞ at a = ℓ_P (`C5_R9-9_report.md:120,186`; its NN control 16π|Ξ| ≈ 0.096). Untuned edge values |Ξ| ~ 1e-3 therefore give ~5e-2 in speed². GW170817's band, −3e-15 ≤ Δc/c ≤ 7e-16 (`C5_R7-4_report.md:46`, comparator), needs |Ξ| ≲ 1e-16. So each of the two tunings must hold to ~1e-13 relative. This is the same type of price as P62's tuning; the O((ma)²) drift (~2e-36) is far below it.

## 6. Prices (named, not adopted)

- **P-Z (new): zigzag edge for the graviton cone.**
  - The band beyond the box oscillates at full slope |σ′| = 1 with sharp turns (transition width ≲ 0.1–0.15 in k).
  - This gives several heavy edge valleys at 0.35–0.9/a below the box-face energy, and hopping tails of ~1e-7 to 1e-6 at r ~ 128–512 (raw |ε_r|).
  - **Plus two edge-shape tunings per edge per TT-vertex prescription** (Ξ_Eg = Ξ_T2g = 0), mass-dependent only at O((ma)²).
  - Axiom cost: none. The edge dispersion is downstream dynamics (`AX:116-123`).
  - It replaces P63(i)'s "E_g only" and P63(iv)'s per-polarization seagull as the cheapest unpaired option, within the prescription.
- **P-TTV (inherited, P63(iii)).** The TT vertex is a law datum. M zeros are not U zeros (§3.6). Source/action gate `AX:187`.
- **Inherited.**
  - R9-9's assumed standard-W1 completion of the pair stress, not built (`vR9-9` item 1).
  - The supplied zero-point vacuum (`AX:184-187`).
  - Ξ is the bare-cone shift, not the dressed split (`vR9-9` item 5; R11-1(b) excluded).
  - R14-1's box-route prices.
- **P62 + P-Z together:** no law found. If both are required, a third mechanism is needed (pairing, or an empty-vacuum class).
- **No axiom text changes.**

## 7. Strong-word check

- **"Proved"** is used only for:
  - the v_z form of Theorem T;
  - the relaxed-problem monotonicity (F₂ ≤ G₁);
  - Lemma V;
  - Theorem B″;
  - analyticity of Ξ(m) in m²;
  - |σ′| ≤ 1 for the constructions (non-overlapping convex blends) and for convex mixtures.
- **"Checked"** is used for every number. Methods: Laplace-separable evaluation at 1D n = 2^12–2^16 and ν = 500–4000, cross-checked by the 3D zone grid in both forms (N up to 960). v_max by exact separable bisection on 2·10⁵ points.
- **"Every"** appears only inside Lemma V's and Theorem B″'s hypotheses.
- **"Exactly zero"** is never claimed. The simultaneous zeros are |Ξ| ≤ 1e-14 (Laplace, at a Newton root) and ≤ 2e-7 (3D grid, N = 960).
- **"Not found"** (triple zero with P62; T₂g ≥ 0 at m = 1; positivity with every valley ≥ 1.05/a) covers the listed families only.
- **Not claimed:**
  - anything gauge-invariant (W2 standard or deformed);
  - the dressed graviton–matter split;
  - Wilson or Dirac edges;
  - q off-axis;
  - two loops;
  - certified interval bounds.

## 8. For the referee

1. Z1's definition and |σ′| ≤ 1. Ξ_T2g > 0 for M and U at m = 0.3 by an independent 3D grid (needs N ≳ 700 for the A-form). The wt = 0.15 sign control.
2. The v_z form Ξ = (1/32)⟨|V|²(5v_z² − 1)/ε⁵⟩ (a rewriting of R14-3's confirmed (R2)).
3. Lemma V: the B₂g symmetrization of a vertex supported where I > 0. Whether such abstract vertices belong in "nonnegative nonzero transverse vertices" (`TESTS:5093`).
4. Theorem B″: the stretch decomposition, the gentle-stretch pointwise bound, and strictness from the first rise.
5. The simultaneous zeros (A, C2, C table): in-simplex coordinates, max|σ′| = 1, and residuals. Optionally the N = 960 IBP grid on the A, Z1, C zero.
6. Analyticity of Ξ in m² (A_zz vanishes on the exact box; g bounded below elsewhere).
7. Whether §4's REFUTED plus Theorem B″ as a sub-class result is the right recording against the non-exclusive FIXED clauses.

## 9. Files (all in `S/scripts/`)

- `zz.py`: law class (piecewise ±1/0 σ′ with C^∞ steps), Laplace evaluators for Ξ (four vertices) and μ_E, I(B), convex `Mix`, v_max.
- `laws.py`: G(b), Z1, W08/W14 re-implementation.
- `grid3d.py`: direct 3D zone grid, both forms.
- `calib.{py,out}`, `mucal.{py,out}`, `verify_w.{py,out}`: calibration (NN, G(1.4), W08/W14) and the Lemma V vertex.
- `zzscan.{py,out}`: first zigzag scan. `verify_z1.{py,out}`, `verify_z1b.{py,out}`: the Z1 witness, width dependence, 3D grids.
- `floor_scan.{py,out}`: valley-floor map. `relax.{py,out}`, `relax2.{py,out}`, `relax_m1.{py,out}`: relaxed problem.
- `cross.{py,out}`: one-knob crossing map. `findC.{py,out}`: E_g < 0 < T₂g corners.
- `simul.{py,out}`: first fsolve attempt. Superseded: it left the simplex, and its "zeros" are superluminal and invalid.
- `simul2.{py,out}`, `final_checks.{py,out}`, `final_checks2.{py,out}`: simultaneous zeros, 3D grid on a zero, tails, Theorem B″ check.
- `terr.{py,out}`, `hybrid.{py,out}`: the P62 searches. `soft_m1.{py,out}`: Lemma V at m = 1. `vmax_all.{py,out}`: v_max and corner values.
- `floor_scan.py`, `verify_w.py` and `simul2.py` had their main blocks wrapped in `if __name__ == '__main__'` after their runs, for import. Their logic is unchanged.

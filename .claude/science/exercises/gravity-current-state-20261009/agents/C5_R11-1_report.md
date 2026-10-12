# C5 R11-1 report: is an edge supertrace necessary? And the dressed matter speed under graviton loops

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 18:44Z to about 19:25Z. No repository file edited (`git status` clean).

**Scratch.** `S/` = `.../scratchpad/C5/R11-1/`. Scripts and outputs are in `S/scripts/`. Each runs in under 40 s with `OMP_NUM_THREADS=2`.
- `r111_necessity.{py,out}`: part (a) checks. Total masses, the Laplace form, paired versus unpaired content, and the edge onset.
- `r111_obs_by_obs.{py,out}`: part (a). Pairing the photon does not pair the graviton.
- `r111_check_PT_weight.{py,out}`: an independent 8×8 check of R10-5's fermion TT pair weight, the fermion input to (a).
- `r111_q0int.{py,out}`: sympy closed forms of the frequency integrals, with quadrature and old-fashioned-perturbation-theory checks.
- `r111_matter_speed.{py,out}`, `r111_matter_speed_light.out`: part (b), the matter self-energy from box-graviton loops.
- `r111_vpv_identity.{py,out}`: Lemma M.
- `r111_split_numbers.{py,out}`: the c_m − c_T table and its physical sizes.
- Unmodified copies: `r99_profiles_copy.py` (R9-9), `r101_pairing_copy.py` and `r85_box_qed_copy.py` (via R10-5's scratch).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`:
  - the C5 method and round 1 (`:2302-2420`);
  - R11-1 (`:4086-4120`) and all of round 11 (`:4062-4267`);
  - the round-10 referee results (`:4268-4309`).
- `agents/C5_S11_synthesis.md`: `:1-115` and `:265-312`, plus grep hits.
- `SUMMARY.md` §§21–24 (`:534-636`).
- Agents:
  - `C5_R10-1_report.md` and `C5_R10-1_referee_verdict.md`;
  - `C5_R9-9_report.md` and verdict;
  - `C5_R10-5_report.md` (worker; unrefereed);
  - `C5_O3_report.md:14,50-64` and `C5_O3_referee.md:5,17`;
  - `scripts/C5/R8-5/r85_box_qed.py`, `scripts/C5/R9-9/*`, R10-5's `r105_tt_paired.{py,out}`.

**Labels.**
- **proved**: complete under the stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature, RECALLED unless verified.
- **[worker R10-5]**: an unrefereed claim used as input.

---

## 0. In plain words

1. **(a) Pairing is necessary in the registered sense, and here is why.**
   - Every species' one-loop light-speed coefficient in 𝒞_A is an average of the grid's leftover "boost anomaly" A, weighted by a positive vertex factor.
   - On every periodic band, A averages to exactly −1 along each line. So each scalar contributes a weight of definite **negative** total, and each Clifford-flat fermion one of definite **positive** total.
   - Asking a coefficient to vanish for a whole interval of masses forces, by Laplace-transform uniqueness, the boson and fermion weighted spectral measures to cancel. This is the same mechanism as O3's vacuum-energy theorem.
   - So neither statistics alone can do it, and the cancellation must hold separately for the photon and for the graviton (proved).
   - In a natural subclass the measure condition forces exactly R10-1's and R10-5's minimal pairing: one boson curve and one fermion curve, the same masses, no doublers. There it requires the same curve, the same box and the pairing TT vertex (proved).
   - **What this does not say.** All physical masses are about 1e-19 in Planck-lattice units. A single tuned edge shape can null one coefficient at m → 0 for every light species of one statistics. Necessity holds for "zero on a mass interval", which is the registered criterion, not for "small at physical masses".
2. **(b) The matter's own speed shift from graviton loops is computed for both edges, and it is not what sets the split.**
   - **The prescription.** Box graviton, de Donder-type propagator, minimal metric coupling. In it, the one-loop on-shell exchange is exactly proportional to m² (an algebraic identity), and the seagull tadpole carries no Lorentz violation.
   - **The consequence.** The matter speed shift is 4κ_lat·m²·J₂, with J₂ ≈ −5.7e-3 (G edge) and −7.3e-3 (L edge). For a proton at Planck spacing that is about 2e-39: negligible.
   - **So the graviton side sets the split:** c_m − c_T → −κ_lat·Ξ. That is R9-9's anomaly moment, about +2.8e-2 (G, T_2g) and −0.13 (L) at a = ℓ_P, some 1e13 times the GW170817 band.
   - **At lattice-scale masses** (m = 1, 0.3) both sides matter. The split is nonzero on both edges and for both polarizations (table in §4). Its sign is **not** fixed on the gapped edge: on G, T_2g is +0.014 at m = 0.3 and −1.59 at m = 1, in κ_lat/16π² units.
   - **Birefringence.** The graviton's two polarizations already travel at different speeds (R9-9). So matter can sit on at most one of the two TT cones whatever its own shift.
   - **Scope.** This is one stated prescription. The lattice Ward identity is not exact off the box, so the gauge independence of the number is not established.
3. **(c) The count.** Without pairing, each coefficient needs its own condition. With minimal pairing, the photon (R10-1) and the graviton TT (R10-5) coefficients go away at one loop with matched masses. Two follow-on points:
   - The graviton–matter split then drops to O(κ_lat m²), negligible, in this prescription (new).
   - The electron–photon split stays (R10-1/R10-5).

**Against the FIXED readings (worker; referee required).**
- **(a) DERIVED** in 𝒞_A at the measure level (Theorem N\*), with the species-level form proved in subclass 𝒞_A^S (Theorem S).
- **(b) SPLIT-PRESENT, in the stated prescription only** (not class-wide).

---

## 1. Hypotheses and classes (stated before any title)

- **𝒞_A (as registered).**
  - **Lattice and matter.** Z³ × ℝ, continuous time, free Gaussian matter. Bands are separable, C² and periodic, ε_s² = m_s² + Σ_j u_s(k_j), and box-exact on an open box (H-box, `C5_R10-1_report.md:67-96`).
  - **Gauge vertices.** Peierls, Ward-forced onto the zone (Lemma C `TESTS:3808`; Lemma Q `TESTS:3841`).
  - **Species:**
    - complex scalars (photon coefficient: Theorem T′; TT: Theorem T with a vertex |V_b|²(k_x, k_y) ≥ 0 in R9-9's class 𝒱);
    - Clifford-flat 8-component fermions (photon: Theorem P; TT: R10-5's vielbein vertex Γ = ½(S_xA_y + S_yA_x) [worker R10-5]).
  - **Untuned.** Band shapes and vertices are fixed per statistics and do not depend on the observable or the mass.
- **Mass family.** M is the varied parameter. Species masses are m_s² = a_s M + c_s with a_s > 0; §3.1 Remark (iii) relaxes this.
- **The coefficients (normalizations as in the sources; checked in §3.4):**
  - photon: C_γ = Σ_b q_b²(1/32)⟨u_b′(k_y)²A_b(k_x)/ε_b⁵⟩ − Σ_f q_f²(1/8)⟨v_f′(k_y)²A_f(k_x)/E_f⁵⟩. Here v = S² + W², A = u″(k_∥)/2 − 1, and 1/8 is per 8 components (Theorem P: −2× the scalar per 4 components; `vR10-1:7`).
  - graviton T_2g, q ∥ z: C_T = Σ_b (2/32)⟨|V_b|²A_b(k_z)/ε_b⁵⟩ − Σ_f ⟨S_x²S_y²A_f(k_z)/E_f⁵⟩.
    - The fermion term is R10-5 Theorem PT for Clifford-flat curves (`C5_R10-5_report.md:191-235`) [worker R10-5].
    - Its pair weight is independently checked here (§3.4).
- **Part (b) prescription "dD-M"** (stated, not derived from the axioms):
  - **Matter.** A real scalar with R9-9's L or G band. The lattice derivative has symbol i·s(k), s odd, s² = u.
  - **Coupling.** Minimal metric coupling √g g^{μν}D_μφD_νφ, with g = δ + κh and κ² = 32πG = 4κ_lat. This is R9-9's member M extended to all ten components.
  - **Vertex.** V^{μν} = p̂^μp̂′^ν + p̂^νp̂′^μ − δ^{μν}(p̂·p̂′ + m²).
  - **Seagull.** Ultralocal in h.
  - **Graviton.** R9-9's box symbol d(q) (C1 = 1.0, C2 = 2.5) with a de Donder-type propagator P_{μνρσ}/(q₀² + |d(q)|² + λ²). Here λ is an IR regulator, extrapolated to 0.
  - **Ward identity.** It is exact only where every line is in its box. Off the box p̂ − p̂′ ≠ d(q), so the linearized-diffeomorphism Ward identity of this vertex is **not** exact. This is R9-9's open item (`vR9-9:5`) in another guise.
- **Subtractions named before the runs (round-11 rule).**
  - (a) Large-t / edge-onset statements: nothing is subtracted. F_A has no box part because A ≡ 0 on the box exactly. The numerical check sets A to exactly 0 there, which is the identity itself, not a channel subtraction.
  - (b) The graviton-mass IR regulator: no channel is subtracted. J(λ) is extrapolated in λ² from λ = 0.2 and 0.1, and the N = 64/96 convergence is shown.
  - The mass-scaling clause "J ∝ m²" is an exact identity (Lemma M), not a fit.
- **Excluded (outside realizations):**
  - class (D) Dirac with nonzero a- and mixing-moments (Theorem D);
  - non-Peierls or transverse-Pauli vertices; INV vertices;
  - interacting matter; two loops;
  - k_z- or q-dependent TT vertices;
  - non-separable bands; non-axis q;
  - massless species in the loops (the photon's own contribution to C_T included);
  - for (b): fermion matter, other gauges (§4.4), and a Ward-exact pair stress.

## 2. Prior art (each counted once)

- **O3 Theorem 1(a)** (CWC). Exact vanishing of the vacuum energy on an open mass interval forces equality of the aggregate signed DOS measures (`C5_O3_report.md:50-64`; `C5_O3_referee.md:5,17`; `TESTS:2400`). Theorem N\* below is the same Laplace-uniqueness mechanism applied to the A-weighted LV measures.
- **R8-2 Theorem E** (CWC): A = Hess(ε²/2) − I with zone mean −I (`TESTS:3556`).
- **R9-9 Theorem T** (CWC; `vR9-9:7`) and **Lemma N**, valid only with vertex richness (`vR9-9:14`). The richness caveat matters: Lemma N says no band nulls Ξ for *all* vertices; Theorem N\* needs no richness.
- **R10-1** (CWC, SUGGESTED; `vR10-1:7,11`):
  - Theorem T′ (`C5_R10-1_report.md:137-158`);
  - Theorem P (`:206-230`), corrected to 4 complex scalars per 8 components with matched masses;
  - Lemma N(m) for one fixed shape (`:197-201`). The referee: "does not exclude isolated mass zeros or simultaneous cancellation for finitely many masses" (`vR10-1:11`).
- **R10-5** [worker, unrefereed]:
  - Theorem PT. Minimal pairing cancels the TT speed and mass; coupling through Q does not (`C5_R10-5_report.md:191-235`).
  - The electron's partner loops enlarge Δ (`:237-263`).
  - Not duplicated here. Its fermion pair weight is rechecked (§3.4).
- **R8-5** (CWC). The Feynman-gauge, photon-mass-regulated electron self-energy method (`scripts/C5/R8-5/r85_box_qed.py:62-109`). §4 follows its structure for gravity, but extracts on-shell (the matter is massive).
- **Nielsen–Ninomiya** (RECALLED). Not used. Theorem S excludes doublers by hypothesis instead.
- **Repo search.** grep over TESTS, SUMMARY and agents for "supertrace", "pairing", "necessary", "graviton loop", "matter self-energy" and "dressed matter speed".
  - The matter-from-graviton-loop shift appears only as an open item (`vR9-9:23`; `C5_R9-9_report.md:50,206`; `C5_S11_synthesis.md:93`).
  - Necessity of pairing for LV coefficients appears only as R11-1's registration and R10-1's photon-only Lemma N(m).

## 3. Part (a): necessity

### 3.1 Theorem N\* (measure pairing across statistics, observable by observable). Proved

**Setting.**
- Take a finite content in 𝒞_A with m_s² = a_sM + c_s.
- For O ∈ {γ, T_2g, E_g}, write C_O(M) = Σ_s σ_s⟨w_s^O(k_⊥)A_s(k_∥)/ε_s⁵⟩:
  - σ_b = +1 for bosons and σ_f = −1 for fermions;
  - w_s^O ≥ 0 is the species' weight (charges and normalizations included), independent of k_∥.
- Let μ_s^O be the pushforward of w_s^O A_s dk under k ↦ Σ_j u_s(k_j). This is a finite signed measure on [0, 3 max u_s].
- Write T_c for the shift by c and D_a for the dilation λ ↦ λ/a.

**Claim.** If C_O(M) = 0 for every M in an open interval, then

  **Σ_s σ_s a_s^{−5/2} D_{a_s}T_{c_s}μ_s^O = 0 as a signed measure, i.e. Σ_s σ_s a_s^{−5/2}e^{−τc_s/a_s}Φ_s^O(τ/a_s) ≡ 0 for τ > 0,**

where Φ_s^O(t) = ∫e^{−tλ}dμ_s^O(λ). In particular, at τ = 0:

  **Σ_b a_b^{−5/2}⟨w_b^O⟩ = Σ_f a_f^{−5/2}⟨w_f^O⟩.**

Every term is ≥ 0, so a nonzero coefficient cannot vanish on a mass interval unless **both statistics are present** with matched weighted totals.
- Photon: Σ_b q_b²a_b^{−5/2}⟨u_b′²⟩/32 = Σ_f q_f²a_f^{−5/2}⟨v_f′²⟩/8.
- T_2g: Σ_b a_b^{−5/2}⟨|V_b|²⟩/16 = Σ_f a_f^{−5/2}⟨S_f²⟩².

**Proof.**
1. C_O is real-analytic in M on the connected domain {a_sM + c_s > −min u_s for all s} ⊃ (M₀, ∞). So vanishing on an interval gives vanishing on (M₀, ∞).
2. ε^{−5} = Γ(5/2)^{−1}∫₀^∞t^{3/2}e^{−tε²}dt. Substituting τ = a_st gives C_O(M) = Γ(5/2)^{−1}∫₀^∞dτ τ^{3/2}e^{−τM}H(τ), with H(τ) = Σ_sσ_s a_s^{−5/2}e^{−τc_s/a_s}Φ_s^O(τ/a_s), which is continuous and exponentially bounded.
3. By Lerch uniqueness, H ≡ 0. Since Φ_s^O are Laplace transforms, the measure identity follows.
4. **The value at τ = 0.** Φ_s^O(0) = ⟨w_s^O(k_⊥)A_s(k_∥)⟩. At fixed k_⊥, ∫A_s dk_∥ = ∫(u_s″/2 − 1)dk_∥ = −2π by periodicity (Theorem E's mean, `TESTS:3556`). Since w is independent of k_∥, Φ_s^O(0) = −⟨w_s^O⟩ ≤ 0, with equality only for a vanishing vertex. With σ_s the claim follows. ∎

**Remarks.**
- (i) This needs no vertex richness (cf. `vR9-9:14`): the vertices are fixed.
- (ii) "Observable by observable": the weights for γ (u′(k_y)², Ward-forced, charged species only) and for T (|V|², all species) differ. So the two identities are independent conditions.
- (iii) If the masses are any analytic m_s(m) with m_s ~ y_s m as m → ∞, the large-mass expansion of the vanishing function gives Σσ_s y_s^{−5}Φ_s(0) = 0 at leading order. The cross-statistics corollary still holds (proved, sketch).
- (iv) Isolated mass zeros remain possible (`vR10-1:11`).

### 3.2 Theorem S (species-level pairing in a subclass). Proved

**Subclass 𝒞_A^S:**
- (S1) one boson band u and TT vertex |V_B|² = 4w(k_x)w(k_y), with w ≥ 0 even, shared by all bosons; one Clifford-flat curve c = (S, W), v = |c|², shared by all fermions;
- (S2) u and v are even and strictly increasing on (0, π), so there are no doublers;
- (S3) a common mass for all species (a_s = 1, c_s = 0), or more generally a common mass spectrum (see the last point below);
- (S4) the charge/multiplicity ratio c_γ := (Σ_f q_f²/8)/(Σ_b q_b²/32) = 1. This is R10-1's unit with equal charges: 4 complex scalars per 8 components.

**Claim.** In 𝒞_A^S, C_γ ≡ 0 and C_{T_2g} ≡ 0 on a mass interval ⇔ the minimal pairing of R10-1 and R10-5:
- u = v;
- the two boxes coincide;
- w = λS² with N_B^{cplx}λ² = 4N_F, so λ = 1 for R10-1's unit.

The "⇐" direction is Theorem P plus Theorem PT [worker R10-5].

**Proof of "⇒".**
1. **Equal boxes.** By Theorem N\* with common mass, μ_u^γ = μ_v^γ (with c_γ = 1). μ^γ = ν_A ∗ ν_V ∗ ν_1 is a convolution of the 1D pushforwards of A dk, u′² dk and dk.
   - Box-exactness makes A ≡ 0 for |k| < b, so inf supp ν_A = b². Also inf supp ν_V = inf supp ν_1 = 0.
   - By Titchmarsh's convolution theorem, inf supp μ_u = b_u² and inf supp μ_v = b_v². Hence b_u = b_v =: b.
2. **Window induction.** For a monotone even band, all three 1D measures are fixed by g(λ) := u′(k(λ))². In particular:
   - dν_1 = dλ/(π√g) and dν_V = √g dλ/π;
   - dν_A = (g′/4 − 1)dλ/(π√g), since g′ = 2u″.

   Suppose g_u = g_v on [0, L) (true for L = b², where both equal 4λ). Write δ = ν_A^u − ν_A^v and η = ρ^u − ρ^v, with ρ = ν_V ∗ ν_1. Both δ and η are supported in [L, ∞).
   - The identity gives δ ∗ ρ^u = −ν_A^v ∗ η, and the right side is supported in [L + b², ∞).
   - Titchmarsh applied to the truncations (δ|_{[L, L+b²)}, ρ^u|_{[0, b²)}, with inf supp ρ^u = 0) gives δ = 0 on [L, L + b²).
   - The ODE g′ = 4 + 4π a(λ)√g, where a is the density of ν_A, is Lipschitz where g > 0. Same data and the same initial value at L give g_u = g_v on [L, L + b²).
   - Iterating up to λ_max gives g_u ≡ g_v, hence u = v (k(λ) = ∫dλ/√g).
3. **The TT condition with u = v.** It reads N_B·¼F_A(t)F_w(t)² = N_F F_A(t)F_{S²}(t)².
   - F_A is analytic with F_A(0) = −1, so F_w = 2√(N_F/N_B)·F_{S²} for all t.
   - Pushforwards under a monotone even map determine even functions, so w = λS².
   - E_g gives the same λ, since its weight (w_x − w_y)² brings in F_{w²}F_1 − F_w².
4. **Mass spectra.** If instead u = v is assumed, the photon identity forces Σ_b q_b²e^{−tc_b} ≡ 4Σ_f q_f²e^{−tc_f}: the charge-weighted mass spectra must pair. Conversely, matched spectra divide out (the Laplace factor is > 0 for real t) and reduce to the common-mass case. ∎

**Not proved (suggested).**
- **c_γ ≠ 1.** The window recursion then determines v uniquely from u and c_γ. The closure conditions are g_v → 0 at some λ_max^v, ∫dλ/√g_v = π, and the identity on [λ_max^v, 3λ_max] with no remaining freedom. This is an overdetermined problem, and I expect no solution, but it is not proved.
- **Non-monotone bands.** These include the literal L edge, with its doubler at k = π. There g is not single-valued.
- **Unmatched mass spectra with u ≠ v.**

### 3.3 Pairing the photon does not pair the graviton. Checked

Take bosons on the fermion's own curve v. The photon coefficient then cancels identically. Give the bosons the minimal-metric TT vertex w = v (R9-9's M) instead of w = S². Then C_{T_2g}·16π² = −2.1 to −2.9 (Wilson curve) and −2.0 to −3.3 (box b₁ = 0.8), for m = 1, 0.3 and 0.05 (`r111_obs_by_obs.out:1-6`). The pairing has to be imposed per observable: on the curve for γ, and on the vertex for T.

### 3.4 Checks (`r111_necessity.out`, `r111_check_PT_weight.out`)

- **Zone means.** ⟨A⟩ = −1 for L, G, NN and the three fermion curves, to 3e-8. L's departure, 2.5e-8, is the finite-difference u″.
- **Total-mass signs.** Every boson total is < 0 and every fermion total is > 0, for both observables (`:3-11`).
- **Laplace form against the direct 3D mean.** Agreement to 1.2e-5 (G) and 3.4e-6 (L) at m = 0.3, N = 96 (`:14-15`).
- **Paired content** (4 complex scalars on v with TT vertex S², plus 1 fermion): C_γ = C_T = 0 identically on m ∈ [0.05, 1.5] (`:18-19`). This checks the normalizations 4 × 1/32 = 1/8 and 8 × 4/32 = 1.
- **Unpaired content with the t = 0 totals matched by a real-valued multiplicity.** C_γ and C_T stay strictly positive over the whole range, with no sign change, for three content pairs (`:20-25`). Matching totals alone does not make the coefficients vanish.
- **Edge onset** (Titchmarsh step). −(1/t)ln|F_A| decreases toward u(face) = b²: G reaches 4.94 at t = 20 against b² = 4. The approach is slow because the plateaus vanish to infinite order at the face. L instead decays toward 0, consistent with its doubler, where u(π) = 0 (`:28-31`). Consistent only, not a proof; the proof is the support statement.
- **R10-5's fermion TT pair weight.** t(k, k′) from explicit 8×8 Clifford matrices matches R10-5's closed form to 9.5e-16 at 200 random points (`r111_check_PT_weight.out:2`). The remaining α step of Theorem PT is R10-5's numerics (`r105_tt_paired.out`), which I did not redo.

## 4. Part (b): the dressed matter speed under graviton loops (prescription dD-M)

### 4.1 Method (checked)

- **Self-energy.** Π(p₀, p) = −(κ²/4)∫_q∫dr/2π V·P·V/((q₀² + a²)(r² + b²)), with:
  - r = p₀ − q₀ the internal matter frequency;
  - a² = |d(q)|² + λ²;
  - b² = ε(p − q)².
- **The r-integrals** are closed rational functions of p₀ (sympy residues). Their only singular factor is the threshold [(a + b)² + p₀²]^k (`r111_q0int.out:1-8`). They agree with quadrature to 3e-11, and the continuation p₀ = iE reproduces the old-fashioned-perturbation-theory form exactly (`:9-10`).
- **Dispersion.** First order, on shell: ω² = ε²(p) + Π(iE_p, p). So c_m² − 1 = dΠ_on/dp² at p = 0, by exact grid shifts p_x = n·2π/N (n = 1, 2, 4) with two Richardson steps.
- **Normalization.** J := dΠ_on/dp² at κ² = 1, so c_m² − 1 = 4κ_lat J. R9-9 has c_T² − 1 = 2κ_lat Ξ. Hence **c_m − c_T = κ_lat(2J − Ξ)**, with κ_lat = 8π(ℓ_P/a)².
- **Units.** The registered unit "κ_lat²/(16π²a²)" (`TESTS:4105`) looks like a typo. The split is first order in κ_lat, which is already dimensionless. I report κ_lat/(16π²).

### 4.2 Lemma M (structure). Proved; checked

- **The identity.** For V = p̂p̂′ᵀ + p̂′p̂ᵀ − δ(p̂·p̂′ + m²) and 4D de Donder P,

  V·P·V = 2p̂²p̂′² − 4m²(p̂·p̂′ + m²), for arbitrary vectors.

  Checked to 9e-15 on random complex vectors (`r111_vpv_identity.out`).
- **On shell.** p̂² = −E_p² + Σs(p_j)² = −m² exactly, for every p, because s² = u. Then V·P·V = −2m²[(p̂ + p̂′)² + 3m²] for any internal vector p̂′(k). Checked to 5e-12.
- **The seagull.** It is ultralocal in h, so its tadpole is P_{abcd}·∫_q D times a covariant contraction with p̂p̂: c₁p̂·p̂ + c₂m², which is p-independent on shell.
- **Hence** c_m² − 1 = κ²m²·(an edge integral), and J = m²J₂(m). Checked: J/m² = −5.51e-3, −5.68e-3, −5.70e-3, −5.68e-3 (G) and −6.89e-3, −7.26e-3, −7.31e-3, −7.30e-3 (L) at m = 1, 0.3, 0.1, 0.05 (`r111_split_numbers.out:2-9`).
- **Reading.** The m⁰ term of V·P·V is p̂²p̂′², which is proportional to the external equation of motion and so drops out on shell. The suppression rests on de Donder plus a vertex of covariant tensor form in the *external* leg. The internal momentum functions may be arbitrary.

### 4.3 Numbers (checked; λ → 0 extrapolated, N = 96; Ξ from R9-9, `scripts/C5/R9-9/r99_tt_selfenergy.out:28-29,40-41,52-53,64-65`)

- **Convergence.** N = 64 against N = 96 at λ = 0.1 differs by ≤ 3e-4 relative. The λ dependence is ∝ λ² (successive differences fall by a factor of 3.9). Π_on has no imaginary part below threshold (`r111_matter_speed.out`).

| edge, m | pol. | 2J | Ξ (R9-9, M) | 16π²(2J − Ξ) | c_m − c_T at a = ℓ_P |
|---|---|---|---|---|---|
| G, 1.0 | T_2g | −1.102e-2 | −9.60e-4 | **−1.589** | −0.253 |
| G, 1.0 | E_g | −1.102e-2 | −5.29e-4 | **−1.657** | −0.264 |
| G, 0.3 | T_2g | −1.023e-3 | −1.112e-3 | **+0.0141** | +2.3e-3 |
| G, 0.3 | E_g | −1.023e-3 | −6.28e-4 | **−0.0623** | −9.9e-3 |
| L, 1.0 | T_2g | −1.377e-2 | +2.41e-3 | **−2.555** | −0.407 |
| L, 1.0 | E_g | −1.377e-2 | +2.32e-3 | **−2.541** | −0.405 |
| L, 0.3 | T_2g | −1.307e-3 | +5.28e-3 | **−1.040** | −0.165 |
| L, 0.3 | E_g | −1.307e-3 | +5.52e-3 | **−1.078** | −0.172 |

(`r111_split_numbers.out:11-19`.)

- **Light external matter** (m·a → 0; physical particles): J = m²J₂ → 0, so c_m − c_T → −κ_lat Ξ.
  - G: +0.176 (T_2g) and +0.099 (E_g) in κ_lat/16π² units; at a = ℓ_P, +2.8e-2 and +1.6e-2.
  - L: −0.83 and −0.87; at a = ℓ_P, −0.13 and −0.14.
  - This uses R9-9's m = 0.3 Ξ for the loop species, as representative.
  - These are about 1e13–1e14 times the GW170817 band (RECALLED via R7-4).
- **The matter side for a proton** at a = ℓ_P (m·a ≈ 7.7e-20): δc_m ≈ −2e-39 (`r111_split_numbers.out:26-27`).
- **Reading on `AX:189-190`.** Every Planck-unit size uses a = ℓ_P, which the axioms leave open. The graviton-side split scales as (ℓ_P/a)², so it is harmless only for a ≳ 1e7 ℓ_P (R9-9's estimate).

### 4.4 What (b) does and does not establish

- **Computed.** c_m − c_T ≠ 0 on both edges, at both masses, for both polarizations, in dD-M.
- **Sign.** Not fixed on the gapped edge. G/T_2g changes sign between m = 0.3 and 1 (an isolated mass zero), while E_g at the same masses does not vanish. The registered expectation "sign-definite on the gapped edge" is **not** borne out for the split. The matter side alone, J < 0, is negative in every run.
- **Polarization-independent observation** (a reading on refereed numbers). Ξ_T2g ≠ Ξ_Eg in every R9-9 row. So c_T(T_2g) ≠ c_T(E_g) at one loop, and matter shares at most one TT cone whatever its own shift. A graviton–matter split therefore exists for at least one polarization without computing the matter side, given R9-9's class.
- **Not established:**
  - **Gauge independence.** The vertex's Ward identity fails off the box.
  - **A pure-gauge diagnostic.** I first added a ζ·(dd δ + perms)/D² propagator term (code kept, `R111_ZETA=1`) and found a large LV (−6.7e-2 at N = 32). That diagnostic is invalid without the seagull's own gauge part, which a second-order Ward identity would fix, so it is withdrawn and not used.
  - **Other prescriptions.** Coulomb-type gauges or non-covariant vertex tensor forms are not covered.
  - **Fermion matter.** The electron's graviton-loop shift is not computed.
  - **The Ward completion of the pair-creating stress** that enters Ξ (`vR9-9:5`).
- **Reading.** If an exactly Ward-invariant lattice coupling existed, de Donder would be as good a gauge as any and Lemma M would make the matter-side shift O(κm²) generally. With the present inexact Ward identity this is a conjecture (suggested).

## 5. (c) The one-loop count, with and without pairing

| coefficient (one loop, 𝒞_A-type content) | without pairing | with minimal pairing (u = v, w = S², matched masses) | status |
|---|---|---|---|
| photon speed | 1 condition, no interval zero (Theorem N\*) | 0 (Theorem P) | ref (`vR10-1:7`) + this probe |
| graviton TT speed, T_2g and E_g | 2 conditions (Theorem N\*; birefringent) | 0 (Theorem PT) | [worker R10-5] |
| graviton TT mass | per-polarization seagull choice (narrow FAIL, `vR9-9:16`) | 0 (Theorem PT) | [worker R10-5] |
| matter–graviton split | ≈ −κ_lat Ξ for light matter, the same conditions as the TT speeds; no new one at O(m⁰) (§4) | O(κ_lat m²) J₂ ≈ 1e-39, harmless (scalar matter, dD-M) | this probe, prescription-scoped |
| electron–photon split | 1 (Δ ≈ −11 to −71) | 1 (Δ ≈ −10.7 to −18.0; partners enlarge it) | ref `vR10-1:9`; [worker R10-5] |
| mass-split residuals of broken pairing | n/a | photon 0.335 m_s²; vacuum 2⟨1/E⟩Δm²; TT not computed | ref / [worker] |

**Changes from R10-1's referee.**
- "Six tunings" is bookkeeping, not derived (`vR10-1:15`). I keep it that way and do not give a total.
- The pairing unit is 4 complex scalars per 8 components, with matched masses (`vR10-1:7`). Theorem S derives exactly this ratio as the c_γ = 1 case.
- New here: without pairing, no coefficient in 𝒞_A can vanish on a mass interval (Theorem N\*). With pairing, the matter–graviton split falls to O(κ m²) (dD-M).
- The electron–photon split is the one coefficient that pairing does not remove at one loop.

## 6. Against the FIXED readings (`TESTS:4107-4120`)

**(a) Worker reading: DERIVED** (needs the referee).
- **Proved:**
  - in 𝒞_A, vanishing of any one of {photon, T_2g, E_g} on a mass interval forces cancellation of the aggregate, mass-rescaled, A-weighted pushforward measures of bosons against fermions for that observable (Theorem N\*);
  - neither statistics alone suffices (signed totals);
  - in 𝒞_A^S with R10-1's charge ratio, it forces the species-level minimal pairing (Theorem S).
- **REFUTED is impossible in 𝒞_A**, since an "unpaired" interval cancellation would contradict Theorem N\*.
- **Inputs.** The fermion TT moment is [worker R10-5]. If PT fails refereeing, the TT half of Theorem N\* stands for bosons only, and the cross-statistics conclusion for T is then unsupported.
- **Scope.**
  - The criterion is vanishing on an interval.
  - A tuned edge can null one coefficient at m → 0 for all light species of one statistics. This is R10-1's own "physically weak" reading of Lemma N(m) (`C5_R10-1_report.md:201`).
  - Beyond 𝒞_A it is SUGGESTED, as expected: class (D) a- and mixing-moments have no fixed sign and no bosonic counterpart.

**(b) Worker reading: SPLIT-PRESENT, in prescription dD-M only.**
- **Computed:** c_m − c_T ≠ 0 for both edges and masses with the numbers of §4.3, including R9-9's Ξ.
- **Not class-wide.** The off-box Ward identity is inexact and gauge independence is not established. Any class-wide use needs the referee.
- **Against the expectation.** Unsuppressed at a = ℓ_P: yes. Sign-definite on the gapped edge: no.
- **The structural new fact.** For physical (light) matter, the split is set by the graviton side, because the matter side is O(κ m²).

## 7. Prices (named, not adopted)

- **P42** (edge supertrace), sharpened by Theorem S. If the observable criterion is interval cancellation, pairing is not optional in 𝒞_A. The price is then:
  - a common Clifford-flat curve, the same box and no doublers;
  - matched charge-weighted mass spectra;
  - the pairing TT vertex w = S²;
  - all against Qubit `AX:47` (bosons plus 8-component fermions per cell), with dynamics downstream (`AX:116-130`).
- **The alternative** is one tuned edge condition per observable (and per polarization) at m → 0.
- **dD-M** (part (b)): a de Donder-type box graviton propagator and the lattice minimal metric coupling. These are a law choice, not derived, and the source/action gate stays open (`AX:187`).

## 8. Strong-word check

- **"Proved":**
  - Theorem N\* (Lerch plus periodicity);
  - Theorem S (Titchmarsh plus ODE uniqueness, under S1–S4);
  - Lemma M (algebra);
  - the seagull covariance (P is a constant tensor).

  Theorem N\*'s Remark (iii) is a sketch.
- **"Exact":** used only for algebraic identities (Lemma M; paired content giving 0 with identical integrands).
- **"Checked":** every number, with N, λ and m scans in the `.out` files.
- **"Necessary":** necessary for interval vanishing in 𝒞_A, and nothing more.
- **Not claimed:**
  - gauge independence of dD-M;
  - fermion matter speed;
  - two loops;
  - a proof for c_γ ≠ 1 or for non-monotone bands;
  - anything about class (D).

## 9. For the referee

1. **Theorem N\*:** analyticity domain, Lerch, the τ → 0 limit, and whether "w independent of k_∥" holds for every vertex used (Peierls: yes; 𝒱: by definition; vielbein: yes).
2. **Theorem S:**
   - Titchmarsh on truncations;
   - the ODE g′ = 2u″, i.e. dν_A = (g′/4 − 1)dλ/(π√g);
   - the use of box-exactness for the b² gap;
   - whether c_γ = 1 can be removed.
3. **Lemma M and the on-shell continuation:** the threshold-only denominators (`r111_q0int.out`), and p̂² = −m² for all p because s² = u.
4. **Whether dD-M's number can be called SPLIT-PRESENT** without a Ward-exact coupling, and whether the birefringence argument (§4.4) alone carries a polarization-level split.
5. **R10-5's PT α step** (not redone here).

## 10. Files

All in `S/scripts/`:
- `r111_necessity`, `r111_obs_by_obs`, `r111_check_PT_weight`, `r111_q0int` (with `.pkl` cache), `r111_matter_speed` (`.out` and `_light.out`), `r111_vpv_identity`, `r111_split_numbers`: each as `.py` and `.out`;
- copies `r99_profiles_copy.py`, `r101_pairing_copy.py`, `r85_box_qed_copy.py`.

No downloads.
